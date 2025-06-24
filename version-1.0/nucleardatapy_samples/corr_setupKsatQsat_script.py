
import os
import sys
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter corr_setupKsatQsat_script.py:")
    print(50*'-')
    #
    #constraints = [ '1991-Pearson', 'EDF-SKY', 'EDF-ESKY', 'EDF-DDRH', \
    #         'EDF-NLRH', 'EDF-DDRHF', 'EDF-Gogny', \
    #         'EDF-xEFT' ]
    #constraints, constraints_lower = nuda.corr.KsatQsat_constraints()
    constraints = [ 'EDF-SKY' ]
    #
    for constraint in constraints:
        #
        kq = nuda.corr.setupKsatQsat( constraint = constraint )
        #print('Ksat:',kq.Ksat)
        #print('Qsat:',kq.Qsat)
        #print('m,c:',kq.m,kq.c)
        if nuda.env.verb_output: kq.print_outputs( )
        kq.print_outputs( )
    #
    print(50*'-')
    print("Exit corr_setupKsatQsat_script.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
