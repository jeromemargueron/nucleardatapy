import os
import sys
import math
import numpy as np  # 1.15.0

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda


def eos_hic_constraints():
    """
    Return a list of the HIC constraints available in this toolkit 
    for the equation of state in SM and NM and print them all on 
    the prompt. These constraints are the following
    ones: [ 'DLL-2002', 'FOPI-2016' ].

    :return: The list of constraints.
    :rtype: list[str].
    """
    #
    if nuda.env.verb: print("\nEnter eos_hic_constraints()")
    #
    constraints = [ 'DLL-2002', 'FOPI-2016' ]
    #
    print('HIC constraints available in the toolkit:',constraints)
    constraints_lower = [ item.lower() for item in constraints ]
    if nuda.env.verb: print('HIC constraints available in the toolkit:',constraints_lower)
    #
    if nuda.env.verb: print("Exit constraints_HIC_matter()")
    #
    return constraints, constraints_lower


class SetupEOSHIC():
    """
    Instantiate the constraints on the EOS from HIC.

    This choice is defined in the variable `constraint`.

    `constraint` can chosen among the following ones: [ 'DLL-2002', 'FOPI-2016' ].

    :param constraint: Fix the name of `constraint`. Default value: 'DLL-2002'.
    :type constraint: str, optional. 

    **Attributes:**
    """
    def __init__(self, constraint = 'DLL-2002'):
        #
        if nuda.env.verb: print("Enter SetupEOSHIC()")
        #
        self.constraint = constraint
        if nuda.env.verb: print("constraint:",constraint)
        #
        self = SetupEOSHIC.init_self( self )
        #
        constraints, constraints_lower = eos_hic_constraints()
        if constraint.lower() not in constraints_lower:
            print('The constraint ',constraint,' is not in the list of EOS HIC constraints.')
            print('list of EOS HIC constraints:',constraints)
            print('-- Exit the code --')
            exit()
        #
        #
        if constraint.lower()=='dll-2002':
            #
            file_in1 = nuda.param.path_data+'matter/hic/2002-DLL-SM.dat'
            file_in2 = nuda.param.path_data+'matter/hic/2002-DLL-NM-soft.dat'
            file_in3 = nuda.param.path_data+'matter/hic/2002-DLL-NM-stiff.dat'
            if nuda.env.verb: print('Reads file:',file_in1)
            if nuda.env.verb: print('Reads file:',file_in2)
            if nuda.env.verb: print('Reads file:',file_in3)
            self.ref = 'P. Danielewicz, R. Lacey, and W. Lynch, Science, 298, 1592 (2002).'
            self.note = "write here notes about this constraint."
            self.label = 'DLL-2002'
            den2densat, self.sm_pre_up, self.sm_pre_lo = np.loadtxt( file_in1, usecols=(0,1,2), unpack = True )
            den2densat, self.nm_pre_so_up, self.nm_pre_so_lo = np.loadtxt( file_in2, usecols=(0,1,2), unpack = True )
            den2densat, self.nm_pre_st_up, self.nm_pre_st_lo = np.loadtxt( file_in3, usecols=(0,1,2), unpack = True )
            self.den = den2densat * nuda.cst.nsat # in fm-3
            self.sm_pre = nuda.cst.half * ( self.sm_pre_up + self.sm_pre_lo )
            self.sm_pre_err = nuda.cst.half * ( self.sm_pre_up - self.sm_pre_lo )
            self.nm_pre_so = nuda.cst.half * ( self.nm_pre_so_up + self.nm_pre_so_lo )
            self.nm_pre_so_err = nuda.cst.half * ( self.nm_pre_so_up - self.nm_pre_so_lo )
            # decide that the NM pressure should be the asy-soft one by default
            self.nm_pre = self.nm_pre_so
            self.nm_pre_err = self.nm_pre_so_err
            self.nm_pre_up = self.nm_pre_so_up
            self.nm_pre_lo = self.nm_pre_so_lo
            #
        elif constraint.lower()=='fopi-2016':
            #
            file_in = nuda.param.path_data+'matter/hic/2016-FOPI.dat'
            #if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'A. Le Fevre, Y. Leifels, W. Reisdorf, J. Aichelin, and C. Hartnack, Nuclear Physics A 945, 112 (2016).'
            self.note = "write here notes about this constraint."
            self.label = 'FOPI-2016'
            den2densat, self.sm_e2a, self.sm_e2a_err = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.den = den2densat * nuda.cst.nsat # in fm-3
            self.sm_e2a_up = self.sm_e2a + self.sm_e2a_err
            self.sm_e2a_lo = self.sm_e2a - self.sm_e2a_err
            #
            # pressure?

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
       print("   constraint:",self.constraint)
       print("   ref:     ",self.ref)
       print("   label:   ",self.label)
       print("   note:    ",self.note)
       if self.den is not None: print(f"   den: {self.den} in {self.den_unit}.")
       if self.sm_pre is not None: print(f"   sm_pre: {self.sm_pre} in {self.pre_unit}.")
       if self.sm_pre_err is not None: print(f"   sm_pre_err: {self.sm_pre_err} in {self.pre_unit}.")
       if self.nm_pre is not None: print(f"   nm_pre: {self.nm_pre} in {self.pre_unit}.")
       if self.nm_pre_err is not None: print(f"   nm_pre_err: {self.nm_pre_err} in {self.pre_unit}.")
       #
       if nuda.env.verb: print("Exit print_outputs()")
       #
    def init_self( self ):
        """
        Initialize variables in self.
        """
        print("")
        #
        if nuda.env.verb: print("Enter init_self()")
        #
        #: Attribute providing the full reference to the paper to be citted.
        self.ref = ''
        #: Attribute providing additional notes about the data.
        self.note = ''
        #: Attribute the density of the system (in fm^-3).
        self.den = None
        #: Attribute the upper limit of the energy per particle in SM (in MeV fm-3).
        self.sm_e2a_up = None
        #: Attribute the lower limit of the energy per particle in SM (in MeV fm-3).
        self.sm_e2a_lo = None
        #: Attribute the energy per particle in SM (in MeV fm-3).
        self.sm_e2a = None
        #: Attribute the uncertainty in the energy per particle in SM (in MeV fm-3).
        self.sm_e2a_err = None
        #: Attribute the upper limit of the pressure in SM (in MeV fm-3).
        self.sm_pre_up = None
        #: Attribute the lower limit of the pressure in SM (in MeV fm-3).
        self.sm_pre_lo = None
        #: Attribute the upper limit of the pressure in NM (in MeV fm-3).
        self.nm_pre_up = None
        #: Attribute the lower limit of the pressure in NM (in MeV fm-3).
        self.nm_pre_lo = None
        #: Attribute the centroid of the pressure in SM (in MeV fm-3).
        self.sm_pre = None
        #: Attribute the uncertainty of the pressure in SM (in MeV fm-3).
        self.sm_pre_err = None
        #: Attribute the centroid of the pressure in NM (in MeV fm-3).
        self.nm_pre = None
        #: Attribute the uncertainty of the pressure in NM (in MeV fm-3).
        self.nm_pre_err = None
        #: Attribute the upper limit of the pressure in NM for azy-soft EOS (in MeV fm-3).
        self.nm_pre_so_up = None
        #: Attribute the lower limit of the pressure in NM for azy-soft EOS (in MeV fm-3).
        self.nm_pre_so_lo = None
        #: Attribute the upper limit of the pressure in NM for azy-stiff EOS (in MeV fm-3).
        self.nm_pre_st_up = None
        #: Attribute the lower limit of the pressure in NM for azy-stiff EOS (in MeV fm-3).
        self.nm_pre_st_lo = None
        #: Attribute the centroid of the pressure in NM for azy-soft EOS (in MeV fm-3).
        self.nm_pre_so = None
        #: Attribute the uncertainty of the pressure in NM for azy-soft EOS (in MeV fm-3).
        self.nm_pre_so_err = None
        #: Attribute the centroid of the pressure in NM for azy-stiff EOS (in MeV fm-3).
        self.nm_pre_st = None
        #: Attribute the uncertainty of the pressure in NM for azy-stiff EOS (in MeV fm-3).
        self.nm_pre_st_err = None
        #: Attribute the plot linestyle.
        self.linestyle = 'solid'
        #: Attribute plot label.
        self.label = ''
        #: Attribute plot alpha.
        self.alpha = 0.5
        #
        self.den_unit = 'fm$^{-3}$'
        self.kf_unit = 'fm$^{-1}$'
        self.e2a_unit = 'MeV'
        self.e2v_unit = 'MeV fm$^{-3}$'
        self.pre_unit = 'MeV fm$^{-3}$'
        self.gap_unit = 'MeV'        #
        if nuda.env.verb: print("Exit init_self()")
        #
        return self         
