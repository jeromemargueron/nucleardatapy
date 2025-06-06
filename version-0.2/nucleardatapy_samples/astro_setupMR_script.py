 
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter astro_setupMR_script.py:")
    print(50*'-')
    #
    sources, sources_lower = nuda.astro.mr_sources( )
    print('Complete list of available sources:', sources )
    #
    sources = [ 'J0030+0451', 'J0740+6620', 'J0437-4715' ]
    #
    print('sources considered:',sources)
    #
    for source in sources:
        #
        # get the mass associated to `source` and `obs`
        #
        obss = nuda.astro.mr_obss( source = source )
        print(f'source: {source}, obss: {obss}')
        #
        for obs in obss:
            mr = nuda.astro.setupMR( source = source, obs = obs )
            if nuda.env.verb_output: mr.print_output( )
            if nuda.env.verb_latex: mr.print_latex( )
            #
    #
    # Average
    #
    print('averages:')
    #
    sources_av = [ 'J0030+0451', 'J0740+6620' ]
    #
    print('sources considered:',sources_av)
    #
    for source in sources_av:
        #
        # get the mass associated to `source` and `obs`
        #
        obss = nuda.astro.mr_obss( source = source )
        print(f'source: {source}, obss: {obss}')
        mrav = nuda.astro.setupMRAverage( source = source, obss = obss )
        if nuda.env.verb_output: mrav.print_output( )
        if nuda.env.verb_latex: mrav.print_latex( )
        #
    #
    print(50*'-')
    print("Exit astro_setupMR_script.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
