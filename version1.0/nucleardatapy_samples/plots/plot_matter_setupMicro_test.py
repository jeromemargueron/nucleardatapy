
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plot_matter_setupMicro_nm_e2a_test( pname, group, models, band ):
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
    axs[0,0].set_ylim([10, 35])
    #
    axs[0,1].set_xlim([1.0, 2.0])
    axs[0,1].set_ylim([10, 35])
    #
    axs[1,0].set_xlabel(r'n (fm$^{-3}$)')
    axs[1,0].set_ylabel(r'$E_{NM}/E_{FFG,NR}$')
    axs[1,0].set_xlim([0, 0.3])
    axs[1,0].set_ylim([0.4, 0.7])
    #
    axs[1,1].set_xlabel(r'$k_F$ (fm$^{-1}$)')
    axs[1,1].set_xlim([1.0, 2.0])
    axs[1,1].set_ylim([0.4, 0.7])
    #
    #print('\nmodels in NM:',models,'\n')
    #
    kres = 1
    kfit = 1
    for model in models:
        #
        mic = nuda.matter.setupMicro( model = model, var2=1.0 )
        print('model:',model)
        print('marker:',mic.marker)
        print('err:',mic.err)
        if mic.nm_e2a is not None:
            if 'RES' in model:
                axs[0,0].errorbar( mic.nm_den, mic.nm_e2a, yerr=mic.nm_e2a_err, marker=mic.marker, markevery=mic.every, color=nuda.param.col[kres], linestyle=mic.linestyle, label=mic.label, errorevery=mic.every )
                axs[0,1].errorbar( mic.nm_kfn, mic.nm_e2a, yerr=mic.nm_e2a_err, marker=mic.marker, markevery=mic.every, color=nuda.param.col[kres], linestyle=mic.linestyle, errorevery=mic.every )
                axs[1,0].errorbar( mic.nm_den, mic.nm_e2a/nuda.effg_nr(mic.nm_kfn), yerr=mic.nm_e2a_err/nuda.effg_nr(mic.nm_kfn), marker=mic.marker, markevery=mic.every, color=nuda.param.col[kres], linestyle=mic.linestyle, errorevery=mic.every )
                axs[1,1].errorbar( mic.nm_kfn, mic.nm_e2a/nuda.effg_nr(mic.nm_kfn), yerr=mic.nm_e2a_err/nuda.effg_nr(mic.nm_kfn), marker=mic.marker, markevery=mic.every, color=nuda.param.col[kres], linestyle=mic.linestyle, errorevery=mic.every )
                kres += 1
            if 'FIT' in model:
                axs[0,0].plot( mic.nm_den, mic.nm_e2a, color=nuda.param.col[kfit], linestyle=mic.linestyle, label=mic.label )
                axs[0,1].plot( mic.nm_kfn, mic.nm_e2a, color=nuda.param.col[kfit], linestyle=mic.linestyle )
                axs[1,0].plot( mic.nm_den, mic.nm_e2a/nuda.effg_nr(mic.nm_kfn), color=nuda.param.col[kfit], linestyle=mic.linestyle )
                axs[1,1].plot( mic.nm_kfn, mic.nm_e2a/nuda.effg_nr(mic.nm_kfn), color=nuda.param.col[kfit], linestyle=mic.linestyle )
                kfit += 1
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
    #if group not in 'BHF':
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
    print("Enter plot_matter_setupMicro_AFDMC.py:")
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
    band = nuda.matter.setupMicroBand( bmodels )
    #
    # create the groups for the figures
    #
    groups = [ 'AFDMC' ]
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
        pname = 'figs/plot_matter_setupMicro_e2a_NM_'+group+'-test.png'
        print('pname:',pname)
        #
        # list the available models in groups
        #
        models, models_lower = nuda.matter.micro_models_group_NM( group )
        #
        print('models:',models)
        plot_matter_setupMicro_nm_e2a_test( pname, group, models, band )
        #
    #
    print(50*'-')
    print("Exit plot_matter_setupMicro.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
