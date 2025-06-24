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
    fig.subplots_adjust(left=0.12, bottom=0.12, right=0.95, top=0.85, wspace=0.3, hspace=0.3)
    #
    axs.set_xlabel(r'$R$ (km)',fontsize='14')
    axs.set_ylabel(r'M (M$_\odot$)',fontsize='14')
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
            if nuda.env.verb_latex: mr.print_latex( )
            if source.lower() == 'j0030+0451' and obs == 3:
                axs.errorbar( mr.rad, mr.mass, xerr=np.array([(mr.rad_sig_lo,mr.rad_sig_up)]).T, yerr=np.array([(mr.mass_sig_lo,mr.mass_sig_up)]).T, label=mr.label, color=nuda.param.col[isource], marker=mr.marker, linewidth = 1 )
            elif source.lower() == 'j0030+0451' and obs == 4:
                axs.errorbar( mr.rad, mr.mass, xerr=np.array([(mr.rad_sig_lo,mr.rad_sig_up)]).T, yerr=np.array([(mr.mass_sig_lo,mr.mass_sig_up)]).T, label=mr.label, color=nuda.param.col[isource], marker=mr.marker, linewidth = 1 )
            else:
                axs.errorbar( mr.rad, mr.mass, xerr=np.array([(mr.rad_sig_lo,mr.rad_sig_up)]).T, yerr=np.array([(mr.mass_sig_lo,mr.mass_sig_up)]).T, label=mr.label, color=nuda.param.col[isource], marker=mr.marker, linewidth = 1 )
            iobs += 1
            #
        isource += 1
        #
    #isource = 1
    for isource,source in enumerate(sources_av):
        #if source.lower() == 'j0030+0451': 
        #    obss = [ 1, 2 ]
        #if source.lower() == 'j0740+6620': 
        #    obss = [ 1, 2, 3 ]
        obss = nuda.astro.mr_obss( source = source )
        if source.lower() == 'j0030+0451': 
            obss = [ 1, 2 ]
        mrav = nuda.astro.setupMRAverage( source = source, obss = obss )
        if nuda.env.verb_output: mrav.print_output( )
        if nuda.env.verb_latex: mrav.print_latex( )
        axs.errorbar( mrav.rad_cen, mrav.mass_cen, xerr=mrav.rad_sig_std, yerr=mrav.mass_sig_std, ms=12, label=mrav.label, color=nuda.param.col[isource+1], marker='^', linewidth = 3 )
    #
    # write source name in plot:
    #
    for source in sources:
        print('source:',source)
        if source.lower() == 'j0030+0451':
            axs.text(13.3,1.25,'J0030+0451')
        elif source.lower() == 'j0740+6620':
            axs.text(13,1.95,'J0740+6620')
        elif source.lower() == 'j0437-4715':
            axs.text(10.7,1.5,'J0437-4715')
    #
    #axs.legend(loc='upper left',fontsize='8', ncol=2)
    axs.legend(loc='lower center',bbox_to_anchor=(0.48,1.01),columnspacing=2,fontsize='8',ncol=4,frameon=False)
    #
    if pname is not None:
    	plt.savefig(pname, dpi=200)
    	plt.close()
    #