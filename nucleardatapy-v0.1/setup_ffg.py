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
    return nuda.cst.half * nuda.cst.h2m * kf_n**2

def effg_NM( kf_n ):
    """
    Free Fermi gas energy as a function of the neutron Fermi momentum.

    :param kf_n: neutron Fermi momentum.
    :type kf_n: float or numpy vector of real numbers.
    """
    return nuda.cst.threeFifth * nuda.cst.half * nuda.cst.h2m * kf_n**2

def effg_SM( kf ):
    """
    Free Fermi gas energy as a function of the Fermi momentum in SM.

    :param kf: neutron Fermi momentum.
    :type kf: float or numpy vector of real numbers.
    """
    return nuda.cst.threeFifth * nuda.cst.half * nuda.cst.h2m * kf**2

def effg( kf ):
    """
    Free Fermi gas energy as a function of the Fermi momentum.

    :param kf: Fermi momentum.
    :type kf: float or numpy vector of real numbers.
    """
    return nuda.cst.threeFifth * nuda.cst.half * nuda.cst.h2m * kf**2

def esymffg( kf ):
    """
    Free Fermi gas symmetry energy as a function of the Fermi momentum.

    :param kf: Fermi momentum.
    :type kf: float or numpy vector of real numbers.
    """
    return effg( kf ) * ( nuda.cst.two**nuda.cst.twoThird - 1.0 )

class SetupFFG():
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
        if nuda.env.verb: print("Enter SetupFFG()")
        #
        #: Attribute providing the label the data is references for figures.
        self.label = r'FFG $\,\delta=$'+str(delta[0])
        #: Attribute providing additional notes about the data.
        self.note = ""
        #: Attribute isoscalar density
        self.den = den 
        #: Attribute isospin parameter
        self.delta = delta 
        #: Attribute neutron density
        self.den_n = nuda.cst.half * ( nuda.cst.one + delta ) * den
        #: Attribute proton density
        self.den_p = nuda.cst.half * ( nuda.cst.one - delta ) * den
        #: Attribute Fermi momentum
        self.kf = (1.5 * nuda.cst.pi2 * self.den)**nuda.cst.third
        #: Attribute neutron Fermi momentum
        self.kf_n = (nuda.cst.three * nuda.cst.pi2 * self.den_n)**nuda.cst.third
        #: Attribute proton Fermi momentum
        self.kf_p = (nuda.cst.three * nuda.cst.pi2 * self.den_p)**nuda.cst.third
        #: Attribute neutron Fermi energy
        self.eF_n = nuda.cst.half * nuda.cst.h2m * self.kf_n**nuda.cst.two
        #: Attribute proton Fermi energy
        self.eF_p = nuda.cst.half * nuda.cst.h2m * self.kf_p**nuda.cst.two
        #: Attribute FFG energy per particle
        self.e2a_int = nuda.cst.threeFifth * nuda.cst.half * nuda.cst.h2m * \
           (3*nuda.cst.pi2*nuda.cst.half*den)**nuda.cst.twoThird * \
           nuda.cst.half * \
           ( (nuda.cst.one+delta)**nuda.cst.fiveThird + \
             (nuda.cst.one-delta)**nuda.cst.fiveThird )
        #: Attribute FFG energy per unit volum
        self.e2v_int = self.e2a_int * self.den
        #: Attribute FFG symmetry energy
        self.esym = nuda.cst.threeFifth * nuda.cst.half * nuda.cst.h2m * \
           (3*nuda.cst.pi2*nuda.cst.half*den)**nuda.cst.twoThird * \
           ( nuda.cst.two**nuda.cst.twoThird - nuda.cst.one )
        #: Attribute FFG quadratic contribution to the symmetry energy
        self.esym2 = nuda.cst.threeFifth * nuda.cst.half * nuda.cst.h2m * \
           (3*nuda.cst.pi2*nuda.cst.half*den)**nuda.cst.twoThird * \
           10.0/18.0
        #: Attribute FFG quartic contribution to the symmetry energy
        self.esym4 = nuda.cst.threeFifth * nuda.cst.half * nuda.cst.h2m * \
           (3*nuda.cst.pi2*nuda.cst.half*den)**nuda.cst.twoThird * \
           5.0/243.0
        #: Attribute FFG pressure
        self.pre = nuda.cst.twoThird * self.e2v_int
        #
        self.den_unit = 'fm$^{-3}$'
        self.kf_unit = 'fm$^{-1}$'
        self.e2a_unit = 'MeV'
        self.pre_unit = 'MeV fm$^{-3}$'
        #
        if nuda.env.verb: print("Exit SetupFFG()")
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

