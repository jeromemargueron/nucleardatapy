
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plotMicro_e2a( pname, models ):
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
    axs[0,0].set_ylim([0, 1.0])
    #
    axs[1,0].set_xlabel(r'n (fm$^{-3}$)')
    axs[1,0].set_ylabel(r'$E_{NM}/A$ (MeV)')
    axs[1,0].set_xlim([0, 0.3])
    axs[1,0].set_ylim([0, 28])
    #
    #axs[0,1].set_ylabel(r'$\Delta/E_F$')
    axs[0,1].set_xlim([0, 0.65])
    axs[0,1].set_ylim([0, 1.0])
    #
    axs[1,1].set_xlabel(r'k_F (fm$^{-1}$)')
    #axs[1,1].set_ylabel(r'$\Delta$ (MeV)')
    axs[1,1].set_xlim([0, 0.65])
    axs[1,1].set_ylim([0, 2.5])
    #
    for model in models:
        #
        mic = nuda.SetupMicro( model = model )
        if mic.nm_e2a is not None: 
            print('model:',model)
            axs[0,0].plot( mic.nm_den, mic.nm_e2a/nuda.effg(mic.nm_kfn), linestyle=mic.linestyle, label=mic.label )
            axs[1,0].plot( mic.nm_den, mic.nm_e2a, linestyle=mic.linestyle, label=mic.label )
            axs[0,1].plot( mic.nm_kfn, mic.nm_e2a/nuda.eF_n(mic.nm_kfn), linestyle=mic.linestyle, label=mic.label )
            axs[1,1].plot( mic.nm_kfn, mic.nm_e2a, linestyle=mic.linestyle, label=mic.label )
        mic.print_outputs( )
    #
    axs[1,1].legend(loc='upper left',fontsize='xx-small', ncol=2)
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
    axs[0,0].set_xlim([0, 0.08])
    axs[0,0].set_ylim([0, 1.0])
    #
    axs[1,0].set_xlabel(r'n (fm$^{-3}$)')
    axs[1,0].set_ylabel(r'$\Delta$ (MeV)')
    axs[1,0].set_xlim([0, 0.08])
    axs[1,0].set_ylim([0, 2.8])
    #
    #axs[0,1].set_ylabel(r'$\Delta/E_F$')
    axs[0,1].set_xlim([0, 0.65])
    axs[0,1].set_ylim([0, 1.0])
    #
    axs[1,1].set_xlabel(r'k_F (fm$^{-1}$)')
    #axs[1,1].set_ylabel(r'$\Delta$ (MeV)')
    axs[1,1].set_xlim([0, 0.65])
    axs[1,1].set_ylim([0, 2.5])
    #
    #
    for model in models:
        #
        mic = nuda.SetupMicro( model = model )
        if mic.nm_gap is not None: 
            axs[0,0].plot( mic.nm_den, mic.nm_gap/nuda.effg(mic.nm_kfn), linestyle=mic.linestyle, label=mic.label )
            axs[1,0].plot( mic.nm_den, mic.nm_gap, linestyle=mic.linestyle, label=mic.label )
            axs[0,1].plot( mic.nm_kfn, mic.nm_gap/nuda.eF_n(mic.nm_kfn), linestyle=mic.linestyle, label=mic.label )
            axs[1,1].plot( mic.nm_kfn, mic.nm_gap, linestyle=mic.linestyle, label=mic.label )
        mic.print_outputs( )
    #
    axs[1,1].legend(loc='upper left',fontsize='xx-small')
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
    groups = [ 'AFDMC', 'BHF', 'QMC', 'MBPT' ]
    #
    models, models_lower = nuda.models_micro()
    #
    # plot pairing gaps in NM
    #
    pname = 'figs/plot_SetupMicro_gap_NM_.png'
    plotMicro_gap( pname, models )
    #
    # plot E/A in NM
    #
    for i,group in enumerate(groups):
        #
        pname = 'figs/plot_SetupMicro_e2a_NM_'+group+'.png'
        #
        models2 = [ '1981-VAR-AM-FP', '1998-VAR-AM-APR' ]
        for j,model in enumerate(models):
            if group in model:
                models2.append( model )
        #
        print('models2:',models2)
        print('pname:',pname)
        #
        plotMicro_e2a( pname, models2 )
    #
    print(50*'-')
    print("Exit plot_SetupMicro.py:")
    print(50*'-')
    #

    
if __name__ == "__main__":
    main()
