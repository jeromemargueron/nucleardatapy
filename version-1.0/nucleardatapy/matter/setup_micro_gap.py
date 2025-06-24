import os
import sys
import math
import numpy as np  # 1.15.0
from scipy.interpolate import CubicSpline
from scipy.optimize import curve_fit
import random

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def micro_gap_models( matter = 'NM' ):
    """
    Return a list with the name of the models available in this toolkit and \
    print them all on the prompt. These models are the following ones: \
    '2008-BCS-NM', '2008-QMC-NM-swave', '2009-DLQMC-NM', '2010-QMC-NM-AV4', '2017-MBPT-NM-GAP-EMG-450-500-N2LO', \
    '2017-MBPT-NM-GAP-EMG-450-500-N3LO', '2017-MBPT-NM-GAP-EMG-450-700-N2LO', \
    '2017-MBPT-NM-GAP-EMG-450-700-N3LO', '2017-MBPT-NM-GAP-EM-500-N2LO', '2017-MBPT-NM-GAP-EM-500-N3LO', \
    '2022-AFDMC-NM' \

    :param matter: matter can be 'NM' (by default) or 'SM'.
    :type matter: str.
    :return: The list of models.
    :rtype: list[str].
    """
    #
    if nuda.env.verb: print("\nEnter micro_gap_models()")
    #
    models_all = [ '2006-BHF-NM-Av18', '2006-BHF-SM-Av18', '2008-BCS-NM', '2008-QMC-NM-swave', '2009-DLQMC-NM', '2010-QMC-NM-AV4', \
            '2017-MBPT-NM-GAP-EMG-450-500-N2LO', '2017-MBPT-NM-GAP-EMG-450-500-N3LO', '2017-MBPT-NM-GAP-EMG-450-700-N2LO', \
            '2017-MBPT-NM-GAP-EMG-450-700-N3LO', '2017-MBPT-NM-GAP-EM-500-N2LO', '2017-MBPT-NM-GAP-EM-500-N3LO', \
            '2022-AFDMC-NM' ]
    models_all_lower = [ item.lower() for item in models_all ]
    if nuda.env.verb: print('All models available in the toolkit:',models_all)
    #
    models = []
    models_lower = []
    for model in models_all:
        #print('split:',model.split('-'))
        if matter in model.split('-')[2]:
            models.append( model )
            models_lower.append( model.lower() )
    #
    if nuda.env.verb: print("Exit micro_gap_models()")
    #
    return models, models_lower, models_all, models_all_lower

