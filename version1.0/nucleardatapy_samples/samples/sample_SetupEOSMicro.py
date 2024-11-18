
import os
import sys
import numpy as np

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_SetupEOSMicro.py:")
    print(50*'-')
    #
    models, models_lower = nuda.eos_micro_models()
    #
    for model in models:
        #
        mic = nuda.SetupEOSMicro( model = model )
        mic.print_outputs( )
    #
    print(50*'-')
    print("Exit sample_SetupEOSMicro.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
