
import os
import sys
import numpy as np

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_astro_setupMup.py:")
    print(50*'-')
    #
    sources = nuda.astro.mup_sources( )[0]
    print('Complete list of available sources:',sources)
    #
    sources = [ 'GW170817', 'GW190814' ]
    #
    print('sources considered:',sources)
    #
    for source in sources:
        #
        # get the mass associated to `source` and `obs`
        #
        hyps = nuda.astro.mup_hyps( source = source )
        print(f'source: {source}, hyps: {hyps}')
        #
        for hyp in hyps:
            mup = nuda.astro.setupMup( source = source, hyp = hyp )
            if nuda.env.verb_output: mup.print_output( )
            if nuda.env.verb_table: mup.print_table( )
            #
        mupav = nuda.astro.setupMupAverage( source = source )
        if nuda.env.verb_output: mupav.print_output( )
        if nuda.env.verb_table: mupav.print_table( )
    #
    print(50*'-')
    print("Exit sample_astro_setupMup.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
