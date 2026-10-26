import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def eos_setupAMLeqi_xe_fig( pname, models1, models2, band ):
    """
    Plot the electron fraction (=xe) in asymmetric matter at lepton equilibrium.

    The plot is 2x1 with:

    [0]: microscopic models.  [1]: phenomenologic models.

    :param pname: name of the figure (*.png)
    :type pname: str.
    :param models1: array of models.
    :type models1: array of str.
    :param models2: array of models.
    :type models2: array of str.
    :param band: object instantiated on the reference band.
    :type band: object.
    """
    #
    print(f'Plot name: {pname}')
    #
    # xe at micro-equilibrium
    #
    asy = 0.5
    #
    fig, axs = plt.subplots(1,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=0.95, top=0.90, wspace=0.05, hspace=0.3 )
    #
    axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    axs[0].set_ylabel(r'electron fraction $x_e$',fontsize='14')
    axs[0].set_xlim([0, 0.33])
    axs[0].set_ylim([0.1, 0.3])
    #
    axs[1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    #axs[1].set_ylabel(r'electron fraction $x_e$',fontsize='14')
    axs[1].set_xlim([0, 0.33])
    axs[1].set_ylim([0.1, 0.3])
    axs[1].tick_params('y', labelleft=False)
    #
    for k in range(2):
        #
        if k == 0:
            models = models1
            axs[0].text(0.08,0.22,'microscopic models',fontsize='10')
        if k == 1:
            models = models2
            axs[1].text(0.08,0.22,'phenomenological models',fontsize='10')
        #
        model_check = []
        #
        for kmodel,model in enumerate(models):
            #
            params, params_lower = nuda.matter.matter_esym_params( model = model )
            #
            for param in params:
                #
                matt = nuda.eos.setupAMLeqi( model = model, param = param, asy = asy )
                if nuda.env.verb_output: matt.print_outputs()
                #
                lstyle = "dashed"
                if matt.nm_e2a_int is not None and matt.sm_e2a_int is not None:
                    check = nuda.matter.setupCheck(eos=matt, band=band)
                    if check.isInside:
                        lstyle = "solid"
                #
                if matt.x_el is not None:
                    print('model:',model,' param:',param)
                    if model in model_check:
                        axs[k].plot( matt.den, matt.x_el, linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                    else:
                        model_check.append(model)
                        axs[k].plot( matt.den, matt.x_el, linestyle=lstyle, label=model, markevery=matt.every, color=nuda.param.col[kmodel] )
            # end of param
        # end of model
    #
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=6,frameon=False)
    #
    if pname is not None:
    	fig.savefig(pname, dpi=200)
    	plt.close()

def eos_setupAMLeqi_xmu_fig( pname, models1, models2, band ):
    """
    Plot the muon fraction (=xmu) in asymmetric matter at lepton equilibrium.

    The plot is 2x1 with:

    [0]: microscopic models.  [1]: phenomenologic models.

    :param pname: name of the figure (*.png)
    :type pname: str.
    :param models1: array of models.
    :type models1: array of str.
    :param models2: array of models.
    :type models2: array of str.
    :param band: object instantiated on the reference band.
    :type band: object.
    """
    #
    print(f'Plot name: {pname}')
    #
    # xmu at micro-equilibrium
    #
    asy = 0.5
    #
    fig, axs = plt.subplots(1,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=0.95, top=0.90, wspace=0.05, hspace=0.3 )
    #
    axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    axs[0].set_ylabel(r'muon fraction $x_\mu$',fontsize='14')
    axs[0].set_xlim([0, 0.33])
    axs[0].set_ylim([0, 0.15])
    #
    axs[1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    #axs[1].set_ylabel(r'muon fraction $x_\mu$',fontsize='14')
    axs[1].set_xlim([0, 0.33])
    axs[1].set_ylim([0, 0.15])
    axs[1].tick_params('y', labelleft=False)
    #
    for k in range(2):
        #
        if k == 0:
            models = models1
            axs[0].text(0.08,0.12,'microscopic models',fontsize='10')
        if k == 1:
            models = models2
            axs[1].text(0.08,0.12,'phenomenological models',fontsize='10')
        #
        model_check = []
        #
        for kmodel,model in enumerate(models):
            #
            params, params_lower = nuda.matter.matter_esym_params( model = model )
            #
            for param in params:
                #
                matt = nuda.eos.setupAMLeqi( model = model, param = param, asy = asy )
                if nuda.env.verb_output: matt.print_outputs()
                #
                lstyle = "dashed"
                if matt.nm_e2a_int is not None and matt.sm_e2a_int is not None:
                    check = nuda.matter.setupCheck(eos=matt, band=band)
                    if check.isInside:
                        lstyle = "solid"
                #
                if matt.x_mu is not None: 
                    print('model:',model)
                    if model in model_check:
                        axs[k].plot( matt.den, matt.x_mu, marker='o', linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                    else:
                        model_check.append(model)
                        axs[k].plot( matt.den, matt.x_mu, marker='o', linestyle=lstyle, label=model, markevery=matt.every, color=nuda.param.col[kmodel] )
            # end of model
        # end of mb
    #
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=6,frameon=False)
    #
    if pname is not None:
    	fig.savefig(pname, dpi=200)
    	plt.close()

def eos_setupAMLeqi_xexmu_fig( pname, models1, models2, band ):
    """
    Plot the electron and muon fractions (=xe and xmu) in asymmetric matter at lepton equilibrium.

    The plot is 2x1 with:

    [0]: microscopic models.  [1]: phenomenologic models.

    :param pname: name of the figure (*.png)
    :type pname: str.
    :param models1: array of models.
    :type models1: array of str.
    :param models2: array of models.
    :type models2: array of str.
    :param band: object instantiated on the reference band.
    :type band: object.
    """
    #
    print(f'Plot name: {pname}')
    #
    fig, axs = plt.subplots(1,1)
    #fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=0.95, top=0.90, wspace=0.3, hspace=0.3 )
    #
    axs.set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    axs.set_ylabel(r'$x_e$, $x_\mu$',fontsize='14')
    axs.set_xlim([0, 0.33])
    axs.set_ylim([0, 0.5])
    #
    asys = [ 0.1, 0.3, 0.5, 0.7, 0.9 ]
    #asys = [ 0.5 ]
    #
    for iasy,asy in enumerate(asys):
        #
        model_check = []
        #
        for k in range(2):
            #
            if k == 0:
                models = models1
            if k == 1:
                models = models2
            #
            for kmodel,model in enumerate(models):
                #
                params, params_lower = nuda.matter.matter_esym_params( model = model )
                #
                for param in params:
                    #
                    matt = nuda.eos.setupAMLeqi( model = model, param = param, asy = asy )
                    if nuda.env.verb_output: matt.print_outputs()
                    #
                    lstyle = "dashed"
                    if matt.nm_e2a_int is not None and matt.sm_e2a_int is not None:
                        check = nuda.matter.setupCheck(eos=matt, band=band)
                        if check.isInside:
                            lstyle = "solid"
                    #
                    if matt.esym is not None: 
                        print('model:',model,' param:',param)
                        if model in model_check:
                            axs.plot( matt.den, matt.x_el, linestyle='solid', color=nuda.param.col[iasy] )
                            axs.plot( matt.den, matt.x_mu, linestyle='dashed', color=nuda.param.col[iasy] )
                        else:
                            model_check.append(model)
                            axs.plot( matt.den, matt.x_el, linestyle='solid', label=r'$\delta=$'+str(asy), color=nuda.param.col[iasy] )
                            axs.plot( matt.den, matt.x_mu, linestyle='dashed', color=nuda.param.col[iasy] )
                        #
                    break
                # end of param
            # end of model
        #
        axs.legend(loc='upper right',fontsize='10',ncol=3)
        axs.text(0.05,0.35,r'$x_e$',fontsize='14')
        axs.text(0.02,0.10,r'$x_\mu$',fontsize='14')
    #
    if pname is not None:
    	fig.savefig(pname, dpi=200)
    	plt.close()
    #