class setupMicroGap():
    """
    Instantiate the object with microscopic results choosen \
    by the toolkit practitioner.

    This choice is defined in `model`, which can chosen among \
    the following choices: \
    '2008-BCS-NM', '2008-QMC-NM-swave', '2009-DLQMC-NM', '2010-QMC-NM-AV4', '2017-MBPT-NM-GAP-EMG-450-500-N2LO', \
    '2017-MBPT-NM-GAP-EMG-450-500-N3LO', '2017-MBPT-NM-GAP-EMG-450-700-N2LO', \
    '2017-MBPT-NM-GAP-EMG-450-700-N3LO', '2017-MBPT-NM-GAP-EM-500-N2LO', '2017-MBPT-NM-GAP-EM-500-N3LO', \
    '2022-AFDMC-NM' \

    :param model: Fix the name of model. Default value: '2008-BCS-NM'.
    :type model: str, optional. 

    **Attributes:**
    """
    #
    def __init__( self, model = '2008-BCS-NM', matter = 'NM' ):
        """
        Parameters
        ----------
        model : str, optional
        The model to consider. Choose between: 2008-BCS-NM (default), 2008-AFDMC-NM, ...
        """
        #
        if nuda.env.verb: print("Enter setupMicroGap()")
        #
        #: Attribute model.
        self.model = model
        if nuda.env.verb: print("model:",model)
        print("-> model:",model)
        #
        self = setupMicroGap.init_self( self )
        #
        models, models_lower, models_all, models_all_lower = micro_gap_models( matter = matter )
        #
        if model.lower() not in models_all_lower:
            print('setup_micro_gap: The model name ',model,' is not in the list of models.')
            print('setup_micro_gap: list of models:',models)
            print('setup_micro_gap: -- Exit the code --')
            exit()
        #
        if model.lower() == '2006-bhf-nm-av18':
            #
            file_in_fs = os.path.join(nuda.param.path_data,'matter/micro/2006-BHF/2006-BHF-Av18-GAP-NM-FreeSpectrum.dat')
            if nuda.env.verb: print('Reads file (free spectrum):',file_in_fs)
            file_in_se = os.path.join(nuda.param.path_data,'matter/micro/2006-BHF/2006-BHF-Av18-GAP-NM-SelfEnergy.dat')
            if nuda.env.verb: print('Reads file (self energy):',file_in_se)
            self.ref = 'L.G. Cao, U. Lombardo, and P. Schuck, Phys. Rev. C 74, 64301 (2006)'
            self.note = ""
            self.label = 'EBHF-Av18-2006'
            self.marker = 'o'
            self.every = 1
            self.lstyle = 'solid'
            self.gap_err = False
            self.nm_kfn_1s0_fs, self.nm_gap_bare_1s0_fs, self.nm_gap_bare_onebubble_1s0_fs, self.nm_gap_bare_full_1s0_fs \
                = np.loadtxt( file_in_fs, usecols=(0,1,2,3), unpack = True )
            self.nm_den_1s0_fs = nuda.den_n( self.nm_kfn_1s0_fs )
            self.nm_kfn_1s0, self.nm_gap_bare_1s0, self.nm_gap_1s0 \
                = np.loadtxt( file_in_se, usecols=(0,1,2), unpack = True )
            self.nm_den_1s0 = nuda.den_n( self.nm_kfn_1s0 )
            #
        elif model.lower() == '2006-bhf-sm-av18':
            #
            file_in_fs = os.path.join(nuda.param.path_data,'matter/micro/2006-BHF/2006-BHF-Av18-GAP-SM-FreeSpectrum.dat')
            if nuda.env.verb: print('Reads file (free spectrum):',file_in_fs)
            file_in_se = os.path.join(nuda.param.path_data,'matter/micro/2006-BHF/2006-BHF-Av18-GAP-SM-SelfEnergy.dat')
            if nuda.env.verb: print('Reads file (self energy):',file_in_se)
            self.ref = 'L.G. Cao, U. Lombardo, and P. Schuck, Phys. Rev. C 74, 64301 (2006)'
            self.note = ""
            self.label = 'EBHF-Av18-2006'
            self.marker = 'o'
            self.every = 1
            self.lstyle = 'solid'
            self.gap_err = False
            self.sm_kfn_1s0_fs, self.sm_gap_bare_1s0_fs, self.sm_gap_bare_onebubble_1s0_fs, self.sm_gap_bare_full_1s0_fs \
                = np.loadtxt( file_in_fs, usecols=(0,1,2,3), unpack = True )
            self.sm_den_1s0_fs = nuda.den( self.sm_kfn_1s0_fs )
            self.sm_kfn_1s0, self.sm_gap_1s0 \
                = np.loadtxt( file_in_se, usecols=(0,1), unpack = True )
            self.sm_den_1s0 = nuda.den( self.sm_kfn_1s0 )
            #
        elif model.lower() == '2008-bcs-nm':
            #
            file_in = os.path.join(nuda.param.path_data,'matter/micro/2008-BCS-NM.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'A. Fabrocini, S. Fantoni, A.Y. Illarionov, and K.E. Schmidt, Nuc. Phys. A 803, 137 (2008)'
            self.note = ""
            self.label = 'BCS-2008'
            self.marker = 'o'
            self.every = 1
            self.lstyle = 'dashed'
            self.gap_err = False
            self.nm_kfn_1s0, self.nm_gap_1s0, self.nm_chempot, self.nm_effmass \
                = np.loadtxt( file_in, usecols=(0,1,2,3), unpack = True )
            self.nm_den_1s0     = nuda.den_n( self.nm_kfn_1s0 )
            self.nm_kfn_effmass = self.nm_kfn_1s0
            self.nm_den_effmass = self.nm_den_1s0
            #
        elif model.lower() == '2008-afdmc-nm':
            #
            file_in = os.path.join(nuda.param.path_data,'matter/micro/2008-AFDMC-NM.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'A. Fabrocini, S. Fantoni, A.Y. Illarionov, and K.E. Schmidt, Phys. Rev. Lett. 95, 192501 (2005); A. Fabrocini, S. Fantoni, A.Y. Illarionov, and K.E. Schmidt, Nuc. Phys. A 803, 137 (2008)'
            self.note = ""
            self.label = 'AFDMC-2008'
            self.marker = 'D'
            self.every = 1
            self.lstyle = 'solid'
            self.gap_err = False
            self.nm_kfn_1s0, self.nm_gap_1s0, self.nm_chempot, self.nm_effmass \
                = np.loadtxt( file_in, usecols=(0,1,2,3), unpack = True )
            self.nm_den_1s0     = nuda.den_n( self.nm_kfn_1s0 )
            self.nm_kfn_effmass = self.nm_kfn_1s0
            self.nm_den_effmass = self.nm_den_1s0
            #
        elif model.lower() == '2008-qmc-nm-swave':
            #
            file_in = os.path.join(nuda.param.path_data,'matter/micro/2008-QMC-NM-swave.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'A. Gezerlis and J. Carlson PRC 81, 025803 (2010)'
            self.note = ""
            self.label = 'QMC-swave-2008'
            self.marker = 'o'
            self.every = 1
            self.lstyle = 'solid'
            self.gap_err = True
            self.nm_kfn_1s0, gap2ef, gap2ef_err, e2effg, e2effg_err \
                = np.loadtxt( file_in, usecols=(0,1,2,3,4), unpack = True )
            self.nm_den_1s0     = nuda.den_n( self.nm_kfn_1s0 )
            self.nm_gap_1s0     = gap2ef * nuda.eF_n( self.nm_kfn_1s0 )
            self.nm_gap_1s0_err = gap2ef_err * nuda.eF_n( self.nm_kfn_1s0 )
            #
        elif model.lower() == '2009-dlqmc-nm':
            #
            file_in = os.path.join(nuda.param.path_data,'matter/micro/2009-dQMC-NM.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'T. Abe, R. Seki, Phys. Rev. C 79, 054002 (2009)'
            self.note = ""
            self.label = 'dLQMC-2009'
            self.marker = 'v'
            self.every = 1
            self.lstyle = 'solid'
            self.gap_err = True
            self.nm_kfn_1s0, gap2ef, gap2ef_err, e2effg, e2effg_err \
                = np.loadtxt( file_in, usecols=(0,1,2,3,4), unpack = True )
            self.nm_den_1s0     = nuda.den_n( self.nm_kfn_1s0 )
            self.nm_gap_1s0     = gap2ef * nuda.eF_n( self.nm_kfn_1s0 )
            self.nm_gap_1s0_err = gap2ef_err * nuda.eF_n( self.nm_kfn_1s0 )
            #
        elif model.lower() == '2010-qmc-nm-av4':
            #
            file_in = os.path.join(nuda.param.path_data,'matter/micro/2010-QMC-NM-AV4.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'A. Gezerlis and J. Carlson PRC 81, 025803 (2010)'
            self.note = ""
            self.label = 'QMC-AV4-2008'
            self.marker = 's'
            self.every = 1
            self.lstyle = 'solid'
            self.gap_err = True
            self.nm_kfn_1s0, gap2ef, gap2ef_err, e2effg, e2effg_err \
                = np.loadtxt( file_in, usecols=(0,1,2,3,4), unpack = True )
            self.nm_den_1s0     = nuda.den_n( self.nm_kfn_1s0 )
            self.nm_gap_1s0     = gap2ef * nuda.eF_n( self.nm_kfn_1s0 )
            self.nm_gap_1s0_err = gap2ef_err * nuda.eF_n( self.nm_kfn_1s0 )
            #
        elif '2017-mbpt-nm-gap-em' in model.lower() :
            #
            self.ref = 'C. Drischler, T. Kr\"uger, K. Hebeler, and A. Schwenk, Phys. Rev. C 95, 024302 (2017).'
            self.note = ""
            self.marker = 's'
            self.lstyle = 'dashed'
            self.every = 2
            self.err = True
            if model.lower() == '2017-mbpt-nm-gap-emg-450-500-n2lo':
                self.label = 'BCS-EMG450-500-N2LO-2017'
                file_effmass = os.path.join(nuda.param.path_data,'matter/micro/2017-Drischler/N3LO_EGM450_500_effmass_1S0_HF_spectrum_N2LO_3N_forces.csv')
                file_1s0 = os.path.join(nuda.param.path_data,'matter/micro/2017-Drischler/N3LO_EGM450_500_gap_1S0_HF_spectrum_N2LO_3N_forces.csv')
                file_3pf2 = os.path.join(nuda.param.path_data,'matter/micro/2017-Drischler/N3LO_EGM450_500_gap_3PF2_HF_spectrum_N2LO_3N_forces.csv')
            elif model.lower() == '2017-mbpt-nm-gap-emg-450-500-n3lo':
                self.label = 'BCS-EMG450-500-N3LO-2017'
                file_effmass = os.path.join(nuda.param.path_data,'matter/micro/2017-Drischler/N3LO_EGM450_500_effmass_1S0_HF_spectrum_N3LO_3N_forces.csv')
                file_1s0 = os.path.join(nuda.param.path_data,'matter/micro/2017-Drischler/N3LO_EGM450_500_gap_1S0_HF_spectrum_N3LO_3N_forces.csv')
                file_3pf2 = os.path.join(nuda.param.path_data,'matter/micro/2017-Drischler/N3LO_EGM450_500_gap_3PF2_HF_spectrum_N3LO_3N_forces.csv')
            elif model.lower() == '2017-mbpt-nm-gap-emg-450-700-n2lo':
                self.label = 'BCS-EMG450-700-N2LO-2017'
                file_effmass = os.path.join(nuda.param.path_data,'matter/micro/2017-Drischler/N3LO_EGM450_700_effmass_1S0_HF_spectrum_N2LO_3N_forces.csv')
                file_1s0 = os.path.join(nuda.param.path_data,'matter/micro/2017-Drischler/N3LO_EGM450_700_gap_1S0_HF_spectrum_N2LO_3N_forces.csv')
                file_3pf2 = os.path.join(nuda.param.path_data,'matter/micro/2017-Drischler/N3LO_EGM450_700_gap_3PF2_HF_spectrum_N2LO_3N_forces.csv')
            elif model.lower() == '2017-mbpt-nm-gap-emg-450-700-n3lo':
                self.label = 'BCS-EMG450-700-N3LO-2017'
                file_effmass = os.path.join(nuda.param.path_data,'matter/micro/2017-Drischler/N3LO_EGM450_700_effmass_1S0_HF_spectrum_N3LO_3N_forces.csv')
                file_1s0 = os.path.join(nuda.param.path_data,'matter/micro/2017-Drischler/N3LO_EGM450_700_gap_1S0_HF_spectrum_N3LO_3N_forces.csv')
                file_3pf2 = os.path.join(nuda.param.path_data,'matter/micro/2017-Drischler/N3LO_EGM450_700_gap_3PF2_HF_spectrum_N3LO_3N_forces.csv')
            elif model.lower() == '2017-mbpt-nm-gap-em-500-n2lo':
                self.label = 'BCS-EM500-N2LO-2017'
                file_effmass = os.path.join(nuda.param.path_data,'matter/micro/2017-Drischler/N3LO_EM500_effmass_1S0_HF_spectrum_N2LO_3N_forces.csv')
                file_1s0 = os.path.join(nuda.param.path_data,'matter/micro/2017-Drischler/N3LO_EM500_gap_1S0_HF_spectrum_N2LO_3N_forces.csv')
                file_3pf2 = os.path.join(nuda.param.path_data,'matter/micro/2017-Drischler/N3LO_EM500_gap_3PF2_HF_spectrum_N2LO_3N_forces.csv')
            elif model.lower() == '2017-mbpt-nm-gap-em-500-n3lo':
                self.label = 'BCS-EM500-N3LO-2017'
                file_effmass = os.path.join(nuda.param.path_data,'matter/micro/2017-Drischler/N3LO_EM500_effmass_1S0_HF_spectrum_N3LO_3N_forces.csv')
                file_1s0 = os.path.join(nuda.param.path_data,'matter/micro/2017-Drischler/N3LO_EM500_gap_1S0_HF_spectrum_N3LO_3N_forces.csv')
                file_3pf2 = os.path.join(nuda.param.path_data,'matter/micro/2017-Drischler/N3LO_EM500_gap_3PF2_HF_spectrum_N3LO_3N_forces.csv')
            if nuda.env.verb: 
                print('Reads file_effmass:',file_in_effmass)
                print('Reads file_1s0:    ',file_in_1s0)
                print('Reads file_3pf2:   ',file_in_3pf2)
            self.nm_kfn_effmass, effmass_lo, effmass_up \
                = np.loadtxt( file_effmass, usecols = (0, 1, 2), delimiter=',', comments='#', unpack = True)
            self.nm_den_effmass = nuda.den_n( self.nm_kfn_effmass )
            self.nm_effmass = 0.5 * ( effmass_up + effmass_lo )
            self.nm_effmass_err = 0.5 * ( effmass_up - effmass_up )
            self.nm_kfn_1s0, gap_lo, gap_up \
                = np.loadtxt( file_1s0, usecols = (0, 1, 2), delimiter=',', comments='#', unpack = True)
            self.nm_den_1s0 = nuda.den_n( self.nm_kfn_1s0 )
            self.nm_gap_1s0 = 0.5 * ( gap_up + gap_lo )
            self.nm_gap_1s0_err = 0.5 * ( gap_up - gap_up )
            self.nm_kfn_3pf2, gap_lo, gap_up \
                = np.loadtxt( file_3pf2, usecols = (0, 1, 2), delimiter=',', comments='#', unpack = True)
            self.nm_den_3pf2 = nuda.den_n( self.nm_kfn_3pf2 )
            self.nm_gap_3pf2 = 0.5 * ( gap_up + gap_lo )
            self.nm_gap_3pf2_err = 0.5 * ( gap_up - gap_up )
            #
        elif model.lower() == '2022-afdmc-nm':
            #
            file_in = os.path.join(nuda.param.path_data,'matter/micro/2022-AFDMC-NM-gap.csv')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'S. Gandolfi, G. Palkanoglou, J. Carlson, A. Gezerlis, K.E. Schmidt, Condensed Matter 7(1) (2022).'
            self.note = ""
            self.label = 'AFDMC+corr.-2022'
            self.marker = 'o'
            self.lstyle = 'solid'
            self.every = 1
            self.gap_err = True
            # read gap
            self.nm_kfn_1s0, self.nm_gap_1s0, self.nm_gap_1s0_err = np.loadtxt( file_in, usecols=(0,1,2), delimiter=',', comments='#', unpack = True )
            self.nm_den_1s0 = nuda.den_n( self.nm_kfn_1s0 )
            #
            #
        self.den_unit = 'fm$^{-3}$'
        self.kf_unit = 'fm$^{-1}$'
        self.gap_unit = 'MeV'
        #
        if nuda.env.verb: print("Exit setupMicroGap()")
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
        print("   note:  ",self.note)
        print("   label: ",self.label)
        print("   marker:",self.marker)
        print("   every: ",self.every)
        # NM
        if self.nm_den_effmass is not None: print(f"   nm_den_effmass: {np.round(self.nm_den_effmass,3)} in {self.den_unit}")
        if self.nm_kfn_effmass is not None: print(f"   nm_kfn_effmass: {np.round(self.nm_kfn_effmass,3)} in {self.kf_unit}")
        if self.nm_den_1s0 is not None: print(f"   nm_den_1s0: {np.round(self.nm_den_1s0,3)} in {self.den_unit}")
        if self.nm_kfn_1s0 is not None: print(f"   nm_kfn_1s0: {np.round(self.nm_kfn_1s0,3)} in {self.kf_unit}")
        if self.nm_den_3pf2 is not None: print(f"   nm_den_3pf2: {np.round(self.nm_den_3pf2,3)} in {self.den_unit}")
        if self.nm_kfn_3pf2 is not None: print(f"   nm_kfn_3pf2: {np.round(self.nm_kfn_3pf2,3)} in {self.kf_unit}")
        if self.nm_effmass is not None: print(f"   nm_effmass: {np.round(self.nm_effmass,3)}")
        if self.nm_gap_1s0 is not None: print(f"   nm_gap_1s0: {np.round(self.nm_gap_1s0,3)} in {self.gap_unit}")
        if self.nm_gap_1s0_err is not None: print(f"   nm_gap_1s0_err: {np.round(self.nm_gap_1s0_err,3)} in {self.gap_unit}")
        if self.nm_gap_3pf2 is not None: print(f"   nm_gap_3pf2: {np.round(self.nm_gap_3pf2,3)} in {self.gap_unit}")
        if self.nm_gap_3pf2_err is not None: print(f"   nm_gap_3pf2_err: {np.round(self.nm_gap_3pf2_err,3)} in {self.gap_unit}")
        # SM
        if self.sm_den_1s0 is not None: print(f"   sm_den_1s0: {np.round(self.sm_den_1s0,3)} in {self.den_unit}")
        if self.sm_kfn_1s0 is not None: print(f"   sm_kfn_1s0: {np.round(self.sm_kfn_1s0,3)} in {self.kf_unit}")
        if self.sm_gap_1s0 is not None: print(f"   sm_gap_1s0: {np.round(self.sm_gap_1s0,3)} in {self.gap_unit}")
        if self.sm_gap_1s0_err is not None: print(f"   sm_gap_1s0_err: {np.round(self.sm_gap_1s0_err,3)} in {self.gap_unit}")
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
        #: Attribute the neutron matter Fermi momentum for which the effective mass is provided.
        self.nm_kfn_effmass = None
        self.sm_kfn_effmass = None
        #: Attribute the neutron matter densities for which the effective mass is provided.
        self.nm_den_effmass = None
        self.sm_den_effmass = None
        #: Attribute the neutron matter Fermi momentum for which the 1S0 pairing gap is provided.
        self.nm_kfn_1s0 = None
        self.sm_kfn_1s0 = None
        #: Attribute the neutron matter densities for which the 1S0 pairing gap is provided.
        self.nm_den_1s0 = None
        self.sm_den_1s0 = None
        #: Attribute the neutron matter Fermi momentum for which the 3PF2 pairing gap is provided.
        self.nm_kfn_3pf2 = None
        self.sm_kfn_3pf2 = None
        #: Attribute the neutron matter densities for which the 3PF2 pairing gap is provided.
        self.nm_den_3pf2 = None
        self.sm_den_3pf2 = None
        #: Attribute the neutron matter effective mass.
        self.nm_effmass = None
        self.sm_effmass = None
        #: Attribute the neutron matter 1S0 pairing gap.
        self.nm_gap_1s0 = None
        self.sm_gap_1s0 = None
        #: Attribute the uncertainty in the neutron matter 1S0 pairing gap.
        self.nm_gap_1s0_err = None
        self.sm_gap_1s0_err = None
        #: Attribute the neutron matter 3PF2 pairing gap.
        self.nm_gap_3pf2 = None
        self.sm_gap_3pf2 = None
        #: Attribute the uncertainty in the neutron matter 3PF2 pairing gap.
        self.nm_gap_3pf2_err = None
        self.sm_gap_3pf2_err = None
        #: Attribute the plot label data.
        self.label = ''
        #: Attribute the plot linestyle.
        self.lstyle = None
        #: Attribute the plot marker.
        self.marker = None
        #: Attribute the plot every data.
        self.every = 1
        #
        if nuda.env.verb: print("Exit init_self()")
        #
        return self        

