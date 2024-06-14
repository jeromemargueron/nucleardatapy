
import os
import sys
import numpy as np

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nudy

def main():
    #
    print(50*'-')
    print("Enter sample_SetupMicro.py:")
    print(50*'-')
    #
    #keys = [ '1998-VAR-AM-APR', '2008-AFDMC-NM', '2008-QMC-NM-swave', '2008-QMC-NM-AV4', \
    #         '2009-dQMC-NM', '2010-NM-Hebeler', '2013-QMC-NM', '2014-AFQMC-NM', '2016-QMC-NM', \
    #         '2016-MBPT-AM', '2018-QMC-NM', '2020-MBPT-AM-DHSL59', '2020-MBPT-AM-DHSL69', \
    #         '2023-MBPT-AM' ]
    keys = nudy.modelsMicro()
    #
    for key in keys:
        #
        mic = nudy.SetupMicro( model = key )
        nudy.print_outputs_micro( mic )
    #
    print(50*'-')
    print("Exit sample_SetupMicro.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
