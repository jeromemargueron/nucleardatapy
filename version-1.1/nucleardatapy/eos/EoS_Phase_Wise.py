import numpy as np
from pathlib import Path
from scipy.interpolate import interp1d, CubicSpline, PchipInterpolator
from copy import deepcopy
import os
import nucleardatapy as nuda
import pandas as pd


#with open(nuda.param.path_eos+"/dict_boundaries.txt", "r") as f:
    #available_models = eval(f.read(), {"np": np})

#print(available_models)

class setupCSEoS:
    """
    Construct an EoS from specified hadronic layers and inner-core phases.
    
    input : eos_object : optional, dictionary
           An dictionary with mentoning the information for each layers of the Neutron Star, 
           Neutron star is considered as atomsphere+ outer_crust +inner_crust + outer_core +inner_core
           
           In the absence of any information the code results BPS-PNM EoS for dense matter
            Fixed  layers: atmosphere,outer_crust, inner_crust, outer_core
            eos_object= {"atmosphere":"model name","outer_crust":"model name",
                                "inner_crust":"model name", "outer_core":"model name"} 
            In the absence of a inner-core, the model assumes the Neutron star is completely nucleonic : i.e., the maximum density of the outer core is the end of NS EoS
                Inner-core phases: A dictionary within the eos_object with anynumber of phases, specified using keys such as: "1", 1, "phase1", "phase2", ...

            Each inner-core phase requires:type  : , e.g. "YM" or "QM" (only acceptale)
                model : model name (such as "1974-BPS-YM")
                
            If model matches a list of  functions, that function will be considered: 
            Currently, only applicable to the QM phase
             Availbel functions : QM_linear model, The linear constant -speed of sound model from  http://dx.doi.org/10.1103/PhysRevD.88.083013
             
             To consider the inner-core phases :
             eos_object= {"atmosphere":"model name","outer_crust":"model name",
                            "inner_crust":"model name", "outer_core":"model name",
                            "inner_core":{"1 or phase1" or 1 : {"type":"YM" or "QM","model":"model or function name","parameters":{in case of function}}}}
                            
    input : "base_dir" : optional, path to the folders/ files with the EoS data files.
    input : "PT_Method_core ": Method for construction of phase transition and parameters. Default : Maxwell
                            : Avilable methods : {"Maxwell","MIM"}
                            : For MIM, use  PT_Method_core= {"method":"MIM","parameters":{"x_deltaP":0.001}}
                            
    output :
         Returns the class object, which can  be avail to obtain different informations:
           object.boundaries gives the bounadry of each layer
           object.eps_tot : energy density
           object.pre_tot : pressure
           object.den_tot : number density
           object.cs2_tot : squared speed of sound
           
           ## The phase transition and boundaries can also be obtained.
                            
    
         

    Units:
        nuclear_unit=True:
            den : fm^-3
            pre : MeV/fm^3
            eps : MeV/fm^3

        nuclear_unit=False:
            den : cm^-3
            pre : dyn/cm^2
            eps : erg/cm^3
    """

    def __init__(self,eos_object=None,PT_Method_core=None,full_outputs=False):

        
        self.base_dir = Path(nuda.param.path_eos)       
        self.full_outputs = full_outputs        
        self.default_eos = {
            "atmosphere": "1949-FMT",
            "outer_crust": "1971-BPS",
            "inner_crust": "1971-BPS",
            "outer_core": "1971-BPS-PNM",
            "inner_core": {},
        }

        self.eos_layers = eos_object
        self.init_self()

        
        self.PT_Method= PT_Method_core
        if PT_Method_core is None:
            self.PT_Method = {"method": "Maxwell"}

    @staticmethod
    def _phase_number(phase_name):
        """
        Accept phase keys such as:
            "phase1", "Phase1", "1", 1
        """

        name = str(phase_name).strip().lower()

        if name.startswith("phase"):
            number = name[len("phase"):].strip()
        else:
            number = name

        if not number.isdigit() or int(number) < 1:
            raise ValueError(f"Invalid phase name '{phase_name}' Use 'phase1', '1', or 1, for example.")

        return int(number)

    # =========================================================
    # Set and validate the EoS configuration
    # =========================================================

    def set_eos(self):
        """
        update the default eos with the one from user

        Inner-core phases use a dictionary of phase definitions.
        """

        eos_input = self.eos_layers

        self.eos_layers = deepcopy(self.default_eos)
        
       

        if eos_input is not None:

            if not isinstance(eos_input, dict):
                raise TypeError("eos_object must be a dictionary or None.")
            self.eos_layers.update(eos_input)

        phases = self.eos_layers.get("inner_core", {})  

        if phases == "" or phases == " ":
            phases = {}

        if not isinstance(phases, dict):
            raise TypeError("'inner_core' must be a dictionary of phases.")

        self.eos_layers["inner_core"] = phases

        if not isinstance(phases, dict):
            raise TypeError("'inner_core' must be a dictionary of phases.")

        
        phase_numbers = set()

        for phase_name, phase_info in phases.items():

            number = self._phase_number(phase_name)

            if number in phase_numbers:
                raise ValueError(f"Duplicate inner-core phase number {number}. ")

            phase_numbers.add(number)

            if not isinstance(phase_info, dict):
                raise TypeError(f"Definition for '{phase_name}' must be a dictionary.")

            if "type" not in phase_info:
                raise KeyError(f"Missing 'type' for '{phase_name}'.")

            if "model" not in phase_info:
                raise KeyError(f"Missing 'model' for '{phase_name}'.")

            if not isinstance(phase_info["type"], str):
                raise TypeError(f"'type' for '{phase_name}' must be a string.")

            if not isinstance(phase_info["model"], str):
                raise TypeError(f"'model' for '{phase_name}' must be a string.")

            # Validate parameters for function-based models.
            model_name = phase_info["model"]

            if model_name.strip().lower() in self.QMeos_functions:
                parameters = phase_info.get("parameters", {})
                if not isinstance(parameters, dict):
                    raise TypeError(f"'parameters' for '{phase_name}' must be a dictionary.")

        self.identify_inner_core_phases()
        return self

    # =========================================================
    # Identify ordinary hadronic models
    # =========================================================
    
    
        
    
    
    def identify_inner_core_phases(self):
        """
        Identify each inner-core phase.
        If model matches a  function:
            source = "function"
        else:
            source = "file"
        """

        phases = self.eos_layers.get("inner_core", {})

        

        sorted_phases = sorted(
            phases.items(),
            key=lambda item: self._phase_number(item[0]))

        for phase_name, phase_info in sorted_phases:

            phase_type = phase_info["type"].strip().upper()
            model_name = phase_info["model"].strip()
            phase_data = {**phase_info,"type": phase_type,"phase_number": self._phase_number(phase_name)}

            
            if model_name.strip().lower() in self.QMeos_functions:

                phase_data["source"] = "function"
                phase_data["function"] = (self.QMeos_functions[model_name.strip().lower()])

            
            else:
                phase_data["source"] = "file"
                phase_dir = (self.base_dir / "inner_core" / phase_type)
                if not phase_dir.is_dir():
                    raise FileNotFoundError(f"Directory not found: {phase_dir}")

                matching_files = sorted(
                    filename
                    for filename in phase_dir.iterdir()
                    if filename.is_file()
                    and filename.stem.startswith(model_name)
                )

                if not matching_files:
                    raise FileNotFoundError(f"No file found for model '{model_name}' in {phase_dir}")

                if len(matching_files) > 1:
                    raise ValueError(f"Multiple files match '{model_name}' in {phase_dir}: {matching_files}")

                phase_data["filename"] = matching_files[0].name
                phase_data["filepath"] = matching_files[0]
                
                

            self.inner_core_phases[phase_name] = phase_data

        return self

    # =========================================================
    # Find selected files
    # =========================================================

    
    
    def _load_eos_file(self, filepath,layer=None,model_name=None):
        """
        Load an EoS file with columns:

            rho  : mass density [in g/cm^3 or kg/m^3 or MeV/fm^3]
            pre : pressure [in dyn/cm^2 or Pascal or MeV/fm^{3}]
            den : baryon number density [in cm^-3 or m^{-3} or fm^{-3}]

        Convert to nuclear units if nuclear_unit=True.
        
        """
        df=pd.read_csv(filepath,sep=r'\s+',comment='#')
        
        pre_col = next(c for c in ("pre_cgs", "pre_nuc", "pre_SI") if c in df.columns)
        den_col = next(c for c in ("den_cgs", "den_nuc", "den_SI") if c in df.columns)
        rho_col = next(c for c in ("rho_cgs", "rho_nuc", "rho_SI") if c in df.columns)
        
        
        if None in (pre_col, den_col, rho_col):
            raise ValueError( f"Could not identify the required EoS columns in {filepath}, Available columns: {df.columns.tolist()}"  )
        
        pre = df[pre_col].to_numpy() 
        den = df[den_col].to_numpy() 
        rho = df[rho_col].to_numpy()
        
        
        

   
       
        if self.nuclear_unit:
            pre = df[pre_col].to_numpy() * {"cgs": nuda.cst.cgsP2MeVfm3,"nuc": 1,"SI": 10.0*nuda.cst.cgsP2MeVfm3 }[pre_col.split("_")[-1]]
            den = df[den_col].to_numpy() * {"cgs": 1/nuda.cst.cm3_to_fm3, "nuc":1, "SI": 1e-6*1/nuda.cst.cm3_to_fm3}[den_col.split("_")[-1]]
            rho = df[rho_col].to_numpy() * {"cgs": nuda.cst.g_cm3toMeVfm3, "nuc":1, "SI": 1e-3*nuda.cst.g_cm3toMeVfm3}[rho_col.split("_")[-1]]
            eps= rho
        
        if not self.full_outputs: 
            
            df={"den": den.copy(),"pre": pre.copy(),"eps": eps.copy()}           
            
            return pd.DataFrame(df)
        else:            
            self.models[layer] = {"model": model_name,"filename": filepath}
            df["den"] = den.copy()
            df["pre"] = pre.copy()
            df["eps"] = eps.copy()
            df["rho"]= rho.copy()
            for key in ("den", "pre", "eps","rho"):
                setattr(self,f"initial_{key}_{layer}",df[key].to_numpy())
            self.boundaries_from_data[layer] = {key: [np.min(df[key].to_numpy()), np.max(df[key].to_numpy())] for key in ("den", "pre", "eps","rho")}

                
            return  df
            
            
    def _load_from_nuda_beta(self,layer,model):
        model_name= model.strip().upper()
        micro_models = nuda.matter.micro_esym_models()[0]
        eos_beta={}
        
        if model_name in micro_models:
            eos_beta=nuda.eos.setupAMBeq(model=model_name)
            if any(not hasattr(eos_beta, q) or getattr(eos_beta, q) is None or not np.all(np.isfinite(getattr(eos_beta, q))) for q in ['pre_tot','den','eps_tot']):
                raise ValueError(f"Invalid EoS quantities for model '{model}'.")
            
            df={"den":eos_beta.den,"pre":eos_beta.pre_tot,"eps":eos_beta.eps_tot}   #,"rho":eos_beta.eps_tot}
            if self.full_outputs:
                df={"den":eos_beta.den,"pre":eos_beta.pre_tot,"eps":eos_beta.eps_tot,"rho":eos_beta.eps_tot}            
                self.boundaries_from_data[layer] = {key: [np.min(df[key].copy()), np.max(df[key].copy())] for key in ("den", "pre", "eps","rho")}
            return pd.DataFrame(df)
            
        else:
            pheno_types = nuda.matter.pheno_esym_models()[0]  
            
            for model_type in pheno_types:
            
                available_pheno_models = nuda.pheno_esym_params(model=model_type)[0]
                
                if model_name in available_pheno_models:
                    eos_beta=nuda.eos.setupAMBeq(param=model_name,kind='pheno',model=model_type)                    
                    
                    if any(not hasattr(eos_beta, q) or getattr(eos_beta, q) is None or not np.all(np.isfinite(getattr(eos_beta, q))) for q in ['pre_tot','den','eps_tot']):
                        raise ValueError(f"Invalid EoS quantities for model '{model}'.")
                    
                    df={"den":eos_beta.den,"pre":eos_beta.pre_tot,"eps":eos_beta.eps_tot}
                    if self.full_outputs:
                        df["rho"]=eos_beta.eps_tot
                        self.boundaries_from_data[layer] = {key: [np.min(df[key].copy()), np.max(df[key].copy())] for key in ("den", "pre", "rho", "eps")}                    
                    return pd.DataFrame(df)
                else:
                    raise ValueError( f"Could not find outer_core model '{model}' in nucleardatapy.")
    
    def _load_layer(self, layer, model):
        """Load an EoS from a local file or nucleardatapy."""

        if not model:
            return None

        
        layer_dir = self.base_dir / layer

        if layer_dir.is_dir():
            matching_files =[]
            for filepath in layer_dir.iterdir():
                if filepath.is_file()   and filepath.stem.startswith(model)    and filepath.suffix == ".csv":
                    matching_files.append(filepath.name)
            
            
            if len(matching_files) > 1:
                raise ValueError(f"Multiple files found for '{model}' in {layer_dir}")
            
            if matching_files:
                filepath = layer_dir / matching_files[0]
                return self._load_eos_file( filepath=filepath, layer=layer, model_name=model )
        
        if layer == "outer_core":
            return self._load_from_nuda_beta(layer, model)

        
        raise FileNotFoundError(f"Model '{model}' was not found in '{layer_dir}'" )   
        
    
    
    
    def _load_layer_outer_core(self, layer):
        """Load an EoS from a model, a function, or both."""

        config = self.eos_layers[layer]
        if isinstance(config, str):
            config = {"model": config}

        model = config.get("model")
        #print(model)
        

        eos_data_file = None
        df = None

        
        if model:
            data = self._load_layer(layer, model)
            df = data.copy() if isinstance(data, pd.DataFrame) else pd.DataFrame(data)

            for key in ("den", "pre", "eps"):
                if key not in df.columns:
                    raise ValueError(f"Missing '{key}' in the loaded outer-core EoS.")

                values = df[key].to_numpy(copy=True)
                if not np.all(np.isfinite(values)):
                    raise ValueError(f"Non-finite values found in outer_core['{key}'].")

            if df.empty:
                raise ValueError("The loaded outer-core EoS is empty.")

            eos_data_file = { key: df[key].to_numpy(copy=True) for key in ("den", "pre", "eps") }

        
        function_name = config.get("function")
        
        if function_name:
            function_name = function_name.strip().lower()

            if function_name not in self.agnostic_models:
                raise ValueError(f"Unknown function '{function_name}' Available functions: {list(self.agnostic_models)}")

            parameters = dict(config.get("parameters") or {})

            # Prepare transition-point parameters when stitching
            if eos_data_file is not None and function_name == "random_speed_of_sound":

                den = eos_data_file["den"]
                eps = eos_data_file["eps"]
                pre = eos_data_file["pre"]

                den_tr = parameters.get("den_tr")

                if den_tr is None:
                    den_tr = den[-1]
                    eps_tr, pre_tr = eps[-1], pre[-1]
                else:
                    den_tr = min(den_tr, den[-1])

                    eps_tr = np.exp(PchipInterpolator(np.log(den), np.log(eps))(np.log(den_tr)))
                    pre_tr = np.exp(PchipInterpolator(np.log(den), np.log(pre))(np.log(den_tr)))
                    

                mu_tr = (eps_tr + pre_tr) / den_tr

                logpre_logeps = PchipInterpolator(np.log(eps), np.log(pre))
                cs2_tr = pre_tr / eps_tr* logpre_logeps.derivative()(np.log(eps_tr))

                parameters.update({
                    "den_tr": den_tr,
                    "eps_tr": eps_tr,
                    "pre_tr": pre_tr,
                    "mu_tr": mu_tr,
                    "cs2_tr": cs2_tr,
                })

            parameters["full_outputs"] = self.full_outputs

            eos_function_data = self._evaluate_eos_function( self.agnostic_models[function_name], **parameters)
            if eos_function_data is None:
                return None

            for key in ("den", "pre", "eps"):
                if key not in eos_function_data.columns:
                    raise ValueError(f"Function '{function_name}' did not return '{key}'.")

            # --------------------------------------------------
            # 3. Stitch only if an existing EoS is available
            # --------------------------------------------------
            if eos_data_file is not None:
                den_tr = parameters["den_tr"]
                mask = eos_data_file["den"] <= den_tr

                eos_data = {key: np.concatenate((eos_data_file[key][mask],eos_function_data[key].to_numpy() )) for key in ("den", "pre", "eps") }

                if self.full_outputs:
                    df = df.loc[df["den"] <= den_tr].copy()

                    for col in eos_function_data.columns:
                        if col not in df.columns:
                            df[col] = np.nan

                    for col in df.columns:
                        if col not in eos_function_data.columns:
                            eos_function_data[col] = np.nan

                    df = pd.concat([df, eos_function_data[df.columns]], ignore_index=True )

            else:
                # Function-only EoS
                eos_data = {key: eos_function_data[key].to_numpy(copy=True) for key in ("den", "pre", "eps") }

                if self.full_outputs:
                    df = eos_function_data.copy()

        
        elif eos_data_file is not None:
            eos_data = eos_data_file

        else:
            raise ValueError( f"Outer-core EoS requires either 'model' or 'function'.")

        if not self.full_outputs:
            return pd.DataFrame(eos_data)

        df["rho"] = df["eps"].to_numpy()
        return df

    
    
    
    def _evaluate_eos_function(self, function, **parameters):
        """
        Evaluate a  function-based EoS.        
        It works independently, when the parameters, does not depend upon the nucleoninc EoSs
        Helpful, if we plan to include MIT, vMIT, NJL , vNJL, vQCD models for QM
        or Any other agnostic approaches
        
        """
        eos_function_class = function(**parameters) ### This is wehere we calculate the EoS
        eos_data_from_function=eos_function_class.get_eos()
        if eos_data_from_function is None:
            return None
        

        pre = eos_function_class.pre        
        den = eos_function_class.den
        eps = eos_function_class.eps        
        #mub = (eps + pre) / den
        df= {"den": den.copy(),"pre": pre.copy(), "eps": eps.copy()}
        if not self.full_outputs:
            return pd.DataFrame(df)
        else:
            all_data = getattr(eos_function_class, "all_data", None)
            if all_data:
                return pd.DataFrame(all_data)
            else:
                return pd.DataFrame(df)
        
               
        
    def load_data(self):
        """
        Load all selected hadronic layers and inner-core phases.

        full_outputs=False:
            self.data[layer] contains a dictionary of EoS arrays.

        full_outputs=True:
            self.data[layer] contains a DataFrame with the original
            columns and standardized EoS columns.
        """

        self.set_eos()
        
        for layer in self.nucleonic_layers:
            if layer == "atmosphere":
                model = self.eos_layers.get(layer, "")
                if model:
                    df=self._load_layer(layer, model)
                    if df is not None : self.data[layer]=df 
                    
                    
            
            if layer == "outer_crust":
                model = self.eos_layers.get(layer, "")
                if model:
                    df=self._load_layer(layer, model)
                    if df is not None : self.data[layer]=df 
                    
                    
            if layer == "inner_crust":
                model = self.eos_layers.get(layer, "")
                if model:
                    df=self._load_layer(layer, model)
                    if df is not None : self.data[layer]=df 
                    
            if layer == "outer_core":
                df=self._load_layer_outer_core('outer_core')
                if df is not None : self.data[layer]=df 
                
        
        
        
        #self.identify_inner_core_phases()
        for phase_name, phase_info in self.inner_core_phases.items():

            if phase_info["source"] == "file":

                layer = f"inner_core_phase{phase_info['phase_number']}"

                model_name = phase_info.get("model")

                phase_data = self._load_eos_file( filepath=phase_info["filepath"], layer=layer,model_name=model_name)
                phase_info["data"] = phase_data
                if phase_data is not None : self.data[layer]=df 

            elif phase_info["source"] == "function":
                # Function-based phases are handled separately.
                continue

            else:
                raise ValueError(f"Unknown model for phase '{phase_name}'.")

        return self        
        
        
    def _match_eos_layers(self, layers):
        """
        Match EoS layers .
        """

        den_all, pre_all, eps_all = [], [], []

        previous_den = None
        previous_pre = None
        previous_eps = None

        # Reset layeral attributes for layers being reconstructed.
        if self.full_outputs :
            for layer, _ in layers:
                for quantity in ("den", "pre", "rho","eps"):
                    setattr(self, f"{quantity}_{layer}", None)

        for layer, values in layers:
        
            #print(layer,values)

            den = np.asarray(values["den"])
            pre = np.asarray(values["pre"])            
            eps = np.asarray(values["eps"])
            #mub = np.asarray(values["mub"])
            #rho = np.asarray(values["rho"])

            if len(den) == 0:
                continue

            # Sort in decreasing density order.
            order = np.argsort(den)[::-1]
            den, pre, eps = (arr[order] for arr in (den, pre, eps))

            # Apply matching conditions.
            if previous_den is not None:
                mask = ((den < previous_den) & (pre < previous_pre) & (eps < previous_eps))

                den, pre,  eps= ( arr[mask] for arr in (den, pre, eps))

            if len(den) == 0:
                continue

            # Update the retained layeral data.
            if self.full_outputs:
                rho = eps
                for quantity, array in (("den", den),("pre", pre),("rho", rho),("eps", eps)):
                    setattr(self, f"{quantity}_{layer}", array.copy())

                # Update the boundaries after matching.
                boundary = {
                    "den": np.array([den.min(), den.max()]),
                    "pre": np.array([pre.min(), pre.max()]),
                    "rho": np.array([rho.min(), rho.max()]),
                    "eps": np.array([eps.min(), eps.max()]),
                }

                self.boundaries[layer] = boundary
            
            # Collect the retained data.
            den_all.append(den)
            pre_all.append(pre)
            eps_all.append(eps)

            # The next layer must extend below the lowest retained point.
            previous_den = den[-1]
            previous_pre = pre[-1]
            previous_eps = eps[-1]

        if not den_all:
            raise ValueError("No EoS data available for stitching.")

        # Reverse the complete arrays to increasing density.
        den = np.concatenate(den_all)[::-1]
        pre = np.concatenate(pre_all)[::-1]
        eps = np.concatenate(eps_all)[::-1]

        mub = (eps + pre) / den

        return den, pre, eps, mub
        
        
    
    def EoS_nucleonic(self):
        """Construct the hadronic EoS through the outer core and crust."""

        #self.load_data()
        layers = [(layer, self.data[layer]) for layer in self.nucleonic_layers if layer in self.data ]  
        
        #print(layers)
        self.den_tot, self.pre_tot,self.eps_tot, self.mub_tot = self._match_eos_layers(layers)
        if self.full_outputs:
            self.rho_tot =  self.eps_tot
            self._set_active_layers(include_ym=False)
            for layer in self.active_layers:
                self.data_after_eos_construction[layer] = self._get_layer_data(layer)

        return self
        
        #(self.den_tot, self.pre_tot, self.rho_tot, self.eps_tot,)
        
    def EoS_YM(self):
        """Construct an EoS containing one or two YM phases."""

        #self.load_data()
        
        

        phases = sorted( self.inner_core_phases.items(),
            key=lambda item: item[1]["phase_number"],
        )

        if not phases:
            return self.EoS_nucleonic()

        if len(phases) > 2:
            raise ValueError("At most two inner-core phases are currently supported." )

        phases = sorted([
        (phase_name, phase_info)
        for phase_name, phase_info in self.inner_core_phases.items()
        if phase_info["type"].upper() == "YM"],
        key=lambda item: item[1]["phase_number"])
        

        layers = [
            (
                f"inner_core_phase{phase_info['phase_number']}",
                phase_info["data"],
            )
            for _, phase_info in phases
        ]

        # Continue from the outer core through the atmosphere.
        layers.extend( (layer, self.data[layer])  for layer in self.nucleonic_layers   if layer in self.data )
        
        #self._set_active_layers(include_ym=True)

        (self.den_tot,self.pre_tot,self.eps_tot,self.mub_tot,) = self._match_eos_layers(layers)
        if self.full_outputs:
            self.rho_tot=self.eps_tot
            self._set_active_layers(include_ym=True)

            self.data_after_eos_construction = {layer: self._get_layer_data(layer)  for layer in self.active_layers}

        return self
        
        
        
    def interpolate_at_pressure(self, pressure, nb, pb, eps):

        valid = (np.isfinite(pb)  & np.isfinite(nb)  & np.isfinite(eps)  & (pb > 0)   & (nb > 0)   & (eps > 0) )

        pb = pb[valid]
        nb = nb[valid]
        eps = eps[valid]

        order = np.argsort(pb)

        pb = pb[order]
        nb = nb[order]
        eps = eps[order]

        pb_unique, indices = np.unique(pb, return_index=True)

        nb = nb[indices]
        eps = eps[indices]
        pb = pb_unique

        if not (pb[0] <= pressure <= pb[-1]):
            raise ValueError(  "Transition pressure lies outside the EoS pressure range."    )

        log_P = np.log(pb)
        log_Pc = np.log(pressure)

        

        nb_at_P = np.exp(PchipInterpolator(log_P, np.log(nb))(log_Pc)) # PchipInterpolator flacuates

        eps_at_P = np.exp(PchipInterpolator(log_P, np.log(eps))(log_Pc))
        
            

        return nb_at_P, eps_at_P 

        
        
        
    def _update_layer_boundaries(self, layer):
        """Update the boundaries of a layeral EoS."""

        boundary = {}

        for quantity in ("den", "pre", "rho", "eps"):
            values = getattr(self, f"{quantity}_{layer}", None)

            if values is None or len(values) == 0:
                boundary[quantity] = np.array([])
            else:
                boundary[quantity] = np.array([ np.min(values),   np.max(values) ])

        # Update layeral chemical potential if available.
        den = getattr(self, f"den_{layer}", None)
        pre = getattr(self, f"pre_{layer}", None)
        eps = getattr(self, f"eps_{layer}", None)

        if ( den is not None and pre is not None  and eps is not None  and len(den) > 0):
            setattr(self, f"mub_{layer}", (eps + pre) / den)

            boundary["mub"] = np.array([np.min(getattr(self, f"mub_{layer}")), np.max(getattr(self, f"mub_{layer}"))])
        else:
            boundary["mub"] = np.array([])

        self.boundaries[layer] = boundary
        
    def _find_transition_layer(self, transition_density):
        """Find the active background layer containing the transition."""
        #print(self.active_layers)

        for layer in self.active_layers:
        
            
            den = getattr(self, f"den_{layer}", None)
            
            if den is None or len(den) == 0:
                continue

            if den.min() <= transition_density <= den.max():
                return layer

        raise ValueError(f"Could not identify the layer containing transition density n = {transition_density}.")
        
        
        
        
    def update_layers(self, Pc, nH,epsH):
        """Update background layers after a phase transition."""

        transition_layer = self._find_transition_layer(nH)
        self.transition_layer = transition_layer

        active_layers = []

        for layer in self.active_layers:

            den = getattr(self, f"den_{layer}", None)
            pre = getattr(self, f"pre_{layer}", None)
            #rho = getattr(self, f"rho_{layer}", None)
            eps = getattr(self, f"eps_{layer}", None)

            if den is None or len(den) == 0:
                continue

            # Retain the background branch below the transition pressure.
            mask = pre <= Pc

            den = den[mask].copy()
            pre = pre[mask].copy()
            
            eps = eps[mask].copy()

            # Insert the hadronic-side critical point.
            if layer == transition_layer:
                den = np.append(den, nH)
                pre = np.append(pre, Pc)
                #rho = np.append(rho, rhoH)
                eps = np.append(eps, epsH)

            # Remove layers that have no valid points remaining.
            rho=eps
            if len(den) == 0:
                for quantity in ("den", "pre", "rho", "eps"):
                    setattr(self, f"{quantity}_{layer}", None)

                self.boundaries[layer] = {
                    quantity: np.array([])
                    for quantity in ("den", "pre", "rho", "eps", "mub")
                }
                continue

            # Sort by increasing density.
            order = np.argsort(den)
            den, pre, rho, eps = (
                arr[order] for arr in (den, pre, rho, eps)
            )

            for quantity, array in (
                ("den", den),
                ("pre", pre),
                ("rho", rho),
                ("eps", eps),
            ):
                setattr(self, f"{quantity}_{layer}", array)

            self._update_layer_boundaries(layer)
            active_layers.append(layer)

        # Keep only layers with valid data.
        self.active_layers = active_layers

        return transition_layer   
        
        
    def _get_layer_data(self, layer):
        """Return the currently valid data for a layer."""

        data = self.data[layer]

        if not self.full_outputs:
            return data
        
                 
        data["rho"] = data["eps"].copy()
        data["pre_cgs"]=np.asarray(data["pre"])*1/nuda.cst.cgsP2MeVfm3
        data["rho_cgs"]=np.asarray(data["eps"])*1/nuda.cst.g_cm3toMeVfm3
        data["eps_cgs"]=np.asarray(data["eps"])*nuda.cst.c_cgs**2
        data["den_cgs"]=np.asarray(data["den"])*nuda.cst.cm3_to_fm3
        

        den_min, den_max = self.boundaries[layer]["den"]

        return data.loc[data["den"].between(den_min, den_max)].copy()
                
        
    def _set_active_layers(self, include_ym=False):
        """Set the valid layers from the constructed EoS. Currently works for nuclear and YM
        
         This is  just an internal function, latter being used to identify the phase transition layers        
        """

        layers = []

        if include_ym:
            phases = sorted(self.inner_core_phases.items(),key=lambda item: item[1]["phase_number"],)

            for _, phase in phases:
                if phase["type"].upper() == "YM":
                    layers.append(f"inner_core_phase{phase['phase_number']}")

        layers.extend(["outer_core","inner_crust","outer_crust","atmosphere",])

    
        self.active_layers = [layer for layer in layers  if getattr(self, f"den_{layer}", None) is not None    ]
        
            
    
                
        
    def EoS_Hybrid(self, Method=None):
        """
        Construct a hybrid EoS by applying one QM phase transition        to the previously constructed background EoS.

        The background eos may be:     1. nucleoninc EoS      2. YM + hadronic EoS

        The background eos must be constructed before using this.
        """

        # --------------------------------------------------
        # 1. Identify the configured QM phase
        # --------------------------------------------------
        
        
        required = ("den_tot","pre_tot","eps_tot")

        if not all(hasattr(self, name) for name in required):
            raise RuntimeError(
                "The background EoS has not been constructed. "
                "Call EoS_nucleonic() or EoS_YM() first."
            )

        den_bg = np.asarray(self.den_tot).copy()
        pre_bg = np.asarray(self.pre_tot).copy()
        #rho_bg = np.asarray(self.rho_tot).copy()
        eps_bg = np.asarray(self.eps_tot).copy()

        mub_bg = np.asarray(self.mub_tot).copy()
        
        
        
        
        valid_bg = den_bg >= self.den_sat

        den_H = den_bg[valid_bg]
        pre_H = pre_bg[valid_bg]
        eps_H = eps_bg[valid_bg]
        mub_H = mub_bg[valid_bg]
        
        
        
        phases = sorted(self.inner_core_phases.items(),key=lambda item: item[1]["phase_number"])

        qm_phases = [(key, phase) for key, phase in phases if phase["type"].upper() == "QM"]

        if len(qm_phases) == 0:
            raise ValueError("No QM phase is configured.")

        if len(qm_phases) > 1:
            raise ValueError("Only one QM phase transition is currently supported.")

        phase_key, qm_phase = qm_phases[0]
        
        if qm_phase['source'] == 'function':
            QM_eos_function_name = qm_phase['model']
            if  QM_eos_function_name.strip().lower() not in self.QMeos_functions :
                print(qm_phase['model'])
                raise KeyError('In valid function for QM. See avilable models model.self.QMeos_functions')
            parameters=qm_phase.get("parameters", {})
            
            self.den_critical_H = parameters['den_tr_H']
            self.delta_Den_pt =parameters['delta_den']
            #alpha = parameters['alpha']
             
            if self.den_sat > self.den_critical_H:
                raise ("no phase transition below saturation density is allowed ")
            
            if max(den_H) < self.den_critical_H:
                raise ("The critical density is outside the density range ")
            
            
            self.pre_critical_H = np.exp(PchipInterpolator(np.log(den_H), np.log(pre_H))(np.log(self.den_critical_H)))

            self.eps_critical_H = np.exp(PchipInterpolator(np.log(den_H), np.log(eps_H))(np.log(self.den_critical_H )))

            self.mu_critical = (self.pre_critical_H + self.eps_critical_H ) /self.den_critical_H
            
            #self.rho_critical_H = self.eps_critical_H 
            self.pre_critical = self.pre_critical_H
            

             
            
            
            parameters.update({"eps_tr_H":self.eps_critical_H,"pre_critical":self.pre_critical,"mu_critical":self.mu_critical})
            
            #self.den_critical_H ,self.eps_critical_H,self.pre_critical_H,self.delta_Den_pt,alpha,self.mu_critical)
            
            eos_QM=self._evaluate_eos_function(self.QMeos_functions[QM_eos_function_name.strip().lower()], **parameters)
            if eos_QM is None:
                print("Valid QM EoS not found. Returning the hadronic EoS")
                return self            
            
            if self.full_outputs:
                qm_layer = f"inner_core_phase{qm_phase['phase_number']}"
                self.data[qm_layer]=eos_QM
            
            for key in ("den", "pre", "eps"):
                if key not in eos_QM.columns:
                    raise ValueError(f"Function '{QM_eos_function_name}' did not return '{key}'.")
                
            
            den_Q_branch = eos_QM["den"].to_numpy()
            pre_Q_branch =  eos_QM["pre"].to_numpy()            
            eps_Q_branch = eos_QM["eps"].to_numpy()
            mu_Q_branch = (pre_Q_branch + eps_Q_branch)/den_Q_branch
            
             
            self.den_critical_Q = den_Q_branch[0]
            self.eps_critical_Q = eps_Q_branch[0]            
            self.delta_E= self.eps_critical_Q - self.eps_critical_H 
            
            
            den_M = np.linspace(self.den_critical_H+0.005*self.den_critical_H , self.den_critical_Q-0.005*self.den_critical_Q, 20)
            pre_M=np.zeros_like(den_M)+self.pre_critical_H
            mu_M=np.zeros_like(den_M)+self.mu_critical
            eps_M= den_M*self.mu_critical-self.pre_critical_H
            #rho_M = eps_M.copy()

            # Convert energy density to mass density if using cgs units.
            
            den_Q_branch  = np.concatenate((den_M, den_Q_branch ))
            pre_Q_branch = np.concatenate((pre_M, pre_Q_branch ))
            #rho_Q_branch = np.concatenate((rho_M, rho_Q_branch ))
            eps_Q_branch = np.concatenate((eps_M, eps_Q_branch ))
            
        
        if qm_phase['source'] == 'file':
        
            if "data" not in qm_phase:
                raise RuntimeError( f"Data for QM phase '{phase_key}' have not been loaded.")

            values = qm_phase["data"]
            den_Q = np.asarray(values["den"])
            pre_Q = np.asarray(values["pre"])
            #rho_Q = np.asarray(values["rho"])
            eps_Q = np.asarray(values["eps"]) 
            mub_Q = (eps_Q + pre_Q) / den_Q        
            method = Method or self.PT_Method["method"]
            parameters = self.PT_Method.get("parameters", {})
            
            
            if method not in ["Maxwell", "MIM", "tanH_Interp"]:
                raise KeyError(f"Invalid method for phase construction: {method}")

            
            if method == "MIM":
                self.x_deltaP = parameters.get("x_deltaP")

                if self.x_deltaP is None:
                    self.x_deltaP =0.
                    method= "Maxwell"
                    raise RuntimeError("No Delta P is given for MIM construction.")

            elif method == "tanH_Interp":
                self.den_critical_H = parameters.get("den_H")
                self.den_critical_Q = parameters.get("den_Q")

                if self.den_critical_H is None or self.den_critical_Q is None:
                    raise RuntimeError("Both den_H and den_Q must be given for tanH_Interp construction." )
                    
                if (self.den_critical_Q - self.den_critical_H)<=0. :
                    raise RuntimeError("den_H > den_Q Not Acceptable." )


            elif method == "Maxwell":
                pass

        
        

            if len(den_H) < 2 or len(den_Q) < 2:
                raise ValueError("Insufficient EoS points for the phase transition." )
                
            
            if method =='tanH_Interp':
            
            
                self.pre_critical = np.exp(PchipInterpolator(np.log(den_H), np.log(pre_H))(np.log(self.den_critical_H )))

                self.eps_critical_H = np.exp(PchipInterpolator(np.log(den_H), np.log(eps_H))(np.log(self.den_critical_H )))

                self.mu_critical = (self.pre_critical + self.eps_critical_H ) /self.den_critical_H
                
                #self.rho_critical_H= self.eps_critical_H 
                raise NotImplementedError("not implimented Yet")
            
            
            if method  in ["Maxwell",'MIM'] :
                if (np.min(mub_Q) > np.max(mub_H) or np.max(mub_Q) < np.min(mub_H)):
                    print("No common chemical-potential range between the hadronic and quark EoSs. Returning EoS upto previous layer" )

                    return (self.den_tot,  self.pre_tot, self.rho_tot,  self.eps_tot )

                if ( np.min(pre_Q) > np.max(pre_H) or np.max(pre_Q) < np.min(pre_H)):
                    print( "No common pressure range for the Maxwell construction."  )

                    return self #(self.den_tot,  self.pre_tot, self.rho_tot,  self.eps_tot )
     
            
                core1_core2_layers = {'r1': {'pre': pre_H,'mub': mub_H}, 'r2': {'pre': pre_Q,'mub': mub_Q}}
                Maxwell= nuda.eos.mix_phase_Classes.Maxwell_construction(core1_core2_layers)
                Maxwell.muc_pc_intersection()

                if not Maxwell.check:
                    print("Maxwell construction failed. \n")
                    print("Returning the hadronic EoS." )

                    return self#(self.den_tot,  self.pre_tot, self.rho_tot,  self.eps_tot )

                # Transition chemical potential and pressure
                self.mu_critical = Maxwell.mu_c
                self.pre_critical = Maxwell.P_c
                
                
                
                #if method == 'Maxwell':
                Pc = self.pre_critical

                nH,  epsH = self.interpolate_at_pressure(self.pre_critical, den_H, pre_H,  eps_H)
                self.den_critical_H = nH
                #self.rho_critical_H = rhoH
                self.eps_critical_H = epsH

                nQ, epsQ = self.interpolate_at_pressure(self.pre_critical, den_Q, pre_Q,  eps_Q)

                self.den_critical_Q = nQ
                #self.rho_critical_Q = rhoQ
                self.eps_critical_Q = epsQ

    
                
                
                mask_Q = pre_Q > Pc

                den_Q_branch = den_Q[mask_Q]
                pre_Q_branch = pre_Q[mask_Q]
                #rho_Q_branch = rho_Q[mask_Q]
                eps_Q_branch = eps_Q[mask_Q]

                # Insert the QM-side critical point.
                den_Q_branch = np.append(nQ, den_Q_branch)
                pre_Q_branch = np.append(Pc, pre_Q_branch)
                #rho_Q_branch = np.append(rhoQ, rho_Q_branch)
                eps_Q_branch = np.append(epsQ, eps_Q_branch)

                # Ensure increasing density order.
                order = np.argsort(den_Q_branch)

                den_Q_branch = den_Q_branch[order]
                pre_Q_branch = pre_Q_branch[order]
                #rho_Q_branch = rho_Q_branch[order]
                eps_Q_branch = eps_Q_branch[order]
                mub_Q_branch = (pre_Q_branch + eps_Q_branch ) / den_Q_branch
                
                if method == 'Maxwell':
                    self.pre_critical_H= self.pre_critical
                    
                    
                    if (self.den_critical_Q -self.den_critical_H) <=0.:
                        print("n_Q < n_H. \n")
                        print("Returning the hadronic EoS." )
                        return self
                    if (self.eps_critical_Q -self.eps_critical_H) <=0.:
                        print("E_Q < E_H. \n")
                        print("Returning the hadronic EoS." )
                        return self
                        
                    den_M = np.linspace(self.den_critical_H+0.005*self.den_critical_H , self.den_critical_Q-0.005*self.den_critical_Q, 20)
                    pre_M=np.zeros_like(den_M)+self.pre_critical_H
                    mu_M=np.zeros_like(den_M)+self.mu_critical
                    eps_M= den_M*self.mu_critical-self.pre_critical_H
                    #rho_M = eps_M.copy()

                    # Convert energy density to mass density if using cgs units.
                    

                    den_Q_branch  = np.concatenate((den_M, den_Q_branch ))
                    pre_Q_branch = np.concatenate((pre_M, pre_Q_branch ))
                    eps_Q_branch = np.concatenate((eps_M, eps_Q_branch ))
                    
                    
                
                if method == 'MIM':
                    valid_bg = ((den_bg >= self.den_sat) & (pre_bg < self.pre_critical))

                    den_H = den_bg[valid_bg]
                    pre_H = pre_bg[valid_bg]
                    #rho_H = rho_bg[valid_bg]
                    eps_H = eps_bg[valid_bg]
                    mub_H = mub_bg[valid_bg]
                    
                    den_H = np.append(den_H, self.den_critical_H)
                    pre_H = np.append(pre_H, self.pre_critical)
                    eps_H = np.append(eps_H, self.eps_critical_H)
                    mub_H = np.append(mub_H, self.mu_critical)
                    
                
                    
                
                
                    core1_core2_layers = {'r1': {'pre': pre_H,'mub': mub_H,'den':den_H}, 'r2': {'pre': pre_Q_branch,'mub': mub_Q_branch,'den':den_Q_branch}}
                    MIM = nuda.eos.mix_phase_Classes.MixedInterpolatePhase(core1_core2_layers,muc=self.mu_critical,Pc=self.pre_critical)
                    result_MIM = MIM.find_boundaries(x_deltaP=self.x_deltaP)
                    if not MIM.check_MIM:
                        print("MIM failed : Returing the Hadronic EoS")
                        return self 
                    if result_MIM is None:
                        print("MIM failed : Returing the Hadronic EoS")
                        return self
                        
                    #print(result_MIM)
                        
                    self.alpha1=  result_MIM['alpha1']
                    self.alpha2= result_MIM['alpha2']               
                    
                    self.pre_critical_H= result_MIM['P_H']
                    self.den_critical_H= result_MIM['n_H']
                    self.mu_H= result_MIM['mu_H']
                    
                    self.eps_critical_H= self.mu_H * self.den_critical_H - self.pre_critical
                    #self.rho_critical_H=self.eps_critical_H
                
                    self.mu_Q= result_MIM['mu_Q']
                    self.pre_critical_Q =  result_MIM['P_Q']
                    self.den_critical_Q = result_MIM['n_Q']
                    self.eps_critical_Q= self.mu_Q * self.den_critical_Q- self.pre_critical_Q
                    #self.rho_critical_Q=self.eps_critical_Q
                    
                        
                    if (self.den_critical_Q -self.den_critical_H) <=0.:
                        return self
                    if (self.eps_critical_Q -self.eps_critical_H) <=0.:
                        return self
                    if (self.mu_Q -self.mu_H) <=0.:
                        return self
                    if (self.pre_critical_Q -self.pre_critical_H) <=0.:
                        return self
                    
                    
                    
                    
                    mask_quark = ((pre_Q > self.pre_critical_Q) & (mub_Q > self.mu_Q) &  (den_Q >self.den_critical_Q))

               
                    den_quark = den_Q[mask_quark].copy()
                    pre_quark = pre_Q[mask_quark].copy()
                    #rho_quark = eps_Q[mask_quark].copy()
                    eps_quark = eps_Q[mask_quark].copy()
                    mub_quark = mub_Q[mask_quark].copy()

                    mueval = np.linspace(self.mu_H+0.01*self.mu_H , self.mu_Q, 30)
                
                    

                    den_M, pre_M, eps_M = (MIM.Pre_MIM_den_MIM_and_eps_MIM(mueval, self.alpha1, self.alpha2))
                    den_M = np.asarray(den_M)
                    pre_M = np.asarray(pre_M)
                    eps_M = np.asarray(eps_M)
                    #print(den_M, pre_M, eps_M)

                    # Assumption: eps_M is in energy-density units.
                    #rho_M = eps_M.copy()

                    # Convert energy density to mass density if using cgs units.
                    #if not self.nuclear_unit :
                     #   rho_quark =rho_quark / nuda.cst.c2_cgs
                      #  rho_M = eps_M / nuda.cst.c2_cgs

                    den_Q_branch  = np.concatenate((den_M, den_quark))
                    pre_Q_branch= np.concatenate((pre_M, pre_quark))
                    #rho_Q_branch = np.concatenate((rho_M, rho_quark))
                    eps_Q_branch = np.concatenate((eps_M, eps_quark))
                    #mub_quark = np.concatenate((mueval, mub_quark))
                    
                    order = np.argsort(den_Q_branch)

                    den_Q_branch = den_Q_branch[order]
                    pre_Q_branch = pre_Q_branch[order]
                    #rho_Q_branch = rho_Q_branch[order]
                    eps_Q_branch = eps_Q_branch[order]
                        
                        

             
       
        if len(den_Q_branch) == 0 or len(pre_Q_branch) != len(den_Q_branch) or  len(eps_Q_branch) != len(den_Q_branch) :
            return self
        if not all(np.all(np.isfinite(arr)) for arr in [den_Q_branch, pre_Q_branch,eps_Q_branch]):
            return self
        if any(np.any(arr <= 0.) for arr in [den_Q_branch, pre_Q_branch, eps_Q_branch]):
            return self#(self.den_tot,  self.pre_tot, self.rho_tot,  self.eps_tot )
        
        
        
        
                   
        mask_H = ((pre_bg < self.pre_critical_H) & (den_bg < self.den_critical_H) & (eps_bg < self.eps_critical_H) )

        den_H = den_bg[mask_H]
        pre_H = pre_bg[mask_H]
        #rho_H = rho_bg[mask_H]
        eps_H = eps_bg[mask_H]
        
        den_H = np.append(den_H, self.den_critical_H)
        pre_H = np.append(pre_H, self.pre_critical_H)
        #rho_H = np.append(rho_H, self.rho_critical_H)
        eps_H = np.append(eps_H, self.eps_critical_H)
        
        self.den_tot = np.concatenate((den_H, den_Q_branch))
        self.pre_tot = np.concatenate((pre_H, pre_Q_branch))
        #self.rho_tot = np.concatenate((rho_H, rho_Q_branch))
        self.eps_tot = np.concatenate((eps_H, eps_Q_branch))
        self.mub_tot = (self.pre_tot + self.eps_tot) / self.den_tot
        
        # Check positive quantities
        
        
        if not self.full_outputs :
            return self 
        if self.full_outputs :
            #rho = rho[mask].copy()
            self.rho_tot =self.eps_tot
            self.rho_critical_H= self.eps_critical_H
            self.rho_critical_Q= self.eps_critical_Q 
            rho_Q_branch = eps_Q_branch
            
            self.update_layers(self.pre_critical_H, self.den_critical_H,self.eps_critical_H )
            qm_layer = f"inner_core_phase{qm_phase['phase_number']}"
            
            #for quantity, array in (("den", den_Q_branch[den_Q_branch>=self.den_critical_Q]), ("pre", pre_Q_branch[den_Q_branch>=self.den_critical_Q]), 
            #("rho", rho_Q_branch[den_Q_branch>=self.den_critical_Q]), ("eps", eps_Q_branch[den_Q_branch>=self.den_critical_Q])):
               # setattr(self, f"{quantity}_{qm_layer}", np.asarray(array).copy())
                
                
            for quantity, array in (("den", den_Q_branch), ("pre", pre_Q_branch), ("rho", rho_Q_branch), ("eps", eps_Q_branch)):
                setattr(self, f"{quantity}_{qm_layer}", np.asarray(array).copy())

            # Update the quark layer's boundaries.
            self._update_layer_boundaries(qm_layer)
            layers = []
            
            for layer in reversed(self.active_layers):
                if layer != qm_layer and getattr(self, f"den_{layer}", None) is not None and len(getattr(self, f"den_{layer}")) > 0:
                    layers.append(layer)
            
            layers.append(qm_layer)
            self.active_layers=layers
            #print(self.active_layers)
            self.data_after_eos_construction = {
                layer: self._get_layer_data(layer)
                for layer in layers
                if layer in self.boundaries
            }
            df={"den":den_M,"pre":pre_M,"eps":eps_M}
            self.data_after_eos_construction['Mixed_Phase']=pd.DataFrame(df)
            self.boundaries['Mixed_Phase']={
                key:np.array([ np.min(df[key]),   np.max(df[key]) ]) for key in ["den","pre","eps"]}
            return self


        
        

        return self# self.den_tot, self.pre_tot, self.rho_tot, self.eps_tot
    def _necessary_eos_checks(self):
    
        if np.any(self.pre_tot <= 0.):
            raise ValueError("Pressure must be strictly positive")

        if np.any(self.eps_tot <= 0.):
            raise ValueError("Energy density must be strictly positive.")

        if np.any(self.den_tot <= 0.):
            raise ValueError("Density must be strictly positive.")

        # Check monotonicity
        dn = np.diff(np.log(self.den_tot))
        dp = np.diff(np.log(self.pre_tot))
        de = np.diff(np.log(self.eps_tot))
        #print(self.pre_tot)
        
        
        

        if np.any(dn <= 0.):
            self.init_self()
            raise ValueError("Density must increase strictly (dn > 0).")
            
         if np.any(de <= 0.):
            self.init_self()
            raise ValueError("Energy density must increase strictly (de > 0).")
            
        

        if np.any(dp < 0.):# and np.any(self.cs2_tot <0):
            #self.init_self()
            #print(dp)
            raise ValueError(f"Pressure must be non-decreasing (dp >= 0).")

       
        
        
            
        
        try:
            logeoflogp = PchipInterpolator(np.log(self.eps_tot), np.log(self.pre_tot))
            self.gamma_tot = logeoflogp.derivative()(np.log(self.eps_tot))
            self.cs2_tot = self.pre_tot / self.eps_tot * self.gamma_tot 
        except:
            pass
            
        mask_cs2_acausal = self.cs2_tot > 1.

        if np.any(mask_cs2_acausal):
            print(f"Acausal EoS at densities [ in {self.den_unit} ] := {self.den_tot[mask_cs2_acausal]} , with cs^2 [in c^2] = {self.cs2_tot[mask_cs2_acausal]}")
            return self
            
        return self
        
             
        
    def Final_EoS(self):
        """Construct the final EoS based on the configured inner-core phases."""

        self.load_data()
        #print(self.data)

        phases = sorted(self.inner_core_phases.values(),key=lambda phase: phase["phase_number"] )

        if len(phases) > 2:
            raise ValueError("maximum 2 inner-core phases are supported.")

        if not phases:
            self.EoS_nucleonic()
            self._necessary_eos_checks()
            return self
            

        phase1_type = phases[0]["type"].upper()
        phase2_type = phases[1]["type"].upper() if len(phases) == 2 else None

        if phase1_type not in {"YM", "QM"}:
            raise ValueError(f"Unsupported phase-1 type: {phase1}")

        if phase2_type is not None and phase2_type not in {"YM", "QM"}:
            raise ValueError(f"Unsupported phase-2 type: {phase2}")

        # QM followed by YM is not supported.
        if phase1_type == "QM" and phase2_type == "YM":
            raise ValueError("Phase 1 = QM and phase 2 = YM is not supported.")

        # Only one QM phase transition is currently supported.
        if phase1_type == "QM" and phase2_type == "QM":
            raise ValueError("Only one QM phase transition is currently supported.")

        # YM-only or YM + YM.
        if phase1_type == "YM" and phase2_type in (None, "YM"):
            self.EoS_YM()
            self._necessary_eos_checks()
            return self

        # QM only: construct the hadronic background first.
        if phase1_type == "QM" and phase2_type is None:
            self.EoS_nucleonic()
            self.EoS_Hybrid()
            self._necessary_eos_checks()
            return self

        # YM followed by QM.
        if phase1_type == "YM" and phase2_type == "QM":
            self.EoS_YM()
            self.EoS_Hybrid()
            self._necessary_eos_checks()
            return self
            
    def print_outputs( self ):
        """
        Method which print outputs on terminal's screen.
        """
        #
        if nuda.env.verb: print("Enter print_outputs()")        
        self.set_eos()
        print("- Printing output:")        
        print("Compact star layers:")#,self.eos_layers)
        for key in self.layers:
            if self.eos_layers[key]:
                print(f"layer: {key}, model: {self.eos_layers[key]} ")
        
        self.Final_EoS()
        
        if self.full_outputs:        
            print("Density Boundaries of each layers:")
            #print(self.boundaries)
            for layer in self.active_layers:
                print(f"{layer} : minimum density= {self.boundaries[layer]['den'][0] } {self.den_unit}, maximum density = {self.boundaries[layer]['den'][1] } {self.den_unit}", )
        if not self.full_outputs:
            print(f"Use full_outputs=True, during class initiation to see the boundaries and  available information in each layer")
        
        print("EoS info:")        
        if self.den_tot is not None: print(f"   den: {self.den_tot} in {self.den_unit}")
        if self.eps_tot is not None: print(f"   eps: {self.eps_tot}in {self.eps_unit}")
        if self.pre_tot is not None: print(f"   pre: {self.pre_tot}in {self.pre_unit}")
        if self.cs2_tot is not None: print(f"   cs^2: {self.cs2_tot}in {self.cs2_unit}")
        if nuda.env.verb: print("Exit print_outputs()")
        
    def init_self( self ):
        self.models = {} 
        self.files = {}         
        self.boundaries_from_data = {} ## For the intial layers
        self.boundaries = {} ## after  the final matching of layers       
        self.data = {} ## For the fixed layers
        self.inner_core_phases = {}
        self.data_after_eos_construction={}    
        self.den_tot = None
        self.eps_tot = None
        self.pre_tot = None
        self.rho_tot = None
        self.mub_tot = None        
        self.cs2_tot = None        
        
        
        self.nuclear_unit =True
        
        #if  self.nuclear_unit :
        self.den_sat = nuda.cst.nsat
        self.den_unit = 'fm$^{-3}$'
        self.eps_unit = 'MeV fm$^{-3}$'
        self.pre_unit = 'MeV fm$^{-3}$'
        self.mub_unit = 'MeV'
        self.cs2_unit ="c^2"
            
        self.layers = ["inner_core","outer_core", "inner_crust","outer_crust","atmosphere"]
        self.nucleonic_layers = ["outer_core","inner_crust","outer_crust","atmosphere"]
        self.agnostic_models= {"random_speed_of_sound":nuda.eos.Random_speed_of_sound}
        self.QMeos_functions = {"qm_linear":nuda.eos.mix_phase_Classes.QM_linear} ## currently only applicable to QM_linear


        for layer in self.layers:
            setattr(self, f"den_{layer}", None)
            setattr(self, f"pre_{layer}", None)
            setattr(self, f"eps_{layer}", None)
            setattr(self, f"rho_{layer}", None)
        

                    
                
            
