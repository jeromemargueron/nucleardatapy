
import os
import sys
import numpy as np

# nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
# sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_nuc_setupNeutronSkinTheo.py:")
    print(50*'-')
    #
    #models, models_lower = nudy.models_pheno()
    models = [ 'Skyrme', 'NLRH', 'DDRH' ]
    nuclei = ['48Ca', '208Pb']
    #
    for model in models:
        #
        params, params_lower = nuda.nskin_theo_params( model = model )
                #
        for param in params:
            for nucleus in nuclei:
             #
             if nuda.env.verb: print('in Sample: model, param, nucleus',model,param,nucleus)
             val = nuda.SetupNeutronSkinTheo( model = model, param = param, nucleus = nucleus )
             if nuda.env.verb_output: val.print_outputs( )
             
    #
    print(50*'-')
    print("Exit sample_nuc_setupNeutronSkinThe.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
