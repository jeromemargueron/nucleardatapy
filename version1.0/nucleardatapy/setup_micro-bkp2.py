import os
import sys
import numpy as np  # 1.15.0
from scipy.interpolate import CubicSpline

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

nsat = 0.16
mnuc2 = 939.0

def uncertainty_stat(den):
    return 0.07*(den/nsat)

def models_micro():
    """
    Return a list with the name of the models available in this toolkit and \
    print them all on the prompt. These models are the following ones: \
    '1981-VAR-AM-FP', '1998-VAR-AM-APR', '2006-BHF-AM*', '2008-BCS-NM', '2008-AFDMC-NM', \
    '2012-AFDMC-NM-1', '2012-AFDMC-NM-2', '2012-AFDMC-NM-3', '2012-AFDMC-NM-4', \
    '2012-AFDMC-NM-5', '2012-AFDMC-NM-6', '2012-AFDMC-NM-7', \
    '2008-QMC-NM-swave', '2010-QMC-NM-AV4', '2009-DLQMC-NM', '2010-MBPT-NM', \
    '2013-QMC-NM', '2014-AFQMC-NM', '2016-QMC-NM', '2016-MBPT-AM', \
    '2018-QMC-NM', '2019-MBPT-AM-L59', '2019-MBPT-AM-L69', \
    '2020-MBPT-AM',\
    '2024-BHF-AM-2BF-Av8p', '2024-BHF-AM-2BF-Av18', '2024-BHF-AM-2BF-BONN', '2024-BHF-AM-2BF-CDBONN', \
    '2024-BHF-AM-2BF-NSC97a', '2024-BHF-AM-2BF-NSC97b', '2024-BHF-AM-2BF-NSC97c', '2024-BHF-AM-2BF-NSC97d', \
    '2024-BHF-AM-2BF-NSC97e', '2024-BHF-AM-2BF-NSC97f', '2024-BHF-AM-2BF-SSCV14',\
    '2024-BHF-AM-23BF-Av8p', '2024-BHF-AM-23BF-Av18', '2024-BHF-AM-23BF-BONN', '2024-BHF-AM-23BF-CDBONN', \
    '2024-BHF-AM-23BF-NSC97a', '2024-BHF-AM-23BF-NSC97b', '2024-BHF-AM-23BF-NSC97c', '2024-BHF-AM-23BF-NSC97d', \
    '2024-BHF-AM-23BF-NSC97e', '2024-BHF-AM-23BF-NSC97f', '2024-BHF-AM-23BF-SSCV14',\
    '2024-BHF-AM-23BFmicro-Av18', '2024-BHF-AM-23BFmicro-BONNB', '2024-BHF-AM-23BFmicro-NSC93'\

    :return: The list of models.
    :rtype: list[str].
    """
    models = [ '1981-VAR-AM-FP', '1998-VAR-AM-APR', '2008-BCS-NM', '2008-AFDMC-NM', \
             '2008-QMC-NM-swave', '2010-QMC-NM-AV4', '2009-DLQMC-NM', '2010-MBPT-NM', \
             '2012-AFDMC-NM-1', '2012-AFDMC-NM-2', '2012-AFDMC-NM-3', '2012-AFDMC-NM-4', \
             '2012-AFDMC-NM-5', '2012-AFDMC-NM-6', '2012-AFDMC-NM-7',
             '2013-QMC-NM', '2014-AFQMC-NM', '2016-QMC-NM', '2016-MBPT-AM', \
             '2018-QMC-NM', '2019-MBPT-AM-L59', '2019-MBPT-AM-L69', \
             '2020-MBPT-AM', \
            '2024-BHF-AM-2BF-Av8p', '2024-BHF-AM-2BF-Av18', '2024-BHF-AM-2BF-BONN', '2024-BHF-AM-2BF-CDBONN', \
            '2024-BHF-AM-2BF-NSC97a', '2024-BHF-AM-2BF-NSC97b', '2024-BHF-AM-2BF-NSC97c', '2024-BHF-AM-2BF-NSC97d', \
            '2024-BHF-AM-2BF-NSC97e', '2024-BHF-AM-2BF-NSC97f', '2024-BHF-AM-2BF-SSCV14',\
            '2024-BHF-AM-23BF-Av8p', '2024-BHF-AM-23BF-Av18', '2024-BHF-AM-23BF-BONN', '2024-BHF-AM-23BF-CDBONN', \
            '2024-BHF-AM-23BF-NSC97a', '2024-BHF-AM-23BF-NSC97b', '2024-BHF-AM-23BF-NSC97c', '2024-BHF-AM-23BF-NSC97d', \
            '2024-BHF-AM-23BF-NSC97e', '2024-BHF-AM-23BF-NSC97f', '2024-BHF-AM-23BF-SSCV14' ]
    if nuda.env.verb: print('models available in the toolkit:',models)
    models_lower = [ item.lower() for item in models ]
    return models, models_lower

def func_GCR_e2a(den,a,alfa,b,beta):
    return a * (den/nsat)**alfa + b * (den/nsat)**beta

def func_GCR_pre(den,a,alfa,b,beta):
    return den * ( a * alfa * (den/nsat)**alfa + b * beta * (den/nsat)**beta )

def func_GCR_cs2(den,a,alfa,b,beta):
    dp_dn = a * alfa * ( alfa + 1.0 ) * (den/nsat)**alfa + b * beta * ( beta + 1.0 ) * (den/nsat)**beta
    enth = mnuc2 + func_GCR_e2a(den,a,alfa,b,beta) + func_GCR_pre(den,a,alfa,b,beta) / den
    return dp_dn / enth

