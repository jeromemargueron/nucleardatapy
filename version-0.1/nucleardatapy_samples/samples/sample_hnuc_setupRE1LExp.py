
import os
import sys
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_hnuc_setupRE1LExp.py:")
    print(50*'-')
    #
    tables = [ '2016-1L-GHM' ]
    #tables, tables_lower = nuda.hnuc.re1L_exp_tables()
    #
    print('run over tables:',tables)
    for table in tables:
        #
        hnuc = nuda.hnuc.setupRE1LExp( table = table )
        print('  Z:',hnuc.Z)
        print('  A:',hnuc.A)
        print(' ch:',hnuc.ch)
        print('lre:',hnuc.lre)
        print('lre_err:',hnuc.lre_err)
        if nuda.env.verb_output: hnuc.print_outputs( )
        if nuda.env.verb_latex:  hnuc.print_latex( )
    #
    print(50*'-')
    print("Exit sample_hnuc_setupRE1LExp.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
