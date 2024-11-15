
import os
import sys
import numpy as np

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_SetupAstroMR.py:")
    print(50*'-')
    #
    sources = nuda.astro_mr( )[0]
    print('Complete list of available sources:', sources )
    #
    sources = [ 'J0030+0451', 'J0740+6620' ]
    #
    print('sources considered:',sources)
    #
    for source in sources:
        #
        # get the mass associated to `source` and `obs`
        #
        obss = nuda.astro_mr_source( source = source )
        #print('obss:',obss)
        #
        for obs in obss:
            mr = nuda.SetupAstroMR( source = source, obs = obs )
            mr.print_outputs( )
            #
        #print('Call average for source:', source)
        #avmass = nuda.SetupAstroMRAverage( source = source )
        #print('End of call average')
        #avmass.print_outputs( )
    #
    print(50*'-')
    print("Exit sample_SetupAstroMR.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
