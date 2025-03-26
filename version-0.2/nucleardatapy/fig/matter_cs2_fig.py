import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def matter_cs2_fig( pname, micro_models, pheno_models, band ):
    """
    Plot nuclear chart (N versus Z).\
    The plot is 1x1 with:\
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
    fig.subplots_adjust(left=0.10, bottom=0.12, right=None, top=0.98, wspace=0.3, hspace=0.3 )
    #
    axs[0].set_xlabel(r'n (fm$^{-3}$)')
    axs[0].set_ylabel(r'$c_{s,NM}^2(n)$')
    axs[0].set_xlim([0, 0.3])
    axs[0].set_ylim([0, 0.5])
    #
    axs[1].set_xlabel(r'n (fm$^{-3}$)')
    axs[1].set_ylabel(r'$c_{s,NM}^2(n)$')
    axs[1].set_xlim([0, 0.3])
    axs[1].set_ylim([0, 0.5])
    #
    for model in micro_models:
        #
        mic = nuda.matter.setupMicro( model = model )
        if mic.nm_cs2 is not None: 
            print('model:',model)
            if mic.marker:
                if mic.err:
                    axs[0].errorbar( mic.nm_den, mic.nm_cs2, yerr=mic.nm_cs2_err, marker=mic.marker, linestyle=None, label=mic.label, errorevery=mic.every )
                else:
                    axs[0].plot( mic.nm_den, mic.nm_cs2, marker=mic.marker, linestyle=None, label=mic.label, markevery=mic.every )
            else:
                if mic.err:
                    axs[0].errorbar( mic.nm_den, mic.nm_cs2, yerr=mic.nm_cs2_err, marker=mic.marker, linestyle=mic.linestyle, label=mic.label, errorevery=mic.every )
                else:
                    axs[0].plot( mic.nm_den, mic.nm_cs2, marker=mic.marker, linestyle=mic.linestyle, label=mic.label, markevery=mic.every )
        if nuda.env.verb: mic.print_outputs( )
    #axs[0].fill_between( band.den, y1=(band.pre-band.pre_std), y2=(band.pre+band.pre_std), color=band.color, alpha=band.alpha, visible=True )
    #axs[0].plot( band.den, (band.pre-band.pre_std), color='k', linestyle='dashed' )
    #axs[0].plot( band.den, (band.pre+band.pre_std), color='k', linestyle='dashed' )
    axs[0].text(0.01,0.4,'microscopic models',fontsize='10')
    axs[0].legend(loc='upper left',fontsize='8', ncol=3)
    #
    for model in pheno_models:
        #
        params, params_lower = nuda.matter.pheno_params( model = model )
        #
        for param in params:
            #
            pheno = nuda.matter.setupPheno( model = model, param = param )
            if pheno.nm_pre is not None: 
                print('model:',model,' param:',param)
                #pheno.label=None
                axs[1].plot( pheno.nm_den, pheno.nm_cs2, label=pheno.label )
            if nuda.env.verb: pheno.print_outputs( )
    #axs[1].fill_between( band.den, y1=(band.e2a-band.e2a_std), y2=(band.e2a+band.e2a_std), color=band.color, alpha=band.alpha, visible=True )
    #axs[1].plot( band.den, (band.e2a-band.e2a_std), color='k', linestyle='dashed' )
    #axs[1].plot( band.den, (band.e2a+band.e2a_std), color='k', linestyle='dashed' )
    axs[1].text(0.01,0.4,'phenomenological models',fontsize='10')
    #axs[1].legend(loc='upper left',fontsize='8', ncol=2)
    #axs[0,1].legend(loc='upper left',fontsize='xx-small', ncol=2)
    #
    if pname is not None:
    	plt.savefig(pname, dpi=200)
    	plt.close()
    #
