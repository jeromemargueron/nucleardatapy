
import os
import sys
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_hnuc_setupRE1XiExp.py:")
    print(50*'-')
    #
    tables = [ '2015-1Xi-Nakazawa' ]
    #tables, tables_lower = nuda.hnuc.re1Xi_exp_tables()
    #
    print('run over tables:',tables)
    for table in tables:
        #
        hnuc = nuda.hnuc.setupRE1XiExp( table = table )
        print('  A:',hnuc.A)
        print('  Z:',hnuc.Z)
        print(' ch:',hnuc.ch)
        print('lre:',hnuc.xire)
        print('lre_err:',hnuc.xire_err)
        if nuda.env.verb_output: hnuc.print_outputs( )
        if nuda.env.verb_latex:  hnuc.print_latex( )
    #
    print(50*'-')
    print("Exit sample_hnuc_setupRE1XiExp.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
