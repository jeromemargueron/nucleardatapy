
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter matter_setupFFGNuc_script.py:")
    print(50*'-')
    #
    den = 0.01+0.02*np.arange(20)
    #den = np.array([0.01, 0.02, 0.03])
    delta = np.zeros(den.size)
    ffg = nuda.matter.setupFFGNuc( den = den, delta = delta )
    #ffg = nuda.matter.setupFFGNuc( den = den, delta = delta, ms = 1.0 )
    if nuda.env.verb_output: ffg.print_outputs( )
    print('e2a:',ffg.e2a)
    #
    print(50*'-')
    print("Exit matter_setupFFGNuc_script.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
