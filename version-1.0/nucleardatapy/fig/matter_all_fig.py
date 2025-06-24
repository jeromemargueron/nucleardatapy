import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def matter_all_e2a_fig( pname, micro_mbs, pheno_models, band_check, band_plot, matter ):
    """
    Plot nucleonic energy per particle E/A in matter.\
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
    fig.subplots_adjust(left=0.10, bottom=0.12, right=0.95, top=0.9, wspace=0.05, hspace=0.3 )
    #
    if matter.lower() == 'nm':
        axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)', fontsize = '14' )
        axs[0].set_ylabel(r'$e_\text{int,NM}(n_\text{nuc})$ (MeV)', fontsize = '14' )
        axs[0].set_xlim([0, 0.33])
        axs[0].set_ylim([0, 35])
        axs[1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)', fontsize = '14' )
        #axs[1].set_ylabel(r'$e_{sym}(n)$')
        axs[1].set_xlim([0, 0.33])
        axs[1].set_ylim([0, 35])
        axs[1].tick_params('y', labelleft=False)
    elif matter.lower() == 'sm':
        axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)', fontsize = '14' )
        axs[0].set_ylabel(r'$e_\text{int,SM}(n_\text{nuc})$ (MeV)', fontsize = '14' )
        axs[0].set_xlim([0, 0.33])
        axs[0].set_ylim([-22, 5])
        axs[1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)', fontsize = '14' )
        #axs[1].set_ylabel(r'$e_{sym}(n)$')
        axs[1].set_xlim([0, 0.33])
        axs[1].set_ylim([-22, 5])
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
            if matter.lower() == 'sm' and 'NM' in model:
                continue
            #
            if 'fit' in model: continue
            #
            micro = nuda.matter.setupMicro( model = model )
            if nuda.env.verb: micro.print_outputs( )
            #
            check = nuda.matter.setupCheck( eos = micro, band = band_check )
            #
            if check.isInside:
                lstyle = 'solid'
            else:
                lstyle = 'dashed'
                #continue
            #
            if matter.lower() == 'nm':
                #
                if micro.nm_e2a_int is not None:
                    print('mb:',mb,'model:',model)
                    if mb in mb_check:
                        if micro.marker:
                            if micro.e_err:
                                axs[0].errorbar( micro.nm_den, micro.nm_e2a_int, yerr=micro.nm_e2a_err, marker=micro.marker, markevery=micro.every, linestyle=lstyle, errorevery=micro.every, color=nuda.param.col[kmb] )
                            else:
                                axs[0].plot( micro.nm_den, micro.nm_e2a_int, marker=micro.marker, markevery=micro.every, linestyle=lstyle, color=nuda.param.col[kmb] )
                        else:
                            if micro.e_err:
                                axs[0].errorbar( micro.nm_den, micro.nm_e2a_int, yerr=micro.nm_e2a_err, marker=micro.marker, markevery=micro.every, linestyle=lstyle, errorevery=micro.every, color=nuda.param.col[kmb] )
                            else:
                                axs[0].plot( micro.nm_den, micro.nm_e2a_int, marker=micro.marker, markevery=micro.every, linestyle=lstyle, color=nuda.param.col[kmb] )
                    else:
                        mb_check.append(mb)
                        if micro.marker:
                            if micro.e_err:
                                axs[0].errorbar( micro.nm_den, micro.nm_e2a_int, yerr=micro.nm_e2a_err, marker=micro.marker, markevery=micro.every, linestyle=lstyle, label=mb, errorevery=micro.every, color=nuda.param.col[kmb] )
                            else:
                                axs[0].plot( micro.nm_den, micro.nm_e2a_int, marker=micro.marker, markevery=micro.every, linestyle=lstyle, label=mb, color=nuda.param.col[kmb] )
                        else:
                            if micro.e_err:
                                axs[0].errorbar( micro.nm_den, micro.nm_e2a_int, yerr=micro.nm_e2a_err, marker=micro.marker, markevery=micro.every, linestyle=lstyle, label=mb, errorevery=micro.every, color=nuda.param.col[kmb] )
                            else:
                                axs[0].plot( micro.nm_den, micro.nm_e2a_int, marker=micro.marker, markevery=micro.every, linestyle=lstyle, label=mb, color=nuda.param.col[kmb] )
                #
            elif matter.lower() == 'sm':
                #
                if micro.sm_e2a_int is not None:
                    print('mb:',mb,'model:',model)
                    if mb in mb_check:
                        if micro.marker:
                            print('with marker 1:',micro.marker)
                            if micro.e_err:
                                print('with error',micro.e_err)
                                axs[0].errorbar( micro.sm_den, micro.sm_e2a_int, yerr=micro.sm_e2a_err, marker=micro.marker, markevery=micro.every, linestyle=lstyle, errorevery=micro.every, color=nuda.param.col[kmb] )
                            else:
                                print('with no error',micro.e_err)
                                axs[0].plot( micro.sm_den, micro.sm_e2a_int, marker=micro.marker, markevery=micro.every, linestyle=lstyle, color=nuda.param.col[kmb] )
                        else:
                            print('with no marker',micro.marker)
                            if micro.e_err:
                                print('with error',micro.e_err)
                                axs[0].errorbar( micro.sm_den, micro.sm_e2a_int, yerr=micro.sm_e2a_err, marker=micro.marker, linestyle=lstyle, errorevery=micro.every, color=nuda.param.col[kmb] )
                            else:
                                print('with no error',micro.e_err)
                                axs[0].plot( micro.sm_den, micro.sm_e2a_int, marker=micro.marker, linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                    else:
                        mb_check.append(mb)
                        if micro.marker:
                            print('with marker 2:',micro.marker)
                            if micro.e_err:
                                print('with error',micro.e_err)
                                axs[0].errorbar( micro.sm_den, micro.sm_e2a_int, yerr=micro.sm_e2a_err, marker=micro.marker, markevery=micro.every, linestyle=lstyle, label=mb, errorevery=micro.every, color=nuda.param.col[kmb] )
                            else:
                                print('with no error',micro.e_err)
                                axs[0].plot( micro.sm_den, micro.sm_e2a_int, marker=micro.marker, markevery=micro.every, linestyle=lstyle, label=mb, color=nuda.param.col[kmb] )
                        else:
                            print('with no marker',micro.marker)
                            if micro.e_err:
                                print('with error',micro.e_err)
                                axs[0].errorbar( micro.sm_den, micro.sm_e2a_int, yerr=micro.sm_e2a_err, marker=micro.marker, linestyle=lstyle, label=mb, errorevery=micro.every, color=nuda.param.col[kmb] )
                            else:
                                print('with no error',micro.e_err)
                                axs[0].plot( micro.sm_den, micro.sm_e2a_int, marker=micro.marker, linestyle=lstyle, label=mb, markevery=micro.every, color=nuda.param.col[kmb] )
                # end of matter
            # end of model
        # end of mb
    axs[0].fill_between( band_plot.den, y1=(band_plot.e2a_int-band_plot.e2a_std), y2=(band_plot.e2a_int+band_plot.e2a_std), color=band_plot.color, alpha=band_plot.alpha, visible=True )
    axs[0].plot( band_plot.den, (band_plot.e2a_int-band_plot.e2a_std), color='k', linestyle='dashed', zorder = 100 )
    axs[0].plot( band_plot.den, (band_plot.e2a_int+band_plot.e2a_std), color='k', linestyle='dashed', zorder = 100 )
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
            check = nuda.matter.setupCheck( eos = pheno, band = band_check )
            #
            if check.isInside:
                lstyle = 'solid'
            else:
                lstyle = 'dashed'
                #continue
            #
            if matter.lower() == 'nm':
                #
                if pheno.nm_e2a_int is not None: 
                    print('model:',model,' param:',param)
                    if model in model_check:
                        axs[1].plot( pheno.nm_den, pheno.nm_e2a_int, linestyle=lstyle, color=nuda.param.col[kmodel] )
                    else:
                        model_check.append(model)
                        axs[1].plot( pheno.nm_den, pheno.nm_e2a_int, linestyle=lstyle, color=nuda.param.col[kmodel], label=model )
                #
            elif matter.lower() == 'sm':
                #
                if pheno.sm_e2a_int is not None: 
                    print('model:',model,' param:',param)
                    if model in model_check:
                        axs[1].plot( pheno.sm_den, pheno.sm_e2a_int, linestyle=lstyle, color=nuda.param.col[kmodel] )
                    else:
                        model_check.append(model)
                        axs[1].plot( pheno.sm_den, pheno.sm_e2a_int, linestyle=lstyle, color=nuda.param.col[kmodel], label=model )
            # end of param
        # end of model
    axs[1].fill_between( band_plot.den, y1=(band_plot.e2a_int-band_plot.e2a_std), y2=(band_plot.e2a_int+band_plot.e2a_std), color=band_plot.color, alpha=band_plot.alpha, visible=True )
    axs[1].plot( band_plot.den, (band_plot.e2a_int-band_plot.e2a_std), color='k', linestyle='dashed', zorder = 100 )
    axs[1].plot( band_plot.den, (band_plot.e2a_int+band_plot.e2a_std), color='k', linestyle='dashed', zorder = 100 )
    #
    #axs[1].legend(loc='upper left',fontsize='8', ncol=2)
    #axs[0,1].legend(loc='upper left',fontsize='xx-small', ncol=2)
    if matter.lower() == 'nm':
        axs[0].text(0.06,2,'microscopic models',fontsize='12')
        axs[1].text(0.06,2,'phenomenological models',fontsize='12')
        fig.legend(loc='upper left',bbox_to_anchor=(0.07,1.0),columnspacing=2,fontsize='8',ncol=6,frameon=False)
    elif matter.lower() == 'sm':
        axs[0].text(0.03,2,'microscopic models',fontsize='12')
        axs[1].text(0.03,2,'phenomenological models',fontsize='12')
        fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=5,frameon=False)
    #
    if pname is not None:
    	plt.savefig(pname, dpi=200)
    #
    	plt.close()
    #

def matter_all_Esym_fig( pname, micro_mbs, pheno_models, band_check, band_plot ):
    """
    Plot nucleonic symmetry energy.\
    The plot is 2x2 with:\
    [0,0]: Esym versus den.            [0,1]: Esym versus kfn.\
    [1,0]: Esym/Esym_NRFFG versus den. [1,1]: Esym/Esym_NRFFG versus kfn.\

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
    matter = 'Esym'
    #
    fig, axs = plt.subplots(1,2)
    #fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.10, bottom=0.12, right=0.95, top=0.9, wspace=0.05, hspace=0.05 )
    #
    axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)', fontsize = '14' )
    axs[0].set_ylabel(r'$e_\text{sym}(n_\text{nuc})$ (MeV)', fontsize = '14' )
    axs[0].set_xlim([0, 0.33])
    axs[0].set_ylim([0, 60])
    #
    axs[1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)', fontsize = '14' )
    #axs[1].set_ylabel(r'$e_{sym}(n)$')
    axs[1].set_xlim([0, 0.33])
    axs[1].set_ylim([0, 60])
    axs[1].tick_params('y', labelleft=False)
    #
    mb_check = []
    #
    for kmb,mb in enumerate(micro_mbs):
        #
        models, models_lower = nuda.matter.micro_esym_models_mb( mb )
        #
        for model in models:
            #
            if 'fit' in model: continue
            #
            micro = nuda.matter.setupMicroEsym( model = model )
            if nuda.env.verb: micro.print_outputs( )
            #
            check = nuda.matter.setupCheck( eos = micro, band = band_check )
            #
            if check.isInside:
                lstyle = 'solid'
            else:
                lstyle = 'dashed'
            #
            if micro.esym is not None:
                print('mb:',mb,'model:',model)
                if mb in mb_check:
                    if micro.marker:
                        if micro.err:
                            axs[0].errorbar( micro.den, micro.esym, yerr=micro.esym_err, marker=micro.marker, linestyle=lstyle, markevery=micro.every, errorevery=micro.every, color=nuda.param.col[kmb] )
                        else:
                            axs[0].plot( micro.den, micro.esym, marker=micro.marker, linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                    else:
                        if micro.err:
                            axs[0].errorbar( micro.den, micro.esym, yerr=micro.esym_err, marker=micro.marker, linestyle=lstyle, markevery=micro.every, errorevery=micro.every, color=nuda.param.col[kmb] )
                        else:
                            axs[0].plot( micro.den, micro.esym, marker=micro.marker, linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                else:
                    mb_check.append(mb)
                    if micro.marker:
                        if micro.err:
                            axs[0].errorbar( micro.den, micro.esym, yerr=micro.esym_err, marker=micro.marker, linestyle=lstyle, label=mb, markevery=micro.every, errorevery=micro.every, color=nuda.param.col[kmb] )
                        else:
                            axs[0].plot( micro.den, micro.esym, marker=micro.marker, linestyle=lstyle, label=mb, markevery=micro.every, color=nuda.param.col[kmb] )
                    else:
                        if micro.err:
                            axs[0].errorbar( micro.den, micro.esym, yerr=micro.esym_err, marker=micro.marker, linestyle=lstyle, label=mb, markevery=micro.every, errorevery=micro.every, color=nuda.param.col[kmb] )
                        else:
                            axs[0].plot( micro.den, micro.esym, marker=micro.marker, linestyle=lstyle, label=mb, markevery=micro.every, color=nuda.param.col[kmb] )
            # end of model
        # end of mb
    axs[0].fill_between( band_plot.den, y1=(band_plot.e2a_int-band_plot.e2a_std), y2=(band_plot.e2a_int+band_plot.e2a_std), color=band_plot.color, alpha=band_plot.alpha, visible=True )
    axs[0].plot( band_plot.den, (band_plot.e2a_int-band_plot.e2a_std), color='k', linestyle='dashed', zorder=100 )
    axs[0].plot( band_plot.den, (band_plot.e2a_int+band_plot.e2a_std), color='k', linestyle='dashed', zorder=100 )
    #
    model_check = []
    #
    for kmodel,model in enumerate(pheno_models):
        #
        params, params_lower = nuda.matter.pheno_params( model = model )
        #
        for param in params:
            #
            pheno = nuda.matter.setupPhenoEsym( model = model, param = param )
            if nuda.env.verb: pheno.print_outputs( )
            #
            check = nuda.matter.setupCheck( eos = pheno, band = band_check )
            #
            if check.isInside:
                lstyle = 'solid'
            else:
                lstyle = 'dashed'
            #
            if pheno.esym is not None: 
                print('model:',model,' param:',param)
                if model in model_check:
                    axs[1].plot( pheno.den, pheno.esym, linestyle=lstyle, color=nuda.param.col[kmodel] )
                else:
                    model_check.append(model)
                    axs[1].plot( pheno.den, pheno.esym, linestyle=lstyle, color=nuda.param.col[kmodel], label=model )
            # end of param
        # end of model
    axs[1].fill_between( band_plot.den, y1=(band_plot.e2a_int-band_plot.e2a_std), y2=(band_plot.e2a_int+band_plot.e2a_std), color=band_plot.color, alpha=band_plot.alpha, visible=True )
    axs[1].plot( band_plot.den, (band_plot.e2a_int-band_plot.e2a_std), color='k', linestyle='dashed', zorder=100 )
    axs[1].plot( band_plot.den, (band_plot.e2a_int+band_plot.e2a_std), color='k', linestyle='dashed', zorder=100 )
    #
    axs[0].text(0.05,5,'microscopic models',fontsize='12')
    axs[1].text(0.05,5,'phenomenological models',fontsize='12')
    #
    #axs[1].legend(loc='upper left',fontsize='8', ncol=2)
    #axs[0,1].legend(loc='upper left',fontsize='xx-small', ncol=2)
    fig.legend(loc='upper left',bbox_to_anchor=(0.2,1.0),columnspacing=2,fontsize='8',ncol=5,frameon=False)
    #
    if pname is not None:
        plt.savefig(pname, dpi=200)
        plt.close()
    #

def matter_all_pre_fig( pname, micro_mbs, pheno_models, band_check, matter ):
    """
    Plot nucleonic pressure in matter.\
    The plot is 1x2 with:\
    [0]: pre versus den (micro). [1]: pre versus den (pheno).\

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
    fig.subplots_adjust(left=0.10, bottom=0.12, right=0.95, top=0.9, wspace=0.05, hspace=0.3 )
    #
    p_den = 0.32
    if matter.lower() == 'nm':
        p_cen = 23.0
        p_std = 14.5 
        p_micro_cen = 17.0
        p_micro_std =  8.5
        p_pheno_cen = 23.0
        p_pheno_std = 14.5
        axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)', fontsize = '14' )
        axs[0].set_ylabel(r'$p_\text{NM}(n_\text{nuc})$ (MeV fm$^{-3}$)', fontsize = '14' )
        axs[0].set_xlim([0, 0.35])
        axs[0].set_ylim([-2, 45])
        axs[1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)', fontsize = '14' )
        #axs[1].set_ylabel(r'$e_{sym}(n)$')
        axs[1].set_xlim([0, 0.35])
        axs[1].set_ylim([-2, 45])
        axs[1].tick_params('y', labelleft=False)
    elif matter.lower() == 'sm':
        p_cen = 16.0
        p_std = 12.0
        p_micro_cen = 10.0
        p_micro_std =  6.0
        p_pheno_cen = 19.0
        p_pheno_std =  9.0
        axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)', fontsize = '14' )
        axs[0].set_ylabel(r'$p_\text{SM}(n_\text{nuc})$ (MeV fm$^{-3}$)', fontsize = '14' )
        axs[0].set_xlim([0, 0.35])
        axs[0].set_ylim([-2, 45])
        axs[1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)', fontsize = '14' )
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
            if 'fit' in model: continue
            #
            micro = nuda.matter.setupMicro( model = model )
            if nuda.env.verb: micro.print_outputs( )
            #
            check = nuda.matter.setupCheck( eos = micro, band = band_check )
            #
            if check.isInside:
                lstyle = 'solid'
            else:
                lstyle = 'dashed'
                #continue
            #
            if matter.lower() == 'nm':
                #
                if micro.nm_pre is not None:
                    print('mb:',mb,'model:',model)
                    if mb in mb_check:
                        if micro.marker:
                            if micro.p_err:
                                axs[0].errorbar( micro.nm_den, micro.nm_pre, yerr=micro.nm_pre_err, marker=micro.marker, markevery=micro.every, linestyle=lstyle, errorevery=micro.every, color=nuda.param.col[kmb] )
                            else:
                                axs[0].plot( micro.nm_den, micro.nm_pre, marker=micro.marker, markevery=micro.every, linestyle=lstyle, color=nuda.param.col[kmb] )
                        else:
                            if micro.p_err:
                                axs[0].errorbar( micro.nm_den, micro.nm_pre, yerr=micro.nm_pre_err, marker=micro.marker, markevery=micro.every, linestyle=lstyle, errorevery=micro.every, color=nuda.param.col[kmb] )
                            else:
                                axs[0].plot( micro.nm_den, micro.nm_pre, marker=micro.marker, markevery=micro.every, linestyle=lstyle, color=nuda.param.col[kmb] )
                    else:
                        mb_check.append(mb)
                        if micro.marker:
                            if micro.p_err:
                                axs[0].errorbar( micro.nm_den, micro.nm_pre, yerr=micro.nm_pre_err, marker=micro.marker, markevery=micro.every, linestyle=lstyle, label=mb, errorevery=micro.every, color=nuda.param.col[kmb] )
                            else:
                                axs[0].plot( micro.nm_den, micro.nm_pre, marker=micro.marker, markevery=micro.every, linestyle=lstyle, label=mb, color=nuda.param.col[kmb] )
                        else:
                            if micro.p_err:
                                axs[0].errorbar( micro.nm_den, micro.nm_pre, yerr=micro.nm_pre_err, marker=micro.marker, markevery=micro.every, linestyle=lstyle, label=mb, errorevery=micro.every, color=nuda.param.col[kmb] )
                            else:
                                axs[0].plot( micro.nm_den, micro.nm_pre, marker=micro.marker, markevery=micro.every, linestyle=lstyle, label=mb, color=nuda.param.col[kmb] )
                #
            elif matter.lower() == 'sm':
                #
                if micro.sm_pre is not None:
                    print('mb:',mb,'model:',model)
                    if mb in mb_check:
                        if micro.marker:
                            print('with marker 1:',micro.marker)
                            if micro.p_err:
                                print('with error',micro.p_err)
                                axs[0].errorbar( micro.sm_den, micro.sm_pre, yerr=micro.sm_pre_err, marker=micro.marker, markevery=micro.every, linestyle=lstyle, errorevery=micro.every, color=nuda.param.col[kmb] )
                            else:
                                print('with no error',micro.p_err)
                                axs[0].plot( micro.sm_den, micro.sm_pre, marker=micro.marker, markevery=micro.every, linestyle=lstyle, color=nuda.param.col[kmb] )
                        else:
                            print('with no marker',micro.marker)
                            if micro.p_err:
                                print('with error',micro.p_err)
                                axs[0].errorbar( micro.sm_den, micro.sm_pre, yerr=micro.sm_pre_err, marker=micro.marker, linestyle=lstyle, errorevery=micro.every, color=nuda.param.col[kmb] )
                            else:
                                print('with no error',micro.p_err)
                                axs[0].plot( micro.sm_den, micro.sm_pre, marker=micro.marker, linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                    else:
                        mb_check.append(mb)
                        if micro.marker:
                            print('with marker 2:',micro.marker)
                            if micro.p_err:
                                print('with error',micro.p_err)
                                axs[0].errorbar( micro.sm_den, micro.sm_pre, yerr=micro.sm_pre_err, marker=micro.marker, markevery=micro.every, linestyle=lstyle, label=mb, errorevery=micro.every, color=nuda.param.col[kmb] )
                            else:
                                print('with no error',micro.p_err)
                                axs[0].plot( micro.sm_den, micro.sm_pre, marker=micro.marker, markevery=micro.every, linestyle=lstyle, label=mb, color=nuda.param.col[kmb] )
                        else:
                            print('with no marker',micro.marker)
                            if micro.p_err:
                                print('with error',micro.p_err)
                                axs[0].errorbar( micro.sm_den, micro.sm_pre, yerr=micro.sm_pre_err, marker=micro.marker, linestyle=lstyle, label=mb, errorevery=micro.every, color=nuda.param.col[kmb] )
                            else:
                                print('with no error',micro.p_err)
                                axs[0].plot( micro.sm_den, micro.sm_pre, marker=micro.marker, linestyle=lstyle, label=mb, markevery=micro.every, color=nuda.param.col[kmb] )
                # end of matter
            # end of model
        # end of mb
    #
    axs[0].errorbar( p_den, p_cen, yerr=p_std, color='k' )
    axs[0].errorbar( p_den+0.005, p_micro_cen, yerr=p_micro_std, color='r' )
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
            check = nuda.matter.setupCheck( eos = pheno, band = band_check )
            #
            if check.isInside:
                lstyle = 'solid'
            else:
                lstyle = 'dashed'
                #continue
            #
            if matter.lower() == 'nm':
                #
                if pheno.nm_pre is not None: 
                    print('model:',model,' param:',param)
                    if model in model_check:
                        axs[1].plot( pheno.nm_den, pheno.nm_pre, linestyle=lstyle, color=nuda.param.col[kmodel] )
                    else:
                        model_check.append(model)
                        axs[1].plot( pheno.nm_den, pheno.nm_pre, linestyle=lstyle, color=nuda.param.col[kmodel], label=model )
                #
            elif matter.lower() == 'sm':
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
    #
    axs[1].errorbar( p_den, p_cen, yerr=p_std, color='k' )
    axs[1].errorbar( p_den+0.005, p_pheno_cen, yerr=p_pheno_std, color='r' )
    #axs[1].legend(loc='upper left',fontsize='8', ncol=2)
    #axs[0,1].legend(loc='upper left',fontsize='xx-small', ncol=2)
    if matter.lower() == 'nm':
        axs[0].text(0.02,40,'microscopic models',fontsize='12')
        axs[1].text(0.02,40,'phenomenological models',fontsize='12')
        fig.legend(loc='upper left',bbox_to_anchor=(0.1,1.0),columnspacing=2,fontsize='8',ncol=6,frameon=False)
    elif matter.lower() == 'sm':
        axs[0].text(0.02,40,'microscopic models',fontsize='12')
        axs[1].text(0.02,40,'phenomenological models',fontsize='12')
        fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=5,frameon=False)
    #
    if pname is not None:
        plt.savefig(pname, dpi=200)
    #
        plt.close()
    #

def matter_all_eos_fig( pname, micro_mbs, pheno_models, band_check, matter ):
    """
    Plot EoS in matter.\
    The plot is 1x2 with:\
    [0]: pre versus energy-density (micro). [1]: pre versus energy-density (pheno).\

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
    fig.subplots_adjust(left=0.10, bottom=0.12, right=0.95, top=0.9, wspace=0.05, hspace=0.3 )
    #
    p_eps = 312.0
    if matter.lower() == 'nm':
        p_cen = 23.0
        p_std = 14.5 
        p_micro_cen = 17.0
        p_micro_std =  8.5
        p_pheno_cen = 23.0
        p_pheno_std = 14.5
        axs[0].set_xlabel(r'$\epsilon_\text{NM}$ (MeV fm$^{-3}$)', fontsize = '14' )
        axs[0].set_ylabel(r'$p_\text{NM}(n_\text{nuc})$ (MeV fm$^{-3}$)', fontsize = '14' )
        axs[0].set_xlim([0, 350])
        axs[0].set_ylim([-2, 45])
        axs[1].set_xlabel(r'$\epsilon_\text{NM}$ (MeV fm$^{-3}$)', fontsize = '14' )
        #axs[1].set_ylabel(r'$e_{sym}(n)$')
        axs[1].set_xlim([0, 350])
        axs[1].set_ylim([-2, 45])
        axs[1].tick_params('y', labelleft=False)
    elif matter.lower() == 'sm':
        p_cen = 18.75
        p_std = 14.25
        p_micro_cen = 11.0
        p_micro_std =  6.5
        p_pheno_cen = 22.0
        p_pheno_std = 11.0
        axs[0].set_xlabel(r'$\epsilon_\text{SM}$ (MeV fm$^{-3}$)', fontsize = '14' )
        axs[0].set_ylabel(r'$p_\text{SM}(n_\text{nuc})$ (MeV fm$^{-3}$)', fontsize = '14' )
        axs[0].set_xlim([0, 350])
        axs[0].set_ylim([-2, 45])
        axs[1].set_xlabel(r'$\epsilon_\text{SM}$ (MeV fm$^{-3}$)', fontsize = '14' )
        #axs[1].set_ylabel(r'$e_{sym}(n)$')
        axs[1].set_xlim([0, 350])
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
            if 'fit' in model: continue
            #
            micro = nuda.matter.setupMicro( model = model )
            if nuda.env.verb: micro.print_outputs( )
            #
            check = nuda.matter.setupCheck( eos = micro, band = band_check )
            #
            if check.isInside:
                lstyle = 'solid'
            else:
                lstyle = 'dashed'
                #continue
            #
            if matter.lower() == 'nm':
                #
                if micro.nm_pre is not None:
                    print('mb:',mb,'model:',model)
                    if mb in mb_check:
                        if micro.marker:
                            if micro.p_err:
                                axs[0].errorbar( micro.nm_eps, micro.nm_pre, yerr=micro.nm_pre_err, marker=micro.marker, markevery=micro.every, linestyle=lstyle, errorevery=micro.every, color=nuda.param.col[kmb] )
                            else:
                                axs[0].plot( micro.nm_eps, micro.nm_pre, marker=micro.marker, markevery=micro.every, linestyle=lstyle, color=nuda.param.col[kmb] )
                        else:
                            if micro.p_err:
                                axs[0].errorbar( micro.nm_eps, micro.nm_pre, yerr=micro.nm_pre_err, marker=micro.marker, markevery=micro.every, linestyle=lstyle, errorevery=micro.every, color=nuda.param.col[kmb] )
                            else:
                                axs[0].plot( micro.nm_eps, micro.nm_pre, marker=micro.marker, markevery=micro.every, linestyle=lstyle, color=nuda.param.col[kmb] )
                    else:
                        mb_check.append(mb)
                        if micro.marker:
                            if micro.p_err:
                                axs[0].errorbar( micro.nm_eps, micro.nm_pre, yerr=micro.nm_pre_err, marker=micro.marker, markevery=micro.every, linestyle=lstyle, label=mb, errorevery=micro.every, color=nuda.param.col[kmb] )
                            else:
                                axs[0].plot( micro.nm_eps, micro.nm_pre, marker=micro.marker, markevery=micro.every, linestyle=lstyle, label=mb, color=nuda.param.col[kmb] )
                        else:
                            if micro.p_err:
                                axs[0].errorbar( micro.nm_eps, micro.nm_pre, yerr=micro.nm_pre_err, marker=micro.marker, markevery=micro.every, linestyle=lstyle, label=mb, errorevery=micro.every, color=nuda.param.col[kmb] )
                            else:
                                axs[0].plot( micro.nm_eps, micro.nm_pre, marker=micro.marker, markevery=micro.every, linestyle=lstyle, label=mb, color=nuda.param.col[kmb] )
                #
            elif matter.lower() == 'sm':
                #
                if micro.sm_pre is not None:
                    print('mb:',mb,'model:',model)
                    if mb in mb_check:
                        if micro.marker:
                            print('with marker 1:',micro.marker)
                            if micro.p_err:
                                print('with error',micro.p_err)
                                axs[0].errorbar( micro.sm_eps, micro.sm_pre, yerr=micro.sm_pre_err, marker=micro.marker, markevery=micro.every, linestyle=lstyle, errorevery=micro.every, color=nuda.param.col[kmb] )
                            else:
                                print('with no error',micro.p_err)
                                axs[0].plot( micro.sm_eps, micro.sm_pre, marker=micro.marker, markevery=micro.every, linestyle=lstyle, color=nuda.param.col[kmb] )
                        else:
                            print('with no marker',micro.marker)
                            if micro.p_err:
                                print('with error',micro.p_err)
                                axs[0].errorbar( micro.sm_eps, micro.sm_pre, yerr=micro.sm_pre_err, marker=micro.marker, linestyle=lstyle, errorevery=micro.every, color=nuda.param.col[kmb] )
                            else:
                                print('with no error',micro.p_err)
                                axs[0].plot( micro.sm_eps, micro.sm_pre, marker=micro.marker, linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                    else:
                        mb_check.append(mb)
                        if micro.marker:
                            print('with marker 2:',micro.marker)
                            if micro.p_err:
                                print('with error',micro.p_err)
                                axs[0].errorbar( micro.sm_eps, micro.sm_pre, yerr=micro.sm_pre_err, marker=micro.marker, markevery=micro.every, linestyle=lstyle, label=mb, errorevery=micro.every, color=nuda.param.col[kmb] )
                            else:
                                print('with no error',micro.p_err)
                                axs[0].plot( micro.sm_eps, micro.sm_pre, marker=micro.marker, markevery=micro.every, linestyle=lstyle, label=mb, color=nuda.param.col[kmb] )
                        else:
                            print('with no marker',micro.marker)
                            if micro.p_err:
                                print('with error',micro.p_err)
                                axs[0].errorbar( micro.sm_eps, micro.sm_pre, yerr=micro.sm_pre_err, marker=micro.marker, linestyle=lstyle, label=mb, errorevery=micro.every, color=nuda.param.col[kmb] )
                            else:
                                print('with no error',micro.p_err)
                                axs[0].plot( micro.sm_eps, micro.sm_pre, marker=micro.marker, linestyle=lstyle, label=mb, markevery=micro.every, color=nuda.param.col[kmb] )
                # end of matter
            # end of model
        # end of mb
    #
    axs[0].errorbar( p_eps, p_cen, yerr=p_std, color='k' )
    axs[0].errorbar( p_eps+5, p_micro_cen, yerr=p_micro_std, color='r' )
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
            check = nuda.matter.setupCheck( eos = pheno, band = band_check )
            #
            if check.isInside:
                lstyle = 'solid'
            else:
                lstyle = 'dashed'
                #continue
            #
            if matter.lower() == 'nm':
                #
                if pheno.nm_pre is not None: 
                    print('model:',model,' param:',param)
                    if model in model_check:
                        axs[1].plot( pheno.nm_eps, pheno.nm_pre, linestyle=lstyle, color=nuda.param.col[kmodel] )
                    else:
                        model_check.append(model)
                        axs[1].plot( pheno.nm_eps, pheno.nm_pre, linestyle=lstyle, color=nuda.param.col[kmodel], label=model )
                #
            elif matter.lower() == 'sm':
                #
                if pheno.sm_pre is not None: 
                    print('model:',model,' param:',param)
                    if model in model_check:
                        axs[1].plot( pheno.sm_eps, pheno.sm_pre, linestyle=lstyle, color=nuda.param.col[kmodel] )
                    else:
                        model_check.append(model)
                        axs[1].plot( pheno.sm_eps, pheno.sm_pre, linestyle=lstyle, color=nuda.param.col[kmodel], label=model )
            # end of param
        # end of model
    #
    axs[1].errorbar( p_eps, p_cen, yerr=p_std, color='k' )
    axs[1].errorbar( p_eps+5, p_pheno_cen, yerr=p_pheno_std, color='r' )
    #axs[1].legend(loc='upper left',fontsize='8', ncol=2)
    #axs[0,1].legend(loc='upper left',fontsize='xx-small', ncol=2)
    if matter.lower() == 'nm':
        axs[0].text(10,40,'microscopic models',fontsize='12')
        axs[1].text(10,40,'phenomenological models',fontsize='12')
        fig.legend(loc='upper left',bbox_to_anchor=(0.1,1.0),columnspacing=2,fontsize='8',ncol=6,frameon=False)
    elif matter.lower() == 'sm':
        axs[0].text(10,40,'microscopic models',fontsize='12')
        axs[1].text(10,40,'phenomenological models',fontsize='12')
        fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=5,frameon=False)
    #
    if pname is not None:
        plt.savefig(pname, dpi=200)
    #
        plt.close()
    #

def matter_all_cs2_fig( pname, micro_mbs, pheno_models, band_check, matter ):
    """
    Plot nucleonic sound speed in matter.\
    The plot is 1x2 with:\
    [0]: cs2 versus den (micro). [1]: cs2 versus den (pheno).\

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
    fig.subplots_adjust(left=0.10, bottom=0.12, right=0.95, top=0.9, wspace=0.05, hspace=0.3 )
    #
    if matter.lower() == 'nm':
        axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)', fontsize = '14' )
        axs[0].set_ylabel(r'$c_\text{s,NM}^2/c^2(n_\text{nuc})$', fontsize = '14' )
        axs[0].set_xlim([0, 0.35])
        axs[0].set_ylim([-0.01, 0.4])
        axs[1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)', fontsize = '14' )
        #axs[1].set_ylabel(r'$e_{sym}(n)$')
        axs[1].set_xlim([0, 0.35])
        axs[1].set_ylim([-0.01, 0.4])
        axs[1].tick_params('y', labelleft=False)
    elif matter.lower() == 'sm':
        axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)', fontsize = '14' )
        axs[0].set_ylabel(r'$c_\text{s,SM}^2/c^2(n_\text{nuc})$', fontsize = '14' )
        axs[0].set_xlim([0, 0.35])
        axs[0].set_ylim([-0.02, 0.3])
        axs[1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)', fontsize = '14' )
        #axs[1].set_ylabel(r'$e_{sym}(n)$')
        axs[1].set_xlim([0, 0.35])
        axs[1].set_ylim([-0.02, 0.3])
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
            if 'fit' in model: continue
            #
            micro = nuda.matter.setupMicro( model = model )
            if nuda.env.verb: micro.print_outputs( )
            #
            check = nuda.matter.setupCheck( eos = micro, band = band_check )
            #
            if check.isInside:
                lstyle = 'solid'
            else:
                lstyle = 'dashed'
                #continue
            #
            if matter.lower() == 'nm':
                #
                if micro.nm_cs2 is not None:
                    print('mb:',mb,'model:',model)
                    if mb in mb_check:
                        if micro.marker:
                            if micro.cs2_err:
                                axs[0].errorbar( micro.nm_den[:-1], micro.nm_cs2[:-1], yerr=micro.nm_cs2_err[:-1], marker=micro.marker, markevery=micro.every, linestyle=lstyle, errorevery=micro.every, color=nuda.param.col[kmb] )
                            else:
                                axs[0].plot( micro.nm_den[:-1], micro.nm_cs2[:-1], marker=micro.marker, markevery=micro.every, linestyle=lstyle, color=nuda.param.col[kmb] )
                        else:
                            if micro.cs2_err:
                                axs[0].errorbar( micro.nm_den[:-1], micro.nm_cs2[:-1], yerr=micro.nm_cs2_err[:-1], marker=micro.marker, markevery=micro.every, linestyle=lstyle, errorevery=micro.every, color=nuda.param.col[kmb] )
                            else:
                                axs[0].plot( micro.nm_den[:-1], micro.nm_cs2[:-1], marker=micro.marker, markevery=micro.every, linestyle=lstyle, color=nuda.param.col[kmb] )
                    else:
                        mb_check.append(mb)
                        if micro.marker:
                            if micro.cs2_err:
                                axs[0].errorbar( micro.nm_den[:-1], micro.nm_cs2[:-1], yerr=micro.nm_cs2_err[:-1], marker=micro.marker, markevery=micro.every, linestyle=lstyle, label=mb, errorevery=micro.every, color=nuda.param.col[kmb] )
                            else:
                                axs[0].plot( micro.nm_den[:-1], micro.nm_cs2[:-1], marker=micro.marker, markevery=micro.every, linestyle=lstyle, label=mb, color=nuda.param.col[kmb] )
                        else:
                            if micro.cs2_err:
                                axs[0].errorbar( micro.nm_den[:-1], micro.nm_cs2[:-1], yerr=micro.nm_cs2_err[:-1], marker=micro.marker, markevery=micro.every, linestyle=lstyle, label=mb, errorevery=micro.every, color=nuda.param.col[kmb] )
                            else:
                                axs[0].plot( micro.nm_den[:-1], micro.nm_cs2[:-1], marker=micro.marker, markevery=micro.every, linestyle=lstyle, label=mb, color=nuda.param.col[kmb] )
                #
            elif matter.lower() == 'sm':
                #
                if micro.sm_pre is not None:
                    print('mb:',mb,'model:',model)
                    if mb in mb_check:
                        if micro.marker:
                            print('with marker 1:',micro.marker)
                            if micro.cs2_err:
                                print('with error',micro.cs2_err)
                                axs[0].errorbar( micro.sm_den[:-1], micro.sm_cs2[:-1], yerr=micro.sm_cs2_err[:-1], marker=micro.marker, markevery=micro.every, linestyle=lstyle, errorevery=micro.every, color=nuda.param.col[kmb] )
                            else:
                                print('with no error',micro.cs2_err)
                                axs[0].plot( micro.sm_den[:-1], micro.sm_cs2[:-1], marker=micro.marker, markevery=micro.every, linestyle=lstyle, color=nuda.param.col[kmb] )
                        else:
                            print('with no marker',micro.marker)
                            if micro.cs2_err:
                                print('with error',micro.cs2_err)
                                axs[0].errorbar( micro.sm_den[:-1], micro.sm_cs2[:-1], yerr=micro.sm_cs2_err[:-1], marker=micro.marker, linestyle=lstyle, errorevery=micro.every, color=nuda.param.col[kmb] )
                            else:
                                print('with no error',micro.cs2_err)
                                axs[0].plot( micro.sm_den[:-1], micro.sm_cs2[:-1], marker=micro.marker, linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                    else:
                        mb_check.append(mb)
                        if micro.marker:
                            print('with marker 2:',micro.marker)
                            if micro.cs2_err:
                                print('with error',micro.cs2_err)
                                axs[0].errorbar( micro.sm_den[:-1], micro.sm_cs2[:-1], yerr=micro.sm_cs2_err[:-1], marker=micro.marker, markevery=micro.every, linestyle=lstyle, label=mb, errorevery=micro.every, color=nuda.param.col[kmb] )
                            else:
                                print('with no error',micro.cs2_err)
                                axs[0].plot( micro.sm_den[:-1], micro.sm_cs2[:-1], marker=micro.marker, markevery=micro.every, linestyle=lstyle, label=mb, color=nuda.param.col[kmb] )
                        else:
                            print('with no marker',micro.marker)
                            if micro.cs2_err:
                                print('with error',micro.cs2_err)
                                axs[0].errorbar( micro.sm_den[:-1], micro.sm_cs2[:-1], yerr=micro.sm_cs2_err[:-1], marker=micro.marker, linestyle=lstyle, label=mb, errorevery=micro.every, color=nuda.param.col[kmb] )
                            else:
                                print('with no error',micro.cs2_err)
                                axs[0].plot( micro.sm_den[:-1], micro.sm_cs2[:-1], marker=micro.marker, linestyle=lstyle, label=mb, markevery=micro.every, color=nuda.param.col[kmb] )
                # end of matter
            # end of model
        # end of mb
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
            check = nuda.matter.setupCheck( eos = pheno, band = band_check )
            #
            if check.isInside:
                lstyle = 'solid'
            else:
                lstyle = 'dashed'
                #continue
            #
            if matter.lower() == 'nm':
                #
                if pheno.nm_cs2 is not None: 
                    print('model:',model,' param:',param)
                    if model in model_check:
                        axs[1].plot( pheno.nm_den[:-1], pheno.nm_cs2[:-1], linestyle=lstyle, color=nuda.param.col[kmodel] )
                    else:
                        model_check.append(model)
                        axs[1].plot( pheno.nm_den[:-1], pheno.nm_cs2[:-1], linestyle=lstyle, color=nuda.param.col[kmodel], label=model )
                #
            elif matter.lower() == 'sm':
                #
                if pheno.sm_cs2 is not None: 
                    print('model:',model,' param:',param)
                    if model in model_check:
                        axs[1].plot( pheno.sm_den[:-1], pheno.sm_cs2[:-1], linestyle=lstyle, color=nuda.param.col[kmodel] )
                    else:
                        model_check.append(model)
                        axs[1].plot( pheno.sm_den[:-1], pheno.sm_cs2[:-1], linestyle=lstyle, color=nuda.param.col[kmodel], label=model )
            # end of param
        # end of model
    #
    #axs[1].legend(loc='upper left',fontsize='8', ncol=2)
    #axs[0,1].legend(loc='upper left',fontsize='xx-small', ncol=2)
    if matter.lower() == 'nm':
        axs[0].text(0.02,0.3,'microscopic models',fontsize='12')
        axs[1].text(0.02,0.3,'phenomenological models',fontsize='12')
        fig.legend(loc='upper left',bbox_to_anchor=(0.1,1.0),columnspacing=2,fontsize='8',ncol=6,frameon=False)
    elif matter.lower() == 'sm':
        axs[0].text(0.02,0.2,'microscopic models',fontsize='12')
        axs[1].text(0.02,0.2,'phenomenological models',fontsize='12')
        fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=5,frameon=False)
    #
    if pname is not None:
        plt.savefig(pname, dpi=200)
    #
        plt.close()
    #