
import os
import sys
import numpy as np

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_SetupEOSPheno.py:")
    print(50*'-')
    #
    #models, models_lower = nudy.eos_pheno_models()
    #models = [ 'Skyrme', 'NLRH', 'DDRHF' ]
    models = [ 'Skyrme' ]
    #
    for model in models:
        #
        #params, params_lower = nuda.eos_pheno_params( model = model )
        #params = [ 'SLy5' ]
        #params = [ 'ABC' ]
        params = [ 'BSK14' ]
        #
        for param in params:
            #
            print('in Sample: model, param',model,param)
            mic = nuda.SetupEOSPheno( model = model, param = param )
            mic.print_outputs( )
    #
    print(50*'-')
    print("Exit sample_SetupEOSPheno.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
