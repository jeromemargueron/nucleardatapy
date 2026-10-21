
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
    eos=nuda.eos.setupCSEoS()
    #
    # ==============
    # show dictionnary file
    # ==============
    #
    print('eos:')
    #
    eos.Final_EoS()
    #
    print(50*'-')
    print("Exit eos_create_boundaries_script.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
