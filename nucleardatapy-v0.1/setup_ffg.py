import os
import sys
import numpy as np  # 1.15.0

import nucleardatapy as nuda

def kf_n( den_n ):
    """
    Neutron Fermi momentum as a function of the neutron density.

    :param den_n: neutron density.
    :type den_n: float or numpy vector of real numbers.
    """
    return (3*nuda.cst.pi2*den_n)**nuda.cst.third

def den_n( kf_n ):
    """
    Neutron density as a function of the neutron Fermi momentum.

    :param kf_n: neutron Fermi momentum.
    :type kf_n: float or numpy vector of real numbers.
    """
    return kf_n**nuda.cst.three / ( nuda.cst.three * nuda.cst.pi2 )

def epsF_n( kf_n ):
    """
    Neutron Fermi energy as a function of the neutron Fermi momentum.

    :param kf_n: neutron Fermi momentum.
    :type kf_n: float or numpy vector of real numbers.
    """
    return nuda.cst.half * nuda.cst.h2m * kf_n**2

def effg( kf_n ):
    """
    Free Fermi gas energy as a function of the neutron Fermi momentum.

    :param kf_n: neutron Fermi momentum.
    :type kf_n: float or numpy vector of real numbers.
    """
    return nuda.cst.threeFifth * nuda.cst.half * nuda.cst.h2m * kf_n**2

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
        #: Attribute isoscalar density
        self.den = den 
        #: Attribute isospin parameter
        self.delta = delta 
        #: Attribute neutron density
        self.den_n = 0.5 * ( 1.0 - delta ) * den
        #: Attribute proton density
        self.den_p = 0.5 * ( 1.0 + delta ) * den
        #: Attribute neutron Fermi momentum
        self.kf_n = (3*nuda.cst.pi2*self.den_n)**nuda.cst.third
        #: Attribute proton Fermi momentum
        self.kf_p = (3*nuda.cst.pi2*self.den_p)**nuda.cst.third
        #: Attribute neutron Fermi energy
        self.epsF_n = nuda.cst.half * nuda.cst.h2m * self.kf_n**2
        #: Attribute proton Fermi energy
        self.epsF_p = nuda.cst.half * nuda.cst.h2m * self.kf_p**2
        #: Attribute FFG energy per particle
        self.e2a = nuda.cst.threeFifth * nuda.cst.half * nuda.cst.h2m * \
           (3*nuda.cst.pi2*nuda.cst.half*den)**nuda.cst.twoThird * \
           nuda.cst.half * \
           ( (1.0+delta)**nuda.cst.fiveThird + (1.0-delta)**nuda.cst.fiveThird )

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
        if any(self.den): print(f"   den: {np.round(self.den,2)} in {self.den_unit}")
        if any(self.delta): print(f"   delta: {np.round(self.delta,2)}")
        if any(self.kf_n): print(f"   kf_n: {np.round(self.kf_n,2)} in {self.kf_unit}")
        if any(self.e2a): print(f"   e2a: {np.round(self.e2a,2)} in {self.e2a_unit}")
        #
        if nuda.env.verb: print("Exit print_outputs()")
        #

