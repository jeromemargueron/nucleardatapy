import os
import sys
import numpy as np  # 1.15.0
from scipy.interpolate import CubicSpline

import nucleardatapy as nuda

class setupNEPStat_model():
    """
    Instantiate the object with results based on phenomenological\
    interactions and choosen by the toolkit practitioner. \
    This choice is defined in the variables `model` and `param`.

    :param model: Fix the name of model: 'Skyrme', 'GSkyrme', 'NLRH', \
    'DDRH', 'DDRHF'. Default value: 'Skyrme'.
    :type model: str, optional. 
    :param param: Fix the parameterization associated to model. \
    Default value: 'SLY5'.
    :type param: str, optional. 

    **Attributes:**
    """
    #
    def __init__( self, model = 'Skyrme' ):
        #
        if nuda.env.verb: print("\nEnter setupNEPStat_model()")
        #
        #: Attribute model.
        self.model = model
        if nuda.env.verb: print("model:",model)
        #print("-> model:",model)
        #
        self = setupNEPStat_model.init_self( self )
        #
        models, models_lower = nuda.matter.nep_models( )
        #
        if model.lower() not in models_lower:
            print('The model name ',model,' is not in the list of models.')
            print('list of models:',models)
            print('-- Exit the code --')
            exit()
        #
        params, params_lower = nuda.matter.nep_params( model = model )
        #
        self.params =params
        #
        for param in params:
            #
            print('param:',param)
            nep = nuda.matter.setupNEP( model = model, param = param )
            self.nep = nep.nep
            if nep.nep:
                if nep.nsat is not None: self.nsat.append( nep.nsat ); 
                if nep.Esat is not None: self.Esat.append( nep.Esat ); 
                if nep.Ksat is not None: self.Ksat.append( nep.Ksat ); 
                if nep.Qsat is not None: self.Qsat.append( nep.Qsat ); 
                if nep.Zsat is not None: self.Zsat.append( nep.Zsat ); 
                if nep.Esym is not None: self.Esym.append( nep.Esym ); 
                if nep.Lsym is not None: self.Lsym.append( nep.Lsym ); 
                if nep.Ksym is not None: self.Ksym.append( nep.Ksym ); 
                if nep.Qsym is not None: self.Qsym.append( nep.Qsym ); 
                if nep.Zsym is not None: self.Zsym.append( nep.Zsym ); 
                if nep.kappas is not None: self.kappas.append( nep.kappas ); 
                if nep.kappav is not None: self.kappav.append( nep.kappav ); 
                if nep.kappasat is not None: self.kappasat.append( nep.kappasat ); 
                if nep.kappasym is not None: self.kappasym.append( nep.kappasym ); 
                if nep.msat is not None: self.msat.append( nep.msat ); 
                if nep.Dmsat is not None: self.Dmsat.append( nep.Dmsat ); 
        #
        #  Compute statistical properties: centroids and standard distributions
        #
        if any(self.Esat): 
            self.Esat_mean = np.mean(self.Esat); self.Esat_std = np.std(self.Esat)
        else:
            self.Esat_mean = 0.0; self.Esat_std = 0.0
        if any(self.nsat): self.nsat_mean = np.mean(self.nsat); self.nsat_std = np.std(self.nsat)
        else:
            self.nsat_mean = 0.0; self.nsat_std = 0.0
        if any(self.Ksat): self.Ksat_mean = np.mean(self.Ksat); self.Ksat_std = np.std(self.Ksat)
        else:
            self.Ksat_mean = 0.0; self.Ksat_std = 0.0
        if any(self.Qsat): self.Qsat_mean = np.mean(self.Qsat); self.Qsat_std = np.std(self.Qsat)
        else:
            self.Qsat_mean = 0.0; self.Qsat_std = 0.0
        if any(self.Zsat): self.Zsat_mean = np.mean(self.Zsat); self.Zsat_std = np.std(self.Zsat)
        else:
            self.Zsat_mean = 0.0; self.Zsat_std = 0.0
        if any(self.Esym): self.Esym_mean = np.mean(self.Esym); self.Esym_std = np.std(self.Esym)
        else:
            self.Esym_mean = 0.0; self.Esym_std = 0.0
        if any(self.Lsym): self.Lsym_mean = np.mean(self.Lsym); self.Lsym_std = np.std(self.Lsym)
        else:
            self.Lsym_mean = 0.0; self.Lsym_std = 0.0
        if any(self.Ksym): self.Ksym_mean = np.mean(self.Ksym); self.Ksym_std = np.std(self.Ksym)
        else:
            self.Ksym_mean = 0.0; self.Ksym_std = 0.0
        if any(self.Qsym): self.Qsym_mean = np.mean(self.Qsym); self.Qsym_std = np.std(self.Qsym)
        else:
            self.Qsym_mean = 0.0; self.Qsym_std = 0.0
        if any(self.Zsym): self.Zsym_mean = np.mean(self.Zsym); self.Zsym_std = np.std(self.Zsym)
        else:
            self.Zsym_mean = 0.0; self.Zsym_std = 0.0
        if any(self.kappas): self.kappas_mean = np.mean(self.kappas); self.kappas_std = np.std(self.kappas)
        else:
            self.kappas_mean = 0.0; self.kappas_std = 0.0
        if any(self.kappav): self.kappav_mean = np.mean(self.kappav); self.kappav_std = np.std(self.kappav)
        else:
            self.kappav_mean = 0.0; self.kappav_std = 0.0
        if any(self.kappasat): self.kappasat_mean = np.mean(self.kappasat); self.kappasat_std = np.std(self.kappasat)
        else:
            self.kappasat_mean = 0.0; self.kappasat_std = 0.0
        if any(self.kappasym): self.kappasym_mean = np.mean(self.kappasym); self.kappasym_std = np.std(self.kappasym)
        else:
            self.kappasym_mean = 0.0; self.kappasym_std = 0.0
        if any(self.msat): self.msat_mean = np.mean(self.msat);   self.msat_std = np.std(self.msat)
        else:
            self.msat_mean = 0.0; self.msat_std = 0.0
        if any(self.Dmsat): self.Dmsat_mean = np.mean(self.Dmsat); self.Dmsat_std = np.std(self.Dmsat)
        else:
            self.Dmsat_mean = 0.0; self.Dmsat_std = 0.0
        #
        if nuda.env.verb: print("Exit SetupNEPStat_model()")
    #
    def print_outputs( self ):
        """
        Method which print outputs on terminal's screen.
        """
        print("")
        #
        if nuda.env.verb: print("Enter print_outputs()")
        #
        print("- Print output:")
        print("   model:",self.model)
        print(' NEP:')
        if any(self.Esat): print(f"   Esat: {np.round(self.Esat,2)}")
        if any(self.nsat): print(f"   nsat: {np.round(self.nsat,3)}")
        if any(self.Ksat): print(f"   Ksat: {np.round(self.Ksat,2)}")
        if any(self.Qsat): print(f"   Qsat: {np.round(self.Qsat,2)}")
        if any(self.Zsat): print(f"   Zsat: {np.round(self.Zsat,2)}")
        if any(self.Esym): print(f"   Esym: {np.round(self.Esym,2)}")
        if any(self.Lsym): print(f"   Lsym: {np.round(self.Lsym,2)}")
        if any(self.Ksym): print(f"   Ksym: {np.round(self.Ksym,2)}")
        if any(self.Qsym): print(f"   Qsym: {np.round(self.Qsym,2)}")
        if any(self.Zsym): print(f"   Zsym: {np.round(self.Zsym,2)}")
        if any(self.kappas): print(f"   kappas: {np.round(self.kappas,2)}")
        if any(self.kappav): print(f"   kappav: {np.round(self.kappav,2)}")
        if any(self.kappasat): print(f"   kappasat: {np.round(self.kappasat,2)}")
        if any(self.kappasym): print(f"   kappasym: {np.round(self.kappasym,2)}")
        if any(self.msat): print(f"   msat: {np.round(self.msat,2)}")
        if any(self.Dmsat): print(f"  Dmsat: {np.round(self.Dmsat,2)}")
        #
        if nuda.env.verb: print("Exit print_outputs()")
        #
    def print_latex( self ):
        """
        Method which print outputs on terminal's screen.
        """
        print("")
        #
        if nuda.env.verb: print("Enter print_latex()")
        #
        print("- Print latex:")
        print("   model:",self.model, len(self.params), self.params)
        print(' table:')
        print(r' NEP & $E_{\sat}$ & $n_{\sat}$ & $K_{\sat}$ & $Q_{\sat}$ & $Z_{\sat}$ &',
            r' $E_{sym}$ & $L_{sym}$ & $K_{sym}$ & $Q_{sym}$ & $Z_{sym}$ &',
            r' $m^*_{sat}/m$ & $\Delta m^*_{sat}/m$ \\\\')
        print(r' & MeV & fm$^{-3}n$ & MeV & MeV & MeV &',
            r' MeV & MeV & MeV & MeV & MeV &',
            r'  &  \\\\')
        print(rf' centroid & {self.Esat_mean:.2f} & {self.nsat_mean:.3f} &',
            rf' {self.Ksat_mean:.1f} & {self.Qsat_mean:.0f} & {self.Zsat_mean:.0f} &',
            rf' {self.Esym_mean:.2f} & {self.Lsym_mean:.1f} & {self.Ksym_mean:.0f} &',
            rf' {self.Qsym_mean:.0f} & {self.Zsym_mean:.0f} & {self.msat_mean:.2f} &',
            rf' {self.Dmsat_mean:.3f} \\\\')
        print(rf' std.dev. & {self.Esat_std:.2f} & {self.nsat_std:.3f} &',
            rf' {self.Ksat_std:.1f} & {self.Qsat_std:.0f} & {self.Zsat_std:.0f} &',
            rf' {self.Esym_std:.2f} & {self.Lsym_std:.1f} & {self.Ksym_std:.0f} &',
            rf' {self.Qsym_std:.0f} & {self.Zsym_std:.0f} & {self.msat_std:.2f} &',
            rf' {self.Dmsat_std:.3f} \\\\')
        #
        if nuda.env.verb: print("Exit print_latex()")
        #
    def init_self( self ):
        """
        Initialize variables in self.
        """
        #
        if nuda.env.verb: print("Enter init_self()")
        #
        #: Attribute the NEP.
        self.nsat = []; self.Esat = []; self.Ksat = []; self.Qsat = []; self.Zsat = []
        self.Esym = []; self.Lsym = []; self.Ksym = []; self.Qsym = []; self.Zsym = []
        self.kappas = []; self.kappav = []; self.kappasat = []; self.kappasym = []
        self.msat = []; self.Dmsat = [];
        self.nsat_mean = None; self.Esat_mean = None; self.Ksat_mean = None; self.Qsat_mean = None; self.Zsat_mean = None
        self.Esym_mean = None; self.Lsym_mean = None; self.Ksym_mean = None; self.Qsym_mean = None; self.Zsym_mean = None
        self.kappas_mean = None; self.kappav_mean = None; self.kappasat_mean = None; self.kappasym_mean = None
        self.msat_mean = None; self.Dmsat_mean = None;
        self.nsat_std = None; self.Esat_std = None; self.Ksat_std = None; self.Qsat_std = None; self.Zsat_std = None
        self.Esym_std = None; self.Lsym_std = None; self.Ksym_std = None; self.Qsym_std = None; self.Zsym_std = None
        self.kappas_std = None; self.kappav_std = None; self.kappasat_std = None; self.kappasym_std = None
        self.msat_std = None; self.Dmsat_std = None;
        #
        if nuda.env.verb: print("Exit init_self()")
        #
        return self
