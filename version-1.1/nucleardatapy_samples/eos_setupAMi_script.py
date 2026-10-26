
import numpy as np

import nucleardatapy as nuda

def main():
    #
    asy = 0.25
    print(50*'-')
    print("Enter eos_setupAMi_script.py:")
    print("for asymmetry parameter: asy=",asy)
    print(50*'-')
    #
    #models, models_lower = nuda.matter.matter_models()
    models = [ 'Var' ]
    #
    for model in models:
        #
        params, params_lower = nuda.matter.matter_esym_params( model = model )
        #
        for param in params:
            #
            matt = nuda.eos.setupAMi( model = model, param = param, asy = asy )
            if nuda.env.verb_output: matt.print_outputs( )
    #
    print(50*'-')
    print("Exit eos_setupAMi_script.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
