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

def beta_eq(var,*args):
    x_e, x_mu = var
    den, esym = args
    n_e = x_e * den
    kFe = ( 3 * nuda.cst.pi2 * n_e )**nuda.cst.third
    mu_e = nuda.cst.hbc * kFe
    if mu_e < nuda.cst.mmuc2:
        x_p = x_e
        eq1 = 4 * esym * (1-2*x_p) - nuda.cst.hbc * ( 3 * nuda.cst.pi2 * x_e * den )**nuda.cst.third
        eq2 = 0.0
    else:
        x_p = x_e + x_mu
        eq1 = 4 * esym * (1-2*x_p) - nuda.cst.hbc * ( 3 * nuda.cst.pi2 * x_e * den )**nuda.cst.third
        n_mu = x_mu * den
        kFmu = ( 3 * nuda.cst.pi2 * n_mu )**nuda.cst.third
        eq2 = kFmu - math.sqrt( kFe**2 - (nuda.cst.mmuc2/nuda.cst.hbc)**2 )
    return (eq1,eq2)

class setupBeta():
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
    def __init__( self, model = '1998-VAR-AM-APR', param = None, kind = 'micro', var1 = np.linspace(0.01,0.4,100) ):
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
        if nuda.env.verb: print("Enter setupBeta()")
        #
        #: Attribute model.
        self.model = model
        if nuda.env.verb: print("model:",model)
        #
        self = setupBeta.init_self( self )
        #
        # read var and define den, asy and xpr:
        self.den = var1[:] # density n_b=n_n+n_p
        #
        if kind == 'micro':
            models, models_lower = nuda.eos.micro_esym_models()
            models.remove('1998-VAR-AM-APRfit')
            models_lower.remove('1998-var-am-aprfit')
        elif kind == 'pheno':
            models, models_lower = nuda.eos.pheno_esym_models()
        #
        if model.lower() not in models_lower:
            print('The model name ',model,' is not in the list of models.')
            print('list of models:',models)
            print('-- Exit the code --')
            exit()
        #
        if kind == 'micro':
            esym = nuda.eos.setupMicroEsym( model = model )
            #eos.print_outputs( )
        elif kind == 'pheno':
            esym = nuda.eos.setupPhenoEsym( model = model, param = param )
            #eos.print_outputs( )
        self.label = esym.label
        self.every = esym.every
        self.linestyle = esym.linestyle
        self.marker = esym.marker
        #print('type esym:',type(esym.esym))

        #if isinstance(esym.esym, np.ndarray ):
        if esym.esym is not None:
            self.den = esym.den
            self.esym = esym.esym
            self.x_e = []
            self.x_mu = []
            tmp1 = (4*esym.esym[0]/nuda.cst.hbc)**nuda.cst.three
            x_e = tmp1 / (3*nuda.cst.pi2*esym.den[0] + 6*tmp1 )
            #x_e = 0.1
            x_mu = 0.0
            for ind,den in enumerate(esym.den):
                x_e, x_mu =  fsolve(beta_eq, (x_e, x_mu), args=(den,esym.esym[ind]) )
                #print(f' ind:{ind}, den:{den:.3f}, esym:{esym.esym[ind]:.0f}, x_e:{x_e:.3f}, x_mu:{x_mu:.3f}')
                self.x_e.append( x_e )
                self.x_mu.append( x_mu )
            self.x_e = np.array( self.x_e, dtype = float )
            self.x_mu = np.array( self.x_mu, dtype = float )
            #print('x_e:',self.x_e)
            #print('x_mu:',self.x_mu)
            self.x_p = self.x_e + self.x_mu
            self.x_n = 1.0 - self.x_p
            self.asy = self.x_n - self.x_p
            self.n_n = self.x_n * self.den
            self.n_p = self.x_p * self.den
            #print('n_n:',self.n_n)
            self.kfn = nuda.kf_n( self.n_n )
            #
            # Thermodynamical variables (with contributions from nucleons and leptons)
            # self.e2a_nuc = eos.e2a
            # self.e2a_lep = 
            # self.e2a = self.e2a_nuc + self.e2a_lep
            # self.e2v = self.e2a * self.den
            # self.pre_nuc = eos.pre
            # self.pre_lep = 
            # self.pre = self.pre_nuc + self.pre_lep
            # self.pre
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
        if nuda.env.verb: print("Exit setupMicro()")
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
        #: Attribute the matter density.
        self.den = None
        #: Attribute the symmetry energy.
        self.esym = None
        #: Attribute the neutron fraction.
        self.x_n = None
        #: Attribute the proton fraction.
        self.x_p = None
        #: Attribute the electron fraction.
        self.x_e = None
        #: Attribute the muon fraction.
        self.x_mu = None
        #: Attribute the matter asymmetry parameter (n_n-n_p)/(n_n+n_p).
        self.asy = None
        #: Attribute the neutron density
        self.n_n = None
        #: Attribute the proton density.
        self.n_p = None
        #: Attribute the neutron Fermi momentum.
        self.kfn = None

        #: Attribute the energy per particle (nucleon contribution).
        self.e2a_nuc = None
        #: Attribute the energy per particle (lepton contribution).
        self.e2a_lep = None
        #: Attribute the energy per particle (total).
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

