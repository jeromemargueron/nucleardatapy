import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def matter_setupCheck_fig( pname, mb, models, band ):
    """
    Plot nucleonic energy per particle E/A in matter.\
    The plot is 1x1 with: E/A versus den.

    :param pname: name of the figure (*.png)
    :type pname: str.
    :param mb: many-body (mb) approach considered.
    :type mb: str.
    :param models: models to run on.
    :type models: array of str.
    :param band: object instantiated on the reference band.
    :type band: object.
    :param matter: can be 'SM' or 'NM'.
    :type matter: str.

    """
    #
    print(f'Plot name: {pname}')
    matter = band.matter
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.10, bottom=0.12, right=0.95, top=0.85, wspace=0.05, hspace=0.05 )
    #
    axs.set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    axs.set_xlim([0, 0.33])
    if matter.lower() == 'nm':
        axs.set_ylabel(r'$E_\text{NM}^\text{int}/A$ (MeV)')
        axs.set_ylim([0, 30])
        delta = 1.0
    elif matter.lower() == 'sm':
        axs.set_ylabel(r'$E_\text{SM}^\text{int}/A$ (MeV)')
        axs.set_ylim([-20, 10])
        delta = 0.0
    #
    for model in models:
        #
        mic = nuda.matter.setupMicro( model = model, var2 = delta )
        if nuda.env.verb_output: mic.print_outputs( )
        #
        print('model:',model,' delta:',delta)
        #
        check = nuda.matter.setupCheck( eos = mic, band = band )
        #
        if check.isInside:
            lstyle = 'solid'
        else:
            lstyle = 'dashed'
        #
        if mic.e_err:
            #
            print('=> model (with err):',model,mic.e_err)
            if 'NLEFT' in model:
                #
                print('   => model (NLEFT):',model)
                if matter.lower() == 'nm':
                    axs.errorbar( mic.nm_den, mic.nm_e2adata_int, yerr=mic.nm_e2adata_err, linestyle = 'dotted', markevery=mic.every, linewidth = 1, alpha=0.6 )
                    axs.fill_between( mic.nm_den, y1=(mic.nm_e2a_int-mic.nm_e2a_err), y2=(mic.nm_e2a_int+mic.nm_e2a_err), alpha=0.3 )
                elif matter.lower() == 'sm':
                    axs.errorbar( mic.sm_den, mic.sm_e2adata_int, yerr=mic.sm_e2adata_err, linestyle = 'dotted', markevery=mic.every, linewidth = 1, alpha=0.6 )
                    axs.fill_between( mic.sm_den, y1=(mic.sm_e2a_int-mic.sm_e2a_err), y2=(mic.sm_e2a_int+mic.sm_e2a_err), alpha=0.3 )
                #
            if mic.marker:
                #
                print('with marker:',mic.marker)
                if matter.lower() == 'nm':
                    axs.errorbar( mic.nm_den, mic.nm_e2a_int, yerr=mic.nm_e2a_err, marker=mic.marker, markevery=mic.every, linestyle=lstyle, label=mic.label, errorevery=mic.every )
                elif matter.lower() == 'sm':
                    axs.errorbar( mic.sm_den, mic.sm_e2a_int, yerr=mic.sm_e2a_err, marker=mic.marker, markevery=mic.every, linestyle=lstyle, label=mic.label, errorevery=mic.every )
                #
            else:
                #
                print('with no marker:',mic.marker)
                if matter.lower() == 'nm':
                    axs.errorbar( mic.nm_den, mic.nm_e2a_int, yerr=mic.nm_e2a_err, marker=mic.marker, markevery=mic.every, linestyle=lstyle, label=mic.label, errorevery=mic.every )
                elif matter.lower() == 'sm':
                    axs.errorbar( mic.sm_den, mic.sm_e2a_int, yerr=mic.sm_e2a_err, marker=mic.marker, markevery=mic.every, linestyle=lstyle, label=mic.label, errorevery=mic.every )
        else:
            print('=> model (no err):',model,mic.e_err)
            if 'fit' in model:
                axs.plot( mic.den, mic.e2a_int, marker=mic.marker, linestyle=lstyle, markevery=mic.every, label=mic.label )
            else:
                if matter.lower() == 'nm':
                    axs.plot( mic.nm_den, mic.nm_e2a_int, marker=mic.marker, linestyle=lstyle, markevery=mic.every, label=mic.label )
                elif matter.lower() == 'sm':
                    axs.plot( mic.sm_den, mic.sm_e2a_int, marker=mic.marker, linestyle=lstyle, markevery=mic.every, label=mic.label )
        #
    axs.fill_between( band.den, y1=(band.e2a_int-band.e2a_std), y2=(band.e2a_int+band.e2a_std), color=band.color, alpha=band.alpha, visible=True )
    axs.plot( band.den, (band.e2a_int-band.e2a_std), color='k', linestyle='dashed' )
    axs.plot( band.den, (band.e2a_int+band.e2a_std), color='k', linestyle='dashed' )
    #
    fig.legend(loc='upper left',bbox_to_anchor=(0.1,1.0),fontsize='8',ncol=3,frameon=False)
    #
    if pname is not None: 
        plt.savefig(pname, dpi=300)
        plt.close()
    #