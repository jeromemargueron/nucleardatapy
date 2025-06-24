
import numpy as np  # 1.15.0
#from scipy.interpolate import CubicSpline

import nucleardatapy as nuda

def kf( den ):
    """
    Fermi momentum as a function of the density.

    :param den: density.
    :type den: float or numpy vector of real numbers.

    """
    return (1.5*nuda.cst.pi2*den)**nuda.cst.third

def den( kf ):
    """
    Density as a function of the Fermi momentum.

    :param kf_n: Fermi momentum.
    :type kf_n: float or numpy vector of real numbers.

    """
    return nuda.cst.two * kf**nuda.cst.three / ( nuda.cst.three * nuda.cst.pi2 )

def kf_n( den_n ):
    """
    Neutron Fermi momentum as a function of the neutron density.

    :param den_n: neutron density.
    :type den_n: float or numpy vector of real numbers.

    """
    return (nuda.cst.three*nuda.cst.pi2*den_n)**nuda.cst.third

def den_n( kf_n ):
    """
    Neutron density as a function of the neutron Fermi momentum.

    :param kf_n: neutron Fermi momentum.
    :type kf_n: float or numpy vector of real numbers.

    """
    return kf_n**nuda.cst.three / ( nuda.cst.three * nuda.cst.pi2 )

def eF_n( kf_n ):
    """
    Neutron Fermi energy as a function of the neutron Fermi momentum.

    :param kf_n: neutron Fermi momentum.
    :type kf_n: float or numpy vector of real numbers.

    """
    return np.sqrt(nuda.cst.mnc2**2 + (nuda.cst.hbc*kf_n)**2) - nuda.cst.mnc2

def eF_n_nr( kf_n ):
    """
    Non-relativistic neutron Fermi energy as a function of the neutron Fermi momentum.

    :param kf_n: neutron Fermi momentum.
    :type kf_n: float or numpy vector of real numbers.

    """
    return nuda.cst.half * nuda.cst.h2m * kf_n**2

def effg_NM_nr( kf_n ):
    """
    Free Fermi gas energy as a function of the neutron Fermi momentum.

    :param kf_n: neutron Fermi momentum.
    :type kf_n: float or numpy vector of real numbers.

    """
    return nuda.cst.threeFifth * nuda.cst.half * nuda.cst.h2m * kf_n**2

def effg_SM_nr( kf ):
    """
    Free Fermi gas energy as a function of the Fermi momentum in SM.

    :param kf: neutron Fermi momentum.
    :type kf: float or numpy vector of real numbers.

    """
    return nuda.cst.threeFifth * nuda.cst.half * nuda.cst.h2m * kf**2

def effg_nr( kf ):
    """
    Free Fermi gas energy as a function of the Fermi momentum.

    :param kf: Fermi momentum.
    :type kf: float or numpy vector of real numbers.

    """
    return nuda.cst.threeFifth * nuda.cst.half * nuda.cst.h2m * kf**2

def esymffg_nr( kf ):
    """
    Free Fermi gas symmetry energy as a function of the Fermi momentum.

    :param kf: Fermi momentum.
    :type kf: float or numpy vector of real numbers.

    """
    return effg_nr( kf ) * ( nuda.cst.two**nuda.cst.twoThird - 1.0 )

def pre_nr( kf ):
    """
    Free Fermi gas pressure as a function of the Fermi momentum.

    :param kf: Fermi momentum.
    :type kf: float or numpy vector of real numbers.

    """
    return nuda.cst.twoThird * effg_nr( kf ) * den( kf )

def cs2_nr( kf ):
    """
    Free Fermi gas sound speed as a function of the Fermi momentum.

    :param kf: Fermi momentum.
    :type kf: float or numpy vector of real numbers.

    """
    return nuda.cst.twoThird

