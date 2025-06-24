import os
import sys
import numpy as np  # 1.15.0
from scipy.interpolate import CubicSpline

import nucleardatapy as nuda

def pheno_models():
    """
    Return a list of models available in this toolkit and print them all on the prompt.

    :return: The list of models with can be 'Skyrme', 'ESkyrme', 'NLRH', 'DDRH', 'DDRHF'.
    :rtype: list[str].
    """
    #
    if nuda.env.verb: print("\nEnter pheno_models()")
    #
    models = [ 'Skyrme', 'ESkyrme', 'Gogny', 'Fayans', 'NLRH', 'DDRH', 'DDRHF' ]
    #print('Phenomenological models available in the toolkit:',models)
    models_lower = [ item.lower() for item in models ]
    #
    if nuda.env.verb: print("Exit pheno_models()")
    #
    return models, models_lower

def pheno_params( model ):
    """
    Return a list with the parameterizations available in 
    this toolkit for a given model and print them all on the prompt.

    :param model: The type of model for which there are parametrizations. \
    They should be chosen among the following options: 'Skyrme', 'ESkyrme', 'Gogny', 'Fayans', 'NLRH', 'DDRH', 'DDRHF' .
    :type model: str.
    :return: The list of parametrizations. \
    If `models` == 'Skyrme': 'BSK14', \
    'BSK16', 'BSK17', 'BSK27','BSkG1', 'BSkG2', 'F-', 'F+', 'F0', 'FPL', 'LNS', 'LNS1', 'LNS5', \
    'NRAPR', 'RATP', 'SAMI', 'SGII', 'SIII', 'SKGSIGMA', 'SKI2', 'SKI4', 'SKMP', \
    'SKMS', 'SKO', 'SKOP', 'SKP', 'SKRSIGMA', 'SKX', 'Skz2', 'SLY4', 'SLY5', \
    'SLY230A', 'SLY230B', 'SV', 'T6', 'T44', 'UNEDF0', 'UNEDF1'. \
    If `models` == 'ESkyrme': 'BSk22', 'BSk24', 'BSk25', 'BSk26', 'BSk31', 'BSk32', \
     'BSkG3','BSkG4' . \
    If `models` == 'Fayans': 'SLy4', 'SkM*', 'Fy(IVP)', 'Fy(Dr,HDB)', 'Fy(std)', \
    'SV-min', 'SV-bas', 'SV-K218', 'SV-K226', 'SV-K241', 'SV-mas07', 'SV-mas08', 'SV-mas10',
    'SV-sym28', 'SV-sym32', 'SV-sym34', 'SV-kap00', 'SV-kap20', 'SV-kap60'.
    If `models` == 'NLRH': 'NL-SH', 'NL3', 'NL3II', 'PK1', 'PK1R', 'TM1'. \
    If `models` == 'DDRH': 'DDME1', 'DDME2', 'DDMEd', 'PKDD', 'TW99'. \
    If `models` == 'DDRHF': 'PKA1', 'PKO1', 'PKO2', 'PKO3'.
    :rtype: list[str].
    """
    #
    if nuda.env.verb: print("\nEnter pheno_params()")
    #
    #print('For model:',model)
    if model.lower() == 'skyrme':
        params = [ 'BSK14', 'BSK16', 'BSK17', 'BSK27', 'BSkG1', 'BSkG2','F-', \
            'F+', 'F0', 'FPL', 'LNS', 'LNS1', 'LNS5', 'NRAPR', 'RATP', \
            'SAMI', 'SGII', 'SIII', 'SKGSIGMA', 'SKI2', 'SKI4', 'SKMP', \
            'SKMS', 'SKO', 'SKOP', 'SKP', 'SKRSIGMA', 'SKX', 'Skz2', \
            'SLY4', 'SLY5', 'SLY230A', 'SLY230B', 'SV', 'T6', 'T44', \
            'UNEDF0', 'UNEDF1' ]
    elif model.lower() == 'eskyrme':
        params = [ 'BSk22', 'BSk24', 'BSk25', 'BSk26', 'BSk31', 'BSk32',  'BSkG3','BSkG4' ]
    elif model.lower() == 'fayans':
        params = [ 'SLy4', 'SkM*', 'Fy(IVP)', 'Fy(Dr,HDB)', 'Fy(std)', \
            'SV-min', 'SV-bas', 'SV-K218', 'SV-K226', 'SV-K241', 'SV-mas07', 'SV-mas08', 'SV-mas10',\
            'SV-sym28', 'SV-sym32', 'SV-sym34', 'SV-kap00', 'SV-kap20', 'SV-kap60' ]
    elif model.lower() == 'gogny':
        params = [ 'D1S', 'D1', 'D250', 'D260', 'D280', 'D300' ]
    elif model.lower() == 'nlrh':
        params = [ 'NL-SH', 'NL3', 'NL3II', 'PK1', 'PK1R', 'TM1' ]
    elif model.lower() == 'ddrh':
        params = [ 'DDME1', 'DDME2', 'DDMEd', 'PKDD', 'TW99' ]
    elif model.lower() == 'ddrhf':
        params = [ 'PKA1', 'PKO1', 'PKO2', 'PKO3' ]
    #print('For model:',model)
    #print('Parameters available in the toolkit:',params)
    params_lower = [ item.lower() for item in params ]
    #
    if nuda.env.verb: print("Exit pheno_params()")
    #
    return params, params_lower

