
import os
import sys
import numpy as np

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nudy

def main():
    #
    print(50*'-')
    print("Enter sample_SetupPheno.py:")
    print(50*'-')
    #
    #models, models_lower = nudy.models_pheno()
    models = [ 'Skyrme', 'NLRH', 'DDRHF' ]
    #
    for model in models:
        #
        params, params_lower = nudy.params_pheno( model = model )
        #params = [ 'SLy5' ]
        #params = [ 'ABC' ]
        #
        for param in params:
            #
            print('in Sample: model, param',model,param)
            mic = nudy.SetupPheno( model = model, param = param )
            nudy.print_outputs_pheno( mic )
    #
    print(50*'-')
    print("Exit sample_SetupPheno.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
