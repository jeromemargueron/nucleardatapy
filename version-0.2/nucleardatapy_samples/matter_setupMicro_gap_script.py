
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter matter_setupMicro_gap_script.py:")
    print(50*'-')
    #
    models, models_lower, models_all, models_all_lower = nuda.matter.micro_gap_models( matter = 'SM' )
    #
    for model in models:
        #
        gap = nuda.matter.setupMicroGap( model = model, matter = 'NM' )
        if nuda.env.verb_output: gap.print_outputs( )
    #
    print(50*'-')
    print("Exit matter_setupMicro_gap_script.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
