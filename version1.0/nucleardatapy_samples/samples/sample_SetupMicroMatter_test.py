
import os
import sys
import numpy as np

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_SetupMicroMatter.py:")
    print(50*'-')
    #
    #models = [ '1981-VAR-AM-FP' ]
    #models = [ '1998-VAR-AM-APR' ]
    models = [ '1998-VAR-AM-APRfit' ]
    #models = [ '2010-QMC-NM-AV4' ]
    #models = [ '2012-AFDMC-NM-2' ]
    #models = [ '2016-MBPT-AM' ]
    #models = [ '2020-MBPT-AM-DHSL59' ]
    #models = [ '2020-MBPT-AM-DHSL69' ]
    #models = [ '2023-MBPT-AM' ]
    #models = [ '2024-NLEFT-AM' ]
    #models = [ '2024-bhf-am-2bf-av8p' ]
    #models = [ '2024-bhf-am-2bf-av18' ]
    #models = [ '2024-bhf-am-2bf-BONN' ]
    #models = [ '2024-bhf-am-2bf-CDBONN' ]
    #models = [ '2024-bhf-am-2bf-SSCV14' ]
    #models = [ '2024-bhf-am-2bf-NSC97a' ]
    #models = [ '2024-bhf-am-2bf-NSC97b' ]
    #models = [ '2024-bhf-am-2bf-NSC97c' ]
    #models = [ '2024-bhf-am-2bf-NSC97d' ]
    #models = [ '2024-bhf-am-2bf-NSC97e' ]
    #models = [ '2024-bhf-am-2bf-NSC97f' ]
    #models = [ '2024-bhf-am-23bf-av8p' ]
    #models = [ '2024-bhf-am-23bf-av18' ]
    #models = [ '2024-bhf-am-23bf-BONN' ]
    #models = [ '2024-bhf-am-23bf-CDBONN' ]
    #models = [ '2024-bhf-am-23bf-SSCV14' ]
    #models = [ '2024-bhf-am-23bf-NSC97a' ]
    #models = [ '2024-bhf-am-23bf-NSC97b' ]
    #models = [ '2024-bhf-am-23bf-NSC97c' ]
    #models = [ '2024-bhf-am-23bf-NSC97d' ]
    #models = [ '2024-bhf-am-23bf-NSC97e' ]
    #models = [ '2024-bhf-am-23bf-NSC97f' ]
    #
    for model in models:
        #
        mic = nuda.SetupMicroMatter( model = model )
        if nuda.env.verb_output: mic.print_outputs( )
    #
    print(50*'-')
    print("Exit sample_SetupMicroMatter.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
