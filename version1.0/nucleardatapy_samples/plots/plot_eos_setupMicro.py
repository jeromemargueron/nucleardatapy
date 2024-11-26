
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plot_eos_setupMicro_nm_e2a( pname, group, models, band ):
    #
    # plot E/A in NM
    #
    print(f'Plot name: {pname}')
    #
    fig, axs = plt.subplots(2,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.98, wspace=0.2, hspace=0.2 )
    #
    axs[0,0].set_ylabel(r'$E_{NM}/A$ (MeV)')
    axs[0,0].set_xlim([0, 0.3])
    axs[0,0].set_ylim([0, 35])
    #
    axs[0,1].set_xlim([0, 1.5])
    axs[0,1].set_ylim([0, 15])
    #
    axs[1,0].set_xlabel(r'n (fm$^{-3}$)')
    axs[1,0].set_ylabel(r'$E_{NM}/E_{FFG}$')
    axs[1,0].set_xlim([0, 0.3])
    axs[1,0].set_ylim([0.2, 0.8])
    #
    axs[1,1].set_xlabel(r'$k_F$ (fm$^{-1}$)')
    axs[1,1].set_xlim([0, 1.5])
    axs[1,1].set_ylim([0.2, 0.8])
    #
    print('\nmodels in NM:',models,'\n')
    #
    for model in models:
        #
        mic = nuda.eos.setupMicro( model = model, var2=1.0 )
        print('\nmodel:',model,'\n')
        if mic.nm_e2a is not None:
            if 'NLEFT' in model:
                axs[0,0].errorbar( mic.nm_den, mic.nm_e2adata, yerr=mic.nm_e2adata_err, linestyle = 'dotted', linewidth = 1, alpha=0.6 )
                axs[0,1].errorbar( mic.nm_kfn, mic.nm_e2adata, yerr=mic.nm_e2adata_err, linestyle = 'dotted', linewidth = 1, alpha=0.6 )
                axs[1,0].errorbar( mic.nm_den, mic.nm_e2adata/nuda.effg(mic.nm_kfn), yerr=mic.nm_e2adata_err/nuda.effg(mic.nm_kfn), linestyle = 'dotted', linewidth = 1, alpha=0.6 )
                axs[1,1].errorbar( mic.nm_kfn, mic.nm_e2adata/nuda.effg(mic.nm_kfn), yerr=mic.nm_e2adata_err/nuda.effg(mic.nm_kfn), linestyle = 'dotted', linewidth = 1, alpha=0.6 )
                #
                axs[0,0].fill_between( mic.nm_den, y1=(mic.nm_e2a-mic.nm_e2a_err), y2=(mic.nm_e2a+mic.nm_e2a_err), alpha=0.3 )
                axs[0,1].fill_between( mic.nm_kfn, y1=(mic.nm_e2a-mic.nm_e2a_err), y2=(mic.nm_e2a+mic.nm_e2a_err), alpha=0.3 )
                axs[1,0].fill_between( mic.nm_den, y1=(mic.nm_e2a-mic.nm_e2a_err)/nuda.effg(mic.nm_kfn), y2=(mic.nm_e2a+mic.nm_e2a_err)/nuda.effg(mic.nm_kfn), alpha=0.3 )
                axs[1,1].fill_between( mic.nm_kfn, y1=(mic.nm_e2a-mic.nm_e2a_err)/nuda.effg(mic.nm_kfn), y2=(mic.nm_e2a+mic.nm_e2a_err)/nuda.effg(mic.nm_kfn), alpha=0.3 )
            if mic.marker:
                if mic.err:
                    axs[0,0].errorbar( mic.nm_den, mic.nm_e2a, yerr=mic.nm_e2a_err, marker=mic.marker, linestyle='none', label=mic.label, errorevery=mic.every )
                    axs[0,1].errorbar( mic.nm_kfn, mic.nm_e2a, yerr=mic.nm_e2a_err, marker=mic.marker, linestyle='none', label=mic.label, errorevery=mic.every )
                    axs[1,0].errorbar( mic.nm_den, mic.nm_e2a/nuda.effg(mic.nm_kfn), yerr=mic.nm_e2a_err/nuda.effg(mic.nm_kfn), marker=mic.marker, linestyle='none', label=mic.label, errorevery=mic.every )
                    axs[1,1].errorbar( mic.nm_kfn, mic.nm_e2a/nuda.effg(mic.nm_kfn), yerr=mic.nm_e2a_err/nuda.effg(mic.nm_kfn), marker=mic.marker, linestyle='none', label=mic.label, errorevery=mic.every )
                else:
                    axs[0,0].plot( mic.nm_den, mic.nm_e2a, marker=mic.marker, linestyle=None, label=mic.label, markevery=mic.every )
                    axs[0,1].plot( mic.nm_kfn, mic.nm_e2a, marker=mic.marker, linestyle=None, label=mic.label, markevery=mic.every )
                    axs[1,0].plot( mic.nm_den, mic.nm_e2a/nuda.effg(mic.nm_kfn), marker=mic.marker, linestyle=None, label=mic.label, markevery=mic.every )
                    axs[1,1].plot( mic.nm_kfn, mic.nm_e2a/nuda.effg(mic.nm_kfn), marker=mic.marker, linestyle=None, label=mic.label, markevery=mic.every )
            else:
                if mic.err:
                    axs[0,0].errorbar( mic.nm_den, mic.nm_e2a, yerr=mic.nm_e2a_err, marker=mic.marker, linestyle=mic.linestyle, label=mic.label, errorevery=mic.every )
                    axs[0,1].errorbar( mic.nm_kfn, mic.nm_e2a, yerr=mic.nm_e2a_err, marker=mic.marker, linestyle=mic.linestyle, label=mic.label, errorevery=mic.every )
                    axs[1,0].errorbar( mic.nm_den, mic.nm_e2a/nuda.effg(mic.nm_kfn), yerr=mic.nm_e2a_err/nuda.effg(mic.nm_kfn), marker=mic.marker, linestyle=mic.linestyle, label=mic.label, errorevery=mic.every )
                    axs[1,1].errorbar( mic.nm_kfn, mic.nm_e2a/nuda.effg(mic.nm_kfn), yerr=mic.nm_e2a_err/nuda.effg(mic.nm_kfn), marker=mic.marker, linestyle=mic.linestyle, label=mic.label, errorevery=mic.every )
                else:
                    axs[0,0].plot( mic.nm_den, mic.nm_e2a, marker=mic.marker, linestyle=mic.linestyle, label=mic.label, markevery=mic.every )
                    axs[0,1].plot( mic.nm_kfn, mic.nm_e2a, marker=mic.marker, linestyle=mic.linestyle, label=mic.label, markevery=mic.every )
                    axs[1,0].plot( mic.nm_den, mic.nm_e2a/nuda.effg(mic.nm_kfn), marker=mic.marker, linestyle=mic.linestyle, label=mic.label, markevery=mic.every )
                    axs[1,1].plot( mic.nm_kfn, mic.nm_e2a/nuda.effg(mic.nm_kfn), marker=mic.marker, linestyle=mic.linestyle, label=mic.label, markevery=mic.every )
        elif mic.e2a is not None: 
            if 'fit' in model:
                print('den:',mic.den)
                print('e2a:',mic.e2a)                
                axs[0,0].plot( mic.den, mic.e2a, marker=mic.marker, linestyle=mic.linestyle, label=mic.label, markevery=mic.every )
                axs[0,1].plot( mic.kfn, mic.e2a, marker=mic.marker, linestyle=mic.linestyle, label=mic.label, markevery=mic.every )
                axs[1,0].plot( mic.den, mic.e2a/nuda.effg(mic.kfn), marker=mic.marker, linestyle=mic.linestyle, label=mic.label, markevery=mic.every )
                axs[1,1].plot( mic.kfn, mic.e2a/nuda.effg(mic.kfn), marker=mic.marker, linestyle=mic.linestyle, label=mic.label, markevery=mic.every )
        #
        if nuda.env.verb_output: mic.print_outputs( )
        #
    axs[0,0].fill_between( band.den, y1=(band.e2a-band.e2a_std), y2=(band.e2a+band.e2a_std), color=band.color, alpha=band.alpha )
    axs[0,0].plot( band.den, (band.e2a-band.e2a_std), color='k', linestyle='dashed' )
    axs[0,0].plot( band.den, (band.e2a+band.e2a_std), color='k', linestyle='dashed' )
    axs[0,1].fill_between( band.kfn, y1=(band.e2a-band.e2a_std), y2=(band.e2a+band.e2a_std), color=band.color, alpha=band.alpha )        
    axs[0,1].plot( band.kfn, (band.e2a-band.e2a_std), color='k', linestyle='dashed' )
    axs[0,1].plot( band.kfn, (band.e2a+band.e2a_std), color='k', linestyle='dashed' )
    axs[1,0].fill_between( band.den, y1=(band.e2a-band.e2a_std)/nuda.effg(band.kfn), y2=(band.e2a+band.e2a_std)/nuda.effg(band.kfn), color=band.color, alpha=band.alpha )
    axs[1,0].plot( band.den, (band.e2a-band.e2a_std)/nuda.effg(band.kfn), color='k', linestyle='dashed' )
    axs[1,0].plot( band.den, (band.e2a+band.e2a_std)/nuda.effg(band.kfn), color='k', linestyle='dashed' )
    axs[1,1].fill_between( band.kfn, y1=(band.e2a-band.e2a_std)/nuda.effg(band.kfn), y2=(band.e2a+band.e2a_std)/nuda.effg(band.kfn), color=band.color, alpha=band.alpha )
    axs[1,1].plot( band.kfn, (band.e2a-band.e2a_std)/nuda.effg(band.kfn), color='k', linestyle='dashed' )
    axs[1,1].plot( band.kfn, (band.e2a+band.e2a_std)/nuda.effg(band.kfn), color='k', linestyle='dashed' )
    #
    axs[0,1].legend(loc='upper left',fontsize='8', ncol=2)
    #if group not in 'BHF':
    #    axs[0,1].legend(loc='upper left',fontsize='8', ncol=2)
    #
    plt.savefig(pname)
    plt.close()

