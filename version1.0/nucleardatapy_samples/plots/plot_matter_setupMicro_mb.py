
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def plot_matter_setupMicro_e2a( pname, mb, models, band, matter ):
    #
    # plot E/A in NM
    #
    #print(f'Plot name: {pname}')
    #
    fig, axs = plt.subplots(2,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.85, wspace=0.2, hspace=0.2 )
    #
    axs[0,0].set_ylabel(r'$E_{NM}/A$ (MeV)')
    axs[0,0].set_xlim([0, 0.3])
    axs[1,0].set_xlabel(r'n (fm$^{-3}$)')
    axs[1,0].set_ylabel(r'$E_{NM}/E_{FFG,NR}$')
    axs[1,0].set_xlim([0, 0.3])
    axs[1,1].set_xlabel(r'$k_F$ (fm$^{-1}$)')
    if matter.lower() == 'nm':
        axs[0,0].set_ylim([0, 35])
        axs[0,1].set_xlim([0.5, 2.0])
        axs[0,1].set_ylim([0, 35])
        axs[1,0].set_ylim([0.3, 0.8])
        axs[1,1].set_xlim([0.5, 2.0])
        axs[1,1].set_ylim([0.3, 0.8])
        delta = 1.0
    elif matter.lower() == 'sm':
        axs[0,0].set_ylim([-20, 10])
        axs[0,1].set_xlim([0, 1.5])
        axs[0,1].set_ylim([-20, 10])
        axs[1,0].set_ylim([-2.0, 0.1])
        axs[1,1].set_xlim([0, 1.5])
        axs[1,1].set_ylim([-2.0, 0.1])
        delta = 0.0
    #
    for model in models:
        #
        mic = nuda.matter.setupMicro( model = model, var2 = delta )
        print('model:',model,' delta:',delta)
        if mic.nm_e2a is not None and 'FIT' not in model:
            if 'NLEFT' in model:
                if matter.lower() == 'nm':
                    axs[0,0].errorbar( mic.nm_den, mic.nm_e2adata, yerr=mic.nm_e2adata_err, linestyle = 'dotted', linewidth = 1, alpha=0.6 )
                    axs[0,1].errorbar( mic.nm_kfn, mic.nm_e2adata, yerr=mic.nm_e2adata_err, linestyle = 'dotted', linewidth = 1, alpha=0.6 )
                    axs[1,0].errorbar( mic.nm_den, mic.nm_e2adata/nuda.effg_nr(mic.nm_kfn), yerr=mic.nm_e2adata_err/nuda.effg_nr(mic.nm_kfn), linestyle = 'dotted', linewidth = 1, alpha=0.6 )
                    axs[1,1].errorbar( mic.nm_kfn, mic.nm_e2adata/nuda.effg_nr(mic.nm_kfn), yerr=mic.nm_e2adata_err/nuda.effg_nr(mic.nm_kfn), linestyle = 'dotted', linewidth = 1, alpha=0.6 )
                elif matter.lower() == 'sm':
                    axs[0,0].errorbar( mic.sm_den, mic.sm_e2adata, yerr=mic.sm_e2adata_err, linestyle = 'dotted', linewidth = 1, alpha=0.6 )
                    axs[0,1].errorbar( mic.sm_kfn, mic.sm_e2adata, yerr=mic.sm_e2adata_err, linestyle = 'dotted', linewidth = 1, alpha=0.6 )
                    axs[1,0].errorbar( mic.sm_den, mic.sm_e2adata/nuda.effg_nr(mic.sm_kfn), yerr=mic.sm_e2adata_err/nuda.effg_nr(mic.sm_kfn), linestyle = 'dotted', linewidth = 1, alpha=0.6 )
                    axs[1,1].errorbar( mic.sm_kfn, mic.sm_e2adata/nuda.effg_nr(mic.sm_kfn), yerr=mic.sm_e2adata_err/nuda.effg_nr(mic.sm_kfn), linestyle = 'dotted', linewidth = 1, alpha=0.6 )
                #
                if matter.lower() == 'nm':
                    axs[0,0].fill_between( mic.nm_den, y1=(mic.nm_e2a-mic.nm_e2a_err), y2=(mic.nm_e2a+mic.nm_e2a_err), alpha=0.3 )
                    axs[0,1].fill_between( mic.nm_kfn, y1=(mic.nm_e2a-mic.nm_e2a_err), y2=(mic.nm_e2a+mic.nm_e2a_err), alpha=0.3 )
                    axs[1,0].fill_between( mic.nm_den, y1=(mic.nm_e2a-mic.nm_e2a_err)/nuda.effg_nr(mic.nm_kfn), y2=(mic.nm_e2a+mic.nm_e2a_err)/nuda.effg_nr(mic.nm_kfn), alpha=0.3 )
                    axs[1,1].fill_between( mic.nm_kfn, y1=(mic.nm_e2a-mic.nm_e2a_err)/nuda.effg_nr(mic.nm_kfn), y2=(mic.nm_e2a+mic.nm_e2a_err)/nuda.effg_nr(mic.nm_kfn), alpha=0.3 )
                elif matter.lower() == 'sm':
                    axs[0,0].fill_between( mic.sm_den, y1=(mic.sm_e2a-mic.sm_e2a_err), y2=(mic.sm_e2a+mic.sm_e2a_err), alpha=0.3 )
                    axs[0,1].fill_between( mic.sm_kfn, y1=(mic.sm_e2a-mic.sm_e2a_err), y2=(mic.sm_e2a+mic.sm_e2a_err), alpha=0.3 )
                    axs[1,0].fill_between( mic.sm_den, y1=(mic.sm_e2a-mic.sm_e2a_err)/nuda.effg_nr(mic.sm_kfn), y2=(mic.sm_e2a+mic.sm_e2a_err)/nuda.effg_nr(mic.sm_kfn), alpha=0.3 )
                    axs[1,1].fill_between( mic.sm_kfn, y1=(mic.sm_e2a-mic.sm_e2a_err)/nuda.effg_nr(mic.sm_kfn), y2=(mic.sm_e2a+mic.sm_e2a_err)/nuda.effg_nr(mic.sm_kfn), alpha=0.3 )
            if mic.marker:
                if mic.err:
                    if matter.lower() == 'nm':
                        axs[0,0].errorbar( mic.nm_den, mic.nm_e2a, yerr=mic.nm_e2a_err, marker=mic.marker, markevery=mic.every, linestyle='None', label=mic.label, errorevery=mic.every )
                        axs[0,1].errorbar( mic.nm_kfn, mic.nm_e2a, yerr=mic.nm_e2a_err, marker=mic.marker, markevery=mic.every, linestyle='None', errorevery=mic.every )
                        axs[1,0].errorbar( mic.nm_den, mic.nm_e2a/nuda.effg_nr(mic.nm_kfn), yerr=mic.nm_e2a_err/nuda.effg_nr(mic.nm_kfn), marker=mic.marker, markevery=mic.every, linestyle='None', errorevery=mic.every )
                        axs[1,1].errorbar( mic.nm_kfn, mic.nm_e2a/nuda.effg_nr(mic.nm_kfn), yerr=mic.nm_e2a_err/nuda.effg_nr(mic.nm_kfn), marker=mic.marker, markevery=mic.every, linestyle='None', errorevery=mic.every )
                    elif matter.lower() == 'sm':
                        axs[0,0].errorbar( mic.sm_den, mic.sm_e2a, yerr=mic.sm_e2a_err, marker=mic.marker, markevery=mic.every, linestyle='None', label=mic.label, errorevery=mic.every )
                        axs[0,1].errorbar( mic.sm_kfn, mic.sm_e2a, yerr=mic.sm_e2a_err, marker=mic.marker, markevery=mic.every, linestyle='None', errorevery=mic.every )
                        axs[1,0].errorbar( mic.sm_den, mic.sm_e2a/nuda.effg_nr(mic.sm_kfn), yerr=mic.sm_e2a_err/nuda.effg_nr(mic.sm_kfn), marker=mic.marker, markevery=mic.every, linestyle='None', errorevery=mic.every )
                        axs[1,1].errorbar( mic.sm_kfn, mic.sm_e2a/nuda.effg_nr(mic.sm_kfn), yerr=mic.sm_e2a_err/nuda.effg_nr(mic.sm_kfn), marker=mic.marker, markevery=mic.every, linestyle='None', errorevery=mic.every )
                else:
                    if matter.lower() == 'nm':
                        axs[0,0].plot( mic.nm_den, mic.nm_e2a, marker=mic.marker, markevery=mic.every, linestyle='None', label=mic.label )
                        axs[0,1].plot( mic.nm_kfn, mic.nm_e2a, marker=mic.marker, markevery=mic.every, linestyle='None' )
                        axs[1,0].plot( mic.nm_den, mic.nm_e2a/nuda.effg_nr(mic.nm_kfn), marker=mic.marker, markevery=mic.every, linestyle='None' )
                        axs[1,1].plot( mic.nm_kfn, mic.nm_e2a/nuda.effg_nr(mic.nm_kfn), marker=mic.marker, markevery=mic.every, linestyle='None' )
                    elif matter.lower() == 'sm':
                        axs[0,0].plot( mic.sm_den, mic.sm_e2a, marker=mic.marker, markevery=mic.every, linestyle='None', label=mic.label )
                        axs[0,1].plot( mic.sm_kfn, mic.sm_e2a, marker=mic.marker, markevery=mic.every, linestyle='None' )
                        axs[1,0].plot( mic.sm_den, mic.sm_e2a/nuda.effg_nr(mic.sm_kfn), marker=mic.marker, markevery=mic.every, linestyle='None' )
                        axs[1,1].plot( mic.sm_kfn, mic.sm_e2a/nuda.effg_nr(mic.sm_kfn), marker=mic.marker, markevery=mic.every, linestyle='None' )
            else:
                if mic.err:
                    if matter.lower() == 'nm':
                        axs[0,0].errorbar( mic.nm_den, mic.nm_e2a, yerr=mic.nm_e2a_err, marker=mic.marker, markevery=mic.every, linestyle=mic.linestyle, label=mic.label, errorevery=mic.every )
                        axs[0,1].errorbar( mic.nm_kfn, mic.nm_e2a, yerr=mic.nm_e2a_err, marker=mic.marker, markevery=mic.every, linestyle=mic.linestyle, errorevery=mic.every )
                        axs[1,0].errorbar( mic.nm_den, mic.nm_e2a/nuda.effg_nr(mic.nm_kfn), yerr=mic.nm_e2a_err/nuda.effg_nr(mic.nm_kfn), marker=mic.marker, markevery=mic.every, linestyle=mic.linestyle, errorevery=mic.every )
                        axs[1,1].errorbar( mic.nm_kfn, mic.nm_e2a/nuda.effg_nr(mic.nm_kfn), yerr=mic.nm_e2a_err/nuda.effg_nr(mic.nm_kfn), marker=mic.marker, markevery=mic.every, linestyle=mic.linestyle, errorevery=mic.every )
                    elif matter.lower() == 'sm':
                        axs[0,0].errorbar( mic.sm_den, mic.sm_e2a, yerr=mic.sm_e2a_err, marker=mic.marker, markevery=mic.every, linestyle=mic.linestyle, label=mic.label, errorevery=mic.every )
                        axs[0,1].errorbar( mic.sm_kfn, mic.sm_e2a, yerr=mic.sm_e2a_err, marker=mic.marker, markevery=mic.every, linestyle=mic.linestyle, errorevery=mic.every )
                        axs[1,0].errorbar( mic.sm_den, mic.sm_e2a/nuda.effg_nr(mic.sm_kfn), yerr=mic.sm_e2a_err/nuda.effg_nr(mic.sm_kfn), marker=mic.marker, markevery=mic.every, linestyle=mic.linestyle, errorevery=mic.every )
                        axs[1,1].errorbar( mic.sm_kfn, mic.sm_e2a/nuda.effg_nr(mic.sm_kfn), yerr=mic.sm_e2a_err/nuda.effg_nr(mic.sm_kfn), marker=mic.marker, markevery=mic.every, linestyle=mic.linestyle, errorevery=mic.every )
                else:
                    if matter.lower() == 'nm':
                        axs[0,0].plot( mic.nm_den, mic.nm_e2a, marker=mic.marker, markevery=mic.every, linestyle=mic.linestyle, label=mic.label )
                        axs[0,1].plot( mic.nm_kfn, mic.nm_e2a, marker=mic.marker, markevery=mic.every, linestyle=mic.linestyle )
                        axs[1,0].plot( mic.nm_den, mic.nm_e2a/nuda.effg_nr(mic.nm_kfn), marker=mic.marker, markevery=mic.every, linestyle=mic.linestyle )
                        axs[1,1].plot( mic.nm_kfn, mic.nm_e2a/nuda.effg_nr(mic.nm_kfn), marker=mic.marker, markevery=mic.every, linestyle=mic.linestyle )
                    elif matter.lower() == 'sm':
                        axs[0,0].plot( mic.sm_den, mic.sm_e2a, marker=mic.marker, markevery=mic.every, linestyle=mic.linestyle, label=mic.label )
                        axs[0,1].plot( mic.sm_kfn, mic.sm_e2a, marker=mic.marker, markevery=mic.every, linestyle=mic.linestyle )
                        axs[1,0].plot( mic.sm_den, mic.sm_e2a/nuda.effg_nr(mic.sm_kfn), marker=mic.marker, markevery=mic.every, linestyle=mic.linestyle )
                        axs[1,1].plot( mic.sm_kfn, mic.sm_e2a/nuda.effg_nr(mic.sm_kfn), marker=mic.marker, markevery=mic.every, linestyle=mic.linestyle )
        elif mic.e2a is not None: 
            if 'fit' in model:
                #print('den:',mic.den)
                #print('e2a:',mic.e2a)                
                axs[0,0].plot( mic.den, mic.e2a, marker=mic.marker, linestyle=mic.linestyle, markevery=mic.every, label=mic.label )
                axs[0,1].plot( mic.kfn, mic.e2a, marker=mic.marker, linestyle=mic.linestyle )
                axs[1,0].plot( mic.den, mic.e2a/nuda.effg_nr(mic.kfn), marker=mic.marker, linestyle=mic.linestyle )
                axs[1,1].plot( mic.kfn, mic.e2a/nuda.effg_nr(mic.kfn), marker=mic.marker, linestyle=mic.linestyle )
        #
        if nuda.env.verb_output: mic.print_outputs( )
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
    plt.savefig(pname)
    plt.close()

