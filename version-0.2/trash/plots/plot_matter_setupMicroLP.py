
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plot_matter_setupMicroLP0_SM( pname, models ):
    #
    # plot Landau Parameters in SM
    #
    print(f'Plot name: {pname}')
    #
    fig, axs = plt.subplots(2,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=0.98, top=0.98, wspace=0.15, hspace=0.05 )
    #
    axs[0,0].set_ylabel(r'$F_0$')
    axs[0,0].set_xlim([0, 2.0])
    axs[0,0].set_ylim([-1, 1.8])
    #
    axs[0,1].set_ylabel(r'$G_0$')
    axs[0,1].set_xlim([0, 2.0])
    axs[0,1].set_ylim([-1, 1.8])
    #
    axs[1,0].set_ylabel(r'$F_0^\prime$')
    axs[1,0].set_xlabel(r'$k_F$ (fm$^{-1}$)')
    axs[1,0].set_xlim([0, 2.0])
    axs[1,0].set_ylim([-1, 1.8])
    #
    axs[1,1].set_ylabel(r'$G_0^\prime$')
    axs[1,1].set_xlabel(r'$k_F$ (fm$^{-1}$)')
    axs[1,1].set_xlim([0, 2.0])
    axs[1,1].set_ylim([-1, 1.8])
    #
    axs[0,0].tick_params('x', labelbottom=False)
    axs[0,1].tick_params('x', labelbottom=False)
    axs[0,1].tick_params('y', labelleft=False)
    axs[1,1].tick_params('y', labelleft=False)
    #
    for model in models:
        #
        mic = nuda.matter.setupMicroLP( model = model )
        if mic.sm_kfn is not None and '-SM-' in model: 
            print('\nmodel:',model,'\n')
            if mic.err:
                axs[0,0].errorbar( mic.sm_kfn, mic.sm_LP['F'][0], yerr=mic.sm_LP_F_err[0], marker=mic.marker, linestyle='none', label=mic.label )
                axs[0,1].errorbar( mic.sm_kfn, mic.sm_LP['G'][0], yerr=mic.sm_LP_G_err[0], marker=mic.marker, linestyle='none', label=mic.label )
                axs[1,0].errorbar( mic.sm_kfn, mic.sm_LP['Fp'][0], yerr=mic.sm_LP_Fp_err[0], marker=mic.marker, linestyle='none', label=mic.label )
                axs[1,1].errorbar( mic.sm_kfn, mic.sm_LP['Gp'][0], yerr=mic.sm_LP_Gp_err[0], marker=mic.marker, linestyle='none', label=mic.label )
            else:
                #print('kFn:',mic.sm_kfn)
                #print('F0:',mic.sm_LP['F'][0])
                #print('G0p:',mic.sm_LP['Gp'][0])
                axs[0,0].scatter( mic.sm_kfn, mic.sm_LP['F'][0], marker=mic.marker, linestyle=mic.linestyle, label=mic.label )
                axs[0,1].scatter( mic.sm_kfn, mic.sm_LP['G'][0], marker=mic.marker, linestyle=mic.linestyle, label=mic.label )
                axs[1,0].scatter( mic.sm_kfn, mic.sm_LP['Fp'][0], marker=mic.marker, linestyle=mic.linestyle, label=mic.label )
                axs[1,1].scatter( mic.sm_kfn, mic.sm_LP['Gp'][0], marker=mic.marker, linestyle=mic.linestyle, label=mic.label )
        #
        if nuda.env.verb_output: mic.print_outputs( )
        #
    #
    axs[0,0].legend(loc='upper left',fontsize='8', ncol=1)
    #
    plt.savefig(pname, dpi=300)
    plt.close()