def plot_eos_setupMicro_sm_e2a( pname, group, models, band ):
    #
    # plot E/A in SM
    #
    print(f'Plot name: {pname}')
    #
    fig, axs = plt.subplots(2,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.98, wspace=0.2, hspace=0.2 )
    #
    axs[0,0].set_ylabel(r'$E_{SM}/A$ (MeV)')
    axs[0,0].set_xlim([0, 0.3])
    axs[0,0].set_ylim([-20, 10])
    #
    axs[0,1].set_xlim([0, 1.5])
    axs[0,1].set_ylim([-20, 10])
    #
    axs[1,0].set_ylabel(r'$E_{SM}/E_{FFG}$')
    axs[1,0].set_xlabel(r'n (fm$^{-3}$)')
    axs[1,0].set_xlim([0, 0.3])
    axs[1,0].set_ylim([-2.0, 0.1])
    #
    axs[1,1].set_xlabel(r'$k_F$ (fm$^{-1}$)')
    axs[1,1].set_xlim([0, 1.5])
    axs[1,1].set_ylim([-2.0, 0.1])
    #
    print('\nmodels in SM:',models,'\n')
    #
    for model in models:
        #
        mic = nuda.eos.setupMicro( model = model, var2=0.0 )
        print('\nmodel:',model,'\n')
        if mic.sm_e2a is not None:
            if 'NLEFT' in model:
                axs[0,0].errorbar( mic.sm_den, mic.sm_e2adata, yerr=mic.sm_e2adata_err, linestyle = 'dotted', linewidth = 1, alpha=0.6 )
                axs[0,1].errorbar( mic.sm_kfn, mic.sm_e2adata, yerr=mic.sm_e2adata_err, linestyle = 'dotted', linewidth = 1, alpha=0.6 )
                axs[1,0].errorbar( mic.sm_den, mic.sm_e2adata/nuda.effg(mic.sm_kfn), yerr=mic.sm_e2adata_err/nuda.effg(mic.sm_kfn), linestyle = 'dotted', linewidth = 1, alpha=0.6 )
                axs[1,1].errorbar( mic.sm_kfn, mic.sm_e2adata/nuda.effg(mic.sm_kfn), yerr=mic.sm_e2adata_err/nuda.effg(mic.sm_kfn), linestyle = 'dotted', linewidth = 1, alpha=0.6 )
                #
                #den2 = 0.0001 + 0.001*np.arange(300)
                #kfn2 = nuda.kf_n( nuda.cst.half * den2 )
                #for k in range(50):
                #    param = np.array( [ mic.sm_pcerr[k,0], mic.sm_pcerr[k,1], mic.sm_pcerr[k,2] ] )
                #    axs[0,0].plot( den2, nuda.func_e2a_NLEFT2024( kfn2, *param )/nuda.effg(kfn2), label='Fit', alpha=0.1 )
                #    axs[1,0].plot( den2, nuda.func_e2a_NLEFT2024( kfn2, *param ), label='Fit', alpha=0.1 )
                #    axs[0,1].plot( kfn2, nuda.func_e2a_NLEFT2024( kfn2, *param )/nuda.effg(kfn2), alpha=0.1 )
                #    axs[1,1].plot( kfn2, nuda.func_e2a_NLEFT2024( kfn2, *param ), label='Fit', alpha=0.1 )
                axs[0,0].fill_between( mic.sm_den, y1=(mic.sm_e2a-mic.sm_e2a_err), y2=(mic.sm_e2a+mic.sm_e2a_err), alpha=0.3 )
                axs[0,1].fill_between( mic.sm_kfn, y1=(mic.sm_e2a-mic.sm_e2a_err), y2=(mic.sm_e2a+mic.sm_e2a_err), alpha=0.3 )
                axs[1,0].fill_between( mic.sm_den, y1=(mic.sm_e2a-mic.sm_e2a_err)/nuda.effg(mic.sm_kfn), y2=(mic.sm_e2a+mic.sm_e2a_err)/nuda.effg(mic.sm_kfn), alpha=0.3 )
                axs[1,1].fill_between( mic.sm_kfn, y1=(mic.sm_e2a-mic.sm_e2a_err)/nuda.effg(mic.sm_kfn), y2=(mic.sm_e2a+mic.sm_e2a_err)/nuda.effg(mic.sm_kfn), alpha=0.3 )
            if mic.marker:
                if mic.err:
                    axs[0,0].errorbar( mic.sm_den, mic.sm_e2a, yerr=mic.sm_e2a_err, marker=mic.marker, linestyle='none', label=mic.label, errorevery=mic.every )
                    axs[0,1].errorbar( mic.sm_kfn, mic.sm_e2a, yerr=mic.sm_e2a_err, marker=mic.marker, linestyle='none', label=mic.label, errorevery=mic.every )
                    axs[1,0].errorbar( mic.sm_den, mic.sm_e2a/nuda.effg(mic.sm_kfn), yerr=mic.sm_e2a_err/nuda.effg(mic.sm_kfn), marker=mic.marker, linestyle='none', label=mic.label, errorevery=mic.every )
                    axs[1,1].errorbar( mic.sm_kfn, mic.sm_e2a/nuda.effg(mic.sm_kfn), yerr=mic.sm_e2a_err/nuda.effg(mic.sm_kfn), marker=mic.marker, linestyle='none', label=mic.label, errorevery=mic.every )
                else:
                    axs[0,0].plot( mic.sm_den, mic.sm_e2a, marker=mic.marker, linestyle=None, label=mic.label, markevery=mic.every )
                    axs[0,1].plot( mic.sm_kfn, mic.sm_e2a, marker=mic.marker, linestyle=None, label=mic.label, markevery=mic.every )
                    axs[1,0].plot( mic.sm_den, mic.sm_e2a/nuda.effg(mic.sm_kfn), marker=mic.marker, linestyle=None, label=mic.label, markevery=mic.every )
                    axs[1,1].plot( mic.sm_kfn, mic.sm_e2a/nuda.effg(mic.sm_kfn), marker=mic.marker, linestyle=None, label=mic.label, markevery=mic.every )
            else:
                if mic.err:
                    axs[0,0].errorbar( mic.sm_den, mic.sm_e2a, yerr=mic.sm_e2a_err, marker=mic.marker, linestyle=mic.linestyle, label=mic.label, errorevery=mic.every )
                    axs[0,1].errorbar( mic.sm_kfn, mic.sm_e2a, yerr=mic.sm_e2a_err, marker=mic.marker, linestyle=mic.linestyle, label=mic.label, errorevery=mic.every )
                    axs[1,0].errorbar( mic.sm_den, mic.sm_e2a/nuda.effg(mic.sm_kfn), yerr=mic.sm_e2a_err/nuda.effg(mic.sm_kfn), marker=mic.marker, linestyle=mic.linestyle, label=mic.label, errorevery=mic.every )
                    axs[1,1].errorbar( mic.sm_kfn, mic.sm_e2a/nuda.effg(mic.sm_kfn), yerr=mic.sm_e2a_err/nuda.effg(mic.sm_kfn), marker=mic.marker, linestyle=mic.linestyle, label=mic.label, errorevery=mic.every )
                else:
                    axs[0,0].plot( mic.sm_den, mic.sm_e2a, marker=mic.marker, linestyle=mic.linestyle, label=mic.label, markevery=mic.every )
                    axs[0,1].plot( mic.sm_kfn, mic.sm_e2a, marker=mic.marker, linestyle=mic.linestyle, label=mic.label, markevery=mic.every )
                    axs[1,0].plot( mic.sm_den, mic.sm_e2a/nuda.effg(mic.sm_kfn), marker=mic.marker, linestyle=mic.linestyle, label=mic.label, markevery=mic.every )
                    axs[1,1].plot( mic.sm_kfn, mic.sm_e2a/nuda.effg(mic.sm_kfn), marker=mic.marker, linestyle=mic.linestyle, label=mic.label, markevery=mic.every )
        elif mic.e2a is not None: 
            if 'fit' in model:
                axs[0,0].plot( mic.den, mic.e2a, marker=mic.marker, linestyle=mic.linestyle, label=mic.label, markevery=mic.every )
                axs[0,1].plot( mic.kfn, mic.e2a, marker=mic.marker, linestyle=mic.linestyle, label=mic.label, markevery=mic.every )
                axs[1,0].plot( mic.den, mic.e2a/nuda.effg(mic.kfn), marker=mic.marker, linestyle=mic.linestyle, label=mic.label, markevery=mic.every )
                axs[1,1].plot( mic.kfn, mic.e2a/nuda.effg(mic.kfn), marker=mic.marker, linestyle=mic.linestyle, label=mic.label, markevery=mic.every )
        #
        mic.print_outputs( )
        #
    axs[0,0].fill_between( band.den, y1=(band.e2a-band.e2a_std), y2=(band.e2a+band.e2a_std), color=band.color, alpha=band.alpha )
    axs[0,0].plot( band.den, (band.e2a-band.e2a_std), color='k', linestyle='dashed' )
    axs[0,0].plot( band.den, (band.e2a+band.e2a_std), color='k', linestyle='dashed' )
    axs[0,1].fill_between( band.kfn, y1=(band.e2a-band.e2a_std), y2=(band.e2a+band.e2a_std), color=band.color, alpha=band.alpha )        
    axs[0,1].plot( band.kfn, (band.e2a-band.e2a_std), color='k', linestyle='dashed' )
    axs[0,1].plot( band.kfn, (band.e2a+band.e2a_std), color='k', linestyle='dashed' )
    axs[1,0].fill_between( band.den, y1=(band.e2a-band.e2a_std)/nuda.effg(band.kfn), y2=(band.e2a+band.e2a_std)/nuda.effg(band.kfn), color=band.color, alpha=band.alpha )
    axs[1,0].plot( band.den, (band.e2a-band.e2a_std)/nuda.effg(band.kfn), color='k', linestyle='dashed' )
    axs[1,0].plot( band.den, (band.e2a+band.e2a_std)/nuda.effg(band.kfn), color='k', linestyle='dashed' )
    axs[1,1].fill_between( band.kfn, y1=(band.e2a-band.e2a_std)/nuda.effg(band.kfn), y2=(band.e2a+band.e2a_std)/nuda.effg(band.kfn), color=band.color, alpha=band.alpha )
    axs[1,1].plot( band.kfn, (band.e2a-band.e2a_std)/nuda.effg(band.kfn), color='k', linestyle='dashed' )
    axs[1,1].plot( band.kfn, (band.e2a+band.e2a_std)/nuda.effg(band.kfn), color='k', linestyle='dashed' )
    #
    axs[0,1].legend(loc='upper left',fontsize='8', ncol=2)
    #if group not in 'BHF':
    #    axs[0,1].legend(loc='upper left',fontsize='8', ncol=2)
    #
    plt.savefig(pname)
    plt.close()


