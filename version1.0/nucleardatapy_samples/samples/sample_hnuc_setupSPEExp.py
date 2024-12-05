
import os
import sys
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_hnuc_setupSPEExp.py:")
    print(50*'-')
    #
    #tables = [ '2013-Angeli' ]
    tables, tables_lower = nuda.hnuc.spe_exp_tables()
    #
    for table in tables:
        #
        hnuc = nuda.hnuc.setupSPEExp( table = table )
        print('Z:',hnuc.Z)
        print('A:',hnuc.A)
        print('spe:',hnuc.spe)
        if nuda.env.verb_output: hnuc.print_outputs( )
    #
    print(50*'-')
    print("Exit sample_hnuc_setupSPEExp.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
