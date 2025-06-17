import math
import numpy as np  # 1.15.0
from scipy.optimize import fsolve
from scipy.interpolate import CubicSpline
from scipy.optimize import curve_fit
import random

import nucleardatapy as nuda

def func_betaeq(var,*args):
    x_el, x_mu = var
    den, esym = args
    n_el = x_el * den
    kFel = ( 3 * nuda.cst.pi2 * n_el )**nuda.cst.third
    mu_el = nuda.cst.hbc * kFel
    if mu_el < nuda.cst.mmuc2:
        x_p = x_el
        eq1 = 4 * esym * (1-2*x_p) - nuda.cst.hbc * ( 3 * nuda.cst.pi2 * x_el * den )**nuda.cst.third
        eq2 = 0.0
    else:
        x_p = x_el + x_mu
        eq1 = 4 * esym * (1-2*x_p) - nuda.cst.hbc * ( 3 * nuda.cst.pi2 * x_el * den )**nuda.cst.third
        n_mu = x_mu * den
        kFmu = ( 3 * nuda.cst.pi2 * n_mu )**nuda.cst.third
        eq2 = kFmu - math.sqrt( kFel**2 - (nuda.cst.mmuc2/nuda.cst.hbc)**2 )
    return (eq1,eq2)

class setupAMBeq():
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
        if nuda.env.verb: print("Enter setupAMBeq()")
        #
        #: Attribute model.
        self.model = model
        if nuda.env.verb: print("model:",model)
        #
        self = setupAMBeq.init_self( self )
        #
        # read var and define den, asy and xpr:
        self.den = var1[:] # density n_b=n_n+n_p
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
        self.label = esym.label
        self.every = esym.every
        self.linestyle = esym.linestyle
        self.marker = esym.marker
        #print('type esym:',type(esym.esym))
        #
        # lepton fractions
        #
        #if isinstance(esym.esym, np.ndarray ):
        if esym.esym is not None:
            self.den = esym.den
            self.nm_den = esym.den
            self.sm_den = esym.den
            self.nm_e2a_int = esym.esym_nm_e2a_int
            self.sm_e2a_int = esym.esym_sm_e2a_int
            self.esym = esym.esym
            self.x_el = []
            self.x_mu = []
            tmp1 = (4*esym.esym[0]/nuda.cst.hbc)**nuda.cst.three
            x_el = tmp1 / (3*nuda.cst.pi2*esym.den[0] + 6*tmp1 )
            #x_el = 0.1
            x_mu = 0.0
            for ind,den in enumerate(esym.den):
                x_el, x_mu =  fsolve(func_betaeq, (x_el, x_mu), args=(den,esym.esym[ind]) )
                #print(f' ind:{ind}, den:{den:.3f}, esym:{esym.esym[ind]:.0f}, x_el:{x_el:.3f}, x_mu:{x_mu:.3f}')
                self.x_el.append( x_el )
                self.x_mu.append( x_mu )
            self.x_el = np.array( self.x_el, dtype = float )
            self.x_mu = np.array( self.x_mu, dtype = float )
            self.x_lep = self.x_el + self.x_mu
            #print('x_el:',self.x_el)
            #print('x_mu:',self.x_mu)
            self.x_p = self.x_el + self.x_mu
            self.x_n = 1.0 - self.x_p
            self.asy = self.x_n - self.x_p
            self.n_n = self.x_n * self.den
            self.n_p = self.x_p * self.den
            #print('n_n:',self.n_n)
            self.kfn = nuda.kf_n( self.n_n )
            self.n_el = self.x_el * self.den
            self.n_mu = self.x_mu * self.den
            self.x_lep = self.x_el + self.x_mu
            #
            # Thermodynamical variables
            # nucleons
            self.rmass = self.x_n * nuda.cst.mnc2 + self.x_p * nuda.cst.mpc2
            self.e2a_int_nuc = esym.esym_sm_e2a_int + esym.esym * self.asy**2
            self.e2a_nuc = self.rmass + self.e2a_int_nuc
            self.eps_int_nuc = self.e2a_int_nuc * self.den
            self.eps_nuc = self.e2a_nuc * self.den
            self.pre_nuc = esym.esym_sm_pre + esym.esym_sym_pre * self.asy**2
            # leptons
            lep = nuda.matter.setupFFGLep( den_el = self.n_el, den_mu = self.n_mu )
            self.e2a_el = self.x_el * lep.e2n_el
            self.e2a_int_el = self.e2a_el - self.x_el * nuda.cst.mec2
            self.e2a_mu = self.x_mu * lep.e2n_mu
            self.e2a_int_mu = self.e2a_mu - self.x_mu * nuda.cst.mmuc2
            self.e2a_lep = self.x_lep * lep.e2n_lep
            self.eps_lep = self.e2a_lep / self.den
            self.pre_el = lep.pre_el
            self.pre_mu = lep.pre_mu
            self.pre_lep = lep.pre_el + lep.pre_mu
            # total
            self.e2a_int_tot = self.e2a_int_nuc + self.e2a_lep
            self.e2a_tot = self.e2a_nuc + self.e2a_lep
            self.eps_int_tot = self.eps_int_nuc + self.eps_lep
            self.eps_tot = self.eps_nuc + self.eps_lep
            self.pre_tot = self.pre_nuc + self.pre_lep
            # enthalpy self.h2a
            self.h2a_lep = self.e2a_lep + self.pre_lep / self.den
            self.h2a_nuc = self.e2a_nuc + self.pre_nuc / self.den
            self.h2a_tot = self.e2a_tot + self.pre_tot / self.den
            # enthaply density self.h2v
            self.h2v_lep = self.h2a_lep * self.den
            self.h2v_nuc = self.h2a_nuc * self.den
            self.h2v_tot = self.h2a_tot * self.den
            # sound speed self.cs2
            x = np.insert(self.den, 0, 0.0)
            y = np.insert(self.pre_lep, 0, 0.0)
            cs_pre = CubicSpline(x, y)
            self.cs2_lep = cs_pre(self.den, 1) / self.h2a_lep
            y = np.insert(self.pre_nuc, 0, 0.0)
            cs_pre = CubicSpline(x, y)
            self.cs2_nuc = cs_pre(self.den, 1) / self.h2a_nuc
            y = np.insert(self.pre_tot, 0, 0.0)
            cs_pre = CubicSpline(x, y)
            self.cs2_tot = cs_pre(self.den, 1) / self.h2a_tot
            #            #
        self.den_unit = 'fm$^{-3}$'
        self.kf_unit = 'fm$^{-1}$'
        self.e2a_unit = 'MeV'
        self.eps_unit = 'MeV fm$^{-3}$'
        self.pre_unit = 'MeV fm$^{-3}$'
        self.gap_unit = 'MeV'
        #
        if nuda.env.verb: print("Exit setupAMBeq()")
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
        if self.eps is not None: print(f"   eps: {np.round(self.eps,3)} in {self.eps_unit}")
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
        self.x_el = None
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
        self.eps = None
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

