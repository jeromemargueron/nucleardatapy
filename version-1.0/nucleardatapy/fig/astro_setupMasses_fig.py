import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def astro_setupMasses_fig( pname, sources ):
    """
    Plot Masses for massives neutron stars as a function of sources.\
    The plot is 1x1 with:\
    [0]: masses versus sources.

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
    fig.subplots_adjust(left=0.12, bottom=0.12, right=0.95, top=0.75, wspace=0.3, hspace=0.3)
    #
    axs.set_ylabel(r'M (M$_\odot$)',fontsize='14')
    axs.set_xlabel(r'sources',fontsize='14')
    axs.set_ylim([1.7, 3.5])
    axs.set_xlim([0.8, 5.5])
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
        obss = nuda.astro.masses_obss( source = source )
        print(f'source: {source}, obss: {obss}')
        #
        iobs = 0
        for obs in obss:
            m = nuda.astro.setupMasses( source = source, obs = obs )
            if nuda.env.verb_output: m.print_output( )
            if nuda.env.verb_latex: m.print_latex( )
            axs.errorbar( isource+iobs/10, m.mass, yerr=np.array([(m.sig_lo,m.sig_up)]).T, label=m.label, color=nuda.param.col[isource], marker='s', linestyle = 'solid', linewidth = 1 )
            iobs += 1
            #
        mav = nuda.astro.setupMassesAverage( source = source )
        if nuda.env.verb_output: mav.print_output( )
        if nuda.env.verb_latex: mav.print_latex( )
        axs.errorbar( isource+iobs/10, mav.mass_cen, yerr=mav.sig_std, label=mav.label, color=nuda.param.col[isource], marker='o', linestyle = 'solid', linewidth = 3 )
        isource += 1
    #
    axs.set_xticks( ilabel )
    axs.set_xticklabels( xlabel )
    #axs.legend(loc='upper left',fontsize='8', ncol=2)
    axs.legend(loc='lower center',bbox_to_anchor=(0.5,1.01),columnspacing=2,fontsize='8', ncol=3,frameon=False)
    #
    if pname is not None:
    	plt.savefig(pname, dpi=200)
    	plt.close()
    #
