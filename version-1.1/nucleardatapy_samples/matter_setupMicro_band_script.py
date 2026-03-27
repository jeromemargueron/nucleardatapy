
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter matter_setupMicro_band_script.py:")
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
    band = nuda.matter.setupMicroBand( models, den=den, matter='NM' )
    if nuda.env.verb_output: band.print_outputs( )
    #
    # Band for SM
    #
    models = [ '2016-MBPT-AM', '2020-MBPT-AM' ]
    #
    band = nuda.matter.setupMicroBand( models, den=den, matter='SM' )
    if nuda.env.verb_output: band.print_outputs( )
    #
    # Band for esym
    #
    models = [ '2016-MBPT-AM', '2020-MBPT-AM' ]
    #
    band = nuda.matter.setupMicroBand( models, den=den, matter='ESYM' )
    if nuda.env.verb_output: band.print_outputs( )
    #
    print(50*'-')
    print("Exit matter_setupMicro_band_script.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
