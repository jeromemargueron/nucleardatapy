import os
import sys
import math
import numpy as np  # 1.15.0
from scipy.optimize import fsolve
from scipy.interpolate import CubicSpline
from scipy.optimize import curve_fit
import random

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

class setupAM():
    """
    Instantiate the object with microscopic results choosen \
    by the toolkit practitioner.

    :param model: Fix the name of model. Default value: '1998-VAR-AM-APR'.
    :type model: str, optional. 
    :param kind: chose between 'micro' and 'pheno'.
    :type kind: str, optional.

    **Attributes:**
    """
    #
    def __init__( self, model = '1998-VAR-AM-APR', param = None, kind = 'micro', asy = 0.0, x_mu = 0.0, var1 = np.linspace(0.01,0.4,100) ):
        """
        Parameters
        ----------
        model : str, optional
        The model to consider. Choose between: 1998-VAR-AM-APR (default), 2008-AFDMC-NM, ...
        kind : chose between 'micro' or 'pheno'.
        var1 and var2 : densities (array) and isospin asymmetry (scalar) if necessary (for interpolation function in APRfit for instance)
        var1 = np.array([0.1,0.15,0.16,0.17,0.2,0.25])
        """
        #
        if nuda.env.verb: print("Enter setupAM()")
        #
        #: Attribute model.
        self.model = model
        if nuda.env.verb: print("model:",model)
        #
        self = setupAM.init_self( self )
        #
        # read var and define den, asy and xpr:
        self.den = np.array( var1, dtype=float ) # density n_b=n_n+n_p
        self.asy = float(asy)
        #
        if kind == 'micro':
            models, models_lower = nuda.matter.micro_esym_models()
            models.remove('1998-VAR-AM-APR-fit')
            models_lower.remove('1998-var-am-apr-fit')
        elif kind == 'pheno':
            models, models_lower = nuda.matter.pheno_esym_models()
        #
        if model.lower() not in models_lower:
            print('The model name ',model,' is not in the list of models.')
            print('list of models:',models)
            print('-- Exit the code --')
            exit()
        #
        if kind == 'micro':
            esym = nuda.matter.setupMicroEsym( model = model )
            #eos.print_outputs( )
        elif kind == 'pheno':
            esym = nuda.matter.setupPhenoEsym( model = model, param = param )
            #eos.print_outputs( )
        else:
            print('Issue with variable kind=',kind)
            exit()
        self.label = esym.label
        self.every = esym.every
        self.linestyle = esym.linestyle
        self.marker = esym.marker
        #print('type esym:',type(esym.esym))
        self.den = esym.den
        self.esym = esym.esym
        #print('esym:',self.esym)
        self.x_n = ( 1.0 + self.asy ) / 2.0
        self.x_p = ( 1.0 - self.asy ) / 2.0
        self.x_mu = x_mu
        self.x_e = self.x_p - self.x_mu
        self.n_n = self.x_n * self.den
        self.n_p = self.x_p * self.den
        self.kfn = nuda.kf_n( self.n_n )
        self.n_e = self.x_e * self.den
        self.n_mu = self.x_mu * self.den
        #
        # Thermodynamical variables
        self.e2a_nuc = esym.e2a_sm + esym.esym * self.asy**2
        self.e2v_nuc = self.e2a_nuc * self.den
        lep = nuda.matter.setupFFGLep( den_e = self.n_e, den_mu = self.n_mu )
        self.e2a_el = lep.e2a_el
        self.e2a_mu = lep.e2a_mu
        self.e2a_lep = lep.e2a_el + lep.e2a_mu
        self.pre_el = lep.pre_el
        self.pre_mu = lep.pre_mu
        self.pre_lep = lep.pre_el + lep.pre_mu
        # self.h2a
        # self.h2v
        # self.cs2

        self.den_unit = 'fm$^{-3}$'
        self.kf_unit = 'fm$^{-1}$'
        self.e2a_unit = 'MeV'
        self.e2v_unit = 'MeV fm$^{-3}$'
        self.pre_unit = 'MeV fm$^{-3}$'
        self.gap_unit = 'MeV'
        #
        if nuda.env.verb: print("Exit setupAM()")
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
        #if any(self.sm_den): print(f"   sm_den: {np.round(self.sm_den,3)} in {self.den_unit}")
        if self.den is not None: print(f"   den: {np.round(self.den,3)} in {self.den_unit}")
        if self.kfn is not None: print(f"   kfn: {np.round(self.den,3)} in {self.kf_unit}")
        if self.asy is not None: print(f"   asy: {np.round(self.asy,3)}")
        if self.e2a is not None: print(f"   e2a: {np.round(self.e2a,3)} in {self.e2a_unit}")
        if self.e2v is not None: print(f"   e2v: {np.round(self.e2v,3)} in {self.e2v_unit}")
        if self.pre is not None: print(f"   pre: {np.round(self.pre,3)} in {self.pre_unit}")
        if self.cs2 is not None: print(f"   cs2: {np.round(self.cs2,2)}")
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
        #: Attribute the matter asymmetry parameter (n_n-n_p)/(n_n+n_p).
        self.asy = None
        #: Attribute the matter density.
        self.den = None
        #: Attribute the symmetry energy.
        self.esym = None
        #: Attribute the neutron fraction.
        self.x_n = None
        #: Attribute the proton fraction.
        self.x_p = None
        #: Attribute the neutron density
        self.n_n = None
        #: Attribute the proton density.
        self.n_p = None
        #: Attribute the neutron Fermi momentum.
        self.kfn = None

        #: Attribute the energy per particle.
        self.e2a = None
        #: Attribute the energy per unit volume.
        self.e2v = None
        #: Attribute the enthalpy per particle.
        self.h2a = None
        #: Attribute the enthalpy per unit volume.
        self.h2v = None
        #: Attribute the pressure.
        self.pre = None
        #: Attribute the sound speed.
        self.cs2 = None
        #self.chempot_n
        #self.chempot_p
        #: Attribute the neutron matter effective mass.
        #self.effmass_n = None
        #: Attribute the symmetric matter effective mass.
        #self.effmass_p = None

        #: Attribute the plot linestyle.
        self.linestyle = None
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

