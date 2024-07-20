
import os
import sys
import numpy as np

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_SetupPhenoMatter.py:")
    print(50*'-')
    #
    #models, models_lower = nudy.models_pheno()
    models = [ 'Skyrme', 'NLRH', 'DDRH', 'DDRHF' ]
    #
    for model in models:
        #
        params, params_lower = nuda.params_pheno_matter( model = model )
        #params = [ 'SLy5' ]
        #params = [ 'ABC' ]
        #
        for param in params:
            #
            print('in Sample: model, param',model,param)
            mic = nuda.SetupPhenoMatter( model = model, param = param )
            mic.print_outputs( )
    #
    print(50*'-')
    print("Exit sample_SetupPhenoMatter.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
