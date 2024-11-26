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

nsat = 0.16
mnuc2 = 939.0

def micro_esym_models():
    """
    Return a list with the name of the models available in this toolkit and \
    print them all on the prompt. These models are the following ones: \
    '1981-VAR-AM-FP', '1998-VAR-AM-APR', '1998-VAR-AM-APRfit', '2006-BHF-AM*', \
    2016-MBPT-AM', 2019-MBPT-AM-L59', '2019-MBPT-AM-L69', \
    '2020-MBPT-AM', '2024-NLEFT-AM', \
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
    #
    if nuda.env.verb: print("\nEnter micro_esym_models()")
    #
    models = [ '1981-VAR-AM-FP', '1998-VAR-AM-APR', '1998-VAR-AM-APRfit', \
               '2016-MBPT-AM', '2019-MBPT-AM-L59', '2019-MBPT-AM-L69', \
             '2020-MBPT-AM', '2024-NLEFT-AM', \
            '2024-BHF-AM-2BF-Av8p', '2024-BHF-AM-2BF-Av18', '2024-BHF-AM-2BF-BONN', '2024-BHF-AM-2BF-CDBONN', \
            '2024-BHF-AM-2BF-NSC97a', '2024-BHF-AM-2BF-NSC97b', '2024-BHF-AM-2BF-NSC97c', '2024-BHF-AM-2BF-NSC97d', \
            '2024-BHF-AM-2BF-NSC97e', '2024-BHF-AM-2BF-NSC97f', '2024-BHF-AM-2BF-SSCV14',\
            '2024-BHF-AM-23BF-Av8p', '2024-BHF-AM-23BF-Av18', '2024-BHF-AM-23BF-BONN', '2024-BHF-AM-23BF-CDBONN', \
            '2024-BHF-AM-23BF-NSC97a', '2024-BHF-AM-23BF-NSC97b', '2024-BHF-AM-23BF-NSC97c', '2024-BHF-AM-23BF-NSC97d', \
            '2024-BHF-AM-23BF-NSC97e', '2024-BHF-AM-23BF-NSC97f', '2024-BHF-AM-23BF-SSCV14' ]
    if nuda.env.verb: print('models available in the toolkit:',models)
    models_lower = [ item.lower() for item in models ]
    #
    if nuda.env.verb: print("Exit micro_esym_models()")
    #
    return models, models_lower

class setupMicroEsym():
    """
    Instantiate the object with microscopic results choosen \
    by the toolkit practitioner.

    This choice is defined in `model`, which can chosen among \
    the following choices: \
    '1981-VAR-AM-FP', '1998-VAR-AM-APR', '1998-VAR-AM-iAPR', '2006-BHF-AM*', \
    '2016-MBPT-AM', '2019-MBPT-AM-L59', '2019-MBPT-AM-L69', \
    '2020-MBPT-AM', '2024-NLEFT-AM', \
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
    def __init__( self, model = '1998-VAR-AM-APR', var1 = np.linspace(0.01,0.4,20), var2 = 0.0 ):
        """
        Parameters
        ----------
        model : str, optional
        The model to consider. Choose between: 1998-VAR-AM-APR (default), 2008-AFDMC-NM, ...
        var1 and var2 : densities (array) and isospin asymmetry (scalar) if necessary (for interpolation function in APRfit for instance)
        var1 = np.array([0.1,0.15,0.16,0.17,0.2,0.25])
        """
        #
        if nuda.env.verb: print("Enter setupMicroEsym()")
        #
        #: Attribute model.
        self.model = model
        if nuda.env.verb: print("model:",model)
        print("-> model:",model)
        #
        self = setupMicroEsym.init_self( self )
        #
        models, models_lower = micro_esym_models()
        #
        if model.lower() not in models_lower:
            print('The model name ',model,' is not in the list of models.')
            print('list of models:',models)
            print('-- Exit the code --')
            exit()
        #
        # =========================
        # load NM and SM quantities
        # =========================
        #
        if 'fit' in model.lower():
            #
            # SM
            #
            mic = nuda.eos.setupMicro( model = model, var1 = var1, var2 = 0.0 )
            sm_den = mic.den
            sm_e2a = mic.e2a
            sm_e2a_err = mic.e2a_err
            #
            # NM
            #
            mic = nuda.eos.setupMicro( model = model, var1 = var1, var2 = 1.0 )
            nm_den = mic.den
            nm_e2a = mic.e2a
            nm_e2a_err = mic.e2a_err
            #
        else:
            mic = nuda.eos.setupMicro( model = model )
            sm_den = mic.sm_den
            sm_e2a = mic.sm_e2a
            sm_e2a_err = mic.sm_e2a_err
            nm_den = mic.nm_den
            nm_e2a = mic.nm_e2a
            nm_e2a_err = mic.nm_e2a_err
            #mic.print_outputs( )
        #
        # ===========================
        # compute the symmetry energy
        # ===========================
        #
        self.ref = mic.ref
        self.note = mic.note
        self.label = mic.label
        self.marker = mic.marker
        self.linestyle = mic.linestyle
        self.err = True
        #
        # E/A in SM (cubic spline)
        #
        x = np.insert( sm_den, 0, 0.0 ); y = np.insert( sm_e2a, 0, 0.0 )
        cs_sm_e2a = CubicSpline( x, y )
        y_err = np.insert( sm_e2a_err, 0, 0.0 )
        cs_sm_e2a_err = CubicSpline( x, y_err )
        #
        # E/A in NM (cubic spline)
        #
        x = np.insert( nm_den, 0, 0.0 ); y = np.insert( nm_e2a, 0, 0.0 )
        cs_nm_e2a = CubicSpline( x, y )
        y_err = np.insert( nm_e2a_err, 0, 0.0 )
        cs_nm_e2a_err = CubicSpline( x, y_err )
        #
        # density for Esym (no extroplation, only interpolation)
        #
        self.den_min = max( min( nm_den), min( sm_den) )
        self.den_max = min( max( nm_den), max( sm_den) )
        self.kf_min = nuda.kf( self.den_min ); self.kf_max = nuda.kf( self.den_max )
        den_step = ( self.den_max - self.den_min ) / float( self.nesym )
        self.den = self.den_min + np.arange(self.nesym+1) * den_step
        self.kf = nuda.kf( self.den )
        #
        # Symmetry energy for the densities defined in self.den
        #
        self.e2a_sm = cs_sm_e2a( self.den )
        self.e2a_nm = cs_nm_e2a( self.den )
        self.esym = self.e2a_nm - self.e2a_sm
        self.esym_err = np.sqrt( cs_nm_e2a_err( self.den )**2 + cs_sm_e2a_err( self.den )**2 )
        #
        self.den_unit = 'fm$^{-3}$'
        self.kf_unit = 'fm$^{-1}$'
        self.esym_unit = 'MeV'
        #
        if nuda.env.verb: print("Exit setupMicroEsym()")
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
        #
        if self.den is not None: print(f"   den: {np.round(self.den,3)} in {self.den_unit}")
        if self.kf is not None: print(f"   kf: {np.round(self.kf,3)} in {self.kf_unit}")
        if self.esym is not None: print(f"   esym: {np.round(self.esym,3)} in {self.esym_unit}")
        if self.esym_err is not None: print(f"   esym_err: {np.round(self.esym_err,3)} in {self.esym_unit}")
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
        #: Attribute the number of points for esym calculation.
        self.nesym = 20; 
        #: Attribute providing the full reference to the paper to be citted.
        self.ref = ''
        #: Attribute providing additional notes about the data.
        self.note = ''
        #: Attribute the plot label data.
        self.label = ''
        #: Attribute the plot linestyle.
        self.linestyle = None
        #: Attribute the plot marker.
        self.marker = None
        #: Attribute the plot every data.
        self.every = 1
        #
        #: Attribute the matter density.
        self.den = None
        #: Attribute the neutron Fermi momentum.
        self.kf = None
        #: Attribute the minimum of the density.
        self.den_min = None
        #: Attribute the maximum of the density.
        self.den_max = None
        #: Attribute the minimum of the Fermi momentum.
        self.kf_min = None
        #: Attribute the maximum of the Fermi momentum.
        self.kf_max = None
        #: Attribute the symmetry energy per particle.
        self.esym = None
        #: Attribute the uncertainty in the symmetry energy per particle.
        self.esym_err = None
        #
        if nuda.env.verb: print("Exit init_self()")
        #
        return self        

