
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter eos_create_boundaries_script.py:")
    print(50*'-')
    #
    # ==============
    # create boundaries for the different layers
    # ==============
    #
    nuda.eos.create_boundaries()
    #
    # ==============
    # show dictionnary file
    # ==============
    #
    print('boundaries:')
    with open("nuda.param.path_eos/dict_boundaries.txt", "r") as f:
        available_models = eval(f.read(), {"np": np})
    print(available_models)
    #
    print(50*'-')
    print("Exit eos_create_boundaries_script.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
