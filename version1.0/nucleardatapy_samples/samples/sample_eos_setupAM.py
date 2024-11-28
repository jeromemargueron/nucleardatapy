
import os
import sys
import numpy as np

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    asy = 0.25
    print(50*'-')
    print("Enter sample_eos_setupAM.py:")
    print("for asymmetry parameter: asy=",asy)
    print(50*'-')
    #
    # ==============
    # micro models
    # ==============
    #
    models, models_lower = nuda.eos.micro_esym_models()
    models.remove('1998-VAR-AM-APRfit')
    models_lower.remove('1998-var-am-aprfit')
    #models = [ '1998-VAR-AM-APR' ]
    #
    for model in models:
        #
        mic = nuda.eos.setupAM( model = model, kind='micro', asy = asy )
        if nuda.env.verb_output: mic.print_outputs( )
    #
    # ==============
    # pheno models
    # ==============
    #
    models, models_lower = nuda.eos.pheno_esym_models()
    #
    for model in models:
        #
        params, params_lower = nuda.eos.pheno_esym_params( model = model )
        #
        for param in params:
            #
            pheno = nuda.eos.setupAM( model = model, param = param, kind='pheno', asy = asy )
            if nuda.env.verb_output: pheno.print_outputs( )
    #
    print(50*'-')
    print("Exit sample_eos_setupAM.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
