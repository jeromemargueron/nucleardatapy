
import os
import sys
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_hnuc_setupBE2LExp.py:")
    print(50*'-')
    #
    tables = [ '2013-2L-Ahn' ]
    #tables, tables_lower = nuda.hnuc.be2L_exp_tables()
    #
    print('run over tables:',tables)
    for table in tables:
        #
        hnuc = nuda.hnuc.setupBE2LExp( table = table )
        print('   Z:',hnuc.Z)
        print('   A:',hnuc.A)
        print('  ch:',hnuc.ch)
        print('llbe:',hnuc.llbe)
        print('llbe_err:',hnuc.llbe_err)
        print('lldbe:',hnuc.lldbe)
        print('lldbe_err:',hnuc.lldbe_err)
        if nuda.env.verb_output: hnuc.print_outputs( )
        if nuda.env.verb_latex:  hnuc.print_latex( )
    #
    print(50*'-')
    print("Exit sample_hnuc_setupBE2LExp.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
