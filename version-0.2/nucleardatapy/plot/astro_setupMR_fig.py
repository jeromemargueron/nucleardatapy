import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def astro_setupMR_fig( pname, sources, sources_av ):
    """
    Plot M-R constraints from NICER analyses.\
    The plot is 1x1 with:\
    [0]: Masses versus radii.

    :param pname: name of the figure (*.png)
    :type pname: str.
    :param sources: array of sources.
    :type sources: array of str.
    :param sources_av: .
    :type sources_av: .

    """
    #
    print(f'Plot name: {pname}')
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.85, wspace=0.3, hspace=0.3)
    #
    axs.set_xlabel(r'$R$ (km)',fontsize='12')
    axs.set_ylabel(r'M (M$_\odot$)',fontsize='12')
    axs.set_xlim([10.5, 16.5])
    axs.set_ylim([1.15, 2.2])
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
        obss = nuda.astro.mr_obss( source = source )
        print(f'source: {source}, obss: {obss}')
        #
        iobs = 0
        for obs in obss:
            mr = nuda.astro.setupMR( source = source, obs = obs )
            if nuda.env.verb_output: mr.print_output( )
            if nuda.env.verb_table: mr.print_table( )
            if source.lower() == 'j0030+0451' and obs == 3:
                axs.errorbar( mr.rad, mr.mass, xerr=np.array([(mr.rad_sig_do,mr.rad_sig_up)]).T, yerr=np.array([(mr.mass_sig_do,mr.mass_sig_up)]).T, label=mr.label, color=nuda.param.col[isource], marker=mr.marker, linewidth = 1 )
            elif source.lower() == 'j0030+0451' and obs == 4:
                axs.errorbar( mr.rad, mr.mass, xerr=np.array([(mr.rad_sig_do,mr.rad_sig_up)]).T, yerr=np.array([(mr.mass_sig_do,mr.mass_sig_up)]).T, label=mr.label, color=nuda.param.col[isource], marker=mr.marker, linewidth = 1 )
            else:
                axs.errorbar( mr.rad, mr.mass, xerr=np.array([(mr.rad_sig_do,mr.rad_sig_up)]).T, yerr=np.array([(mr.mass_sig_do,mr.mass_sig_up)]).T, label=mr.label, color=nuda.param.col[isource], marker=mr.marker, linewidth = 1 )
            iobs += 1
            #
        isource += 1
        #
    isource = 1
    for source in sources_av:
        if source.lower() == 'j0030+0451': obss = [ 1, 2 ]
        if source.lower() == 'j0740+6620': obss = [ 1, 2 ]
        mrav = nuda.astro.setupMRAverage( source = source, obss = obss )
        if nuda.env.verb_output: mrav.print_output( )
        if nuda.env.verb_table: mrav.print_table( )
        axs.errorbar( mrav.rad_cen, mrav.mass_cen, xerr=mrav.rad_sig_std, yerr=mrav.mass_sig_std, ms=12, label=mrav.label, color=nuda.param.col[isource], marker='^', linestyle = 'solid', linewidth = 3 )
        isource += 1
    #
    #axs.legend(loc='upper left',fontsize='8', ncol=2)
    axs.legend(loc='lower center',bbox_to_anchor=(0.48,1.01),columnspacing=2,fontsize='8',ncol=3,frameon=False)
    #
    if pname is not None:
    	plt.savefig(pname, dpi=200)
    	plt.close()
    #