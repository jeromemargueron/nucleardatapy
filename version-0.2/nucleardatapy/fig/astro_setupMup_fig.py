import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def astro_setupMup_fig( pname, sources ):
    """
    Plot upper boundaries for the tov mass.\
    The plot is 1x1 with:\
    [0]: upper boundary for the mass versus sources.

    :param pname: name of the figure (*.png)
    :type pname: str.
    :param sources: array of sources.
    :type sources: array of str.

    """
    #
    print(f'Plot name: {pname}')
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=0.95, top=0.85, wspace=0.3, hspace=0.3)
    #
    axs.set_xlabel(r'sources',fontsize='14')
    axs.set_ylabel(r'M (M$_\odot$)',fontsize='14')
    axs.set_xlim([0.8, 2.5])
    axs.set_ylim([2.4, 3.4])
    #
    isource = 1
    xlabel = []
    ilabel = []
    for source in sources:
        xlabel.append( source )
        ilabel.append( isource )
        #
        # get mup associated to `source` and `hyp`
        #
        hyps = nuda.astro.mup_hyps( source = source )
        print('source:',source)
        print('hyps:',hyps)
        #
        ihyp = 0
        for hyp in hyps:
            mup = nuda.astro.setupMup( source = source, hyp = hyp )
            if nuda.env.verb_output: mup.print_output( )
            if nuda.env.verb_latex: mup.print_latex( )
            axs.errorbar( isource+ihyp/10, mup.mup, yerr=np.array([(mup.sig_lo,mup.sig_up)]).T, label=mup.label, color=nuda.param.col[isource], marker=mup.marker, linestyle = 'solid', linewidth = 1 )
            ihyp += 1
            #
        if source=='GW170817': hyps = [ 3, 4 ]
        mupav = nuda.astro.setupMupAverage( source = source, hyps = hyps )
        if nuda.env.verb_output: mupav.print_output( )
        if nuda.env.verb_latex: mupav.print_latex( )
        axs.errorbar( isource+ihyp/10, mupav.mup_cen, yerr=mupav.sig_std, label=mupav.label, color=nuda.param.col[isource], marker='o', linestyle = 'solid', linewidth = 3 )
        #
        isource += 1
    #
    axs.set_xticks( ilabel )
    axs.set_xticklabels( xlabel )
    #
    #axs.legend(loc='upper left',fontsize='8', ncol=2)
    axs.legend(loc='lower center',bbox_to_anchor=(0.5,1.01),columnspacing=2,fontsize='8',ncol=3,frameon=False)
    #
    if pname is not None:
    	plt.savefig(pname, dpi=200)
    	plt.close()
    #