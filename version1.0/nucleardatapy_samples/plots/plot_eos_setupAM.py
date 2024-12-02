
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plot_eos_setupAM_e( pname, models_micro, models_pheno, asy ):
    #
    # E/A for a given asymmetry parameter asy
    #
    print(f'Plot name: {pname}')
    #
    fig, axs = plt.subplots(1,2)
    #fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.95, wspace=0.3, hspace=0.3 )
    #
    axs[0].set_xlabel(r'n (fm$^{-3}$)')
    axs[0].set_ylabel(r'$E/A$')
    axs[0].set_xlim([0, 0.3])
    axs[0].set_ylim([-13, 15])
    #
    axs[1].set_xlabel(r'n (fm$^{-3}$)')
    axs[1].set_ylabel(r'$E/A$')
    axs[1].set_xlim([0, 0.3])
    axs[1].set_ylim([-13, 15])
    #
    for model in models_micro:
        #
        am = nuda.eos.setupAM( model = model, kind = 'micro', asy = asy )
        if nuda.env.verb_output: am.print_outputs( )
        #
        if am.esym is not None: 
            print('model:',model)
            axs[0].plot( am.den, am.e2a, marker='o', linestyle=am.linestyle, label=am.label, markevery=am.every )
    axs[0].text(0.02,12,'microscopic models',fontsize='10')
    axs[0].text(0.02,10,'for $\delta=$'+str(asy),fontsize='10')
    #axs[0].legend(loc='upper left',fontsize='8', ncol=3)
    #axs[0].legend(loc='lower center',bbox_to_anchor=(0.5,1.02),mode='expand',columnspacing=0,fontsize='8', ncol=2,frameon=False)
    #
    for model in models_pheno:
        #
        params, params_lower = nuda.matter.pheno_esym_params( model = model )
        #
        for param in params:
            #
            am = nuda.eos.setupAM( model = model, param = param, kind = 'pheno', asy = asy )
            if am.esym is not None: 
                print('model:',model,' param:',param)
                #beta.label=None
                axs[1].plot( am.den, am.e2a, linestyle=am.linestyle, label=am.label, markevery=am.every )
            if nuda.env.verb_output: pheno.print_outputs( )
    #
    #axs[1].fill_between( band.den, y1=(band.e2a-band.e2a_std), y2=(band.e2a+band.e2a_std), color=band.color, alpha=band.alpha, visible=True )
    #axs[1].plot( band.den, (band.e2a-band.e2a_std), color='k', linestyle='dashed' )
    #axs[1].plot( band.den, (band.e2a+band.e2a_std), color='k', linestyle='dashed' )
    axs[1].text(0.02,12,'phenomenological models',fontsize='10')
    axs[1].text(0.02,10,'for $\delta=$'+str(asy),fontsize='10')
    #axs[1].legend(loc='upper left',fontsize='8', ncol=2)
    #axs[0,1].legend(loc='upper left',fontsize='xx-small', ncol=2)
    #axs[1].legend(loc='lower center',bbox_to_anchor=(0.5,1.02),mode='expand',columnspacing=0,fontsize='8', ncol=2,frameon=False)
    #fig.legend(loc='lower center',bbox_to_anchor=(0.5,1.02),mode='expand',columnspacing=0,fontsize='8', ncol=2,frameon=False)
    #plt.tight_layout(rect=[0,0,1,0.95])
    #
    plt.savefig(pname)
    plt.close()

def plot_eos_setupAM_xmu( pname, models_micro, models_pheno ):
    #
    # E/A for a given asymmetry parameter asy
    #
    print(f'Plot name: {pname}')
    #
    fig, axs = plt.subplots(1,1)
    #fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.95, wspace=0.3, hspace=0.3 )
    #
    axs.set_xlabel(r'n (fm$^{-3}$)',fontsize='10')
    axs.set_ylabel(r'$x_e$, $x_\mu$',fontsize='10')
    axs.set_xlim([0, 0.3])
    axs.set_ylim([0, 0.5])
    #
    asys = [ 0.1, 0.3, 0.5, 0.7, 0.9 ]
    #asys = [ 0.5 ]
    #
    for inda,asy in enumerate(asys):
        #
        for model in models_micro:
            #
            continue
            am = nuda.eos.setupAM( model = model, kind = 'micro', asy = asy )
            if nuda.env.verb_output: am.print_outputs( )
            #
            if am.esym is not None: 
                print('model:',model)
                axs.plot( am.den, am.x_mu, marker='o', linestyle=am.linestyle, label=am.label, markevery=am.every )
        #axs[0].text(0.02,12,'microscopic models',fontsize='10')
        #axs[0].text(0.02,10,'for $\delta=$'+str(asy),fontsize='10')
        #
        for model in models_pheno:
            #
            params, params_lower = nuda.matter.pheno_esym_params( model = model )
            #
            for param in params:
                #
                am = nuda.eos.setupAM( model = model, param = param, kind = 'pheno', asy = asy )
                if am.esym is not None: 
                    print('model:',model,' param:',param)
                    #beta.label=None
                    axs.plot( am.den, am.x_e, linestyle='solid', label='$\delta=$'+str(asy), color=nuda.param.col[inda] )
                    axs.plot( am.den, am.x_mu, linestyle='dashed', color=nuda.param.col[inda] )
                if nuda.env.verb_output: pheno.print_outputs( )
                break
        #
        axs.legend(loc='upper right',fontsize='10',ncol=3)
        axs.text(0.05,0.35,'$x_e$',fontsize='14')
        axs.text(0.02,0.10,'$x_\mu$',fontsize='14')
    #
    plt.savefig(pname)
    plt.close()

def main():
    #
    print(50*'-')
    print("Enter plot_eos_setupAM.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    # fix the asymmetry parameter
    #
    asy = 0.5
    #
    # fix the uncertainty band
    #
    #den = np.array([0.04,0.06,0.08,0.1,0.12,0.14,0.16])
    #models = [ '2016-MBPT-AM', '2020-MBPT-AM' ]
    #band = nuda.SetupEOSMicroBand( models, den=den, matter='ESYM' )
    #
    # list the available models
    #
    micro_models, micro_models_lower = nuda.matter.micro_esym_models()
    micro_models.remove('1998-VAR-AM-APR-fit')
    micro_models_lower.remove('1998-var-am-apr-fit')
    #micro_models = [ '1998-VAR-AM-APR' ]
    #pheno_models, pheno_models_lower = nuda.matter.pheno_esym_models()
    pheno_models = [ 'Skyrme', 'ESkyrme', 'NLRH', 'DDRH', 'DDRHF' ]
    #
    # plot E/A for a given asymmetric parameter asy
    #
    pname = 'figs/plot_eos_setupAM_e.png'
    plot_eos_setupAM_e( pname, micro_models, pheno_models, asy )
    #
    micro_models = [ ]
    pheno_models = [ 'DDRHF' ]
    pname = 'figs/plot_eos_setupAM_xmu.png'
    plot_eos_setupAM_xmu( pname, micro_models, pheno_models )
    #
    print(50*'-')
    print("Exit plot_eos_setupAM.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
