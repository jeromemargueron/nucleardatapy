import os
import sys
import numpy as np  # 1.15.0
from scipy.interpolate import CubicSpline

import nucleardatapy as nuda

class setupNEPStat_models():
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
    def __init__( self, models = [ 'Skyrme' ] ):
        #
        if nuda.env.verb: print("\nEnter setupNEPStat_models()")
        #
        #: Attribute model.
        self.models = models
        if nuda.env.verb: print("models:",models)
        #
        self = setupNEPStat_models.init_self( self )
        #
        models_tmp, models_lower = nuda.matter.nep_models( )
        #
        for model in models:
            #
            if model.lower() not in models_lower:
                print('The model name ',model,' is not in the list of models.')
                print('list of models:',models)
                print('-- Exit the code --')
                exit()
            #
            dist = nuda.matter.setupNEPStat_model( model )
            #        
            if dist.nep:
                if dist.params: self.params.extend( dist.params ); 
                if dist.Esat: self.Esat.extend( dist.Esat ); 
                if dist.nsat: self.nsat.extend( dist.nsat ); 
                if dist.Ksat: self.Ksat.extend( dist.Ksat ); 
                if dist.Qsat: self.Qsat.extend( dist.Qsat ); 
                if dist.Zsat: self.Zsat.extend( dist.Zsat ); 
                if dist.Esym: self.Esym.extend( dist.Esym ); 
                if dist.Lsym: self.Lsym.extend( dist.Lsym ); 
                if dist.Ksym: self.Ksym.extend( dist.Ksym ); 
                if dist.Qsym: self.Qsym.extend( dist.Qsym ); 
                if dist.Zsym: self.Zsym.extend( dist.Zsym ); 
                if dist.kappas: self.kappas.extend( dist.kappas ); 
                if dist.kappav: self.kappav.extend( dist.kappav ); 
                if dist.kappasat: self.kappasat.extend( dist.kappasat ); 
                if dist.kappasym: self.kappasym.extend( dist.kappasym ); 
                if dist.msat: self.msat.extend( dist.msat ); 
                if dist.Dmsat: self.Dmsat.extend( dist.Dmsat ); 
        self.Esat = np.array( self.Esat, dtype = float )
        self.nsat = np.array( self.nsat, dtype = float )
        self.Ksat = np.array( self.Ksat, dtype = float )
        self.Qsat = np.array( self.Qsat, dtype = float )
        self.Zsat = np.array( self.Zsat, dtype = float )
        self.Esym = np.array( self.Esym, dtype = float )
        self.Lsym = np.array( self.Lsym, dtype = float )
        self.Ksym = np.array( self.Ksym, dtype = float )
        self.Qsym = np.array( self.Qsym, dtype = float )
        self.Zsym = np.array( self.Zsym, dtype = float )
        self.kappas = np.array( self.kappas, dtype = float )
        self.kappav = np.array( self.kappav, dtype = float )
        self.kappasat = np.array( self.kappasat, dtype = float )
        self.kappasym = np.array( self.kappasym, dtype = float )
        self.msat = np.array( self.msat, dtype = float )
        self.Dmsat = np.array( self.Dmsat, dtype = float )
        #
        #  Compute statistical properties: centroids and standard distributions
        #
        self.Esat_mean = np.mean(self.Esat); self.Esat_std = np.std(self.Esat)
        self.nsat_mean = np.mean(self.nsat); self.nsat_std = np.std(self.nsat)
        self.Ksat_mean = np.mean(self.Ksat); self.Ksat_std = np.std(self.Ksat)
        self.Qsat_mean = np.mean(self.Qsat); self.Qsat_std = np.std(self.Qsat)
        self.Zsat_mean = np.mean(self.Zsat); self.Zsat_std = np.std(self.Zsat)
        self.Esym_mean = np.mean(self.Esym); self.Esym_std = np.std(self.Esym)
        self.Lsym_mean = np.mean(self.Lsym); self.Lsym_std = np.std(self.Lsym)
        self.Ksym_mean = np.mean(self.Ksym); self.Ksym_std = np.std(self.Ksym)
        self.Qsym_mean = np.mean(self.Qsym); self.Qsym_std = np.std(self.Qsym)
        self.Zsym_mean = np.mean(self.Zsym); self.Zsym_std = np.std(self.Zsym)
        self.kappas_mean = np.mean(self.kappas); self.kappas_std = np.std(self.kappas)
        self.kappav_mean = np.mean(self.kappav); self.kappav_std = np.std(self.kappav)
        self.kappasat_mean = np.mean(self.kappasat); self.kappasat_std = np.std(self.kappasat)
        self.kappasym_mean = np.mean(self.kappasym); self.kappasym_std = np.std(self.kappasym)
        self.msat_mean = np.mean(self.msat);   self.msat_std = np.std(self.msat)
        self.Dmsat_mean = np.mean(self.Dmsat); self.Dmsat_std = np.std(self.Dmsat)
        #
        if nuda.env.verb: print("Exit SetupNEPStat_models()")
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
        print("   models:",self.models)
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
        if any(self.msat): print(f"   msat: {np.round(self.msat,2)}")
        if any(self.Dmsat): print(f"  Dmsat: {np.round(self.Dmsat,2)}")
        #
        print(f" Esat_mean: {self.Esat_mean:.2f} +- {self.Esat_std:.2f}")
        print(f" nsat_mean: {self.nsat_mean:.2f} +- {self.nsat_std:.2f}")
        print(f" Ksat_mean: {self.Ksat_mean:.1f} +- {self.Ksat_std:.1f}")
        print(f" Qsat_mean: {self.Qsat_mean:.0f} +- {self.Qsat_std:.0f}")
        print(f" Zsat_mean: {self.Zsat_mean:.0f} +- {self.Zsat_std:.0f}")
        print(f" Esym_mean: {self.Esym_mean:.2f} +- {self.Esym_std:.2f}")
        print(f" Lsym_mean: {self.Lsym_mean:.1f} +- {self.Lsym_std:.1f}")
        print(f" Ksym_mean: {self.Ksym_mean:.0f} +- {self.Ksym_std:.0f}")
        print(f" Qsym_mean: {self.Qsym_mean:.0f} +- {self.Qsym_std:.0f}")
        print(f" Zsym_mean: {self.Zsym_mean:.0f} +- {self.Zsym_std:.0f}")
        print(f" kappas_mean: {self.kappas_mean:.2f} +- {self.kappas_std:.2f}")
        print(f" kappav_mean: {self.kappav_mean:.2f} +- {self.kappav_std:.2f}")
        print(f" kappasat_mean: {self.kappasat_mean:.2f} +- {self.kappasat_std:.2f}")
        print(f" kappasym_mean: {self.kappasym_mean:.2f} +- {self.kappasym_std:.2f}")
        print(f" msat_mean: {self.msat_mean:.2f} +- {self.msat_std:.2f}")
        print(f" Dmsat_mean: {self.Dmsat_mean:.2f} +- {self.Dmsat_std:.2f}")
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
        print("   models:", len(self.models), self.models, len(self.params))
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
        self.params = []
        self.nsat = []; self.Esat = []; self.Ksat = []; self.Qsat = []; self.Zsat = []
        self.Esym = []; self.Lsym = []; self.Ksym = []; self.Qsym = []; self.Zsym = []
        self.kappas = []; self.kappav = []; self.kappasat = []; self.kappasym = []
        self.msat = []; self.Dmsat = []; 
        #
        if nuda.env.verb: print("Exit init_self()")
        #
        return self
