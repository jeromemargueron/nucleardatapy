import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def matter_Esym_fig( pname, micro_mbs, pheno_models, band ):
    """
    Plot nucleonic energy per particle E/A in matter.\
    The plot is 2x2 with:\
    [0,0]: E/A versus den.       [0,1]: E/A versus kfn.\
    [1,0]: E/E_NRFFG versus den. [1,1]: E/E_NRFFG versus kfn.\

    :param pname: name of the figure (*.png)
    :type pname: str.
    :param mb: many-body (mb) approach considered.
    :type mb: str.
    :param models: models to run on.
    :type models: array of str.
    :param band: object instantiated on the reference band.
    :type band: object.
    :param matter: can be 'SM' or 'NM'.
    :type matter: str.

    """
    #
    print(f'Plot name: {pname}')
    #
    fig, axs = plt.subplots(1,2)
    #fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.10, bottom=0.12, right=None, top=0.9, wspace=0.05, hspace=0.3 )
    #
    axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    axs[0].set_ylabel(r'$e_\text{sym}(n)$')
    axs[0].set_xlim([0, 0.33])
    axs[0].set_ylim([0, 60])
    #
    axs[1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    #axs[1].set_ylabel(r'$e_{sym}(n)$')
    axs[1].set_xlim([0, 0.33])
    axs[1].set_ylim([0, 60])
    axs[1].tick_params('y', labelleft=False)
    #
    mb_check = []
    k = 0
    #
    for mb in micro_mbs:
        #
        models, models_lower = nuda.matter.micro_esym_models_mb( mb )
        #
        for model in models:
            #
            esym = nuda.matter.setupMicroEsym( model = model )
            #
            if esym.esym is not None:
                print('mb:',mb,'model:',model)
                if mb in mb_check:
                    if esym.marker:
                        if esym.err:
                            axs[0].errorbar( esym.den, esym.esym, yerr=esym.esym_err, marker=esym.marker, linestyle=None, errorevery=esym.every, color=nuda.param.col[k] )
                        else:
                            axs[0].plot( esym.den, esym.esym, marker=esym.marker, linestyle=None, markevery=esym.every, color=nuda.param.col[k] )
                    else:
                        if esym.err:
                            axs[0].errorbar( esym.den, esym.esym, yerr=esym.esym_err, marker=esym.marker, linestyle=esym.linestyle, errorevery=esym.every, color=nuda.param.col[k] )
                        else:
                            axs[0].plot( esym.den, esym.esym, marker=esym.marker, linestyle=esym.linestyle, markevery=esym.every, color=nuda.param.col[k] )
                else:
                    mb_check.append(mb)
                    k += 1
                    if esym.marker:
                        if esym.err:
                            axs[0].errorbar( esym.den, esym.esym, yerr=esym.esym_err, marker=esym.marker, linestyle=None, label=mb, errorevery=esym.every, color=nuda.param.col[k] )
                        else:
                            axs[0].plot( esym.den, esym.esym, marker=esym.marker, linestyle=None, label=mb, markevery=esym.every, color=nuda.param.col[k] )
                    else:
                        if esym.err:
                            axs[0].errorbar( esym.den, esym.esym, yerr=esym.esym_err, marker=esym.marker, linestyle=esym.linestyle, label=mb, errorevery=esym.every, color=nuda.param.col[k] )
                        else:
                            axs[0].plot( esym.den, esym.esym, marker=esym.marker, linestyle=esym.linestyle, label=mb, markevery=esym.every, color=nuda.param.col[k] )
                    #axs[0].plot( esym.den, esym.esym, color=nuda.param.col[k], label=mb )
            if nuda.env.verb: esym.print_outputs( )
    axs[0].fill_between( band.den, y1=(band.e2a-band.e2a_std), y2=(band.e2a+band.e2a_std), color=band.color, alpha=band.alpha, visible=True )
    axs[0].plot( band.den, (band.e2a-band.e2a_std), color='k', linestyle='dashed' )
    axs[0].plot( band.den, (band.e2a+band.e2a_std), color='k', linestyle='dashed' )
    axs[0].text(0.05,5,'microscopic models',fontsize='10')
    #axs[0].legend(loc='upper left',fontsize='8', ncol=3)
    #
    model_check = []
    k = 0
    #
    for model in pheno_models:
        #
        params, params_lower = nuda.matter.pheno_params( model = model )
        #
        for param in params:
            #
            esym = nuda.matter.setupPhenoEsym( model = model, param = param )
            #
            if esym.esym is not None: 
                print('model:',model,' param:',param)
                if model in model_check:
                    axs[1].plot( esym.den, esym.esym, color=nuda.param.col[k] )
                else:
                    model_check.append(model)
                    k += 1
                    axs[1].plot( esym.den, esym.esym, color=nuda.param.col[k], label=model )
                #pheno.label=None
                #axs[1].plot( esym.den, esym.esym, label=esym.label )
            if nuda.env.verb: esym.print_outputs( )
    axs[1].fill_between( band.den, y1=(band.e2a-band.e2a_std), y2=(band.e2a+band.e2a_std), color=band.color, alpha=band.alpha, visible=True )
    axs[1].plot( band.den, (band.e2a-band.e2a_std), color='k', linestyle='dashed' )
    axs[1].plot( band.den, (band.e2a+band.e2a_std), color='k', linestyle='dashed' )
    axs[1].text(0.05,5,'phenomenological models',fontsize='10')
    #axs[1].legend(loc='upper left',fontsize='8', ncol=2)
    #axs[0,1].legend(loc='upper left',fontsize='xx-small', ncol=2)
    fig.legend(loc='upper left',bbox_to_anchor=(0.2,1.0),columnspacing=2,fontsize='8',ncol=4,frameon=False)
    #
    #plt.tight_layout()
    if pname is not None:
    	plt.savefig(pname, dpi=200)
    	plt.close()
    #