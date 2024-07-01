import os
import sys
import numpy as np  # 1.15.0
from scipy.interpolate import CubicSpline

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def models_micro():
    """
    Return a list with the name of the models available in this toolkit and
    print them all on the prompt. These models are the following ones: \
    '1981-VAR-AM-FP', '1998-VAR-AM-APR', '2006-BHF-AM'*, '2008-BCS-NM', '2008-AFDMC-NM', \
    '2008-QMC-NM-swave', '2010-QMC-NM-AV4', '2009-DLQMC-NM', '2010-NM-Hebeler', \
    '2013-QMC-NM', '2014-AFQMC-NM', '2016-QMC-NM', '2016-MBPT-AM', \
    '2018-QMC-NM', '2020-MBPT-AM-DHSL59', '2020-MBPT-AM-DHSL69', \
    '2023-MBPT-AM'.

    :return: The list of models.
    :rtype: list[str].
    """
    models = [ '1981-VAR-AM-FP', '1998-VAR-AM-APR', '2008-BCS-NM', '2008-AFDMC-NM', \
             '2008-QMC-NM-swave', '2010-QMC-NM-AV4', '2009-DLQMC-NM', '2010-NM-Hebeler', \
             '2013-QMC-NM', '2014-AFQMC-NM', '2016-QMC-NM', '2016-MBPT-AM', \
             '2018-QMC-NM', '2020-MBPT-AM-DHSL59', '2020-MBPT-AM-DHSL69', \
             '2023-MBPT-AM' ]
    print('models available in the toolkit:',models)
    models_lower = [ item.lower() for item in models ]
    return models, models_lower

class SetupStat():
    """
    Instantiate the object with statistical distributions averaging over
    the models given as inputs.

    :param models: The models given as inputs. 
    :type models: str, optional. 

    **Attributes:**
    """
    #
    def __init__( self, models ):
        """
        Parameters
        ----------
        model : str, optional
        The model to consider. Choose between: 1998-VAR-AM-APR (default), 2008-AFDMC-NM, ...
        """
        #
        if nuda.env.verb: print("Enter SetupStat()")
        #
        #: Attribute model.
        self.models = models
        if nuda.env.verb: print("models:",models)
        #
        # check that the models are available in the toolkit
        #
        modelsref, modelsref_lower = models_micro()
        for model in models:
            if model.lower() not in modelsref_lower:
                print('model:',model,' is not available in the toolkit')
                print('exit')
                exit()
        #
        # compute n_min and n_max for the models in order to never extrapolate
        #
        den_min_tmp = []; den_max_tmp = [];
        for model in models:
            mic = nuda.SetupMicro( model = model )
            den_min_tmp.append( mic.den_min ); den_max_tmp.append( mic.den_max )
        print('den_max_tmp:',den_max_tmp)
        print('den_min_tmp:',den_min_tmp)
        #den_min = max( den_min_tmp ); den_max = min( den_max_tmp );
        #print('den_max:',den_max)
        #print('den_min:',den_min)
        #
        # loop over models
        #    interpolate models and errors
        #    contruct a matrix with Gaussian distributions
        #    compute centroid and standard deviation as function of the density
        #
        #
        if nuda.env.verb: print("Exit SetupStat()")
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
        #print("   den_min:",self.den_min)
        #print("   den_max:",self.den_max)
        #if self.sm_den is not None: print(f"   sm_den: {np.round(self.sm_den,3)} in {self.den_unit}")
        #
        if nuda.env.verb: print("Exit print_outputs()")
        #
