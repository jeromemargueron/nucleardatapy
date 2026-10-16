import math
import numpy as np  # 1.15.0
from scipy.interpolate import CubicSpline

import nucleardatapy as nuda


def denCC_emp(nsat, Esym, Lsym, Ksym, Qsym, emp):
    varEsym = Esym / 30.0
    varLsym = Lsym / 70.0
    den_cc = 0.0
    pre_cc = 0.0
    x01 = (0.1 - nsat) / (3.0 * nsat)
    if emp == "Simple":
        den_cc = 0.5 * nsat
    elif emp == "Ducoin":
        den_cc = 0.0802 + 0.000323 * (Lsym + 0.426 * Ksym + (Ksym + 0.426 * Qsym) * x01)
        pre_cc = -0.328 + 0.00959 * (Lsym - 0.343 * Ksym + (Ksym - 0.343 * Qsym) * x01)
    elif emp == "Newton":
        den_cc = (varEsym) * (0.135 - 0.098 * varLsym + 0.026 * varLsym**2)
        pre_cc = -0.724 + 0.0157 * (
            Lsym - 0.343 * Ksym**2 + (1 - 2 * 0.343 * Qsym) * x01 * Ksym
        )
    elif emp == "Steiner":
        den_cc = (varEsym) * (0.1327 - 0.0898 * varLsym + 0.0228 * varLsym**2)
    else:
        print("setupCC, denCC_emp: `emp` is badly defined ", emp)
        print("setupCC, denCC_emp: exit")
        exit()
    return den_cc, pre_cc  # in fm-3 and MeV fm-3


