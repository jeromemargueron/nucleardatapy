
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter matter_setupFFGLep_script.py:")
    print(50*'-')
    #
    den_el = np.linspace(0.001,0.1,num=20)
    den_mu = 0.1 * den_el
    lep = nuda.matter.setupFFGLep( den_el = den_el, den_mu = den_mu )
    if nuda.env.verb_output: lep.print_outputs( )
    print('e2n_el:',lep.e2n_el)
    print('kf_el:',lep.kf_el)
    print('e2n_mu:',lep.e2n_mu)
    print('kf_mu:',lep.kf_mu)
    #
    print(50*'-')
    print("Exit matter_setupFFGLep_script.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
