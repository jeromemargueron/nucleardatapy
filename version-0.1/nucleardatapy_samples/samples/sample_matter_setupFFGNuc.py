
import os
import sys
import numpy as np

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_matter_setupFFGNuc.py:")
    print(50*'-')
    #
    den = 0.01+0.02*np.arange(20)
    delta = np.zeros(den.size)
    ffg = nuda.matter.setupFFGNuc( den = den, delta = delta )
    if nuda.env.verb_output: ffg.print_outputs( )
    #
    print(50*'-')
    print("Exit sample_matter_setupFFGNuc.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
