
import os
import sys
import numpy as np

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_astro_setupMasses.py:")
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
            if nuda.env.verb_table: m.print_table( )
            #
        mav = nuda.astro.setupMassesAverage( source = source )
        if nuda.env.verb_output: mav.print_output( )
        if nuda.env.verb_table: mav.print_table( )
    #
    print(50*'-')
    print("Exit sample_astro_setupMasses.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
