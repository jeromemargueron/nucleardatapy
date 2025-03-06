
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter matter_setupPheno_script.py:")
    print(50*'-')
    #
    #models, models_lower = nuda.matter.pheno_models()
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
    print("Exit matter_setupPheno_script.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
