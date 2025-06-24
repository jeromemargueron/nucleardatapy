
import os
import sys
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter hnuc_setupRE2LExp_script.py:")
    print(50*'-')
    #
    tables = [ '2013-2L-Ahn' ]
    #tables, tables_lower = nuda.hnuc.re2L_exp_tables()
    #
    print('run over tables:',tables)
    for table in tables:
        #
        hnuc = nuda.hnuc.setupRE2LExp( table = table )
        print('   Z:',hnuc.Z)
        print('   A:',hnuc.A)
        print('  ch:',hnuc.ch)
        print('llre:',hnuc.llre)
        print('llre_err:',hnuc.llre_err)
        print('lldre:',hnuc.lldre)
        print('lldre_err:',hnuc.lldre_err)
        if nuda.env.verb_output: hnuc.print_outputs( )
        if nuda.env.verb_latex:  hnuc.print_latex( )
    #
    print(50*'-')
    print("Exit hnuc_setupRE2LExp_script.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
