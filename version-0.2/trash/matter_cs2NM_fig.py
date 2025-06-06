import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def matter_cs2NM_fig( pname, micro_mbs, pheno_models, band ):
    """
    Plot nucleonic pressure in NM.\
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
    p_den = 0.32
    p_cen = 23.0
    p_std = 14.5 
    p_micro_cen = 17.0
    p_micro_std =  8.5
    p_pheno_cen = 23.0
    p_pheno_std = 14.5
    #
    fig, axs = plt.subplots(1,2)
    #fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.10, bottom=0.12, right=0.95, top=0.9, wspace=0.05, hspace=0.3 )
    #
    axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    axs[0].set_ylabel(r'$c_\text{s,NM}^2(n_\text{nuc})$')
    axs[0].set_xlim([0, 0.35])
    axs[0].set_ylim([-0.01, 0.4])
    #
    axs[1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    #axs[1].set_ylabel(r'$e_{sym}(n)$')
    axs[1].set_xlim([0, 0.35])
    axs[1].set_ylim([-0.01, 0.4])
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
            print('p_err:',micro.p_err)
            print('nm_den:',micro.nm_den)
            print('nm_pre:',micro.nm_pre)
            print('nm_pre_err:',micro.nm_pre_err)
            print('nm_cs2:',micro.nm_cs2)
            if micro.nm_cs2 is not None:
                print('mb:',mb,'model:',model)
                if mb in mb_check:
                    if micro.marker:
                        if micro.p_err:
                            axs[0].errorbar( micro.nm_den, micro.nm_cs2, yerr=micro.nm_pre_err, marker=micro.marker, linestyle=lstyle, errorevery=micro.every, color=nuda.param.col[kmb] )
                        else:
                            axs[0].plot( micro.nm_den, micro.nm_cs2, marker=micro.marker, linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                    else:
                        if micro.p_err:
                            axs[0].errorbar( micro.nm_den, micro.nm_cs2, yerr=micro.nm_pre_err, marker=micro.marker, linestyle=lstyle, errorevery=micro.every, color=nuda.param.col[kmb] )
                        else:
                            axs[0].plot( micro.nm_den, micro.nm_cs2, marker=micro.marker, linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                else:
                    mb_check.append(mb)
                    if micro.marker:
                        if micro.p_err:
                            axs[0].errorbar( micro.nm_den, micro.nm_cs2, yerr=micro.nm_pre_err, marker=micro.marker, linestyle=lstyle, label=mb, errorevery=micro.every, color=nuda.param.col[kmb] )
                        else:
                            axs[0].plot( micro.nm_den, micro.nm_cs2, marker=micro.marker, linestyle=lstyle, label=mb, markevery=micro.every, color=nuda.param.col[kmb] )
                    else:
                        if micro.p_err:
                            axs[0].errorbar( micro.nm_den, micro.nm_cs2, yerr=micro.nm_pre_err, marker=micro.marker, linestyle=lstyle, label=mb, errorevery=micro.every, color=nuda.param.col[kmb] )
                        else:
                            axs[0].plot( enm.nm_den, enm.nm_cs2, marker=enm.marker, linestyle=lstyle, label=mb, markevery=micro.every, color=nuda.param.col[kmb] )
            # end of model
        # end of mb
    #axs[0].errorbar( p_den, p_cen, yerr=p_std, color='k' )
    #axs[0].errorbar( p_den+0.005, p_micro_cen, yerr=p_micro_std, color='r' )
    #axs[0].text(0.02,40,'microscopic models',fontsize='10')
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
            if pheno.nm_pre is not None: 
                print('model:',model,' param:',param)
                if model in model_check:
                    axs[1].plot( pheno.nm_den, pheno.nm_cs2, linestyle=lstyle, color=nuda.param.col[kmodel] )
                else:
                    model_check.append(model)
                    axs[1].plot( pheno.nm_den, pheno.nm_cs2, linestyle=lstyle, color=nuda.param.col[kmodel], label=model )
            # end of param
        # end of model
    #axs[1].errorbar( p_den, p_cen, yerr=p_std, color='k' )
    #axs[1].errorbar( p_den+0.005, p_pheno_cen, yerr=p_pheno_std, color='r' )
    #axs[1].fill_between( band.den, y1=(band.e2a-band.e2a_std), y2=(band.e2a+band.e2a_std), color=band.color, alpha=band.alpha, visible=True )
    #axs[1].plot( band.den, (band.e2a-band.e2a_std), color='k', linestyle='dashed' )
    #axs[1].plot( band.den, (band.e2a+band.e2a_std), color='k', linestyle='dashed' )
    #axs[1].text(0.02,40,'phenomenological models',fontsize='10')
    #
    #axs[1].legend(loc='upper left',fontsize='8', ncol=2)
    #axs[0,1].legend(loc='upper left',fontsize='xx-small', ncol=2)
    fig.legend(loc='upper left',bbox_to_anchor=(0.1,1.0),columnspacing=2,fontsize='8',ncol=6,frameon=False)
    #
    #plt.tight_layout()
    if pname is not None:
    	plt.savefig(pname, dpi=200)
    	plt.close()
    #