def main():
    #
    print(50*'-')
    print("Enter plot_eos_setupMicro.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    # 
    # ===============================
    # Neutron Matter (NM)
    # ===============================
    #
    # fix the uncertainty band in NM
    #
    bmodels = [ '2016-MBPT-AM', '2016-QMC-NM', '2020-MBPT-AM' ]
    #
    band = nuda.eos.setupMicroBand( bmodels )
    #
    # create the groups for the figures
    #
    groups = [ 'VAR', 'AFDMC', 'BHF', 'QMC', 'MBPT', 'NLEFT' ]
    #groups = [ 'VAR' ]
    #groups = [ 'NLEFT' ]
    #
    # list the available models
    #
    #models, models_lower = nuda.eos_micro_models()
    #
    # plot E/A in NM
    #
    for i,group in enumerate(groups):
        #
        print('For group:',group)
        #
        pname = 'figs/plot_eos_setupMicro_e2a_NM_'+group+'.png'
        print('pname:',pname)
        #
        # list the available models in groups
        #
        models, models_lower = nuda.eos.micro_models_group_NM( group )
        #
        print('models:',models)
        plot_eos_setupMicro_nm_e2a( pname, group, models, band )
        #
    #
    # ===============================
    # Symmetric Matter (SM)
    # ===============================
    #
    # fix the uncertainty band in SM
    #
    bmodels = [ '2016-MBPT-AM', '2020-MBPT-AM' ]
    #
    band = nuda.eos.setupMicroBand( bmodels, matter='SM' )
    #
    # create the groups for the figures
    #
    groups = [ 'VAR', 'AFDMC', 'BHF', 'QMC', 'MBPT', 'NLEFT' ]
    #groups = [ 'VAR' ]
    #groups = [ 'NLEFT' ]
    #
    # plot E/A in SM
    #
    for i,group in enumerate(groups):
        #
        print('For group:',group)
        #
        pname = 'figs/plot_SetupEOSMicro_e2a_SM_'+group+'.png'
        print('pname:',pname)
        #
        # list the available models in groups
        #
        models, models_lower = nuda.eos.micro_models_group_SM( group )
        #
        print('models:',models)
        #
        plot_eos_setupMicro_sm_e2a( pname, group, models, band )
        #
    #
    print(50*'-')
    print("Exit plot_eos_setupMicro.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
