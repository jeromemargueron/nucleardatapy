import numpy as np
from pathlib import Path
import numpy as np
from scipy.interpolate import interp1d
from scipy.optimize import minimize_scalar
from scipy.optimize import brentq
from scipy.optimize import bisect
from scipy.interpolate import interp1d
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import root
from scipy.optimize import least_squares
import numpy as np
from scipy.interpolate import PchipInterpolator
from scipy.integrate import cumulative_trapezoid
from pathlib import Path
from copy import deepcopy
#import mix_phase_Classes as PT_methods
#import constants as cst

import os
#os.system('python boundaries.py')
#os.system('sleep 0.001')

import nucleardatapy as nuda


with open("nuda.param.path_eos/dict_boundaries.txt", "r") as f:
    available_models = eval(f.read(), {"np": np})

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
           object.boundaries gives the bounadry of each region
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

    # =========================================================
    # Constants
    # =========================================================

    light_speed = nuda.cst.c * 1e2
    cgsP2MeVfm3 = 1./ nuda.cst.MeVfm32dyncm2
    g_cm3toMeVfm3 = 1./nuda.cst.MeVfm32gcm3 #5.6096e-13
    #cm3_to_fm3 = 1e39

    den_sat = nuda.cst.nsat # fm^-3

    # Ordinary hadronic layers
    regions = ["inner_core","outer_core", "inner_crust","outer_crust","atmosphere"]

    hadronic_regions = ["outer_core","inner_crust","outer_crust","atmosphere",]

    # =========================================================
    # Initialization
    # =========================================================

    def __init__(self,eos_object=None, data_dict=available_models, nuclear_unit=True,PT_Method_core=None):

        self.data_dict = ( available_models if data_dict is None else data_dict  )

        self.base_dir = Path(nuda.param.path_eos)
        self.nuclear_unit = nuclear_unit

        # Default EoS configuration
        self.default_eos = {
            "atmosphere": "1949-FMT",
            "outer_crust": "1971-BPS",
            "inner_crust": "1971-BPS",
            "outer_core": "1971-BPS-PNM",
            "inner_core": {},
        }

        self.eos = eos_object

        self.QMeos_functions = {"QM_linear":nuda.eos.mix_phase_Classes.QM_linear} ## currently only applicable to QM_linear

        
        self.models = {} ## For the hadronic regions
        self.files = {}  ## For the hadronic regions

        # Boundary information
        self.boundaries_from_data = {} ## For the hadronic regions
        self.boundaries = {}

       
        self.data = {} ## For the hadronic regions

        # Inner-core phase information
        self.inner_core_phases = {}

        # Phase-transition settings
        self.PT_Method= PT_Method_core
        if PT_Method_core is None:
            self.PT_Method = {"method": "Maxwell"}
        

        
        # Full EoS arrays
        self.den_tot = None
        self.eps_tot = None
        self.pre_tot = None
        self.rho_tot = None
        self.mub_tot = None

        # Individual layer arrays
        for region in self.regions:
            setattr(self, f"den_{region}", None)
            setattr(self, f"pre_{region}", None)
            setattr(self, f"eps_{region}", None)
            setattr(self, f"rho_{region}", None)

    # =========================================================
    # Sort and validate phase names
    # =========================================================

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

        eos_input = self.eos

        self.eos = deepcopy(self.default_eos)

        if eos_input is not None:

            if not isinstance(eos_input, dict):
                raise TypeError("eos_object must be a dictionary or None.")
            self.eos.update(eos_input)

        phases = self.eos.get("inner_core", {})  

        if phases == "" or phases == " ":
            phases = {}

        if not isinstance(phases, dict):
            raise TypeError("'inner_core' must be a dictionary of phases.")

        self.eos["inner_core"] = phases

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

    def identify_models(self):
        """
        Inner-core phases are identified separately in another function.
        """

        self.set_eos()
        if self.data_dict is None:
            raise ValueError("data_dict containing hadronic model information " )       

        for region in self.hadronic_regions:

            model_name = self.eos.get(region, "")

            # An empty model means that this layer is omitted.
            if not model_name:
                continue

            if region not in self.data_dict:
                raise KeyError(f"Region '{region}' is missing from data_dict." )

            available_region_models = self.data_dict[region]

            matching_files = []
            for filename in available_region_models:
                if Path(filename).stem.startswith(model_name):
                    matching_files.append(filename)
            if not matching_files:
                raise KeyError(f"Model '{model_name}' not found in region '{region}'.")

            filename = sorted(matching_files)[0]

            self.models[region] = {"model": model_name,"filename": filename,}

            model_data = available_region_models[filename]

            den = np.asarray(model_data["den"], dtype=float)
            pre = np.asarray(model_data["pre"], dtype=float)
            rho = np.asarray(model_data["rho"], dtype=float)

            if self.nuclear_unit:
                den = den / nuda.cst.cm3_to_fm3
                pre = pre * self.cgsP2MeVfm3
                rho = rho * self.g_cm3toMeVfm3

            self.boundaries_from_data[region] = {
                "den": den,
                "pre": pre,
                "rho": rho,
                "eps": rho.copy(),
            }

        # Identify inner-core phases.
        self.identify_inner_core_phases()

        return self

    # =========================================================
    # Identify inner-core phases
    # =========================================================

    def identify_inner_core_phases(self):
        """
        Identify each inner-core phase.
        If model matches a  function:
            source = "function"
        else:
            source = "file"
        """

        phases = self.eos.get("inner_core", {})

        

        sorted_phases = sorted(
            phases.items(),
            key=lambda item: self._phase_number(item[0]),
        )

        for phase_name, phase_info in sorted_phases:

            phase_type = phase_info["type"].upper()
            model_name = phase_info["model"]
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
                
                try:
                    filename = matching_files[0].name
                    model_boundaries = self.data_dict["inner_core"][phase_type][filename]
                    den = np.asarray(model_boundaries["den"], dtype=float)
                    pre = np.asarray(model_boundaries["pre"], dtype=float)
                    rho = np.asarray(model_boundaries["rho"], dtype=float)

                    if self.nuclear_unit:
                        den = den / nuda.cst.cm3_to_fm3
                        pre = pre * self.cgsP2MeVfm3
                        rho = rho * self.g_cm3toMeVfm3
                    region = f"inner_core_phase{phase_data['phase_number']}"

                    self.boundaries_from_data[region] = {
                        "den": den,
                        "pre": pre,
                        "rho": rho,
                        "eps": rho.copy(),
                    }
                except KeyError:
                    pass
                


            self.inner_core_phases[phase_name] = phase_data

        return self

    # =========================================================
    # Find selected files
    # =========================================================

    def find_files(self):
        """
        Find files for ordinary hadronic layers.

        Inner-core file paths are stored separately in
        self.inner_core_phases.
        """

        self.identify_models()

        
        for region, model_info in self.models.items():

            filepath = ( self.base_dir/ region/ model_info["filename"]   )

            if not filepath.is_file():
                raise FileNotFoundError(f"File not found: {filepath}")

            self.files[region] = filepath

        if not self.files and not self.inner_core_phases:
            raise RuntimeError("No EoS models were identified.")

        return self

    # =========================================================
    # Load a file-based EoS
    # =========================================================

    def _load_eos_file(self, filepath):
        """
        Load an EoS file with columns:

            rho : mass density [g/cm^3]
            pre : pressure [dyn/cm^2]
            den : baryon number density [cm^-3]

        Convert to nuclear units if nuclear_unit=True.
        """

        raw = np.loadtxt(filepath,usecols=(0, 1, 2),ndmin=2,)

        rho = raw[:, 0]
        pre = raw[:, 1]
        den = raw[:, 2]

        # Remove non-finite rows.
        valid = (np.isfinite(rho)& np.isfinite(pre)& np.isfinite(den))

        rho = rho[valid]
        pre = pre[valid]
        den = den[valid]

        # Require physically meaningful values.
        valid = ((rho > 0)& (pre >= 0)& (den > 0))

        rho = rho[valid]
        pre = pre[valid]
        den = den[valid]

        if den.size == 0:
            raise ValueError(f"No valid EoS rows found in {filepath}.")

        # Sort all arrays consistently by baryon density.
        order = np.argsort(den)

        rho = rho[order]
        pre = pre[order]
        den = den[order]

        # Energy density in CGS units.
        eps = rho * self.light_speed**2

        if self.nuclear_unit:

            den = den / nuda.cst.cm3_to_fm3
            pre = pre * self.cgsP2MeVfm3

            eps = rho * self.g_cm3toMeVfm3
            rho = rho * self.g_cm3toMeVfm3

        # Baryon chemical potential.
        mub = (eps + pre) / den

        return {"den": den.copy(),"pre": pre.copy(), "rho": rho.copy(),"eps": eps.copy(),"mub": mub.copy(),}

    # =========================================================
    # Evaluate a function-based EoS
    # =========================================================

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
            rho = eps / self.light_speed**2

        mub = (eps + pre) / den

        return {"den": den.copy(),"pre": pre.copy(),"rho": rho.copy(), "eps": eps.copy(), "mub": mub.copy()}

    # =========================================================
    # Load ordinary layers and inner-core phases
    # =========================================================

    def load_data(self):
        """
        Load all selected hadronic layers and inner-core phases.

        layers till outer core:
            self.data[region]

        Inner-core phase data:
            self.inner_core_phases[phase_name]["data"]
        """

        self.find_files()

        # -----------------------------------------------------
        # Load ordinary hadronic layers
        # -----------------------------------------------------

        self.data = {}

        for region, filepath in self.files.items():

            eos_data = self._load_eos_file(filepath)

            self.data[region] = eos_data

            # Preserve region-specific initial arrays.
            for key in ("den", "pre", "eps", "rho", "mub"):
                setattr(self,f"initial_{key}_{region}",eos_data[key].copy())

        # -----------------------------------------------------
        # Load inner-core phases
        # -----------------------------------------------------

        for phase_name, phase_info in self.inner_core_phases.items():

            if phase_info["source"] == "file":

                phase_data = self._load_eos_file(phase_info["filepath"])

            elif phase_info["source"] == "function":
                ## Not useful now
                #phase_data = self._evaluate_eos_function( phase_name,phase_info)
                continue


            else:
                raise ValueError(f"Unknown source '{phase_info['source']}' for phase '{phase_name}'.")
            phase_info["data"] = phase_data

        return self
        
        
    def _match_eos_regions(self, regions):
        """
        Match EoS regions .
        """

        den_all, pre_all, rho_all, eps_all = [], [], [], []

        # Reset matching information so repeated calls do not leave stale data.
        #self.boundaries = {}
        #self.boundaries_after_matching = {}

        previous_den = None
        previous_pre = None
        previous_eps = None

        # Reset regional attributes for regions being reconstructed.
        for region, _ in regions:
            for quantity in ("den", "pre", "rho", "eps", "mub"):
                setattr(self, f"{quantity}_{region}", None)

        for region, values in regions:

            den = np.asarray(values["den"])
            pre = np.asarray(values["pre"])
            rho = np.asarray(values["rho"])
            eps = np.asarray(values["eps"])
            mub = np.asarray(values["mub"])

            if len(den) == 0:
                continue

            # Sort in decreasing density order.
            order = np.argsort(den)[::-1]
            den, pre, rho, eps, mub = (arr[order] for arr in (den, pre, rho, eps, mub))

            # Apply matching conditions.
            if previous_den is not None:
                mask = ((den < previous_den) & (pre < previous_pre) & (eps < previous_eps))

                den, pre, rho, eps, mub = ( arr[mask] for arr in (den, pre, rho, eps, mub))

            if len(den) == 0:
                continue

            # Update the retained regional data.
            for quantity, array in (("den", den),("pre", pre),("rho", rho),("eps", eps),("mub", mub)):
                setattr(self, f"{quantity}_{region}", array.copy())

            # Update the boundaries after matching.
            boundary = {
                "den": np.array([den.min(), den.max()]),
                "pre": np.array([pre.min(), pre.max()]),
                "rho": np.array([rho.min(), rho.max()]),
                "eps": np.array([eps.min(), eps.max()]),
                "mub": np.array([mub.min(), mub.max()]),
            }

            self.boundaries[region] = boundary
            
            # Collect the retained data.
            den_all.append(den)
            pre_all.append(pre)
            rho_all.append(rho)
            eps_all.append(eps)

            # The next region must extend below the lowest retained point.
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
        
        
    def _set_active_regions(self, include_ym=False):
        """Set the valid regions from the constructed EoS. Currently works for nuclear and YM
        
         This is  just an internal function, latter being used to identify the phase transition regions        
        """

        regions = []

        if include_ym:
            phases = sorted(self.inner_core_phases.items(),key=lambda item: item[1]["phase_number"],)

            for _, phase in phases:
                if phase["type"].upper() == "YM":
                    regions.append(f"inner_core_phase{phase['phase_number']}")

        regions.extend(["outer_core","inner_crust","outer_crust","atmosphere",])

    
        self.active_regions = [region for region in regions
            if getattr(self, f"den_{region}", None) is not None    ]
        
    def EoS_Hadronic(self):
        """Construct the hadronic EoS through the outer core and crust."""

        self.load_data()

        regions = [(region, self.data[region]) for region in self.hadronic_regions if region in self.data ]
        
        
        

        self.den_tot, self.pre_tot, self.rho_tot, self.eps_tot, self.mub_tot = self._match_eos_regions(regions)

        #self.den_tot = self.den_had.copy()
        #self.pre_tot = self.pre_had.copy()
        #self.rho_tot = self.rho_had.copy()
        #self.eps_tot = self.eps_had.copy()
        #self.mub_tot = self.mub_had.copy()
        self._set_active_regions(include_ym=False)

        return self#(self.den_tot, self.pre_tot, self.rho_tot, self.eps_tot,)
        
    def EoS_YM(self):
        """Construct an EoS containing one or two YM phases."""

        self.load_data()
        
        

        phases = sorted(
            self.inner_core_phases.items(),
            key=lambda item: item[1]["phase_number"],
        )

        if not phases:
            return self.EoS_Hadronic()

        if len(phases) > 2:
            raise ValueError("At most two inner-core phases are currently supported." )

        #phases = [(phase_name, phase_info)
        #for phase_name, phase_info in phases
        #if phase_info["type"].upper() == "YM"]
        
        
        phases = sorted([
        (phase_name, phase_info)
        for phase_name, phase_info in self.inner_core_phases.items()
        if phase_info["type"].upper() == "YM"],
        key=lambda item: item[1]["phase_number"])
        

        # Inner-core phases first, ordered from innermost outward.
        regions = [
            (
                f"inner_core_phase{phase_info['phase_number']}",
                phase_info["data"],
            )
            for _, phase_info in phases
        ]

        # Continue from the outer core through the atmosphere.
        regions.extend( (region, self.data[region])  for region in self.hadronic_regions   if region in self.data )
        
        #self._set_active_regions(include_ym=True)

        (self.den_tot,self.pre_tot,self.rho_tot,self.eps_tot,self.mub_tot,) = self._match_eos_regions(regions)
        self._set_active_regions(include_ym=True)


        return self#(self.den_tot,self.pre_tot,self.rho_tot, self.eps_tot,        )
        
        
        
        
    def interpolate_at_pressure(self, pressure, nb, pb, rho, eps):

        valid = (np.isfinite(pb)  & np.isfinite(nb) & np.isfinite(rho)  & np.isfinite(eps)  & (pb > 0)   & (nb > 0)  & (rho > 0)  & (eps > 0) )

        pb = pb[valid]
        nb = nb[valid]
        rho = rho[valid]
        eps = eps[valid]

        order = np.argsort(pb)

        pb = pb[order]
        nb = nb[order]
        rho = rho[order]
        eps = eps[order]

        pb_unique, indices = np.unique(pb, return_index=True)

        nb = nb[indices]
        rho = rho[indices]
        eps = eps[indices]
        pb = pb_unique

        if not (pb[0] <= pressure <= pb[-1]):
            raise ValueError(  "Transition pressure lies outside the EoS pressure range."    )

        log_P = np.log(pb)
        log_Pc = np.log(pressure)

        

        nb_at_P = np.exp(CubicSpline(log_P, np.log(nb))(log_Pc)) # CubicSpline flacuates

        rho_at_P = np.exp(CubicSpline(log_P, np.log(rho))(log_Pc))

        eps_at_P = np.exp(CubicSpline(log_P, np.log(eps))(log_Pc))

        return nb_at_P, rho_at_P, eps_at_P 

        
        
        
    def _update_region_boundaries(self, region):
        """Update the boundaries of a regional EoS."""

        boundary = {}

        for quantity in ("den", "pre", "rho", "eps"):
            values = getattr(self, f"{quantity}_{region}", None)

            if values is None or len(values) == 0:
                boundary[quantity] = np.array([])
            else:
                boundary[quantity] = np.array([ np.min(values),   np.max(values) ])

        # Update regional chemical potential if available.
        den = getattr(self, f"den_{region}", None)
        pre = getattr(self, f"pre_{region}", None)
        eps = getattr(self, f"eps_{region}", None)

        if ( den is not None and pre is not None  and eps is not None  and len(den) > 0):
            setattr(self, f"mub_{region}", (eps + pre) / den)

            boundary["mub"] = np.array([np.min(getattr(self, f"mub_{region}")), np.max(getattr(self, f"mub_{region}"))])
        else:
            boundary["mub"] = np.array([])

        self.boundaries[region] = boundary
        
    def _find_transition_region(self, transition_density):
        """Find the active background region containing the transition."""
        #print(self.active_regions)

        for region in self.active_regions:
        
            ##attribute = f"den_{region}"

            #print(f"Region: {region}")
            #print(f"Attribute: {attribute}")
            #print(f"Exists: {hasattr(self, attribute)}")

            den = getattr(self, f"den_{region}", None)
            #print(f"Density: {den}\n")
            #den = getattr(self, f"den_{region}", None)
            #print(self.den_inner_crust)

            if den is None or len(den) == 0:
                continue

            if den.min() <= transition_density <= den.max():
                return region

        raise ValueError(f"Could not identify the region containing transition density n = {transition_density}.")
        
    def update_regions(self, Pc, nH, rhoH, epsH):
        """
        Update the background regions after a phase transition.

        The background branch is retained below Pc, and the
        background-side critical point is inserted into its region.
        """

        transition_region = self._find_transition_region(nH)
        self.transition_region = transition_region

        for region in self.active_regions:

            den = getattr(self, f"den_{region}", None)
            pre = getattr(self, f"pre_{region}", None)
            rho = getattr(self, f"rho_{region}", None)
            eps = getattr(self, f"eps_{region}", None)

            if den is None or len(den) == 0:
                continue

            # Keep the background branch below the transition pressure.
            mask = pre < Pc

            den = den[mask].copy()
            pre = pre[mask].copy()
            rho = rho[mask].copy()
            eps = eps[mask].copy()

            # Insert the background-side critical point into its region.
            if region == transition_region:
                den = np.append(den, nH)
                pre = np.append(pre, Pc)
                rho = np.append(rho, rhoH)
                eps = np.append(eps, epsH)

            # Keep each regional array ordered by increasing density.
            order = np.argsort(den)

            den = den[order]
            pre = pre[order]
            rho = rho[order]
            eps = eps[order]

            setattr(self, f"den_{region}", den)
            setattr(self, f"pre_{region}", pre)
            setattr(self, f"rho_{region}", rho)
            setattr(self, f"eps_{region}", eps)

            self._update_region_boundaries(region)

        return transition_region
                
        
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

        mub_bg = (eps_bg + pre_bg) / den_bg
        
        
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
            #print(parameters)
            
            self.den_critical_H = parameters['den_nuc_pt']
            self.delta_Den_pt =parameters['delta_den']
            alpha = parameters['alpha']
            
            #pre_of_den_H=Cubicspline(np.log(den_H),np.log(pre_H),extrapolate=)
            
            if self.den_sat > self.den_critical_H:
                raise ("no phase transition below saturation density is allowed ")
            
            if max(den_H) < self.den_critical_H:
                raise ("The critical density is outside the density range ")
            
            
            self.Pre_critical_H = np.exp(CubicSpline(np.log(den_H), np.log(pre_H))(np.log(self.den_critical_H)))

            self.eps_critical_H = np.exp(CubicSpline(np.log(den_H), np.log(eps_H))(np.log(self.den_critical_H )))

            self.mu_critical = (self.Pre_critical_H + self.eps_critical_H ) /self.den_critical_H
            
            self.rho_critical_H = self.eps_critical_H 
            

             
            
            
            parameters_for_eos = [self.den_critical_H ,self.eps_critical_H,self.Pre_critical_H,self.delta_Den_pt,alpha,self.mu_critical]
            
            eos_QM=nuda.eos.mix_phase_Classes.QM_linear(parameters_for_eos)
            
            eos_QM.liner_EoS()
            
            if not eos_QM.check_Qmlinear :
                print("fails")
                return self#(self.den_tot,  self.pre_tot, self.rho_tot,  self.eps_tot )
                
            
            den_Q_branch = eos_QM.den_QM
            pre_Q_branch =  eos_QM.pre_QM
            rho_Q_branch =  eos_QM.eps_QM
            eps_Q_branch = eos_QM.eps_QM
            mu_Q_branch = eos_QM.mu_QM
            
            if not self.nuclear_unit:
                rho_Q_branch =rho_Q_branch/self.speedoflight**2
                
            self.den_critical_Q = den_Q_branch[0]
            self.rho_critical_Q =rho_Q_branch[0]
            self.eps_critical_Q = eps_Q_branch[0]
            
            self.delta_E= self.eps_critical_Q - self.eps_critical_H 
            
        
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

            
            # Validate the phase-transition method
            if method not in ["Maxwell", "MIM", "tanH_Interp"]:
                raise KeyError(f"Invalid method for phase construction: {method}")

            # Method-specific parameters
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

                    return self#(self.den_tot,  self.pre_tot, self.rho_tot,  self.eps_tot )
     
            
                core1_core2_regions = {'r1': {'pre': pre_H,'mub': mub_H}, 'r2': {'pre': pre_Q,'mub': mub_Q}}
                Maxwell= nuda.eos.mix_phase_Classes.Maxwell_construction(core1_core2_regions)
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
                    
                
                    
                
                
                    core1_core2_regions = {'r1': {'pre': pre_H,'mub': mub_H,'den':den_H}, 'r2': {'pre': pre_Q_branch,'mub': mub_Q_branch,'den':den_Q_branch}}
                    MIM = nuda.eos.mix_phase_Classes.MixedInterpolatePhase(core1_core2_regions,muc=self.mu_critical,Pc=self.Pre_critical)
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
                        self.rho_critical_H = self.rho_critical_H / self.self.light_speed**2
                        self.rho_critical_Q = self.rho_critical_Q / self.self.light_speed**2
                        
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
                        rho_quark =rho_quark / self.light_speed**2
                        rho_M = eps_M / self.light_speed**2

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
                        
                        

            # Store the QM branch under its configured phase name.
            
       
        if len(den_Q_branch) == 0 or len(pre_Q_branch) != len(den_Q_branch) or len(rho_Q_branch) != len(den_Q_branch) or len(eps_Q_branch) != len(den_Q_branch) :
            return self
        if not all(np.all(np.isfinite(arr)) for arr in [den_Q_branch, pre_Q_branch, rho_Q_branch, eps_Q_branch]):
            return self
        if any(np.any(arr <= 0.) for arr in [den_Q_branch, pre_Q_branch, rho_Q_branch, eps_Q_branch]):
            return self#(self.den_tot,  self.pre_tot, self.rho_tot,  self.eps_tot )
        
        
        
        self.update_regions(self.Pre_critical_H, self.den_critical_H , self.rho_critical_H ,self.eps_critical_H )
        
        qm_region = f"inner_core_phase{qm_phase['phase_number']}"

        

        setattr(self, f"den_{qm_region}", den_Q_branch)
        setattr(self, f"pre_{qm_region}", pre_Q_branch)
        setattr(self, f"rho_{qm_region}", rho_Q_branch)
        setattr(self, f"eps_{qm_region}", eps_Q_branch)
        
        

        self._update_region_boundaries(qm_region)
        self.den_tot = np.concatenate([
            np.asarray(getattr(self, f"den_{region}"))
            for region in reversed(self.active_regions)
            if getattr(self, f"den_{region}", None) is not None
            and len(getattr(self, f"den_{region}")) > 0
        ] + [den_Q_branch])

        self.pre_tot = np.concatenate([
            np.asarray(getattr(self, f"pre_{region}"))
            for region in reversed(self.active_regions)
            if getattr(self, f"den_{region}", None) is not None
            and len(getattr(self, f"den_{region}")) > 0
        ] + [pre_Q_branch])

        self.rho_tot = np.concatenate([
            np.asarray(getattr(self, f"rho_{region}"))
            for region in reversed(self.active_regions)
            if getattr(self, f"den_{region}", None) is not None
            and len(getattr(self, f"den_{region}")) > 0
        ] + [rho_Q_branch])

        self.eps_tot = np.concatenate([
            np.asarray(getattr(self, f"eps_{region}"))
            for region in reversed(self.active_regions)
            if getattr(self, f"den_{region}", None) is not None
            and len(getattr(self, f"den_{region}")) > 0
        ] + [eps_Q_branch])

        self.mub_tot = (self.eps_tot + self.pre_tot) / self.den_tot

        return self# self.den_tot, self.pre_tot, self.rho_tot, self.eps_tot
        
             
        
    def Final_EoS(self):
        """Construct the final EoS based on the configured inner-core phases."""

        self.identify_models()

        phases = sorted(self.inner_core_phases.values(),key=lambda phase: phase["phase_number"] )

        if len(phases) > 2:
            raise ValueError("maximum 2 inner-core phases is supported.")

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

                    
                
            
