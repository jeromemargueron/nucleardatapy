
import os
import sys
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_hnuc_setupBE1LExp.py:")
    print(50*'-')
    #
    tables = [ '2016-GHM' ]
    #tables, tables_lower = nuda.hnuc.be1L_exp_tables()
    #
    print('run over tables:',tables)
    for table in tables:
        #
        hnuc1L = nuda.hnuc.setupBE1LExp( table = table )
        print('Z:',hnuc1L.Z)
        print('A:',hnuc1L.A)
        print('lbe:',hnuc1L.lbe)
        print('lbe_err:',hnuc1L.lbe_err)
        if nuda.env.verb_output: hnuc1L.print_outputs( )
    #
    print(50*'-')
    print("Exit sample_hnuc_setupBE1LExp.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
