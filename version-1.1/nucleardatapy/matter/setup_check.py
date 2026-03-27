
import numpy as np  # 1.15.0
from scipy.interpolate import CubicSpline

import nucleardatapy as nuda

class setupCheck():
    """
    Instantiate a flag reflecting if e2a from `eos` passes through the reference `band` or not.

    :param eos: object containing the eos to check.
    :type eos: object. 
    :param band: object containing the band employed to check the eos.
    :type band: object. 
    
    **Attributes:**
    
    """
    #
    def __init__( self, eos, band ):
        """
        Parameters
        ----------
        eos : object.
        Object containing the eos to check.
        band: object.
        Object containing the band employed to check the eos.
        matter: string which can be: 'nm' (default), 'sm', or 'esym'.
        """
        #
        if nuda.env.verb: print("Enter setupCheck()")
        #
        #: Attribute the object `eos`.
        self.eos = eos
        #: Attribute the object `band`.
        self.band = band
        #: Attribute the value for the variable `matter`.
        self.matter = band.matter
        #
        if 'fit' in eos.model:
            if self.matter.lower() == 'nm' or self.matter.lower() == 'sm':
                self.x = np.insert( eos.den, 0, 0.0 )
                self.y = np.insert( eos.e2a_int, 0, 0.0 )
            elif self.matter.lower() == 'esym':
                self.x = np.insert( eos.den, 0, 0.0 )
                self.y = np.insert( eos.esym, 0, 0.0 )
        else:
            if self.matter.lower() == 'nm':
                self.x = np.insert( eos.nm_den, 0, 0.0 )
                self.y = np.insert( eos.nm_e2a_int, 0, 0.0 )
            elif self.matter.lower() == 'sm':
                self.x = np.insert( eos.sm_den, 0, 0.0 )
                self.y = np.insert( eos.sm_e2a_int, 0, 0.0 )
            elif self.matter.lower() == 'esym':
                self.x = np.insert( eos.den, 0, 0.0 )
                self.y = np.insert( eos.esym, 0, 0.0 )
            else:
                print('setup_check: issue with matter:',self.matter)
                exit()
        cs_e2a = CubicSpline( self.x, self.y )
        self.eos_e2a_int = cs_e2a(band.den)
        flag = True
        for ind,den in enumerate(band.den):
            #if abs(cs_e2a(den)-band.e2a[ind]) > band.e2a_std[ind]:
            if abs(self.eos_e2a_int[ind]-band.e2a_int[ind]) > band.e2a_std[ind]:
                flag = False
        #: Attribute is eos is inside the band.
        self.isInside = flag
        #: Attribute is eos is outside the band.
        self.isOutside = not flag
        #
        self.den_unit = 'fm$^{-3}$'
        self.e2a_unit = 'MeV'
        #
        if nuda.env.verb: print("Exit setupCheck()")
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
        print('For matter:',self.matter)
        print('EOS:')
        if self.x is not None: print(f"   den: {np.round(self.x,2)} in {self.den_unit}")
        if self.y is not None: print(f"   e2a: {np.round(self.y,2)} in {self.e2a_unit}")
        print('BAND:')
        if self.band.den is not None: print(f"   den: {np.round(self.band.den,2)} in {self.den_unit}")
        if self.band.e2a_int is not None: print(f"   e2a_int: {np.round(self.band.e2a_int,2)} in {self.e2a_unit}")
        if self.band.e2a_std is not None: print(f"   e2a_std: {np.round(self.band.e2a_std,2)} in {self.e2a_unit}")
        #
        if nuda.env.verb: print("Exit print_outputs()")
        #

