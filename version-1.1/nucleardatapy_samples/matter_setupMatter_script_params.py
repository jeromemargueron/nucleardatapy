
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter matter_setupMatter_script_params.py:")
    print(50*'-')
    #
    print(30*'-')
    print("list models:")
    print(30*'-')
    #
    models, models_lower = nuda.matter.matter_micro_models()
    print(f'micro models: {models}\n')
    #
    models, models_lower = nuda.matter.matter_pheno_models()
    print(f'pheno models: {models} \n')
    #
    models, models_lower = nuda.matter.matter_models()
    print(f'all models: {models}\n')
    #
    print(30*'-')
    print("list models and parameters:")
    print(30*'-')
    #
    for model in models:
        #
        params, params_lower = nuda.matter.matter_params( model = model )
        params.sort()
        print(f'model: {model} params: {params}\n')
        params2, params2_lower = nuda.matter.matter_params_old( model = model )
        print(f'model: {model} params: {params2} (old)\n')
        if len(params) != len(params2):
            print(f'issue with model: {model}') 
            print('Exit')
            exit()
    #
    print(50*'-')
    print("Exit matter_setupMatter_script_params.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
