import os
import sys
import numpy as np  # 1.15.0
from scipy.interpolate import CubicSpline
from scipy.optimize import curve_fit
import random

import nucleardatapy as nuda

#nsat = 0.16
#mnuc2 = 939.0

def micro_LP_models():
    """
    Return a list with the name of the models available in this toolkit and \
    print them all on the prompt. These models are the following ones: \
    '1994-BHF-SM-LP-AV14-GAP', '1994-BHF-SM-LP-AV14-CONT', \
    '1994-BHF-SM-LP-REID-GAP', '1994-BHF-SM-LP-REID-CONT', '1994-BHF-SM-LP-AV14-CONT-0.7', \
    '2006-BHF-SM-AV18', '2006-BHF-NM-AV18', '2006-IBHF-SM-AV18', '2006-IBHF-NM-AV18', '2007-BHF-NM-LP-BONNC'.

    :return: The list of models.
    :rtype: list[str].
    """
    models = [ '1994-BHF-SM-AV14-GAP', '1994-BHF-SM-AV14-CONT', \
    '1994-BHF-SM-REID-GAP', '1994-BHF-SM-REID-CONT', '1994-BHF-SM-AV14-CONT-0.7', \
    '2006-BHF-SM-Av18', '2006-BHF-NM-Av18', '2006-EBHF-SM-Av18', '2006-EBHF-NM-Av18', \
    '2007-BHF-NM-BONNC' ]
    if nuda.env.verb: print('models available in the toolkit:',models)
    models_lower = [ item.lower() for item in models ]
    return models, models_lower

