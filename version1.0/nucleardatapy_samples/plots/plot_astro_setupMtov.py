
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
#plt.rcParams.update({'font.size': 16})

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plot_astro_setupMtov( pname, sources_do, sources_up ):
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
    axs.set_ylim([0.0, 1.0])
    #
    prob = nuda.astro.setupMtov( sources_do, sources_up )
    #
    for ind,source in enumerate(sources_do):
        #
        print(f'source: {source}')
        axs.plot(prob.mass, prob.proba_do[ind], label=prob.label_do[ind], color=nuda.param.col[ind], linestyle='dashed', linewidth = 1 )
        #
    axs.plot(prob.mass, prob.proba_do_tot, label=prob.label_do_tot, marker = 'o', markevery=10, color=nuda.param.col[0], linestyle='None' )
    #
    for ind,source in enumerate(sources_up):
        #
        print(f'source: {source}')
        axs.plot(prob.mass, prob.proba_up[ind], label=prob.label_up[ind], color=nuda.param.col[ind], linestyle='dotted', linewidth = 1 )
        #
    axs.plot(prob.mass, prob.proba_up_tot, label=prob.label_up_tot, marker = 's', markevery=10, color=nuda.param.col[0], linestyle='None' )
    #
    axs.plot(prob.mass, prob.proba_tot, label=prob.label_tot, color=nuda.param.col[0], linestyle='solid', linewidth = 3 )
    #
    #axs.legend( loc='upper left',fontsize='8', ncol=1 )
    axs.legend(loc='lower center',bbox_to_anchor=(0.5,1.01),columnspacing=2,fontsize='8',ncol=4,frameon=False)
    #
    plt.savefig(pname)
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
    sources_do = nuda.astro.masses_sources( )[0]
    print('Complete list of available sources_do:',sources_do)
    #
    sources_do = [ 'J1614–2230', 'J0348+0432', 'J2215+5135', 'J1600+3053', 'J0740+6620' ]
    #sources_do = [ 'J1614–2230', 'J0348+0432', 'J2215+5135', 'J0740+6620' ]
    #
    print('sources_low considered:',sources_do)
    #
    # sources up
    #
    sources_up = nuda.astro.mup_sources( )[0]
    print('Complete list of available sources_up:',sources_up)
    #
    #sources_up = [ 'GW170817', 'GW190814' ]
    #
    print('sources_up considered:',sources_up)
    #
    # plot the results:
    #
    pname = 'figs/plot_astro_setupMtov.png'
    plot_astro_setupMtov( pname, sources_do, sources_up )
    #
    print(50*'-')
    print("Exit plot_astro_setupMtov.py:")
    print(50*'-')
    #

if __name__ == "__main__":
    main()
