
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter astro_setupGW_script.py:")
    print(50*'-')
    #
    sources = nuda.astro.gw_sources( )[0]
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
        hyps = nuda.astro.gw_hyps( source = source )
        print(f'source: {source}, hyps: {hyps}')
        #
        for hyp in hyps:
            gw = nuda.astro.setupGW( source = source, hyp = hyp )
            if nuda.env.verb_output: gw.print_output( )
            if nuda.env.verb_latex: gw.print_latex( )
            #
        gwav = nuda.astro.setupGWAverage( source = source )
        if nuda.env.verb_output: gwav.print_output( )
        if nuda.env.verb_latex: gwav.print_latex( )
    #
    print(50*'-')
    print("Exit astro_setupGW_script.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
