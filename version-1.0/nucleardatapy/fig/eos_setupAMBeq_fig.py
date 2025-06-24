import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def eos_setupAMBeq_e2a_nuc_fig( pname, micro_mbs, pheno_models, band ):
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
    fig.subplots_adjust(left=0.12, bottom=0.12, right=0.95, top=0.90, wspace=0.05, hspace=0.05 )
    #
    axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    axs[0].set_ylabel(r'$e_\text{nuc}^\text{int}$ (MeV)',fontsize='14')
    axs[0].set_xlim([0, 0.33])
    axs[0].set_ylim([-2, 27])
    #axs[0].set_tick_params('y', right=True)
    #axs[0].set_tick_params('x', top=True)
    #
    axs[1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    axs[1].set_xlim([0, 0.33])
    axs[1].set_ylim([-2, 27])
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
            micro = nuda.eos.setupAMBeq( model = model, kind = 'micro' )
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
            if micro.e2a_nuc is not None: 
                print('model:',model)
                if mb in mb_check:
                    axs[0].plot( micro.den, micro.e2a_int_nuc, marker='o', linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                else:
                    mb_check.append(mb)
                    axs[0].plot( micro.den, micro.e2a_int_nuc, marker='o', linestyle=lstyle, label=mb, markevery=micro.every, color=nuda.param.col[kmb] )
            # end of model
        # end of mb
    #
    axs[0].text(0.02,20,'microscopic models',fontsize='10')
    #
    model_check = []
    #
    for kmodel,model in enumerate(pheno_models):
        #
        params, params_lower = nuda.matter.pheno_esym_params( model = model )
        #
        for param in params:
            #
            pheno = nuda.eos.setupAMBeq( model = model, param = param, kind = 'pheno' )
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
            if pheno.e2a_nuc is not None: 
                print('model:',model,' param:',param)
                if model in model_check:
                    axs[1].plot( pheno.den, pheno.e2a_int_nuc, linestyle=lstyle, markevery=pheno.every, color=nuda.param.col[kmodel] )
                else:
                    model_check.append(model)
                    axs[1].plot( pheno.den, pheno.e2a_int_nuc, linestyle=lstyle, label=model, markevery=pheno.every, color=nuda.param.col[kmodel] )
            # end of param
        # end of model
    #
    axs[1].text(0.02,20,'phenomenological models',fontsize='10')
    #
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=5,frameon=False)
    #
    if pname is not None: 
        plt.savefig(pname, dpi=200)
        plt.close()

def eos_setupAMBeq_pre_nuc_fig( pname, micro_mbs, pheno_models, band ):
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
    fig.subplots_adjust(left=0.12, bottom=0.12, right=0.95, top=0.90, wspace=0.05, hspace=0.05 )
    #
    axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    axs[0].set_ylabel(r'$p_\text{nuc}$ (MeV fm$^{-3}$)',fontsize='14')
    axs[0].set_xlim([0, 0.35])
    axs[0].set_ylim([-2, 60])
    #axs[0].set_tick_params('y', right=True)
    #axs[0].set_tick_params('x', top=True)
    #
    axs[1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    axs[1].set_xlim([0, 0.35])
    axs[1].set_ylim([-2, 60])
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
            micro = nuda.eos.setupAMBeq( model = model, kind = 'micro' )
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
            if micro.pre_nuc is not None: 
                print('model:',model)
                if mb in mb_check:
                    axs[0].plot( micro.den, micro.pre_nuc, marker='o', linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                else:
                    mb_check.append(mb)
                    axs[0].plot( micro.den, micro.pre_nuc, marker='o', linestyle=lstyle, label=mb, markevery=micro.every, color=nuda.param.col[kmb] )
            # end of model
        # end of mb
    axs[0].text(0.02,20,'microscopic models',fontsize='10')
    #
    model_check = []
    #
    for kmodel,model in enumerate(pheno_models):
        #
        params, params_lower = nuda.matter.pheno_esym_params( model = model )
        #
        for param in params:
            #
            pheno = nuda.eos.setupAMBeq( model = model, param = param, kind = 'pheno' )
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
            if pheno.pre_nuc is not None: 
                print('model:',model,' param:',param)
                if model in model_check:
                    axs[1].plot( pheno.den, pheno.pre_nuc, linestyle=lstyle, markevery=pheno.every, color=nuda.param.col[kmodel] )
                else:
                    model_check.append(model)
                    axs[1].plot( pheno.den, pheno.pre_nuc, linestyle=lstyle, label=model, markevery=pheno.every, color=nuda.param.col[kmodel] )
            # end of param
        # end of model
    #
    axs[1].text(0.02,20,'phenomenological models',fontsize='10')
    #
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=5,frameon=False)
    #
    if pname is not None: 
        plt.savefig(pname, dpi=200)
        plt.close()

def eos_setupAMBeq_cs2_nuc_fig( pname, micro_mbs, pheno_models, band ):
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
    fig.subplots_adjust(left=0.12, bottom=0.12, right=0.95, top=0.90, wspace=0.05, hspace=0.05 )
    #
    axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    axs[0].set_ylabel(r'$c_\text{s,nuc}^2/c^2$',fontsize='14')
    axs[0].set_xlim([0, 0.35])
    axs[0].set_ylim([-0.05, 0.25])
    #axs[0].set_tick_params('y', right=True)
    #axs[0].set_tick_params('x', top=True)
    #
    axs[1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    axs[1].set_xlim([0, 0.35])
    axs[1].set_ylim([-0.05, 0.25])
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
            micro = nuda.eos.setupAMBeq( model = model, kind = 'micro' )
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
            if micro.cs2_nuc is not None: 
                print('model:',model)
                if mb in mb_check:
                    axs[0].plot( micro.den, micro.cs2_nuc, marker='o', linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                else:
                    mb_check.append(mb)
                    axs[0].plot( micro.den, micro.cs2_nuc, marker='o', linestyle=lstyle, label=mb, markevery=micro.every, color=nuda.param.col[kmb] )
            # end of model
        # end of mb
    axs[0].text(0.02,0.2,'microscopic models',fontsize='10')
    #
    model_check = []
    #
    for kmodel,model in enumerate(pheno_models):
        #
        params, params_lower = nuda.matter.pheno_esym_params( model = model )
        #
        for param in params:
            #
            pheno = nuda.eos.setupAMBeq( model = model, param = param, kind = 'pheno' )
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
            if pheno.cs2_nuc is not None: 
                print('model:',model,' param:',param)
                if model in model_check:
                    axs[1].plot( pheno.den, pheno.cs2_nuc, linestyle=lstyle, markevery=pheno.every, color=nuda.param.col[kmodel] )
                else:
                    model_check.append(model)
                    axs[1].plot( pheno.den, pheno.cs2_nuc, linestyle=lstyle, label=model, markevery=pheno.every, color=nuda.param.col[kmodel] )
            # end of param
        # end of model
    #
    axs[1].text(0.02,0.2,'phenomenological models',fontsize='10')
    #
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=5,frameon=False)
    #
    if pname is not None: 
        plt.savefig(pname, dpi=200)
        plt.close()

def eos_setupAMBeq_e2a_lep_fig( pname, micro_mbs, pheno_models, band ):
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
    fig.subplots_adjust(left=0.12, bottom=0.12, right=0.95, top=0.90, wspace=0.05, hspace=0.05 )
    #
    axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    axs[0].set_ylabel(r'$_\text{lep}^\text{int}$ (MeV)',fontsize='14')
    axs[0].set_xlim([0, 0.33])
    axs[0].set_ylim([-2, 27])
    #axs[0].set_tick_params('y', right=True)
    #axs[0].set_tick_params('x', top=True)
    #
    axs[1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    axs[1].set_xlim([0, 0.33])
    axs[1].set_ylim([-2, 27])
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
            micro = nuda.eos.setupAMBeq( model = model, kind = 'micro' )
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
            #
            if micro.e2a_lep is not None: 
                print('model:',model)
                if mb in mb_check:
                    axs[0].plot( micro.den, micro.e2a_lep, marker='o', linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                else:
                    mb_check.append(mb)
                    axs[0].plot( micro.den, micro.e2a_lep, marker='o', linestyle=lstyle, label=mb, markevery=micro.every, color=nuda.param.col[kmb] )
            # end of model
        # end of mb
    #
    axs[0].text(0.02,20,'microscopic models',fontsize='10')
    #
    model_check = []
    #
    for kmodel,model in enumerate(pheno_models):
        #
        params, params_lower = nuda.matter.pheno_esym_params( model = model )
        #
        for param in params:
            #
            pheno = nuda.eos.setupAMBeq( model = model, param = param, kind = 'pheno' )
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
                #micro.label=None
                if model in model_check:
                    axs[1].plot( pheno.den, pheno.e2a_lep, linestyle=lstyle, markevery=pheno.every, color=nuda.param.col[kmodel] )
                else:
                    model_check.append(model)
                    axs[1].plot( pheno.den, pheno.e2a_lep, linestyle=lstyle, label=model, markevery=pheno.every, color=nuda.param.col[kmodel] )
            # end of param
        # end of model
    #
    axs[1].text(0.02,20,'phenomenological models',fontsize='10')
    #
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=5,frameon=False)
    #
    if pname is not None: 
        plt.savefig(pname, dpi=200)
        plt.close()

def eos_setupAMBeq_pre_lep_fig( pname, micro_mbs, pheno_models, band ):
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
    fig.subplots_adjust(left=0.12, bottom=0.12, right=0.95, top=0.90, wspace=0.05, hspace=0.05 )
    #
    axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    axs[0].set_ylabel(r'$p_\text{lep}$ (MeV fm$^{-3}$)',fontsize='14')
    axs[0].set_xlim([0, 0.35])
    axs[0].set_ylim([-2, 60])
    #axs[0].set_tick_params('y', right=True)
    #axs[0].set_tick_params('x', top=True)
    #
    axs[1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    axs[1].set_xlim([0, 0.35])
    axs[1].set_ylim([-2, 60])
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
            micro = nuda.eos.setupAMBeq( model = model, kind = 'micro' )
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
            #
            if micro.pre_lep is not None: 
                print('model:',model)
                if mb in mb_check:
                    axs[0].plot( micro.den, micro.pre_lep, marker='o', linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                else:
                    mb_check.append(mb)
                    axs[0].plot( micro.den, micro.pre_lep, marker='o', linestyle=lstyle, label=mb, markevery=micro.every, color=nuda.param.col[kmb] )
            # end of model
        # end of mb
    #
    axs[0].text(0.02,20,'microscopic models',fontsize='10')
    #
    model_check = []
    #
    for kmodel,model in enumerate(pheno_models):
        #
        params, params_lower = nuda.matter.pheno_esym_params( model = model )
        #
        for param in params:
            #
            pheno = nuda.eos.setupAMBeq( model = model, param = param, kind = 'pheno' )
            #
            check = nuda.matter.setupCheck( eos = pheno, band = band )
            #
            if check.isInside:
                lstyle = 'solid'
            else:
                lstyle = 'dashed'
                #continue
            #
            if micro.pre_lep is not None: 
                print('model:',model,' param:',param)
                if model in model_check:
                    axs[1].plot( pheno.den, pheno.pre_lep, linestyle=lstyle, markevery=pheno.every, color=nuda.param.col[kmodel] )
                else:
                    model_check.append(model)
                    axs[1].plot( pheno.den, pheno.pre_lep, linestyle=lstyle, label=model, markevery=pheno.every, color=nuda.param.col[kmodel] )
            if nuda.env.verb_output: pheno.print_outputs( )
            # end of param
        # end of model
    #
    axs[1].text(0.02,20,'phenomenological models',fontsize='10')
    #
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=5,frameon=False)
    #
    if pname is not None: 
        plt.savefig(pname, dpi=200)
        plt.close()

def eos_setupAMBeq_cs2_lep_fig( pname, micro_mbs, pheno_models, band ):
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
    fig.subplots_adjust(left=0.12, bottom=0.12, right=0.95, top=0.90, wspace=0.05, hspace=0.05 )
    #
    axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    axs[0].set_ylabel(r'$c_\text{s,lep}^2/c^2$',fontsize='14')
    axs[0].set_xlim([0, 0.35])
    axs[0].set_ylim([0.2, 0.5])
    #axs[0].set_tick_params('y', right=True)
    #axs[0].set_tick_params('x', top=True)
    #
    axs[1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    axs[1].set_xlim([0, 0.35])
    axs[1].set_ylim([0.2, 0.5])
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
            micro = nuda.eos.setupAMBeq( model = model, kind = 'micro' )
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
            #
            if micro.cs2_lep is not None: 
                print('model:',model)
                if mb in mb_check:
                    axs[0].plot( micro.den, micro.cs2_lep, marker='o', linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                else:
                    mb_check.append(mb)
                    axs[0].plot( micro.den, micro.cs2_lep, marker='o', linestyle=lstyle, label=mb, markevery=micro.every, color=nuda.param.col[kmb] )
            # end of model
        # end of mb
    #
    axs[0].text(0.02,0.45,'microscopic models',fontsize='10')
    #
    model_check = []
    #
    for kmodel,model in enumerate(pheno_models):
        #
        params, params_lower = nuda.matter.pheno_esym_params( model = model )
        #
        for param in params:
            #
            pheno = nuda.eos.setupAMBeq( model = model, param = param, kind = 'pheno' )
            #
            check = nuda.matter.setupCheck( eos = pheno, band = band )
            #
            if check.isInside:
                lstyle = 'solid'
            else:
                lstyle = 'dashed'
                #continue
            #
            if micro.cs2_lep is not None: 
                print('model:',model,' param:',param)
                if model in model_check:
                    axs[1].plot( pheno.den, pheno.cs2_lep, linestyle=lstyle, markevery=pheno.every, color=nuda.param.col[kmodel] )
                else:
                    model_check.append(model)
                    axs[1].plot( pheno.den, pheno.cs2_lep, linestyle=lstyle, label=model, markevery=pheno.every, color=nuda.param.col[kmodel] )
            if nuda.env.verb_output: pheno.print_outputs( )
            # end of param
        # end of model
    #
    axs[1].text(0.02,0.45,'phenomenological models',fontsize='10')
    #
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=5,frameon=False)
    #
    if pname is not None: 
        plt.savefig(pname, dpi=200)
        plt.close()


def eos_setupAMBeq_e2a_tot_fig( pname, micro_mbs, pheno_models, band ):
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
    fig.subplots_adjust(left=0.12, bottom=0.12, right=0.95, top=0.90, wspace=0.05, hspace=0.05 )
    #
    axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    axs[0].set_ylabel(r'$e_\text{tot}^\text{int}$ (MeV)',fontsize='14')
    axs[0].set_xlim([0, 0.33])
    axs[0].set_ylim([-2, 27])
    #axs[0].set_tick_params('y', right=True)
    #axs[0].set_tick_params('x', top=True)
    #
    axs[1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    axs[1].set_xlim([0, 0.33])
    axs[1].set_ylim([-2, 27])
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
            micro = nuda.eos.setupAMBeq( model = model, kind = 'micro' )
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
            if micro.e2a_tot is not None: 
                print('model:',model)
                if mb in mb_check:
                    axs[0].plot( micro.den, micro.e2a_int_tot, marker='o', linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                else:
                    mb_check.append(mb)
                    axs[0].plot( micro.den, micro.e2a_int_tot, marker='o', linestyle=lstyle, label=mb, markevery=micro.every, color=nuda.param.col[kmb] )
            # end of model
        # end of mb
    #
    axs[0].text(0.02,20,'microscopic models',fontsize='10')
    #
    model_check = []
    #
    for kmodel,model in enumerate(pheno_models):
        #
        params, params_lower = nuda.matter.pheno_esym_params( model = model )
        #
        for param in params:
            #
            pheno = nuda.eos.setupAMBeq( model = model, param = param, kind = 'pheno' )
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
            if pheno.e2a_tot is not None: 
                print('model:',model,' param:',param)
                if model in model_check:
                    axs[1].plot( pheno.den, pheno.e2a_int_tot, linestyle=lstyle, markevery=pheno.every, color=nuda.param.col[kmodel] )
                else:
                    model_check.append(model)
                    axs[1].plot( pheno.den, pheno.e2a_int_tot, linestyle=lstyle, label=model, markevery=pheno.every, color=nuda.param.col[kmodel] )
            # end of param
        # end of model
    #
    axs[1].text(0.02,20,'phenomenological models',fontsize='10')
    #
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=5,frameon=False)
    #
    if pname is not None: 
        plt.savefig(pname, dpi=200)
        plt.close()

def eos_setupAMBeq_pre_tot_fig( pname, micro_mbs, pheno_models, band ):
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
    p_den = 0.32
    p_cen = 23.0
    p_std = 14.0
    p_micro_cen = 16.3
    p_micro_std =  3.0
    p_pheno_cen = 23.0
    p_pheno_std = 14.0
    #
    fig, axs = plt.subplots(1,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=0.95, top=0.90, wspace=0.05, hspace=0.05 )
    #
    axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    axs[0].set_ylabel(r'$p_\text{tot}$ (MeV fm$^{-3}$)',fontsize='14')
    axs[0].set_xlim([0, 0.35])
    axs[0].set_ylim([-2, 60])
    #axs[0].set_tick_params('y', right=True)
    #axs[0].set_tick_params('x', top=True)
    #
    axs[1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    axs[1].set_xlim([0, 0.35])
    axs[1].set_ylim([-2, 60])
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
            micro = nuda.eos.setupAMBeq( model = model, kind = 'micro' )
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
            #
            if micro.pre_tot is not None: 
                print('model:',model)
                if mb in mb_check:
                    axs[0].plot( micro.den, micro.pre_tot, marker='o', linestyle=micro.linestyle, markevery=micro.every, color=nuda.param.col[kmb] )
                else:
                    mb_check.append(mb)
                    axs[0].plot( micro.den, micro.pre_tot, marker='o', linestyle=micro.linestyle, label=mb, markevery=micro.every, color=nuda.param.col[kmb] )
            # end of model
        # end of mb
    #
    axs[0].errorbar( p_den, p_cen, yerr=p_std, color='k' )
    axs[0].errorbar( p_den+0.005, p_micro_cen, yerr=p_micro_std, color='r' )
    axs[0].text(0.02,20,'microscopic models',fontsize='10')
    #
    model_check = []
    #
    for kmodel,model in enumerate(pheno_models):
        #
        params, params_lower = nuda.matter.pheno_esym_params( model = model )
        #
        for param in params:
            #
            pheno = nuda.eos.setupAMBeq( model = model, param = param, kind = 'pheno' )
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
            if pheno.pre_tot is not None: 
                print('model:',model,' param:',param)
                if model in model_check:
                    axs[1].plot( pheno.den, pheno.pre_tot, linestyle=lstyle, markevery=pheno.every, color=nuda.param.col[kmodel] )
                else:
                    model_check.append(model)
                    axs[1].plot( pheno.den, pheno.pre_tot, linestyle=lstyle, label=model, markevery=pheno.every, color=nuda.param.col[kmodel] )
            # end of param
        # end of model
    #
    axs[1].errorbar( p_den, p_cen, yerr=p_std, color='k' )
    axs[1].errorbar( p_den+0.005, p_pheno_cen, yerr=p_pheno_std, color='r' )
    axs[1].text(0.02,20,'phenomenological models',fontsize='10')
    #
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=5,frameon=False)
    #
    if pname is not None: 
        plt.savefig(pname, dpi=200)
        plt.close()

def eos_setupAMBeq_cs2_tot_fig( pname, micro_mbs, pheno_models, band ):
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
    fig.subplots_adjust(left=0.12, bottom=0.12, right=0.95, top=0.90, wspace=0.05, hspace=0.05 )
    #
    axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    axs[0].set_ylabel(r'$c_\text{s,tot}^2/c^2$',fontsize='14')
    axs[0].set_xlim([0, 0.35])
    axs[0].set_ylim([-0.05, 0.25])
    #axs[0].set_tick_params('y', right=True)
    #axs[0].set_tick_params('x', top=True)
    #
    axs[1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    axs[1].set_xlim([0, 0.35])
    axs[1].set_ylim([-0.05, 0.25])
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
            micro = nuda.eos.setupAMBeq( model = model, kind = 'micro' )
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
            #
            if micro.cs2_tot is not None: 
                print('model:',model)
                if mb in mb_check:
                    axs[0].plot( micro.den, micro.cs2_tot, marker='o', linestyle=micro.linestyle, markevery=micro.every, color=nuda.param.col[kmb] )
                else:
                    mb_check.append(mb)
                    axs[0].plot( micro.den, micro.cs2_tot, marker='o', linestyle=micro.linestyle, label=mb, markevery=micro.every, color=nuda.param.col[kmb] )
            # end of model
        # end of mb
    axs[0].text(0.02,0.2,'microscopic models',fontsize='10')
    #
    model_check = []
    #
    for kmodel,model in enumerate(pheno_models):
        #
        params, params_lower = nuda.matter.pheno_esym_params( model = model )
        #
        for param in params:
            #
            pheno = nuda.eos.setupAMBeq( model = model, param = param, kind = 'pheno' )
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
            if pheno.cs2_tot is not None: 
                print('model:',model,' param:',param)
                if model in model_check:
                    axs[1].plot( pheno.den, pheno.cs2_tot, linestyle=lstyle, markevery=pheno.every, color=nuda.param.col[kmodel] )
                else:
                    model_check.append(model)
                    axs[1].plot( pheno.den, pheno.cs2_tot, linestyle=lstyle, label=model, markevery=pheno.every, color=nuda.param.col[kmodel] )
            # end of param
        # end of model
    axs[1].text(0.02,0.2,'phenomenological models',fontsize='10')
    #
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=5,frameon=False)
    #
    if pname is not None: 
        plt.savefig(pname, dpi=200)
        plt.close()

def eos_setupAMBeq_eos_fig( pname, micro_mbs, pheno_models, band ):
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
    p_den = 312.0
    p_cen = 12.5
    p_std = 11.0
    p_micro_cen = 14.0
    p_micro_std =  2.5
    p_pheno_cen = 12.5
    p_pheno_std = 11.0
    #
    fig, axs = plt.subplots(1,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=0.95, top=0.90, wspace=0.05, hspace=0.05 )
    #
    axs[0].set_xlabel(r'$\epsilon_\text{tot}$ (MeV fm$^{-3}$)',fontsize='14')
    axs[0].set_ylabel(r'$p_\text{tot}$ (MeV fm$^{-3}$)',fontsize='14')
    axs[0].set_xlim([0, 350])
    axs[0].set_ylim([-2, 30])
    #axs[0].set_tick_params('y', right=True)
    #axs[0].set_tick_params('x', top=True)
    #
    axs[1].set_xlabel(r'$\epsilon_\text{tot}$ (MeV fm$^{-3}$)',fontsize='14')
    axs[1].set_xlim([0, 350])
    axs[1].set_ylim([-2, 30])
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
            micro = nuda.eos.setupAMBeq( model = model, kind = 'micro' )
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
            #
            if micro.pre_tot is not None: 
                print('model:',model)
                if mb in mb_check:
                    axs[0].plot( micro.eps_tot, micro.pre_tot, marker='o', linestyle=micro.linestyle, markevery=micro.every, color=nuda.param.col[kmb] )
                else:
                    mb_check.append(mb)
                    axs[0].plot( micro.eps_tot, micro.pre_tot, marker='o', linestyle=micro.linestyle, label=mb, markevery=micro.every, color=nuda.param.col[kmb] )
            # end of model
        # end of mb
    #
    axs[0].errorbar( p_den, p_cen, yerr=p_std, color='k', linewidth = 3 )
    axs[0].errorbar( p_den+5.0, p_micro_cen, yerr=p_micro_std, color='r', linewidth = 3 )
    axs[0].text(10,20,'microscopic models',fontsize='10')
    #
    model_check = []
    #
    for kmodel,model in enumerate(pheno_models):
        #
        params, params_lower = nuda.matter.pheno_esym_params( model = model )
        #
        for param in params:
            #
            pheno = nuda.eos.setupAMBeq( model = model, param = param, kind = 'pheno' )
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
            if pheno.pre_tot is not None: 
                print('model:',model,' param:',param)
                if model in model_check:
                    axs[1].plot( pheno.eps_tot, pheno.pre_tot, linestyle=lstyle, markevery=pheno.every, color=nuda.param.col[kmodel] )
                else:
                    model_check.append(model)
                    axs[1].plot( pheno.eps_tot, pheno.pre_tot, linestyle=lstyle, label=model, markevery=pheno.every, color=nuda.param.col[kmodel] )
            # end of param
        # end of model
    #
    axs[1].errorbar( p_den, p_cen, yerr=p_std, color='k', linewidth = 3 )
    axs[1].errorbar( p_den+5.0, p_pheno_cen, yerr=p_pheno_std, color='r', linewidth = 3 )
    axs[1].text(10,20,'phenomenological models',fontsize='10')
    #
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=5,frameon=False)
    #
    if pname is not None: 
        plt.savefig(pname, dpi=200)
        plt.close()

def eos_setupAMBeq_xp_fig( pname, micro_mbs, pheno_models, band ):
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
    fig.subplots_adjust(left=0.12, bottom=0.12, right=0.95, top=0.90, wspace=0.05, hspace=0.3 )
    #
    axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    axs[0].set_ylabel(r'proton fraction $x_p$',fontsize='14')
    axs[0].set_xlim([0, 0.33])
    axs[0].set_ylim([0, 0.2])
    #axs[0].set_tick_params('y', right=True)
    #axs[0].set_tick_params('x', top=True)
    #
    axs[1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    #axs[1].set_ylabel(r'proton fraction $x_p$')
    axs[1].set_xlim([0, 0.33])
    axs[1].set_ylim([0, 0.2])
    #setp(axs[1].get_yticklabels(), visible=False)
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
            micro = nuda.eos.setupAMBeq( model = model, kind = 'micro' )
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
            if micro.x_p is not None:
                print('model:',model)
                if mb in mb_check:
                    axs[0].plot( micro.den, micro.x_p, marker='o', linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                else:
                    mb_check.append(mb)
                    axs[0].plot( micro.den, micro.x_p, marker='o', linestyle=lstyle, label=mb, markevery=micro.every, color=nuda.param.col[kmb] )
            # end of model
        # end of mb
    #
    axs[0].text(0.02,0.18,'microscopic models',fontsize='10')
    #
    model_check = []
    #
    for kmodel,model in enumerate(pheno_models):
        #
        params, params_lower = nuda.matter.pheno_esym_params( model = model )
        #
        for param in params:
            #
            pheno = nuda.eos.setupAMBeq( model = model, param = param, kind = 'pheno' )
            #
            check = nuda.matter.setupCheck( eos = pheno, band = band )
            #
            if check.isInside:
                lstyle = 'solid'
            else:
                lstyle = 'dashed'
                #continue
            #
            if pheno.x_p is not None:
                print('model:',model,' param:',param)
                if model in model_check:
                    axs[1].plot( pheno.den, pheno.x_p, linestyle=lstyle, markevery=pheno.every, color=nuda.param.col[kmodel] )
                else:
                    model_check.append(model)
                    axs[1].plot( pheno.den, pheno.x_p, linestyle=lstyle, label=model, markevery=pheno.every, color=nuda.param.col[kmodel] )
            if nuda.env.verb_output: pheno.print_outputs( )
            # end of param
        # end of model
    #
    axs[1].text(0.02,0.18,'phenomenological models',fontsize='10')
    #
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=5,frameon=False)
    #
    if pname is not None: 
    	plt.savefig(pname, dpi=200)
    	plt.close()

def eos_setupAMBeq_xe_fig( pname, micro_mbs, pheno_models, band ):
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
    fig.subplots_adjust(left=0.12, bottom=0.12, right=0.95, top=0.90, wspace=0.05, hspace=0.3 )
    #
    axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    axs[0].set_ylabel(r'electron fraction $x_e$',fontsize='14')
    axs[0].set_xlim([0, 0.33])
    axs[0].set_ylim([0, 0.2])
    #
    axs[1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    #axs[1].set_ylabel(r'electron fraction $x_e$')
    axs[1].set_xlim([0, 0.33])
    axs[1].set_ylim([0, 0.2])
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
            micro = nuda.eos.setupAMBeq( model = model, kind = 'micro' )
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
            #
            if micro.x_el is not None: 
                print('model:',model)
                if mb in mb_check:
                    axs[0].plot( micro.den, micro.x_el, marker='o', linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                else:
                    mb_check.append(mb)
                    axs[0].plot( micro.den, micro.x_el, marker='o', linestyle=lstyle, label=mb, markevery=micro.every, color=nuda.param.col[kmb] )
            # end of model
        # end of mb
    #
    axs[0].text(0.02,0.18,'microscopic models',fontsize='10')
    #
    model_check = []
    #
    for kmodel,model in enumerate(pheno_models):
        #
        params, params_lower = nuda.matter.pheno_esym_params( model = model )
        #
        for param in params:
            #
            pheno = nuda.eos.setupAMBeq( model = model, param = param, kind = 'pheno' )
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
            if pheno.x_el is not None: 
                print('model:',model,' param:',param)
                #micro.label=None
                if model in model_check:
                    axs[1].plot( pheno.den, pheno.x_el, linestyle=lstyle, markevery=pheno.every, color=nuda.param.col[kmodel] )
                else:
                    model_check.append(model)
                    axs[1].plot( pheno.den, pheno.x_el, linestyle=lstyle, label=model, markevery=pheno.every, color=nuda.param.col[kmodel] )
            # end of param
        # end of model
    #
    axs[1].text(0.02,0.18,'phenomenological models',fontsize='10')
    #
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=5,frameon=False)
    #
    if pname is not None: 
    	plt.savefig(pname, dpi=200)
    	plt.close()

def eos_setupAMBeq_xmu_fig( pname, micro_mbs, pheno_models, band ):
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
    fig.subplots_adjust(left=0.12, bottom=0.12, right=0.95, top=0.90, wspace=0.05, hspace=0.3 )
    #
    axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    axs[0].set_ylabel(r'muon fraction $x_\mu$',fontsize='14')
    axs[0].set_xlim([0, 0.33])
    axs[0].set_ylim([0, 0.2])
    #
    axs[1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    #axs[1].set_ylabel(r'muon fraction $x_\mu$')
    axs[1].set_xlim([0, 0.33])
    axs[1].set_ylim([0, 0.2])
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
            micro = nuda.eos.setupAMBeq( model = model, kind = 'micro' )
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
            if micro.x_mu is not None: 
                print('model:',model)
                if mb in mb_check:
                    axs[0].plot( micro.den, micro.x_mu, marker='o', linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                else:
                    mb_check.append(mb)
                    axs[0].plot( micro.den, micro.x_mu, marker='o', linestyle=lstyle, label=mb, markevery=micro.every, color=nuda.param.col[kmb] )
            # end of model
        # end of mb
    #
    axs[0].text(0.02,0.18,'microscopic models',fontsize='10')
    #
    model_check = []
    #
    for kmodel,model in enumerate(pheno_models):
        #
        params, params_lower = nuda.matter.pheno_esym_params( model = model )
        #
        for param in params:
            #
            pheno = nuda.eos.setupAMBeq( model = model, param = param, kind = 'pheno' )
            #
            check = nuda.matter.setupCheck( eos = pheno, band = band )
            #
            if check.isInside:
                lstyle = 'solid'
            else:
                lstyle = 'dashed'
                #continue
            #
            if pheno.x_mu is not None: 
                print('model:',model,' param:',param)
                if model in model_check:
                    axs[1].plot( pheno.den, pheno.x_mu, linestyle=lstyle, markevery=pheno.every, color=nuda.param.col[kmodel] )
                else:
                    model_check.append(model)
                    axs[1].plot( pheno.den, pheno.x_mu, linestyle=lstyle, label=model, markevery=pheno.every, color=nuda.param.col[kmodel] )
            if nuda.env.verb_output: pheno.print_outputs( )
            # end of param
        # end of model
    #
    axs[1].text(0.02,0.18,'phenomenological models',fontsize='10')
    #
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=5,frameon=False)
    #
    if pname is not None: 
    	plt.savefig(pname, dpi=200)
    	plt.close()
    #