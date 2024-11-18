
import os
import sys
import numpy as np

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_SetupEOSMicroBand.py:")
    print(50*'-')
    #
    #models = [ '2013-QMC-NM', '2014-AFQMC-NM', '2016-QMC-NM', '2016-MBPT-AM', '2018-QMC-NM', '2019-MBPT-AM-DHSL59', '2019-MBPT-AM-DHSL69', \
    #         '2020-MBPT-AM' ]
    #models = [ '2016-MBPT-AM' ]
    #
    # Band for NM
    #
    models = [ '2013-QMC-NM', '2016-QMC-NM', '2016-MBPT-AM' ]
    #
    den = np.array([0.04,0.06,0.08,0.1,0.12,0.14,0.16])
    band = nuda.SetupEOSMicroBand( models, den=den, matter='NM' )
    band.print_outputs( )
    #
    # Band for SM
    #
    models = [ '2016-MBPT-AM', '2020-MBPT-AM' ]
    #
    band = nuda.SetupEOSMicroBand( models, den=den, matter='SM' )
    band.print_outputs( )
    #
    # Band for esym
    #
    models = [ '2016-MBPT-AM', '2020-MBPT-AM' ]
    #
    band = nuda.SetupEOSMicroBand( models, den=den, matter='ESYM' )
    band.print_outputs( )
    #
    print(50*'-')
    print("Exit sample_SetupEOSMicroBand.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