def main():
    #
    print(50*'-')
    print("Enter plot_matter_setupMicro_mb.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    # create the groups of figures
    #
    mbs, mbs_lower = nuda.matter.micro_mbs()
    #mbs = [ 'VAR', 'AFDMC', 'BHF', 'QMC', 'MBPT', 'NLEFT' ]
    #mbs = [ 'VAR' ]
    #mbs = [ 'NLEFT' ]
    print('mbs:',mbs)
    #
    # list the different matter case investigated
    #
    matters = [ 'NM', 'SM' ]
    #
    for matter in matters:
        #
        # fix the uncertainty band in NM
        #
        if matter.lower() == 'nm':
            bmodels = [ '2016-MBPT-AM', '2016-QMC-NM', '2020-MBPT-AM' ]
        elif matter.lower() == 'sm':
            bmodels = [ '2016-MBPT-AM', '2020-MBPT-AM' ]
        #
        band = nuda.matter.setupMicroBand( bmodels, matter=matter  )
        #
        # plot E/A in matter grouped by mb
        #
        for mb in mbs:
            #
            print('For mb:',mb)
            #
            pname = 'figs/plot_matter_setupMicro_mb_e2a_'+matter+'_'+mb+'.png'
            print('pname:',pname)
            #
            # list the available models in mb
            #
            models, models_lower = nuda.matter.micro_models_mb_matter( mb, matter = matter )
            #
            print('models:',models)
            plot_matter_setupMicro_e2a( pname, mb, models, band, matter )
            #
    #
    print(50*'-')
    print("Exit plot_matter_setupMicro_mb.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
