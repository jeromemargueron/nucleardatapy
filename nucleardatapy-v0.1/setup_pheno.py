import os
import sys
import numpy as np  # 1.15.0

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nudy

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
        #
        if model.lower() == 'skyrme':
            #
            list_param = [ 'BSK14', 'BSK16', 'BSK17', 'BSK27', 'F-', 'F', \
               'F+', 'F0', 'FPL', 'LNS', 'LNS1', 'LNS5', 'NRAPR', 'RATP', \
               'SAMI', 'SGII', 'SIII', 'SKGSIGMA', 'SKI2', 'SKI4', 'SKMP', \
               'SKMS', 'SKO', 'SKOP', 'SKP', 'SKRSIGMA', 'SKX', 'Skz2', \
               'SLY4', 'SLY5', 'SLY230A', 'SLY230B', 'SV', 'T6', 'T44', \
               'UNEDF0', 'UNEDF1']
            if param in list_param:
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
#        elif model.lower() == 'nlrh':
            #
#            pass
            #
#        elif model.lower() == 'ddrh':
            #
#            pass
            #
#        elif model.lower() == 'ddrhf':
            #
#            pass
            #

        self.den_unit = 'fm$^{-3}$'
        self.kfn_unit = 'fm$^{-1}$'
        self.e2a_unit = 'MeV'
        self.gap_unit = 'MeV'
        #
        if nudy.env.verb: print("Exit SetupPheno()")

