import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def eos_setupAMLeq_xe_fig( pname, micro_mbs, pheno_models ):
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
    # xe at beta-equilibrium
    #
    asy = 0.5
    #
    fig, axs = plt.subplots(1,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.90, wspace=0.05, hspace=0.3 )
    #
    axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    axs[0].set_ylabel(r'electron fraction $x_e$')
    axs[0].set_xlim([0, 0.28])
    axs[0].set_ylim([0.1, 0.3])
    #
    axs[1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    #axs[1].set_ylabel(r'electron fraction $x_e$')
    axs[1].set_xlim([0, 0.28])
    axs[1].set_ylim([0.1, 0.3])
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
            beta = nuda.eos.setupAMLeq( model = model, kind = 'micro', asy = asy )
            if nuda.env.verb_output: beta.print_outputs( )
            #
            if beta.x_el is not None: 
                print('model:',model)
                if mb in mb_check:
                    axs[0].plot( beta.den, beta.x_el, marker='o', linestyle=beta.linestyle, markevery=beta.every, color=nuda.param.col[kmb] )
                else:
                    mb_check.append(mb)
                    axs[0].plot( beta.den, beta.x_el, marker='o', linestyle=beta.linestyle, label=mb, markevery=beta.every, color=nuda.param.col[kmb] )
            #axs[0].plot( beta.den, beta.x_el, marker='o', linestyle=beta.linestyle, label=beta.label, markevery=beta.every )
    axs[0].text(0.08,0.22,'microscopic models',fontsize='10')
    #axs[0].legend(loc='upper left',fontsize='8', ncol=3)
    #
    model_check = []
    #
    for kmodel,model in enumerate(pheno_models):
        #
        params, params_lower = nuda.matter.pheno_esym_params( model = model )
        #
        for param in params:
            #
            beta = nuda.eos.setupAMLeq( model = model, param = param, kind = 'pheno', asy = asy )
            if beta.x_el is not None: 
                print('model:',model,' param:',param)
                #beta.label=None
                if model in model_check:
                    axs[1].plot( beta.den, beta.x_el, linestyle=beta.linestyle, markevery=beta.every, color=nuda.param.col[kmodel] )
                else:
                    model_check.append(model)
                    axs[1].plot( beta.den, beta.x_el, linestyle=beta.linestyle, label=model, markevery=beta.every, color=nuda.param.col[kmodel] )
                #
            if nuda.env.verb_output: pheno.print_outputs( )
    #
    axs[1].text(0.08,0.22,'phenomenological models',fontsize='10')
    #
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=5,frameon=False)
    #
    if pname is not None:
    	plt.savefig(pname, dpi=200)
    	plt.close()

def eos_setupAMLeq_xmu_fig( pname, micro_mbs, pheno_models ):
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
    # xmu at beta-equilibrium
    #
    asy = 0.5
    #
    fig, axs = plt.subplots(1,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.90, wspace=0.05, hspace=0.3 )
    #
    axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    axs[0].set_ylabel(r'muon fraction $x_\mu$')
    axs[0].set_xlim([0, 0.28])
    axs[0].set_ylim([0, 0.15])
    #
    axs[1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    #axs[1].set_ylabel(r'muon fraction $x_\mu$')
    axs[1].set_xlim([0, 0.28])
    axs[1].set_ylim([0, 0.15])
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
            beta = nuda.eos.setupAMLeq( model = model, kind = 'micro', asy = asy )
            if nuda.env.verb_output: beta.print_outputs( )
            #
            if beta.x_mu is not None: 
                print('model:',model)
                if mb in mb_check:
                    axs[0].plot( beta.den, beta.x_mu, marker='o', linestyle=beta.linestyle, markevery=beta.every, color=nuda.param.col[kmb] )
                else:
                    mb_check.append(mb)
                    axs[0].plot( beta.den, beta.x_mu, marker='o', linestyle=beta.linestyle, label=mb, markevery=beta.every, color=nuda.param.col[kmb] )
        #
    axs[0].text(0.08,0.12,'microscopic models',fontsize='10')
    #axs[0].legend(loc='upper left',fontsize='8', ncol=3)
    #
    model_check = []
    #
    for kmodel,model in enumerate(pheno_models):
        #
        params, params_lower = nuda.matter.pheno_esym_params( model = model )
        #
        for param in params:
            #
            beta = nuda.eos.setupAMLeq( model = model, param = param, kind = 'pheno', asy = asy )
            if beta.x_mu is not None: 
                print('model:',model,' param:',param)
                #beta.label=None
                if model in model_check:
                    axs[1].plot( beta.den, beta.x_mu, linestyle=beta.linestyle, markevery=beta.every, color=nuda.param.col[kmodel] )
                else:
                    model_check.append(model)
                    axs[1].plot( beta.den, beta.x_mu, linestyle=beta.linestyle, label=model, markevery=beta.every, color=nuda.param.col[kmodel] )
                #
            if nuda.env.verb_output: pheno.print_outputs( )
    #
    axs[1].text(0.08,0.12,'phenomenological models',fontsize='10')
    #
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=5,frameon=False)
    #
    if pname is not None:
    	plt.savefig(pname, dpi=200)
    	plt.close()

def eos_setupAMLeq_xexmu_fig( pname, micro_mbs, pheno_models ):
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
    fig, axs = plt.subplots(1,1)
    #fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.90, wspace=0.3, hspace=0.3 )
    #
    axs.set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='10')
    axs.set_ylabel(r'$x_e$, $x_\mu$',fontsize='10')
    axs.set_xlim([0, 0.28])
    axs.set_ylim([0, 0.5])
    #
    asys = [ 0.1, 0.3, 0.5, 0.7, 0.9 ]
    #asys = [ 0.5 ]
    #
    for iasy,asy in enumerate(asys):
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
                continue
                am = nuda.eos.setupAMLeq( model = model, kind = 'micro', asy = asy )
                if nuda.env.verb_output: am.print_outputs( )
                #
                if am.esym is not None: 
                    print('model:',model)
                    axs.plot( am.den, am.x_mu, marker='o', linestyle=am.linestyle, label=am.label, markevery=am.every )
        #axs[0].text(0.02,12,'microscopic models',fontsize='10')
        #axs[0].text(0.02,10,'for $\delta=$'+str(asy),fontsize='10')
        #
        model_check = []
        #
        for kmodel,model in enumerate(pheno_models):
            #
            params, params_lower = nuda.matter.pheno_esym_params( model = model )
            #
            for param in params:
                #
                am = nuda.eos.setupAMLeq( model = model, param = param, kind = 'pheno', asy = asy )
                if am.esym is not None: 
                    print('model:',model,' param:',param)
                    #beta.label=None
                    if model in model_check:
                        axs.plot( am.den, am.x_el, linestyle='solid', color=nuda.param.col[iasy] )
                        axs.plot( am.den, am.x_mu, linestyle='dashed', color=nuda.param.col[iasy] )
                    else:
                        model_check.append(model)
                        axs.plot( am.den, am.x_el, linestyle='solid', label=r'$\delta=$'+str(asy), color=nuda.param.col[iasy] )
                        axs.plot( am.den, am.x_mu, linestyle='dashed', color=nuda.param.col[iasy] )
                    #
                if nuda.env.verb_output: pheno.print_outputs( )
                break
        #
        axs.legend(loc='upper right',fontsize='10',ncol=3)
        axs.text(0.05,0.35,r'$x_e$',fontsize='14')
        axs.text(0.02,0.10,r'$x_\mu$',fontsize='14')
    #
    if pname is not None:
    	plt.savefig(pname, dpi=200)
    	plt.close()