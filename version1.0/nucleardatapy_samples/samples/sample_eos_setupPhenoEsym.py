
import os
import sys
import numpy as np

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_eos_setupPhenoEsym.py:")
    print(50*'-')
    #
    #models, models_lower = nuda.eos_pheno_esym_models()
    models = [ 'Skyrme', 'ESkyrme', 'NLRH', 'DDRH', 'DDRHF' ]
    #
    for model in models:
        #
        params, params_lower = nuda.eos.pheno_params( model = model )
        #
        for param in params:
            #
            print('in Sample: model, param',model,param)
            pheno = nuda.eos.setupPhenoEsym( model = model, param = param )
            if nuda.env.verb_output: pheno.print_outputs( )
            #
        #
    #
    print(50*'-')
    print("Exit sample_eos_setupPhenoEsym.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
