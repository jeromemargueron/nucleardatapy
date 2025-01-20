
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def plot_matter_setupNEPModelDist( pname, models ):
    #
    # plot sat in the left and sym on the right
    #
    print(f'Plot name: {pname}')
    #
    # Set figure
    #
    fig, axs = plt.subplots(5,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.06, right=None, top=0.9, wspace=0.3, hspace=0.4 )
    #
    axs[0,0].set_ylabel(r'$E_{sat}$')
    axs[0,0].set_xlim([-16.5, -15])
    axs[1,0].set_ylabel(r'$n_{sat}$')
    axs[1,0].set_xlim([0.14, 0.18])
    axs[2,0].set_ylabel(r'$K_{sat}$')
    axs[2,0].set_xlim([180, 360])
    axs[3,0].set_ylabel(r'$Q_{sat}$')
    axs[3,0].set_xlim([-1000, 1000])
    axs[4,0].set_ylabel(r'$m_{sat}^{*}/m$')
    axs[4,0].set_xlim([0.35, 1.2])
    axs[0,1].set_ylabel(r'$E_{sym}$')
    axs[0,1].set_xlim([26, 40])
    axs[1,1].set_ylabel(r'$L_{sym}$')
    axs[1,1].set_xlim([0, 120])
    axs[2,1].set_ylabel(r'$K_{sym}$')
    axs[2,1].set_xlim([-400, 220])
    axs[3,1].set_ylabel(r'$Q_{sym}$')
    axs[3,1].set_xlim([-50, 900])
    axs[4,1].set_ylabel(r'$\Delta m_{sat}^{*}/m$')
    axs[4,1].set_xlim([-0.5, 1.1])
    #
    # Built distribution of NEP
    #
    for model in models:
        #
        dist = nuda.matter.setupNEPModelDist( model )
        #
        axs[0,0].hist( dist.Esat, bins=10, label=model )
        axs[1,0].hist( dist.nsat, bins=10 )
        axs[2,0].hist( dist.Ksat, bins=10 )
        axs[3,0].hist( dist.Qsat, bins=10 )
        axs[4,0].hist( dist.msat, bins=10 )
        axs[0,1].hist( dist.Esym, bins=10 )
        axs[1,1].hist( dist.Lsym, bins=10 )
        axs[2,1].hist( dist.Ksym, bins=10 )
        axs[3,1].hist( dist.Qsym, bins=10 )
        axs[4,1].hist( dist.Dmsat, bins=10 )
    #
    #axs[0,0].legend(loc='lower right',fontsize='10',ncol=2)
    fig.legend(loc='upper left',bbox_to_anchor=(0.01,0.98),columnspacing=2,fontsize='8',ncol=7,frameon=False)
    #
    plt.savefig(pname)
    plt.close()

def main():
    #
    print(50*'-')
    print("Enter plot_matter_setupNEPModelDist.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    # list the available models
    #
    #models = [ 'Skyrme', 'ESkyrme', 'Gogny', 'Fayans', 'NLRH', 'DDRH', 'DDRHF' ]
    models, models_lower = nuda.matter.nep_models()
    #
    # plot distribution of NEP
    #
    pname = 'figs/plot_matter_setupNEPModelDist.png'
    plot_matter_setupNEPModelDist( pname, models )
    #
    print(50*'-')
    print("Exit plot_matter_setupNEPModelDist.py:")
    print(50*'-')
    #

    
if __name__ == "__main__":
    main()
