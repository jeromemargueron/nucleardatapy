
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
    sources = nuda.astro_mtot( )[0]
    print('Complete list of available sources:',sources)
    #
    sources = [ 'GW170817' ]
    #
    print('sources considered:',sources)
    #
    for source in sources:
        #
        # get the mass associated to `source` and `obs`
        #
        hyps = nuda.astro_mtot_source( source = source )
        #hyps = ['low-spin+TaylorF2']
        print('hyps:',hyps)
        #
        for hyp in hyps:
            mass = nuda.SetupAstroMtot( source = source, hyp = hyp )
            mass.print_outputs( )
            #
        print('Call average for source:', source)
        avmtot = nuda.SetupAstroMtotAverage( source = source )
        print('End of call average')
        avmtot.print_outputs( )
    #
    print(50*'-')
    print("Exit sample_SetupAstroMtot.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
