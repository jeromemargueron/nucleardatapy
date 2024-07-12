
import os
import sys
import numpy as np

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_SetupMassesTheory.py:")
    print(50*'-')
    #
    #tables = [ '1995-DZ' ]
    tables, tables_lower = nuda.tables_masses_theory()
    #
    for table in tables:
        #
        # Search for GS and unstable nuclei in the 'AME' '2020'
        #
        mas = nuda.SetupMassesTheory( table = table )
        mas.print_outputs( )
    #
    print(50*'-')
    print("Exit sample_SetupMasses.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
