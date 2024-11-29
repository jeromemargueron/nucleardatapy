
import os
import sys
import numpy as np

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_SetupNucNskinExp.py:")
    print(50*'-')
    #
    sources, sources_lower = nuda.nuc_nskin_exp( )[0]
    print('Complete list of available sources:', sources )
    #
    sources = ['48Ca', '208Pb']
    #
    print('sources considered:',sources)
    #
    for source in sources:
        #
        # get the neutron skin associated to `source` and `cal`
        #
        # 
        cals = nuda.nuc_nskin_exp_source( source = source )
        print(f'source: {source}, cals: {cals}')
        #
        for cal in cals:
            nskin = nuda.SetupNeutronSkinExp( source = source, cal = cal )
            nskin.print_output( )
            #
    #
    print(50*'-')
    print("Exit sample_SetupNucNskinExp.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
