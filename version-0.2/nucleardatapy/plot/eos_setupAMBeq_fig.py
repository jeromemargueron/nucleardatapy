import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def eos_setupAMBeq_xp_fig( pname, models_micro, models_pheno ):
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
    fig, axs = plt.subplots(1,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.98, wspace=0.05, hspace=0.3 )
    #
    axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    axs[0].set_ylabel(r'proton fraction $x_p$')
    axs[0].set_xlim([0, 0.28])
    axs[0].set_ylim([0, 0.2])
    #axs[0].set_tick_params('y', right=True)
    #axs[0].set_tick_params('x', top=True)
    #
    axs[1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    #axs[1].set_ylabel(r'proton fraction $x_p$')
    axs[1].set_xlim([0, 0.28])
    axs[1].set_ylim([0, 0.2])
    #setp(axs[1].get_yticklabels(), visible=False)
    axs[1].tick_params('y', labelleft=False)
    #
    for model in models_micro:
        #
        beta = nuda.eos.setupAMBeq( model = model, kind = 'micro' )
        if nuda.env.verb_output: beta.print_outputs( )
        #
        if beta.esym is not None: 
            print('model:',model)
            axs[0].plot( beta.den, beta.x_p, marker='o', linestyle=beta.linestyle, label=beta.label, markevery=beta.every )
    axs[0].text(0.02,0.18,'microscopic models',fontsize='10')
    #axs[0].legend(loc='upper left',fontsize='8', ncol=3)
    #
    for model in models_pheno:
        #
        params, params_lower = nuda.matter.pheno_esym_params( model = model )
        #
        for param in params:
            #
            beta = nuda.eos.setupAMBeq( model = model, param = param, kind = 'pheno' )
            if beta.esym is not None: 
                print('model:',model,' param:',param)
                #beta.label=None
                axs[1].plot( beta.den, beta.x_p, linestyle=beta.linestyle, label=beta.label, markevery=beta.every )
            if nuda.env.verb_output: pheno.print_outputs( )
    #
    #axs[1].fill_between( band.den, y1=(band.e2a-band.e2a_std), y2=(band.e2a+band.e2a_std), color=band.color, alpha=band.alpha, visible=True )
    #axs[1].plot( band.den, (band.e2a-band.e2a_std), color='k', linestyle='dashed' )
    #axs[1].plot( band.den, (band.e2a+band.e2a_std), color='k', linestyle='dashed' )
    axs[1].text(0.02,0.18,'phenomenological models',fontsize='10')
    #axs[1].legend(loc='upper left',fontsize='8', ncol=2)
    #axs[0,1].legend(loc='upper left',fontsize='xx-small', ncol=2)
    #
    if pname is not None: 
    	plt.savefig(pname, dpi=200)
    	plt.close()

def eos_setupAMBeq_xe_fig( pname, models_micro, models_pheno ):
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
    fig, axs = plt.subplots(1,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.98, wspace=0.05, hspace=0.3 )
    #
    axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    axs[0].set_ylabel(r'electron fraction $x_e$')
    axs[0].set_xlim([0, 0.28])
    axs[0].set_ylim([0, 0.2])
    #
    axs[1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    #axs[1].set_ylabel(r'electron fraction $x_e$')
    axs[1].set_xlim([0, 0.28])
    axs[1].set_ylim([0, 0.2])
    axs[1].tick_params('y', labelleft=False)
    #
    for model in models_micro:
        #
        beta = nuda.eos.setupAMBeq( model = model, kind = 'micro' )
        if nuda.env.verb_output: beta.print_outputs( )
        #
        if beta.esym is not None: 
            print('model:',model)
            axs[0].plot( beta.den, beta.x_el, marker='o', linestyle=beta.linestyle, label=beta.label, markevery=beta.every )
    axs[0].text(0.02,0.18,'microscopic models',fontsize='10')
    #axs[0].legend(loc='upper left',fontsize='8', ncol=3)
    #
    for model in models_pheno:
        #
        params, params_lower = nuda.matter.pheno_esym_params( model = model )
        #
        for param in params:
            #
            beta = nuda.eos.setupAMBeq( model = model, param = param, kind = 'pheno' )
            if beta.esym is not None: 
                print('model:',model,' param:',param)
                #beta.label=None
                axs[1].plot( beta.den, beta.x_el, linestyle=beta.linestyle, label=beta.label, markevery=beta.every )
            if nuda.env.verb_output: pheno.print_outputs( )
    #
    axs[1].text(0.02,0.18,'phenomenological models',fontsize='10')
    #
    if pname is not None: 
    	plt.savefig(pname, dpi=200)
    	plt.close()

def eos_setupAMBeq_xmu_fig( pname, models_micro, models_pheno ):
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
    fig, axs = plt.subplots(1,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.98, wspace=0.05, hspace=0.3 )
    #
    axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    axs[0].set_ylabel(r'muon fraction $x_\mu$')
    axs[0].set_xlim([0, 0.28])
    axs[0].set_ylim([0, 0.2])
    #
    axs[1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    #axs[1].set_ylabel(r'muon fraction $x_\mu$')
    axs[1].set_xlim([0, 0.28])
    axs[1].set_ylim([0, 0.2])
    axs[1].tick_params('y', labelleft=False)
    #
    for model in models_micro:
        #
        beta = nuda.eos.setupAMBeq( model = model, kind = 'micro' )
        if nuda.env.verb_output: beta.print_outputs( )
        #
        if beta.esym is not None: 
            print('model:',model)
            axs[0].plot( beta.den, beta.x_mu, marker='o', linestyle=beta.linestyle, label=beta.label, markevery=beta.every )
    axs[0].text(0.02,0.18,'microscopic models',fontsize='10')
    #axs[0].legend(loc='upper left',fontsize='8', ncol=3)
    #
    for model in models_pheno:
        #
        params, params_lower = nuda.matter.pheno_esym_params( model = model )
        #
        for param in params:
            #
            beta = nuda.eos.setupAMBeq( model = model, param = param, kind = 'pheno' )
            if beta.esym is not None: 
                print('model:',model,' param:',param)
                #beta.label=None
                axs[1].plot( beta.den, beta.x_mu, linestyle=beta.linestyle, label=beta.label, markevery=beta.every )
            if nuda.env.verb_output: pheno.print_outputs( )
    #
    axs[1].text(0.02,0.18,'phenomenological models',fontsize='10')
    #
    if pname is not None: 
    	plt.savefig(pname, dpi=200)
    	plt.close()