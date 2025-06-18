import math
import numpy as np  # 1.15.0
from scipy.interpolate import CubicSpline

import nucleardatapy as nuda

class setupCC():
    """
    Instantiate the object with microscopic results choosen \
    by the toolkit practitioner.

    :param model: Fix the name of model. Default value: '1998-VAR-AM-APR'.
    :type model: str, optional. 
    :param kind: chose between 'micro' and 'pheno'.
    :type kind: str, optional.

    **Attributes:**
    """
    #
    def __init__( self, crust_model, core_model = '1998-VAR-AM-APR', core_param = None, core_kind = 'micro', connect = 'density', boundaries = [ 0.016, 0.16 ] ):
        """
        Parameters
        ----------
        core_model : str, optional
        The model to consider. Choose between: 1998-VAR-AM-APR (default), 2008-AFDMC-NM, ...
        core_kind : chose between 'micro' or 'pheno'.
        """
        #
        if nuda.env.verb: print("Enter setupCC()")
        #
        #: Attribute models.
        self.crust_model = crust_model
        self.core_model = core_model
        if nuda.env.verb: print("crust_model:",crust_model)
        if nuda.env.verb: print("core_model:",core_model)
        #
        self = setupCC.init_self( self )
        #
        if core_param is not None:
            self.label = crust_model+' '+core_model+' '+core_param+' '+connect
        else:
            self.label = crust_model+' '+core_model+' '+connect
        self.every = 1
        self.linestyle = 'solid'
        self.marker = 'o'
        #
        # Fixes the crust EoS
        #
        crust_models, crust_models_lower = nuda.crust.crust_models()
        #
        if crust_model.lower() not in crust_models_lower:
            print('setupCC.py: The crust_model name ',crust_model,' is not in the list of models.')
            print('setupCC.py: list of models:',crust_models)
            print('setupCC.py: -- Exit the code --')
            exit()
        #
        crust_eos = nuda.crust.setupCrust( model = crust_model )
        if nuda.env.verb_output: crust_eos.print_outputs( )
        #
        # Fixes the core EoS at beta-equilibrium
        #
        if core_kind == 'micro':
            models, models_lower = nuda.matter.micro_esym_models()
            models.remove('1998-VAR-AM-APR-fit')
            models_lower.remove('1998-var-am-apr-fit')
        elif core_kind == 'pheno':
            models, models_lower = nuda.matter.pheno_esym_models()
        #
        if core_model.lower() not in models_lower:
            print('setupCC.py: The core_model name ',core_model,' is not in the list of models.')
            print('setupCC.py: list of models:',models)
            print('setupCC.py: -- Exit the code --')
            exit()
        #
        core_eos = nuda.eos.setupAMBeq( model = core_model, param = core_param, kind=core_kind )
        if nuda.env.verb_output: core_eos.print_outputs( )
        #
        print('crust:')
        print('densities:',crust_eos.den)
        print('eps:',crust_eos.eps_tot)
        print('pre:',crust_eos.pre_tot)
        print('cs2',crust_eos.cs2_tot)
        print('core:')
        print('densities:',core_eos.den)
        print('eps:',core_eos.eps_tot)
        print('pre:',core_eos.pre_tot)
        print('cs2',core_eos.cs2_tot)
        #
        # connects crust and core, depending on the variable `connect`:
        #
        eos_den = []
        eos_eps = []
        eos_pre = []
        eos_cs2 = []
        #
        if connect == 'density' or connect == 'steiner' :
            #
            if connect == 'steiner':
                #nep = nuda.matter.setupNEP( model = ’ddrhf’ , param = ’pka1’ )
                #nep=nuda.matter.setupNEP( model = crust_model, )
                Esym = 32.0
                Lsym = 50.0
                tmp = Lsym/70.0
                b_lo = (Esym/30.0)*(0.1327 - 0.0898*tmp + 0.0228*tmp**2)
                b_up=b_lo
            else:
                b_lo = boundaries[0]
                b_up = boundaries[1]
            print('Boundaries:',b_lo,b_up)
            for ind,den in enumerate(crust_eos.den):
                if den < b_lo:
                    eos_den.append( den )
                    eos_eps.append( crust_eos.eps_tot[ind] )
                    eos_pre.append( crust_eos.pre_tot[ind] )
                    eos_cs2.append( crust_eos.cs2_tot[ind] )
            for ind,den in enumerate(core_eos.den):
                if den > b_up:
                    eos_den.append( den )
                    eos_eps.append( core_eos.eps_tot[ind] )
                    eos_pre.append( core_eos.pre_tot[ind] )
                    eos_cs2.append( core_eos.cs2_tot[ind] )
            #
