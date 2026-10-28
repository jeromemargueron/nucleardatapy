import nucleardatapy as nuda
import numpy as np
import os
import h5py
import matplotlib.pyplot as plt



def main_without_full_outputs():
    #
    print(50*'-')
    print("Enter in function 'without_full_outputs' of eos_setupCSEoS_with_a_outercore_from_nucleardatapy_and_extrapolation.py:")
    print(50*'-')
    
    print("Run nuda.eos.available_modelsi('outer_core') to see the available models")
    
    eos_object = {"outer_core": {"model": "2019-l59",
                                "function": "random_speed_of_sound",
                                "parameters": {"den_tr":0.2,"den_max":2.,"seed":129}}}                                
    

    eos=nuda.eos.setupCSEoS(eos_object=eos_object,full_outputs=False)     
   
    eos.print_outputs()
    
       
    print(50*'-')
    print("Exit from function 'without_full_outputs' of eos_setupCSEoS_with_a_outercore_from_nucleardatapy_and_extrapolation.py")
    print(50*'-')

def main_with_full_outputs():
    #
    print(50*'-')
    print("Enter in function 'with_full_outputs' of eos_setupCSEoS_with_a_outercore_from_nucleardatapy_and_extrapolation.py:")
    print(50*'-')   
    
    eos_object = {"outer_core": {"model": "2019-l59",
                                "function": "random_speed_of_sound", 
                                "parameters": {"den_tr":0.2,"den_max":2.,"seed":129}}} 
                                
    # if you do not give den_tr : the code uses den_tr = max(densities available in the "model" here it is 2019-l59) 
    # if you  give a den_tr  : then the code uses den_tr = min(given den_tr, max(densities available in the "model" here it is 2019-l59))
    # Every different seed generates a new EoS or not fixing the seed will generate a new EoS in every run

    eos=nuda.eos.setupCSEoS(eos_object=eos_object,full_outputs=True)     
   
    eos.print_outputs()
    
     
    
    # In case we need the other datas, for example we can take all the available data fro the inner_crust model as
    #print(eos.data_after_eos_construction['inner_crust'])
    
    print("randomly generated densities:")
    print( eos.den_random_extrapolation)
    print("randomly generated c^2_s at the randomly generated densities:")
    print(eos.cs2_random_extrapolation)
    print("The thermodynamic quantities at   transition point are:")
    print(f"den_tr: {eos.den_tr}  {eos.den_unit}")
    print(f"pre_tr: { eos.pre_tr}  {eos.pre_unit}" )
    print(f"eps_tr: { eos.eps_tr}  {eos.eps_unit}")
    print(f"cs2_tr: { eos.cs2_tr} {eos.cs2_unit}")
    
    
    print(50*'-')
    print("Exit from function 'with_full_outputs' of eos_setupCSEoS_with_a_outercore_from_nucleardatapy_and_extrapolation.py:")
    print(50*'-')
    #










if __name__ == "__main__":
    main_without_full_outputs()
    main_with_full_outputs()
   
    

