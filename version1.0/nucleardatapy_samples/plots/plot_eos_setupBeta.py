
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plot_eos_setupBeta_xp( pname, models_micro, models_pheno ):
    #
    # xp at beta-equilibrium
    #
    print(f'Plot name: {pname}')
    #
    fig, axs = plt.subplots(1,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.98, wspace=0.3, hspace=0.3 )
    #
    axs[0].set_xlabel(r'n (fm$^{-3}$)')
    axs[0].set_ylabel(r'proton fraction $x_p$')
    axs[0].set_xlim([0, 0.3])
    axs[0].set_ylim([0, 0.25])
    #
    axs[1].set_xlabel(r'n (fm$^{-3}$)')
    axs[1].set_ylabel(r'proton fraction $x_p$')
    axs[1].set_xlim([0, 0.3])
    axs[1].set_ylim([0, 0.25])
    #
    for model in models_micro:
        #
        beta = nuda.eos.setupBeta( model = model, kind = 'micro' )
        if nuda.env.verb_output: beta.print_outputs( )
        #
        if beta.esym is not None: 
            print('model:',model)
            axs[0].plot( beta.den, beta.x_p, marker='o', linestyle=beta.linestyle, label=beta.label, markevery=beta.every )
    axs[0].text(0.05,0.1,'microscopic models',fontsize='10')
    axs[0].legend(loc='upper left',fontsize='8', ncol=3)
    #
    for model in models_pheno:
        #
        params, params_lower = nuda.eos.pheno_esym_params( model = model )
        #
        for param in params:
            #
            beta = nuda.eos.setupBeta( model = model, param = param, kind = 'pheno' )
            if beta.esym is not None: 
                print('model:',model,' param:',param)
                #beta.label=None
                axs[1].plot( beta.den, beta.x_p, linestyle=beta.linestyle, label=beta.label, markevery=beta.every )
            if nuda.env.verb_output: pheno.print_outputs( )
    #
    #axs[1].fill_between( band.den, y1=(band.e2a-band.e2a_std), y2=(band.e2a+band.e2a_std), color=band.color, alpha=band.alpha, visible=True )
    #axs[1].plot( band.den, (band.e2a-band.e2a_std), color='k', linestyle='dashed' )
    #axs[1].plot( band.den, (band.e2a+band.e2a_std), color='k', linestyle='dashed' )
    axs[1].text(0.05,0.1,'phenomenological models',fontsize='10')
    #axs[1].legend(loc='upper left',fontsize='8', ncol=2)
    #axs[0,1].legend(loc='upper left',fontsize='xx-small', ncol=2)
    #
    plt.savefig(pname)
    plt.close()

def plot_eos_setupBeta_xe( pname, models_micro, models_pheno ):
    #
    # xe at beta-equilibrium
    #
    print(f'Plot name: {pname}')
    #
    fig, axs = plt.subplots(1,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.98, wspace=0.3, hspace=0.3 )
    #
    axs[0].set_xlabel(r'n (fm$^{-3}$)')
    axs[0].set_ylabel(r'electron fraction $x_e$')
    axs[0].set_xlim([0, 0.3])
    axs[0].set_ylim([0, 0.25])
    #
    axs[1].set_xlabel(r'n (fm$^{-3}$)')
    axs[1].set_ylabel(r'electron fraction $x_e$')
    axs[1].set_xlim([0, 0.3])
    axs[1].set_ylim([0, 0.25])
    #
    for model in models_micro:
        #
        beta = nuda.eos.setupBeta( model = model, kind = 'micro' )
        if nuda.env.verb_output: beta.print_outputs( )
        #
        if beta.esym is not None: 
            print('model:',model)
            axs[0].plot( beta.den, beta.x_e, marker='o', linestyle=beta.linestyle, label=beta.label, markevery=beta.every )
    axs[0].text(0.05,0.1,'microscopic models',fontsize='10')
    axs[0].legend(loc='upper left',fontsize='8', ncol=3)
    #
    for model in models_pheno:
        #
        params, params_lower = nuda.eos.pheno_esym_params( model = model )
        #
        for param in params:
            #
            beta = nuda.eos.setupBeta( model = model, param = param, kind = 'pheno' )
            if beta.esym is not None: 
                print('model:',model,' param:',param)
                #beta.label=None
                axs[1].plot( beta.den, beta.x_e, linestyle=beta.linestyle, label=beta.label, markevery=beta.every )
            if nuda.env.verb_output: pheno.print_outputs( )
    #
    axs[1].text(0.05,0.1,'phenomenological models',fontsize='10')
    #
    plt.savefig(pname)
    plt.close()