# FFG energy
def feden(gam, kf, mc2):
    den = gam * kf**3 / ( 6 * nuda.cst.pi2 )
    eps = []
    e2a = []
    for ind, val_kf in enumerate(kf):
        if val_kf > 1e-12:
            pf = nuda.cst.hbc * val_kf
            if mc2 == 0.0:
                term = 2.0 * pf**4
        #return gam / (2.0 * nuda.cst.pi) * (nuda.cst.hbc*kf)**4 / 4.0
            else:
                ef = np.sqrt( pf * pf + mc2 * mc2 )
                r = ( pf + ef ) / mc2
        #term = 2.0 * pf * ef**3 - pf * ef * mc2**2 - mc2**4 * np.log(r) - 8.0 / 3.0 * pf**3 * mc2
                term = 2.0 * pf * ef**3 - pf * ef * mc2**2 - mc2**4 * np.log(r)
            eps.append( gam * term / (16.0 * nuda.cst.pi2 * nuda.cst.hbc**3 ) )
            e2a.append( eps[-1] / den[ind] )
        else:
            eps.append( 0.0 )
            e2a.append( 0.0 )
    eps = np.array( eps, dtype = float )
    e2a = np.array( e2a, dtype = float )
    return eps, e2a

# FFG pressure
def fpres(gam, kf, mc2):
    pre = []
    for val_kf in kf:
        if val_kf > 1e-12:
            pf = nuda.cst.hbc * val_kf
            if mc2 == 0.0:
                term = 2.0 * pf**4
        #return gam / (2.0 * nuda.cst.pi) * kf**4 / 12.0
            else:
                ef = np.sqrt( pf * pf + mc2 * mc2 )
                r = ( pf + ef ) / mc2
                #term = 2.0 * pf**3 * ef - 3.0 * pf * ef * mc2**2 + 3.0 * mc2**4 * np.log(r)
                term = 2.0 * pf * ef**3 - 5.0 * pf * ef * mc2**2 + 3.0 * mc2**4 * np.log(r)
            pre.append( gam * term / (48.0 * nuda.cst.pi2 * nuda.cst.hbc**3 ) )
        else:
            pre.append( 0.0 )
    pre = np.array( pre, dtype = float )
    return pre

# FFG dp/dn
def f_dp_dn(kf, mc2):
    dp_dn = []
    for val_kf in kf:
        if val_kf > 1e-12:
            pf = nuda.cst.hbc * val_kf
            if mc2 == 0.0:
                term = pf
            else:
                ef = np.sqrt( pf * pf + mc2 * mc2 )
                term = pf**2 / ef
            dp_dn.append( term / 3.0 )
        else:
            dp_dn.append( 0.0 )
    dp_dn = np.array( dp_dn, dtype = float )
    return dp_dn

