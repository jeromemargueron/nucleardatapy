import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def matter_preSM_fig( pname, micro_mbs, pheno_models, band ):
    """
    Plot nucleonic pressure in SM.\
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
    :param matter: variable `matter`employed to define the band.
    :type matter: str.

    """
    #
    print(f'Plot name: {pname}')
    #
    p_den = 0.32
    p_cen = 11.5
    p_std =  5.5
    p_micro_cen =  9.0
    p_micro_std =  3.0
    p_pheno_cen = 14.5
    p_pheno_std =  2.5
    #
    fig, axs = plt.subplots(1,2)
    #fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.10, bottom=0.12, right=None, top=0.9, wspace=0.05, hspace=0.3 )
    #
    axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    axs[0].set_ylabel(r'$p_\text{SM}(n_\text{nuc})$')
    axs[0].set_xlim([0, 0.35])
    axs[0].set_ylim([-2, 45])
    #
    axs[1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    #axs[1].set_ylabel(r'$e_{sym}(n)$')
    axs[1].set_xlim([0, 0.35])
    axs[1].set_ylim([-2, 45])
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
                #continue
            #
            print('model:',model)
            print('err:',micro.p_err)
            print('den:',micro.sm_den)
            print('pre:',micro.sm_pre)
            print('pre_err:',micro.sm_pre_err)
            if micro.sm_pre is not None:
                print('mb:',mb,'model:',model)
                if mb in mb_check:
                    if micro.marker:
                        if micro.p_err:
                            axs[0].errorbar( micro.sm_den, micro.sm_pre, yerr=micro.sm_pre_err, marker=micro.marker, linestyle=lstyle, errorevery=micro.every, color=nuda.param.col[kmb] )
                        else:
                            axs[0].plot( micro.sm_den, micro.sm_pre, marker=micro.marker, linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                    else:
                        if micro.p_err:
                            axs[0].errorbar( micro.sm_den, micro.sm_pre, yerr=micro.sm_pre_err, marker=micro.marker, linestyle=lstyle, errorevery=micro.every, color=nuda.param.col[kmb] )
                        else:
                            axs[0].plot( micro.sm_den, micro.sm_pre, marker=micro.marker, linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                else:
                    mb_check.append(mb)
                    if micro.marker:
                        if micro.p_err:
                            axs[0].errorbar( esm.sm_den, micro.sm_pre, yerr=micro.sm_pre_err, marker=micro.marker, linestyle=lstyle, label=mb, errorevery=micro.every, color=nuda.param.col[kmb] )
                        else:
                            axs[0].plot( micro.sm_den, micro.sm_pre, marker=micro.marker, linestyle=lstyle, label=mb, markevery=micro.every, color=nuda.param.col[kmb] )
                    else:
                        if micro.p_err:
                            axs[0].errorbar( micro.sm_den, micro.sm_pre, yerr=micro.sm_pre_err, marker=micro.marker, linestyle=lstyle, label=mb, errorevery=micro.every, color=nuda.param.col[kmb] )
                        else:
                            axs[0].plot( micro.sm_den, esm.sm_pre, marker=esm.marker, linestyle=lstyle, label=mb, markevery=micro.every, color=nuda.param.col[kmb] )
            # end of model
        # end of mb
    axs[0].errorbar( p_den, p_cen, yerr=p_std, color='k' )
    axs[0].errorbar( p_den+0.005, p_micro_cen, yerr=p_micro_std, color='r' )
    axs[0].text(0.02,40,'microscopic models',fontsize='10')
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
                #continue
            #
            if pheno.sm_pre is not None: 
                print('model:',model,' param:',param)
                if model in model_check:
                    axs[1].plot( pheno.sm_den, pheno.sm_pre, linestyle=lstyle, color=nuda.param.col[kmodel] )
                else:
                    model_check.append(model)
                    axs[1].plot( pheno.sm_den, pheno.sm_pre, linestyle=lstyle, color=nuda.param.col[kmodel], label=model )
            # end of param
        # end of model
    axs[1].errorbar( p_den, p_cen, yerr=p_std, color='k' )
    axs[1].errorbar( p_den+0.005, p_pheno_cen, yerr=p_pheno_std, color='r' )
    axs[1].text(0.02,40,'phenomenological models',fontsize='10')
    #
    #axs[1].legend(loc='upper left',fontsize='8', ncol=2)
    #axs[0,1].legend(loc='upper left',fontsize='xx-small', ncol=2)
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=5,frameon=False)
    #
    if pname is not None:
    	plt.savefig(pname, dpi=200)
    	plt.close()
    #