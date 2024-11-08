
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plotMicro_nm_gap( pname, models ):
    #
    # plot pairing gap in NM
    #
    print(f'Plot name: {pname}')
    print('models:',models)
    #
    fig, axs = plt.subplots(2,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.98, wspace=0.2, hspace=0.2 )
    #
    axs[0,0].set_ylabel(r'$\Delta$ (MeV)')
    axs[0,0].set_xlim([0, 0.05])
    axs[0,0].set_ylim([0, 2.8])
    #
    axs[0,1].set_xlim([0, 1.6])
    axs[0,1].set_ylim([0, 2.8])
    #
    axs[1,0].set_ylabel(r'$\Delta/E_F$')
    axs[1,0].set_xlabel(r'n (fm$^{-3}$)')
    axs[1,0].set_xlim([0, 0.05])
    axs[1,0].set_ylim([0, 0.8])
    #
    axs[1,1].set_xlabel(r'$k_F$ (fm$^{-1}$)')
    axs[1,1].set_xlim([0, 1.6])
    axs[1,1].set_ylim([0, 0.8])
    #
    for model in models:
        #
        mic = nuda.SetupMicroMatter( model = model )
        #
        if mic.gap_nm_gap is not None:
            if mic.gap_err:
                axs[0,0].errorbar( mic.gap_nm_den, mic.gap_nm_gap, yerr=mic.gap_nm_gap_err, marker=mic.marker, linestyle='none', label=mic.label )
                axs[0,1].errorbar( mic.gap_nm_kfn, mic.gap_nm_gap, yerr=mic.gap_nm_gap_err, marker=mic.marker, linestyle='none', label=mic.label )
                axs[1,0].errorbar( mic.gap_nm_den, mic.gap_nm_gap/nuda.eF_n(mic.gap_nm_kfn), yerr=mic.gap_nm_gap_err/nuda.eF_n(mic.gap_nm_kfn), marker=mic.marker, linestyle='none', label=mic.label )
                axs[1,1].errorbar( mic.gap_nm_kfn, mic.gap_nm_gap/nuda.eF_n(mic.gap_nm_kfn), yerr=mic.gap_nm_gap_err/nuda.eF_n(mic.gap_nm_kfn), marker=mic.marker, linestyle='none', label=mic.label )
            else:
                axs[0,0].plot( mic.gap_nm_den, mic.gap_nm_gap, marker=mic.marker, linestyle='none', label=mic.label )
                axs[0,1].plot( mic.gap_nm_kfn, mic.gap_nm_gap, marker=mic.marker, linestyle='none', label=mic.label )
                axs[1,0].plot( mic.gap_nm_den, mic.gap_nm_gap/nuda.eF_n(mic.gap_nm_kfn), marker=mic.marker, linestyle='none', label=mic.label )
                axs[1,1].plot( mic.gap_nm_kfn, mic.gap_nm_gap/nuda.eF_n(mic.gap_nm_kfn), marker=mic.marker, linestyle='none', label=mic.label )
        #mic.print_outputs( )
        #
    #
    axs[1,0].legend(loc='upper right',fontsize='8')
    #
    plt.savefig(pname)
    plt.close()


def main():
    #
    print(50*'-')
    print("Enter plot_SetupMicroMatterGap.py:")
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
    # create the groups for the figures
    #
    groups = [ 'VAR', 'AFDMC', 'BHF', 'QMC', 'MBPT', 'NLEFT' ]
    #groups = [ 'VAR' ]
    #groups = [ 'NLEFT' ]
    #
    # list the available models
    #
    models, models_lower = nuda.models_micro_matter()
    #
    # plot pairing gaps in NM
    #
    pname = 'figs/plot_SetupMicroMatter_gap_NM.png'
    #
    plotMicro_nm_gap( pname, models )
    #
    print(50*'-')
    print("Exit plot_SetupMicroGap.py:")
    print(50*'-')
    #

    
if __name__ == "__main__":
    main()
