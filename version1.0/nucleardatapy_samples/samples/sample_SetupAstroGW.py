
import os
import sys
import numpy as np

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_SetupAstroGW.py:")
    print(50*'-')
    #
    sources = nuda.astro_gw( )[0]
    print('Complete list of available sources:', sources )
    #
    sources = [ 'GW170817', 'GW190425' ]
    #
    print('sources considered:',sources)
    #
    for source in sources:
        #
        # get the mass associated to `source` and `hyp`
        #
        hyps = nuda.astro_gw_source( source = source )
        print(f'source: {source}, hyps: {hyps}')
        #
        for hyp in hyps:
            gw = nuda.SetupAstroGW( source = source, hyp = hyp )
            gw.print_output( )
            gw.print_table( )
            #
        gwav = nuda.SetupAstroGWAverage( source = source )
        gwav.print_output( )
        gwav.print_table( )
    #
    print(50*'-')
    print("Exit sample_SetupAstroGW.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
