
import os
import sys
import numpy as np

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_matter_setupMicro.py:")
    print(50*'-')
    #
    models, models_lower = nuda.matter.micro_models()
    print('models:',models)
    #
    for model in models:
        #
        print('model:',model)
        mic = nuda.matter.setupMicro( model = model )
        if nuda.env.verb_output: mic.print_outputs( )
    #
    print(50*'-')
    print("Exit sample_matter_setupMicro.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
