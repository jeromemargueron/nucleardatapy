
import os
import sys
import numpy as np

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_matter_setupPheno.py:")
    print(50*'-')
    #
    #models, models_lower = nuda.pheno_models()
    #models = [ 'Skyrme', 'ESkyrme', 'NLRH', 'DDRH', 'DDRHF' ]
    models = [ 'ESkyrme' ]
    #
    for model in models:
        #
        params, params_lower = nuda.matter.pheno_params( model = model )
        #params = [ 'SLy5' ]
        #params = [ 'ABC' ]
        #
        for param in params:
            #
            print('in Sample: model, param',model,param)
            pheno = nuda.matter.setupPheno( model = model, param = param )
            if nuda.env.verb_output: pheno.print_outputs( )
            #
        #
    #
    print(50*'-')
    print("Exit sample_matter_setupPheno.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
