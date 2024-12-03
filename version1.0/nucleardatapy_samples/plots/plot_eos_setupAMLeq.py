
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plot_eos_setupAMLeq_xe( pname, models_micro, models_pheno ):
    #
    # xe at beta-equilibrium
    #
    asy = 0.5
    print(f'Plot name: {pname}')
    #
    fig, axs = plt.subplots(1,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.98, wspace=0.05, hspace=0.3 )
    #
    axs[0].set_xlabel(r'n (fm$^{-3}$)')
    axs[0].set_ylabel(r'electron fraction $x_e$')
    axs[0].set_xlim([0, 0.3])
    axs[0].set_ylim([0.1, 0.3])
    #
    axs[1].set_xlabel(r'n (fm$^{-3}$)')
    #axs[1].set_ylabel(r'electron fraction $x_e$')
    axs[1].set_xlim([0, 0.3])
    axs[1].set_ylim([0.1, 0.3])
    #
    for model in models_micro:
        #
        beta = nuda.eos.setupAMLeq( model = model, kind = 'micro', asy = asy )
        if nuda.env.verb_output: beta.print_outputs( )
        #
        if beta.esym is not None: 
            print('model:',model)
            axs[0].plot( beta.den, beta.x_e, linestyle=beta.linestyle, label=beta.label, markevery=beta.every )
            #axs[0].plot( beta.den, beta.x_e, marker='o', linestyle=beta.linestyle, label=beta.label, markevery=beta.every )
    axs[0].text(0.08,0.22,'microscopic models',fontsize='10')
    #axs[0].legend(loc='upper left',fontsize='8', ncol=3)
    #
    for model in models_pheno:
        #
        params, params_lower = nuda.matter.pheno_esym_params( model = model )
        #
        for param in params:
            #
            beta = nuda.eos.setupAMLeq( model = model, param = param, kind = 'pheno', asy = asy )
            if beta.esym is not None: 
                print('model:',model,' param:',param)
                #beta.label=None
                axs[1].plot( beta.den, beta.x_e, linestyle=beta.linestyle, label=beta.label, markevery=beta.every )
            if nuda.env.verb_output: pheno.print_outputs( )
    #
    axs[1].text(0.08,0.22,'phenomenological models',fontsize='10')
    #
    plt.savefig(pname)
    plt.close()

def plot_eos_setupAMLeq_xmu( pname, models_micro, models_pheno ):
    #
    # xmu at beta-equilibrium
    #
    asy = 0.5
    print(f'Plot name: {pname}')
    #
    fig, axs = plt.subplots(1,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.98, wspace=0.05, hspace=0.3 )
    #
    axs[0].set_xlabel(r'n (fm$^{-3}$)')
    axs[0].set_ylabel(r'muon fraction $x_\mu$')
    axs[0].set_xlim([0, 0.3])
    axs[0].set_ylim([0, 0.15])
    #
    axs[1].set_xlabel(r'n (fm$^{-3}$)')
    #axs[1].set_ylabel(r'muon fraction $x_\mu$')
    axs[1].set_xlim([0, 0.3])
    axs[1].set_ylim([0, 0.15])
    #
    for model in models_micro:
        #
        beta = nuda.eos.setupAMLeq( model = model, kind = 'micro', asy = asy )
        if nuda.env.verb_output: beta.print_outputs( )
        #
        if beta.esym is not None: 
            print('model:',model)
            axs[0].plot( beta.den, beta.x_mu, marker='o', linestyle=beta.linestyle, label=beta.label, markevery=beta.every )
    axs[0].text(0.08,0.12,'microscopic models',fontsize='10')
    #axs[0].legend(loc='upper left',fontsize='8', ncol=3)
    #
    for model in models_pheno:
        #
        params, params_lower = nuda.matter.pheno_esym_params( model = model )
        #
        for param in params:
            #
            beta = nuda.eos.setupAMLeq( model = model, param = param, kind = 'pheno', asy = asy )
            if beta.esym is not None: 
                print('model:',model,' param:',param)
                #beta.label=None
                axs[1].plot( beta.den, beta.x_mu, linestyle=beta.linestyle, label=beta.label, markevery=beta.every )
            if nuda.env.verb_output: pheno.print_outputs( )
    #
    axs[1].text(0.08,0.12,'phenomenological models',fontsize='10')
    #
    plt.savefig(pname)
    plt.close()

def plot_eos_setupAMLeq_xexmu( pname, models_micro, models_pheno ):
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
            am = nuda.eos.setupAMLeq( model = model, kind = 'micro', asy = asy )
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
                am = nuda.eos.setupAMLeq( model = model, param = param, kind = 'pheno', asy = asy )
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
    print("Enter plot_eos_setupAMLeq.py:")
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
    micro_models, micro_models_lower = nuda.matter.micro_esym_models()
    micro_models.remove('1998-VAR-AM-APR-fit')
    micro_models_lower.remove('1998-var-am-apr-fit')
    #micro_models = [ '1998-VAR-AM-APR' ]
    pheno_models, pheno_models_lower = nuda.matter.pheno_esym_models()
    #pheno_models = [ 'Skyrme', 'ESkyrme', 'NLRH', 'DDRH', 'DDRHF' ]
    #
    # plot Esym
    #
    pname = 'figs/plot_eos_setupAMLeq_xe.png'
    plot_eos_setupAMLeq_xe( pname, micro_models, pheno_models )
    #
    pname = 'figs/plot_eos_setupAMLeq_xmu.png'
    plot_eos_setupAMLeq_xmu( pname, micro_models, pheno_models )
    #
    micro_models = [ ]
    pheno_models = [ 'DDRHF' ]
    pname = 'figs/plot_eos_setupAMLeq_xexmu.png'
    plot_eos_setupAMLeq_xexmu( pname, micro_models, pheno_models )
    #
    print(50*'-')
    print("Exit plot_eos_setupAMLeq.py:")
    print(50*'-')
    #

if __name__ == "__main__":
    main()