def plot_matter_setupMicroLP1_SM( pname, models ):
    #
    # plot Landau Parameters in SM
    #
    print(f'Plot name: {pname}')
    #
    fig, axs = plt.subplots(2,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=0.98, top=0.98, wspace=0.15, hspace=0.05 )
    #
    axs[0,0].set_ylabel(r'$F_1$')
    axs[0,0].set_xlim([0, 2.0])
    axs[0,0].set_ylim([-1.4, 1])
    #
    axs[0,1].set_ylabel(r'$G_1$')
    axs[0,1].set_xlim([0, 2.0])
    axs[0,1].set_ylim([-1.4, 1])
    #
    axs[1,0].set_ylabel(r'$F_1^\prime$')
    axs[1,0].set_xlabel(r'$k_F$ (fm$^{-1}$)')
    axs[1,0].set_xlim([0, 2.0])
    axs[1,0].set_ylim([-1.4, 1])
    #
    axs[1,1].set_ylabel(r'$G_1^\prime$')
    axs[1,1].set_xlabel(r'$k_F$ (fm$^{-1}$)')
    axs[1,1].set_xlim([0, 2.0])
    axs[1,1].set_ylim([-1.4, 1])
    #
    axs[0,0].tick_params('x', labelbottom=False)
    axs[0,1].tick_params('x', labelbottom=False)
    axs[0,1].tick_params('y', labelleft=False)
    axs[1,1].tick_params('y', labelleft=False)
    #
    for model in models:
        #
        mic = nuda.matter.setupMicroLP( model = model )
        if mic.sm_kfn is not None and '-SM-' in model: 
            print('\nmodel:',model,'\n')
            if mic.err:
                axs[0,0].errorbar( mic.sm_kfn, mic.sm_LP['F'][1], yerr=mic.sm_LP_F_err[0], marker=mic.marker, linestyle='none', label=mic.label )
                axs[0,1].errorbar( mic.sm_kfn, mic.sm_LP['G'][1], yerr=mic.sm_LP_G_err[0], marker=mic.marker, linestyle='none', label=mic.label )
                axs[1,0].errorbar( mic.sm_kfn, mic.sm_LP['Fp'][1], yerr=mic.sm_LP_Fp_err[0], marker=mic.marker, linestyle='none', label=mic.label )
                axs[1,1].errorbar( mic.sm_kfn, mic.sm_LP['Gp'][1], yerr=mic.sm_LP_Gp_err[0], marker=mic.marker, linestyle='none', label=mic.label )
            else:
                axs[0,0].scatter( mic.sm_kfn, mic.sm_LP['F'][1], marker=mic.marker, linestyle=mic.linestyle, label=mic.label )
                axs[0,1].scatter( mic.sm_kfn, mic.sm_LP['G'][1], marker=mic.marker, linestyle=mic.linestyle, label=mic.label )
                axs[1,0].scatter( mic.sm_kfn, mic.sm_LP['Fp'][1], marker=mic.marker, linestyle=mic.linestyle, label=mic.label )
                axs[1,1].scatter( mic.sm_kfn, mic.sm_LP['Gp'][1], marker=mic.marker, linestyle=mic.linestyle, label=mic.label )
        #
        if nuda.env.verb_output: mic.print_outputs( )
        #
    #
    axs[0,0].legend(loc='upper left',fontsize='8', ncol=1)
    #
    plt.savefig(pname, dpi=300)
    plt.close()

def plot_matter_setupMicroLP0_NM( pname, models ):
    #
    # plot Landau Parameters in NM
    #
    print(f'Plot name: {pname}')
    #
    fig, axs = plt.subplots(1,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.14, bottom=0.12, right=0.98, top=0.98, wspace=0.4, hspace=0.3 )
    #
    axs[0].set_ylabel(r'$F_0$')
    axs[0].set_xlabel(r'$k_F$ (fm$^{-1}$)')
    axs[0].set_xlim([0, 2.0])
    axs[0].set_ylim([-1, 1])
    #
    axs[1].set_ylabel(r'$G_0$')
    axs[1].set_xlabel(r'$k_F$ (fm$^{-1}$)')
    axs[1].set_xlim([0, 2.0])
    axs[1].set_ylim([-1, 1])
    #
    for model in models:
        #
        mic = nuda.matter.setupMicroLP( model = model )
        if mic.nm_kfn is not None and '-NM-' in model: 
            print('model:',model,'\n')
            if mic.err:
                axs[0].errorbar( mic.nm_kfn, mic.nm_LP['F'][0], marker=mic.marker, linestyle='none', label=mic.label )
                axs[1].errorbar( mic.nm_kfn, mic.nm_LP['G'][0], marker=mic.marker, linestyle='none', label=mic.label )
            else:
                #print('kFn:',mic.nm_kfn)
                #print('F0:',mic.nm_LP['F'][0])
                #print('G0:',mic.nm_LP['G'][0])
                axs[0].scatter( mic.nm_kfn, mic.nm_LP['F'][0], marker=mic.marker, linestyle=mic.linestyle, label=mic.label )
                axs[1].scatter( mic.nm_kfn, mic.nm_LP['G'][0], marker=mic.marker, linestyle=mic.linestyle, label=mic.label )
        #
        if nuda.env.verb_output: mic.print_outputs( )
        #
    #
    axs[0].legend(loc='upper left',fontsize='8', ncol=1)
    #
    plt.savefig(pname, dpi=200)
    plt.close()

def main():
    #
    print(50*'-')
    print("Enter plot_matter_setupMicroLP.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    # list the available models
    #
    models, models_lower = nuda.matter.micro_LP_models()
    #
    # plot Landau Parameters L=0 in SM
    #
    pname = 'figs/plot_matter_setupMicroLP0_SM.png'
    #
    print('\npname:',pname)
    plot_matter_setupMicroLP0_SM( pname, models )
    #
    # plot Landau Parameters L=1 in SM
    #
    pname = 'figs/plot_matter_setupMicroLP1_SM.png'
    #
    print('\npname:',pname)
    plot_matter_setupMicroLP1_SM( pname, models )
    #
    # plot Landau Parameters L=0 in NM
    #
    pname = 'figs/plot_matter_setupMicroLP0_NM.png'
    #
    print('\npname:',pname)
    plot_matter_setupMicroLP0_NM( pname, models )
    #
    print(50*'-')
    print("Exit plot_matter_setupMicroLP.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