class setupPheno():
    """
    Instantiate the object with results based on phenomenological\
    interactions and choosen by the toolkit practitioner. \
    This choice is defined in the variables `model` and `param`.

    If `models` == 'Skyrme', `param` can be: 'BSK14', \
    'BSK16', 'BSK17', 'BSK27', 'BSkG1', 'BSkG2','F-', 'F+', 'F0', 'FPL', 'LNS', 'LNS1', 'LNS5', \
    'NRAPR', 'RATP', 'SAMI', 'SGII', 'SIII', 'SKGSIGMA', 'SKI2', 'SKI4', 'SKMP', \
    'SKMS', 'SKO', 'SKOP', 'SKP', 'SKRSIGMA', 'SKX', 'Skz2', 'SLY4', 'SLY5', \
    'SLY230A', 'SLY230B', 'SV', 'T6', 'T44', 'UNEDF0', 'UNEDF1'. 

    If `models` == 'ESkyrme', `param` can be: 'BSk22', 'BSk24', 'BSk25', \
    'BSk26', 'BSk31', 'BSk32',  'BSkG3','BSkG4' .

    If `models` == 'NLRH', `param` can be: 'NL-SH', 'NL3', 'NL3II', 'PK1', 'PK1R', 'TM1'. 

    If `models` == 'DDRH', `param` can be: 'DDME1', 'DDME2', 'DDMEd', 'PKDD', 'TW99'. 

    If `models` == 'DDRHF', `param` can be: 'PKA1', 'PKO1', 'PKO2', 'PKO3'. 
    
    :param model: Fix the name of model: 'Skyrme', 'NLRH', \
    'DDRH', 'DDRHF'. Default value: 'Skyrme'.
    :type model: str, optional. 
    :param param: Fix the parameterization associated to model. \
    Default value: 'SLY5'.
    :type param: str, optional. 

    **Attributes:**
    """
    #
    def __init__( self, model = 'Skyrme', param = 'SLY5' ):
        #
        if nuda.env.verb: print("\nEnter setupPheno()")
        #
        #: Attribute model.
        self.model = model
        if nuda.env.verb: print("model:",model)
        #print("-> model:",model)
        #: Attribute param.
        self.param = param
        if nuda.env.verb: print("param:",param)
        #print("-> param:",param)
        #
        self = setupPheno.init_self( self )
        #
        models, models_lower = pheno_models( )
        #
        if model.lower() not in models_lower:
            print('The model name ',model,' is not in the list of models.')
            print('list of models:',models)
            print('-- Exit the code --')
            exit()
        #
        params, params_lower = pheno_params( model = model )
        #
        self.nm_rmass = nuda.cst.mnc2
        self.sm_rmass = 0.5 * ( nuda.cst.mnc2 + nuda.cst.mpc2 )
        #self.rmass = (1.0-self.xpr) * nuda.cst.mnc2 + self.xpr * nuda.cst.mpc2
        #
        if param.lower() not in params_lower:
            print('The param set ',param,' is not in the list of param.')
            print('list of param:',params)
            print('-- Exit the code --')
            exit()
        #
        if model.lower() == 'skyrme':
            #
            file_in1 = os.path.join(nuda.param.path_data,'matter/pheno/Skyrme/'+param+'-SM.dat')
            file_in2 = os.path.join(nuda.param.path_data,'matter/pheno/Skyrme/'+param+'-NM.dat')
            if nuda.env.verb: print('Reads file1:',file_in1)
            if nuda.env.verb: print('Reads file2:',file_in2)
            #: Attribute providing the full reference to the paper to be citted.
            #self.ref = ''
            #: Attribute providing the label the data is references for figures.
            self.label = 'SKY-'+param
            #: Attribute providing additional notes about the data.
            self.note = "write here notes about this EOS."
            self.sm_den, self.sm_kfn, self.sm_e2a_int, self.sm_pre, a, self.sm_cs2 = np.loadtxt( file_in1, usecols=(0,1,2,3,4,5), comments='#', unpack = True )
            self.nm_den, self.nm_kfn, self.nm_e2a_int, self.nm_pre, a, self.nm_cs2 = np.loadtxt( file_in2, usecols=(0,1,2,3,4,5), comments='#', unpack = True )
            self.sm_e2a = self.sm_rmass + self.sm_e2a_int
            self.nm_e2a = self.nm_rmass + self.nm_e2a_int
            self.sm_eps = self.sm_e2a * self.sm_den
            self.nm_eps = self.nm_e2a * self.nm_den
            self.sm_kf = self.sm_kfn
            # pressure in SM
            x = np.insert( self.sm_den, 0, 0.0 )
            y = np.insert( self.sm_e2a_int, 0, 0.0 )
            cs_sm_e2a = CubicSpline( x, y )
            self.sm_pre = np.array( self.sm_den**2 * cs_sm_e2a( self.sm_den, 1) )
            # pressure in NM
            x = np.insert( self.nm_den, 0, 0.0 )
            y = np.insert( self.nm_e2a_int, 0, 0.0 )
            cs_nm_e2a = CubicSpline( x, y )
            self.nm_pre = np.array( self.nm_den**2 * cs_nm_e2a( self.nm_den, 1) )
            # enthalpy
            self.sm_h2a = self.sm_e2a + self.sm_pre / self.sm_den
            self.nm_h2a = self.nm_e2a + self.nm_pre / self.nm_den
            # sound speed in SM
            x = np.insert(self.sm_den, 0, 0.0)
            y = np.insert(self.sm_pre, 0, 0.0)
            cs_sm_pre = CubicSpline(x, y)
            self.sm_cs2 = cs_sm_pre(self.sm_den, 1) / self.sm_h2a
            # sound speed in NM
            x = np.insert(self.nm_den, 0, 0.0)
            y = np.insert(self.nm_pre, 0, 0.0)
            cs_nm_pre = CubicSpline(x, y)
            self.nm_cs2 = cs_nm_pre(self.nm_den, 1) / self.nm_h2a
            #
        #
        elif model.lower() == 'eskyrme':
            #
            file_in1 = os.path.join(nuda.param.path_data,'matter/pheno/ESkyrme/'+param+'-SM.dat')
            file_in2 = os.path.join(nuda.param.path_data,'matter/pheno/ESkyrme/'+param+'-NM.dat')
            if nuda.env.verb: print('Reads file1:',file_in1)
            if nuda.env.verb: print('Reads file2:',file_in2)
            #: Attribute providing the full reference to the paper to be citted.
            #self.ref = ''
            #: Attribute providing the label the data is references for figures.
            self.label = 'ESKY-'+param
            #: Attribute providing additional notes about the data.
            self.note = "write here notes about this EOS."
            self.sm_den, self.sm_e2a_int, self.sm_pre = np.loadtxt( file_in1, usecols=(0,1,2), comments='#', unpack = True )
            self.nm_den, self.nm_e2a_int, self.nm_pre = np.loadtxt( file_in2, usecols=(0,1,2), comments='#', unpack = True )
            self.sm_e2a = self.sm_rmass + self.sm_e2a_int
            self.nm_e2a = self.nm_rmass + self.nm_e2a_int
            self.sm_eps = self.sm_e2a * self.sm_den
            self.nm_eps = self.nm_e2a * self.nm_den
            self.sm_kf = self.sm_kfn
            self.sm_kfn = nuda.kf_n( nuda.cst.half * self.sm_den )
            self.nm_kfn = nuda.kf_n( self.nm_den )
            self.sm_kf = self.sm_kfn
            # enthalpy
            self.sm_h2a = self.sm_e2a + self.sm_pre / self.sm_den
            self.nm_h2a = self.nm_e2a + self.nm_pre / self.nm_den
            # sound speed in SM
            x = np.insert( self.sm_den, 0, 0.0 )
            y = np.insert( self.sm_pre, 0, 0.0 )
            cs_sm_pre = CubicSpline( x, y )
            self.sm_cs2 = cs_sm_pre( self.sm_den, 1) / self.sm_h2a
            # sound speed in NM
            x = np.insert( self.nm_den, 0, 0.0 )
            y = np.insert( self.nm_pre, 0, 0.0 )
            cs_nm_pre = CubicSpline( x, y )
            self.nm_cs2 = cs_nm_pre( self.nm_den, 1) / self.nm_h2a
            #
        elif model.lower() == 'gogny':
            #
            file_in3 = os.path.join(nuda.param.path_data,'matter/pheno/GognyNEP.dat')
            if nuda.env.verb: print('Reads file3:',file_in3)
            self.label = 'Gogny-'+param
            self.note = "write here notes about this EOS."
            #
