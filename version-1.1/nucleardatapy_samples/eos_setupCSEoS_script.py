
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter eos_setupCSEoS_script.py:")
    print(50*'-')
    #
    # ==============
    # create boundaries for the different layers
    # ==============
    #
    eos=nuda.eos.setupCSEoS()
    eos.print_outputs()
    #print(eos.data_dict)
    
    #
    # ==============
    # show dictionnary file
    # ==============
    #
    print('eos:')
    #
    
    
    #
    print(50*'-')
    print("Exit eos_setupCSEoS_script.py")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
