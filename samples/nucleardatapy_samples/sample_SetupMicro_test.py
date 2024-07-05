
import os
import sys
import numpy as np

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_SetupMicro.py:")
    print(50*'-')
    #
    #models = [ '1981-VAR-AM-FP' ]
    #models = [ '1998-VAR-AM-APR' ]
    #models = [ '2010-QMC-NM-AV4' ]
    models = [ '2012-AFDMC-NM-2' ]
    #models = [ '2016-MBPT-AM' ]
    #models = [ '2020-MBPT-AM-DHSL59' ]
    #models = [ '2020-MBPT-AM-DHSL69' ]
    #models = [ '2023-MBPT-AM' ]
    #
    for model in models:
        #
        mic = nuda.SetupMicro( model = model )
        mic.print_outputs( )
    #
    print(50*'-')
    print("Exit sample_SetupMicro.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
