
import os
import sys
import numpy as np

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_SetupAstroGW.py:")
    print(50*'-')
    #
    sources = [ 'GW170817', 'GW190425' ]
    #
    for source in sources:
        #
        # get the mass associated to `source` and `obs`
        #
        gw = nuda.SetupAstroGW( source = source, hyp = 1 )
        gw.print_outputs( )
    #
    print(50*'-')
    print("Exit sample_SetupAstroGW.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
