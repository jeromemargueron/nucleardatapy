
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plot_eos_setupMicro_nm_gap_1s0( pname, models ):
    #
    # plot 1S0 pairing gap in NM
    #
    print(f'Plot name: {pname}')
    print('models:',models)
    #
    fig, axs = plt.subplots(2,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.98, wspace=0.2, hspace=0.2 )
    #
    axs[0,0].set_ylabel(r'$\Delta_{1S0}$ (MeV)')
    axs[0,0].set_xlim([0, 0.05])
    axs[0,0].set_ylim([0, 3.0])
    #
    axs[0,1].set_xlim([0, 1.6])
    axs[0,1].set_ylim([0, 3.0])
    #
    axs[1,0].set_ylabel(r'$\Delta_{1S0}/E_F$')
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
        gap = nuda.eos.setupMicroGap( model = model )
        #
        if gap.nm_gap_1s0 is not None:
            if gap.nm_gap_1s0_err is not None:
                axs[0,0].errorbar( gap.nm_den_1s0, gap.nm_gap_1s0, yerr=gap.nm_gap_1s0_err, marker=gap.marker, linestyle='none', label=gap.label )
                axs[0,1].errorbar( gap.nm_kfn_1s0, gap.nm_gap_1s0, yerr=gap.nm_gap_1s0_err, marker=gap.marker, linestyle='none', label=gap.label )
                axs[1,0].errorbar( gap.nm_den_1s0, gap.nm_gap_1s0/nuda.eF_n(gap.nm_kfn_1s0), yerr=gap.nm_gap_1s0_err/nuda.eF_n(gap.nm_kfn_1s0), marker=gap.marker, linestyle='none', label=gap.label )
                axs[1,1].errorbar( gap.nm_kfn_1s0, gap.nm_gap_1s0/nuda.eF_n(gap.nm_kfn_1s0), yerr=gap.nm_gap_1s0_err/nuda.eF_n(gap.nm_kfn_1s0), marker=gap.marker, linestyle='none', label=gap.label )
            else:
                axs[0,0].plot( gap.nm_den_1s0, gap.nm_gap_1s0, marker=gap.marker, linestyle='none', label=gap.label )
                axs[0,1].plot( gap.nm_kfn_1s0, gap.nm_gap_1s0, marker=gap.marker, linestyle='none', label=gap.label )
                axs[1,0].plot( gap.nm_den_1s0, gap.nm_gap_1s0/nuda.eF_n(gap.nm_kfn_1s0), marker=gap.marker, linestyle='none', label=gap.label )
                axs[1,1].plot( gap.nm_kfn_1s0, gap.nm_gap_1s0/nuda.eF_n(gap.nm_kfn_1s0), marker=gap.marker, linestyle='none', label=gap.label )
        if nuda.env.verb_output: gap.print_outputs( )
    #
    axs[1,0].legend(loc='upper right',fontsize='8')
    #
    plt.savefig(pname)
    plt.close()

def plot_eos_setupMicro_nm_gap_3pf2( pname, models ):
    #
    # plot 3PF2 pairing gap in NM
    #
    print(f'Plot name: {pname}')
    print('models:',models)
    #
    fig, axs = plt.subplots(2,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.98, wspace=0.2, hspace=0.2 )
    #
    axs[0,0].set_ylabel(r'$\Delta_{3PF2}$ (MeV)')
    axs[0,0].set_xlim([0, 0.4])
    axs[0,0].set_ylim([0, 0.6])
    #
    axs[0,1].set_xlim([0.8, 2.3])
    axs[0,1].set_ylim([0, 0.6])
    #
    axs[1,0].set_ylabel(r'$100\times \Delta_{3PF2}/E_F$')
    axs[1,0].set_xlabel(r'n (fm$^{-3}$)')
    axs[1,0].set_xlim([0, 0.4])
    axs[1,0].set_ylim([0, 0.8])
    #
    axs[1,1].set_xlabel(r'$k_F$ (fm$^{-1}$)')
    axs[1,1].set_xlim([0.8, 2.3])
    axs[1,1].set_ylim([0, 0.8])
    #
    for model in models:
        #
        gap = nuda.eos.setupMicroGap( model = model )
        #
        if gap.nm_gap_3pf2 is not None:
            if gap.nm_gap_3pf2_err is not None:
                axs[0,0].errorbar( gap.nm_den_3pf2, gap.nm_gap_3pf2, yerr=gap.nm_gap_3pf2_err, marker=gap.marker, linestyle='none', label=gap.label )
                axs[0,1].errorbar( gap.nm_kfn_3pf2, gap.nm_gap_3pf2, yerr=gap.nm_gap_3pf2_err, marker=gap.marker, linestyle='none', label=gap.label )
                axs[1,0].errorbar( gap.nm_den_3pf2, 100*gap.nm_gap_3pf2/nuda.eF_n(gap.nm_kfn_3pf2), yerr=gap.nm_gap_3pf2_err/nuda.eF_n(gap.nm_kfn_3pf2), marker=gap.marker, linestyle='none', label=gap.label )
                axs[1,1].errorbar( gap.nm_kfn_3pf2, 100*gap.nm_gap_3pf2/nuda.eF_n(gap.nm_kfn_3pf2), yerr=gap.nm_gap_3pf2_err/nuda.eF_n(gap.nm_kfn_3pf2), marker=gap.marker, linestyle='none', label=gap.label )
            else:
                axs[0,0].plot( gap.nm_den_3pf2, gap.nm_gap_3pf2, marker=gap.marker, linestyle='none', label=gap.label )
                axs[0,1].plot( gap.nm_kfn_3pf2, gap.nm_gap_3pf2, marker=gap.marker, linestyle='none', label=gap.label )
                axs[1,0].plot( gap.nm_den_3pf2, 100*gap.nm_gap_3pf2/nuda.eF_n(gap.nm_kfn_3pf2), marker=gap.marker, linestyle='none', label=gap.label )
                axs[1,1].plot( gap.nm_kfn_3pf2, 100*gap.nm_gap_3pf2/nuda.eF_n(gap.nm_kfn_3pf2), marker=gap.marker, linestyle='none', label=gap.label )
        if nuda.env.verb_output: gap.print_outputs( )
    #
    axs[1,0].legend(loc='upper right',fontsize='8')
    #
    plt.savefig(pname)
    plt.close()

def main():
    #
    print(50*'-')
    print("Enter plot_eos_setupMicroGap.py:")
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
    # list the available models
    #
    models, models_lower = nuda.eos.micro_gap_models()
    #
    # plot 1S0 pairing gaps in NM
    #
    pname = 'figs/plot_eos_setupMicro_gap_1s0_NM.png'
    #
    plot_eos_setupMicro_nm_gap_1s0( pname, models )
    #
    # plot 3PF2 pairing gaps in NM
    #
    pname = 'figs/plot_eos_setupMicro_gap_3pf2_NM.png'
    #
    plot_eos_setupMicro_nm_gap_3pf2( pname, models )
    #
    print(50*'-')
    print("Exit plot_eos_setupMicroGap.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
