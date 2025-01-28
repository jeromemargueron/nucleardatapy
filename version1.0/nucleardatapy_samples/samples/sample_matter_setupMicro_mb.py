
import os
import sys
import numpy as np

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_matter_setupMicro_mb.py:")
    print(50*'-')
    #
    # Print the many-body models available:
    #
    mbs, mbs_lower = nuda.matter.micro_mbs()
    print('mbs available:',mbs)
    #
    # select the mb you wish to study
    #
    mb = 'VAR'
    #
    # select the models balonging to this mb
    #
    models, models_lower = nuda.matter.micro_models_mb( mb )
    #
    print('for mb:',mb)
    print('models:',models)
    #
    # or select the mbs you wish to study
    #
    mbs = [ 'VAR', 'QMC' ]
    #
    # select the models balonging to this mb
    #
    models, models_lower = nuda.matter.micro_models_mbs( mbs )
    #
    print('for mbs:',mbs)
    print('models:',models)
    #
    for model in models:
        #
        mic = nuda.matter.setupMicro( model = model )
        if nuda.env.verb_output: mic.print_outputs( )
    #
    print(50*'-')
    print("Exit sample_matter_setupMicro_mb.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
