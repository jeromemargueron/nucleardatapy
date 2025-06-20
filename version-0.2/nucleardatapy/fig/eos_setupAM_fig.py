import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def eos_setupAM_e2a_fig( pname, micro_mbs, pheno_models, band ):
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
    fig.subplots_adjust(left=0.10, bottom=0.12, right=0.95, top=0.9, wspace=0.05, hspace=0.05 )
    #
    #axs[0,0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    axs[0,0].set_ylabel(r'$e_\text{lep}^\text{int}$ (MeV)',fontsize='14')
    axs[0,0].set_xlim([0, 0.33])
    axs[0,0].set_ylim([-2, 38])
    axs[0,0].tick_params('x', labelbottom=False)
    #
    #axs[0,1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    axs[0,1].set_xlim([0, 0.33])
    axs[0,1].set_ylim([-2, 38])
    axs[0,1].tick_params('y', labelleft=False)
    axs[0,1].tick_params('x', labelbottom=False)
    #
    #axs[1,0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    axs[1,0].set_ylabel(r'$e_\text{nuc}^\text{int}$ (MeV)',fontsize='14')
    axs[1,0].set_xlim([0, 0.33])
    axs[1,0].set_ylim([-10, 30])
    axs[1,0].tick_params('x', labelbottom=False)
    #
    #axs[1,1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    axs[1,1].set_xlim([0, 0.33])
    axs[1,1].set_ylim([-10, 30])
    axs[1,1].tick_params('y', labelleft=False)
    axs[1,1].tick_params('x', labelbottom=False)
    #
    axs[2,0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    axs[2,0].set_ylabel(r'$e_\text{tot}^\text{int}$ (MeV)',fontsize='14')
    axs[2,0].set_xlim([0, 0.33])
    axs[2,0].set_ylim([-2, 38])
    #
    axs[2,1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    axs[2,1].set_xlim([0, 0.33])
    axs[2,1].set_ylim([-2, 38])
    axs[2,1].tick_params('y', labelleft=False)
    #
    # fix the asymmetry parameters
    #
    asys = [ 0.6, 0.8 ]
    #
    mb_check = []
    model_check = []
    #
    for asy in asys:
        #
        print('asy:',asy)
        #
        for kmb,mb in enumerate(micro_mbs):
            #
            print('mb:',mb,kmb)
            #
            models, models_lower = nuda.matter.micro_esym_models_mb( mb )
            #models, models_lower = nuda.matter.micro_models_mb( mb )
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
                    continue
                #
                if micro.e2a_lep is not None: 
                    if mb in mb_check:
                        print('model:',model)
                        print('den:',micro.den)
                        print('e2a_lep:',micro.e2a_lep)
                        axs[0,0].plot( micro.den, micro.e2a_lep, marker='o', linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                        axs[1,0].plot( micro.den, micro.e2a_int_nuc, marker='o', linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                        axs[2,0].plot( micro.den, micro.e2a_int_tot, marker='o', linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                    else:
                        mb_check.append(mb)
                        print('mb:',mb)
                        print('model:',model)
                        print('den:',micro.den)
                        print('e2a_lep:',micro.e2a_lep)
                        axs[0,0].plot( micro.den, micro.e2a_lep, marker='o', linestyle=lstyle, label=mb, markevery=micro.every, color=nuda.param.col[kmb] )
                        axs[1,0].plot( micro.den, micro.e2a_int_nuc, marker='o', linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                        axs[2,0].plot( micro.den, micro.e2a_int_tot, marker='o', linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                # end of model
            # end of mb
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
                    continue
                #
                if pheno.e2a_lep is not None: 
                    print('model:',model,' param:',param)
                    if model in model_check:
                        axs[0,1].plot( pheno.den, pheno.e2a_lep, linestyle=lstyle, markevery=pheno.every, color=nuda.param.col[kmodel] )
                        axs[1,1].plot( pheno.den, pheno.e2a_int_nuc, linestyle=lstyle, markevery=pheno.every, color=nuda.param.col[kmodel] )
                        axs[2,1].plot( pheno.den, pheno.e2a_int_tot, linestyle=lstyle, markevery=pheno.every, color=nuda.param.col[kmodel] )
                    else:
                        model_check.append(model)
                        axs[0,1].plot( pheno.den, pheno.e2a_lep, linestyle=lstyle, label=model, markevery=pheno.every, color=nuda.param.col[kmodel] )
                        axs[1,1].plot( pheno.den, pheno.e2a_int_nuc, linestyle=lstyle, markevery=pheno.every, color=nuda.param.col[kmodel] )
                        axs[2,1].plot( pheno.den, pheno.e2a_int_tot, linestyle=lstyle, markevery=pheno.every, color=nuda.param.col[kmodel] )
                # end of param
            # end of model
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
    fig.legend(loc='upper left',bbox_to_anchor=(0.1,1.0),columnspacing=2,fontsize='8',ncol=6,frameon=False)
    #
    if pname is not None: 
        plt.savefig(pname, dpi=200)
        plt.close()
    #

def eos_setupAM_pre_fig( pname, micro_mbs, pheno_models, band ):
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
    fig.subplots_adjust(left=0.10, bottom=0.12, right=0.95, top=0.9, wspace=0.05, hspace=0.05 )
    #
    #axs[0,0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    axs[0,0].set_ylabel(r'$p_\text{lep}$ (MeV fm$^{-3}$)',fontsize='14')
    axs[0,0].set_xlim([0, 0.33])
    axs[0,0].set_ylim([-1, 4])
    axs[0,0].tick_params('x', labelbottom=False)
    #
    #axs[0,1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    axs[0,1].set_xlim([0, 0.33])
    axs[0,1].set_ylim([-1, 4])
    axs[0,1].tick_params('y', labelleft=False)
    axs[0,1].tick_params('x', labelbottom=False)
    #
    #axs[1,0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    axs[1,0].set_ylabel(r'$p_\text{nuc}$ (MeV fm$^{-3}$)',fontsize='14')
    axs[1,0].set_xlim([0, 0.33])
    axs[1,0].set_ylim([-2, 15])
    axs[1,0].tick_params('x', labelbottom=False)
    #
    #axs[1,1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    axs[1,1].set_xlim([0, 0.33])
    axs[1,1].set_ylim([-2, 15])
    axs[1,1].tick_params('y', labelleft=False)
    axs[1,1].tick_params('x', labelbottom=False)
    #
    axs[2,0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    axs[2,0].set_ylabel(r'$p_\text{tot}$ (MeV fm$^{-3}$)',fontsize='14')
    axs[2,0].set_xlim([0, 0.33])
    axs[2,0].set_ylim([-2, 15])
    #
    axs[2,1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    axs[2,1].set_xlim([0, 0.33])
    axs[2,1].set_ylim([-2, 15])
    axs[2,1].tick_params('y', labelleft=False)
    #
    # fix the asymmetry parameters
    #
    asys = [ 0.6, 0.8 ]
    #
    mb_check = []
    model_check = []
    #
    for asy in asys:
        #
        print('asy:',asy)
        #
        for kmb,mb in enumerate(micro_mbs):
            #
            print('mb:',mb,kmb)
            #
            models, models_lower = nuda.matter.micro_esym_models_mb( mb )
            #models, models_lower = nuda.matter.micro_models_mb( mb )
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
                    continue
                #
                if micro.pre_lep is not None: 
                    if mb in mb_check:
                        print('model:',model)
                        print('den:',micro.den)
                        print('pre_lep:',micro.pre_lep)
                        axs[0,0].plot( micro.den, micro.pre_lep, marker='o', linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                        axs[1,0].plot( micro.den, micro.pre_nuc, marker='o', linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                        axs[2,0].plot( micro.den, micro.pre_tot, marker='o', linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                    else:
                        mb_check.append(mb)
                        print('mb:',mb)
                        print('model:',model)
                        print('den:',micro.den)
                        print('e2a_lep:',micro.e2a_lep)
                        axs[0,0].plot( micro.den, micro.pre_lep, marker='o', linestyle=lstyle, label=mb, markevery=micro.every, color=nuda.param.col[kmb] )
                        axs[1,0].plot( micro.den, micro.pre_nuc, marker='o', linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                        axs[2,0].plot( micro.den, micro.pre_tot, marker='o', linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                # end of model
            # end of mb
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
                    continue
                #
                if pheno.pre_lep is not None: 
                    print('model:',model,' param:',param)
                    if model in model_check:
                        axs[0,1].plot( pheno.den, pheno.pre_lep, linestyle=lstyle, markevery=pheno.every, color=nuda.param.col[kmodel] )
                        axs[1,1].plot( pheno.den, pheno.pre_nuc, linestyle=lstyle, markevery=pheno.every, color=nuda.param.col[kmodel] )
                        axs[2,1].plot( pheno.den, pheno.pre_tot, linestyle=lstyle, markevery=pheno.every, color=nuda.param.col[kmodel] )
                    else:
                        model_check.append(model)
                        axs[0,1].plot( pheno.den, pheno.pre_lep, linestyle=lstyle, label=model, markevery=pheno.every, color=nuda.param.col[kmodel] )
                        axs[1,1].plot( pheno.den, pheno.pre_nuc, linestyle=lstyle, markevery=pheno.every, color=nuda.param.col[kmodel] )
                        axs[2,1].plot( pheno.den, pheno.pre_tot, linestyle=lstyle, markevery=pheno.every, color=nuda.param.col[kmodel] )
                # end of param
            # end of model
    #
    axs[0,0].text(0.02,3.5,'microscopic models',fontsize='10')
    axs[0,1].text(0.02,3.5,'phenomenological models',fontsize='10')
    #
    axs[0,0].text(0.1,2,r'$\delta=0.6$',fontsize='10')
    axs[0,1].text(0.1,2,r'$\delta=0.6$',fontsize='10')
    axs[0,0].text(0.1,-0.5,r'$\delta=0.8$',fontsize='10')
    axs[0,1].text(0.1,-0.5,r'$\delta=0.8$',fontsize='10')
    #
    axs[1,0].text(0.1,-1.5,r'$\delta=0.6$',fontsize='10')
    axs[1,1].text(0.1,-1.5,r'$\delta=0.6$',fontsize='10')
    axs[1,0].text(0.1,3,r'$\delta=0.8$',fontsize='10')
    axs[1,1].text(0.1,3,r'$\delta=0.8$',fontsize='10')
    #
    axs[2,0].text(0.1,3,r'$\delta=0.6$',fontsize='10')
    axs[2,1].text(0.1,3,r'$\delta=0.6$',fontsize='10')
    axs[2,0].text(0.1,-1,r'$\delta=0.8$',fontsize='10')
    axs[2,1].text(0.1,-1,r'$\delta=0.8$',fontsize='10')
    #
    fig.legend(loc='upper left',bbox_to_anchor=(0.1,1.0),columnspacing=2,fontsize='8',ncol=6,frameon=False)
    #
    if pname is not None: 
        plt.savefig(pname, dpi=200)
        plt.close()
    #

def eos_setupAM_cs2_fig( pname, micro_mbs, pheno_models, band ):
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
    fig.subplots_adjust(left=0.10, bottom=0.12, right=0.95, top=0.9, wspace=0.05, hspace=0.05 )
    #
    #axs[0,0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    axs[0,0].set_ylabel(r'$c_\text{s,lep}^2/c^2$',fontsize='14')
    axs[0,0].set_xlim([0, 0.33])
    axs[0,0].set_ylim([0.2, 0.5])
    axs[0,0].tick_params('x', labelbottom=False)
    #
    #axs[0,1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    axs[0,1].set_xlim([0, 0.33])
    axs[0,1].set_ylim([0.2, 0.5])
    axs[0,1].tick_params('y', labelleft=False)
    axs[0,1].tick_params('x', labelbottom=False)
    #
    #axs[1,0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    axs[1,0].set_ylabel(r'$c_\text{s,nuc}^2/c^2$',fontsize='14')
    axs[1,0].set_xlim([0, 0.33])
    axs[1,0].set_ylim([-0.05, 0.25])
    axs[1,0].tick_params('x', labelbottom=False)
    #
    #axs[1,1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    axs[1,1].set_xlim([0, 0.33])
    axs[1,1].set_ylim([-0.05, 0.25])
    axs[1,1].tick_params('y', labelleft=False)
    axs[1,1].tick_params('x', labelbottom=False)
    #
    axs[2,0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    axs[2,0].set_ylabel(r'$c_\text{s,tot}^2/c^2$',fontsize='14')
    axs[2,0].set_xlim([0, 0.33])
    axs[2,0].set_ylim([-0.05, 0.25])
    #
    axs[2,1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    axs[2,1].set_xlim([0, 0.33])
    axs[2,1].set_ylim([-0.05, 0.25])
    axs[2,1].tick_params('y', labelleft=False)
    #
    # fix the asymmetry parameters
    #
    asys = [ 0.6, 0.8 ]
    #
    mb_check = []
    model_check = []
    #
    for asy in asys:
        #
        print('asy:',asy)
        #
        for kmb,mb in enumerate(micro_mbs):
            #
            print('mb:',mb,kmb)
            #
            models, models_lower = nuda.matter.micro_esym_models_mb( mb )
            #models, models_lower = nuda.matter.micro_models_mb( mb )
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
                    continue
                #
                if micro.cs2_lep is not None: 
                    if mb in mb_check:
                        axs[0,0].plot( micro.den, micro.cs2_lep, marker='o', linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                        axs[1,0].plot( micro.den, micro.cs2_nuc, marker='o', linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                        axs[2,0].plot( micro.den, micro.cs2_tot, marker='o', linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                    else:
                        mb_check.append(mb)
                        axs[0,0].plot( micro.den, micro.cs2_lep, marker='o', linestyle=lstyle, label=mb, markevery=micro.every, color=nuda.param.col[kmb] )
                        axs[1,0].plot( micro.den, micro.cs2_nuc, marker='o', linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                        axs[2,0].plot( micro.den, micro.cs2_tot, marker='o', linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                # end of model
            # end of mb
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
                    continue
                #
                if pheno.cs2_lep is not None: 
                    print('model:',model,' param:',param)
                    if model in model_check:
                        axs[0,1].plot( pheno.den, pheno.cs2_lep, linestyle=lstyle, markevery=pheno.every, color=nuda.param.col[kmodel] )
                        axs[1,1].plot( pheno.den, pheno.cs2_nuc, linestyle=lstyle, markevery=pheno.every, color=nuda.param.col[kmodel] )
                        axs[2,1].plot( pheno.den, pheno.cs2_tot, linestyle=lstyle, markevery=pheno.every, color=nuda.param.col[kmodel] )
                    else:
                        model_check.append(model)
                        axs[0,1].plot( pheno.den, pheno.cs2_lep, linestyle=lstyle, label=model, markevery=pheno.every, color=nuda.param.col[kmodel] )
                        axs[1,1].plot( pheno.den, pheno.cs2_nuc, linestyle=lstyle, markevery=pheno.every, color=nuda.param.col[kmodel] )
                        axs[2,1].plot( pheno.den, pheno.cs2_tot, linestyle=lstyle, markevery=pheno.every, color=nuda.param.col[kmodel] )
                # end of param
            # end of model
    #
    axs[0,0].text(0.02,0.45,'microscopic models',fontsize='10')
    axs[0,1].text(0.02,0.45,'phenomenological models',fontsize='10')
    #
    axs[0,0].text(0.1,0.4,r'$\delta=0.6$',fontsize='10')
    axs[0,1].text(0.1,0.4,r'$\delta=0.6$',fontsize='10')
    axs[0,0].text(0.1,0.3,r'$\delta=0.8$',fontsize='10')
    axs[0,1].text(0.1,0.3,r'$\delta=0.8$',fontsize='10')
    #
    axs[1,0].text(0.1,0.2,r'$\delta=0.6$',fontsize='10')
    axs[1,1].text(0.1,0.2,r'$\delta=0.6$',fontsize='10')
    axs[1,0].text(0.1,0.15,r'$\delta=0.8$',fontsize='10')
    axs[1,1].text(0.1,0.15,r'$\delta=0.8$',fontsize='10')
    #
    axs[2,0].text(0.1,0.2,r'$\delta=0.6$',fontsize='10')
    axs[2,1].text(0.1,0.2,r'$\delta=0.6$',fontsize='10')
    axs[2,0].text(0.1,0.15,r'$\delta=0.8$',fontsize='10')
    axs[2,1].text(0.1,0.15,r'$\delta=0.8$',fontsize='10')
    #
    fig.legend(loc='upper left',bbox_to_anchor=(0.1,1.0),columnspacing=2,fontsize='8',ncol=6,frameon=False)
    #
    if pname is not None: 
        plt.savefig(pname, dpi=200)
        plt.close()
    #