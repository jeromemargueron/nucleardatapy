
import os
import sys
import numpy as np

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_matter_setupMicroLP.py:")
    print(50*'-')
    #
    models, models_lower = nuda.matter.micro_LP_models()
    #
    for model in models:
        #
        print('Model:',model)
        lp = nuda.matter.setupMicroLP( model = model )
        print('LP in SM:')
        print('kfn:',lp.sm_kfn)
        print('F0:',lp.sm_LP['F'][0])
        print('G0:',lp.sm_LP['G'][0])
        print('LP in NM:')
        print('kfn:',lp.nm_kfn)
        print('F0:',lp.nm_LP['F'][0])
        print('G0:',lp.nm_LP['G'][0])
        if nuda.env.verb_output: lp.print_outputs( )
    #
    print(50*'-')
    print("Exit sample_matter_setupMicroLP.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
