
import os
import sys
import numpy as np

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_SetupEOSMicroLP.py:")
    print(50*'-')
    #
    models, models_lower = nuda.eos_micro_LP_models()
    #
    for model in models:
        #
        mic = nuda.SetupEOSMicroLP( model = model )
        mic.print_outputs( )
    #
    print(50*'-')
    print("Exit sample_SetupEOSMicroLP.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