def plot_eos_setupBeta_xmu( pname, models_micro, models_pheno ):
    #
    # xmu at beta-equilibrium
    #
    print(f'Plot name: {pname}')
    #
    fig, axs = plt.subplots(1,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.98, wspace=0.3, hspace=0.3 )
    #
    axs[0].set_xlabel(r'n (fm$^{-3}$)')
    axs[0].set_ylabel(r'muon fraction $x_\mu$')
    axs[0].set_xlim([0, 0.3])
    axs[0].set_ylim([0, 0.25])
    #
    axs[1].set_xlabel(r'n (fm$^{-3}$)')
    axs[1].set_ylabel(r'muon fraction $x_\mu$')
    axs[1].set_xlim([0, 0.3])
    axs[1].set_ylim([0, 0.25])
    #
    for model in models_micro:
        #
        beta = nuda.eos.setupBeta( model = model, kind = 'micro' )
        if nuda.env.verb_output: beta.print_outputs( )
        #
        if beta.esym is not None: 
            print('model:',model)
            axs[0].plot( beta.den, beta.x_mu, marker='o', linestyle=beta.linestyle, label=beta.label, markevery=beta.every )
    axs[0].text(0.05,0.1,'microscopic models',fontsize='10')
    axs[0].legend(loc='upper left',fontsize='8', ncol=3)
    #
    for model in models_pheno:
        #
        params, params_lower = nuda.eos.pheno_esym_params( model = model )
        #
        for param in params:
            #
            beta = nuda.eos.setupBeta( model = model, param = param, kind = 'pheno' )
            if beta.esym is not None: 
                print('model:',model,' param:',param)
                #beta.label=None
                axs[1].plot( beta.den, beta.x_mu, linestyle=beta.linestyle, label=beta.label, markevery=beta.every )
            if nuda.env.verb_output: pheno.print_outputs( )
    #
    axs[1].text(0.05,0.1,'phenomenological models',fontsize='10')
    #
    plt.savefig(pname)
    plt.close()

def main():
    #
    print(50*'-')
    print("Enter plot_eos_setupBeta.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    # fix the uncertainty band
    #
    #den = np.array([0.04,0.06,0.08,0.1,0.12,0.14,0.16])
    #models = [ '2016-MBPT-AM', '2020-MBPT-AM' ]
    #band = nuda.SetupEOSMicroBand( models, den=den, matter='ESYM' )
    #
    # list the available models
    #
    micro_models, micro_models_lower = nuda.eos.micro_esym_models()
    micro_models.remove('1998-VAR-AM-APRfit')
    micro_models_lower.remove('1998-var-am-aprfit')
    #micro_models = [ '1998-VAR-AM-APR' ]
    pheno_models, pheno_models_lower = nuda.eos.pheno_esym_models()
    #pheno_models = [ 'Skyrme', 'ESkyrme', 'NLRH', 'DDRH', 'DDRHF' ]
    #
    # plot Esym
    #
    pname = 'figs/plot_eos_setupBeta_xp.png'
    plot_eos_setupBeta_xp( pname, micro_models, pheno_models )
    #
    pname = 'figs/plot_eos_setupBeta_xe.png'
    plot_eos_setupBeta_xe( pname, micro_models, pheno_models )
    #
    pname = 'figs/plot_eos_setupBeta_xmu.png'
    plot_eos_setupBeta_xmu( pname, micro_models, pheno_models )
    #
    print(50*'-')
    print("Exit plot_eos_setupBeta.py:")
    print(50*'-')
    #

if __name__ == "__main__":
    main()
