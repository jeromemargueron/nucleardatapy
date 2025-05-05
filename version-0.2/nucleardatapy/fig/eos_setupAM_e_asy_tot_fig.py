import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def eos_setupAM_e_asy_tot_fig( pname, models_micro, models_pheno, asy ):
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
    #fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.10, bottom=0.12, right=None, top=0.95, wspace=0.05, hspace=0.3 )
    #
    axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    axs[0].set_ylabel(r'$E_\text{tot}/A$')
    axs[0].set_xlim([0, 0.28])
    axs[0].set_ylim([-10, 35])
    #
    axs[1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    #axs[1].set_ylabel(r'$E/A$')
    axs[1].set_xlim([0, 0.28])
    axs[1].set_ylim([-10, 35])
    axs[1].tick_params('y', labelleft=False)
    #
    for model in models_micro:
        #
        micro = nuda.eos.setupAM( model = model, kind = 'micro', asy = asy )
        if nuda.env.verb_output: micro.print_outputs( )
        #
        if micro.esym is not None: 
            print('model:',model)
            #print('den:',am.den)
            #print('e2a:',am.e2a_nuc)
            axs[0].plot( micro.den, micro.e2a_tot, marker='o', linestyle=micro.linestyle, label=micro.label, markevery=micro.every )
    axs[0].text(0.02,-8,'microscopic models',fontsize='10')
    axs[0].text(0.02,-9.5,r'for $\delta=$'+str(asy),fontsize='10')
    #axs[0].legend(loc='upper left',fontsize='8', ncol=3)
    #axs[0].legend(loc='lower center',bbox_to_anchor=(0.5,1.02),mode='expand',columnspacing=0,fontsize='8', ncol=2,frameon=False)
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
                axs[1].plot( pheno.den, pheno.e2a_tot, linestyle=pheno.linestyle, label=pheno.label, markevery=pheno.every )
            if nuda.env.verb_output: pheno.print_outputs( )
    #
    #axs[1].fill_between( band.den, y1=(band.e2a-band.e2a_std), y2=(band.e2a+band.e2a_std), color=band.color, alpha=band.alpha, visible=True )
    #axs[1].plot( band.den, (band.e2a-band.e2a_std), color='k', linestyle='dashed' )
    #axs[1].plot( band.den, (band.e2a+band.e2a_std), color='k', linestyle='dashed' )
    axs[1].text(0.02,-8,'phenomenological models',fontsize='10')
    axs[1].text(0.02,-9.5,r'for $\delta=$'+str(asy),fontsize='10')
    #axs[1].legend(loc='upper left',fontsize='8', ncol=2)
    #axs[0,1].legend(loc='upper left',fontsize='xx-small', ncol=2)
    #axs[1].legend(loc='lower center',bbox_to_anchor=(0.5,1.02),mode='expand',columnspacing=0,fontsize='8', ncol=2,frameon=False)
    #fig.legend(loc='lower center',bbox_to_anchor=(0.5,1.02),mode='expand',columnspacing=0,fontsize='8', ncol=2,frameon=False)
    #plt.tight_layout(rect=[0,0,1,0.95])
    #
    if pname is not None: 
        plt.savefig(pname, dpi=200)
        plt.close()
