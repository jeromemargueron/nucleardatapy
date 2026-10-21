
import nucleardatapy as nuda
import numpy as np

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
    print("avilable atmosphere  models:",nuda.eos.available_models('atmosphere'),"\n")
    print("avilable outer_crusr models:",nuda.eos.available_models('outer_crust'),"\n")
    print("avilable inner_crust models:",nuda.eos.available_models('inner_crust'),"\n") 
    print("avilable outer core  models:",nuda.eos.available_models('outer_core'),"\n")
    print("avilable inner core  models:",nuda.eos.available_models('inner_core'),"\n")
    
    
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

