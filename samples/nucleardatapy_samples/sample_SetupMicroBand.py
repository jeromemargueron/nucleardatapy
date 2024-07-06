
import os
import sys
import numpy as np

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_SetupMicroBand.py:")
    print(50*'-')
    #
    #models = [ '2013-QMC-NM', '2014-AFQMC-NM', '2016-QMC-NM', '2016-MBPT-AM', '2018-QMC-NM', '2020-MBPT-AM-DHSL59', '2020-MBPT-AM-DHSL69', \
    #         '2023-MBPT-AM' ]
    models = [ '2013-QMC-NM', '2016-QMC-NM', '2016-MBPT-AM' ]
    #models = [ '2016-MBPT-AM' ]
    #
    band = nuda.SetupMicroBand( models )
    band.print_outputs( )
    #
    print(50*'-')
    print("Exit sample_SetupMicroBand.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
