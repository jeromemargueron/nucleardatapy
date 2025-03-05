import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter crust_setupCrust_script.py:")
    print(50*'-')
    #
    models, models_lower = nuda.crust.crust_models()
    #
    for model in models:
        #
        crust = nuda.crust.setupCrust( model = model )
        if nuda.env.verb_output: crust.print_outputs( )
    #
    print(50*'-')
    print("Exit crust_setupCrust_script.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
