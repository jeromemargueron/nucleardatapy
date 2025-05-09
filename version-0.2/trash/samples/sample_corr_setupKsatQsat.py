
import os
import sys
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_corr_setupKsatQsat.py:")
    print(50*'-')
    #
    #edfs = [ '2024-DFT-SKY', '2024-DFT-ESKY', '2024-DFT-DDRH', \
    #         '2024-DFT-NLRH', '2024-DFT-DDRHF', '2024-DFT-Gogny', \
    #         '2024-DFT-xEFT' ]
    edfs, edfs_lower = nuda.corr.KsatQsat_edfs()
    #
    for edf in edfs:
        #
        kq = nuda.corr.setupKsatQsat( edf = edf )
        print('Ksat:',kq.Ksat)
        print('Qsat:',kq.Qsat)
        print('m,c:',kq.m,kq.c)
        if nuda.env.verb_output: kq.print_outputs( )
    #
    print(50*'-')
    print("Exit sample_corr_setupKsatQsat.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
