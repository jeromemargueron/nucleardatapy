
import nucleardatapy as nuda
import numpy as np

print(nuda.__file__)

def main():
    #
    print(50*'-')
    print("Enter eps_Layers_info_script.py:")
    print(50*'-')
    #
    # ==============
    # Show the models available for the different layers
    # ==============
    #
    #['atmosphere', 'outer_crust', 'inner_crust', 'outer_core', 'inner_core']
    #
    print("available atmosphere  models:",nuda.eos.available_modelsi('atmosphere'),"\n")
    print("available outer crust models:",nuda.eos.available_modelsi('outer_crust'),"\n")
    print("available inner crust models:",nuda.eos.available_modelsi('inner_crust'),"\n") 
    print("available outer core  models:",nuda.eos.available_modelsi('outer_core'),"\n")
    print("available inner core  models:",nuda.eos.available_modelsi('inner_core'),"\n")    
    #
    print(50*'-')
    print("Exit eos_Layers_info_script.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()

