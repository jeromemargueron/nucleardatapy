
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter astro_setupMup_script.py:")
    print(50*'-')
    #
    sources, sources_lower = nuda.astro.mup_sources( )
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
            if nuda.env.verb_latex: mup.print_latex( )
            #
        mupav = nuda.astro.setupMupAverage( source = source )
        if nuda.env.verb_output: mupav.print_output( )
        if nuda.env.verb_latex: mupav.print_latex( )
    #
    print(50*'-')
    print("Exit astro_setupMup_script.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
