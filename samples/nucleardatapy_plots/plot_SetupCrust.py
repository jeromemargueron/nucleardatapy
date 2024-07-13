
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plot_crust( pname, modcrusts ):
    #
    # plot E/A and Z in crust
    #
    print(f'Plot name: {pname}')
    #
    fig, axs = plt.subplots(1,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.10, bottom=0.12, right=None, top=0.98, wspace=0.3, hspace=0.3 )
    #
    axs[0].set_xlabel(r'n (fm$^{-3}$)')
    axs[0].set_ylabel(r'$e_{int}(n)$')
    axs[0].set_xlim([1e-4, 1e-1])
    axs[0].set_ylim([-2, 10])
    axs[0].set_xscale('log')
    #
    axs[1].set_xlabel(r'n (fm$^{-3}$)')
    axs[1].set_ylabel(r'$Z$')
    axs[1].set_xlim([1e-4, 1e-1])
    axs[1].set_ylim([0, 60])
    axs[1].set_xscale('log')
    #
    for modcrust in modcrusts:
        #
        crust = nuda.SetupCrust( modcrust = modcrust )
        if crust.e2a_int is not None: 
            axs[0].plot( crust.den, crust.e2a_int, label=crust.label )
        if crust.Z is not None: 
            axs[1].plot( crust.den, crust.Z, label=crust.label )
    axs[0].legend(loc='upper left',fontsize='8', ncol=1)
    axs[1].legend(loc='upper left',fontsize='8', ncol=1)
    #
    plt.savefig(pname)
    plt.close()

def main():
    #
    print(50*'-')
    print("Enter plot_SetupCrust.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    # list the available models
    #
    modcrusts, modcrusts_lower = nuda.models_crust()
    #
    # plot crust
    #
    pname = 'figs/plot_SetupCrust.png'
    plot_crust( pname, modcrusts )
    #
    print(50*'-')
    print("Exit plot_SetupCrust.py:")
    print(50*'-')
    #

    
if __name__ == "__main__":
    main()
