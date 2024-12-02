
import os
import sys
import numpy as np

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_matter_setupMicroGap.py:")
    print(50*'-')
    #
    models, models_lower = nuda.matter.micro_gap_models()
    #
    for model in models:
        #
        gap = nuda.matter.setupMicroGap( model = model )
        if nuda.env.verb_output: gap.print_outputs( )
    #
    print(50*'-')
    print("Exit sample_matter_setupMicroGap.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
