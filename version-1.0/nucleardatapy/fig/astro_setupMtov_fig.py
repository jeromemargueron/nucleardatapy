import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def astro_setupMtov_fig( pname, sources_lo_all, sources_lo_dist, sources_up1, sources_up2, sources_up3 ):
    """
    Plot the distribution of maximum masses.\
    The plot is 1x1 with:\
    [0]: distribution of maximum mass versus maximum mass.

    :param pname: name of the figure (*.png)
    :type pname: str.
    :param sources_lo_all: array of all sources (low boundaries).
    :type sources_lo_all: array of str.
    :param sources_lo_dist: array of sources considered for the distribution (low boundaries).
    :type sources_lo_dist: array of str.
    :param sources_up1: array of sources (up boundaries).
    :type sources_up1: array of str.
    :param sources_up2: array of sources (up boundaries).
    :type sources_up2: array of str.
    :param sources_up3: array of sources (up boundaries).
    :type sources_up3: array of str.

    """
    #
    print(f'Plot name: {pname}')
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=0.95, top=0.9, wspace=0.3, hspace=0.3)
    #
    axs.set_xlabel(r'M$_\mathrm{tov}$ (M$_\odot$)',fontsize='14')
    axs.set_ylabel(r'probability (non-normalised)',fontsize='14')
    axs.set_xlim([1.6, 3.4])
    axs.set_ylim([0.0, 1.03])
    #
    sources_lo_nondist = []
    for source in sources_lo_all:
        if source not in sources_lo_dist:
            sources_lo_nondist.append(source)
    print('sources removed from distribution:',sources_lo_nondist)
    #
    prob0 = nuda.astro.setupMtov( sources_lo_nondist, sources_up1 )
    prob1 = nuda.astro.setupMtov( sources_lo_dist, sources_up1 )
    prob2 = nuda.astro.setupMtov( sources_lo_dist, sources_up2 )
    prob3 = nuda.astro.setupMtov( sources_lo_dist, sources_up3 )
    #
    for ind,source in enumerate(sources_lo_nondist):
        #
        print(f'source: {source}')
        axs.plot(prob0.mass, prob0.proba_lo[ind], label=prob0.label_lo[ind], color=nuda.param.col[ind], linestyle='dotted', linewidth = 1 )
        #
    for ind,source in enumerate(sources_lo_dist):
        #
        print(f'source: {source}')
        axs.plot(prob1.mass, prob1.proba_lo[ind], label=prob1.label_lo[ind], color=nuda.param.col[ind], linestyle='dashed', linewidth = 3 )
        #
    #axs.plot(prob1.mass, prob1.proba_lo_tot, label=prob1.label_lo_tot, marker = 'o', markevery=4, color=nuda.param.col[0], linestyle='None' )
    #
    for ind,source in enumerate(sources_up1):
        #
        print(f'source: {source}')
        axs.plot(prob1.mass, prob1.proba_up[ind], label=prob1.label_up[ind], color=nuda.param.col[ind], linestyle='dotted', linewidth = 3 )
        #
    #axs.plot(prob1.mass, prob1.proba_up_tot, label=prob1.label_up_tot, marker = 's', markevery=4, color=nuda.param.col[4], linestyle='None' )
    #axs.plot(prob2.mass, prob2.proba_up_tot, label=prob2.label_up_tot, marker = 'v', markevery=7, color=nuda.param.col[5], linestyle='None' )
    #axs.plot(prob3.mass, prob3.proba_up_tot, label=prob3.label_up_tot, marker = '^', markevery=10, color=nuda.param.col[6], linestyle='None' )
    #
    axs.plot(prob1.mass, prob1.proba_tot, label=prob1.label_tot+' case 1', marker = 's', markevery=4, color=nuda.param.col[4], linestyle='None' )
    axs.plot(prob2.mass, prob2.proba_tot, label=prob2.label_tot+' case 2', marker = 'v', markevery=5, color=nuda.param.col[5], linestyle='None' )
    axs.plot(prob3.mass, prob3.proba_tot, label=prob3.label_tot+' case 3', marker = '^', markevery=7, color=nuda.param.col[6], linestyle='None' )
    #
    #axs.plot(prob1.mass, prob1.proba_tot, label=prob1.label_tot, color=nuda.param.col[4], linestyle=(1, (2, 10)), linewidth = 3 )
    #axs.plot(prob2.mass, prob2.proba_tot, label=prob2.label_tot, color=nuda.param.col[4], linestyle=(1, (3, 9)), linewidth = 3 )
    #axs.plot(prob3.mass, prob3.proba_tot, label=prob3.label_tot, color=nuda.param.col[4], linestyle=(1, (4, 8)), linewidth = 3 )
    #
    #axs.legend( loc='upper left',fontsize='8', ncol=1 )
    axs.legend(loc='lower center',bbox_to_anchor=(0.5,1.01),columnspacing=2,fontsize='8',ncol=5,frameon=False)
    #
    if pname is not None:
    	plt.savefig(pname, dpi=200)
    	plt.close()
    #
