import os
import sys
import math
import numpy as np  # 1.15.0

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda


def hic_constraints():
    """
    Return a list of the HIC constraints available in this toolkit 
    for the equation of state in SM and NM and print them all on 
    the prompt. These constraints are the following
    ones: [ '2002-DLL', '2002-KAON', '2016-FOPI', '2011-FOPI-LAND', '2016-ASY-EOS'
    , '2021-SPIRIT','2019-NP-RATIO','2009-ISO-DIFF' ].

    :return: The list of constraints.
    :rtype: list[str].
    """
    #
    if nuda.env.verb: print("\nEnter hic_constraints()")
    #
    constraints = [ '2002-DLL', '2002-KAON', '2016-FOPI', '2009-ISO-DIFF' ,'2011-FOPI-LAND'
                   , '2016-ASY-EOS','2019-NP-RATIO', '2021-SPIRIT']
    #
    constraints_lower = [ item.lower() for item in constraints ]
    if nuda.env.verb: print('HIC constraints available in the toolkit:',constraints_lower)
    #
    if nuda.env.verb: print("Exit hic_constraints()")
    #
    return constraints, constraints_lower


class setupHIC():
    """
    Instantiate the constraints on the EOS from HIC.

    This choice is defined in the variable `constraint`.

    `constraint` can chosen among the following ones: 
    [ '2002-DLL', '2016-FOPI', '2002-KAON','2009-ISO-DIFF', '2011-FOPI_LAND'
    , '2016-ASY_EOS','2019-NP-RATIO', '2021-SPIRIT' ].

    :param constraint: Default value: '2002-DLL'.
    :type constraint: str, optional. 

    **Attributes:**
    """
    def __init__(self, constraint = '2002-DLL'):
        #
        if nuda.env.verb: print("Enter setupHIC()")
        #
        self.constraint = constraint
        
        if nuda.env.verb: print("constraint:",constraint)
        #
        self = setupHIC.init_self( self )
        #
        constraints, constraints_lower = hic_constraints()
        if constraint.lower() not in constraints_lower:
            print('The constraint ',constraint,' is not in the list of EOS HIC constraints.')
            print('list of EOS HIC constraints:',constraints)
            print('-- Exit the code --')
            exit()
        #
        #
        if constraint.lower()=='2002-dll':
            #
            file_in1 = nuda.param.path_data+'matter/hic/2002-DLL-SM.dat'
            file_in2 = nuda.param.path_data+'matter/hic/2002-DLL-NM-soft.dat'
            file_in3 = nuda.param.path_data+'matter/hic/2002-DLL-NM-stiff.dat'
            if nuda.env.verb: print('Reads file:',file_in1)
            if nuda.env.verb: print('Reads file:',file_in2)
            if nuda.env.verb: print('Reads file:',file_in3)
            self.ref = 'P. Danielewicz, R. Lacey, and W. Lynch, Science, 298, 1592 (2002).'
            self.note = "Flow data used to contraint EOS of symmetric matter"
            self.label = 'DLL-2002'
            self.label_so = 'DLL-2002-Asy_soft'
            self.label_st = 'DLL-2002-Asy_stiff'
            self.color= 'blue'
            den2densat, self.sm_pre, self.sm_pre_err = np.loadtxt( file_in1, usecols=(0,1,2), unpack = True )
            den2densat, self.nm_pre_so, self.nm_pre_so_err = np.loadtxt( file_in2, usecols=(0,1,2), unpack = True )
            den2densat, self.nm_pre_st, self.nm_pre_st_err = np.loadtxt( file_in3, usecols=(0,1,2), unpack = True )
            self.den = den2densat * nuda.cst.nsat # in fm-3
            self.sm_pre_up = self.sm_pre + self.sm_pre_err
            self.sm_pre_lo = self.sm_pre - self.sm_pre_err
            #self.sm_pre = nuda.cst.half * ( self.sm_pre_up + self.sm_pre_lo )
            #self.sm_pre_err = nuda.cst.half * ( self.sm_pre_up - self.sm_pre_lo )
            #self.nm_pre_so = nuda.cst.half * ( self.nm_pre_so_up + self.nm_pre_so_lo )
            #self.nm_pre_so_err = nuda.cst.half * ( self.nm_pre_so_up - self.nm_pre_so_lo )
            # decide that the NM pressure should be the asy-soft one by default
            self.nm_pre = self.nm_pre_so
            self.nm_pre_err = self.nm_pre_so_err
            self.nm_pre_up = self.nm_pre_so + self.nm_pre_so_err
            self.nm_pre_lo = self.nm_pre_so - self.nm_pre_so_err

            self.nm_pre_st_up = self.nm_pre_st + self.nm_pre_st_err
            self.nm_pre_st_lo = self.nm_pre_st - self.nm_pre_st_err
            #
        elif constraint.lower()=='2002-kaon':
            file_in = nuda.param.path_data+'matter/hic/2002-KAON.dat'
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'C. Fuchs, PPNP 56,1 (2006); W. Lynch et al., PPNP 62, 427 (2009).'
            self.note = "Kaon yield ratios studied to contraint symmetric EOS."
            self.label = 'KAON-2002'
            self.color = 'cyan'
            den2densat, self.sm_pre_lo, self.sm_pre_up = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.den = den2densat * nuda.cst.nsat # in fm-3
            self.sm_pre = nuda.cst.half * ( self.sm_pre_up + self.sm_pre_lo )
            self.sm_pre_err = nuda.cst.half * ( self.sm_pre_up - self.sm_pre_lo )
            

        elif constraint.lower()=='2016-fopi':
            #
            file_in1 = nuda.param.path_data+'matter/hic/2016-FOPI-E2A.dat'
            file_in2 = nuda.param.path_data+'matter/hic/2016-FOPI-SM.dat'
            #if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'A. Le Fevre, Y. Leifels, W. Reisdorf, J. Aichelin, and C. Hartnack, Nuclear Physics A 945, 112 (2016).'
            self.note = "Elliptical flow data is used to constraint symmetric matter EOS"
            self.label = 'FOPI-2016'
            self.color = 'magenta'
            den2densat_e2a, self.sm_e2a, self.sm_e2a_err = np.loadtxt( file_in1, usecols=(0,1,2), unpack = True )
            den2densat, self.sm_pre_lo, self.sm_pre_up = np.loadtxt( file_in2, usecols=(0,1,2), unpack = True )
            self.den_e2a = den2densat_e2a * nuda.cst.nsat # in fm-3
            self.den = den2densat * nuda.cst.nsat # in fm-3
            self.sm_e2a_up = self.sm_e2a + self.sm_e2a_err
            self.sm_e2a_lo = self.sm_e2a - self.sm_e2a_err
            self.sm_pre = nuda.cst.half * ( self.sm_pre_up + self.sm_pre_lo )
            self.sm_pre_err = nuda.cst.half * ( self.sm_pre_up - self.sm_pre_lo )
            #
        elif constraint.lower()=='2009-iso-diff':
            file_in = nuda.param.path_data+'matter/hic/2009-iso-diff.dat'
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'M. B. Tsang et al., Phys. Rev. Lett. 102, 122701 (2009); W. Lynch, M. B. Tsang, Phys. Lett. B 830, 137098 (2022).'
            self.note = "Isospin diffusion data studied to constraint symmetry energy at sub-saturation."
            self.label = 'Iso Diff-2009'
            self.color = 'k'
            den2densat, den2densat_err, self.sym_enr_isodiff, self.sym_enr_isodiff_err = np.loadtxt( file_in, usecols=(0,1,2,3), unpack = True )
            self.den_isodiff = den2densat * nuda.cst.nsat # in fm-3
            self.den_isodiff_err = den2densat_err * nuda.cst.nsat # in fm-3
            #
        elif constraint.lower()=='2011-fopi-land':
            file_in = nuda.param.path_data+'matter/hic/2011-FOPI-LAND.dat'
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = ' P. Russotto et al., Physics Letters B 697, 471 (2011).'
            self.note = "Sura-saturation information on symmtery energy usinf n/p elliptical flows"
            self.label = 'FOPI-LAND-2011'
            self.color = 'yellow'
            den2densat, self.sym_enr_lo, self.sym_enr_up = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.den = den2densat * nuda.cst.nsat # in fm-3
            self.sym_enr = nuda.cst.half * ( self.sym_enr_up + self.sym_enr_lo )
            self.sym_enr_err = nuda.cst.half * ( self.sym_enr_up - self.sym_enr_lo )
            
        elif constraint.lower()=='2016-asy-eos':
            file_in = nuda.param.path_data+'matter/hic/2016-ASY-EOS.dat'
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'P. Russotto et al., Phys. Rev. C 94, 034608 (2016).'
            self.note = "Sura-saturation information on symmtery energy usinf n/p elliptical flows."
            self.label = 'ASY-EOS-2016'
            self.color = 'red'
            den2densat, self.sym_enr_lo, self.sym_enr_up = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.den = den2densat * nuda.cst.nsat # in fm-3
            self.sym_enr = nuda.cst.half * ( self.sym_enr_up + self.sym_enr_lo )
            self.sym_enr_err = nuda.cst.half * ( self.sym_enr_up - self.sym_enr_lo )
        #   
        elif constraint.lower()=='2019-np-ratio':
            file_in = nuda.param.path_data+'matter/hic/2019-n2p-ratio.dat'
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'P. Morfouace et al., Phys. Lett. B 799, 135045 (2019).'
            self.note = "n/p spectral ratios to constraint symmetry energy at sub-saturation densities"
            self.label = 'n/p ratio-2019'
            self.color = 'green'
            den2densat, den2densat_err, self.sym_enr_np, self.sym_enr_np_err = np.loadtxt( file_in, usecols=(0,1,2,3), unpack = True )
            self.den_np = den2densat * nuda.cst.nsat # in fm-3
            self.den_np_err = den2densat_err * nuda.cst.nsat # in fm-3
        #    
        elif constraint.lower()=='2021-spirit':
            file_in = nuda.param.path_data+'matter/hic/2021-SPIRIT.dat'
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'J. Estee et al., Phys. Rev. Lett. 126, 162701 (2021).'
            self.note = "Pion double ratios is studied in neutron rich and poor colliding nuclei."
            self.label = 'SPIRIT-2021'
            self.color = 'blue'
            den2densat, den2densat_err, self.sym_enr_spirit, self.sym_enr_spirit_err, self.sym_pre_spirit, self.sym_pre_spirit_err = np.loadtxt( file_in, usecols=(0,1,2,3,4,5), unpack = True )
            self.den_spirit = den2densat * nuda.cst.nsat # in fm-3
            self.den_spirit_err = den2densat_err * nuda.cst.nsat # in fm-3
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
       if self.den_isodiff is not None: print(f"   den: {self.den_isodiff} in {self.den_unit}.")
       if self.den_np is not None: print(f"   den: {self.den_np} in {self.den_unit}.")
       if self.den_spirit is not None: print(f"   den: {self.den_spirit} in {self.den_unit}.")
       if self.sm_pre is not None: print(f"   sm_pre: {self.sm_pre} in {self.pre_unit}.")
       if self.sm_pre_err is not None: print(f"   sm_pre_err: {self.sm_pre_err} in {self.pre_unit}.")
       if self.nm_pre is not None: print(f"   nm_pre: {self.nm_pre} in {self.pre_unit}.")
       if self.nm_pre_err is not None: print(f"   nm_pre_err: {self.nm_pre_err} in {self.pre_unit}.")
       if self.sym_enr is not None: print(f"   nm_pre_err: {self.sym_enr} in {self.e2a_unit}.")
       if self.sym_enr_err is not None: print(f"   nm_pre_err: {self.sym_enr_err} in {self.e2a_unit}.")
       if self.sym_enr_spirit is not None: print(f"   nm_pre_err: {self.sym_enr_spirit} in {self.e2a_unit}.")
       if self.sym_enr_spirit_err is not None: print(f"   nm_pre_err: {self.sym_enr_spirit_err} in {self.e2a_unit}.")
       if self.sym_enr_isodiff is not None: print(f"   nm_pre_err: {self.sym_enr_isodiff} in {self.e2a_unit}.")
       if self.sym_enr_isodiff_err is not None: print(f"   nm_pre_err: {self.sym_enr_isodiff_err} in {self.e2a_unit}.")
       if self.sym_enr_np is not None: print(f"   nm_pre_err: {self.sym_enr_np} in {self.e2a_unit}.")
       if self.sym_enr_np_err is not None: print(f"   nm_pre_err: {self.sym_enr_np_err} in {self.e2a_unit}.")

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
        self.note = 'HIC constraints'
        #: Attribute the density of the system (in fm^-3).
        self.den = None
        #: Attribute the upper limit of the energy per particle in SM (in MeV).
        self.sm_e2a_up = None
        #: Attribute the lower limit of the energy per particle in SM (in MeV).
        self.sm_e2a_lo = None
        #: Attribute the energy per particle in SM (in MeV).
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
        #: Attribute the upper limit of the pressure in NM for asy-soft EOS (in MeV fm-3).
        self.nm_pre_so_up = None
        #: Attribute the lower limit of the pressure in NM for asy-soft EOS (in MeV fm-3).
        self.nm_pre_so_lo = None
        #: Attribute the upper limit of the pressure in NM for asy-stiff EOS (in MeV fm-3).
        self.nm_pre_st_up = None
        #: Attribute the lower limit of the pressure in NM for asy-stiff EOS (in MeV fm-3).
        self.nm_pre_st_lo = None
        #: Attribute the centroid of the pressure in NM for asy-soft EOS (in MeV fm-3).
        self.nm_pre_so = None
        #: Attribute the uncertainty of the pressure in NM for asy-soft EOS (in MeV fm-3).
        self.nm_pre_so_err = None
        #: Attribute the centroid of the pressure in NM for asy-stiff EOS (in MeV fm-3).
        self.nm_pre_st = None
        #: Attribute the uncertainty of the pressure in NM for asy-stiff EOS (in MeV fm-3).
        self.nm_pre_st_err = None
        #: Attribute the lower limit of the pressure in NM for asy-stiff EOS (in MeV fm-3).
        self.nm_pre_st_lo = None
        #: Attribute the upper edge of the symmetry energy for FOPI/ASY-EOS constraints (in MeV).
        self.sym_enr_lo = None
        #: Attribute the upper edge of the symmetry energy for FOPI/ASY-EOS constraints (in MeV).
        self.sym_enr_up = None
        #: Attribute the centroids of the symmetry energy for FOPI/ASY-EOS constraints (in MeV).
        self.sym_enr = None
        #: Attribute the uncertainty of the symmetry energy for FOPI/ASY-EOS constraints (in MeV).
        self.sym_enr_err = None
        #: Attribute the centroid of the symmetry energy for SPIRIT constraints (in MeV).
        self.sym_enr_spirit = None
        #: Attribute the uncertainty of the symmetry energy for SPIRIT constraints (in MeV).
        self.sym_enr_spirit_err = None
        #: Attribute the centroid of the symmetry energy for isospin difusion (in MeV).
        self.sym_enr_isodiff = None
        #: Attribute the uncertainty of the symmetry energy for isospin difusion (in MeV).
        self.sym_enr_isodiff_err = None
        #: Attribute the centroid of the symmetry energy for isospin difusion (in MeV).
        self.sym_enr_np = None
        #: Attribute the uncertainty of the symmetry energy for isospin difusion (in MeV).
        self.sym_enr_np_err = None
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
