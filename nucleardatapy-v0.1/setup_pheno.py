import os
import sys
import numpy as np  # 1.15.0

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nudy

def models_pheno():
    """
    Returns a list with the name of the models available in this toolkit and
    print them all.
    """
    models = [ 'Skyrme', 'NLRH', 'DDRHF' ]
    print('Phenomenological models available in the toolkit:',models)
    models_lower = [ item.lower() for item in models ]
    return models, models_lower

def params_pheno( model ):
    """
    For a given model given as input, returns a list with the name of the
    parameterizations available in this toolkit and print them all.
    """
    print('For model:',model)
    if model.lower() == 'skyrme':
        params = [ 'BSK14', 'BSK16', 'BSK17', 'BSK27', 'F-', \
            'F+', 'F0', 'FPL', 'LNS', 'LNS1', 'LNS5', 'NRAPR', 'RATP', \
            'SAMI', 'SGII', 'SIII', 'SKGSIGMA', 'SKI2', 'SKI4', 'SKMP', \
            'SKMS', 'SKO', 'SKOP', 'SKP', 'SKRSIGMA', 'SKX', 'Skz2', \
            'SLY4', 'SLY5', 'SLY230A', 'SLY230B', 'SV', 'T6', 'T44', \
            'UNEDF0', 'UNEDF1']
    elif model.lower() == 'nlrh':
        params = [ 'DDME1', 'DDME2', 'DDMEd', 'NL-SH', 'NL3', \
            'NL3II', 'PK1', 'PK1R', 'PKDD', 'TM1', 'TW99' ]
    elif model.lower() == 'ddrhf':
        params = [ 'PKA1', 'PKO1', 'PKO2', 'PKO3' ]

    print('Parameters available in the toolkit:',params)
    params_lower = [ item.lower() for item in params ]
    return params, params_lower

class SetupPheno():
    """
    Instantiate the value for the lowden data file.
    
    :param model: name of the model: '2008-AFDMC', ...
    :type model: string().
    :returns: kfn, gap, gap_err, e2a, e2a_err, etc.
    """
    #
    def __init__( self, model = 'Skyrme', param = 'SLY5' ):
        #
        if nudy.env.verb: print("Enter SetupPheno()")
        #
        self.model = model
        if nudy.env.verb: print("model:",model)
        self.param = param
        if nudy.env.verb: print("param:",param)
        #
        self.nm_den = []
        self.sm_den = []
        self.nm_kfn = []
        self.sm_kfn = []
        self.nm_e2a = []
        self.sm_e2a = []
        self.nm_kfn = []
        self.sm_kfn = []
        self.sm_gap = []
        self.nm_gap = []
        self.nm_pre = []
        self.sm_pre = []
        self.nm_cs2 = []
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
            file_in1 = os.path.join(nudy.param.path_data,'pheno/Skyrme/'+param+'-SM.dat')
            file_in2 = os.path.join(nudy.param.path_data,'pheno/Skyrme/'+param+'-NM.dat')
            if nudy.env.verb: print('Reads file1:',file_in1)
            if nudy.env.verb: print('Reads file2:',file_in2)
            self.ref = ''
            self.label = 'SKY-'+param
            self.note = "write here notes about this EOS."
            self.sm_den, self.sm_kfn, self.sm_e2a, a, self.sm_pre, self.sm_cs2 = np.loadtxt( file_in1, usecols=(0,1,2,3,4,5), unpack = True )
            self.nm_den, self.nm_kfn, self.nm_e2a, a, self.nm_pre, self.nm_cs2 = np.loadtxt( file_in2, usecols=(0,1,2,3,4,5), unpack = True )
            #
#        elif model.lower() == 'gogny':
            #
#            pass
            #
        elif model.lower() == 'nlrh':
            #
            file_in1 = os.path.join(nudy.param.path_data,'pheno/nlrh/'+param+'-SM.dat')
            file_in2 = os.path.join(nudy.param.path_data,'pheno/nlrh/'+param+'-NM.dat')
            if nudy.env.verb: print('Reads file1:',file_in1)
            if nudy.env.verb: print('Reads file2:',file_in2)
            self.ref = ''
            self.label = 'NLRH-'+param
            self.note = "write here notes about this EOS."
            self.sm_den, self.sm_kfn, self.sm_e2a, self.sm_pre, self.sm_cs2 = np.loadtxt( file_in1, usecols=(0,1,2,3,4), unpack = True )
            self.nm_den, self.nm_kfn, self.nm_e2a, self.nm_pre, self.nm_cs2 = np.loadtxt( file_in2, usecols=(0,1,2,3,4), unpack = True )
            #
#        elif model.lower() == 'ddrh':
            #
#            pass
            #
        elif model.lower() == 'ddrhf':
            #
            file_in1 = os.path.join(nudy.param.path_data,'pheno/ddrhf/'+param+'-SM.dat')
            file_in2 = os.path.join(nudy.param.path_data,'pheno/ddrhf/'+param+'-NM.dat')
            if nudy.env.verb: print('Reads file1:',file_in1)
            if nudy.env.verb: print('Reads file2:',file_in2)
            self.ref = ''
            self.label = 'DDRH-'+param
            self.note = "write here notes about this EOS."
            self.sm_den, self.sm_kfn, self.sm_e2a, self.sm_pre, self.sm_cs2 = np.loadtxt( file_in1, usecols=(0,1,2,3,4), unpack = True )
            self.nm_den, self.nm_kfn, self.nm_e2a, self.nm_pre, self.nm_cs2 = np.loadtxt( file_in2, usecols=(0,1,2,3,4), unpack = True )
            #

        self.den_unit = 'fm$^{-3}$'
        self.kfn_unit = 'fm$^{-1}$'
        self.e2a_unit = 'MeV'
        self.pre_unit = 'MeV fm$^{-3}$'
        self.gap_unit = 'MeV'
        #
        if nudy.env.verb: print("Exit SetupPheno()")

