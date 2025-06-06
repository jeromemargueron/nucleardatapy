
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
    #constraints = [ '2024-DFT-SKY', '2024-DFT-ESKY', '2024-DFT-DDRH', \
    #         '2024-DFT-NLRH', '2024-DFT-DDRHF', '2024-DFT-Gogny', \
    #         '2024-DFT-xEFT' ]
    #constraints, constraints_lower = nuda.corr.KsatQsat_constraints()
    constraints = [ '2024-DFT-SKY' ]
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