class setupFFGNuc():
    """
    Instantiate the object with free Fermi gas (FFG) quantities.

    :param den: density or densities for which the FFG quantities are calculated.
    :type den: float or numpy vector of floats. 
    :param delta: isospin density or densities for which the FFG quantities are calculated.
    :type delta: float or numpy vector of floats. 
    **Attributes:**
    
    """
    #
    def __init__( self, den, delta, ms = 1.0 ):
        """
        Parameters
        ----------
        den : float or numpy array of floats.
        Density or densities for which the FFG quantities are calculated.
        delta: float or numpy array of floats.
        Isospin density or densities for which the FFG quantities are calculated.
        ms: effective mass in unit of mass.
        """
        #
        if nuda.env.verb: print("Enter setupFFGNuc()")
        #
        #: Attribute providing the label the data is references for figures.
        self.label = r'FFG $\,\delta=$'+str(delta[0])
        #: Attribute providing additional notes about the data.
        self.note = ""
        #: Attribute isoscalar density
        self.den = den 
        #: Attribute isospin parameter
        self.delta = delta 
        #: Attribute the effective mass in unit of mass.
        self.ms = ms
        # Attribute the neutron fraction
        self.x_n = nuda.cst.half * ( nuda.cst.one + self.delta )
        # Attribute the proton fraction
        self.x_p = nuda.cst.half * ( nuda.cst.one - self.delta )
        #: Attribute neutron density
        self.den_n = self.x_n * den
        #: Attribute proton density
        self.den_p = self.x_p * den
        #: Attribute Fermi momentum for a Fermi system with degeneracy = 4
        self.kf_nuc = (1.5 * nuda.cst.pi2 * self.den)**nuda.cst.third
        #: Attribute neutron Fermi momentum (degeneracy = 2)
        self.kf_n = (nuda.cst.three * nuda.cst.pi2 * self.den_n)**nuda.cst.third
        #: Attribute proton Fermi momentum (degeneracy = 2)
        self.kf_p = (nuda.cst.three * nuda.cst.pi2 * self.den_p)**nuda.cst.third
        #: Attribute neutron Fermi energy (degeneracy = 2)
        self.eF_n = np.sqrt( (ms*nuda.cst.mnc2)**2 + (nuda.cst.hbc*self.kf_n)**2 )
        self.eF_n_int = np.sqrt( (ms*nuda.cst.mnc2)**2 + (nuda.cst.hbc*self.kf_n)**2 ) - ms*nuda.cst.mnc2
        self.eF_n_int_nr = nuda.cst.half * nuda.cst.h2m / ms * self.kf_n**nuda.cst.two
        #: Attribute proton Fermi energy (degeneracy = 2)
        self.eF_p = np.sqrt( (ms*nuda.cst.mpc2)**2 + (nuda.cst.hbc*self.kf_p)**2 )
        self.eF_p_int = np.sqrt( (ms*nuda.cst.mpc2)**2 + (nuda.cst.hbc*self.kf_p)**2 ) - ms*nuda.cst.mpc2
        self.eF_p_int_nr = nuda.cst.half * nuda.cst.h2m / ms * self.kf_p**nuda.cst.two
        #: Attribute rest mass energy per particle (degeneracy = 2)
        self.e2a_rm = self.x_n * ms * nuda.cst.mnc2 + self.x_p * ms * nuda.cst.mpc2
        self.eps_rm = self.e2a_rm * self.den
        #: Attribute FFG energy per particle (degeneracy = 2)
        eps_n, e2a_n = feden( 2.0, self.kf_n, ms*nuda.cst.mnc2)
        eps_p, e2a_p = feden( 2.0, self.kf_p, ms*nuda.cst.mpc2)
        self.eps = eps_n + eps_p
        self.e2a = self.x_n * e2a_n + self.x_p * e2a_p
        self.e2a_int = self.e2a - self.e2a_rm
        self.e2a_int_nr = nuda.cst.threeFifth * nuda.cst.half * nuda.cst.h2m / ms * \
           (3*nuda.cst.pi2*nuda.cst.half*den)**nuda.cst.twoThird * \
           nuda.cst.half * \
           ( (nuda.cst.one+delta)**nuda.cst.fiveThird + \
             (nuda.cst.one-delta)**nuda.cst.fiveThird )
        self.e2a_nr = self.e2a_rm + self.e2a_int_nr 
        #: Attribute FFG energy per unit volum (degeneracy = 2)
        self.eps_int = self.e2a_int * self.den
        self.eps_int_nr = self.e2a_int_nr * self.den
        self.eps_nr = self.e2a_nr * self.den
        #: Attribute FFG symmetry energy (degeneracy = 2)
        self.esym_nr = nuda.cst.threeFifth * nuda.cst.half * nuda.cst.h2m / ms * \
           (3*nuda.cst.pi2*nuda.cst.half*den)**nuda.cst.twoThird * \
           ( nuda.cst.two**nuda.cst.twoThird - nuda.cst.one )
        #: Attribute FFG quadratic contribution to the symmetry energy
        self.esym2_nr = nuda.cst.threeFifth * nuda.cst.half * nuda.cst.h2m / ms * \
           (3*nuda.cst.pi2*nuda.cst.half*den)**nuda.cst.twoThird * \
           10.0/18.0
        #: Attribute FFG quartic contribution to the symmetry energy
        self.esym4_nr = nuda.cst.threeFifth * nuda.cst.half * nuda.cst.h2m / ms * \
           (3*nuda.cst.pi2*nuda.cst.half*den)**nuda.cst.twoThird * \
           5.0/243.0
        #: Attribute FFG pressure (degeneracy = 2)
        self.pre = fpres( 2.0, self.kf_n, ms*nuda.cst.mnc2 ) + fpres( 2.0, self.kf_p, ms*nuda.cst.mpc2 )
        #print('pre:',self.pre)
        self.pre_nr = nuda.cst.twoThird * self.eps_int_nr
        #print('pre_nr:',self.pre_nr)
        # spline the pressure p(n) to extract dp/dn:
        #cs_pre = CubicSpline( self.den, self.pre )
        #: Attribute enthalpy
        self.h2a = ( self.eps + self.pre ) / self.den
        #print('h2a:',self.h2a)
        self.h2a_nr = ( self.eps_nr + self.pre_nr ) / self.den
        #print('h2a_nr:',self.h2a_nr)
        #: Attribute sound speed squared
        dp_dn = self.x_n * f_dp_dn( self.kf_n, ms*nuda.cst.mnc2 ) + self.x_p * f_dp_dn( self.kf_p, ms*nuda.cst.mpc2 )
        #print('dp_dn:',dp_dn)
        #dp_dn_num = cs_pre( self.den, 1 )
        #print('dp_dn_num:',dp_dn_num)
        self.cs2 = dp_dn / self.h2a 
        #self.cs2_num = dp_dn_num / self.h2a
        #self.cs2_nr = 10.0 / 9.0 * self.eps_nr / self.den / self.h2a_nr
        dp_dn_nr = 10.0 / 9.0 * self.e2a_int_nr
        #print('dp_dn_nr:',dp_dn_nr)
        #print('dp_dn_nr/dp_dn:',dp_dn_nr/dp_dn)
        self.cs2_nr = dp_dn_nr / self.h2a_nr
        #
        self.den_unit = 'fm$^{-3}$'
        self.kf_unit = 'fm$^{-1}$'
        self.e2a_unit = 'MeV'
        self.eps_unit = 'MeV fm$^{-3}$'
        self.pre_unit = 'MeV fm$^{-3}$'
        self.cs2_unit = 'c$^{2}$'
        #
        if nuda.env.verb: print("Exit setupFFGNuc()")
    #
    def print_outputs( self ):
        """
        Method which print outputs on terminal's screen.
        """
        print("")
        #
        if nuda.env.verb: print("Enter print_outputs()")
        #
        print("- Print output:")
        if self.den is not None: print(f"   den: {np.round(self.den,2)} in {self.den_unit}")
        if self.delta is not None: print(f"   delta: {np.round(self.delta,2)}")
        if self.kf_n is not None: print(f"   kf_n: {np.round(self.kf_n,2)} in {self.kf_unit}")
        if self.e2a_int is not None: print(f"   e2a_int: {np.round(self.e2a_int,2)} in {self.e2a_unit}")
        if self.pre is not None: print(f"   pre: {np.round(self.pre,2)} in {self.pre_unit}")
        if self.cs2 is not None: print(f"   cs2: {np.round(self.cs2,3)} in {self.cs2_unit}")
        print('The non-relativistic quantities are:')
        if self.e2a_int_nr is not None: print(f"   e2a_int_nr: {np.round(self.e2a_int_nr,2)} in {self.e2a_unit}")
        if self.pre_nr is not None: print(f"   pre_nr: {np.round(self.pre_nr,2)} in {self.pre_unit}")
        if self.cs2_nr is not None: print(f"   cs2_nr: {np.round(self.cs2_nr,3)} in {self.cs2_unit}")
        #
        if nuda.env.verb: print("Exit print_outputs()")
        #

