import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def eos_setupAMLeq_xe_fig( pname, models_micro, models_pheno ):
    """
    Plot nuclear chart (N versus Z).\
    The plot is 1x2 with:\
    [0]: nuclear chart.

    :param pname: name of the figure (*.png)
    :type pname: str.
    :param table: table.
    :type table: str.
    :param version: version of table to run on.
    :type version: str.
    :param theo_tables: object instantiated on the reference band.
    :type theo_tables: object.

    """
    #
    print(f'Plot name: {pname}')
    #
    # xe at beta-equilibrium
    #
    asy = 0.5
    #
    fig, axs = plt.subplots(1,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.98, wspace=0.05, hspace=0.3 )
    #
    axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    axs[0].set_ylabel(r'electron fraction $x_e$')
    axs[0].set_xlim([0, 0.28])
    axs[0].set_ylim([0.1, 0.3])
    #
    axs[1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    #axs[1].set_ylabel(r'electron fraction $x_e$')
    axs[1].set_xlim([0, 0.28])
    axs[1].set_ylim([0.1, 0.3])
    axs[1].tick_params('y', labelleft=False)
    #
    for model in models_micro:
        #
        beta = nuda.eos.setupAMLeq( model = model, kind = 'micro', asy = asy )
        if nuda.env.verb_output: beta.print_outputs( )
        #
        if beta.esym is not None: 
            print('model:',model)
            axs[0].plot( beta.den, beta.x_el, linestyle=beta.linestyle, label=beta.label, markevery=beta.every )
            #axs[0].plot( beta.den, beta.x_el, marker='o', linestyle=beta.linestyle, label=beta.label, markevery=beta.every )
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
                axs[1].plot( beta.den, beta.x_el, linestyle=beta.linestyle, label=beta.label, markevery=beta.every )
            if nuda.env.verb_output: pheno.print_outputs( )
    #
    axs[1].text(0.08,0.22,'phenomenological models',fontsize='10')
    #
    if pname is not None:
    	plt.savefig(pname, dpi=200)
    	plt.close()

def eos_setupAMLeq_xmu_fig( pname, models_micro, models_pheno ):
    """
    Plot nuclear chart (N versus Z).\
    The plot is 1x2 with:\
    [0]: nuclear chart.

    :param pname: name of the figure (*.png)
    :type pname: str.
    :param table: table.
    :type table: str.
    :param version: version of table to run on.
    :type version: str.
    :param theo_tables: object instantiated on the reference band.
    :type theo_tables: object.

    """
    #
    print(f'Plot name: {pname}')
    #
    # xmu at beta-equilibrium
    #
    asy = 0.5
    #
    fig, axs = plt.subplots(1,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.98, wspace=0.05, hspace=0.3 )
    #
    axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    axs[0].set_ylabel(r'muon fraction $x_\mu$')
    axs[0].set_xlim([0, 0.28])
    axs[0].set_ylim([0, 0.15])
    #
    axs[1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    #axs[1].set_ylabel(r'muon fraction $x_\mu$')
    axs[1].set_xlim([0, 0.28])
    axs[1].set_ylim([0, 0.15])
    axs[1].tick_params('y', labelleft=False)
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
    if pname is not None:
    	plt.savefig(pname, dpi=200)
    	plt.close()

def eos_setupAMLeq_xexmu_fig( pname, models_micro, models_pheno ):
    """
    Plot nuclear chart (N versus Z).\
    The plot is 1x2 with:\
    [0]: nuclear chart.

    :param pname: name of the figure (*.png)
    :type pname: str.
    :param table: table.
    :type table: str.
    :param version: version of table to run on.
    :type version: str.
    :param theo_tables: object instantiated on the reference band.
    :type theo_tables: object.

    """
    #
    print(f'Plot name: {pname}')
    #
    fig, axs = plt.subplots(1,1)
    #fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.95, wspace=0.3, hspace=0.3 )
    #
    axs.set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='10')
    axs.set_ylabel(r'$x_e$, $x_\mu$',fontsize='10')
    axs.set_xlim([0, 0.28])
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
                    axs.plot( am.den, am.x_el, linestyle='solid', label=r'$\delta=$'+str(asy), color=nuda.param.col[inda] )
                    axs.plot( am.den, am.x_mu, linestyle='dashed', color=nuda.param.col[inda] )
                if nuda.env.verb_output: pheno.print_outputs( )
                break
        #
        axs.legend(loc='upper right',fontsize='10',ncol=3)
        axs.text(0.05,0.35,r'$x_e$',fontsize='14')
        axs.text(0.02,0.10,r'$x_\mu$',fontsize='14')
    #
    if pname is not None:
    	plt.savefig(pname, dpi=200)
    	plt.close()