
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter astro_setupMasses_script.py:")
    print(50*'-')
    #
    sources, sources_lower = nuda.masses_sources( )
    print('Complete list of available sources:', sources )
    #
    #sources = [ 'J1614–2230', 'J0348+0432', 'J2215+5135', 'J1600+3053', 'J0740+6620' ]
    sources = [ 'J1614–2230', 'J1600+3053', 'J0740+6620' ]
    #
    print('sources considered:',sources)
    #
    for source in sources:
        #
        # get the mass associated to `source` and `obs`
        #
        obss = nuda.astro.masses_obss( source = source )
        print(f'source: {source}, obss: {obss}')
        #
        for obs in obss:
            m = nuda.astro.setupMasses( source = source, obs = obs )
            if nuda.env.verb_output: m.print_output( )
            if nuda.env.verb_latex: m.print_latex( )
            #
        mav = nuda.astro.setupMassesAverage( source = source )
        if nuda.env.verb_output: mav.print_output( )
        if nuda.env.verb_latex: mav.print_latex( )
    #
    print(50*'-')
    print("Exit astro_setupMasses_script.py:")
    print(50*'-')
    #
    m = nuda.astro.setupMasses( source = 'J1614–2230', obs = 1 )
    print('For tests:',m.mass)
    #

if __name__ == "__main__":
    main()
