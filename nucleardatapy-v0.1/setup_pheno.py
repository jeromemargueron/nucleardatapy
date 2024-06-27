import os
import sys
import numpy as np  # 1.15.0

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nudy

def models_pheno():
    """
    Return a list of models available in this toolkit and print them all on the prompt.

    :return: The list of models with can be 'Skyrme', 'NLRH', 'DDRH', 'DDRHF'.
    :rtype: list[str].
    """
    #
    if nudy.env.verb: print("\nEnter models_pheno()")
    #
    models = [ 'Skyrme', 'NLRH', 'DDRH', 'DDRHF' ]
    print('Phenomenological models available in the toolkit:',models)
    models_lower = [ item.lower() for item in models ]
    #
    if nudy.env.verb: print("Exit models_pheno()")
    #
    return models, models_lower

def params_pheno( model ):
    """
    Return a list with the parameterizations available in 
    this toolkit for a given model and print them all on the prompt.

    :param model: The type of model for which there are parametrizations. \
    They should be chosen among the following options: 'Skyrme', 'NLRH', \
    'DDRH', 'DDRHF'.
    :type model: str.
    :return: The list of parametrizations. \
    If `models` == 'skyrme': 'BSK14', \
    'BSK16', 'BSK17', 'BSK27', 'F-', 'F+', 'F0', 'FPL', 'LNS', 'LNS1', 'LNS5', \
    'NRAPR', 'RATP', 'SAMI', 'SGII', 'SIII', 'SKGSIGMA', 'SKI2', 'SKI4', 'SKMP', \
    'SKMS', 'SKO', 'SKOP', 'SKP', 'SKRSIGMA', 'SKX', 'Skz2', 'SLY4', 'SLY5', \
    'SLY230A', 'SLY230B', 'SV', 'T6', 'T44', 'UNEDF0', 'UNEDF1'. \
    If `models` == 'NLRH': 'NL-SH', 'NL3', 'NL3II', 'PK1', 'PK1R', 'TM1'. \
    If `models` == 'DDRH': 'DDME1', 'DDME2', 'DDMEd', 'PKDD', 'TW99'. \
    If `models` == 'DDRHF': 'PKA1', 'PKO1', 'PKO2', 'PKO3'.
    :rtype: list[str].
    """
    #
    if nudy.env.verb: print("\nEnter params_pheno()")
    #
    print('For model:',model)
    if model.lower() == 'skyrme':
        params = [ 'BSK14', 'BSK16', 'BSK17', 'BSK27', 'F-', \
            'F+', 'F0', 'FPL', 'LNS', 'LNS1', 'LNS5', 'NRAPR', 'RATP', \
            'SAMI', 'SGII', 'SIII', 'SKGSIGMA', 'SKI2', 'SKI4', 'SKMP', \
            'SKMS', 'SKO', 'SKOP', 'SKP', 'SKRSIGMA', 'SKX', 'Skz2', \
            'SLY4', 'SLY5', 'SLY230A', 'SLY230B', 'SV', 'T6', 'T44', \
            'UNEDF0', 'UNEDF1']
    elif model.lower() == 'nlrh':
        params = [ 'NL-SH', 'NL3', 'NL3II', 'PK1', 'PK1R', 'TM1' ]
    elif model.lower() == 'ddrh':
        params = [ 'DDME1', 'DDME2', 'DDMEd', 'PKDD', 'TW99' ]
    elif model.lower() == 'ddrhf':
        params = [ 'PKA1', 'PKO1', 'PKO2', 'PKO3' ]
    print('Parameters available in the toolkit:',params)
    params_lower = [ item.lower() for item in params ]
    #
    if nudy.env.verb: print("Exit params_pheno()")
    #
    return params, params_lower

