
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter eos_setupAMBeqi_script.py:")
    print(50*'-')
    #
    models, models_lower = nuda.matter.matter_models()
    models = [ 'Var' ]
    #
    for model in models:
        #
        params, params_lower = nuda.matter.matter_esym_params( model = model )
        #
        for param in params:
            #
            matt = nuda.eos.setupAMBeqi( model = model, param = param )
            if nuda.env.verb_output: matt.print_outputs( )
            #
        #
    #
    print(50*'-')
    print("Exit eos_setupAMBeqi_script.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