class setupCC:
    """
    Instantiate the object with a full EoS for the crust and the core of neutron stars.

    :param crust_model: Fix the name of model for the crust. Default value: '1998-VAR-AM-APR'.
    :type crust_model: str, optional.
    :param core_model: Fix the name of model. Default value: '1998-VAR-AM-APR'.
    :type core_model: str, optional.
    :param core_param: Fix the name of model. Default value: None.
    :type core_param: str, optional.
    :param core_kind: chose between 'micro' (default) and 'pheno'.
    :type core_kind: str, optional.
    :param connect: choose between 'density' in fm-3 (default), 'epsilon' in MeV fm-3 or 'pressure' in MeV fm-3.
    :type connect: str, optional.
    :param boundaries: list [ b_down, b_up ] containing the boundaries for the connection.
    :type boundaries: list, optional.
    :param emp: choose between different empirical formulae to localise the crust-core transition: None (default) in case of no use of empirical relations, 'simple' for the simple one and 'Steiner' for the empirical relation suggested by A. Steiner. note that if `emp' is taken to be another value that None, this choice will be considered above the boundary limits given in `boundary`.
    :type emp: str, optional.

    **Attributes:**
    """

    #
    def __init__(
        self,
        crust_model,
        core_model="1998-VAR-AM-APR",
        core_param=None,
        core_kind="micro",
        connect="density",
        boundaries=[0.016, 0.16],
        emp=None,
    ):
        """
        Parameters
        ----------
        core_model : str, optional
        The model to consider. Choose between: 1998-VAR-AM-APR (default), 2008-AFDMC-NM, ...
        core_kind : chose between 'micro' or 'pheno'.
        """
        #
        if nuda.env.verb:
            print("Enter setupCC()")
        #
        #: Attribute models.
        self.crust_model = crust_model
        self.core_model = core_model
        if nuda.env.verb:
            print("crust_model:", crust_model)
        if nuda.env.verb:
            print("core_model:", core_model)
        #
        self = setupCC.init_self(self)
        #
        if core_param is not None:
            self.label = connect
            # self.label = crust_model+' '+core_model+' '+core_param+' '+connect
        else:
            self.label = connect
            # self.label = crust_model+' '+core_model+' '+connect
        self.every = 1
        self.linestyle = "solid"
        self.marker = "o"
        #
        # Fixes the crust EoS
        #
        crust_models, crust_models_lower = nuda.crust.crust_models()
        #
        if crust_model.lower() not in crust_models_lower:
            print(
                "setupCC.py: The crust_model name ",
                crust_model,
                " is not in the list of models.",
            )
            print("setupCC.py: list of models:", crust_models)
            print("setupCC.py: -- Exit the code --")
            exit()
        #
        crust_eos = nuda.crust.setupCrust(model=crust_model)
        if nuda.env.verb_output:
            crust_eos.print_outputs()
        #
        # Fixes the core EoS at beta-equilibrium
        #
        if core_kind == "micro":
            models, models_lower = nuda.matter.micro_esym_models()
            models.remove("1998-VAR-AM-APR-fit")
            models_lower.remove("1998-var-am-apr-fit")
        elif core_kind == "pheno":
            models, models_lower = nuda.matter.pheno_esym_models()
        #
        if core_model.lower() not in models_lower:
            print(
                "setupCC.py: The core_model name ",
                core_model,
                " is not in the list of models.",
            )
            print("setupCC.py: list of models:", models)
            print("setupCC.py: -- Exit the code --")
            exit()
        #
        core_eos = nuda.eos.setupAMBeq(
            model=core_model, param=core_param, kind=core_kind
        )
        if nuda.env.verb_output:
            core_eos.print_outputs()
        #
        print("crust:")
        print("densities:", crust_eos.den)
        print("eps:", crust_eos.eps_tot)
        print("pre:", crust_eos.pre_tot)
        print("cs2", crust_eos.cs2_tot)
        print("core:")
        print("densities:", core_eos.den)
        print("eps:", core_eos.eps_tot)
        print("pre:", core_eos.pre_tot)
        print("cs2", core_eos.cs2_tot)
        #
        # connects crust and core, depending on the variable `connect`:
        #
        eos_den = []
        eos_eps = []
        eos_pre = []
        eos_cs2 = []
        corx_den = []
        corx_eps = []
        corx_pre = []
        corx_cs2 = []
        crux_den = []
        crux_eps = []
        crux_pre = []
        crux_cs2 = []
        #
        print("CC connection:")
        if connect == "density":
            #
            print("density")
            #
            if emp is not None:
                nsat = crust_eos.nsat
                Esym = crust_eos.Esym
                Lsym = crust_eos.Lsym
                Ksym = crust_eos.Ksym
                Qsym = crust_eos.Qsym
                # print('crust NEP:',nsat,Esym,Lsym)
                # opens a small gap -+20% of the empirical density
                b_lo = 0.8 * denCC_emp(nsat, Esym, Lsym, Ksym, Qsym, emp)[0]
                b_up = 1.2 * b_lo / 0.8
            else:
                b_lo = boundaries[0]
                b_up = boundaries[1]
            print("Boundaries:", b_lo, b_up)
            for ind, den in enumerate(crust_eos.den):
                if den < b_lo:
                    eos_den.append(den)
                    eos_eps.append(crust_eos.eps_tot[ind])
                    eos_pre.append(crust_eos.pre_tot[ind])
                    eos_cs2.append(crust_eos.cs2_tot[ind])
                else:
                    crux_den.append(den)
                    crux_eps.append(crust_eos.eps_tot[ind])
                    crux_pre.append(crust_eos.pre_tot[ind])
                    crux_cs2.append(crust_eos.cs2_tot[ind])
            for ind, den in enumerate(core_eos.den):
                if den > b_up:
                    eos_den.append(den)
                    eos_eps.append(core_eos.eps_tot[ind])
                    eos_pre.append(core_eos.pre_tot[ind])
                    eos_cs2.append(core_eos.cs2_tot[ind])
                else:
                    corx_den.append(den)
                    corx_eps.append(core_eos.eps_tot[ind])
                    corx_pre.append(core_eos.pre_tot[ind])
                    corx_cs2.append(core_eos.cs2_tot[ind])
            #
        elif connect == "epsilon":
            #
            print("epsilon")
            #
            b_lo = boundaries[0]
            b_up = boundaries[1]
            print("Boundaries:", b_lo, b_up)
            for ind, eps in enumerate(crust_eos.eps_tot):
                if eps < b_lo:
                    eos_den.append(crust_eos.den[ind])
                    eos_eps.append(eps)
                    eos_pre.append(crust_eos.pre_tot[ind])
                    eos_cs2.append(crust_eos.cs2_tot[ind])
                else:
                    crux_den.append(crust_eos.den[ind])
                    crux_eps.append(eps)
                    crux_pre.append(crust_eos.pre_tot[ind])
                    crux_cs2.append(crust_eos.cs2_tot[ind])
            for ind, eps in enumerate(core_eos.eps_tot):
                if eps > b_up:
                    eos_den.append(core_eos.den[ind])
                    eos_eps.append(eps)
                    eos_pre.append(core_eos.pre_tot[ind])
                    eos_cs2.append(core_eos.cs2_tot[ind])
                else:
                    corx_den.append(core_eos.den[ind])
                    corx_eps.append(eps)
                    corx_pre.append(core_eos.pre_tot[ind])
                    corx_cs2.append(core_eos.cs2_tot[ind])
            #
        elif connect == "pressure":
            #
            print("pressure")
            #
            b_lo = boundaries[0]
            b_up = boundaries[1]
            print("Boundaries:", b_lo, b_up)
            for ind, pre in enumerate(crust_eos.pre_tot):
                if pre < b_lo:
                    eos_den.append(crust_eos.den[ind])
                    eos_eps.append(crust_eos.eps_tot[ind])
                    eos_pre.append(pre)
                    eos_cs2.append(crust_eos.cs2_tot[ind])
                else:
                    crux_den.append(crust_eos.den[ind])
                    crux_eps.append(crust_eos.eps_tot[ind])
                    crux_pre.append(pre)
                    crux_cs2.append(crust_eos.cs2_tot[ind])
            for ind, pre in enumerate(core_eos.pre_tot):
                if pre > b_up:
                    eos_den.append(core_eos.den[ind])
                    eos_eps.append(core_eos.eps_tot[ind])
                    eos_pre.append(pre)
                    eos_cs2.append(core_eos.cs2_tot[ind])
                else:
                    corx_den.append(core_eos.den[ind])
                    corx_eps.append(core_eos.eps_tot[ind])
                    corx_pre.append(pre)
                    corx_cs2.append(core_eos.cs2_tot[ind])
            #
        else:
            print("setupCC.py: Issue with the connection.")
            print("setupCC.py: connect:", connect)
            print("setupCC.py: -- Exit the code --")
            exit()
        self.crust_den = np.array(crust_eos.den)
        self.crust_pre = np.array(crust_eos.pre_tot)
        self.crust_eps = np.array(crust_eos.eps_tot)
        self.crust_cs2 = np.array(crust_eos.cs2_tot)
        self.core_den = np.array(core_eos.den)
        self.core_pre = np.array(core_eos.pre_tot)
        self.core_eps = np.array(core_eos.eps_tot)
        self.core_cs2 = np.array(core_eos.cs2_tot)
        self.crux_den = np.array(crux_den)
        self.crux_pre = np.array(crux_pre)
        self.crux_eps = np.array(crux_eps)
        self.crux_cs2 = np.array(crux_cs2)
        self.corx_den = np.array(corx_den)
        self.corx_pre = np.array(corx_pre)
        self.corx_eps = np.array(corx_eps)
        self.corx_cs2 = np.array(corx_cs2)
        #
        # perform a simple linear interpolation in log-log scale
        #
        log_den = np.log10(eos_den)
        log_eps = np.log10(eos_eps)
        log_pre = np.log10(eos_pre)
        log_cs2 = np.log10(eos_cs2)
        #
        if connect == "density":
            #
            x = log_den
            ye = log_eps
            yp = log_pre
            yc = log_cs2
            # fix the density mesh for the output eos
            print("min(den):", min(eos_den), min(log_den))
            print("max(den):", max(eos_den), max(log_den))
            eos_x = np.logspace(min(log_den), max(log_den), num=100)
            log_x = np.log10(eos_x)
            #
            print("eos_x:", eos_x)
            print("log_x:", log_x)
            # cs_eps = CubicSpline(x, ye)
            # cs_pre = CubicSpline(x, yp)
            # cs_cs2 = CubicSpline(x, yc)
            # cs_cs2_beta = CubicSpline(ye, yp)
            self.den = eos_x
            # self.eps = np.power(10,cs_eps(log_x))
            # self.pre = np.power(10,cs_pre(log_x))
            # self.cs2 = np.power(10,cs_cs2(log_x))
            # self.cs2_beta = self.pre / self.eps * np.power(10,cs_cs2_beta( self.eps, 1 ) ) # to improve...
            # linear interpolation in log-log scale
            self.eps = np.power(10, np.interp(log_x, x, ye))
            self.pre = np.power(10, np.interp(log_x, x, yp))
            self.cs2 = np.power(10, np.interp(log_x, x, yc))
            #
        elif connect == "epsilon":
            #
            yn = log_den
            x = log_eps
            yp = log_pre
            yc = log_cs2
            # fix the density mesh for the output eos
            print("min(eps):", min(eos_eps), min(log_eps))
            print("max(eps):", max(eos_eps), max(log_eps))
            eos_x = np.logspace(min(log_eps), max(log_eps), num=100)
            log_x = np.log10(eos_x)
            self.den = np.power(10, np.interp(log_x, x, yn))
            self.eps = eos_x
            self.pre = np.power(10, np.interp(log_x, x, yp))
            self.cs2 = np.power(10, np.interp(log_x, x, yc))
            #
        elif connect == "pressure":
            #
            yn = log_den
            ye = log_eps
            x = log_pre
            yc = log_cs2
            # fix the density mesh for the output eos
            print("min(pre):", min(eos_pre), min(log_pre))
            print("max(pre):", max(eos_pre), max(log_pre))
            eos_x = np.logspace(min(log_pre), max(log_pre), num=100)
            log_x = np.log10(eos_x)
            self.den = np.power(10, np.interp(log_x, x, yn))
            self.eps = np.power(10, np.interp(log_x, x, ye))
            self.pre = eos_x
            self.cs2 = np.power(10, np.interp(log_x, x, yc))
            #
        self.den_unit = "fm$^{-3}$"
        self.e2a_unit = "MeV"
        self.eps_unit = "MeV fm$^{-3}$"
        self.pre_unit = "MeV fm$^{-3}$"
        #
        if nuda.env.verb:
            print("Exit setupCC()")
        #

    def print_outputs(self):
        """
        Method which print outputs on terminal's screen.
        """
        #
        if nuda.env.verb:
            print("Enter print_outputs()")
        #
        print("- Print output:")
        print("   model:", self.model)
        print("   ref:  ", self.ref)
        print("   label:", self.label)
        print("   note: ", self.note)
        # if any(self.sm_den): print(f"   sm_den: {np.round(self.sm_den,3)} in {self.den_unit}")
        if self.den is not None:
            print(f"   den: {np.round(self.den,3)} in {self.den_unit}")
        if self.e2a is not None:
            print(f"   e2a: {np.round(self.e2a,3)} in {self.e2a_unit}")
        if self.eps is not None:
            print(f"   eps: {np.round(self.eps,3)} in {self.eps_unit}")
        if self.pre is not None:
            print(f"   pre: {np.round(self.pre,3)} in {self.pre_unit}")
        if self.cs2 is not None:
            print(f"   cs2: {np.round(self.cs2,2)}")
        #
        if nuda.env.verb:
            print("Exit print_outputs()")
        #

    def init_self(self):
        """
        Initialize variables in self.
        """
        #
        if nuda.env.verb:
            print("Enter init_self()")
        #
        #: Attribute providing the full reference to the paper to be citted.
        self.ref = ""
        #: Attribute providing additional notes about the data.
        self.note = ""
        #: Attribute the matter density.
        self.den = None
        #: Attribute the total energy density.
        self.eps = None
        #: Attribute the pressure.
        self.pre = None
        #: Attribute the sound speed.
        self.cs2 = None
        #: Attribute the sound speed at beta-equilibrium
        self.cs2_beta = None
        #: Attribute the plot linestyle.
        self.linestyle = None
        #: Attribute the plot label data.
        self.label = ""
        #: Attribute the plot marker.
        self.marker = None
        #: Attribute the plot every data.
        self.every = 1
        #
        if nuda.env.verb:
            print("Exit init_self()")
        #
        return self
