
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter matter_setupPheno_Esym_plot.py:")
    print(50*'-')
    #
    #models, models_lower = nuda.eos_pheno_esym_models()
    models = [ 'Skyrme', 'ESkyrme', 'NLRH', 'DDRH', 'DDRHF' ]
    #
    for model in models:
        #
        params, params_lower = nuda.matter.pheno_params( model = model )
        #
        for param in params:
            #
            print('model, param:',model,param)
            pheno = nuda.matter.setupPhenoEsym( model = model, param = param )
            if nuda.env.verb_output: pheno.print_outputs( )
            #
        #
    #
    print(50*'-')
    print("Exit matter_setupPheno_Esym_plot.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
