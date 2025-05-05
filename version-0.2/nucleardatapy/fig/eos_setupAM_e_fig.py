import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def eos_setupAM_e_fig( pname, models_micro, models_pheno ):
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
    fig, axs = plt.subplots(3,2)
    fig.subplots_adjust(left=0.10, bottom=0.12, right=None, top=0.95, wspace=0.05, hspace=0.05 )
    #
    #axs[0,0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    axs[0,0].set_ylabel(r'$E_\text{lep}/A$')
    axs[0,0].set_xlim([0, 0.28])
    axs[0,0].set_ylim([-2, 38])
    axs[0,0].tick_params('x', labelbottom=False)
    #
    #axs[0,1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    axs[0,1].set_xlim([0, 0.28])
    axs[0,1].set_ylim([-2, 38])
    axs[0,1].tick_params('y', labelleft=False)
    axs[0,1].tick_params('x', labelbottom=False)
    #
    #axs[1,0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    axs[1,0].set_ylabel(r'$E_\text{nuc}/A$')
    axs[1,0].set_xlim([0, 0.28])
    axs[1,0].set_ylim([-10, 30])
    axs[1,0].tick_params('x', labelbottom=False)
    #
    #axs[1,1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    axs[1,1].set_xlim([0, 0.28])
    axs[1,1].set_ylim([-10, 30])
    axs[1,1].tick_params('y', labelleft=False)
    axs[1,1].tick_params('x', labelbottom=False)
    #
    axs[2,0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    axs[2,0].set_ylabel(r'$E_\text{tot}/A$')
    axs[2,0].set_xlim([0, 0.28])
    axs[2,0].set_ylim([-2, 38])
    #
    axs[2,1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    axs[2,1].set_xlim([0, 0.28])
    axs[2,1].set_ylim([-2, 38])
    axs[2,1].tick_params('y', labelleft=False)
    #
    # fix the asymmetry parameters
    #
    asys = [ 0.6, 0.8 ]
    #
    for asy in asys:
        #
        for model in models_micro:
            #
            micro = nuda.eos.setupAM( model = model, kind = 'micro', asy = asy )
            if nuda.env.verb_output: micro.print_outputs( )
            #
            if micro.esym is not None: 
                print('model:',model)
                print('den:',micro.den)
                print('e2a_lep:',micro.e2a_lep)
                axs[0,0].plot( micro.den, micro.e2a_lep, marker='o', linestyle=micro.linestyle, label=micro.label, markevery=micro.every )
                axs[1,0].plot( micro.den, micro.e2a_nuc, marker='o', linestyle=micro.linestyle, label=micro.label, markevery=micro.every )
                axs[2,0].plot( micro.den, micro.e2a_tot, marker='o', linestyle=micro.linestyle, label=micro.label, markevery=micro.every )
        #
        for model in models_pheno:
            #
            params, params_lower = nuda.matter.pheno_esym_params( model = model )
            #
            for param in params:
                #
                pheno = nuda.eos.setupAM( model = model, param = param, kind = 'pheno', asy = asy )
                if pheno.esym is not None: 
                    print('model:',model,' param:',param)
                    #beta.label=None
                    axs[0,1].plot( pheno.den, pheno.e2a_lep, linestyle=pheno.linestyle, label=pheno.label, markevery=pheno.every )
                    axs[1,1].plot( pheno.den, pheno.e2a_nuc, linestyle=pheno.linestyle, label=pheno.label, markevery=pheno.every )
                    axs[2,1].plot( pheno.den, pheno.e2a_tot, linestyle=pheno.linestyle, label=pheno.label, markevery=pheno.every )
                if nuda.env.verb_output: pheno.print_outputs( )
        #
    #
    axs[0,0].text(0.02,0,'microscopic models',fontsize='10')
    axs[0,1].text(0.02,0,'phenomenological models',fontsize='10')
    #
    axs[0,0].text(0.1,30,r'$\delta=0.6$',fontsize='10')
    axs[0,1].text(0.1,30,r'$\delta=0.6$',fontsize='10')
    axs[0,0].text(0.1,13,r'$\delta=0.8$',fontsize='10')
    axs[0,1].text(0.1,13,r'$\delta=0.8$',fontsize='10')
    #
    axs[1,0].text(0.1,-2,r'$\delta=0.6$',fontsize='10')
    axs[1,1].text(0.1,-2,r'$\delta=0.6$',fontsize='10')
    axs[1,0].text(0.1,7,r'$\delta=0.8$',fontsize='10')
    axs[1,1].text(0.1,7,r'$\delta=0.8$',fontsize='10')
    #
    axs[2,0].text(0.1,27,r'$\delta=0.6$',fontsize='10')
    axs[2,1].text(0.1,27,r'$\delta=0.6$',fontsize='10')
    axs[2,0].text(0.1,15,r'$\delta=0.8$',fontsize='10')
    axs[2,1].text(0.1,15,r'$\delta=0.8$',fontsize='10')
    #    
    if pname is not None: 
        plt.savefig(pname, dpi=200)
        plt.close()
