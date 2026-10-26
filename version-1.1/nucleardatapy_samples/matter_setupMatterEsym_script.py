
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter matter_setupMatterEsym_script.py:")
    print(50*'-')
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
    #models = [ 'MBPT' ]
    #models = [ 'NLEFT' ]
    #models = [ 'BHF2BF' ]
    #models = [ 'BHF23BF' ]
    #models = [ 'SCGF' ]
    #models = [ 'CC' ]
    #
    for model in models:
        #
        params, params_lower = nuda.matter.matter_esym_params( model = model )
        #
        for param in params:
            #
            print('model, param:',model,param)
            matt = nuda.matter.setupMatterEsym( model = model, param = param )
            if nuda.env.verb_output: matt.print_outputs( )
            #
        #
    #
    print(50*'-')
    print("Exit matter_setupMatterEsym_script.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