class SetupPheno():
    """
    Instantiate the object with results based on phenomenological\
    interactions and choosen by the toolkit practitioner. \
    This choice is defined in the variables `model` and `param`.

    If `models` == 'skyrme', `param` can be: 'BSK14', \
    'BSK16', 'BSK17', 'BSK27', 'F-', 'F+', 'F0', 'FPL', 'LNS', 'LNS1', 'LNS5', \
    'NRAPR', 'RATP', 'SAMI', 'SGII', 'SIII', 'SKGSIGMA', 'SKI2', 'SKI4', 'SKMP', \
    'SKMS', 'SKO', 'SKOP', 'SKP', 'SKRSIGMA', 'SKX', 'Skz2', 'SLY4', 'SLY5', \
    'SLY230A', 'SLY230B', 'SV', 'T6', 'T44', 'UNEDF0', 'UNEDF1'. 

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
        if nudy.env.verb: print("\nEnter SetupPheno()")
        #
        #: Attribute model.
        self.model = model
        if nudy.env.verb: print("model:",model)
        #: Attribute param.
        self.param = param
        if nudy.env.verb: print("param:",param)
        #
        #: Attribute neutron matter density.
        self.nm_den = []
        #: Attribute symmetric matter density.
        self.sm_den = []
        #: Attribute neutron matter Fermi momentum.
        self.nm_kfn = []
        #: Attribute symmetric matter Fermi momentum.
        self.sm_kfn = []
        #: Attribute neutron matter energy per particle.
        self.nm_e2a = []
        #: Attribute symmetric matter energy per particle.
        self.sm_e2a = []
        #: Attribute neutron matter pairing gap.
        self.nm_gap = []
        #: Attribute symmetric matter pairing gap.
        self.sm_gap = []
        #: Attribute neutron matter pressure.
        self.nm_pre = []
        #: Attribute symmetric matter pressure.
        self.sm_pre = []
        #: Attribute neutron matter sound speed (c_s/c)^2.
        self.nm_cs2 = []
        #: Attribute symmetric matter sound speed (c_s/c)^2.
        self.sm_cs2 = []
        #
        models, models_lower = models_pheno( )
        #
        if model.lower() not in models_lower:
            print('The model name ',model,' is not in the list of models.')
            print('list of models:',models)
            print('-- Exit the code --')
            exit()
        #
        params, params_lower = params_pheno( model = model )
        #
        if param.lower() not in params_lower:
            print('The param set ',param,' is not in the list of param.')
            print('list of param:',params)
            print('-- Exit the code --')
            exit()
        #            
        if model.lower() == 'skyrme':
            #
            file_in1 = os.path.join(nudy.param.path_data,'eos/pheno/Skyrme/'+param+'-SM.dat')
            file_in2 = os.path.join(nudy.param.path_data,'eos/pheno/Skyrme/'+param+'-NM.dat')
            if nudy.env.verb: print('Reads file1:',file_in1)
            if nudy.env.verb: print('Reads file2:',file_in2)
            #: Attribute providing the full reference to the paper to be citted.
            self.ref = ''
            #: Attribute providing the label the data is references for figures.
            self.label = 'SKY-'+param
            #: Attribute providing additional notes about the data.
            self.note = "write here notes about this EOS."
            self.sm_den, self.sm_kfn, self.sm_e2a, a, self.sm_pre, self.sm_cs2 = np.loadtxt( file_in1, usecols=(0,1,2,3,4,5), comments='#', unpack = True )
            self.nm_den, self.nm_kfn, self.nm_e2a, a, self.nm_pre, self.nm_cs2 = np.loadtxt( file_in2, usecols=(0,1,2,3,4,5), comments='#', unpack = True )
            #
#        elif model.lower() == 'gogny':
            #
#            pass
            #
        elif model.lower() == 'nlrh':
            #
            file_in1 = os.path.join(nudy.param.path_data,'eos/pheno/nlrh/'+param+'-SM.dat')
            file_in2 = os.path.join(nudy.param.path_data,'eos/pheno/nlrh/'+param+'-NM.dat')
            if nudy.env.verb: print('Reads file1:',file_in1)
            if nudy.env.verb: print('Reads file2:',file_in2)
            self.ref = ''
            self.label = 'NLRH-'+param
            self.note = "write here notes about this EOS."
            self.sm_den, self.sm_kfn, self.sm_e2a, self.sm_pre, self.sm_cs2 = np.loadtxt( file_in1, usecols=(0,1,2,3,4), comments='#', unpack = True )
            self.nm_den, self.nm_kfn, self.nm_e2a, self.nm_pre, self.nm_cs2 = np.loadtxt( file_in2, usecols=(0,1,2,3,4), comments='#', unpack = True )
            #
        elif model.lower() == 'ddrh':
            #
#            pass
            #
            file_in1 = os.path.join(nudy.param.path_data,'eos/pheno/ddrh/'+param+'-SM.dat')
            file_in2 = os.path.join(nudy.param.path_data,'eos/pheno/ddrh/'+param+'-NM.dat')
            if nudy.env.verb: print('Reads file1:',file_in1)
            if nudy.env.verb: print('Reads file2:',file_in2)
            self.ref = ''
            self.label = 'DDRH-'+param
            self.note = "write here notes about this EOS."
            self.sm_den, self.sm_kfn, self.sm_e2a, self.sm_pre, self.sm_cs2 = np.loadtxt( file_in1, usecols=(0,1,2,3,4), comments='#', unpack = True )
            self.nm_den, self.nm_kfn, self.nm_e2a, self.nm_pre, self.nm_cs2 = np.loadtxt( file_in2, usecols=(0,1,2,3,4), comments='#', unpack = True )
            #
            #
        elif model.lower() == 'ddrhf':
            #
            file_in1 = os.path.join(nudy.param.path_data,'eos/pheno/ddrhf/'+param+'-SM.dat')
            file_in2 = os.path.join(nudy.param.path_data,'eos/pheno/ddrhf/'+param+'-NM.dat')
            if nudy.env.verb: print('Reads file1:',file_in1)
            if nudy.env.verb: print('Reads file2:',file_in2)
            self.ref = ''
            self.label = 'DDRH-'+param
            self.note = "write here notes about this EOS."
            self.sm_den, self.sm_kfn, self.sm_e2a, self.sm_pre, self.sm_cs2 = np.loadtxt( file_in1, usecols=(0,1,2,3,4), comments='#', unpack = True )
            self.nm_den, self.nm_kfn, self.nm_e2a, self.nm_pre, self.nm_cs2 = np.loadtxt( file_in2, usecols=(0,1,2,3,4), comments='#', unpack = True )
            #

        self.den_unit = 'fm$^{-3}$'
        self.kfn_unit = 'fm$^{-1}$'
        self.e2a_unit = 'MeV'
        self.pre_unit = 'MeV fm$^{-3}$'
        self.gap_unit = 'MeV'
        #
        if nudy.env.verb: print("Exit SetupPheno()")
    #
    def print_outputs( self ):
        """
        Method which print outputs on terminal's screen.
        """
        print("")
        #
        if nudy.env.verb: print("Enter print_outputs()")
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
        if any(self.nm_den): print(f"   nm_den: {np.round(self.nm_den,2)} in {self.den_unit}")
        if any(self.nm_kfn): print(f"   nm_kfn: {np.round(self.nm_kfn,2)} in {self.kfn_unit}")
        if any(self.nm_e2a): print(f"   nm_e2a: {np.round(self.nm_e2a,2)} in {self.e2a_unit}")
        if any(self.nm_gap): print(f"   nm_gap: {np.round(self.nm_gap,2)} in {self.gap_unit}")
        #
        if nudy.env.verb: print("Exit print_outputs()")
        #

