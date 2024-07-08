import os
import sys
import numpy as np  # 1.15.0
import random

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

nsat = 0.16

class SetupEsymDen():
    """
    Instantiate the values of Esym and Lsym from the constraint.
    
    :param constraint: name of the model: '2014-IAS', ...
    :type constraint: str.
    :returns: constraint, ref, label, note, Esym, Lsym.
    """
    #
    def __init__( self, constraint = '2014-IAS' ):
        #
        if nuda.env.verb: print("Enter SetupEsymDen()")
        #
        #: Attribute the constraint
        self.constraint = constraint
        if nuda.env.verb: print("constraint:",constraint)
        #
        constraints, constraints_lower = nuda.constraints_EsymLsym()
        #
        if constraint.lower() not in constraints_lower:
            print('The constraint ',constraint,' is not in the list of constraints.')
            print('list of constraints:',constraints)
            print('-- Exit the code --')
            exit()
        #
        el = nuda.SetupEsymLsym( constraint = constraint )
        print('Esym:',el.Esym)
        print('Lsym_min:',el.Lsym_min)
        print('Lsym_max:',el.Lsym_max)
        #cons.print_outputs( )
        #
        if el.plot == 'band_y':
            #
            nden = 5
            den = 0.1+0.1 * np.arange(nden+1) / float( nden )
            self.esym_den = den
            #
            e_min = 100.0 * np.ones( (size(den)) )
            e_max = -100.0 * np.ones( (size(den)) )
            for i,Esym in enumerate(cons.cont_Esym):
                for j,Lsym in enumerate(cons.cont_Lsym):
                    esym = Esym + Lsym*(den-nsat)/(3*nsat)
                    for k in den:
                        if esym[k] > e_max[k]: e_max[k] = esym[k]
                        if esym[k] < e_min[k]: e_min[k] = esym[k]
            #: Attribute the minimal symmetry energy 
            self.esym_e2a_min = e_min
            #: Attribute the maximal symmetry energy 
            self.esym_e2a_max = e_max
            #
        else:
            #
            print('No Esyn(n) construction for constraint:',constraint)
            self.esym_den = None
            self.esym_e2a_min = None
            self.esym_e2a_max = None
            #
        #
        if nuda.env.verb: print("Exit SetupEsymDen()")