class setupFFGLep():
    """
    Instantiate the object with free Fermi gas (FFG) quantities.

    :param den: density or densities for which the FFG quantities are calculated.
    :type den: float or numpy vector of floats. 
    :param delta: isospin density or densities for which the FFG quantities are calculated.
    :type delta: float or numpy vector of floats. 
    **Attributes:**
    
    """
    #
    def __init__( self, den_el, den_mu ):
        """
        Parameters
        ----------
        den_e : float or numpy array of floats.
        Density or densities for the electron component.
        den_mu : float or numpy array of floats.
        Density or densities for the muon component.

        """
        #
        if nuda.env.verb: print("Enter setupFFGLep()")
        #
        #: Attribute providing the label the data is references for figures.
        self.label = r'FFG e+$\mu$'
        #: Attribute providing additional notes about the data.
        self.note = ""
        #: Attribute electron density
        self.den_el = den_el
        #: Attribute muon density
        self.den_mu = den_mu
        #: Attribute lepton density
        self.den_lep = den_el + den_mu
        #: Attribute electron fraction
        self.x_el = den_el / self.den_lep
        #: Attribute muon fraction
        self.x_mu = den_mu / self.den_lep
        #: Attribute electron Fermi momentum (degeneracy = 2)
        self.kf_el = ( nuda.cst.three * nuda.cst.pi2 * self.den_el )**nuda.cst.third
        #: Attribute muon Fermi momentum (degeneracy = 2)
        self.kf_mu = ( nuda.cst.three * nuda.cst.pi2 * self.den_mu )**nuda.cst.third
        #: Attribute electon Fermi energy (degeneracy = 2)
        self.eF_el = np.sqrt( nuda.cst.mec2**2 + (nuda.cst.hbc*self.kf_el)**2 )
        #: Attribute muon Fermi energy (degeneracy = 2)
        self.eF_mu = np.sqrt( nuda.cst.mmuc2**2 + (nuda.cst.hbc*self.kf_mu)**2 )
        #: Attribute FFG energy per particle (degeneracy = 2)
        # energy
        self.eps_el, self.e2n_el = feden( 2.0, self.kf_el, nuda.cst.mec2 )
        self.eps_mu, self.e2n_mu = feden( 2.0, self.kf_mu, nuda.cst.mmuc2 )
        self.eps_lep = self.eps_el + self.eps_mu
        self.e2n_lep = self.eps_lep / self.den_lep
        #self.e2a_el = self.eps_el / self.den_e
        # internal energy
        self.eps_el_int = self.eps_el - nuda.cst.mec2*self.den_el
        self.e2n_el_int = self.eps_el_int / self.den_el
        self.eps_mu_int = self.eps_mu - nuda.cst.mmuc2*self.den_mu
        self.e2n_mu_int = np.zeros( np.size(self.den_mu) )
        for k,n_mu in enumerate(self.den_mu):
            if n_mu > 0.0:
                self.e2n_mu_int[k] = self.eps_mu_int[k] / self.den_mu[k]
        self.eps_lep_int = self.eps_el_int + self.eps_mu_int
        self.e2n_lep_int = self.eps_lep_int / self.den_lep
        #: Attribute FFG pressure (degeneracy = 2)
        self.pre_el = fpres( 2.0, self.kf_el, nuda.cst.mec2)
        self.pre_mu = fpres( 2.0, self.kf_mu, nuda.cst.mmuc2)
        self.pre_lep = self.x_el * self.pre_el + self.x_mu * self.pre_mu
        #: Attribute enthalpy
        self.h2n_el = self.e2n_el + self.pre_el / self.den_el
        self.h2n_mu = []
        for ind,den_mu in enumerate(self.den_mu):
            if den_mu != 0.0:
                self.h2n_mu.append( self.e2n_mu[ind] + self.pre_mu[ind] / self.den_mu[ind] )
            else:
                self.h2n_mu.append( 0.0 )
        self.h2n_mu = np.array( self.h2n_mu, dtype = float )
        self.h2n_lep = self.x_el * self.h2n_el + self.x_mu * self.h2n_mu
        #: Attribute sound speed squared
        dp_dn = self.den_el * f_dp_dn( self.kf_el, nuda.cst.mec2 ) + self.den_mu * f_dp_dn( self.kf_mu, nuda.cst.mmuc2 )
        self.cs2_lep = dp_dn / self.h2n_lep
        #
        self.den_unit = 'fm$^{-3}$'
        self.kf_unit = 'fm$^{-1}$'
        self.e2n_unit = 'MeV'
        self.eps_unit = 'MeV fm$^{-3}$'
        self.pre_unit = 'MeV fm$^{-3}$'
        #
        if nuda.env.verb: print("Exit setupFFGLep()")
    #
    def print_outputs( self ):
        """
        Method which print outputs on terminal's screen.
        """
        print("")
        #
        if nuda.env.verb: print("Enter print_outputs()")
        #
        print("- Print output:")
        if self.den_el is not None: print(f"   den_el: {np.round(self.den_el,2)} in {self.den_unit}")
        if self.den_mu is not None: print(f"   den_mu: {np.round(self.den_mu,2)}")
        if self.kf_el is not None: print(f"   kf_el: {np.round(self.kf_el,2)} in {self.kf_unit}")
        if self.e2n_lep_int is not None: print(f"   e2n_lep_int: {np.round(self.e2n_lep_int,2)} in {self.e2n_unit}")
        if self.pre_lep is not None: print(f"   pre_lep: {np.round(self.pre_lep,2)} in {self.pre_unit}")
        if self.cs2_lep is not None: print(f"   cs2_lep: {np.round(self.cs2_lep,3)}")
        #
        if nuda.env.verb: print("Exit print_outputs()")
        #



