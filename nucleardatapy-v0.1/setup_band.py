import os
import sys
import numpy as np  # 1.15.0
from scipy.interpolate import CubicSpline

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def gauss( e, e_cent, e_err ):
    fac = math.sqrt( nuda.cst.two * nuda.cst.pi ) * sigma
    return nm.exp( -nuda.cst.half * ( ( e - e_cent ) / e_err )**2 ) / fac

class SetupBand():
    """
    Instantiate the object with statistical distributions averaging over
    the models given as inputs.

    :param models: The models given as inputs. 
    :type models: list. 
    :param nden: number of density points. 
    :type nden: int, optional. 
    :param ne: number of points along the energy axis. 
    :type ne: int, optional. 

    **Attributes:**
    """
    #
    def __init__( self, models, nden = 10, ne = 1000 ):
        """
        Parameters
        ----------
        model : str, optional
        The model to consider. Choose between: 1998-VAR-AM-APR (default), 2008-AFDMC-NM, ...
        """
        #
        if nuda.env.verb: print("Enter SetupBand()")
        #
        #: Attribute model.
        self.models = models
        if nuda.env.verb: print("models:",models)
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
        # compute n_min and n_max in NM for the models in order to never extrapolate
        #
        nm_den_min_tmp = []; nm_den_max_tmp = [];
        for model in models:
            mic = nuda.SetupMicro( model = model )
            nm_den_min_tmp.append( mic.nm_den_min ); nm_den_max_tmp.append( mic.nm_den_max )
        print('nm_den_max_tmp:',nm_den_max_tmp)
        print('nm_den_min_tmp:',nm_den_min_tmp)
        self.nm_den_min = max( nm_den_min_tmp ); self.nm_den_max = min( nm_den_max_tmp );
        print('nm_den_max:',self.nm_den_max)
        print('nm_den_min:',self.nm_den_min)
        #
        nm_den_step = ( self.nm_den_max - self.nm_den_min ) / float( nden )
        self.nm_den = self.nm_den_min + np.arange(nden+1) * nm_den_step
        print('nm_den:',self.nm_den)
        self.nm_kfn = nuda.kf_n( self.nm_den )
        # loop over models
        #    interpolate models and errors
        #    contruct a matrix with Gaussian distributions
        #
        e2effg = -1.0 + 2.0 * np.arange( ne + 1 ) / float( ne ) 
        mat = np.zeros( (nden+1,ne+1), dtype = float )
        #
        for model in models:
            mic = nuda.SetupMicro( model = model )
            cs_nm_e2a = CubicSpline( mic.nm_den, mic.nm_e2a )
            cs_nm_e2a_err = CubicSpline( mic.nm_den, mic.nm_e2a_err )
            e2a_cent = cs_nm_e2a( self.nm_den )
            e2a_err = cs_nm_e2a( self.nm_den )
            #e2a = e2effg * nuda.effg( self.nm_kfn )
            #for k in range( nden+1 ):
            #    for j in range( ne+1 ):
            #        mat[k,j] += gauss( e2a, e2a_cent[k], e2a_err[k] )
        #
        #    compute centroid and standard deviation as function of the density
        #
        self.nm_e2a_cent = []; self.nm_e2a_err = [];
        #for k in range(nden+1):
        #    cent = 0.0
        #    for j in range( ne+1 ):
        #        cent += mat(k,j)
        #    self.nm_e2a_cent.append()
        #
        if nuda.env.verb: print("Exit SetupBand()")
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
        #if self.sm_den is not None: print(f"   sm_den: {np.round(self.sm_den,3)} in {self.den_unit}")
        #
        if nuda.env.verb: print("Exit print_outputs()")
        #
