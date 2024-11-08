import os
import sys
import numpy as np  # 1.15.0
from scipy.interpolate import CubicSpline
from scipy.optimize import curve_fit
import random

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

nsat = 0.16
mnuc2 = 939.0

def uncertainty_stat(den):
    return 0.07*(den/nsat)

def models_micro_LP():
    """
    Return a list with the name of the models available in this toolkit and \
    print them all on the prompt. These models are the following ones: \
    '1994-BHF-SM-LP-AV14-GAP', '1994-BHF-SM-LP-AV14-CONT', \
    '1994-BHF-SM-LP-REID-GAP', '1994-BHF-SM-LP-REID-CONT', '1994-BHF-SM-LP-AV14-CONT-0.7'.

    :return: The list of models.
    :rtype: list[str].
    """
    models = [ '1994-BHF-SM-LP-AV14-GAP', '1994-BHF-SM-LP-AV14-CONT', \
    '1994-BHF-SM-LP-REID-GAP', '1994-BHF-SM-LP-REID-CONT', '1994-BHF-SM-LP-AV14-CONT-0.7' ]
    if nuda.env.verb: print('models available in the toolkit:',models)
    models_lower = [ item.lower() for item in models ]
    return models, models_lower

class SetupMicroLP():
    """
    Instantiate the object with Landau parameters from microscopic calculations choosen \
    by the toolkit practitioner.

    This choice is defined in `model`, which can chosen among \
    the following choices: \
    '1994-BHF-SM-LP-AV14-GAP', '1994-BHF-SM-LP-AV14-CONT', \
    '1994-BHF-SM-LP-REID-GAP', '1994-BHF-SM-LP-REID-CONT', '1994-BHF-SM-LP-AV14-CONT-0.7'.

    :param model: Fix the name of model. Default value: '1994-BHF-LP'.
    :type model: str, optional. 

    **Attributes:**
    """
    #
    def __init__( self, model = '1994-BHF-SM-LP-AV14-GAP' ):
        """
        Parameters
        ----------
        model : str, optional
        The model to consider. Choose between: '1994-BHF-SM-LP-AV14-GAP' (default), ...
        """
        #
        if nuda.env.verb: print("Enter SetupMicroLP()")
        #
        #: Attribute model.
        self.model = model
        if nuda.env.verb: print("model:",model)
        #
        self = SetupMicroLP.init_self( self )
        #
        models, models_lower = models_micro_LP()
        #
        if model.lower() not in models_lower:
            print('The model name ',model,' is not in the list of models.')
            print('list of models:',models)
            print('-- Exit the code --')
            exit()
        #
        if '1994-bhf-sm-lp' in model.lower():
            #
            file_in = os.path.join(nuda.param.path_data,'LandauParameters/micro/1994-BHF-SM.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'M. Baldo and L.S. Ferreira, Phys. Rev. C 50, 1887 (1994)'
            self.note = "write here notes about this EOS."
            if model.lower() == '1994-bhf-sm-lp-av14-gap':
                self.label = 'BHF-AV14Gap-1994'
            elif model.lower() == '1994-bhf-sm-lp-av14-cont':
                self.label = 'BHF-AV14Cont-1994'
            elif model.lower() == '1994-bhf-sm-lp-reid-gap':
                self.label = 'BHF-ReidGap-1994'
            elif model.lower() == '1994-bhf-sm-lp-reid-cont':
                self.label = 'BHF-ReidCont-1994'
            elif model.lower() == '1994-bhf-sm-lp-av14-cont-0.7':
                self.label = 'BHF-AV14Cont-0.7-1994'
            self.err = False
            #
            name = np.loadtxt( file_in, usecols=(0), comments='#', unpack = True, dtype=str )
            #
            lp1, lp2, lp3, lp4, lp5 = np.loadtxt( file_in, usecols=(1,2,3,4,5), unpack = True )
            self.sm_LP_F = np.array( (8), dtype=float )
            self.sm_LP_G = np.array( (5), dtype=float )
            self.sm_LP_Fp = np.array( (5), dtype=float )
            self.sm_LP_Gp = np.array( (5), dtype=float )
            if model.lower() == '1994-bhf-sm-lp-av14-gap':
                self.sm_LP_F  = lp1[0:8]
                self.sm_LP_G  = lp1[8:13]
                self.sm_LP_Fp = lp1[13:18]
                self.sm_LP_Gp = lp1[18:23]
                self.sm_kfn  = lp1[23]
                self.sm_effmass = lp1[24]
                self.Ksat = lp1[25]
                self.Esym2 = lp1[26]
                self.sm_effMass = lp1[27]
            elif model.lower() == '1994-bhf-sm-lp-av14-cont':
                self.sm_LP_F  = lp2[0:8]
                self.sm_LP_G  = lp2[8:13]
                self.sm_LP_Fp = lp2[13:18]
                self.sm_LP_Gp = lp2[18:23]
                self.sm_kfn  = lp2[23]
                self.sm_effmass = lp2[24]
                self.Ksat = lp2[25]
                self.Esym2 = lp2[26]
                self.sm_effMass = lp2[27]
            elif model.lower() == '1994-bhf-sm-lp-reid-gap':
                self.sm_LP_F  = lp3[0:8]
                self.sm_LP_G  = lp3[8:13]
                self.sm_LP_Fp = lp3[13:18]
                self.sm_LP_Gp = lp3[18:23]
                self.sm_kfn  = lp3[23]
                self.sm_effmass = lp3[24]
                self.Ksat = lp3[25]
                self.Esym2 = lp3[26]
                self.sm_effMass = lp3[27]
            elif model.lower() == '1994-bhf-sm-lp-reid-cont':
                self.sm_LP_F  = lp4[0:8]
                self.sm_LP_G  = lp4[8:13]
                self.sm_LP_Fp = lp4[13:18]
                self.sm_LP_Gp = lp4[18:23]
                self.sm_kfn  = lp4[23]
                self.sm_effmass = lp4[24]
                self.Ksat = lp4[25]
                self.Esym2 = lp4[26]
                self.sm_effMass = lp4[27]
            elif model.lower() == '1994-bhf-sm-lp-av14-cont-0.7':
                self.sm_LP_F  = lp5[0:8]
                self.sm_LP_G  = lp5[8:13]
                self.sm_LP_Fp = lp5[13:18]
                self.sm_LP_Gp = lp5[18:23]
                self.sm_kfn  = lp5[23]
                self.sm_effmass = lp5[24]
                self.Ksat = lp5[25]
                self.Esym2 = lp5[26]
                self.sm_effMass = lp5[27]
            #
        self.kfn_unit = 'fm$^{-1}$'
        self.Ksat_unit = 'MeV'
        #
        if nuda.env.verb: print("Exit SetupMicroLP()")
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
        if self.sm_kfn is not None: print("   sm_kfn: ",self.sm_kfn)
        if self.sm_effmass is not None: print("   sm_effmass: ",self.sm_effmass)
        if self.Ksat is not None: print("   Ksat: ",self.Ksat)
        if self.Esym2 is not None: print("   Esym2: ",self.Esym2)
        if self.sm_effMass is not None: print("   sm_effMass: ",self.sm_effMass)
        if self.sm_LP_F is not None: print(f"   sm_LP_F: {np.round(self.sm_LP_F,3)}")
        if self.sm_LP_G is not None: print(f"   sm_LP_G: {np.round(self.sm_LP_G,3)}")
        if self.sm_LP_Fp is not None: print(f"   sm_LP_Fp: {np.round(self.sm_LP_Fp,3)}")
        if self.sm_LP_Gp is not None: print(f"   sm_LP_Gp: {np.round(self.sm_LP_Gp,3)}")
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
        #: Attribute the neutron matter density.
        self.nm_den = None
        #: Attribute the symmetric matter density.
        self.sm_den = None
        #: Attribute the neutron matter neutron Fermi momentum.
        self.nm_kfn = None
        #: Attribute the symmetric matter neutron Fermi momentum.
        self.sm_kfn = None
        #: Attribute the symmetric matter Fermi momentum.
        self.nm_kf = None
        #: Attribute the symmetric matter Fermi momentum.
        self.sm_kf = None
        #: Attribute the neutron matter effective mass (from the spe).
        self.nm_effmass = None
        #: Attribute the symmetric matter effective mass.
        self.sm_effmass = None
        #: Attribute the symmetric matter effective mass (from F1 Landau parameter).
        self.sm_effMass = None
        #: Attribute the quadratic contribution to the symmetry energy
        self.Esym2 = None
        #: Attribute the incompressibility modulus
        self.Ksat = None
        #: Attribute the plot linestyle.
        self.linestyle = 'solid'
        #: Attribute the plot to discriminate True uncertainties from False ones.
        self.err = False
        #: Attribute the plot label data.
        self.label = ''
        #
        if nuda.env.verb: print("Exit init_self()")
        #
        return self        

