import math
import os
import sys
import numpy as np  # 1.15.0
from scipy.interpolate import CubicSpline
from scipy.optimize import curve_fit
import random

import nucleardatapy as nuda

nsat = 0.16
mnuc2 = 939.0

def matter_esym_params( model ):
    """
    Return a list with the parameterizations available in 
    this toolkit for a given model and print them all on the prompt.

    :param model: The type of model for which there are parametrizations.
    :type model: str.
    :rtype: list[str].
    """
    #
    if nuda.env.verb: print("\nEnter matter_esym_params()")
    #
    models, models_lower = nuda.matter.matter_models( )
    #print(f'models: {models}')
    #
    if model.lower() not in models_lower:
        print('In matter_esym_params( model ): The model name ',model,' is not in the list of models.')
        print('In matter_esym_params( model ): list of models:',models)
        print('-- Exit the code --')
        exit()
    # extract all parameters existing in the folder model
    path_model = os.path.join(nuda.param.path_data,'matter/type/'+model)
    print(f'path_model: {path_model}')
    #params = [ os.path.splitext(par)[0] for par in os.listdir(path_model) if par.endswith('.dat')]
    all_params = [ par[:-4] for par in os.listdir(path_model) if par.endswith('.dat')]
    # remove params that contain '-AM-' in their name:
    params = []
    for param in all_params:
        if '-AM-' not in param:
            params.append(param)
    # select only the parameters for which SM and NM have been calculated:
    params.sort()
    new_params = []
    #for k,param in enumerate(params):
    for k in range(len(params)-1):
        #print(f'params[{k}][:-3]: {params[k][:-3]}')
        if params[k][:-3]==params[k+1][:-3]:
            new_params.append(params[k][:-3])
    params = list(set(new_params))
    #print(f'params: {params}')
    params.sort()
    #
    params_lower = [ item.lower() for item in params ]
    #
    if nuda.env.verb: print("Exit matter_esym_params()")
    #
    return params, params_lower


def matter_esym_params_old( model ):
    """
    Return a list with the parameterizations available in 
    this toolkit for a given model and print them all on the prompt.

    :param model: The type of model for which there are parametrizations.
    :type model: str.
    :rtype: list[str].
    """
    #
    if nuda.env.verb: print("\nEnter matter_esym_params_old()")
    #
    #print('For model:',model)
    if model.lower() == 'skyrme':
        params = [ 'BSK14', 'BSK16', 'BSK17', 'BSK27', 'BSkG1', 'BSkG2', 'F-', \
            'F+', 'F0', 'FPL', 'LNS', 'LNS1', 'LNS5', 'NRAPR', 'RATP', \
            'SAMI', 'SGII', 'SIII', 'SKGSIGMA', 'SKI2', 'SKI4', 'SKMP', \
            'SKMS', 'SKO', 'SKOP', 'SKP', 'SKRSIGMA', 'SKX', 'Skz2', \
            'SLY4', 'SLY5', 'SLY230A', 'SLY230B', 'SV', 'T6', 'T44', \
            'UNEDF0', 'UNEDF1' ]
    elif model.lower() == 'eskyrme':
        params = [ 'BSk22', 'BSk24', 'BSk25', 'BSk26', 'BSk31', 'BSk32',  'BSkG3','BSkG4' ]
    elif model.lower() == 'fayans':
        params = [ 'Fy(IVP)', 'Fy(Dr,HDB)', 'Fy(std)' ]
    elif model.lower() == 'gogny':
        params = [ 'D1S', 'D1', 'D250', 'D260', 'D280', 'D300' ]
    elif model.lower() == 'nlrh':
        params = [ 'NL-SH', 'NL3', 'NL3II', 'PK1', 'PK1R', 'TM1' ]
    elif model.lower() == 'ddrh':
        params = [ 'DDME1', 'DDME2', 'DDMEd', 'PKDD', 'TW99' ]
    elif model.lower() == 'ddrhf':
        params = [ 'PKA1', 'PKO1', 'PKO2', 'PKO3' ]
    #print('Parameters available in the toolkit:',params)
    #
    params_lower = [ item.lower() for item in params ]
    #
    if nuda.env.verb: print("Exit matter_esym_params_old()")
    #
    return params, params_lower

