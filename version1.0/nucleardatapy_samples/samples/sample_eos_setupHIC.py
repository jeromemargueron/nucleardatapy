
import os
import sys
import numpy as np

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_eos_setupHIC.py:")
    print(50*'-')
    #
    constraints, constraints_lower = nuda.eos.hic_constraints()
    #
    for constraint in constraints:
        #
        print('constraint:',constraint)
        hic = nuda.eos.setupHIC( constraint = constraint )
        if nuda.env.verb_output: hic.print_outputs( )
    #
    print(50*'-')
    print("Exit sample_eos_setupHIC.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
