
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter matter_setupFFGLep_plot.py:")
    print(50*'-')
    #
    den_el = np.linspace(0.001,0.1,num=20)
    den_mu01 = 0.1 * den_el
    den_mu02 = 0.2 * den_el
    den_mu05 = 0.5 * den_el
    #
    pname = 'figs/plot_matter_setupFFGLep.png'
    #
    nuda.fig.matter_setupFFGLep_fig( pname, den_el = den_el, den_mu1 = den_mu01, den_mu2 = den_mu02, den_mu3 = den_mu05 )
    #
    print(50*'-')
    print("Exit matter_setupFFGLep_plot.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
