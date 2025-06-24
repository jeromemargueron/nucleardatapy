
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter matter_setupMicroEsym_script.py:")
    print(50*'-')
    #
    models, models_lower = nuda.matter.micro_esym_models()
    #
    for model in models:
        #
        print('model:',model)
        mic = nuda.matter.setupMicroEsym( model = model )
        if nuda.env.verb_output: mic.print_outputs( )
    #
    print(50*'-')
    print("Exit matter_setupMicroEsym_script.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
