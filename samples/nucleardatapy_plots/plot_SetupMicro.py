
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plotMicro_e2a( pname, group, models, band ):
    #
    # plot E/A in NM
    #
    print(f'Plot name: {pname}')
    #
    fig, axs = plt.subplots(2,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.98, wspace=0.2, hspace=0.2 )
    #
    axs[0,0].set_ylabel(r'$E_{NM}/E_{FFG}$')
    axs[0,0].set_xlim([0, 0.3])
    axs[0,0].set_ylim([0.2, 0.9])
    #
    axs[1,0].set_xlabel(r'n (fm$^{-3}$)')
    axs[1,0].set_ylabel(r'$E_{NM}/A$ (MeV)')
    axs[1,0].set_xlim([0, 0.3])
    axs[1,0].set_ylim([0, 30])
    #
    #axs[0,1].set_ylabel(r'$\Delta/E_F$')
    axs[0,1].set_xlim([0, 1.5])
    axs[0,1].set_ylim([0.2, 0.9])
    #
    axs[1,1].set_xlabel(r'$k_F$ (fm$^{-1}$)')
    #axs[1,1].set_ylabel(r'$\Delta$ (MeV)')
    axs[1,1].set_xlim([0, 1.5])
    axs[1,1].set_ylim([0, 10.0])
    #
    for model in models:
        #
        mic = nuda.SetupMicro( model = model )
        if mic.nm_e2a is not None: 
            print('model:',model)
            if mic.marker:
                if mic.err:
                    axs[0,0].errorbar( mic.nm_den, mic.nm_e2a/nuda.effg(mic.nm_kfn), yerr=mic.nm_e2a_err/nuda.effg(mic.nm_kfn), marker=mic.marker, linestyle=None, label=mic.label, errorevery=mic.every )
                    axs[1,0].errorbar( mic.nm_den, mic.nm_e2a, yerr=mic.nm_e2a_err, marker=mic.marker, linestyle=None, label=mic.label, errorevery=mic.every )
                    axs[0,1].errorbar( mic.nm_kfn, mic.nm_e2a/nuda.effg(mic.nm_kfn), yerr=mic.nm_e2a_err/nuda.effg(mic.nm_kfn), marker=mic.marker, linestyle=None, label=mic.label, errorevery=mic.every )
                    axs[1,1].errorbar( mic.nm_kfn, mic.nm_e2a, yerr=mic.nm_e2a_err, marker=mic.marker, linestyle=None, label=mic.label, errorevery=mic.every )
                else:
                    axs[0,0].plot( mic.nm_den, mic.nm_e2a/nuda.effg(mic.nm_kfn), marker=mic.marker, linestyle=None, label=mic.label, markevery=mic.every )
                    axs[1,0].plot( mic.nm_den, mic.nm_e2a, marker=mic.marker, linestyle=None, label=mic.label, markevery=mic.every )
                    axs[0,1].plot( mic.nm_kfn, mic.nm_e2a/nuda.effg(mic.nm_kfn), marker=mic.marker, linestyle=None, label=mic.label, markevery=mic.every )
                    axs[1,1].plot( mic.nm_kfn, mic.nm_e2a, marker=mic.marker, linestyle=None, label=mic.label, markevery=mic.every )
            else:
                if mic.err:
                    axs[0,0].errorbar( mic.nm_den, mic.nm_e2a/nuda.effg(mic.nm_kfn), yerr=mic.nm_e2a_err/nuda.effg(mic.nm_kfn), marker=mic.marker, linestyle=mic.linestyle, label=mic.label, errorevery=mic.every )
                    axs[1,0].errorbar( mic.nm_den, mic.nm_e2a, yerr=mic.nm_e2a_err, marker=mic.marker, linestyle=mic.linestyle, label=mic.label, errorevery=mic.every )
                    axs[0,1].errorbar( mic.nm_kfn, mic.nm_e2a/nuda.effg(mic.nm_kfn), yerr=mic.nm_e2a_err/nuda.effg(mic.nm_kfn), marker=mic.marker, linestyle=mic.linestyle, label=mic.label, errorevery=mic.every )
                    axs[1,1].errorbar( mic.nm_kfn, mic.nm_e2a, yerr=mic.nm_e2a_err, marker=mic.marker, linestyle=mic.linestyle, label=mic.label, errorevery=mic.every )
                else:
                    axs[0,0].plot( mic.nm_den, mic.nm_e2a/nuda.effg(mic.nm_kfn), marker=mic.marker, linestyle=mic.linestyle, label=mic.label, markevery=mic.every )
                    axs[1,0].plot( mic.nm_den, mic.nm_e2a, marker=mic.marker, linestyle=mic.linestyle, label=mic.label, markevery=mic.every )
                    axs[0,1].plot( mic.nm_kfn, mic.nm_e2a/nuda.effg(mic.nm_kfn), marker=mic.marker, linestyle=mic.linestyle, label=mic.label, markevery=mic.every )
                    axs[1,1].plot( mic.nm_kfn, mic.nm_e2a, marker=mic.marker, linestyle=mic.linestyle, label=mic.label, markevery=mic.every )

        mic.print_outputs( )
        axs[0,0].fill_between( band.den, y1=(band.e2a-band.e2a_std)/nuda.effg(band.kfn), y2=(band.e2a+band.e2a_std)/nuda.effg(band.kfn), color=band.color, alpha=band.alpha )
        axs[0,0].plot( band.den, (band.e2a-band.e2a_std)/nuda.effg(band.kfn), color='k', linestyle='dashed' )
        axs[0,0].plot( band.den, (band.e2a+band.e2a_std)/nuda.effg(band.kfn), color='k', linestyle='dashed' )
        axs[1,0].fill_between( band.den, y1=(band.e2a-band.e2a_std), y2=(band.e2a+band.e2a_std), color=band.color, alpha=band.alpha )
        axs[1,0].plot( band.den, (band.e2a-band.e2a_std), color='k', linestyle='dashed' )
        axs[1,0].plot( band.den, (band.e2a+band.e2a_std), color='k', linestyle='dashed' )
        axs[0,1].fill_between( band.kfn, y1=(band.e2a-band.e2a_std)/nuda.effg(band.kfn), y2=(band.e2a+band.e2a_std)/nuda.effg(band.kfn), color=band.color, alpha=band.alpha )
        axs[0,1].plot( band.kfn, (band.e2a-band.e2a_std)/nuda.effg(band.kfn), color='k', linestyle='dashed' )
        axs[0,1].plot( band.kfn, (band.e2a+band.e2a_std)/nuda.effg(band.kfn), color='k', linestyle='dashed' )
        axs[1,1].fill_between( band.kfn, y1=(band.e2a-band.e2a_std), y2=(band.e2a+band.e2a_std), color=band.color, alpha=band.alpha )        
        axs[1,1].plot( band.kfn, (band.e2a-band.e2a_std), color='k', linestyle='dashed' )
        axs[1,1].plot( band.kfn, (band.e2a+band.e2a_std), color='k', linestyle='dashed' )
    #
    #axs[0,1].legend(loc='upper left',fontsize='8', ncol=2)
    if group not in 'BHF':
        axs[0,1].legend(loc='upper left',fontsize='8', ncol=2)
    #
    plt.savefig(pname)
    plt.close()

