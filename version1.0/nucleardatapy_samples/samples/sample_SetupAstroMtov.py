
import os
import sys
import numpy as np

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_SetupAstroMtot.py:")
    print(50*'-')
    #
    # sources down
    #
    sources_do = nuda.astro_masses( )[0]
    print('Complete list of available sources_low:',sources_do)
    #
    sources_do = [ 'J1614–2230', 'J0348+0432', 'J2215+5135', 'J1600+3053', 'J0740+6620' ]
    #sources_do = [ 'J1614–2230', 'J1600+3053', 'J0740+6620' ]
    #
    print('sources_low considered:',sources_do)
    #
    # sources up
    #
    sources_up = nuda.astro_mup( )[0]
    print('Complete list of available sources_up:',sources_up)
    #
    #sources_up = [ 'GW170817' ]
    #
    print('sources_up considered:',sources_up)
    #
    # compute the distribution
    #
    prob = nuda.SetupAstroMtov( sources_do, sources_up )
    prob.print_output( )
    prob.print_table( )
    #
    print(50*'-')
    print("Exit sample_SetupAstroMtov.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
