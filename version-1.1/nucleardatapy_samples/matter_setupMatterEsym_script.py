
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter matter_setupMatter_Esym.py:")
    print(50*'-')
    #
    #models, models_lower = nuda.eos_pheno_esym_models()
    models = [ 'Skyrme', 'ESkyrme', 'NLRH', 'DDRH', 'DDRHF' ]
    #
    for model in models:
        #
        params, params_lower = nuda.matter.matter_params( model = model )
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
    print("Exit matter_setupMatter_Esym.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
