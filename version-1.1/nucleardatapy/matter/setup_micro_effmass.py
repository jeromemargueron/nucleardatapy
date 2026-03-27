import os
import sys
import math
import numpy as np  # 1.15.0
from scipy.interpolate import CubicSpline
from scipy.optimize import curve_fit
import random

import nucleardatapy as nuda

def effmass_emp( den , delta, mb = 'BHF' ):
    if mb == 'BHF':
        kfsat = 1.32
        kfn = nuda.kf_n( nuda.cst.half * ( 1.0 + delta ) * den )
        kfp = nuda.kf_n( nuda.cst.half * ( 1.0 - delta ) * den )
        ms_n = 1.0 / ( 1.0 + 0.20 * (kfp/kfsat)**3.5 )
        ms_p = 1.0 / ( 1.0 + 0.20 * (kfn/kfsat)**3.5 )
    return ms_n, ms_p

def micro_effmass_models( matter = 'NM' ):
    """
    Return a list with the name of the models available in this toolkit and \
    print them all on the prompt. These models are the following ones: \
    '2008-BCS-NM', '2017-MBPT-NM-GAP-EMG-450-500-N2LO', \
    '2017-MBPT-NM-GAP-EMG-450-500-N3LO', '2017-MBPT-NM-GAP-EMG-450-700-N2LO', \
    '2017-MBPT-NM-GAP-EMG-450-700-N3LO', '2017-MBPT-NM-GAP-EM-500-N2LO', '2017-MBPT-NM-GAP-EM-500-N3LO'

    :param matter: matter can be 'NM' (by default) or 'SM'.
    :type matter: str.
    :return: The list of models.
    :rtype: list[str].
    """
    #
    if nuda.env.verb: print("\nEnter micro_effmass_models()")
    # '2008-AFDMC-NM', 
    models_all = [ '2006-BHF-SM-Av18', '2006-BHF-AM-Av18', '2008-BCS-NM', \
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
    if nuda.env.verb: print("Exit micro_effmass_models()")
    #
    return models, models_lower, models_all, models_all_lower

class setupMicroEffmass():
    """
    Instantiate the object with microscopic results choosen \
    by the toolkit practitioner.

    This choice is defined in `model`, which can chosen among \
    the following choices: \
    '2008-BCS-NM', '2017-MBPT-NM-GAP-EMG-450-500-N2LO', \
    '2017-MBPT-NM-GAP-EMG-450-500-N3LO', '2017-MBPT-NM-GAP-EMG-450-700-N2LO', \
    '2017-MBPT-NM-GAP-EMG-450-700-N3LO', '2017-MBPT-NM-GAP-EM-500-N2LO', '2017-MBPT-NM-GAP-EM-500-N3LO'

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
        if nuda.env.verb: print("Enter setupMicroEffmass()")
        #
        #: Attribute model.
        self.model = model
        if nuda.env.verb: print("model:",model)
        print("-> model:",model)
        #
        self = setupMicroEffmass.init_self( self )
        #
        models, models_lower, models_all, models_all_lower = micro_effmass_models( matter = matter )
        #
        if model.lower() not in models_all_lower:
            print('setup_micro_effmass: The model name ',model,' is not in the list of models.')
            print('setup_micro_effmass: list of models:',models)
            print('setup_micro_effmass: -- Exit the code --')
            exit()
        #
        if model.lower() == '2006-bhf-sm-av18':
            #
            file_in = os.path.join(nuda.param.path_data,'matter/micro/2006-BHF/2006-BHF-Av18-effmass-SM.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'L.G. Cao, U. Lombardo, C.W. Shen, N.V. Giai, Phys. Rev. C 73, 014313 (2006)'
            self.note = ""
            self.label = 'BHF-2006'
            self.marker = 'o'
            self.every = 1
            #self.linestyle = 'dotted'
            self.err = False
            self.nm_effmass_err = None
            self.sm_den, self.sm_effmass \
                = np.loadtxt( file_in, usecols=(0,1), unpack = True )
            self.sm_kfn = nuda.kf_n( nuda.cst.half * self.sm_den )
            #
        elif model.lower() == '2006-bhf-am-av18':
            #
            file_in_00 = os.path.join(nuda.param.path_data,'matter/micro/2006-BHF/2006-BHF-Av18-effmass-SM.dat')
            file_in_02 = os.path.join(nuda.param.path_data,'matter/micro/2006-BHF/2006-BHF-Av18-effmass-beta0.2.dat')
            file_in_04 = os.path.join(nuda.param.path_data,'matter/micro/2006-BHF/2006-BHF-Av18-effmass-beta0.4.dat')
            self.ref = 'L.G. Cao, U. Lombardo, C.W. Shen, N.V. Giai, Phys. Rev. C 73, 014313 (2006)'
            self.note = ""
            self.label = 'BHF-2006'
            self.marker = 'o'
            self.every = 1
            #self.linestyle = 'dotted'
            self.err = False
            self.nm_effmass_err = None
            self.sm_den, self.sm_effmass_p \
                = np.loadtxt( file_in_00, usecols=(0,1), unpack = True )
            self.sm_effmass_n = self.sm_effmass_p
            self.sm_kfn = nuda.kf_n( nuda.cst.half * ( 1.0 + 0.0 ) * self.sm_den )
            #
            # asymmetric matter with delta = 0.2
            self.am02_den, self.am02_effmass_p, self.am02_effmass_n \
                = np.loadtxt( file_in_02, usecols=(0,1,2), unpack = True )
            self.am02_kfn = nuda.kf_n( nuda.cst.half * ( 1.0 + 0.2 ) * self.am02_den )
            #
            # asymmetric matter with delta = 0.4
            self.am04_den, self.am04_effmass_p, self.am04_effmass_n \
                = np.loadtxt( file_in_04, usecols=(0,1,2), unpack = True )
            self.am04_kfn = nuda.kf_n( nuda.cst.half * ( 1.0 + 0.4 ) * self.am04_den )
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
            #self.linestyle = 'dotted'
            self.err = False
            self.nm_effmass_err = None
            self.nm_kfn, nm_gap, nm_chempot, self.nm_effmass \
                = np.loadtxt( file_in, usecols=(0,1,2,3), unpack = True )
            self.nm_den     = nuda.den_n( self.nm_kfn )
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
            #self.linestyle = 'solid'
            self.err = False
            self.nm_effmass_err = None
            self.nm_kfn, nm_gap, nm_chempot, self.nm_effmass \
                = np.loadtxt( file_in, usecols=(0,1,2,3), unpack = True )
            self.nm_den  = nuda.den_n( self.nm_kfn )
            print('kfn:',self.nm_kfn)
            print('ms:',self.nm_effmass)
            #
        elif '2017-mbpt-nm-gap-em' in model.lower() :
            #
            self.ref = 'C. Drischler, T. Kr\"uger, K. Hebeler, and A. Schwenk, Phys. Rev. C 95, 024302 (2017).'
            self.note = ""
            self.marker = 's'
            #self.linestyle = 'solid'
            self.every = 2
            self.err = True
            if model.lower() == '2017-mbpt-nm-gap-emg-450-500-n2lo':
                self.label = 'BCS-EMG450-500-N2LO-2017'
                file_effmass = os.path.join(nuda.param.path_data,'matter/micro/2017-Drischler/N3LO_EGM450_500_effmass_1S0_HF_spectrum_N2LO_3N_forces.csv')
            elif model.lower() == '2017-mbpt-nm-gap-emg-450-500-n3lo':
                self.label = 'BCS-EMG450-500-N3LO-2017'
                file_effmass = os.path.join(nuda.param.path_data,'matter/micro/2017-Drischler/N3LO_EGM450_500_effmass_1S0_HF_spectrum_N3LO_3N_forces.csv')
            elif model.lower() == '2017-mbpt-nm-gap-emg-450-700-n2lo':
                self.label = 'BCS-EMG450-700-N2LO-2017'
                file_effmass = os.path.join(nuda.param.path_data,'matter/micro/2017-Drischler/N3LO_EGM450_700_effmass_1S0_HF_spectrum_N2LO_3N_forces.csv')
            elif model.lower() == '2017-mbpt-nm-gap-emg-450-700-n3lo':
                self.label = 'BCS-EMG450-700-N3LO-2017'
                file_effmass = os.path.join(nuda.param.path_data,'matter/micro/2017-Drischler/N3LO_EGM450_700_effmass_1S0_HF_spectrum_N3LO_3N_forces.csv')
            elif model.lower() == '2017-mbpt-nm-gap-em-500-n2lo':
                self.label = 'BCS-EM500-N2LO-2017'
                file_effmass = os.path.join(nuda.param.path_data,'matter/micro/2017-Drischler/N3LO_EM500_effmass_1S0_HF_spectrum_N2LO_3N_forces.csv')
            elif model.lower() == '2017-mbpt-nm-gap-em-500-n3lo':
                self.label = 'BCS-EM500-N3LO-2017'
                file_effmass = os.path.join(nuda.param.path_data,'matter/micro/2017-Drischler/N3LO_EM500_effmass_1S0_HF_spectrum_N3LO_3N_forces.csv')
            if nuda.env.verb: 
                print('Reads file_effmass:',file_in_effmass)
            self.nm_kfn, effmass_lo, effmass_up \
                = np.loadtxt( file_effmass, usecols = (0, 1, 2), delimiter=',', comments='#', unpack = True)
            self.nm_den = nuda.den_n( self.nm_kfn )
            self.nm_effmass = 0.5 * ( effmass_up + effmass_lo )
            self.nm_effmass_err = 0.5 * ( effmass_up - effmass_up )
            #
        self.den_unit = 'fm$^{-3}$'
        self.kf_unit = 'fm$^{-1}$'
        self.gap_unit = 'MeV'
        #
        if nuda.env.verb: print("Exit setupMicroEffmass()")
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
        if self.nm_den is not None: print(f"   nm_den: {np.round(self.nm_den,3)} in {self.den_unit}")
        if self.nm_kfn is not None: print(f"   nm_kfn: {np.round(self.nm_kfn,3)} in {self.kf_unit}")
        if self.nm_effmass is not None: print(f"   nm_effmass: {np.round(self.nm_effmass,3)}")
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
        self.nm_kfn = None
        self.sm_kfn = None
        #: Attribute the neutron matter densities for which the effective mass is provided.
        self.nm_den = None
        self.sm_den = None
        #: Attribute the neutron matter effective mass.
        self.nm_effmass = None
        self.sm_effmass = None
        self.nm_effmass_err = None
        self.sm_effmass_err = None
        #: Attribute the plot label data.
        self.label = ''
        #: Attribute the plot marker.
        self.marker = None
        self.err = False
        #: Attribute the plot every data.
        self.every = 1
        #
        if nuda.env.verb: print("Exit init_self()")
        #
        return self        

