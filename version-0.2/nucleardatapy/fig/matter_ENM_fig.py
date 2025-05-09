import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def matter_ENM_fig( pname, micro_mbs, pheno_models, band ):
    """
    Plot nucleonic energy per particle E/A in NM.\
    The plot is 1x2 with:\
    [0,0]: E/A versus den (micro). [0,1]: E/A versus den (pheno).\

    :param pname: name of the figure (*.png)
    :type pname: str.
    :param micro_mbs: many-body (mb) approach considered.
    :type micro_mbs: str.
    :param pheno_models: models to run on.
    :type pheno_models: array of str.
    :param band: object instantiated on the reference band.
    :type band: object.

    """
    #
    print(f'Plot name: {pname}')
    #
    fig, axs = plt.subplots(1,2)
    fig.subplots_adjust(left=0.10, bottom=0.12, right=None, top=0.9, wspace=0.05, hspace=0.3 )
    #
    axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    axs[0].set_ylabel(r'$e_\text{NM}(n_\text{nuc})$')
    axs[0].set_xlim([0, 0.34])
    axs[0].set_ylim([0, 35])
    #
    axs[1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    #axs[1].set_ylabel(r'$e_{sym}(n)$')
    axs[1].set_xlim([0, 0.34])
    axs[1].set_ylim([0, 35])
    axs[1].tick_params('y', labelleft=False)
    #
    mb_check = []
    #
    for kmb,mb in enumerate(micro_mbs):
        #
        models, models_lower = nuda.matter.micro_models_mb( mb )
        #
        for model in models:
            #
            micro = nuda.matter.setupMicro( model = model )
            if nuda.env.verb: micro.print_outputs( )
            #
            check = nuda.matter.setupCheck( eos = micro, band = band )
            #
            if check.isInside:
                lstyle = 'solid'
            else:
                lstyle = 'dashed'
            #
            if micro.nm_e2a is not None:
                print('mb:',mb,'model:',model)
                if mb in mb_check:
                    if micro.marker:
                        if micro.e_err:
                            axs[0].errorbar( micro.nm_den, micro.nm_e2a, yerr=micro.nm_e2a_err, marker=micro.marker, markevery=micro.every, linestyle=lstyle, errorevery=micro.every, color=nuda.param.col[kmb] )
                        else:
                            axs[0].plot( micro.nm_den, micro.nm_e2a, marker=micro.marker, markevery=micro.every, linestyle=lstyle, color=nuda.param.col[kmb] )
                    else:
                        if micro.e_err:
                            axs[0].errorbar( micro.nm_den, micro.nm_e2a, yerr=micro.nm_e2a_err, marker=micro.marker, markevery=micro.every, linestyle=lstyle, errorevery=micro.every, color=nuda.param.col[kmb] )
                        else:
                            axs[0].plot( micro.nm_den, micro.nm_e2a, marker=micro.marker, markevery=micro.every, linestyle=lstyle, color=nuda.param.col[kmb] )
                else:
                    mb_check.append(mb)
                    if micro.marker:
                        if micro.e_err:
                            axs[0].errorbar( micro.nm_den, micro.nm_e2a, yerr=micro.nm_e2a_err, marker=micro.marker, markevery=micro.every, linestyle=lstyle, label=mb, errorevery=micro.every, color=nuda.param.col[kmb] )
                        else:
                            axs[0].plot( micro.nm_den, micro.nm_e2a, marker=micro.marker, markevery=micro.every, linestyle=lstyle, label=mb, color=nuda.param.col[kmb] )
                    else:
                        if micro.e_err:
                            axs[0].errorbar( micro.nm_den, micro.nm_e2a, yerr=micro.nm_e2a_err, marker=micro.marker, markevery=micro.every, linestyle=lstyle, label=mb, errorevery=micro.every, color=nuda.param.col[kmb] )
                        else:
                            axs[0].plot( micro.nm_den, micro.nm_e2a, marker=micro.marker, markevery=micro.every, linestyle=lstyle, label=mb, color=nuda.param.col[kmb] )
            # end model
        # end mb
    axs[0].fill_between( band.den, y1=(band.e2a-band.e2a_std), y2=(band.e2a+band.e2a_std), color=band.color, alpha=band.alpha, visible=True )
    axs[0].plot( band.den, (band.e2a-band.e2a_std), color='k', linestyle='dashed' )
    axs[0].plot( band.den, (band.e2a+band.e2a_std), color='k', linestyle='dashed' )
    axs[0].text(0.06,2,'microscopic models',fontsize='10')
    #
    model_check = []
    #
    for kmodel,model in enumerate(pheno_models):
        #
        params, params_lower = nuda.matter.pheno_params( model = model )
        #
        for param in params:
            #
            pheno = nuda.matter.setupPheno( model = model, param = param )
            if nuda.env.verb: pheno.print_outputs( )
            #
            check = nuda.matter.setupCheck( eos = pheno, band = band )
            #
            if check.isInside:
                lstyle = 'solid'
            else:
                lstyle = 'dashed'
            #
            if pheno.nm_e2a is not None: 
                print('model:',model,' param:',param)
                if model in model_check:
                    axs[1].plot( pheno.nm_den, pheno.nm_e2a, linestyle=lstyle, color=nuda.param.col[kmodel] )
                else:
                    model_check.append(model)
                    axs[1].plot( pheno.nm_den, pheno.nm_e2a, linestyle=lstyle, color=nuda.param.col[kmodel], label=model )
            # end param
        # end model
    axs[1].fill_between( band.den, y1=(band.e2a-band.e2a_std), y2=(band.e2a+band.e2a_std), color=band.color, alpha=band.alpha, visible=True )
    axs[1].plot( band.den, (band.e2a-band.e2a_std), color='k', linestyle='dashed' )
    axs[1].plot( band.den, (band.e2a+band.e2a_std), color='k', linestyle='dashed' )
    axs[1].text(0.06,2,'phenomenological models',fontsize='10')
    #
    #axs[1].legend(loc='upper left',fontsize='8', ncol=2)
    #axs[0,1].legend(loc='upper left',fontsize='xx-small', ncol=2)
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=5,frameon=False)
    #
    if pname is not None:
    	plt.savefig(pname, dpi=200)
    	plt.close()
    #