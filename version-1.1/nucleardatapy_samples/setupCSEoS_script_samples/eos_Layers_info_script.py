import nucleardatapy as nuda
from pprint import pprint


import numpy as np
print(nuda.__file__)
def main():
    #
    print(50*'-')
    print("Enter EoS Layers info.py:")
    print(50*'-')
    #
    # ==============
    # create boundaries for the different layers
    # ==============
    #['atmosphere', 'outer_crust', 'inner_crust', 'outer_core', 'inner_core']
    #
    print("avilable atmosphere  models:",nuda.eos.available_modelsi('atmosphere'),"\n")
    print("avilable outer_crusr models:",nuda.eos.available_modelsi('outer_crust'),"\n")
    print("avilable inner_crust models:",nuda.eos.available_modelsi('inner_crust'),"\n") 
    pprint(nuda.eos.available_modelsi('outer_core'),indent=1, compact=True, width=150, sort_dicts=True)
    pprint(nuda.eos.available_modelsi('inner_core'), sort_dicts=True)
    
    
    #
    # ==============
    # show dictionnary file
    # ==============
    #
    
    #
    print(50*'-')
    print("Exit eos_Layers_info_script.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()

