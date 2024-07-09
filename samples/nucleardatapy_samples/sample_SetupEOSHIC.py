
import os
import sys
import numpy as np

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_SetupEOSHIC.py:")
    print(50*'-')
    #
    constraints, constraints_lower = nuda.constraints_EOSHIC()
    #
    for constraint in constraints:
        #
        print('constraint:',constraint)
        hic = nuda.SetupEOSHIC( constraint = constraint )
        hic.print_outputs( )
    #
    print(50*'-')
    print("Exit sample_SetupEOSHIC.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