class setupMatterEsym():
    """
    Instantiate the object with results based on phenomenological\
    interactions and choosen by the toolkit practitioner. \
    This choice is defined in the variables `model` and `param`.

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
        """
        Parameters
        ----------
        model : str, optional
        The model to consider. Choose between: 1998-VAR-AM-APR (default), 2008-AFDMC-NM, ...
        var1 and var2 : densities (array) and isospin asymmetry (scalar) if necessary (for interpolation function in APRfit for instance)
        var1 = np.array([0.1,0.15,0.16,0.17,0.2,0.25])
        """
        #
        if nuda.env.verb: print("Enter setupMatterEsym()")
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
        self = setupMatterEsym.init_self( self )
        #
        models, models_lower = nuda.matter.matter_models()
        #
        if model.lower() not in models_lower:
            print('in setupMatterEsym: The model name ',model,' is not in the list of models.')
            print('in setupMatterEsym: list of models:',models)
            print('-- Exit the code --')
            exit()
        #
        params, params_lower = matter_esym_params( model = model )
        #
        if param.lower() not in params_lower:
            print('in setupMatterEsym: The param set ',param,' is not in the list of param.')
            print('in setupMatterEsym: list of param:',params)
            print('-- Exit the code --')
            exit()
        #
        # =========================
        # load NM and SM quantities
        # =========================
        #
        matt = nuda.matter.setupMatter( model = model, param = param )
        self.sm_den = matt.sm_den
        self.sm_e2a_int = matt.sm_e2a_int
        self.nm_den = matt.nm_den
        self.nm_e2a_int = matt.nm_e2a_int
        #pheno.print_outputs( )
        #
        # ===========================
        # compute the symmetry energy
        # ===========================
        #
        self.ref = matt.ref
        self.note = matt.note
        self.label = matt.label
        self.marker = matt.marker
        self.linestyle = matt.linestyle
        #
        # E/A in SM (cubic spline)
        #
        x = np.insert( self.sm_den, 0, 0.0 ); y = np.insert( self.sm_e2a_int, 0, 0.0 )
        cs_sm_e2a = CubicSpline( x, y )
        #
        # E/A in NM (cubic spline)
        #
        x = np.insert( self.nm_den, 0, 0.0 ); y = np.insert( self.nm_e2a_int, 0, 0.0 )
        cs_nm_e2a = CubicSpline( x, y )
        #
        # density for Esym (no extroplation, only interpolation)
        #
        self.den_min = max( min( self.nm_den), min( self.sm_den) )
        self.den_max = min( max( self.nm_den), max( self.sm_den) )
        self.kf_min = nuda.kf( self.den_min ); self.kf_max = nuda.kf( self.den_max )
        den_step = ( self.den_max - self.den_min ) / float( self.nesym )
        self.den = self.den_min + np.arange(self.nesym+1) * den_step
        self.kfn = nuda.kf_n( nuda.cst.half * self.den )
        #
        # Symmetry energy for the densities defined in self.den
        #
        self.esym_sm_e2a_int = cs_sm_e2a( self.den )
        self.esym_nm_e2a_int = cs_nm_e2a( self.den )
        self.esym = self.esym_nm_e2a_int - self.esym_sm_e2a_int
        self.esym_sm_pre = self.den**2 * cs_sm_e2a( self.den, 1 )
        self.esym_sym_pre = self.den**2 * cs_nm_e2a( self.den, 1 ) - self.esym_sm_pre
        #
        self.den_unit = 'fm$^{-3}$'
        self.kfn_unit = 'fm$^{-1}$'
        self.esym_unit = 'MeV'
        self.eps_unit = 'MeV fm$^{-3}$'
        self.pre_unit = 'MeV fm$^{-3}$'
        #
        if nuda.env.verb: print("Exit SetupMatterEsym()")
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

