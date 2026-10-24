import numpy as np
from pathlib import Path
from scipy.interpolate import CubicSpline, PchipInterpolator
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
           object.rho_tot : mass density
           
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

        self.QMeos_functions = {"QM_linear":nuda.eos.mix_phase_Classes.QM_linear} ## currently only applicable to QM_linear

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

            if model_name in self.QMeos_functions:
                parameters = phase_info.get("parameters", {})
                if not isinstance(parameters, dict):
                    raise TypeError(f"'parameters' for '{phase_name}' must be a dictionary.")

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

            
            if model_name in self.QMeos_functions:

                phase_data["source"] = "function"
                phase_data["function"] = (self.QMeos_functions[model_name])

            
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

            rho : mass density [g/cm^3]
            pre : pressure [dyn/cm^2]
            den : baryon number density [cm^-3]

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
        
        
        

   
        """
        if not self.nuclear_unit :
            pre = pre * {"cgs": 1.0,"nuc": 1/nuda.cst.cgsP2MeVfm3,"SI": 10.0}[pre_col.split("_")[-1]]
            den = den* {"cgs": 1, "nuc": nuda.cst.cm3_to_fm3, "SI": 1e-6}[den_col.split("_")[-1]]
            rho = rho * {"cgs": 1, "nuc": 1/nuda.cst.g_cm3toMeVfm3, "SI": 1e-3}[rho_col.split("_")[-1]]
            eps = rho * nuda.cst.c_cgs**2
        """
        if self.nuclear_unit:
            pre = df[pre_col].to_numpy() * {"cgs": nuda.cst.cgsP2MeVfm3,"nuc": 1,"SI": 10.0*nuda.cst.cgsP2MeVfm3 }[pre_col.split("_")[-1]]
            den = df[den_col].to_numpy() * {"cgs": 1/nuda.cst.cm3_to_fm3, "nuc":1, "SI": 1e-6*1/nuda.cst.cm3_to_fm3}[den_col.split("_")[-1]]
            rho = df[rho_col].to_numpy() * {"cgs": nuda.cst.g_cm3toMeVfm3, "nuc":1, "SI": 1e-3*nuda.cst.g_cm3toMeVfm3}[rho_col.split("_")[-1]]
            eps= rho
        
        if not self.full_outputs: 
            #{"den": den.copy(),"pre": pre.copy(), "rho": rho.copy(),"eps": eps.copy()}                  
            
            self.data[layer] ={"den": den.copy(),"pre": pre.copy(), "rho": rho.copy(),"eps": eps.copy()}                  
            
            return {"den": den.copy(),"pre": pre.copy(), "rho": rho.copy(),"eps": eps.copy()}                  
            
        else:
            
            #df.drop(columns=[pre_col, den_col, rho_col], inplace=True,errors="ignore")
            
            self.models[layer] = {"model": model_name,"filename": filepath}
            df["den"] = den.copy()
            df["pre"] = pre.copy()
            df["rho"] = rho.copy()
            df["eps"] = eps.copy()
            
            df["pre_cgs"]=np.asarray(pre)*1/nuda.cst.cgsP2MeVfm3
            df["rho_cgs"]=np.asarray(rho.copy())*1/nuda.cst.g_cm3toMeVfm3
            df["eps_cgs"]=np.asarray(df["rho_cgs"])*nuda.cst.c_cgs**2
            df["den_cgs"]=np.asarray(den)*nuda.cst.cm3_to_fm3
            
            
            
            
                
                
            self.data[layer] = df
            eos_data={"den": den.copy(),"pre": pre.copy(), "rho": rho.copy(),"eps": eps.copy()}                  
            
            for key in ("den", "pre", "eps", "rho"):
                setattr(self,f"initial_{key}_{layer}",eos_data[key].copy())
            self.boundaries_from_data[layer] = {key: [np.min(eos_data[key].copy()), np.max(eos_data[key].copy())] for key in ("den", "pre", "rho", "eps")}

                
            return  df#{"den": den.copy(),"pre": pre.copy(), "rho": rho.copy(),"eps": eps.copy()}
            #return self
            
            
    def _load_from_nuda_beta(self,layer,model):
        model_name= model.strip().upper()
        #print(model_name)
        micro_models = nuda.matter.micro_esym_models()[0]
        eos_beta={}
        if model_name in micro_models:
            eos_beta=nuda.eos.setupAMBeq(model=model_name)
            if any(not hasattr(eos_beta, q) or getattr(eos_beta, q) is None or not np.all(np.isfinite(getattr(eos_beta, q))) for q in ['pre_tot','den','eps_tot']):
                raise ValueError(f"Invalid EoS quantities for model '{model}'.")
            df={"den":eos_beta.den,"pre":eos_beta.pre_tot,"eps":eos_beta.eps_tot,"rho":eos_beta.eps_tot}
            self.data[layer] = pd.DataFrame(df) if self.full_outputs else df
            return df
        else:
            pheno_types = nuda.matter.pheno_esym_models()[0]        
            for model_type in pheno_types:
                available_pheno_models = nuda.pheno_esym_params(model=model_type)[0]                
                if model_name in available_pheno_models:
                    eos_beta=nuda.eos.setupAMBeq(param=model_name,kind='pheno',model=model_type)                    
                    
                    if any(not hasattr(eos_beta, q) or getattr(eos_beta, q) is None or not np.all(np.isfinite(getattr(eos_beta, q))) for q in ['pre_tot','den','eps_tot']):
                        raise ValueError(f"Invalid EoS quantities for model '{model}'.")
                    
                    df={"den":eos_beta.den,"pre":eos_beta.pre_tot,"eps":eos_beta.eps_tot,"rho":eos_beta.eps_tot}
                    self.data[layer] = pd.DataFrame(df) if self.full_outputs else df
                    return df
                else:
                    raise ValueError( f"Could not find outer_core model '{model}' in nucleardatapy.")
    
    def _load_layer(self, layer, model):
        """Load an EoS from a local file or nucleardatapy."""

        if not model:
            return None

        # 1. Search for the model in the layer directory.
        layer_dir = self.base_dir / layer

        if layer_dir.is_dir():
            matching_files = sorted(filepath.name
            for filepath in layer_dir.iterdir()
            if filepath.is_file()
            and filepath.stem.startswith(model)
            and filepath.suffix == ".csv")
            
            
            if len(matching_files) > 1:
                raise ValueError(f"Multiple files found for '{model}' in {layer_dir}")
            
            if matching_files:
                filepath = layer_dir / matching_files[0]
                return self._load_eos_file( filepath=filepath, layer=layer, model_name=model )
        
        if layer == "outer_core":
            return self._load_from_nuda_beta(layer, model)

        
        raise FileNotFoundError(f"Model '{model}' was not found in '{layer_dir}'" )

            
            
            
            
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
        
        
        

        for layer in self.hadronic_layers:
            model = self.eos_layers.get(layer, "")

            if model:
                self._load_layer(layer, model)
                
        self.identify_inner_core_phases()
        for phase_name, phase_info in self.inner_core_phases.items():

            if phase_info["source"] == "file":

                layer = f"inner_core_phase{phase_info['phase_number']}"

                model_name = phase_info.get("model")

                phase_data = self._load_eos_file( filepath=phase_info["filepath"], layer=layer,model_name=model_name)
                phase_info["data"] = phase_data

            elif phase_info["source"] == "function":
                # Function-based phases are handled separately.
                continue

            else:
                raise ValueError(f"Unknown model for phase '{phase_name}'.")

        return self         
    
    
    
    
    def _evaluate_eos_function(self, phase_name, phase_info):
        """
        Evaluate a  function-based EoS.        
        It works independently, when the parameters, does not depend upon the nucleoninc EoSs
        Helpful, if we plan to include MIT, vMIT, NJL , vNJL, vQCD models
        
        """

        function = phase_info["function"]
        parameters = phase_info.get("parameters", {})
        

        pre, den, eps = function(**parameters) ### This is wehere we calculate the EoS

        pre = np.asarray(pre, dtype=float)
        den = np.asarray(den, dtype=float)
        eps = np.asarray(eps, dtype=float)
        
        order = np.argsort(den)

        den = den[order]
        pre = pre[order]
        eps = eps[order]

        
        if self.nuclear_unit:
            rho = eps.copy()
        else:
            rho = eps / nuda.cst.c2_cgs

        mub = (eps + pre) / den

        return {"den": den.copy(),"pre": pre.copy(),"rho": rho.copy(), "eps": eps.copy(), "mub": mub.copy()}

    # =========================================================
    # Load ordinary layers and inner-core phases
    # =========================================================

    
        
    def _match_eos_layers(self, layers):
        """
        Match EoS layers .
        """

        den_all, pre_all, rho_all, eps_all = [], [], [], []

        previous_den = None
        previous_pre = None
        previous_eps = None

        # Reset layeral attributes for layers being reconstructed.
        if self.full_outputs :
            for layer, _ in layers:
                for quantity in ("den", "pre", "rho", "eps"):
                    setattr(self, f"{quantity}_{layer}", None)

        for layer, values in layers:

            den = np.asarray(values["den"])
            pre = np.asarray(values["pre"])
            rho = np.asarray(values["rho"])
            eps = np.asarray(values["eps"])
            #mub = np.asarray(values["mub"])

            if len(den) == 0:
                continue

            # Sort in decreasing density order.
            order = np.argsort(den)[::-1]
            den, pre, rho, eps = (arr[order] for arr in (den, pre, rho, eps))

            # Apply matching conditions.
            if previous_den is not None:
                mask = ((den < previous_den) & (pre < previous_pre) & (eps < previous_eps))

                den, pre, rho, eps= ( arr[mask] for arr in (den, pre, rho, eps))

            if len(den) == 0:
                continue

            # Update the retained layeral data.
            if self.full_outputs:
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
            rho_all.append(rho)
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
        rho = np.concatenate(rho_all)[::-1]
        eps = np.concatenate(eps_all)[::-1]

        mub = (eps + pre) / den

        return den, pre, rho, eps, mub
        
        
    
    def EoS_Hadronic(self):
        """Construct the hadronic EoS through the outer core and crust."""

        #self.load_data()
        layers = [(layer, self.data[layer]) for layer in self.hadronic_layers if layer in self.data ]  
        self.den_tot, self.pre_tot, self.rho_tot, self.eps_tot, self.mub_tot = self._match_eos_layers(layers)
        if self.full_outputs:
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
            return self.EoS_Hadronic()

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
        layers.extend( (layer, self.data[layer])  for layer in self.hadronic_layers   if layer in self.data )
        
        #self._set_active_layers(include_ym=True)

        (self.den_tot,self.pre_tot,self.rho_tot,self.eps_tot,self.mub_tot,) = self._match_eos_layers(layers)
        if self.full_outputs:
            self._set_active_layers(include_ym=True)

            self.data_after_eos_construction = {layer: self._get_layer_data(layer)  for layer in self.active_layers}

        return self#(self.den_tot,self.pre_tot,self.rho_tot, self.eps_tot,        )
        
        
        
        
    def interpolate_at_pressure(self, pressure, nb, pb, rho, eps):

        valid = (np.isfinite(pb)  & np.isfinite(nb) & np.isfinite(rho)  & np.isfinite(eps)  & (pb > 0)   & (nb > 0)  & (rho > 0)  & (eps > 0) )

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

        

        nb_at_P = np.exp(CubicSpline(log_P, np.log(nb))(log_Pc)) # CubicSpline flacuates

        eps_at_P = np.exp(CubicSpline(log_P, np.log(eps))(log_Pc))
        rho_at_P = eps_at_P
        if not self.nuclear_unit:
            rho_at_P = rho_at_P/nuda.cst.c2_cgs        

        return nb_at_P, rho_at_P, eps_at_P 

        
        
        
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
        
        
        
        
    def update_layers(self, Pc, nH, rhoH, epsH):
        """Update background layers after a phase transition."""

        transition_layer = self._find_transition_layer(nH)
        self.transition_layer = transition_layer

        active_layers = []

        for layer in self.active_layers:

            den = getattr(self, f"den_{layer}", None)
            pre = getattr(self, f"pre_{layer}", None)
            rho = getattr(self, f"rho_{layer}", None)
            eps = getattr(self, f"eps_{layer}", None)

            if den is None or len(den) == 0:
                continue

            # Retain the background branch below the transition pressure.
            mask = pre <= Pc

            den = den[mask].copy()
            pre = pre[mask].copy()
            rho = rho[mask].copy()
            eps = eps[mask].copy()

            # Insert the hadronic-side critical point.
            if layer == transition_layer:
                den = np.append(den, nH)
                pre = np.append(pre, Pc)
                rho = np.append(rho, rhoH)
                eps = np.append(eps, epsH)

            # Remove layers that have no valid points remaining.
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

    
        self.active_layers = [layer for layer in layers
            if getattr(self, f"den_{layer}", None) is not None    ]
        
            
    
                
        
    def EoS_Hybrid(self, Method=None):
        """
        Construct a hybrid EoS by applying one QM phase transition        to the previously constructed background EoS.

        The background eos may be:     1. nucleoninc EoS      2. YM + hadronic EoS

        The background eos must be constructed before using this.
        """

        # --------------------------------------------------
        # 1. Identify the configured QM phase
        # --------------------------------------------------
        
        
        required = ("den_tot","pre_tot","rho_tot","eps_tot")

        if not all(hasattr(self, name) for name in required):
            raise RuntimeError(
                "The background EoS has not been constructed. "
                "Call EoS_Hadronic() or EoS_YM() first."
            )

        den_bg = np.asarray(self.den_tot).copy()
        pre_bg = np.asarray(self.pre_tot).copy()
        rho_bg = np.asarray(self.rho_tot).copy()
        eps_bg = np.asarray(self.eps_tot).copy()

        mub_bg = np.asarray(self.mub_tot).copy()
        
        
        
        
        valid_bg = den_bg >= self.den_sat

        den_H = den_bg[valid_bg]
        pre_H = pre_bg[valid_bg]
        rho_H = rho_bg[valid_bg]
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
            if qm_phase['model'] not in self.QMeos_functions :
                print(qm_phase['model'])
                raise KeyError('In valid function for QM. See avilable models model.self.QMeos_functions')
            parameters=qm_phase.get("parameters", {})
            
            self.den_critical_H = parameters['den_nuc_pt']
            self.delta_Den_pt =parameters['delta_den']
            alpha = parameters['alpha']
             
            if self.den_sat > self.den_critical_H:
                raise ("no phase transition below saturation density is allowed ")
            
            if max(den_H) < self.den_critical_H:
                raise ("The critical density is outside the density range ")
            
            
            self.Pre_critical_H = np.exp(CubicSpline(np.log(den_H), np.log(pre_H))(np.log(self.den_critical_H)))

            self.eps_critical_H = np.exp(CubicSpline(np.log(den_H), np.log(eps_H))(np.log(self.den_critical_H )))

            self.mu_critical = (self.Pre_critical_H + self.eps_critical_H ) /self.den_critical_H
            
            self.rho_critical_H = self.eps_critical_H 
            self.Pre_critical = self.Pre_critical_H
            

             
            
            
            parameters_for_eos = [self.den_critical_H ,self.eps_critical_H,self.Pre_critical_H,self.delta_Den_pt,alpha,self.mu_critical]
            
            eos_QM=nuda.eos.mix_phase_Classes.QM_linear(parameters_for_eos)
            
            eos_QM.liner_EoS()
            
            if not eos_QM.check_Qmlinear :
                print("fails to have a QM - linear EoS")
                return self#(self.den_tot,  self.pre_tot, self.rho_tot,  self.eps_tot )
                
            
            den_Q_branch = eos_QM.den_QM
            pre_Q_branch =  eos_QM.pre_QM
            rho_Q_branch =  eos_QM.eps_QM
            eps_Q_branch = eos_QM.eps_QM
            mu_Q_branch = eos_QM.mu_QM
            
            if not self.nuclear_unit:
                rho_Q_branch =rho_Q_branch/nuda.cst.c2_cgs
                
            self.den_critical_Q = den_Q_branch[0]
            self.rho_critical_Q =rho_Q_branch[0]
            self.eps_critical_Q = eps_Q_branch[0]
            
            self.delta_E= self.eps_critical_Q - self.eps_critical_H 
            
            
            den_M = np.linspace(self.den_critical_H+0.005*self.den_critical_H , self.den_critical_Q-0.005*self.den_critical_Q, 20)
            pre_M=np.zeros_like(den_M)+self.Pre_critical_H
            mu_M=np.zeros_like(den_M)+self.mu_critical
            eps_M= den_M*self.mu_critical-self.Pre_critical_H
            rho_M = eps_M.copy()

            # Convert energy density to mass density if using cgs units.
            if not self.nuclear_unit :
                
                rho_M = eps_M / nuda.cst.c2_cgs

            den_Q_branch  = np.concatenate((den_M, den_Q_branch ))
            pre_Q_branch = np.concatenate((pre_M, pre_Q_branch ))
            rho_Q_branch = np.concatenate((rho_M, rho_Q_branch ))
            eps_Q_branch = np.concatenate((eps_M, eps_Q_branch ))
            
        
        if qm_phase['source'] == 'file':
        
            if "data" not in qm_phase:
                raise RuntimeError( f"Data for QM phase '{phase_key}' have not been loaded.")

            values = qm_phase["data"]
            den_Q = np.asarray(values["den"])
            pre_Q = np.asarray(values["pre"])
            rho_Q = np.asarray(values["rho"])
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
            
            
                self.Pre_critical = np.exp(CubicSpline(np.log(den_H), np.log(pre_H))(np.log(self.den_critical_H )))

                self.eps_critical_H = np.exp(CubicSpline(np.log(den_H), np.log(eps_H))(np.log(self.den_critical_H )))

                self.mu_critical = (self.Pre_critical + self.eps_critical_H ) /self.den_critical_H
                
                self.rho_critical_H= self.eps_critical_H 
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
                self.Pre_critical = Maxwell.P_c
                
                
                
                #if method == 'Maxwell':
                Pc = self.Pre_critical

                nH, rhoH, epsH = self.interpolate_at_pressure(self.Pre_critical, den_H, pre_H, rho_H, eps_H)
                self.den_critical_H = nH
                self.rho_critical_H = rhoH
                self.eps_critical_H = epsH

                nQ, rhoQ, epsQ = self.interpolate_at_pressure(self.Pre_critical, den_Q, pre_Q, rho_Q, eps_Q)

                self.den_critical_Q = nQ
                self.rho_critical_Q = rhoQ
                self.eps_critical_Q = epsQ

    
                
                
                mask_Q = pre_Q > Pc

                den_Q_branch = den_Q[mask_Q]
                pre_Q_branch = pre_Q[mask_Q]
                rho_Q_branch = rho_Q[mask_Q]
                eps_Q_branch = eps_Q[mask_Q]

                # Insert the QM-side critical point.
                den_Q_branch = np.append(nQ, den_Q_branch)
                pre_Q_branch = np.append(Pc, pre_Q_branch)
                rho_Q_branch = np.append(rhoQ, rho_Q_branch)
                eps_Q_branch = np.append(epsQ, eps_Q_branch)

                # Ensure increasing density order.
                order = np.argsort(den_Q_branch)

                den_Q_branch = den_Q_branch[order]
                pre_Q_branch = pre_Q_branch[order]
                rho_Q_branch = rho_Q_branch[order]
                eps_Q_branch = eps_Q_branch[order]
                mub_Q_branch = (pre_Q_branch + eps_Q_branch ) / den_Q_branch
                
                if method == 'Maxwell':
                    self.Pre_critical_H= self.Pre_critical
                    
                    
                    if (self.den_critical_Q -self.den_critical_H) <=0.:
                        print("n_Q < n_H. \n")
                        print("Returning the hadronic EoS." )
                        return self
                    if (self.eps_critical_Q -self.eps_critical_H) <=0.:
                        print("E_Q < E_H. \n")
                        print("Returning the hadronic EoS." )
                        return self
                        
                    den_M = np.linspace(self.den_critical_H+0.005*self.den_critical_H , self.den_critical_Q-0.005*self.den_critical_Q, 20)
                    pre_M=np.zeros_like(den_M)+self.Pre_critical_H
                    mu_M=np.zeros_like(den_M)+self.mu_critical
                    eps_M= den_M*self.mu_critical-self.Pre_critical_H
                    rho_M = eps_M.copy()

                    # Convert energy density to mass density if using cgs units.
                    if not self.nuclear_unit :
                        rho_Q_branch  = rho_Q_branch / nuda.cst.c2_cgs
                        rho_M = eps_M / nuda.cst.c2_cgs

                    den_Q_branch  = np.concatenate((den_M, den_Q_branch ))
                    pre_Q_branch = np.concatenate((pre_M, pre_Q_branch ))
                    rho_Q_branch = np.concatenate((rho_M, rho_Q_branch ))
                    eps_Q_branch = np.concatenate((eps_M, eps_Q_branch ))
                    
                    
                
                if method == 'MIM':
                    valid_bg = ((den_bg >= self.den_sat) & (pre_bg < self.Pre_critical))

                    den_H = den_bg[valid_bg]
                    pre_H = pre_bg[valid_bg]
                    rho_H = rho_bg[valid_bg]
                    eps_H = eps_bg[valid_bg]
                    mub_H = mub_bg[valid_bg]
                    
                    den_H = np.append(den_H, self.den_critical_H)
                    pre_H = np.append(pre_H, self.Pre_critical)
                    eps_H = np.append(eps_H, self.eps_critical_H)
                    mub_H = np.append(mub_H, self.mu_critical)
                    
                
                    
                
                
                    core1_core2_layers = {'r1': {'pre': pre_H,'mub': mub_H,'den':den_H}, 'r2': {'pre': pre_Q_branch,'mub': mub_Q_branch,'den':den_Q_branch}}
                    MIM = nuda.eos.mix_phase_Classes.MixedInterpolatePhase(core1_core2_layers,muc=self.mu_critical,Pc=self.Pre_critical)
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
                    
                    self.Pre_critical_H= result_MIM['P_H']
                    self.den_critical_H= result_MIM['n_H']
                    self.mu_H= result_MIM['mu_H']
                    
                    self.eps_critical_H= self.mu_H * self.den_critical_H - self.Pre_critical
                    self.rho_critical_H=self.eps_critical_H
                
                    self.mu_Q= result_MIM['mu_Q']
                    self.Pre_critical_Q =  result_MIM['P_Q']
                    self.den_critical_Q = result_MIM['n_Q']
                    self.eps_critical_Q= self.mu_Q * self.den_critical_Q- self.Pre_critical_Q
                    self.rho_critical_Q=self.eps_critical_Q
                    
                    if not self.nuclear_unit :
                        self.rho_critical_H = self.rho_critical_H / nuda.cst.c2_cgs
                        self.rho_critical_Q = self.rho_critical_Q / nuda.cst.c2_cgs
                        
                    if (self.den_critical_Q -self.den_critical_H) <=0.:
                        return self
                    if (self.eps_critical_Q -self.eps_critical_H) <=0.:
                        return self
                    if (self.mu_Q -self.mu_H) <=0.:
                        return self
                    if (self.Pre_critical_Q -self.Pre_critical_H) <=0.:
                        return self
                    
                    
                    
                    
                    mask_quark = ((pre_Q > self.Pre_critical_Q) & (mub_Q > self.mu_Q) &  (den_Q >self.den_critical_Q))

               
                    den_quark = den_Q[mask_quark].copy()
                    pre_quark = pre_Q[mask_quark].copy()
                    rho_quark = eps_Q[mask_quark].copy()
                    eps_quark = eps_Q[mask_quark].copy()
                    mub_quark = mub_Q[mask_quark].copy()

                    mueval = np.linspace(self.mu_H+0.01*self.mu_H , self.mu_Q, 30)
                
                    

                    den_M, pre_M, eps_M = (MIM.Pre_MIM_den_MIM_and_eps_MIM(mueval, self.alpha1, self.alpha2))
                    den_M = np.asarray(den_M)
                    pre_M = np.asarray(pre_M)
                    eps_M = np.asarray(eps_M)
                    #print(den_M, pre_M, eps_M)

                    # Assumption: eps_M is in energy-density units.
                    rho_M = eps_M.copy()

                    # Convert energy density to mass density if using cgs units.
                    if not self.nuclear_unit :
                        rho_quark =rho_quark / nuda.cst.c2_cgs
                        rho_M = eps_M / nuda.cst.c2_cgs

                    den_Q_branch  = np.concatenate((den_M, den_quark))
                    pre_Q_branch= np.concatenate((pre_M, pre_quark))
                    rho_Q_branch = np.concatenate((rho_M, rho_quark))
                    eps_Q_branch = np.concatenate((eps_M, eps_quark))
                    #mub_quark = np.concatenate((mueval, mub_quark))
                    
                    order = np.argsort(den_Q_branch)

                    den_Q_branch = den_Q_branch[order]
                    pre_Q_branch = pre_Q_branch[order]
                    rho_Q_branch = rho_Q_branch[order]
                    eps_Q_branch = eps_Q_branch[order]
                        
                        

             
       
        if len(den_Q_branch) == 0 or len(pre_Q_branch) != len(den_Q_branch) or len(rho_Q_branch) != len(den_Q_branch) or len(eps_Q_branch) != len(den_Q_branch) :
            return self
        if not all(np.all(np.isfinite(arr)) for arr in [den_Q_branch, pre_Q_branch, rho_Q_branch, eps_Q_branch]):
            return self
        if any(np.any(arr <= 0.) for arr in [den_Q_branch, pre_Q_branch, rho_Q_branch, eps_Q_branch]):
            return self#(self.den_tot,  self.pre_tot, self.rho_tot,  self.eps_tot )
        
        
        
        
                   
        mask_H = ((pre_bg < self.Pre_critical_H) & (den_bg < self.den_critical_H) & (eps_bg < self.eps_critical_H) )

        den_H = den_bg[mask_H]
        pre_H = pre_bg[mask_H]
        rho_H = rho_bg[mask_H]
        eps_H = eps_bg[mask_H]
        
        den_H = np.append(den_H, self.den_critical_H)
        pre_H = np.append(pre_H, self.Pre_critical_H)
        rho_H = np.append(rho_H, self.rho_critical_H)
        eps_H = np.append(eps_H, self.eps_critical_H)
        
        self.den_tot = np.concatenate((den_H, den_Q_branch))
        self.pre_tot = np.concatenate((pre_H, pre_Q_branch))
        self.rho_tot = np.concatenate((rho_H, rho_Q_branch))
        self.eps_tot = np.concatenate((eps_H, eps_Q_branch))
        self.mub_tot = (self.pre_tot + self.eps_tot) / self.den_tot
        
        if not self.full_outputs :
            return self 
        if self.full_outputs :
            self.update_layers(self.Pre_critical_H, self.den_critical_H , self.rho_critical_H ,self.eps_critical_H )     
            

            qm_layer = f"inner_core_phase{qm_phase['phase_number']}"

            for quantity, array in (("den", den_Q_branch[den_Q_branch>=self.den_critical_Q]), ("pre", pre_Q_branch[den_Q_branch>=self.den_critical_Q]), 
            ("rho", rho_Q_branch[den_Q_branch>=self.den_critical_Q]), ("eps", eps_Q_branch[den_Q_branch>=self.den_critical_Q])):
                setattr(self, f"{quantity}_{qm_layer}", np.asarray(array).copy())

            # Update the quark layer's boundaries.
            self._update_layer_boundaries(qm_layer)
            layers = []
            for layer in reversed(self.active_layers):
                if layer != qm_layer and getattr(self, f"den_{layer}", None) is not None and len(getattr(self, f"den_{layer}")) > 0:
                    layers.append(qm_layer)
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


        
        """
        

        self.mub_tot = (self.eps_tot + self.pre_tot) / self.den_tot
        
        """

        return self# self.den_tot, self.pre_tot, self.rho_tot, self.eps_tot
        
             
        
    def Final_EoS(self):
        """Construct the final EoS based on the configured inner-core phases."""

        self.load_data()

        phases = sorted(self.inner_core_phases.values(),key=lambda phase: phase["phase_number"] )

        if len(phases) > 2:
            raise ValueError("maximum 2 inner-core phases are supported.")

        if not phases:
            return self.EoS_Hadronic()

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
            return self.EoS_YM()

        # QM only: construct the hadronic background first.
        if phase1_type == "QM" and phase2_type is None:
            self.EoS_Hadronic()
            return self.EoS_Hybrid()

        # YM followed by QM.
        if phase1_type == "YM" and phase2_type == "QM":
            self.EoS_YM()
            return self.EoS_Hybrid()
            
    def print_outputs( self ):
        """
        Method which print outputs on terminal's screen.
        """
        #
        if nuda.env.verb: print("Enter print_outputs()")
        self.Final_EoS()
        #
        print("- Print output:")
        print("eos_layers:",self.eos_layers)
        print("   Inner core models:\n  ")
        print([self.inner_core_phases[phase]['model'] for phase in self.inner_core_phases  if phase is not None])
        
        #if any(self.sm_den): print(f"   sm_den: {np.round(self.sm_den,3)} in {self.den_unit}")
        if self.den_tot is not None: print(f"   den: {np.round(self.den_tot,3)} in {self.den_unit}")
        if self.eps_tot is not None: print(f"   eps: {np.round(self.eps_tot,3)}in {self.eps_unit}")
        if self.pre_tot is not None: print(f"   pre: {np.round(self.pre_tot,3)}in {self.pre_unit}")
        #if self.cs2 is not None: print(f"   cs2: {np.round(self.cs2,2)}")
        #
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
        self.den_unit = 'g/cm^{3}$'
        self.eps_unit = 'erg/cm^{3}$'
        self.pre_unit = 'dyn/cm^{3}$'
        self.mub_unit = 'erg'
        self.den_sat = nuda.cst.nsat_cgs
        self.nuclear_unit =True
        
        if  self.nuclear_unit :
            self.den_sat = nuda.cst.nsat
            self.den_unit = 'fm$^{-3}$'
            self.eps_unit = 'MeV fm$^{-3}$'
            self.pre_unit = 'MeV fm$^{-3}$'
            self.mub_unit = 'MeV'
            
        self.layers = ["inner_core","outer_core", "inner_crust","outer_crust","atmosphere"]
        self.hadronic_layers = ["outer_core","inner_crust","outer_crust","atmosphere",]

        for layer in self.layers:
            setattr(self, f"den_{layer}", None)
            setattr(self, f"pre_{layer}", None)
            setattr(self, f"eps_{layer}", None)
            setattr(self, f"rho_{layer}", None)
        

                    
                
            
