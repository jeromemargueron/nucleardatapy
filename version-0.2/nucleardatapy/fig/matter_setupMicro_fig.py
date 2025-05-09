import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def matter_setupMicro_E_fig( pname, mb, models, band ):
    """
    Plot nucleonic energy per particle E/A in matter.\
    The plot is 2x2 with:\
    [0,0]: E/A versus den.       [0,1]: E/A versus kfn.\
    [1,0]: E/E_NRFFG versus den. [1,1]: E/E_NRFFG versus kfn.\

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
    fig, axs = plt.subplots(2,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.10, bottom=0.12, right=None, top=0.85, wspace=0.05, hspace=0.05 )
    #
    axs[1,0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    axs[1,1].set_xlabel(r'$k_{F_n}$ (fm$^{-1}$)')
    axs[0,1].tick_params('y', labelleft=False)
    axs[1,1].tick_params('y', labelleft=False)
    axs[0,0].tick_params('x', labelbottom=False)
    axs[0,1].tick_params('x', labelbottom=False)
    axs[0,0].set_xlim([0, 0.33])
    axs[1,0].set_xlim([0, 0.33])
    axs[0,1].set_xlim([0.5, 1.9])
    axs[1,1].set_xlim([0.5, 1.9])
    if matter.lower() == 'nm':
        axs[0,0].set_ylabel(r'$E_\text{NM}/A$ (MeV)')
        axs[1,0].set_ylabel(r'$E_\text{NM}/E_\text{NRFFG}$')
        axs[0,0].set_ylim([0, 30])
        axs[0,1].set_ylim([0, 30])
        axs[1,0].set_ylim([0.2, 0.84])
        axs[1,1].set_ylim([0.2, 0.84])
        delta = 1.0
    elif matter.lower() == 'sm':
        axs[0,0].set_ylabel(r'$E_\text{SM}/A$ (MeV)')
        axs[1,0].set_ylabel(r'$E_\text{SM}/E_\text{NRFFG}$')
        axs[0,0].set_ylim([-20, 10])
        axs[0,1].set_ylim([-20, 10])
        axs[1,0].set_ylim([-1.2, 0.5])
        axs[1,1].set_ylim([-1.2, 0.5])
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
                    axs[0,0].errorbar( mic.nm_den, mic.nm_e2adata, yerr=mic.nm_e2adata_err, linestyle = 'dotted', markevery=mic.every, linewidth = 1, alpha=0.6 )
                    axs[0,0].fill_between( mic.nm_den, y1=(mic.nm_e2a-mic.nm_e2a_err), y2=(mic.nm_e2a+mic.nm_e2a_err), alpha=0.3 )
                    axs[0,1].errorbar( mic.nm_kfn, mic.nm_e2adata, yerr=mic.nm_e2adata_err, linestyle = 'dotted', markevery=mic.every, linewidth = 1, alpha=0.6 )
                    axs[0,1].fill_between( mic.nm_kfn, y1=(mic.nm_e2a-mic.nm_e2a_err), y2=(mic.nm_e2a+mic.nm_e2a_err), alpha=0.3 )
                    axs[1,0].errorbar( mic.nm_den, mic.nm_e2adata/nuda.effg_nr(mic.nm_kfn), yerr=mic.nm_e2adata_err/nuda.effg_nr(mic.nm_kfn), linestyle = 'dotted', markevery=mic.every, linewidth = 1, alpha=0.6 )
                    axs[1,0].fill_between( mic.nm_den, y1=(mic.nm_e2a-mic.nm_e2a_err)/nuda.effg_nr(mic.nm_kfn), y2=(mic.nm_e2a+mic.nm_e2a_err)/nuda.effg_nr(mic.nm_kfn), alpha=0.3 )
                    axs[1,1].errorbar( mic.nm_kfn, mic.nm_e2adata/nuda.effg_nr(mic.nm_kfn), yerr=mic.nm_e2adata_err/nuda.effg_nr(mic.nm_kfn), linestyle = 'dotted', markevery=mic.every, linewidth = 1, alpha=0.6 )
                    axs[1,1].fill_between( mic.nm_kfn, y1=(mic.nm_e2a-mic.nm_e2a_err)/nuda.effg_nr(mic.nm_kfn), y2=(mic.nm_e2a+mic.nm_e2a_err)/nuda.effg_nr(mic.nm_kfn), alpha=0.3 )
                elif matter.lower() == 'sm':
                    axs[0,0].errorbar( mic.sm_den, mic.sm_e2adata, yerr=mic.sm_e2adata_err, linestyle = 'dotted', markevery=mic.every, linewidth = 1, alpha=0.6 )
                    axs[0,0].fill_between( mic.sm_den, y1=(mic.sm_e2a-mic.sm_e2a_err), y2=(mic.sm_e2a+mic.sm_e2a_err), alpha=0.3 )
                    axs[0,1].errorbar( mic.sm_kfn, mic.sm_e2adata, yerr=mic.sm_e2adata_err, linestyle = 'dotted', markevery=mic.every, linewidth = 1, alpha=0.6 )
                    axs[0,1].fill_between( mic.sm_kfn, y1=(mic.sm_e2a-mic.sm_e2a_err), y2=(mic.sm_e2a+mic.sm_e2a_err), alpha=0.3 )
                    axs[1,0].errorbar( mic.sm_den, mic.sm_e2adata/nuda.effg_nr(mic.sm_kfn), yerr=mic.sm_e2adata_err/nuda.effg_nr(mic.sm_kfn), linestyle = 'dotted', markevery=mic.every, linewidth = 1, alpha=0.6 )
                    axs[1,0].fill_between( mic.sm_den, y1=(mic.sm_e2a-mic.sm_e2a_err)/nuda.effg_nr(mic.sm_kfn), y2=(mic.sm_e2a+mic.sm_e2a_err)/nuda.effg_nr(mic.sm_kfn), alpha=0.3 )
                    axs[1,1].errorbar( mic.sm_kfn, mic.sm_e2adata/nuda.effg_nr(mic.sm_kfn), yerr=mic.sm_e2adata_err/nuda.effg_nr(mic.sm_kfn), linestyle = 'dotted', markevery=mic.every, linewidth = 1, alpha=0.6 )
                    axs[1,1].fill_between( mic.sm_kfn, y1=(mic.sm_e2a-mic.sm_e2a_err)/nuda.effg_nr(mic.sm_kfn), y2=(mic.sm_e2a+mic.sm_e2a_err)/nuda.effg_nr(mic.sm_kfn), alpha=0.3 )
                #
            if mic.marker:
                #
                print('with marker:',mic.marker)
                if matter.lower() == 'nm':
                    axs[0,0].errorbar( mic.nm_den, mic.nm_e2a, yerr=mic.nm_e2a_err, marker=mic.marker, markevery=mic.every, linestyle=lstyle, label=mic.label, errorevery=mic.every )
                    axs[0,1].errorbar( mic.nm_kfn, mic.nm_e2a, yerr=mic.nm_e2a_err, marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
                    axs[1,0].errorbar( mic.nm_den, mic.nm_e2a/nuda.effg_nr(mic.nm_kfn), yerr=mic.nm_e2a_err/nuda.effg_nr(mic.nm_kfn), marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
                    axs[1,1].errorbar( mic.nm_kfn, mic.nm_e2a/nuda.effg_nr(mic.nm_kfn), yerr=mic.nm_e2a_err/nuda.effg_nr(mic.nm_kfn), marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
                elif matter.lower() == 'sm':
                    axs[0,0].errorbar( mic.sm_den, mic.sm_e2a, yerr=mic.sm_e2a_err, marker=mic.marker, markevery=mic.every, linestyle=lstyle, label=mic.label, errorevery=mic.every )
                    axs[0,1].errorbar( mic.sm_kfn, mic.sm_e2a, yerr=mic.sm_e2a_err, marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
                    axs[1,0].errorbar( mic.sm_den, mic.sm_e2a/nuda.effg_nr(mic.sm_kfn), yerr=mic.sm_e2a_err/nuda.effg_nr(mic.sm_kfn), marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
                    axs[1,1].errorbar( mic.sm_kfn, mic.sm_e2a/nuda.effg_nr(mic.sm_kfn), yerr=mic.sm_e2a_err/nuda.effg_nr(mic.sm_kfn), marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
                #
            else:
                #
                print('with no marker:',mic.marker)
                if matter.lower() == 'nm':
                    axs[0,0].errorbar( mic.nm_den, mic.nm_e2a, yerr=mic.nm_e2a_err, marker=mic.marker, markevery=mic.every, linestyle=lstyle, label=mic.label, errorevery=mic.every )
                    axs[0,1].errorbar( mic.nm_kfn, mic.nm_e2a, yerr=mic.nm_e2a_err, marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
                    axs[1,0].errorbar( mic.nm_den, mic.nm_e2a/nuda.effg_nr(mic.nm_kfn), yerr=mic.nm_e2a_err/nuda.effg_nr(mic.nm_kfn), marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
                    axs[1,1].errorbar( mic.nm_kfn, mic.nm_e2a/nuda.effg_nr(mic.nm_kfn), yerr=mic.nm_e2a_err/nuda.effg_nr(mic.nm_kfn), marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
                elif matter.lower() == 'sm':
                    axs[0,0].errorbar( mic.sm_den, mic.sm_e2a, yerr=mic.sm_e2a_err, marker=mic.marker, markevery=mic.every, linestyle=lstyle, label=mic.label, errorevery=mic.every )
                    axs[0,1].errorbar( mic.sm_kfn, mic.sm_e2a, yerr=mic.sm_e2a_err, marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
                    axs[1,0].errorbar( mic.sm_den, mic.sm_e2a/nuda.effg_nr(mic.sm_kfn), yerr=mic.sm_e2a_err/nuda.effg_nr(mic.sm_kfn), marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
                    axs[1,1].errorbar( mic.sm_kfn, mic.sm_e2a/nuda.effg_nr(mic.sm_kfn), yerr=mic.sm_e2a_err/nuda.effg_nr(mic.sm_kfn), marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
        else:
            print('=> model (no err):',model,mic.e_err)
            if 'fit' in model:
                axs[0,0].plot( mic.den, mic.e2a, marker=mic.marker, linestyle=lstyle, markevery=mic.every, label=mic.label )
                axs[0,1].plot( mic.kfn, mic.e2a, marker=mic.marker, linestyle=lstyle )
                axs[1,0].plot( mic.den, mic.e2a/nuda.effg_nr(mic.kfn), marker=mic.marker, linestyle=lstyle )
                axs[1,1].plot( mic.kfn, mic.e2a/nuda.effg_nr(mic.kfn), marker=mic.marker, linestyle=lstyle )
            else:
                if matter.lower() == 'nm':
                    axs[0,0].plot( mic.nm_den, mic.nm_e2a, marker=mic.marker, linestyle=lstyle, markevery=mic.every, label=mic.label )
                    axs[0,1].plot( mic.nm_kfn, mic.nm_e2a, marker=mic.marker, linestyle=lstyle, markevery=mic.every )
                    axs[1,0].plot( mic.nm_den, mic.nm_e2a/nuda.effg_nr(mic.nm_kfn), marker=mic.marker, linestyle=lstyle, markevery=mic.every )
                    axs[1,1].plot( mic.nm_kfn, mic.nm_e2a/nuda.effg_nr(mic.nm_kfn), marker=mic.marker, linestyle=lstyle, markevery=mic.every )
                elif matter.lower() == 'sm':
                    axs[0,0].plot( mic.sm_den, mic.sm_e2a, marker=mic.marker, linestyle=lstyle, markevery=mic.every, label=mic.label )
                    axs[0,1].plot( mic.sm_kfn, mic.sm_e2a, marker=mic.marker, linestyle=lstyle, markevery=mic.every )
                    axs[1,0].plot( mic.sm_den, mic.sm_e2a/nuda.effg_nr(mic.sm_kfn), marker=mic.marker, linestyle=lstyle, markevery=mic.every )
                    axs[1,1].plot( mic.sm_kfn, mic.sm_e2a/nuda.effg_nr(mic.sm_kfn), marker=mic.marker, linestyle=lstyle, markevery=mic.every )
        #
    axs[0,0].fill_between( band.den, y1=(band.e2a-band.e2a_std), y2=(band.e2a+band.e2a_std), color=band.color, alpha=band.alpha, visible=True )
    axs[0,0].plot( band.den, (band.e2a-band.e2a_std), color='k', linestyle='dashed' )
    axs[0,0].plot( band.den, (band.e2a+band.e2a_std), color='k', linestyle='dashed' )
    axs[0,1].fill_between( band.kfn, y1=(band.e2a-band.e2a_std), y2=(band.e2a+band.e2a_std), color=band.color, alpha=band.alpha, visible=True )        
    axs[0,1].plot( band.kfn, (band.e2a-band.e2a_std), color='k', linestyle='dashed' )
    axs[0,1].plot( band.kfn, (band.e2a+band.e2a_std), color='k', linestyle='dashed' )
    axs[1,0].fill_between( band.den, y1=(band.e2a-band.e2a_std)/nuda.effg_nr(band.kfn), y2=(band.e2a+band.e2a_std)/nuda.effg_nr(band.kfn), color=band.color, alpha=band.alpha, visible=True )
    axs[1,0].plot( band.den, (band.e2a-band.e2a_std)/nuda.effg_nr(band.kfn), color='k', linestyle='dashed' )
    axs[1,0].plot( band.den, (band.e2a+band.e2a_std)/nuda.effg_nr(band.kfn), color='k', linestyle='dashed' )
    axs[1,1].fill_between( band.kfn, y1=(band.e2a-band.e2a_std)/nuda.effg_nr(band.kfn), y2=(band.e2a+band.e2a_std)/nuda.effg_nr(band.kfn), color=band.color, alpha=band.alpha, visible=True )
    axs[1,1].plot( band.kfn, (band.e2a-band.e2a_std)/nuda.effg_nr(band.kfn), color='k', linestyle='dashed' )
    axs[1,1].plot( band.kfn, (band.e2a+band.e2a_std)/nuda.effg_nr(band.kfn), color='k', linestyle='dashed' )
    #
    #axs[0,1].legend(loc='upper left',fontsize='8', ncol=2)
    #if mb not in 'BHF':
    #    axs[0,1].legend(loc='upper left',fontsize='8', ncol=2)
    #
    #plt.tight_layout(pad=3.0)
    fig.legend(loc='upper left',bbox_to_anchor=(0.1,1.0),fontsize='8',ncol=3,frameon=False)
    #
    if pname is not None: 
        plt.savefig(pname, dpi=300)
        plt.close()
