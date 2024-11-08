import os
import sys
import math
import numpy as np  # 1.15.0

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda


def models_crust():
    """
    Return a list of the tables available in this toolkit for the experimental masses and
    print them all on the prompt. These tables are the following
    ones: 'Negele-Vautheron-1973'.

    :return: The list of tables.
    :rtype: list[str].
    """
    #
    if nuda.env.verb: print("\nEnter models_crust()")
    #
    modcrusts = [ '1973-Negele-Vautherin', '2020-MVCD-D1S', '2020-MVCD-D1M', '2020-MVCD-D1MS' ]
    #
    print('crust models available in the toolkit:',modcrusts)
    modcrusts_lower = [ item.lower() for item in modcrusts ]
    print('crust models available in the toolkit:',modcrusts_lower)
    #
    if nuda.env.verb: print("Exit models_crust()")
    #
    return modcrusts, modcrusts_lower


class SetupCrust():
    """
    Instantiate the properties of the crust for the existing models.

    This choice is defined in the variable `crust`.

    `crust` can chosen among the following ones: 'Negele-Vautherin-1973'.

    :param crust: Fix the name of `crust`. Default value: 'Negele-Vautherin-1973'.
    :type crust: str, optional. 

    **Attributes:**
    """
    def __init__(self, modcrust = '1973-Negele-Vautherin'):
        #
        if nuda.env.verb: print("Enter SetupCrusts()")
        #
        modcrusts, modcrusts_lower = models_crust()
        if modcrust.lower() not in modcrusts_lower:
            print('Crust model ',modcrust,' is not in the list of crusts.')
            print('list of crust models:',modcrusts)
            print('-- Exit the code --')
            exit()
        self.modcrust = modcrust
        if nuda.env.verb: print("modcrust:",modcrust)
        #
        #: Attribute the density of the system (in cm^-3).
        self.den_cgs = None
        #: Attribute the density of the system (in fm^-3).
        self.den = None
        #: Attribute A (mass of the nucleus).
        self.A = None
        #: Attribute Z (charge of the nucleus).
        self.Z = None
        #: Attribute N (total number of neutrons of the WS cell).
        self.N = None
        #: Attribute N_bound (number of bound neutrons).
        self.N_bound = None
        #: Attribute N_g (number of neutrons in the gas).
        self.N_g = None
        #: Attribute the fraction of neutrons.
        self.xn = None
        #: Attribute the fraction of bound neutrons.
        self.xn_bound = None
        #: Attribute the fraction of protons.
        self.xp = None
        #: Attribute the approximate ratio of proton to neutron in the nucleus.
        self.xpn_bound = None
        #: Attribute the neutron chemical potential (in MeV).
        self.mu_n = None
        #: Attribute the proton chemical potential (in MeV).
        self.mu_p = None
        #: Attribute the approximate density of neutron in the gas (in fm-3).
        self.den_g = None
        #: Attribute the radius of the WS cell (in fm).
        self.RWS = None
        #: Attribute the rest mass energy (in MeV).
        self.e2a_rm = None
        #: Attribute the energy minus the neutron mass (in MeV).
        self.e2a_int2 = None
        #: Attribute the internal energy (in MeV).
        self.e2a_int = None
        #: Attribute the internal energy of the gas component (in MeV).
        self.e2a_int_g = None
        #
        if modcrust.lower()=='1973-negele-vautherin':
            #
            file_in = nuda.param.path_data+'crust/1973-Negele-Vautherin.dat'
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'Negele and Vautherin, Nuc. Phys. A 207, 298 (1973).'
            self.note = "write here notes about this EOS."
            self.label = 'NV-1973'
            self.linestyle = 'solid'
            self.den_cgs, self.N, self.Z, self.mu_n, self.mu_p, self.den_g, self.xpn_bound, self.e2a_int2, \
                self.e2a_int_g = np.loadtxt( file_in, usecols=(0,1,2,3,4,5,6,7,8), unpack = True )
            self.den = self.den_cgs * 1.e-39 # in fm-3
            self.N = np.array([ int(item) for item in self.N ])
            self.Z = np.array([ int(item) for item in self.Z ])
            self.A = self.N + self.Z
            self.N_bound = [ int(item) for item in self.Z * self.xpn_bound ]
            self.xn = self.N / self.A
            self.xn_bound = self.N_bound / self.A
            self.N_g = self.N - self.N_bound
            self.xp = self.Z / self.A
            self.RWS = ( nuda.cst.three * self.N_g / (nuda.cst.four * nuda.cst.pi * self.den_g) )**nuda.cst.third
            self.e2a_tot = self.e2a_int2 + nuda.cst.mnuc2
            self.e2a_rm = self.xn * nuda.cst.mnc2 + self.xp * ( nuda.cst.mpc2 + nuda.cst.mec2 )
            self.e2a_int = self.e2a_tot - self.e2a_rm
            #
        elif '2020-mvcd' in modcrust.lower():
            #
            # Note: N_bound or N_g cannot be determined from the tables (Jerome).
            # It is right?
            #
            if modcrust.lower()=='2020-mvcd-d1s':
                file_in = nuda.param.path_data+'crust/2020-MVCD-D1S.dat'
                self.label = 'MVCD-D1S-2020'
            elif modcrust.lower()=='2020-mvcd-d1m':
                file_in = nuda.param.path_data+'crust/2020-MVCD-D1M.dat'
                self.label = 'MVCD-D1M-2020'
            elif modcrust.lower()=='2020-mvcd-d1ms':
                file_in = nuda.param.path_data+'crust/2020-MVCD-D1MS.dat'
                self.label = 'MVCD-D1M$^*$-2020'
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'C. Mondal, X. Viñas, M. Centelles, and J.N. De, Phys. Rev. C 102, 015802 (2020).'
            self.note = "semiclassical variational Wigner-Kirkwood method along with shell and pairing corrections calculated with the Strutinsky integral method and the BCS approximation."
            self.linestyle = 'solid'
            self.den, self.RWS, self.N, self.Z, self.e2a_int2, self.pre, self.mu_n, self.mu_p, self.mu_e \
                = np.loadtxt( file_in, usecols=(0,1,2,3,4,5,6,7,8), unpack = True )
            self.den_cgs = self.den / 1.e-39 # in cm-3
            self.N = np.array([ int(item) for item in self.N ])
            self.Z = np.array([ int(item) for item in self.Z ])
            self.A = self.N + self.Z
            #self.N_bound = [ int(item) for item in self.Z * self.xpn_bound ]
            self.xn = self.N / self.A
            #self.xn_bound = self.N_bound / self.A
            #self.N_g = self.N - self.N_bound
            self.xp = self.Z / self.A
            self.e2a_tot = self.e2a_int2 + nuda.cst.mnuc2_approx
            self.e2a_rm = self.xn * nuda.cst.mnc2 + self.xp * ( nuda.cst.mpc2 + nuda.cst.mec2 )
            self.e2a_int = self.e2a_tot - self.e2a_rm
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
       print("   modcrust:",self.modcrust)
       print("   ref:     ",self.ref)
       print("   label:   ",self.label)
       print("   note:    ",self.note)
       if self.den is not None: print(f"   den: {self.den}")
       if self.A is not None: print(f"   A: {self.A}")
       if self.Z is not None: print(f"   Z: {self.Z}")
       if self.N is not None: print(f"   N: {self.N}")
       if self.N_bound is not None: print(f"   N_bound: {self.N_bound}")
       if self.N_g is not None: print(f"   N_g: {self.N_g}")
       if self.mu_n is not None: print(f"   mu_n(MeV): {self.mu_n}")
       if self.mu_p is not None: print(f"   mu_p(MeV): {self.mu_p}")
       if self.den_g is not None: print(f"   den_g(fm-3): {self.den_g}")
       if self.RWS is not None: print(f"   RWS(fm): {np.round(self.RWS,3)}")
       if self.xpn_bound is not None: print(f"   xpn_bound: {self.xpn_bound}")
       if self.e2a_tot is not None: print(f"   e2a_tot(MeV): {np.round(self.e2a_tot,3)}")
       if self.e2a_rm is not None: print(f"   e2a_rm(MeV): {np.round(self.e2a_rm,3)}")
       if self.e2a_int2 is not None: print(f"   e2a_int2(MeV): {np.round(self.e2a_int2,3)}")
       if self.e2a_int is not None: print(f"   e2a_int(MeV): {np.round(self.e2a_int,3)}")
       if self.e2a_int_g is not None: print(f"   e2a_int_g(MeV): {np.round(self.e2a_int_g,3)}")
       #
       if nuda.env.verb: print("Exit print_outputs()")
       #
