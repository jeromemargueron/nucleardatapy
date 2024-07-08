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
    ones: 'Negele-Vautheron-1971'.

    :return: The list of tables.
    :rtype: list[str].
    """
    #
    if nuda.env.verb: print("\nEnter models_crust()")
    #
    modcrusts = [ 'Negele-Vautherin-1971' ]
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

    `crust` can chosen among the following ones: 'Negele-Vautherin-1971'.

    :param crust: Fix the name of `crust`. Default value: 'Negele-Vautherin-1971'.
    :type crust: str, optional. 

    **Attributes:**
    """
    def __init__(self, modcrust = 'Negele-Vautherin-1971'):
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
        self.den = None
        #: Attribute A (mass of the nucleus).
        self.A = None
        #: Attribute Z (charge of the nucleus).
        self.Z = None
        #: Attribute N (number of neutrons of the nucleus).
        self.N = None
        #: Attribute Ngas (number of neutrons in the gas).
        self.Ngas = None
        #: Attribute BE (Binding Energy) of the nucleus.
        self.BE = None
        #: Attribute uncertainty in the BE (Binding Energy) of the nucleus.
        self.BE_err = None
        #
        if modcrust.lower()=='negele-vautherin-1971':
            #
            file_in = nuda.param.path_data+'crust/Negele-Vautherin.dat'
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'Negele and Vautherin, Phys. Rev. C (1971)'
            self.note = "write here notes about this EOS."
            self.label = 'NV-1971'
            self.linestyle = 'solid'
            self.den, self.N, self.Z, self.mu_n, self.mu_p, self.rho_g, self.x, self.e2a_tot, \
                self.e2a_g = np.loadtxt( file_in, usecols=(0,1,2,3,4,5,6,7,8), unpack = True )
            self.A = self.N + self.Z


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
       if self.Z is not None: print(f"   Z: {self.Z}")
       if self.N is not None: print(f"   N: {self.N}")
       if self.A is not None: print(f"   A: {self.A}")
       if self.mu_n is not None: print(f"   mu_n(MeV): {self.mu_n}")
       if self.mu_p is not None: print(f"   mu_p(MeV): {self.mu_p}")
       if self.rho_g is not None: print(f"   rho_g(fm-3): {self.rho_g}")
       if self.x is not None: print(f"   x: {self.x}")
       if self.e2a_tot is not None: print(f"   e2a_tot(MeV): {self.e2a_tot}")
       if self.e2a_g is not None: print(f"   e2a_g(MeV): {self.e2a_g}")
       #
       if nuda.env.verb: print("Exit print_outputs()")
       #
