import os
import sys
import numpy as np  # 1.15.0
from scipy.interpolate import CubicSpline

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def models_micro():
    """
    Return a list with the name of the models available in this toolkit and
    print them all on the prompt. These models are the following ones: \
    '1981-VAR-AM-FP', '1998-VAR-AM-APR', '2006-BHF-AM'*, '2008-BCS-NM', '2008-AFDMC-NM', \
    '2008-QMC-NM-swave', '2010-QMC-NM-AV4', '2009-DLQMC-NM', '2010-NM-Hebeler', \
    '2013-QMC-NM', '2014-AFQMC-NM', '2016-QMC-NM', '2016-MBPT-AM', \
    '2018-QMC-NM', '2019-MBPT-AM-DHSL59', '2019-MBPT-AM-DHSL69', \
    '2020-MBPT-AM'.

    :return: The list of models.
    :rtype: list[str].
    """
    models = [ '1981-VAR-AM-FP', '1998-VAR-AM-APR', '2008-BCS-NM', '2008-AFDMC-NM', \
             '2008-QMC-NM-swave', '2010-QMC-NM-AV4', '2009-DLQMC-NM', '2010-NM-Hebeler', \
             '2013-QMC-NM', '2014-AFQMC-NM', '2016-QMC-NM', '2016-MBPT-AM', \
             '2018-QMC-NM', '2019-MBPT-AM-DHSL59', '2019-MBPT-AM-DHSL69', \
             '2020-MBPT-AM' ]
    print('models available in the toolkit:',models)
    models_lower = [ item.lower() for item in models ]
    return models, models_lower