class SetupMicro():
    """
    Instantiate the object with microscopic results choosen \
    by the toolkit practitioner.

    This choice is defined in `model`, which can chosen among \
    the following choices: \
    '1981-VAR-AM-FP', '1998-VAR-AM-APR', '2006-BHF-AM*', '2008-BCS-NM', '2008-AFDMC-NM', \
    '2008-QMC-NM-swave', '2010-QMC-NM-AV4', '2009-DLQMC-NM', '2010-MBPT-NM', \
    '2012-AFDMC-NM-1', '2012-AFDMC-NM-2', '2012-AFDMC-NM-3', '2012-AFDMC-NM-4', \
    '2012-AFDMC-NM-5', '2012-AFDMC-NM-6', '2012-AFDMC-NM-7', \
    '2013-QMC-NM', '2014-AFQMC-NM', '2016-QMC-NM', '2016-MBPT-AM', \
    '2018-QMC-NM', '2019-MBPT-AM-L59', '2019-MBPT-AM-L69', \
    '2020-MBPT-AM', \
    '2024-BHF-AM-2BF-Av8p', '2024-BHF-AM-2BF-Av18', '2024-BHF-AM-2BF-BONN', '2024-BHF-AM-2BF-CDBONN', \
    '2024-BHF-AM-2BF-NSC97a', '2024-BHF-AM-2BF-NSC97b', '2024-BHF-AM-2BF-NSC97c', '2024-BHF-AM-2BF-NSC97d', \
    '2024-BHF-AM-2BF-NSC97e', '2024-BHF-AM-2BF-NSC97f', '2024-BHF-AM-2BF-SSCV14', \
    '2024-BHF-AM-23BF-Av8p', '2024-BHF-AM-23BF-Av18', '2024-BHF-AM-23BF-BONN', '2024-BHF-AM-23BF-CDBONN', \
    '2024-BHF-AM-23BF-NSC97a', '2024-BHF-AM-23BF-NSC97b', '2024-BHF-AM-23BF-NSC97c', '2024-BHF-AM-23BF-NSC97d', \
    '2024-BHF-AM-23BF-NSC97e', '2024-BHF-AM-23BF-NSC97f', '2024-BHF-AM-23BF-SSCV14'

    :param model: Fix the name of model. Default value: '1998-VAR-AM-APR'.
    :type model: str, optional. 

    **Attributes:**
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
        if nuda.env.verb: print("Enter SetupMicro()")
        #
        #: Attribute model.
        self.model = model
        if nuda.env.verb: print("model:",model)
        #
        self = SetupMicro.init_self( self )
        #
        models, models_lower = models_micro()
        #
        if model.lower() not in models_lower:
            print('The model name ',model,' is not in the list of models.')
            print('list of models:',models)
            print('-- Exit the code --')
            exit()
        #
        if model.lower() == '1981-var-am-fp':
            #
            file_in1 = os.path.join(nuda.param.path_data,'eos/micro/1981-VAR-NM-FP.dat')
            file_in2 = os.path.join(nuda.param.path_data,'eos/micro/1981-VAR-SM-FP.dat')
            if nuda.env.verb: print('Reads file:',file_in1)
            if nuda.env.verb: print('Reads file:',file_in2)
            self.ref = 'Friedman and Pandharipande, Nucl. Phys. A. 361, 502 (1981)'
            self.note = "write here notes about this EOS."
            self.label = 'FP-1981'
            self.nm_den, self.nm_e2a = np.loadtxt( file_in1, usecols=(0,1), unpack = True )
            self.sm_den, self.sm_e2a = np.loadtxt( file_in2, usecols=(0,1), unpack = True )
            self.nm_den_min = min( self.nm_den ); self.nm_den_max = max( self.nm_den )
            self.sm_den_min = min( self.sm_den ); self.sm_den_max = max( self.sm_den )
            self.nm_e2v = self.nm_e2a * self.nm_den
            self.sm_e2v = self.sm_e2a * self.sm_den
            self.nm_kfn = nuda.kf_n( self.nm_den )
            self.sm_kfn = nuda.kf_n( nuda.cst.half * self.sm_den )
            self.nm_e2a_err = np.abs( uncertainty_stat(self.nm_den) * self.nm_e2a )
            self.sm_e2a_err = np.abs( uncertainty_stat(self.sm_den) * self.sm_e2a )
            #
            # pressure in NM
            x = np.insert( self.nm_kfn, 0, 0.0 )
            y = np.insert( self.nm_e2a, 0, 0.0 )
            cs_nm_e2a = CubicSpline( x, y )
            y_err = np.insert( self.nm_e2a_err, 0, 0.0 )
            cs_nm_e2a_err = CubicSpline( x, y_err )
            self.nm_pre = nuda.cst.three * self.nm_kfn * self.nm_den * cs_nm_e2a( self.nm_kfn, 1 )
            #self.nm_pre_err = nuda.cst.three * self.nm_kfn * self.nm_den * cs_nm_e2a_err( self.nm_kfn, 1 )
            # pressure in SM
            x = np.insert( self.sm_kfn, 0, 0.0 )
            y = np.insert( self.sm_e2a, 0, 0.0 )
            cs_sm_e2a = CubicSpline( x, y )
            y_err = np.insert( self.sm_e2a_err, 0, 0.0 )
            cs_sm_e2a_err = CubicSpline( x, y_err )
            self.sm_pre = nuda.cst.three * self.sm_kfn * self.sm_den * cs_sm_e2a( self.sm_kfn, 1 )
            #self.sm_pre_err = nuda.cst.three * self.sm_kfn * self.sm_den * cs_sm_e2a_err( self.sm_kfn, 1 )
            #
            # Symmetry energy
            self.esym_den_min = max( min( self.nm_den), min( self.sm_den) )
            self.esym_den_max = min( max( self.nm_den), max( self.sm_den) )
            self.esym_kf_min = nuda.kf( self.esym_den_min )
            self.esym_kf_max = nuda.kf( self.esym_den_max )
            #print('den_min:',self.den_min,' den_max:',self.den_max)
            #print('kf_min:',self.kf_min,' kf_max:',self.kf_max)
            kf_step = ( self.esym_kf_max - self.esym_kf_min ) / float( self.nesym )
            self.esym_kf = self.esym_kf_min + np.arange(self.nesym+1) * kf_step
            self.esym_den = nuda.den( self.esym_kf )
            #print('kf:',self.esym_kf)
            #print('den:',self.esym_den)
            self.esym_e2a = cs_nm_e2a( 2**nuda.cst.third * self.esym_kf ) - cs_sm_e2a( self.esym_kf )
            self.esym_e2a_err = np.sqrt( cs_nm_e2a_err( 2**nuda.cst.third * self.esym_kf )**2 + \
                cs_sm_e2a_err( self.esym_kf )**2 )
            #print('esym:',self.esym_e2a)
            #
            # chemical potential
            self.nm_chempot = ( np.array(self.nm_pre) + np.array(self.nm_e2v) ) / np.array(self.nm_den)
            #self.nm_chempot_err = ( np.array(self.nm_pre_err) + np.array(self.nm_e2v_err) ) / np.array(self.nm_den)
            self.sm_chempot = ( np.array(self.sm_pre) + np.array(self.sm_e2v) ) / np.array(self.sm_den)
            #self.sm_chempot_err = ( np.array(self.sm_pre_err) + np.array(self.sm_e2v_err) ) / np.array(self.nm_den)
            #
        elif model.lower() == '1998-var-am-apr':
            #
            file_in1 = os.path.join(nuda.param.path_data,'eos/micro/1998-VAR-NM-APR.dat')
            file_in2 = os.path.join(nuda.param.path_data,'eos/micro/1998-VAR-SM-APR.dat')
            if nuda.env.verb: print('Reads file:',file_in1)
            if nuda.env.verb: print('Reads file:',file_in2)
            self.ref = 'Akmal, Pandharipande and Ravenhall, Phys. Rev. C 58, 1804 (1998)'
            self.note = "write here notes about this EOS."
            self.label = 'APR-1998'
            self.linestyle = 'solid'
            self.nm_den, self.nm_e2a = np.loadtxt( file_in1, usecols=(0,1), unpack = True )
            self.sm_den, self.sm_e2a = np.loadtxt( file_in2, usecols=(0,1), unpack = True )
            self.nm_den_min = min( self.nm_den ); self.nm_den_max = max( self.nm_den )
            self.sm_den_min = min( self.sm_den ); self.sm_den_max = max( self.sm_den )
            self.nm_e2v = self.nm_e2a * self.nm_den
            self.sm_e2v = self.sm_e2a * self.sm_den
            self.nm_kfn = nuda.kf_n( self.nm_den )
            self.sm_kfn = nuda.kf_n( nuda.cst.half * self.sm_den )
            self.nm_e2a_err = np.abs( uncertainty_stat(self.nm_den) * self.nm_e2a )
            self.sm_e2a_err = np.abs( uncertainty_stat(self.sm_den) * self.sm_e2a )
            #
            # pressure in NM
            x = np.insert( self.nm_den, 0, 0.0 )
            y = np.insert( self.nm_e2a, 0, 0.0 )
            cs_nm_e2a = CubicSpline( x, y )
            y_err = np.insert( self.nm_e2a_err, 0, 0.0 )
            cs_nm_e2a_err = CubicSpline( x, y_err )
            self.nm_pre = self.nm_den**2 * cs_nm_e2a( self.nm_den, 1 )
            #y_err = np.insert( self.nm_e2a_err, 0, 0.0 )
            #cs_nm_e2a_err = CubicSpline( x, y_err )
            #self.nm_pre_err = self.nm_den**2 * cs_nm_e2a_err( self.nm_den, 1 )
            # pressure in SM
            x = np.insert( self.sm_den, 0, 0.0 )
            y = np.insert( self.sm_e2a, 0, 0.0 )
            cs_sm_e2a = CubicSpline( x, y )
            y_err = np.insert( self.sm_e2a_err, 0, 0.0 )
            cs_sm_e2a_err = CubicSpline( x, y_err )
            self.sm_pre = self.sm_den**2 * cs_sm_e2a( self.sm_den, 1 )
            #y_err = np.insert( self.sm_e2a_err, 0, 0.0 )
            #cs_sm_e2a_err = CubicSpline( x, y_err )
            #self.sm_pre_err = self.sm_den**2 * cs_sm_e2a_err( self.sm_den, 1 )
            #
            # Symmetry energy
            self.esym_den_min = max( min( self.nm_den), min( self.sm_den) )
            self.esym_den_max = min( max( self.nm_den), max( self.sm_den) )
            self.esym_kf_min = nuda.kf( self.esym_den_min )
            self.esym_kf_max = nuda.kf( self.esym_den_max )
            #print('den_min:',self.den_min,' den_max:',self.den_max)
            #print('kf_min:',self.kf_min,' kf_max:',self.kf_max)
            kf_step = ( self.esym_kf_max - self.esym_kf_min ) / float( self.nesym )
            self.esym_kf = self.esym_kf_min + np.arange(self.nesym+1) * kf_step
            self.esym_den = nuda.den( self.esym_kf )
            #print('kf:',self.esym_kf)
            #print('den:',self.esym_den)
            self.esym_e2a = cs_nm_e2a( self.esym_den ) - cs_sm_e2a( self.esym_den )
            self.esym_e2a_err = np.sqrt( cs_nm_e2a_err( 2**nuda.cst.third * self.esym_kf )**2 + \
                cs_sm_e2a_err( self.esym_kf )**2 )
            #print('esym:',self.esym_e2a)
            #
            # chemical potential
            self.nm_chempot = ( np.array(self.nm_pre) + np.array(self.nm_e2v) ) / np.array(self.nm_den)
            #self.nm_chempot_err = ( np.array(self.nm_pre_err) + np.array(self.nm_e2v_err) ) / np.array(self.nm_den)
            self.sm_chempot = ( np.array(self.sm_pre) + np.array(self.sm_e2v) ) / np.array(self.sm_den)
            #self.sm_chempot_err = ( np.array(self.sm_pre_err) + np.array(self.sm_e2v_err) ) / np.array(self.nm_den)
            #
        elif model.lower() == '2006-bhf-am':
            #
            print('not yet available')
            exit()
            file_in1 = os.path.join(nuda.param.path_data,'eos/micro/2006-BHF-NM.dat')
            file_in2 = os.path.join(nuda.param.path_data,'eos/micro/2006-BHF-SM.dat')
            if nuda.env.verb: print('Reads file:',file_in1)
            if nuda.env.verb: print('Reads file:',file_in2)
            self.ref = 'L.G. Cao, U. Lombardo, C.W. Shen, N.V. Giai, Phys. Rev. C 73, 014313 (2006)'
            self.note = ""
            self.label = 'BHF-2006'
            self.linestyle = 'solid'
            #
        elif model.lower() == '2008-bcs-nm':
            #
            file_in = os.path.join(nuda.param.path_data,'eos/micro/2008-BCS-NM.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'A. Fabrocini, S. Fantoni, A.Y. Illarionov, and K.E. Schmidt, Nuc. Phys. A 803, 137 (2008)'
            self.note = ""
            self.label = 'BCS-2008'
            self.linestyle = 'dotted'
            #self.marker = None
            self.marker = '.'
            self.nm_kfn, self.nm_gap, self.nm_chempot, self.nm_effmass \
                = np.loadtxt( file_in, usecols=(0,1,2,3), unpack = True )
            self.nm_den     = nuda.den_n( self.nm_kfn )
            self.nm_den_min = min( self.nm_den ); self.nm_den_max = max( self.nm_den )

            #self.nm_gap_err = gap2ef_err * nuda.eF_n( self.nm_kfn )

            #self.nm_e2a     = e2effg * nuda.effg( self.nm_kfn )
            #self.nm_e2a_err = e2effg_err * nuda.effg( self.nm_kfn )
            #
        elif model.lower() == '2008-afdmc-nm':
            #
            file_in = os.path.join(nuda.param.path_data,'eos/micro/2008-AFDMC-NM.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'A. Fabrocini, S. Fantoni, A.Y. Illarionov, and K.E. Schmidt, Phys. Rev. Lett. 95, 192501 (2005); A. Fabrocini, S. Fantoni, A.Y. Illarionov, and K.E. Schmidt, Nuc. Phys. A 803, 137 (2008)'
            self.note = ""
            self.label = 'AFDMC-2008'
            self.linestyle = 'solid'
            self.marker = 'D'
            self.nm_kfn, self.nm_gap, self.nm_chempot, self.nm_effmass \
                = np.loadtxt( file_in, usecols=(0,1,2,3), unpack = True )
            self.nm_den     = nuda.den_n( self.nm_kfn )
            self.nm_den_min = min( self.nm_den ); self.nm_den_max = max( self.nm_den )
            #self.nm_chempot_err = abs( 0.01 * self.nm_chempot )
            #
            # Deduce the energy from the chemical potential
            #
            eps_n = []
            # add zero density to the chemical potential (for the spline)
            x = np.insert( self.nm_kfn, 0, 0.0 )
            y1 = np.insert( self.nm_chempot, 0, 0.0 )
            y2 = np.insert( nuda.den_n(self.nm_kfn), 0, 0.0 )
            # spine the chemical potential
            cs_chempot = CubicSpline( x, y1 )
            cs_den = CubicSpline( x, y2 )
            n_int = 10
            kfn0 = 0.0
            kf = 0.0
            eps = 0.0
            for i,kfn in enumerate(self.nm_kfn):
                #print('i:',i,' kfn:',kfn)
                kstep = ( kfn - kfn0 ) / float(n_int)
                for k in range(n_int):
                    kf += kstep
                    if kf == 0.0: continue
                    eps += nuda.cst.third * cs_den( kf ) / kf * cs_chempot( kf ) * kstep
                    #print('  k:',k,' kf:',kf,' effpot:',cs_chempot( kf ),' eps:',eps)
                eps_n.append( eps )
                kfn0 = kfn
            self.nm_e2v = eps_n
            #self.nm_e2v_err = 0.01 * eps_n
            self.nm_e2a = eps_n / self.nm_den
            self.nm_e2a_err = np.abs( uncertainty_stat(self.nm_den) * self.nm_e2a )
            #self.nm_e2a_err = self.nm_e2v_err / self.nm_den
            #
            # pressure
            self.nm_pre = np.array(self.nm_den) * np.array(self.nm_chempot) - np.array(self.nm_e2v)
            #self.nm_pre_err = np.array(self.nm_den) * np.array(self.nm_chempot_err) - np.array(self.nm_e2v_err)
            #self.nm_kfn, gap2ef, gap2ef_err, e2effg, e2effg_err \
            #    = np.loadtxt( file_in, usecols=(0,1,2,3,4), unpack = True )
            #self.nm_den     = nuda.den_n( self.nm_kfn )
            #self.nm_e2a     = e2effg * nuda.effg( self.nm_kfn )
            #self.nm_e2a_err = e2effg_err * nuda.effg( self.nm_kfn )
            #self.nm_gap     = gap2ef * nuda.epsF_n( self.nm_kfn )
            #self.nm_gap_err = gap2ef_err * nuda.epsF_n( self.nm_kfn )
            #
        elif model.lower() == '2008-qmc-nm-swave':
            #
            file_in = os.path.join(nuda.param.path_data,'eos/micro/2008-QMC-NM-swave.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'A. Gezerlis and J. Carlson PRC 81, 025803 (2010)'
            self.note = ""
            self.label = 'QMC-swave-2008'
            self.linestyle = 'solid'
            self.marker = 'o'
            self.err = True
            self.nm_kfn, gap2ef, gap2ef_err, e2effg, e2effg_err \
                = np.loadtxt( file_in, usecols=(0,1,2,3,4), unpack = True )
            self.nm_den     = nuda.den_n( self.nm_kfn )
            self.nm_den_min = min( self.nm_den ); self.nm_den_max = max( self.nm_den )
            self.nm_e2a     = e2effg * nuda.effg( self.nm_kfn )
            self.nm_e2a_err = e2effg_err * nuda.effg( self.nm_kfn )
            self.nm_e2v     = self.nm_e2a * self.nm_den
            self.nm_e2v_err = self.nm_e2a_err * self.nm_den
            self.nm_gap     = gap2ef * nuda.eF_n( self.nm_kfn )
            self.nm_gap_err = gap2ef_err * nuda.eF_n( self.nm_kfn )
            #
            # pressure in NM
            x = np.insert( self.nm_kfn, 0, 0.0 )
            y = np.insert( self.nm_e2a, 0, 0.0 )
            cs_e2a = CubicSpline( x, y )
            self.nm_pre = nuda.cst.three * self.nm_kfn * self.nm_den * cs_e2a( self.nm_kfn, 1 )
            y_err = np.insert( self.nm_e2a_err, 0, 0.0 )
            cs_nm_e2a_err = CubicSpline( x, y_err )
            self.nm_pre_err = nuda.cst.three * self.nm_kfn * self.nm_den * cs_nm_e2a_err( self.nm_kfn, 1 )
            #
            # chemical potential
            self.nm_chempot = ( np.array(self.nm_pre) + np.array(self.nm_e2v) ) / np.array(self.nm_den)
            self.nm_chempot_err = ( np.array(self.nm_pre_err) + np.array(self.nm_e2v_err) ) / np.array(self.nm_den)
            #
        elif model.lower() == '2009-afdmc-nm':
            #
            file_in = os.path.join(nuda.param.path_data,'eos/micro/2009-AFDMC-NM.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'S. Gandolfi, A.Y. Illarionov, F. Pederiva, K.E. Schmidt, S. Fantoni, Phys. Rev. C 80, 045802 (2009).'
            self.note = ""
            self.label = 'AFDMC-2009'
            self.linestyle = 'solid'
            self.err = True
            self.nm_kfn, self.nm_e2a, self.nm_e2a_err \
                = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.nm_den     = nuda.den_n( self.nm_kfn )
            self.nm_den_min = min( self.nm_den ); self.nm_den_max = max( self.nm_den )
            #self.nm_e2a_err = abs( 0.01 * self.nm_e2a )
            self.nm_e2v = self.nm_e2a * self.nm_den
            self.nm_e2v_err = self.nm_e2a_err * self.nm_den
            #
            # pressure in NM
            x = np.insert( self.nm_kfn, 0, 0.0 )
            y = np.insert( self.nm_e2a, 0, 0.0 )
            cs_nm_e2a = CubicSpline( x, y )
            self.nm_pre = nuda.cst.three * self.nm_kfn * self.nm_den * cs_nm_e2a( self.nm_kfn, 1 )
            y_err = np.insert( self.nm_e2a_err, 0, 0.0 )
            cs_nm_e2a_err = CubicSpline( x, y_err )
            self.nm_pre_err = nuda.cst.three * self.nm_kfn * self.nm_den * cs_nm_e2a_err( self.nm_kfn, 1 )
            #
            # chemical potential
            self.nm_chempot = ( np.array(self.nm_pre) + np.array(self.nm_e2v) ) / np.array(self.nm_den)
            self.nm_chempot_err = ( np.array(self.nm_pre_err) + np.array(self.nm_e2v_err) ) / np.array(self.nm_den)
            #
        elif model.lower() == '2009-dlqmc-nm':
            #
            file_in = os.path.join(nuda.param.path_data,'eos/micro/2009-dQMC-NM.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'T. Abe, R. Seki, Phys. Rev. C 79, 054002 (2009)'
            self.note = ""
            self.label = 'dLQMC-2009'
            self.linestyle = 'solid'
            self.marker = 'v'
            self.err = True
            self.nm_kfn, gap2ef, gap2ef_err, e2effg, e2effg_err \
                = np.loadtxt( file_in, usecols=(0,1,2,3,4), unpack = True )
            self.nm_den     = nuda.den_n( self.nm_kfn )
            self.nm_den_min = min( self.nm_den ); self.nm_den_max = max( self.nm_den )
            self.nm_e2a     = e2effg * nuda.effg( self.nm_kfn )
            self.nm_e2a_err = e2effg_err * nuda.effg( self.nm_kfn )
            self.nm_e2v     = self.nm_e2a * self.nm_den
            self.nm_e2v_err = self.nm_e2a_err * self.nm_den
            self.nm_gap     = gap2ef * nuda.eF_n( self.nm_kfn )
            self.nm_gap_err = gap2ef_err * nuda.eF_n( self.nm_kfn )
            #
            # pressure in NM
            x = np.insert( self.nm_kfn, 0, 0.0 )
            y = np.insert( self.nm_e2a, 0, 0.0 )
            cs_e2a = CubicSpline( x, y )
            self.nm_pre = nuda.cst.three * self.nm_kfn * self.nm_den * cs_e2a( self.nm_kfn, 1 )
            y_err = np.insert( self.nm_e2a_err, 0, 0.0 )
            cs_nm_e2a_err = CubicSpline( x, y_err )
            self.nm_pre_err = nuda.cst.three * self.nm_kfn * self.nm_den * cs_nm_e2a_err( self.nm_kfn, 1 )
            #
            # chemical potential
            self.nm_chempot = ( np.array(self.nm_pre) + np.array(self.nm_e2v) ) / np.array(self.nm_den)
            self.nm_chempot_err = ( np.array(self.nm_pre_err) + np.array(self.nm_e2v_err) ) / np.array(self.nm_den)
            #
        elif model.lower() == '2010-qmc-nm-av4':
            #
            file_in = os.path.join(nuda.param.path_data,'eos/micro/2010-QMC-NM-AV4.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'A. Gezerlis and J. Carlson PRC 81, 025803 (2010)'
            self.note = ""
            self.label = 'QMC-AV4-2008'
            self.linestyle = 'solid'
            self.marker = 's'
            self.err = True
            self.nm_kfn, gap2ef, gap2ef_err, e2effg, e2effg_err \
                = np.loadtxt( file_in, usecols=(0,1,2,3,4), unpack = True )
            self.nm_den     = nuda.den_n( self.nm_kfn )
            self.nm_den_min = min( self.nm_den ); self.nm_den_max = max( self.nm_den )
            self.nm_e2a     = e2effg * nuda.effg( self.nm_kfn )
            self.nm_e2a_err = e2effg_err * nuda.effg( self.nm_kfn )
            self.nm_e2v     = self.nm_e2a * self.nm_den
            self.nm_e2v_err = self.nm_e2a_err * self.nm_den
            self.nm_gap     = gap2ef * nuda.eF_n( self.nm_kfn )
            self.nm_gap_err = gap2ef_err * nuda.eF_n( self.nm_kfn )
            #
            # pressure in NM
            x = np.insert( self.nm_kfn, 0, 0.0 )
            y = np.insert( self.nm_e2a, 0, 0.0 )
            cs_e2a = CubicSpline( x, y )
            self.nm_pre = nuda.cst.three * self.nm_kfn * self.nm_den * cs_e2a( self.nm_kfn, 1 )
            y_err = np.insert( self.nm_e2a_err, 0, 0.0 )
            cs_nm_e2a_err = CubicSpline( x, y_err )
            self.nm_pre_err = nuda.cst.three * self.nm_kfn * self.nm_den * cs_nm_e2a_err( self.nm_kfn, 1 )
            #
            # chemical potential
            self.nm_chempot = ( np.array(self.nm_pre) + np.array(self.nm_e2v) ) / np.array(self.nm_den)
            self.nm_chempot_err = ( np.array(self.nm_pre_err) + np.array(self.nm_e2v_err) ) / np.array(self.nm_den)
            #
        elif model.lower() == '2010-mbpt-nm':
            #
            file_in = os.path.join(nuda.param.path_data,'eos/micro/2010-NM-Hebeler.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'K. Hebeler, et al, Phys. Rev. Lett. 105, 161102 (2010)'
            self.note = "chiral NN forces with SRG and leading 3N forces."
            self.label = 'MBPT-2010'
            self.linestyle = 'solid'
            self.nm_den, self.nm_pre = np.loadtxt( file_in, usecols=(0,1), unpack = True )
            self.nm_den_min = min( self.nm_den ); self.nm_den_max = max( self.nm_den )
            self.nm_kfn = nuda.kf_n( self.nm_den )
            #self.nm_pre_err = np.abs( 0.01 * self.nm_pre )
            #
            # compute nm_e2v by integrating the pressure
            #
            # chemical potential
            #self.nm_chempot = ( self.nm_pre + self.nm_e2v ) / self.nm_den
            #
        elif '2012-afdmc-nm' in model.lower():
            #
            # We do not have the data for this model, but we have a fit of the data
            k=int(model.split(sep='-')[3])
            #print('k:',k)
            file_in = os.path.join(nuda.param.path_data,'eos/micro/2012-AFDMC-NM.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'S. Gandolfi, J. Carlson, S. Reddy, Phys. Rev. C 85, 032801(R) (2012).'
            self.note = "We do not have the data for this model, but we have a fit of the data."
            self.label = 'AFDMC-2012-'+str(k)
            self.linestyle = 'solid'
            ind, a, alfa, b, beta = np.loadtxt( file_in, usecols=(0,1,2,3,4), unpack = True )
            #name = np.loadtxt( file_in, usecols=(5), unpack = True )
            nmodel = np.size(alfa)
            #print('nmodel:',nmodel)
            if k < 0 or k > nmodel:
                print('issue with the model number k:',k)
                print('exit')
                exit()
            #for i in range(nmodel):
            #    print('i:',i,' ind:',ind[i],' a:',a[i],' alfa:',alfa[i],' b:',b[i],' beta:',beta[i])
            self.nm_den = 0.04 + 0.45 * np.arange(self.nden+1)/float(self.nden)
            self.nm_kfn = nuda.kf_n( self.nm_den )
            # energy in NM
            self.nm_e2a = func_GCR_e2a(self.nm_den,a[k-1],alfa[k-1],b[k-1],beta[k-1])
            self.nm_e2a_err = np.abs( uncertainty_stat(self.nm_den) * self.nm_e2a )
            self.nm_e2v = self.nm_den * self.nm_e2a
            self.nm_e2v_err = self.nm_den * self.nm_e2a_err
            # pressure in NM
            self.nm_pre = func_GCR_pre(self.nm_den,a[k-1],alfa[k-1],b[k-1],beta[k-1])
            # chemical potential
            self.nm_chempot = ( self.nm_pre + self.nm_e2v ) / self.nm_den
            # sound speed in NM
            self.nm_cs2 = func_GCR_cs2(self.nm_den,a[k-1],alfa[k-1],b[k-1],beta[k-1])
            #
        elif model.lower() == '2013-qmc-nm':
            #
            file_in = os.path.join(nuda.param.path_data,'eos/micro/2013-QMC-NM.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'I. Tews et al., PRL 110, 032504 (2013)'
            self.note = "write here notes about this EOS."
            self.label = 'QMC-2013'
            self.linestyle = 'solid'
            self.err = True
            self.nm_den, self.nm_e2a_low, self.nm_e2a_up, self.nm_pre_low, self.nm_pre_up \
                = np.loadtxt( file_in, usecols=(0,1,2,3,4), unpack = True )
            self.nm_den_min = min( self.nm_den ); self.nm_den_max = max( self.nm_den )
            self.nm_kfn = nuda.kf_n( self.nm_den )
            self.nm_e2a = 0.5 * ( self.nm_e2a_up + self.nm_e2a_low )
            self.nm_e2a_err = 0.5 * ( self.nm_e2a_up - self.nm_e2a_low )
            self.nm_e2v     = self.nm_e2a * self.nm_den
            self.nm_e2v_err = self.nm_e2a_err * self.nm_den
            self.nm_pre = 0.5 * ( self.nm_pre_up + self.nm_pre_low )
            self.nm_pre_err = 0.5 * ( self.nm_pre_up - self.nm_pre_low )
            #
            # chemical potential
            self.nm_chempot = ( np.array(self.nm_pre) + np.array(self.nm_e2v) ) / np.array(self.nm_den)
            self.nm_chempot_err = ( np.array(self.nm_pre_err) + np.array(self.nm_e2v_err) ) / np.array(self.nm_den)
            #
        elif model.lower() == '2014-afqmc-nm':
            #
            file_in = os.path.join(nuda.param.path_data,'eos/micro/2014-AFQMC-NM.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'G. Wlazłowski, J.W. Holt, S. Moroz, A. Bulgac, and K.J. Roche Phys. Rev. Lett. 113, 182503 (2014)'
            self.note = "write here notes about this EOS."
            self.label = 'AFQMC-2014'
            self.linestyle = 'solid'
            self.nm_den, self.nm_e2a_2bf, self.nm_e2a_23bf \
                = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.nm_kfn = nuda.kf_n( self.nm_den )
            self.nm_den_min = min( self.nm_den ); self.nm_den_max = max( self.nm_den )
            self.nm_e2a = self.nm_e2a_23bf
            self.nm_e2a_err = np.abs( uncertainty_stat(self.nm_den) * self.nm_e2a )
            #self.nm_e2a_err = np.abs( 0.01 * self.nm_e2a )
            self.nm_e2v     = self.nm_e2a * self.nm_den
            self.nm_e2v_err = self.nm_e2a_err * self.nm_den
            #
            # pressure in NM
            x = np.insert( self.nm_kfn, 0, 0.0 )
            y = np.insert( self.nm_e2a, 0, 0.0 )
            cs_e2a = CubicSpline( x, y )
            self.nm_pre = nuda.cst.three * self.nm_kfn * self.nm_den * cs_e2a( self.nm_kfn, 1 )
            #y_err = np.insert( self.nm_e2a_err, 0, 0.0 )
            #cs_nm_e2a_err = CubicSpline( x, y_err )
            #self.nm_pre_err = nuda.cst.three * self.nm_kfn * self.nm_den * cs_nm_e2a_err( self.nm_kfn, 1 )
            #
            # chemical potential
            self.nm_chempot = ( self.nm_pre + self.nm_e2v ) / self.nm_den
            #self.nm_chempot_err = ( np.array(self.nm_pre_err) + np.array(self.nm_e2v_err) ) / np.array(self.nm_den)
            #
        elif model.lower() == '2016-qmc-nm':
            #
            file_in = os.path.join(nuda.param.path_data,'eos/micro/2016-QMC-NM.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = ' I. Tews, S. Gandolfi, A. Gezerlis, A. Schwenk, Phys. Rev. C 93, 024305 (2016).'
            self.note = ""
            self.label = 'QMC-2016'
            self.linestyle = 'solid'
            self.err = True
            self.nm_den, self.nm_e2a_low, self.nm_e2a_up \
                = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.nm_den_min = min( self.nm_den ); self.nm_den_max = max( self.nm_den )
            self.nm_kfn = nuda.kf_n( self.nm_den )
            self.nm_e2a = 0.5 * ( self.nm_e2a_up + self.nm_e2a_low )
            self.nm_e2a_err = 0.5 * ( self.nm_e2a_up - self.nm_e2a_low )
            self.nm_e2v     = self.nm_e2a * self.nm_den
            self.nm_e2v_err = self.nm_e2a_err * self.nm_den
            #
            # pressure in NM
            x = np.insert( self.nm_kfn, 0, 0.0 )
            y = np.insert( self.nm_e2a, 0, 0.0 )
            cs_nm_e2a = CubicSpline( x, y )
            self.nm_pre = nuda.cst.three * self.nm_kfn * self.nm_den * cs_nm_e2a( self.nm_kfn, 1 )
            y_err = np.insert( self.nm_e2a_err, 0, 0.0 )
            cs_nm_e2a_err = CubicSpline( x, y_err )
            self.nm_pre_err = nuda.cst.three * self.nm_kfn * self.nm_den * cs_nm_e2a_err( self.nm_kfn, 1 )
            #
            # chemical potential
            self.nm_chempot = ( np.array(self.nm_pre) + np.array(self.nm_e2v) ) / np.array(self.nm_den)
            self.nm_chempot_err = ( np.array(self.nm_pre_err) + np.array(self.nm_e2v_err) ) / np.array(self.nm_den)
            #
        elif model.lower() == '2016-mbpt-am':
            #
            self.ref = 'C. Drischler, K. Hebeler, A. Schwenk, Phys. Rev. C 93, 054314 (2016).'
            self.note = ""
            self.label = 'MBPT-2016'
            self.linestyle = 'solid'
            self.err = True
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
                    file_in = os.path.join(nuda.param.path_data,'eos/micro/2016-MBPT-AM/EOS_spec_4_beta_0.'+str(i)+'.txt')
                if i==10:
                    file_in = os.path.join(nuda.param.path_data,'eos/micro/2016-MBPT-AM/EOS_spec_4_beta_1.0.txt')
                if nuda.env.verb: print('Reads file:',file_in)
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
            if nuda.env.verb: print('length:',length[:])
            # NM
            self.nm_den = den[10,:]
            self.nm_den_min = min( self.nm_den ); self.nm_den_max = max( self.nm_den )
            self.nm_kfn = nuda.kf_n( self.nm_den )
            self.nm_e2a_up = e2a_up[10,:]
            self.nm_e2a_low = e2a_low[10,:]
            self.nm_e2a = e2a_av[10,:]
            self.nm_e2a_err = e2a_err[10,:]
            self.nm_e2v     = self.nm_e2a * self.nm_den
            self.nm_e2v_err = self.nm_e2a_err * self.nm_den
            # SM
            self.sm_den = den[0,:]
            self.sm_den_min = min( self.sm_den ); self.sm_den_max = max( self.sm_den )
            self.sm_kfn = nuda.kf_n( nuda.cst.half * self.sm_den )
            self.sm_e2a_up = e2a_up[0,:]
            self.sm_e2a_low = e2a_low[0,:]
            self.sm_e2a = e2a_av[0,:]
            self.sm_e2a_err = e2a_err[0,:]
            self.sm_e2v     = self.sm_e2a * self.sm_den
            self.sm_e2v_err = self.sm_e2a_err * self.sm_den
            #
            # Note: here I define the pressure as the derivative of the centroid energy
            # It would however be better to compute the presure for each models and only
            # after that, estimate the centroid and uncertainty.
            #
            # pressure in NM
            x = np.insert( self.nm_den, 0, 0.0 )
            y = np.insert( self.nm_e2a, 0, 0.0 )
            cs_nm_e2a = CubicSpline( x, y )
            self.nm_pre = self.nm_den**2 * cs_nm_e2a( self.nm_den, 1 )
            y_err = np.insert( self.nm_e2a_err, 0, 0.0 )
            cs_nm_e2a_err = CubicSpline( x, y_err )
            self.nm_pre_err = self.nm_den**2 * cs_nm_e2a_err( self.nm_den, 1 )
            # pressure in SM
            x = np.insert( self.sm_den, 0, 0.0 )
            y = np.insert( self.sm_e2a, 0, 0.0 )
            cs_sm_e2a = CubicSpline( x, y )
            self.sm_pre = self.sm_den**2 * cs_sm_e2a( self.sm_den, 1 )
            y_err = np.insert( self.sm_e2a_err, 0, 0.0 )
            cs_sm_e2a_err = CubicSpline( x, y_err )
            self.sm_pre_err = self.sm_den**2 * cs_sm_e2a_err( self.sm_den, 1 )
            #
            # Symmetry energy
            self.esym_den_min = max( min( self.nm_den), min( self.sm_den) )
            self.esym_den_max = min( max( self.nm_den), max( self.sm_den) )
            self.esym_kf_min = nuda.kf( self.esym_den_min )
            self.esym_kf_max = nuda.kf( self.esym_den_max )
            #print('den_min:',self.den_min,' den_max:',self.den_max)
            #print('kf_min:',self.kf_min,' kf_max:',self.kf_max)
            den_step = ( self.esym_den_max - self.esym_den_min ) / float( self.nesym )
            self.esym_den = self.esym_den_min + np.arange(self.nesym+1) * den_step
            self.esym_kf = nuda.kf( self.esym_den )
            #print('kf:',self.esym_kf)
            #print('den:',self.esym_den)
            self.esym_e2a = cs_nm_e2a( self.esym_den ) - cs_sm_e2a( self.esym_den )
            self.esym_e2a_err = np.sqrt( cs_nm_e2a_err( self.esym_den )**2 + cs_sm_e2a_err( self.esym_den )**2 )
            #print('esym:',self.esym_e2a)
            #
            # chemical potential
            self.nm_chempot = ( np.array(self.nm_pre) + np.array(self.nm_e2v) ) / np.array(self.nm_den)
            self.nm_chempot_err = ( np.array(self.nm_pre_err) + np.array(self.nm_e2v_err) ) / np.array(self.nm_den)
            #
        elif model.lower() == '2018-qmc-nm':
            #
            file_in = os.path.join(nuda.param.path_data,'eos/micro/2018-QMC-NM.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'I. Tews, J. Carlson, S. Gandolfi, S. Reddy, Astroph. J. 860(2), 149 (2018).'
            self.note = ""
            self.label = 'QMC-2018'
            self.linestyle = 'solid'
            self.err = True
            self.nm_den, self.nm_e2a_low, self.nm_e2a_up, self.nm_e2a, self.nm_e2a_err \
                = np.loadtxt( file_in, usecols=(0,1,2,3,4), unpack = True )
            self.nm_den_min = min( self.nm_den ); self.nm_den_max = max( self.nm_den )
            self.nm_kfn = nuda.kf_n( self.nm_den )
            self.nm_e2v     = self.nm_e2a * self.nm_den
            self.nm_e2v_err = self.nm_e2a_err * self.nm_den
            #
            # pressure in NM
            x = np.insert( self.nm_kfn, 0, 0.0 )
            y = np.insert( self.nm_e2a, 0, 0.0 )
            cs_nm_e2a = CubicSpline( x, y )
            self.nm_pre = nuda.cst.three * self.nm_kfn * self.nm_den * cs_nm_e2a( self.nm_kfn, 1 )
            y_err = np.insert( self.nm_e2a_err, 0, 0.0 )
            cs_nm_e2a_err = CubicSpline( x, y_err )
            self.nm_pre_err = nuda.cst.three * self.nm_kfn * self.nm_den * cs_nm_e2a_err( self.nm_kfn, 1 )
            #
            # chemical potential
            self.nm_chempot = ( np.array(self.nm_pre) + np.array(self.nm_e2v) ) / np.array(self.nm_den)
            self.nm_chempot_err = ( np.array(self.nm_pre_err) + np.array(self.nm_e2v_err) ) / np.array(self.nm_den)
            #
        elif model.lower() == '2019-mbpt-am-l59':
            #
            # here, the L59 case is compute alone, it would be interesting to compute the uncertainty
            # in the previous MBPT calculation (based on H1-H7) adding this new calculation.
            #
            file_in1 = os.path.join(nuda.param.path_data,'eos/micro/2020-MBPT-SM-DHSL59.dat')
            file_in2 = os.path.join(nuda.param.path_data,'eos/micro/2020-MBPT-NM-DHSL59.dat')
            if nuda.env.verb: print('Reads file1:',file_in1)
            if nuda.env.verb: print('Reads file2:',file_in2)
            self.ref = 'C. Drischler, K. Hebeler, A. Schwenk, Phys. Rev. Lett. 122, 042501 (2019)'
            self.note = ""
            self.label = 'MBPT-2019-L59'
            self.linestyle = 'solid'
            self.sm_kfn, self.sm_den, Kin, HF_tot, Scnd_tot, Trd_tot, Fth_tot, self.sm_e2a \
                 = np.loadtxt( file_in1, usecols = (0, 1, 2, 3, 4, 5, 6, 7), comments='#', unpack = True)
            self.sm_den_min = min( self.sm_den ); self.sm_den_max = max( self.sm_den )
            self.sm_e2a_err = np.abs( uncertainty_stat(self.sm_den) * self.sm_e2a )
            self.sm_e2v     = self.sm_e2a * self.sm_den
            self.sm_e2v_err = self.sm_e2a_err * self.sm_den
            self.nm_kfn, self.nm_den, Kin, HF_tot, Scnd_tot, Trd_tot, Fth_tot, self.nm_e2a \
                 = np.loadtxt( file_in2, usecols = (0, 1, 2, 3, 4, 5, 6, 7), comments='#', unpack = True)
            self.nm_den_min = min( self.nm_den ); self.nm_den_max = max( self.nm_den )
            self.nm_e2a_err = np.abs( uncertainty_stat(self.nm_den) * self.nm_e2a )
            self.nm_e2v     = self.nm_e2a * self.nm_den
            self.nm_e2v_err = self.nm_e2a_err * self.nm_den
            #
            # pressure in NM
            x = np.insert( self.nm_den, 0, 0.0 )
            y = np.insert( self.nm_e2a, 0, 0.0 )
            cs_nm_e2a = CubicSpline( x, y )
            y_err = np.insert( self.nm_e2a_err, 0, 0.0 )
            cs_nm_e2a_err = CubicSpline( x, y_err )
            self.nm_pre = self.nm_den**2 * cs_nm_e2a( self.nm_den, 1 )
            #y_err = np.insert( self.nm_e2a_err, 0, 0.0 )
            #cs_nm_e2a_err = CubicSpline( x, y_err )
            #self.nm_pre_err = self.nm_den**2 * cs_nm_e2a_err( self.nm_den, 1 )
            # pressure in SM
            x = np.insert( self.sm_den, 0, 0.0 )
            y = np.insert( self.sm_e2a, 0, 0.0 )
            cs_sm_e2a = CubicSpline( x, y )
            y_err = np.insert( self.sm_e2a_err, 0, 0.0 )
            cs_sm_e2a_err = CubicSpline( x, y_err )
            self.sm_pre = nuda.cst.three * self.sm_kfn * self.sm_den * cs_sm_e2a( self.sm_den, 1 )
            #y_err = np.insert( self.sm_e2a_err, 0, 0.0 )
            #cs_sm_e2a_err = CubicSpline( x, y_err )
            #self.sm_pre_err = self.sm_den**2 * cs_sm_e2a_err( self.sm_den, 1 )
            #
            # Symmetry energy
            self.esym_den_min = max( min( self.nm_den), min( self.sm_den) )
            self.esym_den_max = min( max( self.nm_den), max( self.sm_den) )
            self.esym_kf_min = nuda.kf( self.esym_den_min )
            self.esym_kf_max = nuda.kf( self.esym_den_max )
            #print('den_min:',self.den_min,' den_max:',self.den_max)
            #print('kf_min:',self.kf_min,' kf_max:',self.kf_max)
            den_step = ( self.esym_den_max - self.esym_den_min ) / float( self.nesym )
            self.esym_den = self.esym_den_min + np.arange(self.nesym+1) * den_step
            self.esym_kf = nuda.kf( self.esym_den )
            #print('kf:',self.esym_kf)
            #print('den:',self.esym_den)
            self.esym_e2a = cs_nm_e2a( self.esym_den ) - cs_sm_e2a( self.esym_den )
            self.esym_e2a_err = np.sqrt( cs_nm_e2a_err( self.esym_den )**2 + cs_sm_e2a_err( self.esym_den )**2 )
            #print('esym:',self.esym_e2a)
            #
            # chemical potential
            self.nm_chempot = ( np.array(self.nm_pre) + np.array(self.nm_e2v) ) / np.array(self.nm_den)
            #self.nm_chempot_err = ( np.array(self.nm_pre_err) + np.array(self.nm_e2v_err) ) / np.array(self.nm_den)
            #
        elif model.lower() == '2019-mbpt-am-l69':
            #
            # same remarck as for L59
            #
            file_in1 = os.path.join(nuda.param.path_data,'eos/micro/2020-MBPT-SM-DHSL69.dat')
            file_in2 = os.path.join(nuda.param.path_data,'eos/micro/2020-MBPT-NM-DHSL69.dat')
            if nuda.env.verb: print('Reads file1:',file_in1)
            if nuda.env.verb: print('Reads file2:',file_in2)
            self.ref = 'C. Drischler, K. Hebeler, A. Schwenk, Phys. Rev. Lett. 122, 042501 (2019)'
            self.note = ""
            self.label = 'MBPT-2019-L69'
            self.linestyle = 'solid'
            self.sm_kfn, self.sm_den, Kin, HF_tot, Scnd_tot, Trd_tot, Fth_tot, self.sm_e2a \
                 = np.loadtxt( file_in1, usecols = (0, 1, 2, 3, 4, 5, 6, 7), comments='#', unpack = True)
            self.sm_den_min = min( self.sm_den ); self.sm_den_max = max( self.sm_den )
            self.sm_e2a_err = np.abs( uncertainty_stat(self.sm_den) * self.sm_e2a )
            self.sm_e2v     = self.sm_e2a * self.sm_den
            self.sm_e2v_err = self.sm_e2a_err * self.sm_den
            self.nm_kfn, self.nm_den, Kin, HF_tot, Scnd_tot, Trd_tot, Fth_tot, self.nm_e2a \
                 = np.loadtxt( file_in2, usecols = (0, 1, 2, 3, 4, 5, 6, 7), comments='#', unpack = True)
            self.nm_den_min = min( self.nm_den ); self.nm_den_max = max( self.nm_den )
            self.nm_e2a_err = np.abs( uncertainty_stat(self.nm_den) * self.nm_e2a )
            self.nm_e2v     = self.nm_e2a * self.nm_den
            self.nm_e2v_err = self.nm_e2a_err * self.nm_den
            #
            # pressure in NM
            x = np.insert( self.nm_den, 0, 0.0 )
            y = np.insert( self.nm_e2a, 0, 0.0 )
            cs_nm_e2a = CubicSpline( x, y )
            y_err = np.insert( self.nm_e2a_err, 0, 0.0 )
            cs_nm_e2a_err = CubicSpline( x, y_err )
            self.nm_pre = self.nm_den**2 * cs_nm_e2a( self.nm_den, 1 )
            #y_err = np.insert( self.nm_e2a_err, 0, 0.0 )
            #cs_nm_e2a_err = CubicSpline( x, y_err )
            #self.nm_pre_err = self.nm_den**2 * cs_nm_e2a_err( self.nm_den, 1 )
            # pressure in SM
            x = np.insert( self.sm_den, 0, 0.0 )
            y = np.insert( self.sm_e2a, 0, 0.0 )
            cs_sm_e2a = CubicSpline( x, y )
            y_err = np.insert( self.sm_e2a_err, 0, 0.0 )
            cs_sm_e2a_err = CubicSpline( x, y_err )
            self.sm_pre = self.sm_den**2 * cs_sm_e2a( self.sm_den, 1 )
            #y_err = np.insert( self.sm_e2a_err, 0, 0.0 )
            #cs_sm_e2a_err = CubicSpline( x, y_err )
            #self.sm_pre_err = self.sm_den**2 * cs_sm_e2a_err( self.nm_den, 1 )
            #
            # Symmetry energy
            self.esym_den_min = max( min( self.nm_den), min( self.sm_den) )
            self.esym_den_max = min( max( self.nm_den), max( self.sm_den) )
            self.esym_kf_min = nuda.kf( self.esym_den_min ); self.esym_kf_max = nuda.kf( self.esym_den_max )
            den_step = ( self.esym_den_max - self.esym_den_min ) / float( self.nesym )
            self.esym_den = self.esym_den_min + np.arange(self.nesym+1) * den_step
            self.esym_kf = nuda.kf( self.esym_den )
            self.esym_e2a = cs_nm_e2a( self.esym_den ) - cs_sm_e2a( self.esym_den )
            self.esym_e2a_err = np.sqrt( cs_nm_e2a_err( self.esym_den )**2 + cs_sm_e2a_err( self.esym_den )**2 )
            #
            # chemical potential
            self.nm_chempot = ( np.array(self.nm_pre) + np.array(self.nm_e2v) ) / np.array(self.nm_den)
            #self.nm_chempot_err = ( np.array(self.nm_pre_err) + np.array(self.nm_e2v_err) ) / np.array(self.nm_den)
            self.sm_chempot = ( np.array(self.sm_pre) + np.array(self.sm_e2v) ) / np.array(self.sm_den)
            #self.sm_chempot_err = ( np.array(self.sm_pre_err) + np.array(self.sm_e2v_err) ) / np.array(self.nm_den)
            #
        elif model.lower() == '2020-mbpt-am':
            #
            file_in1 = os.path.join(nuda.param.path_data,'eos/micro/2023-MBPT-SM.csv')
            file_in2 = os.path.join(nuda.param.path_data,'eos/micro/2023-MBPT-NM.csv')
            if nuda.env.verb: print('Reads file1:',file_in1)
            if nuda.env.verb: print('Reads file2:',file_in2)
            self.ref = 'C. Drischler, R.J. Furnstahl, J.A. Melendez, D.R. Phillips, Phys. Rev. Lett. 125(20), 202702 (2020).; C. Drischler, J. A. Melendez, R. J. Furnstahl, and D. R. Phillips, Phys. Rev. C 102, 054315'
            self.note = ""
            self.label = 'MBPT-2020'
            self.linestyle = 'solid'
            self.every = 4
            self.err = True
            self.sm_den, self.sm_e2a_lo, self.sm_e2a_lo_err, self.sm_e2a_nlo, self.sm_e2a_nlo_err, \
                self.sm_e2a_n2lo, self.sm_e2a_n2lo_err, self.sm_e2a_n3lo, self.sm_e2a_n3lo_err \
                = np.loadtxt( file_in1, usecols = (0, 1, 2, 3, 4, 5, 6, 7, 8), delimiter=',', comments='#', unpack = True)
            self.sm_den_min = min( self.sm_den ); self.sm_den_max = max( self.sm_den )
            self.sm_kfn = nuda.kf_n( nuda.cst.half * self.sm_den )
            self.sm_e2a = self.sm_e2a_n3lo
            self.sm_e2a_err = self.sm_e2a_n3lo_err
            self.sm_e2v     = self.sm_e2a * self.sm_den
            self.sm_e2v_err = self.sm_e2a_err * self.sm_den
            self.nm_den, self.nm_e2a_lo, self.nm_e2a_lo_err, self.nm_e2a_nlo, self.nm_e2a_nlo_err, \
                self.nm_e2a_n2lo, self.nm_e2a_n2lo_err, self.nm_e2a_n3lo, self.nm_e2a_n3lo_err \
                = np.loadtxt( file_in2, usecols = (0, 1, 2, 3, 4, 5, 6, 7, 8), delimiter=',', comments='#', unpack = True)
            self.nm_den_min = min( self.nm_den ); self.nm_den_max = max( self.nm_den )
            self.nm_kfn = nuda.kf_n( self.nm_den )
            self.nm_e2a = self.nm_e2a_n3lo
            self.nm_e2a_err = self.nm_e2a_n3lo_err
            self.nm_e2v     = self.nm_e2a * self.nm_den
            self.nm_e2v_err = self.nm_e2a_err * self.nm_den
            #
            # pressure in NM
            x = np.insert( self.nm_den, 0, 0.0 )
            y = np.insert( self.nm_e2a, 0, 0.0 )
            cs_nm_e2a = CubicSpline( x, y )
            self.nm_pre = self.nm_den**2 * cs_nm_e2a( self.nm_den, 1 )
            y_err = np.insert( self.nm_e2a_err, 0, 0.0 )
            cs_nm_e2a_err = CubicSpline( x, y_err )
            self.nm_pre_err = self.nm_den**2 * cs_nm_e2a_err( self.nm_den, 1 )
            # pressure in SM
            x = np.insert( self.sm_den, 0, 0.0 )
            y = np.insert( self.sm_e2a, 0, 0.0 )
            cs_sm_e2a = CubicSpline( x, y )
            self.sm_pre = self.sm_den**2 * cs_sm_e2a( self.sm_den, 1 )
            y_err = np.insert( self.sm_e2a_err, 0, 0.0 )
            cs_sm_e2a_err = CubicSpline( x, y_err )
            self.sm_pre_err = self.sm_den**2 * cs_sm_e2a_err( self.sm_den, 1 )
            #
            # Symmetry energy
            self.esym_den_min = max( min( self.nm_den), min( self.sm_den) )
            self.esym_den_max = min( max( self.nm_den), max( self.sm_den) )
            self.esym_kf_min = nuda.kf( self.esym_den_min ); self.esym_kf_max = nuda.kf( self.esym_den_max )
            den_step = ( self.esym_den_max - self.esym_den_min ) / float( self.nesym )
            self.esym_den = self.esym_den_min + np.arange(self.nesym+1) * den_step
            self.esym_kf = nuda.kf( self.esym_den )
            self.esym_e2a = cs_nm_e2a( self.esym_den ) - cs_sm_e2a( self.esym_den )
            self.esym_e2a_err = np.sqrt( cs_nm_e2a_err( self.esym_den )**2 + cs_sm_e2a_err( self.esym_den )**2 )
            #
            # chemical potential
            self.nm_chempot = ( np.array(self.nm_pre) + np.array(self.nm_e2v) ) / np.array(self.nm_den)
            self.nm_chempot_err = ( np.array(self.nm_pre_err) + np.array(self.nm_e2v_err) ) / np.array(self.nm_den)
            self.sm_chempot = ( np.array(self.sm_pre) + np.array(self.sm_e2v) ) / np.array(self.sm_den)
            self.sm_chempot_err = ( np.array(self.sm_pre_err) + np.array(self.sm_e2v_err) ) / np.array(self.nm_den)
            #
        elif '2024-bhf-am' in model.lower():
            #
            # 2BF
            if model.lower() == '2024-bhf-am-2bf-av8p':
                file_in1 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-SM-2BF/spin_isosp_Av8p2BF.dat')
                file_in2 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-NM-2BF/spin_isosp_Av8p2BF.dat')
                self.label = 'BHF-2024-2BF-Av8p'
            elif model.lower() == '2024-bhf-am-2bf-av18':
                file_in1 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-SM-2BF/spin_isosp_Av182BF.dat')
                file_in2 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-NM-2BF/spin_isosp_Av182BF.dat')
                self.label = 'BHF-2024-2BF-Av18'
            elif model.lower() == '2024-bhf-am-2bf-bonn':
                file_in1 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-SM-2BF/spin_isosp_BONN2BF.dat')
                file_in2 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-NM-2BF/spin_isosp_BONN2BF.dat')
                self.label = 'BHF-2024-2BF-Bonn'
            elif model.lower() == '2024-bhf-am-2bf-cdbonn':
                file_in1 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-SM-2BF/spin_isosp_CDBONN2BF.dat')
                file_in2 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-NM-2BF/spin_isosp_CDBONN2BF.dat')
                self.label = 'BHF-2024-2BF-CDBonn'
            elif model.lower() == '2024-bhf-am-2bf-sscv14':
                file_in1 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-SM-2BF/spin_isosp_SSCV142BF.dat')
                file_in2 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-NM-2BF/spin_isosp_SSCV142BF.dat')
                self.label = 'BHF-2024-2BF-SSCV14'
            elif model.lower() == '2024-bhf-am-2bf-nsc97a':
                file_in1 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-SM-2BF/spin_isosp_NSC97a2BF.dat')
                file_in2 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-NM-2BF/spin_isosp_NSC97a2BF.dat')
                self.label = 'BHF-2024-2BF-NSC97a'
            elif model.lower() == '2024-bhf-am-2bf-nsc97b':
                file_in1 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-SM-2BF/spin_isosp_NSC97b2BF.dat')
                file_in2 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-NM-2BF/spin_isosp_NSC97b2BF.dat')
                self.label = 'BHF-2024-2BF-NSC97b'
            elif model.lower() == '2024-bhf-am-2bf-nsc97c':
                file_in1 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-SM-2BF/spin_isosp_NSC97c2BF.dat')
                file_in2 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-NM-2BF/spin_isosp_NSC97c2BF.dat')
                self.label = 'BHF-2024-2BF-NSC97c'
            elif model.lower() == '2024-bhf-am-2bf-nsc97d':
                file_in1 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-SM-2BF/spin_isosp_NSC97d2BF.dat')
                file_in2 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-NM-2BF/spin_isosp_NSC97d2BF.dat')
                self.label = 'BHF-2024-2BF-NSC97d'
            elif model.lower() == '2024-bhf-am-2bf-nsc97e':
                file_in1 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-SM-2BF/spin_isosp_NSC97e2BF.dat')
                file_in2 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-NM-2BF/spin_isosp_NSC97e2BF.dat')
                self.label = 'BHF-2024-2BF-NSC97e'
            elif model.lower() == '2024-bhf-am-2bf-nsc97f':
                file_in1 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-SM-2BF/spin_isosp_NSC97f2BF.dat')
                file_in2 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-NM-2BF/spin_isosp_NSC97f2BF.dat')
                self.label = 'BHF-2024-2BF-NSC97f'
            # 2+3BF
            elif model.lower() == '2024-bhf-am-23bf-av8p':
                file_in1 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-SM-23BF/spin_isosp_Av8p23BF.dat')
                file_in2 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-NM-23BF/spin_isosp_Av8p23BF.dat')
                self.label = 'BHF-2024-23BF-Av8p'
            elif model.lower() == '2024-bhf-am-23bf-av18':
                file_in1 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-SM-23BF/spin_isosp_Av1823BF.dat')
                file_in2 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-NM-23BF/spin_isosp_Av1823BF.dat')
                self.label = 'BHF-2024-23BF-Av18'
            elif model.lower() == '2024-bhf-am-23bfmicro-av18':
                file_in1 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-SM-23BF/spin_isosp_Av1823BFmicro.dat')
                file_in2 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-NM-23BF/spin_isosp_Av1823BFmicro.dat')
                self.label = 'BHF-2024-23BFmicro-Av18'
            elif model.lower() == '2024-bhf-am-23bf-bonn':
                file_in1 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-SM-23BF/spin_isosp_BONN23BF.dat')
                file_in2 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-NM-23BF/spin_isosp_BONN23BF.dat')
                self.label = 'BHF-2024-23BF-Bonn'
            elif model.lower() == '2024-bhf-am-23bfmicro-bonnb':
                file_in1 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-SM-23BF/spin_isosp_BONNB23BFmicro.dat')
                file_in2 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-NM-23BF/spin_isosp_BONNB23BFmicro.dat')
                self.label = 'BHF-2024-23BFMicro-BonnB'
            elif model.lower() == '2024-bhf-am-23bf-cdbonn':
                file_in1 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-SM-23BF/spin_isosp_CDBONN23BF.dat')
                file_in2 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-NM-23BF/spin_isosp_CDBONN23BF.dat')
                self.label = 'BHF-2024-23BF-CDBonn'
            elif model.lower() == '2024-bhf-am-23bf-sscv14':
                file_in1 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-SM-23BF/spin_isosp_SSCV1423BF.dat')
                file_in2 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-NM-23BF/spin_isosp_SSCV1423BF.dat')
                self.label = 'BHF-2024-23BF-SSCV14'
            elif model.lower() == '2024-bhf-am-23bfmicro-nsc93':
                file_in1 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-SM-23BF/spin_isosp_NSC9323BFmicro.dat')
                file_in2 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-NM-23BF/spin_isosp_NSC9323BFmicro.dat')
                self.label = 'BHF-2024-23BFmicro-NSC93'
            elif model.lower() == '2024-bhf-am-23bf-nsc97a':
                file_in1 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-SM-23BF/spin_isosp_NSC97a23BF.dat')
                file_in2 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-NM-23BF/spin_isosp_NSC97a23BF.dat')
                self.label = 'BHF-2024-23BF-NSC97a'
            elif model.lower() == '2024-bhf-am-23bf-nsc97b':
                file_in1 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-SM-23BF/spin_isosp_NSC97b23BF.dat')
                file_in2 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-NM-23BF/spin_isosp_NSC97b23BF.dat')
                self.label = 'BHF-2024-23BF-NSC97b'
            elif model.lower() == '2024-bhf-am-23bf-nsc97c':
                file_in1 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-SM-23BF/spin_isosp_NSC97c23BF.dat')
                file_in2 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-NM-23BF/spin_isosp_NSC97c23BF.dat')
                self.label = 'BHF-2024-23BF-NSC97c'
            elif model.lower() == '2024-bhf-am-23bf-nsc97d':
                file_in1 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-SM-23BF/spin_isosp_NSC97d23BF.dat')
                file_in2 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-NM-23BF/spin_isosp_NSC97d23BF.dat')
                self.label = 'BHF-2024-23BF-NSC9d7'
            elif model.lower() == '2024-bhf-am-23bf-nsc97e':
                file_in1 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-SM-23BF/spin_isosp_NSC97e23BF.dat')
                file_in2 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-NM-23BF/spin_isosp_NSC97e23BF.dat')
                self.label = 'BHF-2024-23BF-NSC97e'
            elif model.lower() == '2024-bhf-am-23bf-nsc97f':
                file_in1 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-SM-23BF/spin_isosp_NSC97f23BF.dat')
                file_in2 = os.path.join(nuda.param.path_data,'eos/micro/2024-BHF-NM-23BF/spin_isosp_NSC97f23BF.dat')
                self.label = 'BHF-2024-23BF-NSC97f'

            if nuda.env.verb: print('Reads file:',file_in1)
            if nuda.env.verb: print('Reads file:',file_in2)
            self.ref = 'I. Vida\~na, J. Margueron, H.J. Schulze, Universe 10, 5 (2024).'
            self.note = ""
            self.linestyle = 'solid'
            self.every = 4
            self.err = False
            #
            self.sm_den, self.sm_vS0T0, self.sm_vS0T1, self.sm_vS1T0, self.sm_vS1T1, self.sm_vtot, self.sm_kin, self.sm_etot \
                = np.loadtxt( file_in1, usecols = (0, 1, 2, 3, 4, 5, 6, 7), comments='#', unpack = True)
            self.sm_den_min = min( self.sm_den ); self.sm_den_max = max( self.sm_den )
            self.sm_kfn = nuda.kf_n( nuda.cst.half * self.sm_den )
            self.sm_kf = self.sm_kfn
            self.sm_e2a = self.sm_etot
            self.sm_e2a_err = np.abs( uncertainty_stat(self.sm_den) * self.sm_e2a )
            self.sm_e2v     = self.sm_e2a * self.sm_den
            self.sm_e2v_err = self.sm_e2a_err * self.sm_den
            #
            self.nm_den, self.nm_vS0T0, self.nm_vS0T1, self.nm_vS1T0, self.nm_vS1T1, self.nm_vtot, self.nm_kin, self.nm_etot \
                = np.loadtxt( file_in2, usecols = (0, 1, 2, 3, 4, 5, 6, 7), comments='#', unpack = True)
            self.nm_den_min = min( self.sm_den ); self.sm_den_max = max( self.sm_den )
            self.nm_kfn = nuda.kf_n( self.nm_den )
            self.nm_e2a = self.nm_etot
            self.nm_e2a_err = np.abs( uncertainty_stat(self.nm_den) * self.nm_e2a )
            self.nm_e2v     = self.nm_e2a * self.nm_den
            self.nm_e2v_err = self.nm_e2a_err * self.nm_den
            #
            # pressure in SM
            x = np.insert( self.sm_den, 0, 0.0 ); y = np.insert( self.sm_e2a, 0, 0.0 )
            cs_sm_e2a = CubicSpline( x, y )
            self.sm_pre = self.sm_den**2 * cs_sm_e2a( self.sm_den, 1 )
            y_err = np.insert( self.sm_e2a_err, 0, 0.0 )
            cs_sm_e2a_err = CubicSpline( x, y_err )
            self.sm_pre_err = self.sm_den**2 * cs_sm_e2a_err( self.sm_den, 1 )
            # pressure in NM
            x = np.insert( self.nm_den, 0, 0.0 ); y = np.insert( self.nm_e2a, 0, 0.0 )
            cs_nm_e2a = CubicSpline( x, y )
            self.nm_pre = self.nm_den**2 * cs_nm_e2a( self.nm_den, 1 )
            y_err = np.insert( self.nm_e2a_err, 0, 0.0 )
            cs_nm_e2a_err = CubicSpline( x, y_err )
            self.nm_pre_err = self.nm_den**2 * cs_nm_e2a_err( self.nm_den, 1 )
            #
            # Symmetry energy
            self.esym_den_min = max( min( self.nm_den), min( self.sm_den) )
            self.esym_den_max = min( max( self.nm_den), max( self.sm_den) )
            self.esym_kf_min = nuda.kf( self.esym_den_min ); self.esym_kf_max = nuda.kf( self.esym_den_max )
            den_step = ( self.esym_den_max - self.esym_den_min ) / float( self.nesym )
            self.esym_den = self.esym_den_min + np.arange(self.nesym+1) * den_step
            self.esym_kf = nuda.kf( self.esym_den )
            self.esym_e2a = cs_nm_e2a( self.esym_den ) - cs_sm_e2a( self.esym_den )
            self.esym_e2a_err = np.sqrt( cs_nm_e2a_err( self.esym_den )**2 + cs_sm_e2a_err( self.esym_den )**2 )
            #
            # chemical potential in SM and NM
            self.sm_chempot = ( np.array(self.sm_pre) + np.array(self.sm_e2v) ) / np.array(self.sm_den)
            self.sm_chempot_err = ( np.array(self.sm_pre_err) + np.array(self.sm_e2v_err) ) / np.array(self.nm_den)
            self.nm_chempot = ( np.array(self.nm_pre) + np.array(self.nm_e2v) ) / np.array(self.nm_den)
            self.nm_chempot_err = ( np.array(self.nm_pre_err) + np.array(self.nm_e2v_err) ) / np.array(self.nm_den)
            #
            #
        self.den_unit = 'fm$^{-3}$'
        self.kf_unit = 'fm$^{-1}$'
        self.e2a_unit = 'MeV'
        self.e2v_unit = 'MeV fm$^{-3}$'
        self.pre_unit = 'MeV fm$^{-3}$'
        self.gap_unit = 'MeV'
        #
        if nuda.env.verb: print("Exit SetupMicro()")
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
        print("   self.sm_den: ",self.sm_den)
        print("   self.sm_effmass: ",self.sm_effmass)
        #if any(self.sm_den): print(f"   sm_den: {np.round(self.sm_den,3)} in {self.den_unit}")
        if self.sm_den is not None: print(f"   sm_den: {np.round(self.sm_den,3)} in {self.den_unit}")
        if self.sm_kfn is not None: print(f"   sm_kfn: {np.round(self.sm_kfn,3)} in {self.kf_unit}")
        if self.sm_chempot is not None: print(f"   sm_chempot: {np.round(self.sm_chempot,3)} in {self.e2a_unit}")
        if self.sm_effmass is not None: print(f"   sm_effmass: {np.round(self.sm_effmass,3)}")
        if self.sm_e2a is not None: print(f"   sm_e2a: {np.round(self.sm_e2a,3)} in {self.e2a_unit}")
        if self.sm_e2a_err is not None: print(f"   sm_e2a_err: {np.round(self.sm_e2a_err,3)} in {self.e2a_unit}")
        if self.sm_e2v is not None: print(f"   sm_e2v: {np.round(self.sm_e2v,3)} in {self.e2v_unit}")
        if self.sm_e2v_err is not None: print(f"   sm_e2v_err: {np.round(self.sm_e2v_err,3)} in {self.e2v_unit}")
        if self.sm_pre is not None: print(f"   sm_pre: {np.round(self.sm_pre,3)} in {self.pre_unit}")
        if self.nm_den is not None: print(f"   nm_den: {np.round(self.nm_den,3)} in {self.den_unit}")
        if self.nm_kfn is not None: print(f"   nm_kfn: {np.round(self.nm_kfn,3)} in {self.kf_unit}")
        if self.nm_chempot is not None: print(f"   nm_chempot: {np.round(self.nm_chempot,3)} in {self.e2a_unit}")
        if self.nm_effmass is not None: print(f"   nm_effmass: {np.round(self.nm_effmass,3)}")
        if self.nm_e2a is not None: print(f"   nm_e2a: {np.round(self.nm_e2a,3)} in {self.e2a_unit}")
        if self.nm_e2a_err is not None: print(f"   nm_e2a_err: {np.round(self.nm_e2a_err,3)} in {self.e2a_unit}")
        if self.nm_e2v is not None: print(f"   nm_e2v: {np.round(self.nm_e2v,3)} in {self.e2v_unit}")
        if self.nm_e2v_err is not None: print(f"   nm_e2v_err: {np.round(self.nm_e2v_err,3)} in {self.e2v_unit}")
        if self.nm_pre is not None: print(f"   nm_pre: {np.round(self.nm_pre,3)} in {self.pre_unit}")
        #
        if self.esym_den is not None: print(f"   esym_den: {np.round(self.esym_den,3)} in {self.den_unit}")
        if self.esym_kf is not None: print(f"   esym_kf: {np.round(self.esym_kf,3)} in {self.kf_unit}")
        if self.esym_e2a is not None: print(f"   esym_e2a: {np.round(self.esym_e2a,3)} in {self.e2a_unit}")
        #
        if self.nm_gap is not None: print(f"   nm_gap: {np.round(self.nm_gap,3)} in {self.gap_unit}")
        if self.nm_gap_err is not None: print(f"   nm_gap_err: {np.round(self.nm_gap_err,3)} in {self.gap_unit}")
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
        #: Attribute the number of points for the density.
        self.nden = 10; 
        #: Attribute the number of points for esym calculation.
        self.nesym = 20; 
        #: Attribute providing the full reference to the paper to be citted.
        self.ref = ''
        #: Attribute providing additional notes about the data.
        self.note = ''
        #: Attribute the neutron matter density.
        self.nm_den = None
        #: Attribute the symmetric matter density.
        self.sm_den = None
        #: Attribute the minimum of the neutron matter density.
        self.nm_den_min = None
        #: Attribute the minimum of the symmetric matter density.
        self.sm_den_min = None
        #: Attribute the maximum of the neutron matter density.
        self.nm_den_max = None
        #: Attribute the maximum of the symmetric matter density.
        self.sm_den_max = None
        #: Attribute the neutron matter neutron Fermi momentum.
        self.nm_kfn = None
        #: Attribute the symmetric matter neutron Fermi momentum.
        self.sm_kfn = None
        #: Attribute the symmetric matter Fermi momentum.
        self.nm_kf = None
        #: Attribute the symmetric matter Fermi momentum.
        self.sm_kf = None
        #: Attribute the neutron matter chemical potential.
        self.nm_chempot = None
        #: Attribute the uncertainty in the neutron matter chemical potential.
        self.nm_chempot_err = None
        #: Attribute the symmetric matter chemical potential.
        self.sm_chempot = None
        #: Attribute the uncertainty in the symmetric matter chemical potential.
        self.sm_chempot_err = None
        #: Attribute the neutron matter effective mass.
        self.nm_effmass = None
        #: Attribute the symmetric matter effective mass.
        self.sm_effmass = None
        #: Attribute the neutron matter energy per particle.
        self.nm_e2a = None
        #: Attribute the uncertainty in the neutron matter energy per particle.
        self.nm_e2a_err = None
        #: Attribute the neutron matter potential per particle in the (S=0,T=0) channel.
        self.nm_vS0T0 = None
        #: Attribute the neutron matter potential per particle in the (S=0,T=1) channel.
        self.nm_vS0T1 = None
        #: Attribute the neutron matter potential per particle in the (S=1,T=0) channel.
        self.nm_vS1T0 = None
        #: Attribute the neutron matter potential per particle in the (S=1,T=1) channel.
        self.nm_vS1T1 = None
        #: Attribute the neutron matter total potential per particle.
        self.nm_vtot = None
        #: Attribute the symmetric matter energy per particle.
        self.sm_e2a = None
        #: Attribute the uncertainty in the symmetric matter energy per particle.
        self.sm_e2a_err = None
        #: Attribute the symmetric matter energy per particle in the (S=0,T=0) channel.
        self.sm_vS0T0 = None
        #: Attribute the symmetric matter energy per particle in the (S=0,T=1) channel.
        self.sm_vS0T1 = None
        #: Attribute the symmetric matter energy per particle in the (S=1,T=0) channel.
        self.sm_vS1T0 = None
        #: Attribute the symmetric matter energy per particle in the (S=1,T=1) channel.
        self.sm_vS1T1 = None
        #: Attribute the symmetric matter total potential per particle.
        self.sm_vtot = None
        #: Attribute the neutron matter energy per unit volume.
        self.nm_e2v = None
        #: Attribute the uncertainty in the neutron matter energy per unit volume.
        self.nm_e2v_err = None
        #: Attribute the symmetric matter energy per unit volume.
        self.sm_e2v = None
        #: Attribute the uncertainty in the symmetric matter energy per unit volume.
        self.sm_e2v_err = None
        #: Attribute the neutron matter pressure.
        self.nm_pre = None
        #: Attribute the uncertainty in the neutron matter pressure.
        self.nm_pre_err = None
        #: Attribute the symmetric matter pressure.
        self.sm_pre = None
        #: Attribute the uncertainty in the symmetric matter pressure.
        self.sm_pre_err = None
        #: Attribute the neutron matter pairing gap.
        self.nm_gap = None
        #: Attribute the uncertainty in the neutron matter pairing gap.
        self.nm_gap_err = None
        #: Attribute the symmetric matter pairing gap.
        self.sm_gap = None
        #: Attribute the uncertainty in the symmetric matter pairing gap.
        self.sm_gap_err = None
        #: Attribute the density array for esym.
        self.esym_den = None
        #: Attribute the maximum of the density.
        self.esym_den_max = None
        #: Attribute the minimum of the density.
        self.esym_den_min = None
        #: Attribute the Fermi momentum array for esym.
        self.esym_kf = None
        #: Attribute the minimum of the Fermi momentum.
        self.esym_kf_min = None
        #: Attribute the maximum of the Fermi momentum.
        self.esym_kf_max = None
        #: Attribute the energy per particle for esym.
        self.esym_e2a = None
        #: Attribute the plot linestyle.
        self.linestyle = 'solid'
        #: Attribute the plot to discriminate True uncertainties from False ones.
        self.err = False
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

