import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def eos_setupAM_e2a_asy_lep_fig( pname, micro_mbs, pheno_models, asy, band ):
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
    fig.subplots_adjust(left=0.10, bottom=0.12, right=0.95, top=0.90, wspace=0.05, hspace=0.3 )
    #
    axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    axs[0].set_ylabel(r'$e_\text{lep}^\text{int}$ (MeV)',fontsize='14')
    axs[0].set_xlim([0, 0.33])
    axs[0].set_ylim([-10, 35])
    #
    axs[1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    #axs[1].set_ylabel(r'$E/A$')
    axs[1].set_xlim([0, 0.33])
    axs[1].set_ylim([-10, 35])
    axs[1].tick_params('y', labelleft=False)
    #
    mb_check = []
    #
    for kmb,mb in enumerate(micro_mbs):
        #
        print('mb:',mb,kmb)
        #
        models, models_lower = nuda.matter.micro_esym_models_mb( mb )
        #
        print('models:',models)
        #
        if mb == 'VAR':
            models.remove('1998-VAR-AM-APR-fit')
            models_lower.remove('1998-var-am-apr-fit')
        #
        for model in models:
            #
            micro = nuda.eos.setupAM( model = model, kind = 'micro', asy = asy )
            if nuda.env.verb_output: micro.print_outputs( )
            #
            check = nuda.matter.setupCheck( eos = micro, band = band )
            #
            if check.isInside:
                lstyle = 'solid'
            else:
                lstyle = 'dashed'
                #continue
            #
            if micro.e2a_lep is not None: 
                print('model:',model)
                print('den:',micro.den)
                print('e2a_lep:',micro.e2a_lep)
                if mb in mb_check:
                    axs[0].plot( micro.den, micro.e2a_lep, marker='o', linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                else:
                    mb_check.append(mb)
                    axs[0].plot( micro.den, micro.e2a_lep, marker='o', linestyle=lstyle, label=mb, markevery=micro.every, color=nuda.param.col[kmb] )
            # end of model
        # end of mb
    axs[0].text(0.02,-8,'microscopic models',fontsize='10')
    axs[0].text(0.02,-9.5,r'for $\delta=$'+str(asy),fontsize='10')
    #
    model_check = []
    #
    for kmodel,model in enumerate(pheno_models):
        #
        params, params_lower = nuda.matter.pheno_esym_params( model = model )
        #
        for param in params:
            #
            pheno = nuda.eos.setupAM( model = model, param = param, kind = 'pheno', asy = asy )
            if nuda.env.verb_output: pheno.print_outputs( )
            #
            check = nuda.matter.setupCheck( eos = pheno, band = band )
            #
            if check.isInside:
                lstyle = 'solid'
            else:
                lstyle = 'dashed'
                #continue
            #
            if pheno.e2a_lep is not None: 
                print('model:',model,' param:',param)
                if model in model_check:
                    axs[1].plot( pheno.den, pheno.e2a_lep, linestyle=lstyle, markevery=pheno.every, color=nuda.param.col[kmodel] )
                else:
                    model_check.append(model)
                    axs[1].plot( pheno.den, pheno.e2a_lep, linestyle=lstyle, label=model, markevery=pheno.every, color=nuda.param.col[kmodel] )
            # end of param
        # end of model
    #
    #axs[1].fill_between( band.den, y1=(band.e2a-band.e2a_std), y2=(band.e2a+band.e2a_std), color=band.color, alpha=band.alpha, visible=True )
    #axs[1].plot( band.den, (band.e2a-band.e2a_std), color='k', linestyle='dashed' )
    #axs[1].plot( band.den, (band.e2a+band.e2a_std), color='k', linestyle='dashed' )
    axs[1].text(0.02,-8,'phenomenological models',fontsize='10')
    axs[1].text(0.02,-9.5,r'for $\delta=$'+str(asy),fontsize='10')
    #
    #axs[1].legend(loc='upper left',fontsize='8', ncol=2)
    #axs[0,1].legend(loc='upper left',fontsize='xx-small', ncol=2)
    #axs[1].legend(loc='lower center',bbox_to_anchor=(0.5,1.02),mode='expand',columnspacing=0,fontsize='8', ncol=2,frameon=False)
    #fig.legend(loc='lower center',bbox_to_anchor=(0.5,1.02),mode='expand',columnspacing=0,fontsize='8', ncol=2,frameon=False)
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=5,frameon=False)
    #
    if pname is not None: 
        plt.savefig(pname, dpi=200)
        plt.close()
    #

def eos_setupAM_pre_asy_lep_fig( pname, micro_mbs, pheno_models, asy, band ):
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
    fig.subplots_adjust(left=0.10, bottom=0.12, right=0.95, top=0.90, wspace=0.05, hspace=0.3 )
    #
    axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    axs[0].set_ylabel(r'$p_\text{lep}$ (MeV fm$^{-3}$)',fontsize='14')
    axs[0].set_xlim([0, 0.33])
    axs[0].set_ylim([-10, 35])
    #
    axs[1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    #axs[1].set_ylabel(r'$E/A$')
    axs[1].set_xlim([0, 0.33])
    axs[1].set_ylim([-10, 35])
    axs[1].tick_params('y', labelleft=False)
    #
    mb_check = []
    #
    for kmb,mb in enumerate(micro_mbs):
        #
        print('mb:',mb,kmb)
        #
        models, models_lower = nuda.matter.micro_esym_models_mb( mb )
        #
        print('models:',models)
        #
        if mb == 'VAR':
            models.remove('1998-VAR-AM-APR-fit')
            models_lower.remove('1998-var-am-apr-fit')
        #
        for model in models:
            #
            micro = nuda.eos.setupAM( model = model, kind = 'micro', asy = asy )
            if nuda.env.verb_output: micro.print_outputs( )
            #
            check = nuda.matter.setupCheck( eos = micro, band = band )
            #
            if check.isInside:
                lstyle = 'solid'
            else:
                lstyle = 'dashed'
                #continue
            #
            if micro.pre_lep is not None: 
                print('model:',model)
                print('den:',micro.den)
                print('e2a_lep:',micro.e2a_lep)
                if mb in mb_check:
                    axs[0].plot( micro.den, micro.pre_lep, marker='o', linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                else:
                    mb_check.append(mb)
                    axs[0].plot( micro.den, micro.pre_lep, marker='o', linestyle=lstyle, label=mb, markevery=micro.every, color=nuda.param.col[kmb] )
            # end of model
        # end of mb
    axs[0].text(0.02,-8,'microscopic models',fontsize='10')
    axs[0].text(0.02,-9.5,r'for $\delta=$'+str(asy),fontsize='10')
    #
    model_check = []
    #
    for kmodel,model in enumerate(pheno_models):
        #
        params, params_lower = nuda.matter.pheno_esym_params( model = model )
        #
        for param in params:
            #
            pheno = nuda.eos.setupAM( model = model, param = param, kind = 'pheno', asy = asy )
            if nuda.env.verb_output: pheno.print_outputs( )
            #
            check = nuda.matter.setupCheck( eos = pheno, band = band )
            #
            if check.isInside:
                lstyle = 'solid'
            else:
                lstyle = 'dashed'
                #continue
            #
            if pheno.pre_lep is not None: 
                print('model:',model,' param:',param)
                if model in model_check:
                    axs[1].plot( pheno.den, pheno.pre_lep, linestyle=lstyle, markevery=pheno.every, color=nuda.param.col[kmodel] )
                else:
                    model_check.append(model)
                    axs[1].plot( pheno.den, pheno.pre_lep, linestyle=lstyle, label=model, markevery=pheno.every, color=nuda.param.col[kmodel] )
            # end of param
        # end of model
    #
    #axs[1].fill_between( band.den, y1=(band.e2a-band.e2a_std), y2=(band.e2a+band.e2a_std), color=band.color, alpha=band.alpha, visible=True )
    #axs[1].plot( band.den, (band.e2a-band.e2a_std), color='k', linestyle='dashed' )
    #axs[1].plot( band.den, (band.e2a+band.e2a_std), color='k', linestyle='dashed' )
    axs[1].text(0.02,-8,'phenomenological models',fontsize='10')
    axs[1].text(0.02,-9.5,r'for $\delta=$'+str(asy),fontsize='10')
    #
    #axs[1].legend(loc='upper left',fontsize='8', ncol=2)
    #axs[0,1].legend(loc='upper left',fontsize='xx-small', ncol=2)
    #axs[1].legend(loc='lower center',bbox_to_anchor=(0.5,1.02),mode='expand',columnspacing=0,fontsize='8', ncol=2,frameon=False)
    #fig.legend(loc='lower center',bbox_to_anchor=(0.5,1.02),mode='expand',columnspacing=0,fontsize='8', ncol=2,frameon=False)
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=5,frameon=False)
    #
    if pname is not None: 
        plt.savefig(pname, dpi=200)
        plt.close()
    #

def eos_setupAM_cs2_asy_lep_fig( pname, micro_mbs, pheno_models, asy, band ):
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
    fig.subplots_adjust(left=0.10, bottom=0.12, right=0.95, top=0.90, wspace=0.05, hspace=0.3 )
    #
    axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    axs[0].set_ylabel(r'$c_\text{s,lep}^2/c^2$',fontsize='14')
    axs[0].set_xlim([0, 0.33])
    axs[0].set_ylim([0.2, 0.4])
    #
    axs[1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    #axs[1].set_ylabel(r'$E/A$')
    axs[1].set_xlim([0, 0.33])
    axs[1].set_ylim([0.2, 0.4])
    axs[1].tick_params('y', labelleft=False)
    #
    mb_check = []
    #
    for kmb,mb in enumerate(micro_mbs):
        #
        print('mb:',mb,kmb)
        #
        models, models_lower = nuda.matter.micro_esym_models_mb( mb )
        #
        print('models:',models)
        #
        if mb == 'VAR':
            models.remove('1998-VAR-AM-APR-fit')
            models_lower.remove('1998-var-am-apr-fit')
        #
        for model in models:
            #
            micro = nuda.eos.setupAM( model = model, kind = 'micro', asy = asy )
            if nuda.env.verb_output: micro.print_outputs( )
            #
            check = nuda.matter.setupCheck( eos = micro, band = band )
            #
            if check.isInside:
                lstyle = 'solid'
            else:
                lstyle = 'dashed'
                #continue
            #
            if micro.cs2_lep is not None: 
                if mb in mb_check:
                    axs[0].plot( micro.den, micro.cs2_lep, marker='o', linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                else:
                    mb_check.append(mb)
                    axs[0].plot( micro.den, micro.cs2_lep, marker='o', linestyle=lstyle, label=mb, markevery=micro.every, color=nuda.param.col[kmb] )
            # end of model
        # end of mb
    axs[0].text(0.02,-8,'microscopic models',fontsize='10')
    axs[0].text(0.02,-9.5,r'for $\delta=$'+str(asy),fontsize='10')
    #
    model_check = []
    #
    for kmodel,model in enumerate(pheno_models):
        #
        params, params_lower = nuda.matter.pheno_esym_params( model = model )
        #
        for param in params:
            #
            pheno = nuda.eos.setupAM( model = model, param = param, kind = 'pheno', asy = asy )
            if nuda.env.verb_output: pheno.print_outputs( )
            #
            check = nuda.matter.setupCheck( eos = pheno, band = band )
            #
            if check.isInside:
                lstyle = 'solid'
            else:
                lstyle = 'dashed'
                #continue
            #
            if pheno.cs2_lep is not None: 
                print('model:',model,' param:',param)
                if model in model_check:
                    axs[1].plot( pheno.den, pheno.cs2_lep, linestyle=lstyle, markevery=pheno.every, color=nuda.param.col[kmodel] )
                else:
                    model_check.append(model)
                    axs[1].plot( pheno.den, pheno.cs2_lep, linestyle=lstyle, label=model, markevery=pheno.every, color=nuda.param.col[kmodel] )
            # end of param
        # end of model
    #
    #axs[1].fill_between( band.den, y1=(band.e2a-band.e2a_std), y2=(band.e2a+band.e2a_std), color=band.color, alpha=band.alpha, visible=True )
    #axs[1].plot( band.den, (band.e2a-band.e2a_std), color='k', linestyle='dashed' )
    #axs[1].plot( band.den, (band.e2a+band.e2a_std), color='k', linestyle='dashed' )
    axs[1].text(0.02,-8,'phenomenological models',fontsize='10')
    axs[1].text(0.02,-9.5,r'for $\delta=$'+str(asy),fontsize='10')
    #
    #axs[1].legend(loc='upper left',fontsize='8', ncol=2)
    #axs[0,1].legend(loc='upper left',fontsize='xx-small', ncol=2)
    #axs[1].legend(loc='lower center',bbox_to_anchor=(0.5,1.02),mode='expand',columnspacing=0,fontsize='8', ncol=2,frameon=False)
    #fig.legend(loc='lower center',bbox_to_anchor=(0.5,1.02),mode='expand',columnspacing=0,fontsize='8', ncol=2,frameon=False)
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=5,frameon=False)
    #
    if pname is not None: 
        plt.savefig(pname, dpi=200)
        plt.close()
    #