class SetupMicro():
    """
    Instantiate the object with microscopic results choosen \
    by the toolkit practitioner.

    This choice is defined in `model`, which can chosen among \
    the following choices: \
    '1981-VAR-AM-FP', '1998-VAR-AM-APR', '2006-BHF-AM'*, '2008-BCS-NM', '2008-AFDMC-NM', \
    '2008-QMC-NM-swave', '2010-QMC-NM-AV4', '2009-DLQMC-NM', '2010-NM-Hebeler', \
    '2013-QMC-NM', '2014-AFQMC-NM', '2016-QMC-NM', '2016-MBPT-AM', \
    '2018-QMC-NM', '2019-MBPT-AM-DHSL59', '2019-MBPT-AM-DHSL69', \
    '2020-MBPT-AM'.

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
        #: Attribute neutron matter density.
        self.nm_den = None
        #: Attribute symmetric matter density.
        self.sm_den = None
        #: Attribute minimum of the density.
        self.den_min = None
        #: Attribute maximum of the density.
        self.den_max = None
        #: Attribute minimum of the Fermi momentum.
        self.kf_min = None
        #: Attribute maximum of the Fermi momentum.
        self.kf_max = None
        #: Attribute neutron matter Fermi momentum.
        self.nm_kfn = None
        #: Attribute symmetric matter Fermi momentum.
        self.sm_kfn = None
        #: Attribute neutron matter chemical potential.
        self.nm_chempot = None
        #: Attribute symmetric matter chemical potential.
        self.sm_chempot = None
        #: Attribute neutron matter effective mass.
        self.nm_effmass = None
        #: Attribute symmetric matter effective mass.
        self.sm_effmass = None
        #: Attribute neutron matter energy per particle.
        self.nm_e2a = None
        #: Attribute uncertainty in the neutron matter energy per particle.
        self.nm_e2a_err = None
        #: Attribute symmetric matter energy per particle.
        self.sm_e2a = None
        #: Attribute uncertainty in the symmetric matter energy per particle.
        self.sm_e2a_err = None
        #: Attribute neutron matter energy per unit volume.
        self.nm_e2v = None
        #: Attribute uncertainty in the neutron matter energy per unit volume.
        self.nm_e2v_err = None
        #: Attribute symmetric matter energy per unit volume.
        self.sm_e2v = None
        #: Attribute uncertainty in the symmetric matter energy per unit volume.
        self.sm_e2v_err = None
        #: Attribute neutron matter pressure.
        self.nm_pre = None
        #: Attribute uncertainty in the neutron matter pressure.
        self.nm_pre_err = None
        #: Attribute symmetric matter pressure.
        self.sm_pre = None
        #: Attribute uncertainty in the symmetric matter pressure.
        self.sm_pre_err = None
        #: Attribute neutron matter pairing gap.
        self.nm_gap = None
        #: Attribute uncertainty in the neutron matter pairing gap.
        self.nm_gap_err = None
        #: Attribute symmetric matter pairing gap.
        self.sm_gap = None
        #: Attribute uncertainty in the symmetric matter pairing gap.
        self.sm_gap_err = None
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
            #: Attribute providing the full reference to the paper to be citted.
            self.ref = 'Friedman and Pandharipande, Nucl. Phys. A. 361, 502 (1981)'
            #: Attribute providing the label the data is references for figures.
            self.label = 'APR'
            #: Attribute providing additional notes about the data.
            self.note = "write here notes about this EOS."
            self.nm_den, self.nm_e2a = np.loadtxt( file_in1, usecols=(0,1), unpack = True )
            self.sm_den, self.sm_e2a = np.loadtxt( file_in2, usecols=(0,1), unpack = True )
            self.nm_e2v = self.nm_e2a * self.nm_den
            self.sm_e2v = self.sm_e2a * self.sm_den
            self.nm_kfn = nuda.kf_n( self.nm_den )
            self.sm_kfn = nuda.kf_n( nuda.cst.half * self.sm_den )
            self.nm_e2a_err = np.abs( 0.01 * self.nm_e2a )
            self.sm_e2a_err = np.abs( 0.01 * self.sm_e2a )
            #
            # pressure in NM
            x = np.insert( self.nm_kfn, 0, 0.0 )
            y = np.insert( self.nm_e2a, 0, 0.0 )
            cs_nm_e2a = CubicSpline( x, y )
            self.nm_pre = nuda.cst.three * self.nm_kfn * self.nm_den * cs_nm_e2a( self.nm_kfn, 1 )
            # pressure in SM
            x = np.insert( self.sm_kfn, 0, 0.0 )
            y = np.insert( self.sm_e2a, 0, 0.0 )
            cs_sm_e2a = CubicSpline( x, y )
            self.sm_pre = nuda.cst.three * self.sm_kfn * self.sm_den * cs_sm_e2a( self.sm_kfn, 1 )
            #
            # Symmetry energy
            self.den_min = max( min( self.nm_den), min( self.sm_den) )
            self.den_max = min( max( self.nm_den), max( self.sm_den) )
            self.kf_min = nuda.kf( self.den_min )
            self.kf_max = nuda.kf( self.den_max )
            #print('den_min:',self.den_min,' den_max:',self.den_max)
            #print('kf_min:',self.kf_min,' kf_max:',self.kf_max)
            nesym = 20
            kf_step = ( self.kf_max - self.kf_min ) / float( nesym )
            self.esym_kf = self.kf_min + np.arange(nesym+1) * kf_step
            self.esym_den = nuda.den( self.esym_kf )
            #print('kf:',self.esym_kf)
            #print('den:',self.esym_den)
            self.esym_e2a = cs_nm_e2a( 2**nuda.cst.third * self.esym_kf ) - cs_sm_e2a( self.esym_kf )
            #print('esym:',self.esym_e2a)
            #
            # chemical potential
            self.nm_chempot = ( np.array(self.nm_pre) + np.array(self.nm_e2v) ) / np.array(self.nm_den)
            self.sm_chempot = ( np.array(self.sm_pre) + np.array(self.sm_e2v) ) / np.array(self.sm_den)
            #
        elif model.lower() == '1998-var-am-apr':
            #
            file_in1 = os.path.join(nuda.param.path_data,'eos/micro/1998-VAR-NM-APR.dat')
            file_in2 = os.path.join(nuda.param.path_data,'eos/micro/1998-VAR-SM-APR.dat')
            if nuda.env.verb: print('Reads file:',file_in1)
            if nuda.env.verb: print('Reads file:',file_in2)
            #: Attribute providing the full reference to the paper to be citted.
            self.ref = 'Akmal, Pandharipande and Ravenhall, Phys. Rev. C 58, 1804 (1998)'
            #: Attribute providing the label the data is references for figures.
            self.label = 'APR'
            #: Attribute providing additional notes about the data.
            self.note = "write here notes about this EOS."
            self.nm_den, self.nm_e2a = np.loadtxt( file_in1, usecols=(0,1), unpack = True )
            self.sm_den, self.sm_e2a = np.loadtxt( file_in2, usecols=(0,1), unpack = True )
            self.nm_e2v = self.nm_e2a * self.nm_den
            self.sm_e2v = self.sm_e2a * self.sm_den
            self.nm_kfn = nuda.kf_n( self.nm_den )
            self.sm_kfn = nuda.kf_n( nuda.cst.half * self.sm_den )
            self.nm_e2a_err = np.abs( 0.01 * self.nm_e2a )
            self.sm_e2a_err = np.abs( 0.01 * self.sm_e2a )
            #
            # pressure in NM
            x = np.insert( self.nm_den, 0, 0.0 )
            y = np.insert( self.nm_e2a, 0, 0.0 )
            cs_nm_e2a = CubicSpline( x, y )
            self.nm_pre = self.nm_den**2 * cs_nm_e2a( self.nm_den, 1 )
            # pressure in SM
            x = np.insert( self.sm_den, 0, 0.0 )
            y = np.insert( self.sm_e2a, 0, 0.0 )
            cs_sm_e2a = CubicSpline( x, y )
            self.sm_pre = self.sm_den**2 * cs_sm_e2a( self.sm_kfn, 1 )
            #
            # Symmetry energy
            self.den_min = max( min( self.nm_den), min( self.sm_den) )
            self.den_max = min( max( self.nm_den), max( self.sm_den) )
            self.kf_min = nuda.kf( self.den_min )
            self.kf_max = nuda.kf( self.den_max )
            #print('den_min:',self.den_min,' den_max:',self.den_max)
            #print('kf_min:',self.kf_min,' kf_max:',self.kf_max)
            nesym = 20
            kf_step = ( self.kf_max - self.kf_min ) / float( nesym )
            self.esym_kf = self.kf_min + np.arange(nesym+1) * kf_step
            self.esym_den = nuda.den( self.esym_kf )
            #print('kf:',self.esym_kf)
            #print('den:',self.esym_den)
            self.esym_e2a = cs_nm_e2a( self.esym_den ) - cs_sm_e2a( self.esym_den )
            #print('esym:',self.esym_e2a)
            #
            # chemical potential
            self.nm_chempot = ( np.array(self.nm_pre) + np.array(self.nm_e2v) ) / np.array(self.nm_den)
            self.sm_chempot = ( np.array(self.sm_pre) + np.array(self.sm_e2v) ) / np.array(self.sm_den)
            #
        elif model.lower() == '2006-bhf-am':
            #
            print('not yet available')
            exit()
            file_in1 = os.path.join(nuda.param.path_data,'eos/micro/2006-BHF-NM.dat')
            file_in2 = os.path.join(nuda.param.path_data,'eos/micro/2006-BHF-SM.dat')
            if nuda.env.verb: print('Reads file:',file_in1)
            if nuda.env.verb: print('Reads file:',file_in2)
            self.ref = '.G. Cao, U. Lombardo, C.W. Shen, N.V. Giai, Phys. Rev. C 73, 014313 (2006)'
            self.label = 'BHF-2006'
            self.note = ""
            #
        elif model.lower() == '2008-bcs-nm':
            #
            file_in = os.path.join(nuda.param.path_data,'eos/micro/2008-BCS-NM.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'A. Fabrocini, S. Fantoni, A.Y. Illarionov, and K.E. Schmidt, Nuc. Phys. A 803, 137 (2008)'
            self.label = 'BCS-2008'
            self.note = ""
            self.nm_kfn, self.nm_gap, self.nm_chempot, self.nm_effmass \
                = np.loadtxt( file_in, usecols=(0,1,2,3), unpack = True )
            self.nm_den     = nuda.den_n( self.nm_kfn )

            self.nm_gap_err = gap2ef_err * nuda.eF_n( self.nm_kfn )

            #self.nm_e2a     = e2effg * nuda.effg( self.nm_kfn )
            #self.nm_e2a_err = e2effg_err * nuda.effg( self.nm_kfn )
            #
        elif model.lower() == '2008-afdmc-nm':
            #
            file_in = os.path.join(nuda.param.path_data,'eos/micro/2008-AFDMC-NM.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'A. Fabrocini, S. Fantoni, A.Y. Illarionov, and K.E. Schmidt, Phys. Rev. Lett. 95, 192501 (2005); A. Fabrocini, S. Fantoni, A.Y. Illarionov, and K.E. Schmidt, Nuc. Phys. A 803, 137 (2008)'
            self.label = 'AFDMC-2008'
            self.note = ""
            self.nm_kfn, self.nm_gap, self.nm_chempot, self.nm_effmass \
                = np.loadtxt( file_in, usecols=(0,1,2,3), unpack = True )
            self.nm_den     = nuda.den_n( self.nm_kfn )
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
            self.nm_e2a = eps_n / self.nm_den
            #
            # pressure
            self.nm_pre = np.array(self.nm_den) * np.array(self.nm_chempot) - np.array(self.nm_e2v)
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
            self.label = 'QMC-swave-2008'
            self.note = ""
            self.nm_kfn, gap2ef, gap2ef_err, e2effg, e2effg_err \
                = np.loadtxt( file_in, usecols=(0,1,2,3,4), unpack = True )
            self.nm_den     = nuda.den_n( self.nm_kfn )
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
            #
            # chemical potential
            self.nm_chempot = ( np.array(self.nm_pre) + np.array(self.nm_e2v) ) / np.array(self.nm_den)
            #
        elif model.lower() == '2009-afdmc-nm':
            #
            file_in = os.path.join(nuda.param.path_data,'eos/micro/2009-AFDMC-NM.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'S. Gandolfi, A.Y. Illarionov, F. Pederiva, K.E. Schmidt, S. Fantoni, Phys. Rev. C 80, 045802 (2009).'
            self.label = 'AFDMC-2009'
            self.note = ""
            self.nm_kfn, self.nm_e2a, self.nm_e2a_err \
                = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.nm_den     = nuda.den_n( self.nm_kfn )
            self.nm_e2v = self.nm_e2a * self.nm_den
            #
            # pressure in NM
            x = np.insert( self.nm_kfn, 0, 0.0 )
            y = np.insert( self.nm_e2a, 0, 0.0 )
            cs_e2a = CubicSpline( x, y )
            self.nm_pre = nuda.cst.three * self.nm_kfn * self.nm_den * cs_e2a( self.nm_kfn, 1 )
            #
            # chemical potential
            self.nm_chempot = ( np.array(self.nm_pre) + np.array(self.nm_e2v) ) / np.array(self.nm_den)
            #
        elif model.lower() == '2010-qmc-nm-av4':
            #
            file_in = os.path.join(nuda.param.path_data,'eos/micro/2008-QMC-NM-AV4.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'A. Gezerlis and J. Carlson PRC 81, 025803 (2010)'
            self.label = 'QMC-AV4-2008'
            self.note = ""
            self.nm_kfn, gap2ef, gap2ef_err, e2effg, e2effg_err \
                = np.loadtxt( file_in, usecols=(0,1,2,3,4), unpack = True )
            self.nm_den     = nuda.den_n( self.nm_kfn )
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
            #
            # chemical potential
            self.nm_chempot = ( np.array(self.nm_pre) + np.array(self.nm_e2v) ) / np.array(self.nm_den)
            #
        elif model.lower() == '2009-dlqmc-nm':
            #
            file_in = os.path.join(nuda.param.path_data,'eos/micro/2009-dQMC-NM.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'T. Abe, R. Seki, Phys. Rev. C 79, 054002 (2009)'
            self.label = 'dQMC-2009'
            self.note = ""
            self.nm_kfn, gap2ef, gap2ef_err, e2effg, e2effg_err \
                = np.loadtxt( file_in, usecols=(0,1,2,3,4), unpack = True )
            self.nm_den     = nuda.den_n( self.nm_kfn )
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
            #
            # chemical potential
            self.nm_chempot = ( np.array(self.nm_pre) + np.array(self.nm_e2v) ) / np.array(self.nm_den)
            #
        elif model.lower() == '2010-nm-hebeler':
            #
            file_in = os.path.join(nuda.param.path_data,'eos/micro/2010-NM-Hebeler.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'K. Hebeler, PRL 105, 161102 (2010)'
            self.label = 'Hebeler-2010'
            self.note = "chiral NN forces with SRG and leading 3N forces."
            self.nm_den, self.nm_pre = np.loadtxt( file_in, usecols=(0,1), unpack = True )
            self.nm_kfn = nuda.kf_n( self.nm_den )
            self.nm_pre_err = np.abs( 0.01 * self.nm_pre )
            #
            # chemical potential
            #self.nm_chempot = ( self.nm_pre + self.nm_e2v ) / self.nm_den
            #
        elif model.lower() == '2013-qmc-nm':
            #
            file_in = os.path.join(nuda.param.path_data,'eos/micro/2013-QMC-NM.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'I. Tews et al., PRL 110, 032504 (2013)'
            self.label = 'QMC-2013'
            self.note = "write here notes about this EOS."
            self.nm_den, self.nm_e2a_low, self.nm_e2a_up, self.nm_pre_low, self.nm_pre_up \
                = np.loadtxt( file_in, usecols=(0,1,2,3,4), unpack = True )
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
            #
        elif model.lower() == '2014-afqmc-nm':
            #
            file_in = os.path.join(nuda.param.path_data,'eos/micro/2014-AFQMC-NM.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'G. Wlazłowski, J.W. Holt, S. Moroz, A. Bulgac, and K.J. Roche Phys. Rev. Lett. 113, 182503 (2014)'
            self.label = 'AFQMC-2014'
            self.note = "write here notes about this EOS."
            self.nm_den, self.nm_e2a_2bf, self.nm_e2a_23bf \
                = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.nm_e2a = self.nm_e2a_23bf
            self.nm_kfn = nuda.kf_n( self.nm_den )
            self.nm_e2a_err = np.abs( 0.01 * self.nm_e2a )
            self.nm_e2v     = self.nm_e2a * self.nm_den
            self.nm_e2v_err = self.nm_e2a_err * self.nm_den
            #
            # pressure in NM
            x = np.insert( self.nm_kfn, 0, 0.0 )
            y = np.insert( self.nm_e2a, 0, 0.0 )
            cs_e2a = CubicSpline( x, y )
            self.nm_pre = nuda.cst.three * self.nm_kfn * self.nm_den * cs_e2a( self.nm_kfn, 1 )
            #
            # chemical potential
            self.nm_chempot = ( self.nm_pre + self.nm_e2v ) / self.nm_den
            #
        elif model.lower() == '2016-qmc-nm':
            #
            file_in = os.path.join(nuda.param.path_data,'eos/micro/2016-QMC-NM.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = ' I. Tews, S. Gandolfi, A. Gezerlis, A. Schwenk, Phys. Rev. C 93, 024305 (2016).'
            self.label = 'QMC-2016'
            self.note = ""
            self.nm_den, self.nm_e2a_low, self.nm_e2a_up \
                = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.nm_kfn = nuda.kf_n( self.nm_den )
            self.nm_e2a = 0.5 * ( self.nm_e2a_up + self.nm_e2a_low )
            self.nm_e2a_err = 0.5 * ( self.nm_e2a_up - self.nm_e2a_low )
            self.nm_e2v     = self.nm_e2a * self.nm_den
            self.nm_e2v_err = self.nm_e2a_err * self.nm_den
            #
            # pressure in NM
            x = np.insert( self.nm_kfn, 0, 0.0 )
            y = np.insert( self.nm_e2a, 0, 0.0 )
            cs_e2a = CubicSpline( x, y )
            self.nm_pre = nuda.cst.three * self.nm_kfn * self.nm_den * cs_e2a( self.nm_kfn, 1 )
            #
            # chemical potential
            self.nm_chempot = ( np.array(self.nm_pre) + np.array(self.nm_e2v) ) / np.array(self.nm_den)
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
            # SM
            self.sm_den = den[0,:]
            self.sm_kfn = nuda.kf_n( nuda.cst.half * self.sm_den )
            self.sm_e2a_up = e2a_up[0,:]
            self.sm_e2a_low = e2a_low[0,:]
            self.sm_e2a = e2a_av[0,:]
            self.sm_e2a_err = e2a_err[0,:]
            self.sm_e2v     = self.sm_e2a * self.sm_den
            self.sm_e2v_err = self.sm_e2a_err * self.sm_den
            # NM
            self.nm_den = den[10,:]
            self.nm_kfn = nuda.kf_n( self.nm_den )
            self.nm_e2a_up = e2a_up[10,:]
            self.nm_e2a_low = e2a_low[10,:]
            self.nm_e2a = e2a_av[10,:]
            self.nm_e2a_err = e2a_err[10,:]
            self.nm_e2v     = self.nm_e2a * self.nm_den
            self.nm_e2v_err = self.nm_e2a_err * self.nm_den
            #
            # pressure in NM
            x = np.insert( self.nm_den, 0, 0.0 )
            y = np.insert( self.nm_e2a, 0, 0.0 )
            cs_nm_e2a = CubicSpline( x, y )
            self.nm_pre = self.nm_den**2 * cs_nm_e2a( self.nm_den, 1 )
            # pressure in SM
            x = np.insert( self.sm_den, 0, 0.0 )
            y = np.insert( self.sm_e2a, 0, 0.0 )
            cs_sm_e2a = CubicSpline( x, y )
            self.sm_pre = self.sm_den**2 * cs_sm_e2a( self.sm_den, 1 )
            #
            # Symmetry energy
            self.den_min = max( min( self.nm_den), min( self.sm_den) )
            self.den_max = min( max( self.nm_den), max( self.sm_den) )
            self.kf_min = nuda.kf( self.den_min )
            self.kf_max = nuda.kf( self.den_max )
            #print('den_min:',self.den_min,' den_max:',self.den_max)
            #print('kf_min:',self.kf_min,' kf_max:',self.kf_max)
            nesym = 20
            den_step = ( self.den_max - self.den_min ) / float( nesym )
            self.esym_den = self.den_min + np.arange(nesym+1) * den_step
            self.esym_kf = nuda.kf( self.esym_den )
            #print('kf:',self.esym_kf)
            #print('den:',self.esym_den)
            self.esym_e2a = cs_nm_e2a( self.esym_den ) - cs_sm_e2a( self.esym_den )
            #print('esym:',self.esym_e2a)
            #
            # chemical potential
            self.nm_chempot = ( np.array(self.nm_pre) + np.array(self.nm_e2v) ) / np.array(self.nm_den)
            #
        elif model.lower() == '2018-qmc-nm':
            #
            file_in = os.path.join(nuda.param.path_data,'eos/micro/2018-QMC-NM.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = ''
            self.label = 'QMC-2018'
            self.note = ""
            self.nm_den, self.nm_e2a_low, self.nm_e2a_up, self.nm_e2a, self.nm_e2a_err \
                = np.loadtxt( file_in, usecols=(0,1,2,3,4), unpack = True )
            self.nm_kfn = nuda.kf_n( self.nm_den )
            self.nm_e2v     = self.nm_e2a * self.nm_den
            self.nm_e2v_err = self.nm_e2a_err * self.nm_den
            #
            # pressure in NM
            x = np.insert( self.nm_kfn, 0, 0.0 )
            y = np.insert( self.nm_e2a, 0, 0.0 )
            cs_e2a = CubicSpline( x, y )
            self.nm_pre = nuda.cst.three * self.nm_kfn * self.nm_den * cs_e2a( self.nm_kfn, 1 )
            #
            # chemical potential
            self.nm_chempot = ( np.array(self.nm_pre) + np.array(self.nm_e2v) ) / np.array(self.nm_den)
            #
        elif model.lower() == '2019-mbpt-am-dhsl59':
            #
            file_in1 = os.path.join(nuda.param.path_data,'eos/micro/2020-MBPT-SM-DHSL59.dat')
            file_in2 = os.path.join(nuda.param.path_data,'eos/micro/2020-MBPT-NM-DHSL59.dat')
            if nuda.env.verb: print('Reads file1:',file_in1)
            if nuda.env.verb: print('Reads file2:',file_in2)
            self.ref = 'C. Drischler, K. Hebeler, A. Schwenk, Phys. Rev. Lett. 122, 042501 (2019)'
            self.label = 'MBPT-2019-DHSL59'
            self.note = ""
            self.sm_kfn, self.sm_den, Kin, HF_tot, Scnd_tot, Trd_tot, Fth_tot, self.sm_e2a \
                 = np.loadtxt( file_in1, usecols = (0, 1, 2, 3, 4, 5, 6, 7), comments='#', unpack = True)
            self.sm_e2a_err = np.abs( 0.01 * self.sm_e2a )
            self.sm_e2v     = self.sm_e2a * self.sm_den
            self.sm_e2v_err = self.sm_e2a_err * self.sm_den
            self.nm_kfn, self.nm_den, Kin, HF_tot, Scnd_tot, Trd_tot, Fth_tot, self.nm_e2a \
                 = np.loadtxt( file_in2, usecols = (0, 1, 2, 3, 4, 5, 6, 7), comments='#', unpack = True)
            self.nm_e2a_err = np.abs( 0.01 * self.nm_e2a )
            self.nm_e2v     = self.nm_e2a * self.nm_den
            self.nm_e2v_err = self.nm_e2a_err * self.nm_den
            #
            # pressure in NM
            x = np.insert( self.nm_den, 0, 0.0 )
            y = np.insert( self.nm_e2a, 0, 0.0 )
            cs_nm_e2a = CubicSpline( x, y )
            self.nm_pre = nuda.cst.three * self.nm_kfn * self.nm_den * cs_nm_e2a( self.nm_den, 1 )
            # pressure in SM
            x = np.insert( self.sm_den, 0, 0.0 )
            y = np.insert( self.sm_e2a, 0, 0.0 )
            cs_sm_e2a = CubicSpline( x, y )
            self.sm_pre = nuda.cst.three * self.sm_kfn * self.sm_den * cs_sm_e2a( self.sm_den, 1 )
            #
            # Symmetry energy
            self.den_min = max( min( self.nm_den), min( self.sm_den) )
            self.den_max = min( max( self.nm_den), max( self.sm_den) )
            self.kf_min = nuda.kf( self.den_min )
            self.kf_max = nuda.kf( self.den_max )
            #print('den_min:',self.den_min,' den_max:',self.den_max)
            #print('kf_min:',self.kf_min,' kf_max:',self.kf_max)
            nesym = 20
            den_step = ( self.den_max - self.den_min ) / float( nesym )
            self.esym_den = self.den_min + np.arange(nesym+1) * den_step
            self.esym_kf = nuda.kf( self.esym_den )
            #print('kf:',self.esym_kf)
            #print('den:',self.esym_den)
            self.esym_e2a = cs_nm_e2a( self.esym_den ) - cs_sm_e2a( self.esym_den )
            #print('esym:',self.esym_e2a)
            #
            # chemical potential
            self.nm_chempot = ( np.array(self.nm_pre) + np.array(self.nm_e2v) ) / np.array(self.nm_den)
            #
        elif model.lower() == '2019-mbpt-am-dhsl69':
            #
            file_in1 = os.path.join(nuda.param.path_data,'eos/micro/2020-MBPT-SM-DHSL69.dat')
            file_in2 = os.path.join(nuda.param.path_data,'eos/micro/2020-MBPT-NM-DHSL69.dat')
            if nuda.env.verb: print('Reads file1:',file_in1)
            if nuda.env.verb: print('Reads file2:',file_in2)
            self.ref = 'C. Drischler, K. Hebeler, A. Schwenk, Phys. Rev. Lett. 122, 042501 (2019)'
            self.label = 'MBPT-2019-DHSL69'
            self.note = ""
            self.sm_kfn, self.sm_den, Kin, HF_tot, Scnd_tot, Trd_tot, Fth_tot, self.sm_e2a \
                 = np.loadtxt( file_in1, usecols = (0, 1, 2, 3, 4, 5, 6, 7), comments='#', unpack = True)
            self.sm_e2a_err = np.abs( 0.01 * self.sm_e2a )
            self.sm_e2v     = self.sm_e2a * self.sm_den
            self.sm_e2v_err = self.sm_e2a_err * self.sm_den
            self.nm_kfn, self.nm_den, Kin, HF_tot, Scnd_tot, Trd_tot, Fth_tot, self.nm_e2a \
                 = np.loadtxt( file_in2, usecols = (0, 1, 2, 3, 4, 5, 6, 7), comments='#', unpack = True)
            self.nm_e2a_err = np.abs( 0.01 * self.nm_e2a )
            self.nm_e2v     = self.nm_e2a * self.nm_den
            self.nm_e2v_err = self.nm_e2a_err * self.nm_den
            #
            # pressure in NM
            x = np.insert( self.nm_den, 0, 0.0 )
            y = np.insert( self.nm_e2a, 0, 0.0 )
            cs_nm_e2a = CubicSpline( x, y )
            self.nm_pre = self.nm_den**2 * cs_nm_e2a( self.nm_den, 1 )
            # pressure in SM
            x = np.insert( self.sm_den, 0, 0.0 )
            y = np.insert( self.sm_e2a, 0, 0.0 )
            cs_sm_e2a = CubicSpline( x, y )
            self.sm_pre = self.sm_den**2 * cs_sm_e2a( self.sm_den, 1 )
            #
            # Symmetry energy
            self.den_min = max( min( self.nm_den), min( self.sm_den) )
            self.den_max = min( max( self.nm_den), max( self.sm_den) )
            self.kf_min = nuda.kf( self.den_min ); self.kf_max = nuda.kf( self.den_max )
            nesym = 20; den_step = ( self.den_max - self.den_min ) / float( nesym )
            self.esym_den = self.den_min + np.arange(nesym+1) * den_step
            self.esym_kf = nuda.kf( self.esym_den )
            self.esym_e2a = cs_nm_e2a( self.esym_den ) - cs_sm_e2a( self.esym_den )
            #
            # chemical potential
            self.nm_chempot = ( np.array(self.nm_pre) + np.array(self.nm_e2v) ) / np.array(self.nm_den)
            self.sm_chempot = ( np.array(self.sm_pre) + np.array(self.sm_e2v) ) / np.array(self.sm_den)
            #
        elif model.lower() == '2020-mbpt-am':
            #
            file_in1 = os.path.join(nuda.param.path_data,'eos/micro/2023-MBPT-SM.csv')
            file_in2 = os.path.join(nuda.param.path_data,'eos/micro/2023-MBPT-NM.csv')
            if nuda.env.verb: print('Reads file1:',file_in1)
            if nuda.env.verb: print('Reads file2:',file_in2)
            self.ref = 'C. Drischler, R.J. Furnstahl, J.A. Melendez, D.R. Phillips, Phys. Rev. Lett. 125(20), 202702 (2020).; C. Drischler, J. A. Melendez, R. J. Furnstahl, and D. R. Phillips, Phys. Rev. C 102, 054315'
            self.label = 'MBPT-2020'
            self.note = ""
            self.sm_den, self.sm_e2a_lo, self.sm_e2a_lo_err, self.sm_e2a_nlo, self.sm_e2a_nlo_err, \
                self.sm_e2a_n2lo, self.sm_e2a_n2lo_err, self.sm_e2a_n3lo, self.sm_e2a_n3lo_err \
                = np.loadtxt( file_in1, usecols = (0, 1, 2, 3, 4, 5, 6, 7, 8), delimiter=',', comments='#', unpack = True)
            self.sm_kfn = nuda.kf_n( nuda.cst.half * self.sm_den )
            self.sm_e2a = self.sm_e2a_n3lo
            self.sm_e2a_err = self.sm_e2a_n3lo_err
            self.sm_e2v     = self.sm_e2a * self.sm_den
            self.sm_e2v_err = self.sm_e2a_err * self.sm_den
            self.nm_den, self.nm_e2a_lo, self.nm_e2a_lo_err, self.nm_e2a_nlo, self.nm_e2a_nlo_err, \
                self.nm_e2a_n2lo, self.nm_e2a_n2lo_err, self.nm_e2a_n3lo, self.nm_e2a_n3lo_err \
                = np.loadtxt( file_in2, usecols = (0, 1, 2, 3, 4, 5, 6, 7, 8), delimiter=',', comments='#', unpack = True)
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
            # pressure in SM
            x = np.insert( self.sm_den, 0, 0.0 )
            y = np.insert( self.sm_e2a, 0, 0.0 )
            cs_sm_e2a = CubicSpline( x, y )
            self.sm_pre = self.sm_den**2 * cs_sm_e2a( self.sm_den, 1 )
            #
            # Symmetry energy
            self.den_min = max( min( self.nm_den), min( self.sm_den) )
            self.den_max = min( max( self.nm_den), max( self.sm_den) )
            self.kf_min = nuda.kf( self.den_min ); self.kf_max = nuda.kf( self.den_max )
            nesym = 20; den_step = ( self.den_max - self.den_min ) / float( nesym )
            self.esym_den = self.den_min + np.arange(nesym+1) * den_step
            self.esym_kf = nuda.kf( self.esym_den )
            self.esym_e2a = cs_nm_e2a( self.esym_den ) - cs_sm_e2a( self.esym_den )
            #
            # chemical potential
            self.nm_chempot = ( np.array(self.nm_pre) + np.array(self.nm_e2v) ) / np.array(self.nm_den)
            self.sm_chempot = ( np.array(self.sm_pre) + np.array(self.sm_e2v) ) / np.array(self.sm_den)
            #
        self.den_unit = 'fm$^{-3}$'
        self.kf_unit = 'fm$^{-1}$'
        self.e2a_unit = 'MeV'
        self.e2v_unit = 'MeV fm$^{-3}$'
        self.pre_unit = 'MeV fm$^{-3}$'
        self.gap_unit = 'MeV'
        #
        if nuda.env.verb: print("Exit SetupMicro()")
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
