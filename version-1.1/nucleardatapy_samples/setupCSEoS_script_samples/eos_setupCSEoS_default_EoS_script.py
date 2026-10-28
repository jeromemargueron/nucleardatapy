import nucleardatapy as nuda
import numpy as np

import matplotlib.pyplot as plt



def main_without_full_outputs():
    #
    print(50*'-')
    print("Enter in function 'without_full_outputs' of eos_setupEoS_default_EoS_script.py:")
    print(50*'-')   

    eos=nuda.eos.setupCSEoS()
    eos.print_outputs()
    
    print(50*'-')
    print("Exit from function 'without_full_outputs' of eos_setupEoS_default_EoS_script.py:")
    print(50*'-')

def main_with_full_outputs():
    #
    print(50*'-')
    print("Enter in function 'with_full_outputs' of eos_setupEoS_default_EoS_script.py:")
    print(50*'-')   

    eos=nuda.eos.setupCSEoS(full_outputs=True)
    eos.print_outputs()
    
    # In case we need the other datas, for example we can take all the available data fro the inner_crust model as
    #print(eos.data_after_eos_construction['inner_crust'])
    
    print(50*'-')
    print("Exit from function 'with_full_outputs' of eos_setupEoS_default_EoS_script.py:")
    print(50*'-')
    #


if __name__ == "__main__":
    main_without_full_outputs()
    main_with_full_outputs()
    

