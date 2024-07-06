import os
import sys
import numpy as np  # 1.15.0
from scipy.interpolate import CubicSpline

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def gauss( e, e_cent, e_err ):
    fac = np.sqrt( nuda.cst.two * nuda.cst.pi ) * e_err
    return np.exp( -nuda.cst.half * ( ( e - e_cent ) / e_err )**2 ) / fac

class SetupMicroBand():
    """
    Instantiate the object with statistical distributions averaging over
    the models given as inputs and in NM.

    :param models: The models given as inputs. 
    :type models: list. 
    :param nden: number of density points. 
    :type nden: int, optional. 
    :param ne: number of points along the energy axis. 
    :type ne: int, optional. 

    **Attributes:**
    """
    #
    def __init__( self, models, nden = 10, ne = 200 ):
        """
        Parameters
        ----------
        model : str, optional
        The model to consider. Choose between: 1998-VAR-AM-APR (default), 2008-AFDMC-NM, ...
        """
        #
        if nuda.env.verb: print("Enter SetupMicroBand()")
        #
        #: Attribute model.
        self.models = models
        if nuda.env.verb: print("models:",models)
        #: Attribute color
        self.color = 'pink'
        #: Attribute alpha
        self.alpha = 0.5
        #: Attribute number of points in density
        self.nden = nden
        if nuda.env.verb: print("nden:",nden)
        #
        # check that the models are available in the toolkit
        #
        modelsref, modelsref_lower = nuda.models_micro()
        for model in models:
            if model.lower() not in modelsref_lower:
                print('model:',model,' is not available in the toolkit')
                print('exit')
                exit()
        #
        # Fix the density array
        #
        # compute n_min and n_max in NM for the models in order to avoid extrapolation
        nm_den_min_tmp = []; nm_den_max_tmp = [];
        for model in models:
            mic = nuda.SetupMicro( model = model )
            nm_den_min_tmp.append( mic.nm_den_min ); nm_den_max_tmp.append( mic.nm_den_max )
        #if nuda.env.verb: print('nm_den_max_tmp:',nm_den_max_tmp)
        #if nuda.env.verb: print('nm_den_min_tmp:',nm_den_min_tmp)
        self.nm_den_min = max( nm_den_min_tmp ); self.nm_den_max = min( nm_den_max_tmp );
        if nuda.env.verb: print('nm_den_max:',self.nm_den_max)
        if nuda.env.verb: print('nm_den_min:',self.nm_den_min)
        # Set the a density array between den_min and den_max
        nm_den_step = ( self.nm_den_max - self.nm_den_min ) / float( nden )
        self.nm_den = self.nm_den_min + np.arange(nden+1) * nm_den_step
        if nuda.env.verb: print('nm_den:',self.nm_den)
        self.nm_kfn = nuda.kf_n( self.nm_den )
        #
        # Contruct a matrix with Gaussian distributions
        # associated to the models
        #
        e2effg = -1.0 + 2.0 * np.arange( ne + 1 ) / float( ne ) 
        #e2a = 40.0 * np.arange( ne + 1 ) / float( ne )
        mat = np.zeros( (nden+1,ne+1), dtype = float )
        mat1 = mat; mat2= mat;
        #
        for model in models:
            if nuda.env.verb: print('model:',model)
            # Load the results from model
            mic = nuda.SetupMicro( model = model )
            # Prepare spline for E/A
            cs_nm_e2a = CubicSpline( mic.nm_den, mic.nm_e2a )
            # Prepare spline for E/A_err
            cs_nm_e2a_err = CubicSpline( mic.nm_den, mic.nm_e2a_err )
            # Use the spline to get E/A and error for the density array
            e2a_cent = cs_nm_e2a( self.nm_den )
            e2a_err = cs_nm_e2a_err( self.nm_den )
            for k,kfn in enumerate(self.nm_kfn):
                e2a = e2effg * nuda.effg( kfn )
                if nuda.env.verb: print('For k,kfn',k,kfn)
                if nuda.env.verb: print('e2a:',e2a_cent[k],' effg:',nuda.effg(kfn),' err:',e2a_err[k])
                mat[k,:] += e2a_cent[k] * gauss( e2a[:], e2a_cent[k], e2a_err[k] )
        #
        #    compute centroid and standard deviation as function of the density
        #
        self.nm_e2a = []; self.nm_e2a_std = [];
        for k,kfn in enumerate(self.nm_kfn):
            e2a = e2effg * nuda.effg( kfn )
            self.nm_e2a.append( np.mean(mat[k,:]*e2a)/np.mean(mat[k,:]) )
            self.nm_e2a_std.append(  np.mean(mat[k,:]*e2a**2)/np.mean(mat[k,:]) )
        self.nm_e2a = np.array(self.nm_e2a, dtype=float )
        self.nm_e2a_std = np.sqrt( np.array(self.nm_e2a_std, dtype=float ) - self.nm_e2a**2 )
        #
        if nuda.env.verb: print("Exit SetupMicroBand()")
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
        print("   models :",self.models)
        print("   den_min:",self.nm_den_min)
        print("   den_max:",self.nm_den_max)
        print("   den :",np.round(self.nm_den,3))
        print("   kfn :",np.round(self.nm_kfn,2))
        print("   e2a :",np.round(self.nm_e2a,2))
        print("   std :",np.round(self.nm_e2a_std,3))
        #if self.sm_den is not None: print(f"   sm_den: {np.round(self.sm_den,3)} in {self.den_unit}")
        #
        if nuda.env.verb: print("Exit print_outputs()")
        #
