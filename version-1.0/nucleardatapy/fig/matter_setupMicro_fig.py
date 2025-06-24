import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def matter_setupMicro_e2a_fig( pname, mb, models, band ):
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
    fig.subplots_adjust(left=0.12, bottom=0.12, right=0.95, top=0.85, wspace=0.05, hspace=0.05 )
    #
    axs[1,0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)', fontsize = '14' )
    axs[1,1].set_xlabel(r'$k_{F}$ (fm$^{-1}$)', fontsize = '14' )
    axs[0,1].tick_params('y', labelleft=False)
    axs[1,1].tick_params('y', labelleft=False)
    axs[0,0].tick_params('x', labelbottom=False)
    axs[0,1].tick_params('x', labelbottom=False)
    axs[0,0].set_xlim([0, 0.33])
    axs[1,0].set_xlim([0, 0.33])
    axs[0,1].set_xlim([0, 1.9])
    axs[1,1].set_xlim([0, 1.9])
    if matter.lower() == 'nm':
        axs[0,0].set_ylabel(r'$E_\text{int,NM}/A$ (MeV)', fontsize = '14' )
        axs[1,0].set_ylabel(r'$E_\text{int,NM}/E_\text{int,NM}^\text{NRFFG}$', fontsize = '14' )
        axs[0,0].set_ylim([0, 30])
        axs[0,1].set_ylim([0, 30])
        axs[1,0].set_ylim([0.2, 0.84])
        axs[1,1].set_ylim([0.2, 0.84])
        delta = 1.0
    elif matter.lower() == 'sm':
        axs[0,0].set_ylabel(r'$E_\text{int,SM}/A$ (MeV)', fontsize = '14' )
        axs[1,0].set_ylabel(r'$E_\text{int,SM}/E_\text{int,SM}^\text{NRFFG}$', fontsize = '14' )
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
                    axs[0,0].errorbar( mic.nm_den, mic.nm_e2a_int_data, yerr=mic.nm_e2a_err_data, linestyle = 'dotted', markevery=mic.every, linewidth = 1, alpha=0.6 )
                    axs[0,0].fill_between( mic.nm_den, y1=(mic.nm_e2a_int-mic.nm_e2a_err), y2=(mic.nm_e2a_int+mic.nm_e2a_err), alpha=0.3 )
                    axs[0,1].errorbar( mic.nm_kfn, mic.nm_e2a_int_data, yerr=mic.nm_e2a_err_data, linestyle = 'dotted', markevery=mic.every, linewidth = 1, alpha=0.6 )
                    axs[0,1].fill_between( mic.nm_kfn, y1=(mic.nm_e2a_int-mic.nm_e2a_err), y2=(mic.nm_e2a_int+mic.nm_e2a_err), alpha=0.3 )
                    axs[1,0].errorbar( mic.nm_den, mic.nm_e2a_int_data/nuda.effg_nr(mic.nm_kfn), yerr=mic.nm_e2a_err_data/nuda.effg_nr(mic.nm_kfn), linestyle = 'dotted', markevery=mic.every, linewidth = 1, alpha=0.6 )
                    axs[1,0].fill_between( mic.nm_den, y1=(mic.nm_e2a_int-mic.nm_e2a_err)/nuda.effg_nr(mic.nm_kfn), y2=(mic.nm_e2a_int+mic.nm_e2a_err)/nuda.effg_nr(mic.nm_kfn), alpha=0.3 )
                    axs[1,1].errorbar( mic.nm_kfn, mic.nm_e2a_int_data/nuda.effg_nr(mic.nm_kfn), yerr=mic.nm_e2a_err_data/nuda.effg_nr(mic.nm_kfn), linestyle = 'dotted', markevery=mic.every, linewidth = 1, alpha=0.6 )
                    axs[1,1].fill_between( mic.nm_kfn, y1=(mic.nm_e2a_int-mic.nm_e2a_err)/nuda.effg_nr(mic.nm_kfn), y2=(mic.nm_e2a_int+mic.nm_e2a_err)/nuda.effg_nr(mic.nm_kfn), alpha=0.3 )
                elif matter.lower() == 'sm':
                    axs[0,0].errorbar( mic.sm_den, mic.sm_e2a_int_data, yerr=mic.sm_e2a_err_data, linestyle = 'dotted', markevery=mic.every, linewidth = 1, alpha=0.6 )
                    axs[0,0].fill_between( mic.sm_den, y1=(mic.sm_e2a_int-mic.sm_e2a_err), y2=(mic.sm_e2a_int+mic.sm_e2a_err), alpha=0.3 )
                    axs[0,1].errorbar( mic.sm_kfn, mic.sm_e2a_int_data, yerr=mic.sm_e2a_err_data, linestyle = 'dotted', markevery=mic.every, linewidth = 1, alpha=0.6 )
                    axs[0,1].fill_between( mic.sm_kfn, y1=(mic.sm_e2a_int-mic.sm_e2a_err), y2=(mic.sm_e2a_int+mic.sm_e2a_err), alpha=0.3 )
                    axs[1,0].errorbar( mic.sm_den, mic.sm_e2a_int_data/nuda.effg_nr(mic.sm_kfn), yerr=mic.sm_e2a_err_data/nuda.effg_nr(mic.sm_kfn), linestyle = 'dotted', markevery=mic.every, linewidth = 1, alpha=0.6 )
                    axs[1,0].fill_between( mic.sm_den, y1=(mic.sm_e2a_int-mic.sm_e2a_err)/nuda.effg_nr(mic.sm_kfn), y2=(mic.sm_e2a_int+mic.sm_e2a_err)/nuda.effg_nr(mic.sm_kfn), alpha=0.3 )
                    axs[1,1].errorbar( mic.sm_kfn, mic.sm_e2a_int_data/nuda.effg_nr(mic.sm_kfn), yerr=mic.sm_e2a_err_data/nuda.effg_nr(mic.sm_kfn), linestyle = 'dotted', markevery=mic.every, linewidth = 1, alpha=0.6 )
                    axs[1,1].fill_between( mic.sm_kfn, y1=(mic.sm_e2a_int-mic.sm_e2a_err)/nuda.effg_nr(mic.sm_kfn), y2=(mic.sm_e2a_int+mic.sm_e2a_err)/nuda.effg_nr(mic.sm_kfn), alpha=0.3 )
                #
            if mic.marker:
                #
                print('with marker:',mic.marker)
                if matter.lower() == 'nm':
                    axs[0,0].errorbar( mic.nm_den, mic.nm_e2a_int, yerr=mic.nm_e2a_err, marker=mic.marker, markevery=mic.every, linestyle=lstyle, label=mic.label, errorevery=mic.every )
                    axs[0,1].errorbar( mic.nm_kfn, mic.nm_e2a_int, yerr=mic.nm_e2a_err, marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
                    axs[1,0].errorbar( mic.nm_den, mic.nm_e2a_int/nuda.effg_nr(mic.nm_kfn), yerr=mic.nm_e2a_err/nuda.effg_nr(mic.nm_kfn), marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
                    axs[1,1].errorbar( mic.nm_kfn, mic.nm_e2a_int/nuda.effg_nr(mic.nm_kfn), yerr=mic.nm_e2a_err/nuda.effg_nr(mic.nm_kfn), marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
                elif matter.lower() == 'sm':
                    axs[0,0].errorbar( mic.sm_den, mic.sm_e2a_int, yerr=mic.sm_e2a_err, marker=mic.marker, markevery=mic.every, linestyle=lstyle, label=mic.label, errorevery=mic.every )
                    axs[0,1].errorbar( mic.sm_kfn, mic.sm_e2a_int, yerr=mic.sm_e2a_err, marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
                    axs[1,0].errorbar( mic.sm_den, mic.sm_e2a_int/nuda.effg_nr(mic.sm_kfn), yerr=mic.sm_e2a_err/nuda.effg_nr(mic.sm_kfn), marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
                    axs[1,1].errorbar( mic.sm_kfn, mic.sm_e2a_int/nuda.effg_nr(mic.sm_kfn), yerr=mic.sm_e2a_err/nuda.effg_nr(mic.sm_kfn), marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
                #
            else:
                #
                print('with no marker:',mic.marker)
                if matter.lower() == 'nm':
                    axs[0,0].errorbar( mic.nm_den, mic.nm_e2a_int, yerr=mic.nm_e2a_err, marker=mic.marker, markevery=mic.every, linestyle=lstyle, label=mic.label, errorevery=mic.every )
                    axs[0,1].errorbar( mic.nm_kfn, mic.nm_e2a_int, yerr=mic.nm_e2a_err, marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
                    axs[1,0].errorbar( mic.nm_den, mic.nm_e2a_int/nuda.effg_nr(mic.nm_kfn), yerr=mic.nm_e2a_err/nuda.effg_nr(mic.nm_kfn), marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
                    axs[1,1].errorbar( mic.nm_kfn, mic.nm_e2a_int/nuda.effg_nr(mic.nm_kfn), yerr=mic.nm_e2a_err/nuda.effg_nr(mic.nm_kfn), marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
                elif matter.lower() == 'sm':
                    axs[0,0].errorbar( mic.sm_den, mic.sm_e2a_int, yerr=mic.sm_e2a_err, marker=mic.marker, markevery=mic.every, linestyle=lstyle, label=mic.label, errorevery=mic.every )
                    axs[0,1].errorbar( mic.sm_kfn, mic.sm_e2a_int, yerr=mic.sm_e2a_err, marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
                    axs[1,0].errorbar( mic.sm_den, mic.sm_e2a_int/nuda.effg_nr(mic.sm_kfn), yerr=mic.sm_e2a_err/nuda.effg_nr(mic.sm_kfn), marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
                    axs[1,1].errorbar( mic.sm_kfn, mic.sm_e2a_int/nuda.effg_nr(mic.sm_kfn), yerr=mic.sm_e2a_err/nuda.effg_nr(mic.sm_kfn), marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
        else:
            print('=> model (no err):',model,mic.e_err)
            if 'fit' in model:
                axs[0,0].plot( mic.den, mic.e2a_int, marker=mic.marker, linestyle=lstyle, markevery=mic.every, label=mic.label )
                axs[0,1].plot( mic.kfn, mic.e2a_int, marker=mic.marker, linestyle=lstyle )
                axs[1,0].plot( mic.den, mic.e2a_int/nuda.effg_nr(mic.kfn), marker=mic.marker, linestyle=lstyle )
                axs[1,1].plot( mic.kfn, mic.e2a_int/nuda.effg_nr(mic.kfn), marker=mic.marker, linestyle=lstyle )
            else:
                if matter.lower() == 'nm':
                    axs[0,0].plot( mic.nm_den, mic.nm_e2a_int, marker=mic.marker, linestyle=lstyle, markevery=mic.every, label=mic.label )
                    axs[0,1].plot( mic.nm_kfn, mic.nm_e2a_int, marker=mic.marker, linestyle=lstyle, markevery=mic.every )
                    axs[1,0].plot( mic.nm_den, mic.nm_e2a_int/nuda.effg_nr(mic.nm_kfn), marker=mic.marker, linestyle=lstyle, markevery=mic.every )
                    axs[1,1].plot( mic.nm_kfn, mic.nm_e2a_int/nuda.effg_nr(mic.nm_kfn), marker=mic.marker, linestyle=lstyle, markevery=mic.every )
                elif matter.lower() == 'sm':
                    axs[0,0].plot( mic.sm_den, mic.sm_e2a_int, marker=mic.marker, linestyle=lstyle, markevery=mic.every, label=mic.label )
                    axs[0,1].plot( mic.sm_kfn, mic.sm_e2a_int, marker=mic.marker, linestyle=lstyle, markevery=mic.every )
                    axs[1,0].plot( mic.sm_den, mic.sm_e2a_int/nuda.effg_nr(mic.sm_kfn), marker=mic.marker, linestyle=lstyle, markevery=mic.every )
                    axs[1,1].plot( mic.sm_kfn, mic.sm_e2a_int/nuda.effg_nr(mic.sm_kfn), marker=mic.marker, linestyle=lstyle, markevery=mic.every )
        #
    axs[0,0].fill_between( band.den, y1=(band.e2a_int-band.e2a_std), y2=(band.e2a_int+band.e2a_std), color=band.color, alpha=band.alpha, visible=True )
    axs[0,0].plot( band.den, (band.e2a_int-band.e2a_std), color='k', linestyle='dashed' )
    axs[0,0].plot( band.den, (band.e2a_int+band.e2a_std), color='k', linestyle='dashed' )
    axs[0,1].fill_between( band.kfn, y1=(band.e2a_int-band.e2a_std), y2=(band.e2a_int+band.e2a_std), color=band.color, alpha=band.alpha, visible=True )        
    axs[0,1].plot( band.kfn, (band.e2a_int-band.e2a_std), color='k', linestyle='dashed' )
    axs[0,1].plot( band.kfn, (band.e2a_int+band.e2a_std), color='k', linestyle='dashed' )
    axs[1,0].fill_between( band.den, y1=(band.e2a_int-band.e2a_std)/nuda.effg_nr(band.kfn), y2=(band.e2a_int+band.e2a_std)/nuda.effg_nr(band.kfn), color=band.color, alpha=band.alpha, visible=True )
    axs[1,0].plot( band.den, (band.e2a_int-band.e2a_std)/nuda.effg_nr(band.kfn), color='k', linestyle='dashed' )
    axs[1,0].plot( band.den, (band.e2a_int+band.e2a_std)/nuda.effg_nr(band.kfn), color='k', linestyle='dashed' )
    axs[1,1].fill_between( band.kfn, y1=(band.e2a_int-band.e2a_std)/nuda.effg_nr(band.kfn), y2=(band.e2a_int+band.e2a_std)/nuda.effg_nr(band.kfn), color=band.color, alpha=band.alpha, visible=True )
    axs[1,1].plot( band.kfn, (band.e2a_int-band.e2a_std)/nuda.effg_nr(band.kfn), color='k', linestyle='dashed' )
    axs[1,1].plot( band.kfn, (band.e2a_int+band.e2a_std)/nuda.effg_nr(band.kfn), color='k', linestyle='dashed' )
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

def matter_setupMicro_pre_fig( pname, mb, models, band ):
    """
    Plot nucleonic pressure in matter.\
    The plot is 2x2 with:\
    [0,0]: pre versus den.           [0,1]: pre versus kfn.\
    [1,0]: pre/pre_NRFFG versus den. [1,1]: pre/pre_NRFFG versus kfn.\

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
    fig.subplots_adjust(left=0.12, bottom=0.12, right=0.95, top=0.85, wspace=0.05, hspace=0.05 )
    #
    axs[1,0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)', fontsize = '14' )
    axs[1,1].set_xlabel(r'$k_{F}$ (fm$^{-1}$)', fontsize = '14' )
    axs[0,1].tick_params('y', labelleft=False)
    axs[1,1].tick_params('y', labelleft=False)
    axs[0,0].tick_params('x', labelbottom=False)
    axs[0,1].tick_params('x', labelbottom=False)
    axs[0,0].set_xlim([0, 0.33])
    axs[1,0].set_xlim([0, 0.33])
    axs[0,1].set_xlim([0.5, 1.9])
    axs[1,1].set_xlim([0.5, 1.9])
    if matter.lower() == 'nm':
        axs[0,0].set_ylabel(r'$p_\text{NM}$ (MeV)', fontsize = '14' )
        axs[1,0].set_ylabel(r'$p_\text{NM}/p_\text{NRFFG}$', fontsize = '14' )
        axs[0,0].set_ylim([-2, 30])
        axs[0,1].set_ylim([-2, 30])
        axs[1,0].set_ylim([-0.2, 0.84])
        axs[1,1].set_ylim([-0.2, 0.84])
        delta = 1.0
    elif matter.lower() == 'sm':
        axs[0,0].set_ylabel(r'$p_\text{SM}$ (MeV)', fontsize = '14' )
        axs[1,0].set_ylabel(r'$p_\text{SM}/p_\text{NRFFG}$', fontsize = '14' )
        axs[0,0].set_ylim([-5, 10])
        axs[0,1].set_ylim([-5, 10])
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
        if mic.p_err:
            #
            print('=> model (with err):',model,mic.pre_err)
            if mic.marker:
                #
                print('with marker:',mic.marker)
                if matter.lower() == 'nm':
                    axs[0,0].errorbar( mic.nm_den, mic.nm_pre, yerr=mic.nm_pre_err, marker=mic.marker, markevery=mic.every, linestyle=lstyle, label=mic.label, errorevery=mic.every )
                    axs[0,1].errorbar( mic.nm_kfn, mic.nm_pre, yerr=mic.nm_pre_err, marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
                    axs[1,0].errorbar( mic.nm_den, mic.nm_pre/nuda.pre_nr(mic.nm_kfn), yerr=mic.nm_pre_err/nuda.pre_nr(mic.nm_kfn), marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
                    axs[1,1].errorbar( mic.nm_kfn, mic.nm_pre/nuda.pre_nr(mic.nm_kfn), yerr=mic.nm_pre_err/nuda.pre_nr(mic.nm_kfn), marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
                elif matter.lower() == 'sm':
                    axs[0,0].errorbar( mic.sm_den, mic.sm_pre, yerr=mic.sm_pre_err, marker=mic.marker, markevery=mic.every, linestyle=lstyle, label=mic.label, errorevery=mic.every )
                    axs[0,1].errorbar( mic.sm_kfn, mic.sm_pre, yerr=mic.sm_pre_err, marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
                    axs[1,0].errorbar( mic.sm_den, mic.sm_pre/nuda.pre_nr(mic.sm_kfn), yerr=mic.sm_pre_err/nuda.pre_nr(mic.sm_kfn), marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
                    axs[1,1].errorbar( mic.sm_kfn, mic.sm_pre/nuda.pre_nr(mic.sm_kfn), yerr=mic.sm_pre_err/nuda.pre_nr(mic.sm_kfn), marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
                #
            else:
                #
                print('with no marker:',mic.marker)
                if matter.lower() == 'nm':
                    axs[0,0].errorbar( mic.nm_den, mic.nm_pre, yerr=mic.nm_pre_err, marker=mic.marker, markevery=mic.every, linestyle=lstyle, label=mic.label, errorevery=mic.every )
                    axs[0,1].errorbar( mic.nm_kfn, mic.nm_pre, yerr=mic.nm_pre_err, marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
                    axs[1,0].errorbar( mic.nm_den, mic.nm_pre/nuda.pre_nr(mic.nm_kfn), yerr=mic.nm_pre_err/nuda.pre_nr(mic.nm_kfn), marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
                    axs[1,1].errorbar( mic.nm_kfn, mic.nm_pre/nuda.pre_nr(mic.nm_kfn), yerr=mic.nm_pre_err/nuda.pre_nr(mic.nm_kfn), marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
                elif matter.lower() == 'sm':
                    axs[0,0].errorbar( mic.sm_den, mic.sm_pre, yerr=mic.sm_pre_err, marker=mic.marker, markevery=mic.every, linestyle=lstyle, label=mic.label, errorevery=mic.every )
                    axs[0,1].errorbar( mic.sm_kfn, mic.sm_pre, yerr=mic.sm_pre_err, marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
                    axs[1,0].errorbar( mic.sm_den, mic.sm_pre/nuda.pre_nr(mic.sm_kfn), yerr=mic.sm_pre_err/nuda.pre_nr(mic.sm_kfn), marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
                    axs[1,1].errorbar( mic.sm_kfn, mic.sm_pre/nuda.pre_nr(mic.sm_kfn), yerr=mic.sm_pre_err/nuda.pre_nr(mic.sm_kfn), marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
        else:
            print('=> model (no err):',model,mic.e_err)
            if 'fit' in model:
                axs[0,0].plot( mic.den, mic.pre, marker=mic.marker, linestyle=lstyle, markevery=mic.every, label=mic.label )
                axs[0,1].plot( mic.kfn, mic.pre, marker=mic.marker, linestyle=lstyle )
                axs[1,0].plot( mic.den, mic.pre/nuda.pre_nr(mic.kfn), marker=mic.marker, linestyle=lstyle )
                axs[1,1].plot( mic.kfn, mic.pre/nuda.pre_nr(mic.kfn), marker=mic.marker, linestyle=lstyle )
            else:
                if matter.lower() == 'nm':
                    axs[0,0].plot( mic.nm_den, mic.nm_pre, marker=mic.marker, linestyle=lstyle, markevery=mic.every, label=mic.label )
                    axs[0,1].plot( mic.nm_kfn, mic.nm_pre, marker=mic.marker, linestyle=lstyle, markevery=mic.every )
                    axs[1,0].plot( mic.nm_den, mic.nm_pre/nuda.pre_nr(mic.nm_kfn), marker=mic.marker, linestyle=lstyle, markevery=mic.every )
                    axs[1,1].plot( mic.nm_kfn, mic.nm_pre/nuda.pre_nr(mic.nm_kfn), marker=mic.marker, linestyle=lstyle, markevery=mic.every )
                elif matter.lower() == 'sm':
                    axs[0,0].plot( mic.sm_den, mic.sm_pre, marker=mic.marker, linestyle=lstyle, markevery=mic.every, label=mic.label )
                    axs[0,1].plot( mic.sm_kfn, mic.sm_pre, marker=mic.marker, linestyle=lstyle, markevery=mic.every )
                    axs[1,0].plot( mic.sm_den, mic.sm_pre/nuda.pre_nr(mic.sm_kfn), marker=mic.marker, linestyle=lstyle, markevery=mic.every )
                    axs[1,1].plot( mic.sm_kfn, mic.sm_pre/nuda.pre_nr(mic.sm_kfn), marker=mic.marker, linestyle=lstyle, markevery=mic.every )
        #
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

def matter_setupMicro_cs2_fig( pname, mb, models, band ):
    """
    Plot nucleonic pressure in matter.\
    The plot is 1x2 with:\
    [0]: cs2 versus den.   [1]: cs2 versus kfn.\

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
    fig, axs = plt.subplots(1,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=0.95, top=0.85, wspace=0.05, hspace=0.05 )
    #
    axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)', fontsize = '14' )
    axs[1].set_xlabel(r'$k_{F}$ (fm$^{-1}$)')
    axs[1].tick_params('y', labelleft=False)
    axs[0].set_xlim([0, 0.33])
    axs[1].set_xlim([0.5, 1.9])
    if matter.lower() == 'nm':
        axs[0].set_ylabel(r'$c_\text{s,NM}^2/c^2$', fontsize = '14' )
        axs[0].set_ylim([-0.05, 0.3])
        axs[1].set_ylim([-0.05, 0.3])
        delta = 1.0
    elif matter.lower() == 'sm':
        axs[0].set_ylabel(r'$c_\text{s,SM}^2/c^2$', fontsize = '14' )
        axs[0].set_ylim([-0.05, 0.2])
        axs[1].set_ylim([-0.05, 0.2])
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
        if mic.cs2_err:
            #
            print('=> model (with err):',model,mic.cs2_err)
            if mic.marker:
                #
                print('with marker:',mic.marker)
                if matter.lower() == 'nm':
                    axs[0].errorbar( mic.nm_den[:-1], mic.nm_cs2[:-1], yerr=mic.nm_cs2_err[:-1], marker=mic.marker, markevery=mic.every, linestyle=lstyle, label=mic.label, errorevery=mic.every )
                    axs[1].errorbar( mic.nm_kfn[:-1], mic.nm_cs2[:-1], yerr=mic.nm_cs2_err[:-1], marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
                elif matter.lower() == 'sm':
                    axs[0].errorbar( mic.sm_den[:-1], mic.sm_cs2[:-1], yerr=mic.sm_cs2_err[:-1], marker=mic.marker, markevery=mic.every, linestyle=lstyle, label=mic.label, errorevery=mic.every )
                    axs[1].errorbar( mic.sm_kfn[:-1], mic.sm_cs2[:-1], yerr=mic.sm_cs2_err[:-1], marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
                #
            else:
                #
                print('with no marker:',mic.marker)
                if matter.lower() == 'nm':
                    axs[0].errorbar( mic.nm_den[:-1], mic.nm_cs2[:-1], yerr=mic.nm_cs2_err[:-1], marker=mic.marker, markevery=mic.every, linestyle=lstyle, label=mic.label, errorevery=mic.every )
                    axs[1].errorbar( mic.nm_kfn[:-1], mic.nm_cs2[:-1], yerr=mic.nm_cs2_err[:-1], marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
                elif matter.lower() == 'sm':
                    axs[0].errorbar( mic.sm_den[:-1], mic.sm_cs2[:-1], yerr=mic.sm_cs2_err[:-1], marker=mic.marker, markevery=mic.every, linestyle=lstyle, label=mic.label, errorevery=mic.every )
                    axs[1].errorbar( mic.sm_kfn[:-1], mic.sm_cs2[:-1], yerr=mic.sm_cs2_err[:-1], marker=mic.marker, markevery=mic.every, linestyle=lstyle, errorevery=mic.every )
        else:
            print('=> model (no err):',model,mic.cs2_err)
            if 'fit' in model:
                axs[0].plot( mic.den[:-1], mic.cs2[:-1], marker=mic.marker, linestyle=lstyle, markevery=mic.every, label=mic.label )
                axs[1].plot( mic.kfn[:-1], mic.cs2[:-1], marker=mic.marker, linestyle=lstyle )
            else:
                if matter.lower() == 'nm':
                    axs[0].plot( mic.nm_den[:-1], mic.nm_cs2[:-1], marker=mic.marker, linestyle=lstyle, markevery=mic.every, label=mic.label )
                    axs[1].plot( mic.nm_kfn[:-1], mic.nm_cs2[:-1], marker=mic.marker, linestyle=lstyle, markevery=mic.every )
                elif matter.lower() == 'sm':
                    axs[0].plot( mic.sm_den[:-1], mic.sm_cs2[:-1], marker=mic.marker, linestyle=lstyle, markevery=mic.every, label=mic.label )
                    axs[1].plot( mic.sm_kfn[:-1], mic.sm_cs2[:-1], marker=mic.marker, linestyle=lstyle, markevery=mic.every )
        #
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