class setupMicroLP():
    """
    Instantiate the object with Landau parameters from microscopic calculations choosen \
    by the toolkit practitioner.

    This choice is defined in `model`, which can chosen among \
    the following choices: \
    '1994-BHF-SM-LP-AV14-GAP', '1994-BHF-SM-LP-AV14-CONT', \
    '1994-BHF-SM-LP-REID-GAP', '1994-BHF-SM-LP-REID-CONT', '1994-BHF-SM-LP-AV14-CONT-0.7',\
    '2006-BHF-SM-AV18', '2006-BHF-NM-AV18', '2006-IBHF-SM-AV18', '2006-IBHF-NM-AV18', '2007-BHF-NM-LP-BONNC'.

    :param model: Fix the name of model. Default value: '1994-BHF-LP'.
    :type model: str, optional. 

    **Attributes:**
    """
    #
    def __init__( self, model = '1994-BHF-AV14-SM-GAP' ):
        """
        Parameters
        ----------
        model : str, optional
        The model to consider. Choose between: '1994-BHF-SM-LP-AV14-GAP' (default), ...
        """
        #
        if nuda.env.verb: print("Enter setupMicroLP()")
        #
        #: Attribute model.
        self.model = model
        if nuda.env.verb: print("model:",model)
        #
        self = setupMicroLP.init_self( self )
        #
        models, models_lower = micro_LP_models()
        #
        if model.lower() not in models_lower:
            print('The model name ',model,' is not in the list of models.')
            print('list of models:',models)
            print('-- Exit the code --')
            exit()
        #
        for ell in range(0,8):
            self.sm_LP['F'][ell]  = None
            self.sm_LP['G'][ell]  = None
            self.sm_LP['Fp'][ell] = None
            self.sm_LP['Gp'][ell] = None
            self.nm_LP['F'][ell]  = None
            self.nm_LP['G'][ell]  = None
        self.every = 1
        #
        if '1994-bhf-sm' in model.lower():
            #
            file_in = os.path.join(nuda.param.path_data,'LandauParameters/micro/1994-BHF-SM.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'M. Baldo and L.S. Ferreira, Phys. Rev. C 50, 1887 (1994)'
            self.note = "write here notes about this EOS."
            self.err = False
            #
            #name = np.loadtxt( file_in, usecols=(0), comments='#', unpack = True, dtype=str )
            name = []
            with open(file_in,"r") as file:
                for line in file:
                    if '#' in line:
                        continue
                    name.append( line.split()[0] )
            name = np.array( name, dtype = str )
            #
            lp1, lp2, lp3, lp4, lp5 = np.loadtxt( file_in, usecols=(1,2,3,4,5), unpack = True )
            #
            if model.lower() == '1994-bhf-sm-av14-gap':
                self.label = 'BHF-AV14Gap-1994'
                self.marker = 'o'
                for ell in range(0,8):
                    self.sm_LP['F'][ell]  = lp1[ell]
                    self.sm_LP['G'][ell]  = lp1[8+ell]
                    self.sm_LP['Fp'][ell] = lp1[13+ell]
                    self.sm_LP['Gp'][ell] = lp1[18+ell]
                    self.nm_LP['F'][ell]  = None
                    self.nm_LP['G'][ell]  = None
                self.sm_kfn  = lp1[23]
                self.sm_effmass = lp1[24]
                self.Ksat = lp1[25]
                self.Esym2 = lp1[26]
                self.sm_effMass = lp1[27]
                #
            elif model.lower() == '1994-bhf-sm-av14-cont':
                #
                self.label = 'BHF-AV14Cont-1994'
                self.marker = 'o'
                for ell in range(0,8):
                    self.sm_LP['F'][ell]  = lp2[ell]
                    self.sm_LP['G'][ell]  = lp2[8+ell]
                    self.sm_LP['Fp'][ell] = lp2[13+ell]
                    self.sm_LP['Gp'][ell] = lp2[18+ell]
                    self.nm_LP['F'][ell]  = None
                    self.nm_LP['G'][ell]  = None
                self.sm_kfn  = lp2[23]
                self.sm_effmass = lp2[24]
                self.Ksat = lp2[25]
                self.Esym2 = lp2[26]
                self.sm_effMass = lp2[27]
                #
            elif model.lower() == '1994-bhf-sm-reid-gap':
                #
                self.label = 'BHF-ReidGap-1994'
                self.marker = 'o'
                for ell in range(0,8):
                    self.sm_LP['F'][ell]  = lp3[ell]
                    self.sm_LP['G'][ell]  = lp3[8+ell]
                    self.sm_LP['Fp'][ell] = lp3[13+ell]
                    self.sm_LP['Gp'][ell] = lp3[18+ell]
                    self.nm_LP['F'][ell]  = None
                    self.nm_LP['G'][ell]  = None
                self.sm_kfn  = lp3[23]
                self.sm_effmass = lp3[24]
                self.Ksat = lp3[25]
                self.Esym2 = lp3[26]
                self.sm_effMass = lp3[27]
                #
            elif model.lower() == '1994-bhf-sm-reid-cont':
                #
                self.label = 'BHF-ReidCont-1994'
                self.marker = 'o'
                for ell in range(0,8):
                    self.sm_LP['F'][ell]  = lp4[ell]
                    self.sm_LP['G'][ell]  = lp4[8+ell]
                    self.sm_LP['Fp'][ell] = lp4[13+ell]
                    self.sm_LP['Gp'][ell] = lp4[18+ell]
                    self.nm_LP['F'][ell]  = None
                    self.nm_LP['G'][ell]  = None
                self.sm_kfn  = lp4[23]
                self.sm_effmass = lp4[24]
                self.Ksat = lp4[25]
                self.Esym2 = lp4[26]
                self.sm_effMass = lp4[27]
                #
            elif model.lower() == '1994-bhf-sm-av14-cont-0.7':
                #
                self.label = 'BHF-AV14Cont-0.7-1994'
                self.marker = 'o'
                for ell in range(0,8):
                    self.sm_LP['F'][ell]  = lp5[ell]
                    self.sm_LP['G'][ell]  = lp5[8+ell]
                    self.sm_LP['Fp'][ell] = lp5[13+ell]
                    self.sm_LP['Gp'][ell] = lp5[18+ell]
                    self.nm_LP['F'][ell]  = None
                    self.nm_LP['G'][ell]  = None
                self.sm_kfn  = lp5[23]
                self.sm_effmass = lp5[24]
                self.Ksat = lp5[25]
                self.Esym2 = lp5[26]
                self.sm_effMass = lp5[27]
            #print('F:',self.sm_LP['F'][0])
            #print('G:',self.sm_LP['G'][0])
        #
        elif model.lower() == '2006-bhf-sm-av18':
            #
            file_in = os.path.join(nuda.param.path_data,'LandauParameters/micro/2006-BHF-SM-AV18.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'L.G. Cao, U. Lombardo, and P. Schuck, Phys Rev C 74, 064301 (2006)'
            self.note = "write here notes about this EOS."
            self.err = False
            self.label = 'BHF-Av18-2006'
            self.marker = 's'
            self.sm_kfn, self.sm_LP['F'][0], self.sm_LP['Fp'][0], self.sm_LP['G'][0], self.sm_LP['Gp'][0] = \
              np.loadtxt( file_in, usecols=(0,1,2,3,4), comments='#', unpack = True, dtype=float )
            self.every = 300
        #
        elif model.lower() == '2006-bhf-nm-av18':
            #
            file_in = os.path.join(nuda.param.path_data,'LandauParameters/micro/2006-BHF-NM-AV18.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'L.G. Cao, U. Lombardo, and P. Schuck, Phys Rev C 74, 064301 (2006)'
            self.note = "write here notes about this EOS."
            self.err = False
            self.label = 'BHF-Av18-2006'
            self.marker = 's'
            self.nm_kfn, self.nm_LP['F'][0], self.nm_LP['G'][0] = \
              np.loadtxt( file_in, usecols=(0,1,2), comments='#', unpack = True, dtype=float )
            self.every = 300
        #
        elif model.lower() == '2006-ebhf-sm-av18':
            #
            file_in = os.path.join(nuda.param.path_data,'LandauParameters/micro/2006-EBHF-SM-AV18.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'L.G. Cao, U. Lombardo, and P. Schuck, Phys Rev C 74, 064301 (2006)'
            self.note = "write here notes about this EOS."
            self.err = False
            self.label = 'EBHF-Av18-2006'
            self.marker = 'o'
            self.sm_kfn, self.sm_LP['F'][0], self.sm_LP['Fp'][0], self.sm_LP['G'][0], self.sm_LP['Gp'][0] = \
              np.loadtxt( file_in, usecols=(0,1,2,3,4), comments='#', unpack = True, dtype=float )
            self.every = 300
        #
        elif model.lower() == '2006-ebhf-nm-av18':
            #
            file_in = os.path.join(nuda.param.path_data,'LandauParameters/micro/2006-EBHF-NM-AV18.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'L.G. Cao, U. Lombardo, and P. Schuck, Phys Rev C 74, 064301 (2006)'
            self.note = "write here notes about this EOS."
            self.err = False
            self.label = 'EBHF-Av18-2006'
            self.marker = 'o'
            self.nm_kfn, self.nm_LP['F'][0], self.nm_LP['G'][0] = \
              np.loadtxt( file_in, usecols=(0,1,2), comments='#', unpack = True, dtype=float )
            self.every = 300
        #
        elif model.lower() == '2007-bhf-nm-bonnc':
            #
            file_in = os.path.join(nuda.param.path_data,'LandauParameters/micro/2007-BHF-NM.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'Armen Sedrakian, Herbert Müther, Peter Schuck, Phys Rev C 76, 055805 (2007)'
            self.note = "write here notes about this EOS."
            self.err = False
            self.label = 'BHF-BonnC-2007'
            self.marker = 's'
            self.nm_kfn, self.nm_effmass, lp_f, lp_g, self.nm_gap, self.nm_Tc = \
              np.loadtxt( file_in, usecols=(0,1,2,3,4,5), comments='#', unpack = True, dtype=float )
            self.nm_LP['F'][0]  = lp_f
            self.nm_LP['G'][0]  = lp_g
            #print('F:',self.nm_LP['F'][0])
            #print('G:',self.nm_LP['G'][0])
            #
        self.kfn_unit = 'fm$^{-1}$'
        self.gap_unit = 'MeV'
        self.tc_unit  = 'MeV'
        #
        if nuda.env.verb: print("Exit setupMicroLP()")
        #
    def print_outputs( self ):
        """
        Method which print outputs on terminal's screen.
        """
        #
        if nuda.env.verb: print("Enter print_outputs()")
        #
        print("- Print output:")
        print("   model: ",self.model)
        print("   ref:   ",self.ref)
        print("   label: ",self.label)
        print("   marker:",self.marker)
        print("   note:  ",self.note)
        #if any(self.sm_den): print(f"   sm_den: {np.round(self.sm_den,3)} in {self.den_unit}")
        print('in SM:')
        if self.sm_kfn is not None: print("   sm_kfn: ",self.sm_kfn)
        if self.sm_effmass is not None: print("   sm_effmass: ",self.sm_effmass)
        if self.sm_effMass is not None: print("   sm_effMass: ",self.sm_effMass)
        if self.Ksat is not None: print("   Ksat: ",self.Ksat)
        if self.Esym2 is not None: print("   Esym2: ",self.Esym2)
        #print(f"   F: {self.sm_LP['F']}")
        #print(f"   F0: {self.sm_LP['F'][0]}")
        if self.sm_LP['F'][0] is not None: print(f"   F0: {np.round(self.sm_LP['F'][0],3)}")
        if self.sm_LP['G'][0] is not None: print(f"   G0: {np.round(self.sm_LP['G'][0],3)}")
        if self.sm_LP['Fp'][0] is not None: print(f"   Fp0: {np.round(self.sm_LP['Fp'][0],3)}")
        if self.sm_LP['Gp'][0] is not None: print(f"   Gp0: {np.round(self.sm_LP['Gp'][0],3)}")
        print('in NM:')
        if self.nm_kfn is not None: print("   nm_kfn: ",self.nm_kfn)
        if self.nm_effmass is not None: print("   nm_effmass: ",self.nm_effmass)
        if self.nm_LP['F'][0] is not None: print(f"   F0: {np.round(self.nm_LP['F'][0],3)}")
        if self.nm_LP['G'][0] is not None: print(f"   G0: {np.round(self.nm_LP['G'][0],3)}")
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
        #: Attribute the plot linestyle.
        self.linestyle = 'solid'
        #: Attribute the plot to discriminate True uncertainties from False ones.
        self.err = False
        #: Attribute the plot label data.
        self.label = ''
        #: Attribute the plot marker data.
        self.marker = ''
        #
        #: Attribute the neutron matter density.
        self.nm_den = None
        #: Attribute the symmetric matter density.
        self.sm_den = None
        #: Attribute the neutron matter neutron Fermi momentum.
        self.nm_kfn = None
        #: Attribute the symmetric matter neutron Fermi momentum.
        self.sm_kfn = None
        #
        self.sm_LP = {}
        self.nm_LP = {}
        #
        self.sm_LP['F'] = {}
        self.sm_LP['G'] = {}
        self.sm_LP['Fp'] = {}
        self.sm_LP['Gp'] = {}
        self.nm_LP['F'] = {}
        self.nm_LP['G'] = {}
        #
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
        #
        if nuda.env.verb: print("Exit init_self()")
        #
        return self        

