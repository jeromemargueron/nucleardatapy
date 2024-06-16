import os
import sys
import numpy as np  # 1.15.0

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nudy

def models_micro():
    """
    Returns a list with the name of the models available in this toolkit and
    print them all.
    """
    models = [ '1998-VAR-AM-APR', '2008-AFDMC-NM', '2008-QMC-NM-swave', '2008-QMC-NM-AV4', \
             '2009-dQMC-NM', '2010-NM-Hebeler', '2013-QMC-NM', '2014-AFQMC-NM', '2016-QMC-NM', \
             '2016-MBPT-AM', '2018-QMC-NM', '2020-MBPT-AM-DHSL59', '2020-MBPT-AM-DHSL69', \
             '2023-MBPT-AM' ]
    print('models available in the toolkit:',models)
    models_lower = [ item.lower() for item in models ]
    return models, models_lower

class SetupMicro():
    """
    Instantiate the object with microscopic results choosen by the toolkit practitioner. This choice is defined in the variable model. If not defined, it is taken to be the APR equation of state by default.

    ...

    Attributes
    ----------
    model : str, optional
       The model to consider. Choose between: 1998-VAR-AM-APR (default), 2008-AFDMC-NM, ...
    nm_den : list
       A list with densities in neutron matter.       
    sm_den : list
       A list with densities in symmetric matter.       
    nm_kfn : list
       A list with neutron Fermi momentum in neutron matter.
    sm_kfn : list
       A list with neutron Fermi momentum in symmetric matter.
    nm_e2a : list
       A list with energy per particle in neutron matter.
    nm_e2a_err : list
       A list with uncertainties for the energy per particle in neutron matter.
    sm_e2a : list
       A list with energy per particle in symmetric matter.
    sm_e2a_err : list
       A list with uncertainties for the energy per particle in symmetric matter.
    nm_gap : list
       A list with pairing gap in neutron matter.
    sm_gap : list
       A list with pairing gap in symmetric matter.
    nm_pre : list
       A list with pressure in neutron matter.
    nm_pre_err : list
       A list with uncertainties for the pressure in neutron matter.
    sm_pre : list
       A list with pressure in symmetric matter.
    sm_pre_err : list
       A list with uncertainties for the pressure in symmetric matter.
    """
    #
    def __init__( self, model = '1998-VAR-AM-APR' ):
        """
        Parameters
        ----------
        model : str, optional
        The model to consider. Choose between: 1998-VAR-AM-APR (default), 2008-AFDMC-NM, ...
        """
        #
        if nudy.env.verb: print("Enter SetupMicro()")
        #
        self.model = model
        if nudy.env.verb: print("model:",model)
        #
        self.nm_den = []
        self.sm_den = []
        self.nm_kfn = []
        self.sm_kfn = []
        self.nm_e2a = []
        self.nm_e2a_err = []
        self.sm_e2a = []
        self.sm_e2a_err = []
        self.sm_gap = []
        self.nm_gap = []
        self.nm_pre = []
        self.nm_pre_err = []
        self.sm_pre = []
        self.sm_pre_err = []
        #self.gap_sm=np.zeros_like( self.den )
        #self.gap_nm = np.zeros_like( self.den )
        #self.pre_nm = np.zeros_like( self.den )
        #self.pre_nm_err = np.zeros_like( self.den )
        #self.pre_sm = np.zeros_like( self.den )
        #self.pre_sm_err = np.zeros_like( self.den )
        #
        models, models_lower = models_micro()
        #
        if model.lower() not in models_lower:
            print('The model name ',model,' is not in the list of models.')
            print('list of models:',models)
            print('-- Exit the code --')
            exit()
        #
        if model.lower() == '1998-var-am-apr':
            #
            file_in = os.path.join(nudy.param.path_data,'micro/1998-VAR-AM-APR.dat')
            if nudy.env.verb: print('Reads file:',file_in)
            self.ref = 'Akmal, Pandaripande and Ravenhall, Phys. Rev. C 58, 1804 (1998)'
            self.label = 'APR'
            self.note = "write here notes about this EOS."
            self.nm_den, self.sm_e2a, self.nm_e2a = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.sm_den = self.nm_den
            self.nm_kfn = nudy.fermi_gas.kfn( self.nm_den )
            self.sm_kfn = nudy.fermi_gas.kfn( nudy.cst.half * self.nm_den )
            self.nm_e2a_err = np.abs( 0.01 * self.nm_e2a )
            self.sm_e2a_err = np.abs( 0.01 * self.sm_e2a )
            #
        elif model.lower() == '2008-afdmc-nm':
            #
            file_in = os.path.join(nudy.param.path_data,'micro/2008-AFDMC-NM.dat')
            if nudy.env.verb: print('Reads file:',file_in)
            self.ref = 'A. Fabrocini, S. Fantoni, A.Y. Illarionov, and K.E. Schmidt, Phys. Rev. Lett. 95, 192501 (2005); A. Fabrocini, S. Fantoni, A.Y. Illarionov, and K.E. Schmidt, Nuc. Phys. A 803, 137 (2008)'
            self.label = 'AFDMC-2008'
            self.note = ""
            self.nm_kfn, gap2ef, gap2ef_err, e2effg, e2effg_err \
                = np.loadtxt( file_in, usecols=(0,1,2,3,4), unpack = True )
            self.nm_den     = nudy.fermi_gas.density( self.nm_kfn )
            self.nm_e2a     = e2effg * nudy.fermi_gas.effg( self.nm_kfn )
            self.nm_e2a_err = e2effg_err * nudy.fermi_gas.effg( self.nm_kfn )
            self.nm_gap     = gap2ef * nudy.fermi_gas.ef( self.nm_kfn )
            self.nm_gap_err = gap2ef_err * nudy.fermi_gas.ef( self.nm_kfn )
            #
        elif model.lower() == '2008-qmc-nm-av4':
            #
            file_in = os.path.join(nudy.param.path_data,'micro/2008-QMC-NM-AV4.dat')
            if nudy.env.verb: print('Reads file:',file_in)
            self.ref = 'A. Gezerlis and J. Carlson PRC 81, 025803 (2010)'
            self.label = 'QMC-AV4-2008'
            self.note = ""
            self.nm_kfn, gap2ef, gap2ef_err, e2effg, e2effg_err \
                = np.loadtxt( file_in, usecols=(0,1,2,3,4), unpack = True )
            self.nm_den     = nudy.fermi_gas.density( self.nm_kfn )
            self.nm_e2a     = e2effg * nudy.fermi_gas.effg( self.nm_kfn )
            self.nm_e2a_err = e2effg_err * nudy.fermi_gas.effg( self.nm_kfn )
            self.nm_gap     = gap2ef * nudy.fermi_gas.ef( self.nm_kfn )
            self.nm_gap_err = gap2ef_err * nudy.fermi_gas.ef( self.nm_kfn )
            #
        elif model.lower() == '2008-qmc-nm-swave':
            #
            file_in = os.path.join(nudy.param.path_data,'micro/2008-QMC-NM-swave.dat')
            if nudy.env.verb: print('Reads file:',file_in)
            self.ref = 'A. Gezerlis and J. Carlson PRC 81, 025803 (2010)'
            self.label = 'QMC-swave-2008'
            self.note = ""
            self.nm_kfn, gap2ef, gap2ef_err, e2effg, e2effg_err \
                = np.loadtxt( file_in, usecols=(0,1,2,3,4), unpack = True )
            self.nm_den     = nudy.fermi_gas.density( self.nm_kfn )
            self.nm_e2a     = e2effg * nudy.fermi_gas.effg( self.nm_kfn )
            self.nm_e2a_err = e2effg_err * nudy.fermi_gas.effg( self.nm_kfn )
            self.nm_gap     = gap2ef * nudy.fermi_gas.ef( self.nm_kfn )
            self.nm_gap_err = gap2ef_err * nudy.fermi_gas.ef( self.nm_kfn )
            #
        elif model.lower() == '2009-dqmc-nm':
            #
            file_in = os.path.join(nudy.param.path_data,'micro/2009-dQMC-NM.dat')
            if nudy.env.verb: print('Reads file:',file_in)
            self.ref = ''
            self.label = 'dQMC-2009'
            self.note = ""
            self.nm_kfn, gap2ef, gap2ef_err, e2effg, e2effg_err \
                = np.loadtxt( file_in, usecols=(0,1,2,3,4), unpack = True )
            self.nm_den     = nudy.fermi_gas.density( self.nm_kfn )
            self.nm_e2a     = e2effg * nudy.fermi_gas.effg( self.nm_kfn )
            self.nm_e2a_err = e2effg_err * nudy.fermi_gas.effg( self.nm_kfn )
            self.nm_gap     = gap2ef * nudy.fermi_gas.ef( self.nm_kfn )
            self.nm_gap_err = gap2ef_err * nudy.fermi_gas.ef( self.nm_kfn )
            #
        elif model.lower() == '2010-nm-hebeler':
            #
            file_in = os.path.join(nudy.param.path_data,'micro/2010-NM-Hebeler.dat')
            if nudy.env.verb: print('Reads file:',file_in)
            self.ref = 'K. Hebeler, PRL 105, 161102 (2010)'
            self.label = 'Hebeler-2010'
            self.note = "chiral NN forces with SRG and leading 3N forces."
            self.nm_den, self.nm_pre = np.loadtxt( file_in, usecols=(0,1), unpack = True )
            self.nm_kfn = nudy.fermi_gas.kfn( self.nm_den )
            self.nm_pre_err = np.abs( 0.01 * self.nm_pre )
            #
        elif model.lower() == '2013-qmc-nm':
            #
            file_in = os.path.join(nudy.param.path_data,'micro/2013-QMC-NM.dat')
            if nudy.env.verb: print('Reads file:',file_in)
            self.ref = 'I. Tews et al., PRL 110, 032504 (2013)'
            self.label = 'QMC-2013'
            self.note = "write here notes about this EOS."
            self.nm_den, self.nm_e2a_low, self.nm_e2a_up, self.nm_pre_low, self.nm_pre_up \
                = np.loadtxt( file_in, usecols=(0,1,2,3,4), unpack = True )
            self.nm_kfn = nudy.fermi_gas.kfn( self.nm_den )
            self.nm_e2a = 0.5 * ( self.nm_e2a_up + self.nm_e2a_low )
            self.nm_e2a_err = 0.5 * ( self.nm_e2a_up - self.nm_e2a_low )
            self.nm_pre = 0.5 * ( self.nm_pre_up + self.nm_pre_low )
            self.nm_pre_err = 0.5 * ( self.nm_pre_up - self.nm_pre_low )
            #
        elif model.lower() == '2014-afqmc-nm':
            #
            file_in = os.path.join(nudy.param.path_data,'micro/2014-AFQMC-NM.dat')
            if nudy.env.verb: print('Reads file:',file_in)
            self.ref = 'A. Bulgac PRL 113, 182503 (2014)'
            self.label = 'AFQMC-2014'
            self.note = "write here notes about this EOS."
            self.nm_den, self.nm_e2a_2bf, self.nm_e2a_23bf \
                = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.nm_e2a = self.nm_e2a_23bf
            self.nm_kfn = nudy.fermi_gas.kfn( self.nm_den )
            self.nm_e2a_err = np.abs( 0.01 * self.nm_e2a )
            #
        elif model.lower() == '2016-qmc-nm':
            #
            file_in = os.path.join(nudy.param.path_data,'micro/2016-QMC-NM.dat')
            if nudy.env.verb: print('Reads file:',file_in)
            self.ref = ''
            self.label = 'QMC-2016'
            self.note = ""
            self.nm_den, self.nm_e2a_low, self.nm_e2a_up \
                = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.nm_kfn = nudy.fermi_gas.kfn( self.nm_den )
            self.nm_e2a = 0.5 * ( self.nm_e2a_up + self.nm_e2a_low )
            self.nm_e2a_err = 0.5 * ( self.nm_e2a_up - self.nm_e2a_low )
            #
        elif model.lower() == '2016-mbpt-am':
            #
            self.ref = 'PRC (2016)'
            self.label = 'MBPT-2016'
            self.note = ""
            # read the results for the 7 hamiltonians
            length = np.zeros( (11), dtype=int )
            den = np.zeros( (11,35) )
            e2a = np.zeros( (10,11,35) )
            e2a_up = np.zeros( (11,35) )
            e2a_low = np.zeros( (11,35) )
            e2a_av = np.zeros( (11,35) )
            e2a_err = np.zeros( (11,35) )
            for i in range(0,11):
                beta = i/10.0
                if i<10:
                    file_in = os.path.join(nudy.param.path_data,'micro/2016-MBPT-AM/EOS_spec_4_beta_0.'+str(i)+'.txt')
                if i==10:
                    file_in = os.path.join(nudy.param.path_data,'micro/2016-MBPT-AM/EOS_spec_4_beta_1.0.txt')
                if nudy.env.verb: print('Reads file:',file_in)
                deni, e2a_1, e2a_2, e2a_3, e2a_4, e2a_5, e2a_6, e2a_7 = np.genfromtxt( file_in, usecols = (0, 1, 2, 3, 4, 5, 6, 7), comments='#', unpack = True)
                length[i] = len(deni)
                den[i,0:length[i]] = deni
                den_n = deni * (1.0+beta)/2.0
                e2a[1,i,0:length[i]] = e2a_1
                e2a[2,i,0:length[i]] = e2a_2
                e2a[3,i,0:length[i]] = e2a_3
                e2a[4,i,0:length[i]] = e2a_4
                e2a[5,i,0:length[i]] = e2a_5
                e2a[6,i,0:length[i]] = e2a_6
                e2a[7,i,0:length[i]] = e2a_7
                # performs average and compute boundaries
                e2a_up[i,0:length[i]] = e2a_1
                e2a_low[i,0:length[i]] = e2a_1
                for j in range(length[i]):
                    for k in range(2,8):
                        if e2a[k,i,j] > e2a_up[i,j]: e2a_up[i,j] = e2a[k,i,j]
                        if e2a[k,i,j] < e2a_low[i,j]: e2a_low[i,j] = e2a[k,i,j]
                    e2a_av[i,j] = 0.5* ( e2a_up[i,j] + e2a_low[i,j] )
                    e2a_err[i,j] = 0.5* ( e2a_up[i,j] - e2a_low[i,j] )
            if nudy.env.verb: print('length:',length[:])
            # SM
            self.sm_den = den[0,:]
            self.sm_kfn = nudy.fermi_gas.kfn( nudy.cst.half * self.sm_den )
            self.sm_e2a_up = e2a_up[0,:]
            self.sm_e2a_low = e2a_low[0,:]
            self.sm_e2a = e2a_av[0,:]
            self.sm_e2a_err = e2a_err[0,:]
            # NM
            self.nm_den = den[10,:]
            self.nm_kfn = nudy.fermi_gas.kfn( self.nm_den )
            self.nm_e2a_up = e2a_up[10,:]
            self.nm_e2a_low = e2a_low[10,:]
            self.nm_e2a = e2a_av[10,:]
            self.nm_e2a_err = e2a_err[10,:]
            #
        elif model.lower() == '2018-qmc-nm':
            #
            file_in = os.path.join(nudy.param.path_data,'micro/2018-QMC-NM.dat')
            if nudy.env.verb: print('Reads file:',file_in)
            self.ref = ''
            self.label = 'QMC-2018'
            self.note = ""
            self.nm_den, self.nm_e2a_low, self.nm_e2a_up, self.nm_e2a, self.nm_e2a_err \
                = np.loadtxt( file_in, usecols=(0,1,2,3,4), unpack = True )
            self.nm_kfn = nudy.fermi_gas.kfn( self.nm_den )
            #
        elif model.lower() == '2020-mbpt-am-dhsl59':
            #
            file_in1 = os.path.join(nudy.param.path_data,'micro/2020-MBPT-SM-DHSL59.dat')
            file_in2 = os.path.join(nudy.param.path_data,'micro/2020-MBPT-NM-DHSL59.dat')
            if nudy.env.verb: print('Reads file1:',file_in1)
            if nudy.env.verb: print('Reads file2:',file_in2)
            self.ref = 'PRC (2020)'
            self.label = 'MBPT-2020-DHSL59'
            self.note = ""
            self.sm_kfn, self.sm_den, Kin, HF_tot, Scnd_tot, Trd_tot, Fth_tot, self.sm_e2a \
                 = np.loadtxt( file_in1, usecols = (0, 1, 2, 3, 4, 5, 6, 7), comments='#', unpack = True)
            self.sm_e2a_err = np.abs( 0.01 * self.sm_e2a )
            self.nm_kfn, self.nm_den, Kin, HF_tot, Scnd_tot, Trd_tot, Fth_tot, self.nm_e2a \
                 = np.loadtxt( file_in2, usecols = (0, 1, 2, 3, 4, 5, 6, 7), comments='#', unpack = True)
            self.nm_e2a_err = np.abs( 0.01 * self.nm_e2a )
            #
        elif model.lower() == '2020-mbpt-am-dhsl69':
            #
            file_in1 = os.path.join(nudy.param.path_data,'micro/2020-MBPT-SM-DHSL69.dat')
            file_in2 = os.path.join(nudy.param.path_data,'micro/2020-MBPT-NM-DHSL69.dat')
            if nudy.env.verb: print('Reads file1:',file_in1)
            if nudy.env.verb: print('Reads file2:',file_in2)
            self.ref = 'PRC (2020)'
            self.label = 'MBPT-2020-DHSL69'
            self.note = ""
            self.sm_kfn, self.sm_den, Kin, HF_tot, Scnd_tot, Trd_tot, Fth_tot, self.sm_e2a \
                 = np.loadtxt( file_in1, usecols = (0, 1, 2, 3, 4, 5, 6, 7), comments='#', unpack = True)
            self.sm_e2a_err = np.abs( 0.01 * self.sm_e2a )
            self.nm_kfn, self.nm_den, Kin, HF_tot, Scnd_tot, Trd_tot, Fth_tot, self.nm_e2a \
                 = np.loadtxt( file_in2, usecols = (0, 1, 2, 3, 4, 5, 6, 7), comments='#', unpack = True)
            self.nm_e2a_err = np.abs( 0.01 * self.nm_e2a )
            #
        elif model.lower() == '2023-mbpt-am':
            #
            file_in1 = os.path.join(nudy.param.path_data,'micro/2023-MBPT-SM.csv')
            file_in2 = os.path.join(nudy.param.path_data,'micro/2023-MBPT-NM.csv')
            if nudy.env.verb: print('Reads file1:',file_in1)
            if nudy.env.verb: print('Reads file2:',file_in2)
            self.ref = 'PRC (2023)'
            self.label = 'MBPT-2023'
            self.note = ""
            self.sm_den, self.sm_e2a_lo, self.sm_e2a_lo_err, self.sm_e2a_nlo, self.sm_e2a_nlo_err, \
                self.sm_e2a_n2lo, self.sm_e2a_n2lo_err, self.sm_e2a_n3lo, self.sm_e2a_n3lo_err \
                = np.loadtxt( file_in1, usecols = (0, 1, 2, 3, 4, 5, 6, 7, 8), delimiter=',', comments='#', unpack = True)
            self.sm_kfn = nudy.fermi_gas.kfn( nudy.cst.half * self.sm_den )
            self.sm_e2a = self.sm_e2a_n3lo
            self.sm_e2a_err = self.sm_e2a_n3lo_err
            self.nm_den, self.nm_e2a_lo, self.nm_e2a_lo_err, self.nm_e2a_nlo, self.nm_e2a_nlo_err, \
                self.nm_e2a_n2lo, self.nm_e2a_n2lo_err, self.nm_e2a_n3lo, self.nm_e2a_n3lo_err \
                = np.loadtxt( file_in2, usecols = (0, 1, 2, 3, 4, 5, 6, 7, 8), delimiter=',', comments='#', unpack = True)
            self.nm_kfn = nudy.fermi_gas.kfn( self.nm_den )
            self.nm_e2a = self.nm_e2a_n3lo
            self.nm_e2a_err = self.nm_e2a_n3lo_err
            #
        self.den_unit = 'fm$^{-3}$'
        self.kfn_unit = 'fm$^{-1}$'
        self.e2a_unit = 'MeV'
        self.pre_unit = 'MeV fm$^{-3}$'
        self.gap_unit = 'MeV'
        #
        if nudy.env.verb: print("Exit SetupMicro()")

