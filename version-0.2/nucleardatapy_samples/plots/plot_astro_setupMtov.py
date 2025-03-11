
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
#plt.rcParams.update({'font.size': 16})

import nucleardatapy as nuda

def plot_astro_setupMtov( pname, sources_do1, sources_do2, sources_up1, sources_up2, sources_up3 ):
    #
    # plot pdf versus mass
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.85, wspace=0.3, hspace=0.3)
    #
    axs.set_xlabel(r'M$_\mathrm{tov}$ (M$_\odot$)',fontsize='12')
    axs.set_ylabel(r'probability (non-normalised)',fontsize='12')
    axs.set_xlim([1.6, 3.4])
    axs.set_ylim([0.0, 1.03])
    #
    prob0 = nuda.astro.setupMtov( sources_do1, sources_up1 )
    prob1 = nuda.astro.setupMtov( sources_do2, sources_up1 )
    prob2 = nuda.astro.setupMtov( sources_do2, sources_up2 )
    prob3 = nuda.astro.setupMtov( sources_do2, sources_up3 )
    #
    for ind,source in enumerate(sources_do1):
        #
        print(f'source: {source}')
        axs.plot(prob0.mass, prob0.proba_do[ind], label=prob0.label_do[ind], color=nuda.param.col[ind], linestyle='dashed', linewidth = 1 )
        #
    axs.plot(prob1.mass, prob1.proba_do_tot, label=prob1.label_do_tot, marker = 'o', markevery=10, color=nuda.param.col[0], linestyle='None' )
    #
    for ind,source in enumerate(sources_up1):
        #
        print(f'source: {source}')
        axs.plot(prob1.mass, prob1.proba_up[ind], label=prob1.label_up[ind], color=nuda.param.col[ind], linestyle='dotted', linewidth = 1 )
        #
    axs.plot(prob1.mass, prob1.proba_up_tot, label=prob1.label_up_tot, marker = 's', markevery=10, color=nuda.param.col[0], linestyle='None' )
    #
    axs.plot(prob1.mass, prob1.proba_tot, label=prob1.label_tot, color=nuda.param.col[1], linestyle=(1, (2, 10)), linewidth = 3 )
    axs.plot(prob2.mass, prob2.proba_tot, label=prob2.label_tot, color=nuda.param.col[1], linestyle=(1, (3, 9)), linewidth = 3 )
    axs.plot(prob3.mass, prob3.proba_tot, label=prob3.label_tot, color=nuda.param.col[1], linestyle=(1, (4, 8)), linewidth = 3 )
    #
    #axs.legend( loc='upper left',fontsize='8', ncol=1 )
    axs.legend(loc='lower center',bbox_to_anchor=(0.4,1.01),columnspacing=2,fontsize='8',ncol=4,frameon=False)
    #
    plt.savefig(pname, dpi=200)
    plt.close()
    #

def main():
    #
    print(50*'-')
    print("Enter plot_astro_setupMtov.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    # sources low
    #
    sources_do, sources_do_lower = nuda.astro.masses_sources( )
    print('Complete list of available sources_do:',sources_do)
    #
    sources_do1 = [ 'J1614–2230', 'J0348+0432', 'J2215+5135', 'J1600+3053', 'J0740+6620' ]
    sources_do2 = [ 'J1614–2230', 'J0348+0432', 'J0740+6620' ]
    #
    print('sources_low considered:',sources_do2)
    #
    # sources up
    #
    sources_up1, sources_up_lower = nuda.astro.mup_sources( )
    print('Complete list of available sources_up1:',sources_up1)
    #
    sources_up2 = [ 'GW170817' ]
    #
    print('sources_up2 considered:',sources_up2)
    #
    sources_up3 = [ ]
    #
    print('sources_up3 considered:',sources_up3)
    #
    # plot the results:
    #
    pname = 'figs/plot_astro_setupMtov.png'
    plot_astro_setupMtov( pname, sources_do1, sources_do2, sources_up1, sources_up2, sources_up3 )
    #
    print(50*'-')
    print("Exit plot_astro_setupMtov.py:")
    print(50*'-')
    #

if __name__ == "__main__":
    main()