def plotMicro_gap( pname, models ):
    #
    # plot pairing gap in NM
    #
    print(f'Plot name: {pname}')
    #
    fig, axs = plt.subplots(2,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.98, wspace=0.2, hspace=0.2 )
    #
    #axs[0,0].set_ylabel(r'$E_{NM}/E_{FFG}$')
    axs[0,0].set_ylabel(r'$\Delta/E_F$')
    axs[0,0].set_xlim([0, 0.05])
    axs[0,0].set_ylim([0, 0.8])
    #
    axs[1,0].set_xlabel(r'n (fm$^{-3}$)')
    axs[1,0].set_ylabel(r'$\Delta$ (MeV)')
    axs[1,0].set_xlim([0, 0.05])
    axs[1,0].set_ylim([0, 2.8])
    #
    #axs[0,1].set_ylabel(r'$\Delta/E_F$')
    axs[0,1].set_xlim([0, 1.4])
    axs[0,1].set_ylim([0, 0.8])
    #
    axs[1,1].set_xlabel(r'$k_F$ (fm$^{-1}$)')
    #axs[1,1].set_ylabel(r'$\Delta$ (MeV)')
    axs[1,1].set_xlim([0, 1.4])
    axs[1,1].set_ylim([0, 2.8])
    #
    for model in models:
        #
        mic = nuda.SetupMicro( model = model )
        if mic.nm_gap is not None: 
            axs[0,0].plot( mic.nm_den, mic.nm_gap/nuda.eF_n(mic.nm_kfn), marker=mic.marker, linestyle=mic.linestyle, label=mic.label )
            axs[1,0].plot( mic.nm_den, mic.nm_gap, marker=mic.marker, linestyle=mic.linestyle, label=mic.label )
            axs[0,1].plot( mic.nm_kfn, mic.nm_gap/nuda.eF_n(mic.nm_kfn), marker=mic.marker, linestyle=mic.linestyle, label=mic.label )
            axs[1,1].plot( mic.nm_kfn, mic.nm_gap, marker=mic.marker, linestyle=mic.linestyle, label=mic.label )
        mic.print_outputs( )
    #
    axs[0,0].legend(loc='upper right',fontsize='8')
    #
    plt.savefig(pname)
    plt.close()


def main():
    #
    print(50*'-')
    print("Enter plot_SetupMicro.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    # fix the uncertainty band
    #
    bmodels = [ '2016-MBPT-AM', '2016-QMC-NM', '2020-MBPT-AM' ]
    #
    band = nuda.SetupMicroBand( bmodels )
    #
    # create the groups for the figures
    #
    groups = [ 'VAR', 'AFDMC', 'BHF', 'QMC', 'MBPT' ]
    #
    # list the available models
    #
    models, models_lower = nuda.models_micro()
    #
    # plot pairing gaps in NM
    #
    pname = 'figs/plot_SetupMicro_gap_NM.png'
    plotMicro_gap( pname, models )
    #
    # plot E/A in NM
    #
    for i,group in enumerate(groups):
        #
        pname = 'figs/plot_SetupMicro_e2a_NM_'+group+'.png'
        #
        models2 = []
        #models2 = [ '1981-VAR-AM-FP', '1998-VAR-AM-APR' ]
        #
        for j,model in enumerate(models):
            if group in model and '2BF' not in model:
                models2.append( model )
        #
        print('models2:',models2)
        print('pname:',pname)
        #
        plotMicro_e2a( pname, group, models2, band )
    #
    print(50*'-')
    print("Exit plot_SetupMicro.py:")
    print(50*'-')
    #

    
if __name__ == "__main__":
    main()
