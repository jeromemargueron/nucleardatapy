
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter matter_setupCheck_script.py:")
    print(50*'-')
    #
    # select an exemple for a microscopic EOS
    #
    print('For micro:')
    micro_mbs, micro_mbs_lower = nuda.matter.micro_mbs()
    for mb in micro_mbs: 
        print('   For mb:',mb)
        models, models_lower = nuda.matter.micro_models_mb( mb )
        print('   Models: ',models)
    model = '1998-VAR-AM-APR'
    micro = nuda.matter.setupMicro( model = model )
    #
    # select an exemple for a phenomenological EOS
    #
    print('For pheno:')
    pheno_models = [ 'Skyrme', 'ESkyrme', 'NLRH', 'DDRH', 'DDRHF' ]
    for model in pheno_models:
        print('   For model:',model)
        params, params_lower = nuda.matter.pheno_params( model = model )
        print('   Params:',params)
    model = 'Skyrme'
    param = 'SLy5'
    pheno = nuda.matter.setupPheno( model = model, param = param )
    #
    # select EoS (choose between the microscopic and the phenomenological EoS previously fixed):
    #
    eos = micro
    #eos = pheno
    #
    # define reference band
    #
    den = np.array([0.08,0.1,0.12,0.14,0.16])
    models = [ '2016-MBPT-AM', '2016-QMC-NM', '2020-MBPT-AM' ]
    band = nuda.matter.setupMicroBand( models, den=den, matter='NM' )
    #
    # check if eos is inside the band
    #
    check = nuda.matter.setupCheck( eos = eos, band = band )
    #
    print('eos inside band?',check.isInside)
    print('eos outside band?',check.isOutside)
    #
    if nuda.env.verb_output: check.print_outputs( )
    #
    print(50*'-')
    print("Exit matter_setupCheck_script.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
