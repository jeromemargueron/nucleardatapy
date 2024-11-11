
import os
import sys
import numpy as np

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_SetupAstroMasses.py:")
    print(50*'-')
    #
    sources = nuda.astro_masses( )[0]
    print('Complete list of available sources:', sources )
    #
    sources = [ 'J1614–2230', 'J0348+0432', 'J2215+5135', 'J1600+3053', 'J0740+6620' ]
    sources = [ 'J1614–2230', 'J1600+3053', 'J0740+6620' ]
    #
    print('sources considered:',sources)
    #
    for source in sources:
        #
        # get the mass associated to `source` and `obs`
        #
        obss = nuda.astro_masses_source( source = source )
        #print('obss:',obss)
        #
        for obs in obss:
            mass = nuda.SetupAstroMasses( source = source, obs = obs )
            mass.print_outputs( )
            #
        #print('Call average for source:', source)
        avmass = nuda.SetupAstroMassesAverage( source = source )
        #print('End of call average')
        avmass.print_outputs( )
    #
    print(50*'-')
    print("Exit sample_SetupAstroMasses.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
