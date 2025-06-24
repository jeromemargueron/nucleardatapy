import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def astro_setupGW_fig( pname, sources ):
    """
    Plot Tidal deformabilities for each sources.\
    The plot is 1x1 with:\
    [0]: Tidal deformabilities versus sources.

    :param pname: name of the figure (*.png)
    :type pname: str.
    :param sources: array of sources names.
    :type sources: array of str.

    """
    #
    print(f'Plot name: {pname}')
    #
    # plot Lambda versus sources
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.14, bottom=0.12, right=0.95, top=0.85, wspace=0.3, hspace=0.3)
    #
    axs.set_xlabel(r'sources',fontsize='14')
    axs.set_ylabel(r'$\tilde{\Lambda}_{90\%}$',fontsize='14')
    axs.set_xlim([0.8, 2.5])
    axs.set_ylim([0, 1200])
    #
    isource = 1
    xlabel = []
    ilabel = []
    for source in sources:
        xlabel.append( source )
        ilabel.append( isource )
        #
        # get the mass associated to `source` and `obs`
        #
        hyps = nuda.astro.gw_hyps( source = source )
        print('obss:',hyps)
        #
        ihyp = 0
        for hyp in hyps:
            gw = nuda.astro.setupGW( source = source, hyp = hyp )
            if nuda.env.verb_output: gw.print_output( )
            if nuda.env.verb_latex: gw.print_latex( )
            axs.errorbar( isource+ihyp/10, gw.lam, yerr=np.array([(gw.lam_sig_lo,gw.lam_sig_up)]).T, label=gw.label, color=nuda.param.col[isource], marker=gw.marker, linestyle = 'solid', linewidth = 1 )
            ihyp += 1
            #
        gwav = nuda.astro.setupGWAverage( source = source )
        if nuda.env.verb_output: gwav.print_output( )
        if nuda.env.verb_latex: gwav.print_latex( )
        axs.errorbar( isource+ihyp/10, gwav.lam_cen, yerr=gwav.lam_sig_std, ms=12, label=gwav.label, color=nuda.param.col[isource], marker='^', linestyle = 'solid', linewidth = 3 )
        #
        isource += 1
    #
    axs.set_xticks( ilabel )
    axs.set_xticklabels( xlabel )
    axs.legend(loc='lower center',bbox_to_anchor=(0.5,1.01),columnspacing=2,fontsize='8', ncol=3,frameon=False)
    #
    #
    if pname is not None:
    	plt.savefig(pname, dpi=200)
    	plt.close()
    #