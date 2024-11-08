
import os
import sys
import numpy as np

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_SetupMicroMatter.py:")
    print(50*'-')
    #
    models, models_lower = nuda.models_micro_matter()
    #
    for model in models:
        #
        mic = nuda.SetupMicroMatter( model = model )
        mic.print_outputs( )
    #
    print(50*'-')
    print("Exit sample_SetupMicroMatter.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
