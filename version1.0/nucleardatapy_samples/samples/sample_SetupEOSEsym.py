
import os
import sys
import numpy as np

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_SetupEOSEsym.py:")
    print(50*'-')
    #
    #constraints = [ '2009-HIC', '2010-RNP', '2012-FRDM', '2013-NS', '2014-IAS', '2014-IAS+RNP', \
    #         '2015-POL-208PB', '2015-POL-120SN', '2015-POL-68NI', '2017-UG', \
    #          '2021-PREXII-Reed', '2021-PREXII-Reinhard', '2021-PREXII-Zhang' ]
    #constraints, constraints_lower = nuda.CorEsymLsym_constraints()
    constraints = [ '2014-IAS' ]
    #
    Ksym = -100.0
    #
    for constraint in constraints:
        #
        esym = nuda.SetupEOSEsym( constraint = constraint , Ksym=Ksym )
        #print('Esym_max:',esym.esym_e2a_max)
        #print('Esym_min:',esym.esym_e2a_min)
        esym.print_outputs()
    #
    print(50*'-')
    print("Exit sample_SetupEOSEsym.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