"""
def _load_layer_outer_core(self,layer):
        #Load an EoS from a local file or nucleardatapy.
        
        config = self.eos_layers[layer]
        
        
        if isinstance(config, str):
            config = {"model": config}
        
        model = config.get("model")
        eos_data_file={}
        eos_data={}

        if model:
            data= self._load_layer(layer, model)
            
            #print(data,self.full_outputs)
            if not isinstance(data, pd.DataFrame):
                data=pd.DataFrame(data)
            
            df = data.copy()
            eos_data_file = {key: df[key].to_numpy(copy=True)  for key in ("den", "pre", "eps")}
            
            for key in ("den", "pre", "eps"):
                if key not in eos_data_file or eos_data_file[key] is None:
                    raise ValueError( f"Missing '{key}' in the loaded outer-core EoS."   )

                if not np.all(np.isfinite(eos_data_file[key])):
                    raise ValueError(f"Non-finite values found in outer_core['{key}']." )

            if len({len(eos_data_file[key]) for key in ("den", "pre", "eps")}) != 1:
                raise ValueError("The outer-core den, pre, and eps arrays must have equal lengths.")               
                    
        
        
        den_min_file=np.min(np.asarray(df['den']))
        den_max_file=np.max(np.asarray(df['den']))
        eos_data=eos_data_file
        
        
               
        function_name = config.get("function")

        if function_name:
            function_name = function_name.strip().lower()
            if function_name not in self.agnostic_models:
                raise ValueError(f"Unknown function '{function_name}'. Available functions: {list(self.agnostic_models)}")

            parameters = config.get("parameters") or {}

            if function_name == "random_speed_of_sound":
                den_tr = parameters.get("den_tr")
                if den_tr is None:
                    den_tr, eps_tr, pre_tr = eos_data_file["den"][-1], eos_data_file["eps"][-1], eos_data_file["pre"][-1]
                else:
                    den_tr=min(den_tr,den_max_file)
                    eps_tr = np.exp(PchipInterpolator(np.log(eos_data_file["den"]), np.log(eos_data_file["eps"]))(np.log(den_tr)))
                    pre_tr = np.exp(PchipInterpolator(np.log(eos_data_file["den"]), np.log(eos_data_file["pre"]))(np.log(den_tr)))

                mu_tr = (eps_tr + pre_tr) / den_tr
                logeoflogp = PchipInterpolator(np.log(eos_data_file["eps"]), np.log(eos_data_file["pre"]))
                cs2_tr = pre_tr / eps_tr * logeoflogp.derivative()(np.log(eps_tr))
                parameters.update({"den_tr": den_tr, "eps_tr": eps_tr, "pre_tr": pre_tr, "mu_tr": mu_tr, "cs2_tr": cs2_tr})
                parameters["full_outputs"] = self.full_outputs
                
                
            # update function parameters here

            eos_function_data = self._evaluate_eos_function(self.agnostic_models[function_name], **parameters)

            for key in ("den", "pre", "eps"):
                if key not in eos_function_data.columns:
                    raise ValueError(f"Function '{function_name}' did not return '{key}'.")

            mask_den_file=eos_data["den"]<=den_tr 
            
            for key in ("den", "pre", "eps"):                           
                eos_data[key] = np.concatenate((eos_data_file[key][mask_den_file], eos_function_data[key].to_numpy()))

            

            #print(eos_data)
            if self.full_outputs:
                df=df.loc[df["den"].between(den_min_file, den_tr)].copy()
                
                
                df_func = eos_function_data.copy()
                for col in df.columns:
                    if col not in df_func.columns: df_func[col] = np.nan
                for col in df_func.columns:
                    if col not in df.columns: df[col] = np.nan
                df = pd.concat([df, df_func[df.columns]], ignore_index=True)

        if not self.full_outputs:
            return pd.DataFrame(eos_data)
        else:
            df["rho"] = df["eps"].to_numpy()
            return df
"""
