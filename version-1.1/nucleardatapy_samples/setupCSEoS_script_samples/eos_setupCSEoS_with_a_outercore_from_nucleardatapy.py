import nucleardatapy as nuda
import numpy as np

import matplotlib.pyplot as plt



def main_without_full_outputs():
    #
    print(50*'-')
    print("Enter in function 'without_full_outputs' of eos_setupEoS_with_a_outercore_from_nucleardatapy.py:")
    print(50*'-')
    
    print("Run nuda.eos.available_modelsi('outer_core') to see the available models")
    
    eos_object={"outer_core":"2019-l59"} 
    # you can also use 2019-L59. the code is not sensitive to the lowercase or uppercase name. bsk14=BSK14=bSk14 : the code will work always 
    # If you prefer you can also pass the outer_core as a dict {"outer_core":{"model":"2019-l59"}} 
    
    eos=nuda.eos.setupCSEoS(eos_object=eos_object)
    eos.print_outputs()
    
    print(50*'-')
    print("Exit from function 'without_full_outputs' of eos_setupCSEoS_with_a_outercore_from_nucleardatapy.py:")
    print(50*'-')

def main_with_full_outputs():
    #
    print(50*'-')
    print("Enter in function 'with_full_outputs' of eos_setupCSEoS_with_a_outercore_from_nucleardatapy.py:")
    print(50*'-')   
    
    eos_object={"outer_core":{"model":"2019-l59"}}

    eos=nuda.eos.setupCSEoS(eos_object=eos_object,full_outputs=True)
    eos.print_outputs()
    
    # In case we need the other datas, for example we can take all the available data fro the inner_crust model as
    #print(eos.data_after_eos_construction['inner_crust'])
    
    print(50*'-')
    print("Exit from function 'with_full_outputs' of eos_setupCSEoS_with_a_outercore_from_nucleardatapy.py:")
    print(50*'-')
    #


if __name__ == "__main__":
    main_without_full_outputs()
    main_with_full_outputs()
    

