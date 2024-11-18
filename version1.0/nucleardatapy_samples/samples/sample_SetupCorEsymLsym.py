
import os
import sys
import numpy as np

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_SetupCorEsymLsym.py:")
    print(50*'-')
    #
    #constraints = [ '2009-HIC', '2010-RNP', '2012-FRDM', '2013-NS', '2014-IAS', '2014-IAS+RNP', \
    #         '2015-POL-208PB', '2015-POL-120SN', '2015-POL-68NI', '2017-UG', \
    #          '2021-PREXII-Reed', '2021-PREXII-Reinhard', '2021-PREXII-Zhang' ]
    constraints, constraints_lower = nuda.CorEsymLsym_constraints()
    #
    for constraint in constraints:
        #
        mic = nuda.SetupCorEsymLsym( constraint = constraint )
        #print('Esym:',mic.cont_Esym)
        #print('Lsym:',mic.cont_Lsym)
        mic.print_outputs( )
    #
    print(50*'-')
    print("Exit sample_SetupCorEsymLsym.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
