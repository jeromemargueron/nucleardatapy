import os
import sys
import numpy as np  # 1.15.0

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

# FFG energy
def feden(gam, kf, mc2):
    den = gam * kf**3 / ( 6 * nuda.cst.pi2 )
    e2v = []
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
            e2v.append( gam * term / (16.0 * nuda.cst.pi2 * nuda.cst.hbc**3 ) )
            e2a.append( e2v[-1] / den[ind] )
        else:
            e2v.append( 0.0 )
            e2a.append( 0.0 )
    e2v = np.array( e2v )
    e2a = np.array( e2a )
    return e2v, e2a

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
    pre = np.array( pre )
    return pre

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
    def __init__( self, den, delta ):
        """
        Parameters
        ----------
        den : float or numpy array of floats.
        Density or densities for which the FFG quantities are calculated.
        delta: float or numpy array of floats.
        Isospin density or densities for which the FFG quantities are calculated.

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
        # Attribute the neutron fraction
        self.x_n = nuda.cst.half * ( nuda.cst.one + self.delta )
        # Attribute the proton fraction
        self.x_p = nuda.cst.half * ( nuda.cst.one - self.delta )
        #: Attribute neutron density
        self.den_n = self.x_n * den
        #: Attribute proton density
        self.den_p = self.x_p * den
        #: Attribute Fermi momentum for a Fermi system with degeneracy = 4
        self.kf = (1.5 * nuda.cst.pi2 * self.den)**nuda.cst.third
        #: Attribute neutron Fermi momentum (degeneracy = 2)
        self.kf_n = (nuda.cst.three * nuda.cst.pi2 * self.den_n)**nuda.cst.third
        #: Attribute proton Fermi momentum (degeneracy = 2)
        self.kf_p = (nuda.cst.three * nuda.cst.pi2 * self.den_p)**nuda.cst.third
        #: Attribute neutron Fermi energy (degeneracy = 2)
        self.eF_n = np.sqrt( nuda.cst.mnc2**2 + (nuda.cst.hbc*self.kf_n)**2 )
        self.eF_n_int = np.sqrt( nuda.cst.mnc2**2 + (nuda.cst.hbc*self.kf_n)**2 ) - nuda.cst.mnc2
        self.eF_n_int_nr = nuda.cst.half * nuda.cst.h2m * self.kf_n**nuda.cst.two
        #: Attribute proton Fermi energy (degeneracy = 2)
        self.eF_p = np.sqrt( nuda.cst.mpc2**2 + (nuda.cst.hbc*self.kf_p)**2 )
        self.eF_p_int = np.sqrt( nuda.cst.mpc2**2 + (nuda.cst.hbc*self.kf_p)**2 ) - nuda.cst.mpc2
        self.eF_p_int_nr = nuda.cst.half * nuda.cst.h2m * self.kf_p**nuda.cst.two
        #: Attribute FFG energy per particle (degeneracy = 2)
        e2v_n, e2a_n = feden( 2.0, self.kf_n, nuda.cst.mnc2)
        e2v_p, e2a_p = feden( 2.0, self.kf_p, nuda.cst.mpc2)
        self.e2v = e2v_n + e2v_p
        self.e2a = self.x_n * e2a_n + self.x_p * e2a_p
        self.e2a_int = self.e2a - self.x_n * nuda.cst.mnc2 - self.x_p * nuda.cst.mpc2
        self.e2a_int_nr = nuda.cst.threeFifth * nuda.cst.half * nuda.cst.h2m * \
           (3*nuda.cst.pi2*nuda.cst.half*den)**nuda.cst.twoThird * \
           nuda.cst.half * \
           ( (nuda.cst.one+delta)**nuda.cst.fiveThird + \
             (nuda.cst.one-delta)**nuda.cst.fiveThird )
        #: Attribute FFG energy per unit volum (degeneracy = 2)
        self.e2v_int = self.e2a_int * self.den
        self.e2v_int_nr = self.e2a_int_nr * self.den
        #: Attribute FFG symmetry energy (degeneracy = 2)
        self.esym_nr = nuda.cst.threeFifth * nuda.cst.half * nuda.cst.h2m * \
           (3*nuda.cst.pi2*nuda.cst.half*den)**nuda.cst.twoThird * \
           ( nuda.cst.two**nuda.cst.twoThird - nuda.cst.one )
        #: Attribute FFG quadratic contribution to the symmetry energy
        self.esym2_nr = nuda.cst.threeFifth * nuda.cst.half * nuda.cst.h2m * \
           (3*nuda.cst.pi2*nuda.cst.half*den)**nuda.cst.twoThird * \
           10.0/18.0
        #: Attribute FFG quartic contribution to the symmetry energy
        self.esym4_nr = nuda.cst.threeFifth * nuda.cst.half * nuda.cst.h2m * \
           (3*nuda.cst.pi2*nuda.cst.half*den)**nuda.cst.twoThird * \
           5.0/243.0
        #: Attribute FFG pressure (degeneracy = 2)
        self.pre = fpres( 2.0, self.kf_n, nuda.cst.mnc2) + fpres( 2.0, self.kf_p, nuda.cst.mpc2) 
        self.pre_nr = nuda.cst.twoThird * self.e2v_int_nr
        #
        self.den_unit = 'fm$^{-3}$'
        self.kf_unit = 'fm$^{-1}$'
        self.e2a_unit = 'MeV'
        self.pre_unit = 'MeV fm$^{-3}$'
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
        if self.e2a_int is not None: print(f"   e2a: {np.round(self.e2a_int,2)} in {self.e2a_unit}")
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
    def __init__( self, den_e, den_mu ):
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
        self.den_e = den_e
        #: Attribute muon density
        self.den_mu = den_mu
        #: Attribute electron Fermi momentum (degeneracy = 2)
        self.kf_e = (nuda.cst.three * nuda.cst.pi2 * self.den_e)**nuda.cst.third
        #: Attribute muon Fermi momentum (degeneracy = 2)
        self.kf_mu = (nuda.cst.three * nuda.cst.pi2 * self.den_mu)**nuda.cst.third
        #: Attribute electon Fermi energy (degeneracy = 2)
        self.eF_e = np.sqrt( nuda.cst.mec2**2 + (nuda.cst.hbc*self.kf_e)**2 )
        #: Attribute muon Fermi energy (degeneracy = 2)
        self.eF_mu = np.sqrt( nuda.cst.mmuc2**2 + (nuda.cst.hbc*self.kf_mu)**2 )
        #: Attribute FFG energy per particle (degeneracy = 2)
        e2v_e = feden( 2.0, self.kf_e, nuda.cst.mec2)
        e2v_mu = feden( 2.0, self.kf_mu, nuda.cst.mmuc2)
        self.e2v = e2v_e + e2v_mu
        self.e2a = e2v_e / self.den_e + e2v_mu / self.den_mu
        self.e2a_int = self.e2a - (self.den_e*nuda.cst.mec2 + self.den_mu*nuda.cst.mmuc2)/(self.den_e+self.den_mu)
        #: Attribute FFG pressure (degeneracy = 2)
        self.pre = fpres( 2.0, self.kf_e, nuda.cst.mec2) + fpres( 2.0, self.kf_mu, nuda.cst.mmuc2) 
        #
        self.den_unit = 'fm$^{-3}$'
        self.kf_unit = 'fm$^{-1}$'
        self.e2a_unit = 'MeV'
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
        if self.den_e is not None: print(f"   den_e: {np.round(self.den_e,2)} in {self.den_unit}")
        if self.den_mu is not None: print(f"   den_mu: {np.round(self.den_mu,2)}")
        if self.kf_e is not None: print(f"   kf_e: {np.round(self.kf_e,2)} in {self.kf_unit}")
        if self.e2a is not None: print(f"   e2a: {np.round(self.e2a,2)} in {self.e2a_unit}")
        #
        if nuda.env.verb: print("Exit print_outputs()")
        #



