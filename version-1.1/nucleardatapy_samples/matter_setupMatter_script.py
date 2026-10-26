
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter matter_setupMatter_script.py:")
    print(50*'-')
    #
    #models, models_lower = nuda.matter.matter_models()
    #models = [ 'Skyrme', 'ESkyrme', 'NLRH', 'DDRH', 'DDRHF', 'Var', 'MC', 'MBPT', 'NLEFT', 'BHF2BF', 'BHF23BF', 'SCGF', 'CC' ]
    models = [ 'Skyrme' ]
    models = [ 'ESkyrme' ]
    models = [ 'NLRH' ]
    models = [ 'DDRH' ]
    models = [ 'DDRHF' ]
    models = [ 'Var' ]
    models = [ 'MC' ]
    models = [ 'MBPT' ]
    models = [ 'NLEFT' ]
    models = [ 'BHF2BF' ]
    models = [ 'BHF23BF' ]
    models = [ 'SCGF' ]
    models = [ 'CC' ]
    #
    for model in models:
        #
        params, params_lower = nuda.matter.matter_params( model = model )
        #params = [ 'SLy5' ]
        #params = [ 'ABC' ]
        print(f'params: {params}')
        #
        for param in params:
            #
            print('in Sample: model, param',model,param)
            matter = nuda.matter.setupMatter( model = model, param = param )
            if nuda.env.verb_output: matter.print_outputs( )
            if matter.sm_den is not None: print(f" sm_den: {np.round(matter.sm_den,2)} in {matter.den_unit}")
            if matter.sm_e2a is not None: print(f" sm_e2a: {np.round(matter.sm_e2a,2)} in {matter.e2a_unit}")
            if matter.sm_cs2 is not None: print(f" sm_cs2: {np.round(matter.sm_cs2,2)}")
            if matter.nm_den is not None: print(f" nm_den: {np.round(matter.nm_den,2)} in {matter.den_unit}")
            if matter.nm_e2a is not None: print(f" nm_e2a: {np.round(matter.nm_e2a,2)} in {matter.e2a_unit}")
            if matter.nm_cs2 is not None: print(f" nm_cs2: {np.round(matter.nm_cs2,2)}")
            #
        #
    #
    print(50*'-')
    print("Exit matter_setupMatter_script.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