#        elif connect == 'epsilon':


#        elif connect == 'pressure':


        else:
            print('setupCC.py: Issue with the connection.')
            print('setupCC.py: connect:',connect)
            print('setupCC.py: -- Exit the code --')
            exit()
        self.crust_den = crust_eos.den
        self.crust_pre = crust_eos.pre_tot
        self.crust_eps = crust_eos.eps_tot
        self.core_den = core_eos.den
        self.core_pre = core_eos.pre_tot
        self.core_eps = core_eos.eps_tot
        #print('CC eos:')
        #print('densities:',eos_den)
        #print('eps:',eos_eps)
        #print('pre:',eos_pre)
        #print('cs2',eos_cs2)
        #eos_den = np.array( eos_den, dtype = float )
        #eos_eps = np.array( eos_eps, dtype = float )
        #eos_pre = np.array( eos_pre, dtype = float )
        #eos_cs2 = np.array( eos_cs2, dtype = float )
        #
        # perform a spline interpolation in log-log scale
        #
        log_den = np.log10( eos_den )
        log_eps = np.log10( eos_eps )
        log_pre = np.log10( eos_pre )
        log_cs2 = np.log10( eos_cs2 )
        #
        if connect == 'density' or connect == 'steiner' :
            x = log_den
            ye = log_eps
            yp = log_pre
            yc = log_cs2
            # fix the density mesh for the output eos
            eos_x = np.logspace( min(log_den), max(log_den), num = 100 )
            log_x = np.log10( eos_x )
            #
        print('min(den):',min(eos_den),min(log_den))
        print('max(den):',max(eos_den),max(log_den))
        print('eos_x:',eos_x)
        print('log_x:',log_x)
        cs_eps = CubicSpline(x, ye)
        cs_pre = CubicSpline(x, yp)
        cs_cs2 = CubicSpline(x, yc)
        cs_cs2_beta = CubicSpline(ye, yp)
        self.den = eos_x
        self.eps = np.power(10,cs_eps(log_x))
        self.pre = np.power(10,cs_pre(log_x))
        self.cs2 = np.power(10,cs_cs2(log_x))
        self.cs2_beta = self.pre / self.eps * np.power(10,cs_cs2_beta( self.eps, 1 ) ) # to improve...
        #
        self.den_unit = 'fm$^{-3}$'
        self.e2a_unit = 'MeV'
        self.eps_unit = 'MeV fm$^{-3}$'
        self.pre_unit = 'MeV fm$^{-3}$'
        #
        if nuda.env.verb: print("Exit setupCC()")
        #
    def print_outputs( self ):
        """
        Method which print outputs on terminal's screen.
        """
        #
        if nuda.env.verb: print("Enter print_outputs()")
        #
        print("- Print output:")
        print("   model:",self.model)
        print("   ref:  ",self.ref)
        print("   label:",self.label)
        print("   note: ",self.note)
        #if any(self.sm_den): print(f"   sm_den: {np.round(self.sm_den,3)} in {self.den_unit}")
        if self.den is not None: print(f"   den: {np.round(self.den,3)} in {self.den_unit}")
        if self.e2a is not None: print(f"   e2a: {np.round(self.e2a,3)} in {self.e2a_unit}")
        if self.eps is not None: print(f"   eps: {np.round(self.eps,3)} in {self.eps_unit}")
        if self.pre is not None: print(f"   pre: {np.round(self.pre,3)} in {self.pre_unit}")
        if self.cs2 is not None: print(f"   cs2: {np.round(self.cs2,2)}")
        #
        if nuda.env.verb: print("Exit print_outputs()")
        #
    def init_self( self ):
        """
        Initialize variables in self.
        """
        #
        if nuda.env.verb: print("Enter init_self()")
        #
        #: Attribute providing the full reference to the paper to be citted.
        self.ref = ''
        #: Attribute providing additional notes about the data.
        self.note = ''
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
        self.label = ''
        #: Attribute the plot marker.
        self.marker = None
        #: Attribute the plot every data.
        self.every = 1
        #
        if nuda.env.verb: print("Exit init_self()")
        #
        return self        

