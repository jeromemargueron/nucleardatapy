import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def eos_setupAM_e_fig( pname, micro_mbs, pheno_models, band ):
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
    fig.subplots_adjust(left=0.10, bottom=0.12, right=None, top=0.9, wspace=0.05, hspace=0.05 )
    #
    #axs[0,0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    axs[0,0].set_ylabel(r'$E_\text{lep}/A$')
    axs[0,0].set_xlim([0, 0.28])
    axs[0,0].set_ylim([-2, 38])
    axs[0,0].tick_params('x', labelbottom=False)
    #
    #axs[0,1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    axs[0,1].set_xlim([0, 0.28])
    axs[0,1].set_ylim([-2, 38])
    axs[0,1].tick_params('y', labelleft=False)
    axs[0,1].tick_params('x', labelbottom=False)
    #
    #axs[1,0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    axs[1,0].set_ylabel(r'$E_\text{nuc}/A$')
    axs[1,0].set_xlim([0, 0.28])
    axs[1,0].set_ylim([-10, 30])
    axs[1,0].tick_params('x', labelbottom=False)
    #
    #axs[1,1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    axs[1,1].set_xlim([0, 0.28])
    axs[1,1].set_ylim([-10, 30])
    axs[1,1].tick_params('y', labelleft=False)
    axs[1,1].tick_params('x', labelbottom=False)
    #
    axs[2,0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    axs[2,0].set_ylabel(r'$E_\text{tot}/A$')
    axs[2,0].set_xlim([0, 0.28])
    axs[2,0].set_ylim([-2, 38])
    #
    axs[2,1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    axs[2,1].set_xlim([0, 0.28])
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
                        axs[1,0].plot( micro.den, micro.e2a_nuc, marker='o', linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                        axs[2,0].plot( micro.den, micro.e2a_tot, marker='o', linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                    else:
                        mb_check.append(mb)
                        print('mb:',mb)
                        print('model:',model)
                        print('den:',micro.den)
                        print('e2a_lep:',micro.e2a_lep)
                        axs[0,0].plot( micro.den, micro.e2a_lep, marker='o', linestyle=lstyle, label=mb, markevery=micro.every, color=nuda.param.col[kmb] )
                        axs[1,0].plot( micro.den, micro.e2a_nuc, marker='o', linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
                        axs[2,0].plot( micro.den, micro.e2a_tot, marker='o', linestyle=lstyle, markevery=micro.every, color=nuda.param.col[kmb] )
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
                        axs[1,1].plot( pheno.den, pheno.e2a_nuc, linestyle=lstyle, markevery=pheno.every, color=nuda.param.col[kmodel] )
                        axs[2,1].plot( pheno.den, pheno.e2a_tot, linestyle=lstyle, markevery=pheno.every, color=nuda.param.col[kmodel] )
                    else:
                        model_check.append(model)
                        axs[0,1].plot( pheno.den, pheno.e2a_lep, linestyle=lstyle, label=model, markevery=pheno.every, color=nuda.param.col[kmodel] )
                        axs[1,1].plot( pheno.den, pheno.e2a_nuc, linestyle=lstyle, markevery=pheno.every, color=nuda.param.col[kmodel] )
                        axs[2,1].plot( pheno.den, pheno.e2a_tot, linestyle=lstyle, markevery=pheno.every, color=nuda.param.col[kmodel] )
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
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=5,frameon=False)
    #
    if pname is not None: 
        plt.savefig(pname, dpi=200)
        plt.close()
    #