#            pass
        elif model.lower() == 'fayans':
            #
            pass
            #
        elif model.lower() == 'nlrh':
            #
            file_in1 = os.path.join(nuda.param.path_data,'matter/pheno/nlrh/'+param+'-SM.dat')
            file_in2 = os.path.join(nuda.param.path_data,'matter/pheno/nlrh/'+param+'-NM.dat')
            if nuda.env.verb: print('Reads file1:',file_in1)
            if nuda.env.verb: print('Reads file2:',file_in2)
            #self.ref = ''
            self.label = 'NLRH-'+param
            self.note = "write here notes about this EOS."
            self.sm_den, self.sm_kfn, self.sm_e2a_int, self.sm_pre, self.sm_cs2_data = np.loadtxt( file_in1, usecols=(0,1,2,3,4), comments='#', unpack = True )
            self.nm_den, self.nm_kfn, self.nm_e2a_int, self.nm_pre, self.nm_cs2_data = np.loadtxt( file_in2, usecols=(0,1,2,3,4), comments='#', unpack = True )
            self.sm_e2a = self.sm_rmass + self.sm_e2a_int
            self.nm_e2a = self.nm_rmass + self.nm_e2a_int
            self.sm_eps = self.sm_e2a * self.sm_den
            self.nm_eps = self.nm_e2a * self.nm_den
            self.sm_kf = self.sm_kfn
            # enthalpy
            self.sm_h2a = self.sm_e2a + self.sm_pre / self.sm_den
            self.nm_h2a = self.nm_e2a + self.nm_pre / self.nm_den
            # sound speed in SM
            x = np.insert( self.sm_den, 0, 0.0 )
            y = np.insert( self.sm_pre, 0, 0.0 )
            cs_sm_pre = CubicSpline( x, y )
            self.sm_cs2 = cs_sm_pre( self.sm_den, 1) / self.sm_h2a
            # sound speed in NM
            x = np.insert( self.nm_den, 0, 0.0 )
            y = np.insert( self.nm_pre, 0, 0.0 )
            cs_nm_pre = CubicSpline( x, y )
            self.nm_cs2 = cs_nm_pre( self.nm_den, 1) / self.nm_h2a
            #
        elif model.lower() == 'ddrh':
            #
            file_in1 = os.path.join(nuda.param.path_data,'matter/pheno/ddrh/'+param+'-SM.dat')
            file_in2 = os.path.join(nuda.param.path_data,'matter/pheno/ddrh/'+param+'-NM.dat')
            if nuda.env.verb: print('Reads file1:',file_in1)
            if nuda.env.verb: print('Reads file2:',file_in2)
            #self.ref = ''
            self.label = 'DDRH-'+param
            if param == "DDMEd": self.label = "DDRH-DDME$\\delta$"
            self.note = "write here notes about this EOS."
            self.sm_den, self.sm_kfn, self.sm_e2a_int, self.sm_pre, self.sm_cs2_data = np.loadtxt( file_in1, usecols=(0,1,2,3,4), comments='#', unpack = True )
            self.nm_den, self.nm_kfn, self.nm_e2a_int, self.nm_pre, self.nm_cs2_data = np.loadtxt( file_in2, usecols=(0,1,2,3,4), comments='#', unpack = True )
            self.sm_e2a = self.sm_rmass + self.sm_e2a_int
            self.nm_e2a = self.nm_rmass + self.nm_e2a_int
            self.sm_eps = self.sm_e2a * self.sm_den
            self.nm_eps = self.nm_e2a * self.nm_den
            self.sm_kf = self.sm_kfn
            # enthalpy
            self.sm_h2a = self.sm_e2a + self.sm_pre / self.sm_den
            self.nm_h2a = self.nm_e2a + self.nm_pre / self.nm_den
            # sound speed in SM
            x = np.insert( self.sm_den, 0, 0.0 )
            y = np.insert( self.sm_pre, 0, 0.0 )
            cs_sm_pre = CubicSpline( x, y )
            self.sm_cs2 = cs_sm_pre( self.sm_den, 1) / self.sm_h2a
            # sound speed in NM
            x = np.insert( self.nm_den, 0, 0.0 )
            y = np.insert( self.nm_pre, 0, 0.0 )
            cs_nm_pre = CubicSpline( x, y )
            self.nm_cs2 = cs_nm_pre( self.nm_den, 1) / self.nm_h2a
            #
        elif model.lower() == 'ddrhf':
            #
            file_in1 = os.path.join(nuda.param.path_data,'matter/pheno/ddrhf/'+param+'-SM.dat')
            file_in2 = os.path.join(nuda.param.path_data,'matter/pheno/ddrhf/'+param+'-NM.dat')
            if nuda.env.verb: print('Reads file1:',file_in1)
            if nuda.env.verb: print('Reads file2:',file_in2)
            #self.ref = ''
            self.label = 'DDRHF-'+param
            self.note = "write here notes about this EOS."
            self.sm_den, self.sm_kfn, self.sm_e2a_int, self.sm_pre, self.sm_cs2_data = np.loadtxt( file_in1, usecols=(0,1,2,3,4), comments='#', unpack = True )
            self.nm_den, self.nm_kfn, self.nm_e2a_int, self.nm_pre, self.nm_cs2_data = np.loadtxt( file_in2, usecols=(0,1,2,3,4), comments='#', unpack = True )
            self.sm_e2a = self.sm_rmass + self.sm_e2a_int
            self.nm_e2a = self.nm_rmass + self.nm_e2a_int 
            self.sm_eps = self.sm_e2a * self.sm_den
            self.nm_eps = self.nm_e2a * self.nm_den
            self.sm_kf = self.sm_kfn
            # enthalpy
            self.sm_h2a = self.sm_e2a + self.sm_pre / self.sm_den
            self.nm_h2a = self.nm_e2a + self.nm_pre / self.nm_den
            # sound speed in SM
            x = np.insert( self.sm_den, 0, 0.0 )
            y = np.insert( self.sm_pre, 0, 0.0 )
            cs_sm_pre = CubicSpline( x, y )
            self.sm_cs2 = cs_sm_pre( self.sm_den, 1) / self.sm_h2a
            # sound speed in NM
            x = np.insert( self.nm_den, 0, 0.0 )
            y = np.insert( self.nm_pre, 0, 0.0 )
            cs_nm_pre = CubicSpline( x, y )
            self.nm_cs2 = cs_nm_pre( self.nm_den, 1) / self.nm_h2a
            #
        self.den_unit = 'fm$^{-3}$'
        self.kfn_unit = 'fm$^{-1}$'
        self.e2a_unit = 'MeV'
        self.pre_unit = 'MeV fm$^{-3}$'
        self.gap_unit = 'MeV'
        #
        if nuda.env.verb: print("Exit SetupEOSPheno()")
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
        print("   param:",self.param)
        #print("   ref:",self.ref)
        print("   label:",self.label)
        #print("   note:",self.note)
        if any(self.sm_den): print(f"   sm_den: {np.round(self.sm_den,2)} in {self.den_unit}")
        if any(self.sm_kfn): print(f"   sm_kfn: {np.round(self.sm_kfn,2)} in {self.kfn_unit}")
        if any(self.sm_e2a): print(f"   sm_e2a: {np.round(self.sm_e2a,2)} in {self.e2a_unit}")
        if any(self.sm_cs2): print(f"   sm_cs2: {np.round(self.sm_cs2,2)}")
        if any(self.nm_den): print(f"   nm_den: {np.round(self.nm_den,2)} in {self.den_unit}")
        if any(self.nm_kfn): print(f"   nm_kfn: {np.round(self.nm_kfn,2)} in {self.kfn_unit}")
        if any(self.nm_e2a): print(f"   nm_e2a: {np.round(self.nm_e2a,2)} in {self.e2a_unit}")
        if any(self.nm_cs2): print(f"   nm_cs2: {np.round(self.nm_cs2,2)}")
        if any(self.nm_gap): print(f"   nm_gap: {np.round(self.nm_gap,2)} in {self.gap_unit}")
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
        #: Attribute the plot linestyle.
        self.linestyle = 'solid'
        #: Attribute providing the full reference to the paper to be citted.
        self.ref = ''
        #: Attribute providing additional notes about the data.
        self.note = ''
        #: Attribute the plot label data.
        self.label = ''
        #: Attribute the plot marker.
        self.marker = None
        #: Attribute the plot every data.
        self.every = 1
        #
        #: Attribute the neutron matter density.
        self.nm_den = []
        #: Attribute the symmetric matter density.
        self.sm_den = []
        #: Attribute the neutron matter neutron Fermi momentum.
        self.nm_kfn = []
        #: Attribute the symmetric matter neutron Fermi momentum.
        self.sm_kfn = []
        #: Attribute the symmetric matter Fermi momentum.
        self.sm_kf = []
        #: Attribute the neutron matter internal energy per particle.
        self.nm_e2a_int = []
        #: Attribute the symmetric matter internal energy per particle.
        self.sm_e2a_int = []
        #: Attribute the neutron matter energy per particle.
        self.nm_e2a = []
        #: Attribute the symmetric matter energy per particle.
        self.sm_e2a = []
        #: Attribute the neutron matter pairing gap.
        self.nm_gap = []
        #: Attribute the symmetric matter pairing gap.
        self.sm_gap = []
        #: Attribute the neutron matter pressure.
        self.nm_pre = []
        #: Attribute the symmetric matter pressure.
        self.sm_pre = []
        #: Attribute the neutron matter enthalpy per particle.
        self.nm_h2a = []
        #: Attribute the symmetric matter enthalpy per particle.
        self.sm_h2a = []
        #: Attribute the symmetric matter enthalpy density.
        self.sm_h2v = []
        #: Attribute the neutron matter enthalpy density.
        self.nm_h2v = []
        #: Attribute the neutron matter sound speed (c_s/c)^2.
        self.nm_cs2 = []
        #: Attribute the symmetric matter sound speed (c_s/c)^2.
        self.sm_cs2 = []
        #
        if nuda.env.verb: print("Exit init_self()")
        #
        return self


