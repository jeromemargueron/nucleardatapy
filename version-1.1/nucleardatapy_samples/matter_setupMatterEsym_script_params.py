
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter matter_setupMatterEsym_script_params.py:")
    print(50*'-')
    #
    print(30*'-')
    print("list models:")
    print(30*'-')
    #
    #models, models_lower = nuda.matter.matter_models()
    models = [ 'Skyrme', 'ESkyrme', 'NLRH', 'DDRH', 'DDRHF', 'Var', 'MC', 'MBPT', 'NLEFT', 'BHF2BF', 'BHF23BF', 'SCGF', 'CC' ]
    #models = [ 'Skyrme' ]
    #models = [ 'ESkyrme' ]
    #models = [ 'NLRH' ]
    #models = [ 'DDRH' ]
    #models = [ 'DDRHF' ]
    #models = [ 'Var' ]
    #models = [ 'MC' ]
    models = [ 'MBPT' ]
    #models = [ 'NLEFT' ]
    #models = [ 'BHF2BF' ]
    #models = [ 'BHF23BF' ]
    #models = [ 'SCGF' ]
    #models = [ 'CC' ]
    #
    print(f'all models: {models}\n')
    #
    print(30*'-')
    print("list models and parameters:")
    print(30*'-')
    #
    for model in models:
        #
        params, params_lower = nuda.matter.matter_esym_params( model = model )
        #params.sort()
        print(f'model: {model} params: {params}\n')
        #params2, params2_lower = nuda.matter.matter_params_old( model = model )
        #print(f'model: {model} params: {params2} (old)\n')
        #if len(params) != len(params2):
        #    print(f'issue with model: {model}') 
        #    print('Exit')
        #    exit()
    #
    print(50*'-')
    print("Exit matter_setupMatterEsym_script_params.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
