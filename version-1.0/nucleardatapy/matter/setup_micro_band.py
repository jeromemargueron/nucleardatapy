import os
import sys
import numpy as np  # 1.15.0
from scipy.interpolate import CubicSpline

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def gauss( e, e_cent, e_err ):
    fac = np.sqrt( nuda.cst.two * nuda.cst.pi ) * e_err
    return np.exp( -nuda.cst.half * ( ( e - e_cent ) / e_err )**2 ) / fac

class setupMicroBand():
    """
    Instantiate the object with statistical distributions averaging over
    the models given as inputs and in NM.

    :param models: The models given as inputs. 
    :type models: list. 
    :param nden: number of density points. 
    :type nden: int, optional. 
    :param ne: number of points along the energy axis. 
    :type ne: int, optional. 
    :param den: if not None (default), impose the densities. 
    :type den: None or numpy array, optional. 
    :param matter: can be 'NM' (default), 'SM' or 'ESYM'. 
    :type matter: str, optional. 

    **Attributes:**
    """
    #
    def __init__( self, models = [ '2016-MBPT-AM' ], nden = 10, ne = 200, den=None, matter='NM', e2a_min = -20.0, e2a_max = 50.0 ):
        """
        Parameters
        ----------
        model : str, optional.
        The model to consider. Choose between: 1998-VAR-AM-APR (default), 2008-AFDMC-NM, ...
        nden: int, optional.
        The density points to consider.
        ne: int, optional.
        The number of intervalle in the energy direction.
        den: None or numpy array.
        If None, then the density range is calculated automaticaly. If den = list of densities, the code will prefer using them.
        matter: str, optional.
        Set if we consider 'NM' neutron matter, 'SM' symmetric matter, or 'Esym' the symmetry energy.
        e2a_min: float, optional.
        e2a_min is set to be -20 MeV by default, or any number passed by the practitionner.
        e2a_max: float, optional.
        e2a_max is set to be 50 MeV by default, or any number passed by the practitionner.
        """
        #
        if nuda.env.verb: print("Enter setupMicroBand()")
        #
        if matter.lower() == 'nm':
            print('\nBand in NM')
            xfac = 1.2
        elif matter.lower() == 'sm':
            print('\nBand in SM')
            xfac = 1.8
        elif matter.lower() == 'esym':
            print('\nBand for Esym')
            xfac = 1.4
        #
        self = setupMicroBand.init_self( self )
        #
        #: Attribute model.
        self.models = models
        if nuda.env.verb: print("models:",models)
        #: Attribute number of points in density.
        self.nden = nden
        if nuda.env.verb: print("nden:",nden)
        #: Attribute a set of density points.
        self.den = den
        if nuda.env.verb: print("den:",den)
        #: Attribute matter str.
        self.matter = matter
        if nuda.env.verb: print("matter:",matter)
        #
        # check that the models are available in the toolkit
        #
        modelsref, modelsref_lower = nuda.matter.micro_models()
        for model in models:
            if model.lower() not in modelsref_lower:
                print('model:',model,' is not available in the toolkit')
                print('exit')
                exit()
            mic = nuda.matter.setupMicro( model = model )
            if matter.lower() == 'nm':
                if mic.nm_e2a is None:
                    print('There are no calculation in NM for model ',model)
                    print('exit')
                    exit()
            elif matter.lower() == 'sm':
                if mic.sm_e2a is None:
                    print('There are no calculation in SM for model ',model)
                    print('exit')
                    exit()
            elif matter.lower() == 'esym':
                esym = nuda.matter.setupMicroEsym( model = model )
                if esym.esym is None:
                    print('There are no calculation for Esym for model ',model)
                    print('exit')
                    exit()
        #
        # Fix the density array
        #
        if den is not None:
            self.den = den
            self.den_min = min( den )
            self.den_max = max( den )
        else:
            # compute n_min and n_max in NM for the models in order to avoid extrapolation
            den_min_tmp = []; den_max_tmp = [];
            for model in models:
                mic = nuda.matter.setupMicro( model = model )
                #?? esym = nuda.matter.setupMicroEsym( model = model )
                if matter.lower() == 'nm':
                    nm_den_min = min( mic.nm_den )
                    nm_den_max = max( mic.nm_den )
                    den_min_tmp.append( nm_den_min ); den_max_tmp.append( nm_den_max )
                elif matter.lower() == 'sm':
                    sm_den_min = min( mic.sm_den )
                    sm_den_max = max( mic.sm_den )
                    den_min_tmp.append( sm_den_min ); den_max_tmp.append( sm_den_max )
                elif matter.lower() == 'esym':
                    esym = nuda.eos.setupMicroEsym( model = model )
                    den_min = min( esym.den )
                    den_max = max( esym.den )
                    den_min_tmp.append( den_min ); den_max_tmp.append( den_max )
            self.den_min = max( den_min_tmp ); self.den_max = min( den_max_tmp );
            if nuda.env.verb: print('den_max:',self.den_max)
            if nuda.env.verb: print('den_min:',self.den_min)
            # Set the a density array between den_min and den_max
            den_step = ( self.den_max - self.den_min ) / float( nden )
            self.den = self.den_min + np.arange(nden+1) * den_step
        if nuda.env.verb: print('den:',self.den)
        if matter.lower() == 'nm':
            self.kfn = nuda.kf_n( self.den )
            self.kf = self.kfn * nuda.cst.two**nuda.cst.third
        elif matter.lower() == 'sm':
            self.kfn = nuda.kf_n( nuda.cst.half * self.den )
            self.kf = self.kfn
        elif matter.lower() == 'esym':
            self.kfn = nuda.kf_n( nuda.cst.half * self.den )
            self.kf = self.kfn
        #
        # Contruct a matrix with Gaussian distributions
        # associated to the models
        #
        #e2effg = -1.0 + 2.0 * np.arange( ne + 1 ) / float( ne )
        #if matter.lower() == 'nm':
        #    e2a = e2effg * nuda.effg( self.kfn )
        #elif matter.lower() == 'sm':
        #    e2a = e2effg * nuda.effg( self.kf )
        #elif matter.lower() == 'esym':
        #    e2a = e2effg * nuda.esymffg( self.kf )
        if e2a_max < e2a_min:
            print('e2a_max:',e2a_max,' is smaller than e2a_min: ',e2a_min)
            print('Please define these variables properly,')
            print('or leave default values without touching them.')
            print('Exit()')
            exit()
        step = ( e2a_max - e2a_min ) / float( ne )
        e2a = e2a_min + step * np.arange( ne + 1 )
        mat = np.zeros( (nden+1,ne+1), dtype = float )
        #
        for model in models:
            if nuda.env.verb: print('model:',model)
            # Load the results from model
            mic = nuda.matter.setupMicro( model = model )
            #?? esym = nuda.matter.setupMicroEsym( model = model )
            # Prepare spline for E/A and E/A_err
            if matter.lower() == 'nm':
                cs_e2a = CubicSpline( mic.nm_den, mic.nm_e2a_int )
                cs_e2a_err = CubicSpline( mic.nm_den, mic.nm_e2a_err )
            elif matter.lower() == 'sm':
                cs_e2a = CubicSpline( mic.sm_den, mic.sm_e2a_int )
                cs_e2a_err = CubicSpline( mic.sm_den, mic.sm_e2a_err )
            elif matter.lower() == 'esym':
                esym = nuda.matter.setupMicroEsym( model = model )
                cs_e2a = CubicSpline( esym.den, esym.esym )
                cs_e2a_err = CubicSpline( esym.den, esym.esym_err )
            # Use the spline to get E/A and error for the density array
            e2a_cent = cs_e2a( self.den )
            e2a_err = cs_e2a_err( self.den )
            # build mat[]
            for k,den in enumerate(self.den):
                if nuda.env.verb: print('For k,den',k,den)
                #if nuda.env.verb: print('e2a:',e2a_cent[k],' effg:',nuda.effg(kfn),' err:',e2a_err[k])
                mat[k,:] += e2a_cent[k] * gauss( e2a[:], e2a_cent[k], e2a_err[k] )
        #
        #    compute centroid and standard deviation as function of the density
        #
        self.e2a_int = []; self.e2a_std = [];
        for k,kfn in enumerate(self.kfn):
            self.e2a_int.append( np.mean(mat[k,:]*e2a)/np.mean(mat[k,:]) )
            self.e2a_std.append(  np.mean(mat[k,:]*e2a**2)/np.mean(mat[k,:]) )
        self.e2a_int = np.array(self.e2a_int, dtype=float )
        self.e2a_std = xfac * np.sqrt( np.array(self.e2a_std, dtype=float ) - self.e2a_int**2 )
        #
        if nuda.env.verb: print("Exit setupMicroBand()")
        #
    def print_outputs( self ):
        """
        Method which print outputs on terminal's screen.
        """
        #
        if nuda.env.verb: print("Enter print_outputs()")
        #
        print("- Print output:")
        print("   models :",self.models)
        print("   den_min:",self.den_min)
        print("   den_max:",self.den_max)
        print("   den :",np.round(self.den,3))
        print("   kfn :",np.round(self.kfn,2))
        print("   e2a :",np.round(self.e2a,2))
        print("   std :",np.round(self.e2a_std,3))
        #if self.sm_den is not None: print(f"   sm_den: {np.round(self.sm_den,3)} in {self.den_unit}")
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
        #: Attribute color.
        self.color = 'pink'
        #: Attribute alpha.
        self.alpha = 0.5
        #
        if nuda.env.verb: print("Exit init_self()")
        #
        return self        
