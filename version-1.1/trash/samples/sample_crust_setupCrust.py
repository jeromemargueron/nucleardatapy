
import os
import sys
import numpy as np

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_crust_setupCrust.py:")
    print(50*'-')
    #
    models, models_lower = nuda.crust.crust_models()
    #
    for model in models:
        #
        crust = nuda.crust.setupCrust( model = model )
        if nuda.env.verb_output: crust.print_outputs( )
    #
    print(50*'-')
    print("Exit sample_crust_setupCrust.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
