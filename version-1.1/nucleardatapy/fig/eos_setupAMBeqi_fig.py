import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def eos_setupAMBeqi_e2a_nuc_fig( pname, models1, models2, band ):
    """
    Plot the nucleon contribution to the energy per nucleon in asymmetric matter at beta equilibrium.

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
    for k in range(2):
        #
        if k == 0:
            models = models1
            axs[0].text(0.02,20,'microscopic models',fontsize='10')
        if k == 1:
            models = models2
            axs[1].text(0.02,20,'phenomenological models',fontsize='10')
        #
        model_check = []
        #
        for kmodel,model in enumerate(models):
            #
            params, params_lower = nuda.matter.matter_esym_params( model = model )
            #
            for param in params:
                #
                matt = nuda.eos.setupAMBeqi( model = model, param = param )
                if nuda.env.verb_output: matt.print_outputs()
                #
                lstyle = "dashed"
                if matt.nm_e2a_int is not None and matt.sm_e2a_int is not None:
                    check = nuda.matter.setupCheck(eos=matt, band=band)
                    if check.isInside:
                        lstyle = "solid"
                #
                if matt.e2a_int_nuc is not None: 
                    print('model:',model)
                    if model in model_check:
                        if k == 0:
                            axs[k].plot( matt.den, matt.e2a_int_nuc, marker='o', linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                        else:
                            axs[k].plot( matt.den, matt.e2a_int_nuc, linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                    else:
                        model_check.append(model)
                        if k == 0:
                            axs[k].plot( matt.den, matt.e2a_int_nuc, marker='o', linestyle=lstyle, label=model, markevery=matt.every, color=nuda.param.col[kmodel] )
                        else:
                            axs[k].plot( matt.den, matt.e2a_int_nuc, linestyle=lstyle, label=model, markevery=matt.every, color=nuda.param.col[kmodel] )
            # end of param
        # end of model
    #
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=6,frameon=False)
    #
    if pname is not None: 
        fig.savefig(pname, dpi=200)
        plt.close()

def eos_setupAMBeqi_pre_nuc_fig( pname, models1, models2, band ):
    """
    Plot the nucleon contribution to the pressure in asymmetric matter at beta equilibrium.

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
    for k in range(2):
        #
        if k == 0:
            models = models1
            axs[0].text(0.02,20,'microscopic models',fontsize='10')
        if k == 1:
            models = models2
            axs[1].text(0.02,20,'phenomenological models',fontsize='10')
        #
        model_check = []
        #
        for kmodel,model in enumerate(models):
            #
            params, params_lower = nuda.matter.matter_esym_params( model = model )
            #
            for param in params:
                #
                matt = nuda.eos.setupAMBeqi( model = model, param = param )
                if nuda.env.verb_output: matt.print_outputs()
                #
                lstyle = "dashed"
                if matt.nm_e2a_int is not None and matt.sm_e2a_int is not None:
                    check = nuda.matter.setupCheck(eos=matt, band=band)
                    if check.isInside:
                        lstyle = "solid"
                #
                if matt.pre_nuc is not None: 
                    print('model:',model)
                    if model in model_check:
                        if k == 0:
                            axs[k].plot( matt.den, matt.pre_nuc, marker='o', linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                        else:
                            axs[k].plot( matt.den, matt.pre_nuc, linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                    else:
                        model_check.append(model)
                        if k == 0:
                            axs[k].plot( matt.den, matt.pre_nuc, marker='o', linestyle=lstyle, label=model, markevery=matt.every, color=nuda.param.col[kmodel] )
                        else:
                            axs[k].plot( matt.den, matt.pre_nuc, linestyle=lstyle, label=model, markevery=matt.every, color=nuda.param.col[kmodel] )
            # end of param
        # end of model
    #
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=6,frameon=False)
    #
    if pname is not None: 
        fig.savefig(pname, dpi=200)
        plt.close()

def eos_setupAMBeqi_cs2_nuc_fig( pname, models1, models2, band ):
    """
    Plot the nucleon contribution to the square of the sound speed in asymmetric matter at beta equilibrium.

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
    for k in range(2):
        #
        if k == 0:
            models = models1
            axs[0].text(0.02,0.2,'microscopic models',fontsize='10')
        if k == 1:
            models = models2
            axs[1].text(0.02,0.2,'phenomenological models',fontsize='10')
        #
        model_check = []
        #
        for kmodel,model in enumerate(models):
            #
            params, params_lower = nuda.matter.matter_esym_params( model = model )
            #
            for param in params:
                #
                matt = nuda.eos.setupAMBeqi( model = model, param = param )
                if nuda.env.verb_output: matt.print_outputs()
                #
                lstyle = "dashed"
                if matt.nm_e2a_int is not None and matt.sm_e2a_int is not None:
                    check = nuda.matter.setupCheck(eos=matt, band=band)
                    if check.isInside:
                        lstyle = "solid"
                #
                if matt.cs2_nuc is not None: 
                    print('model:',model)
                    if model in model_check:
                        if k == 0:
                            axs[k].plot( matt.den, matt.cs2_nuc, marker='o', linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                        else:
                            axs[k].plot( matt.den, matt.cs2_nuc, linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                    else:
                        model_check.append(model)
                        if k == 0:
                            axs[k].plot( matt.den, matt.cs2_nuc, marker='o', linestyle=lstyle, label=model, markevery=matt.every, color=nuda.param.col[kmodel] )
                        else:
                            axs[k].plot( matt.den, matt.cs2_nuc, linestyle=lstyle, label=model, markevery=matt.every, color=nuda.param.col[kmodel] )
            # end of param
        # end of model
    #
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=6,frameon=False)
    #
    if pname is not None: 
        fig.savefig(pname, dpi=200)
        plt.close()

def eos_setupAMBeqi_e2a_lep_fig( pname, models1, models2, band ):
    """
    Plot the lepton contribution to the energy per nucleon in asymmetric matter at beta equilibrium.

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
    fig, axs = plt.subplots(1,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=0.95, top=0.90, wspace=0.05, hspace=0.05 )
    #
    axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    axs[0].set_ylabel(r'$e_\text{lep}^\text{int}$ (MeV)',fontsize='14')
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
    for k in range(2):
        #
        if k == 0:
            models = models1
            axs[0].text(0.02,20,'microscopic models',fontsize='10')
        if k == 1:
            models = models2
            axs[1].text(0.02,20,'phenomenological models',fontsize='10')
        #
        model_check = []
        #
        for kmodel,model in enumerate(models):
            #
            params, params_lower = nuda.matter.matter_esym_params( model = model )
            #
            for param in params:
                #
                matt = nuda.eos.setupAMBeqi( model = model, param = param )
                if nuda.env.verb_output: matt.print_outputs()
                #
                lstyle = "dashed"
                if matt.nm_e2a_int is not None and matt.sm_e2a_int is not None:
                    check = nuda.matter.setupCheck(eos=matt, band=band)
                    if check.isInside:
                        lstyle = "solid"
                #
                if matt.e2a_lep is not None: 
                    print('model:',model)
                    if model in model_check:
                        if k == 0:
                            axs[k].plot( matt.den, matt.e2a_lep, marker='o', linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                        else:
                            axs[k].plot( matt.den, matt.e2a_lep, linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                    else:
                        model_check.append(model)
                        if k == 0:
                            axs[k].plot( matt.den, matt.e2a_lep, marker='o', linestyle=lstyle, label=model, markevery=matt.every, color=nuda.param.col[kmodel] )
                        else:
                            axs[k].plot( matt.den, matt.e2a_lep, linestyle=lstyle, label=model, markevery=matt.every, color=nuda.param.col[kmodel] )
            # end of param
        # end of model
    #
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=6,frameon=False)
    #
    if pname is not None: 
        fig.savefig(pname, dpi=200)
        plt.close()

def eos_setupAMBeqi_pre_lep_fig( pname, models1, models2, band ):
    """
    Plot the lepton contribution to the pressure in asymmetric matter at beta equilibrium.

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
    for k in range(2):
        #
        if k == 0:
            models = models1
            axs[0].text(0.02,20,'microscopic models',fontsize='10')
        if k == 1:
            models = models2
            axs[1].text(0.02,20,'phenomenological models',fontsize='10')
        #
        model_check = []
        #
        for kmodel,model in enumerate(models):
            #
            params, params_lower = nuda.matter.matter_esym_params( model = model )
            #
            for param in params:
                #
                matt = nuda.eos.setupAMBeqi( model = model, param = param )
                if nuda.env.verb_output: matt.print_outputs()
                #
                lstyle = "dashed"
                if matt.nm_e2a_int is not None and matt.sm_e2a_int is not None:
                    check = nuda.matter.setupCheck(eos=matt, band=band)
                    if check.isInside:
                        lstyle = "solid"
                #
                if matt.pre_lep is not None: 
                    print('model:',model)
                    if model in model_check:
                        if k == 0:
                            axs[k].plot( matt.den, matt.pre_lep, marker='o', linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                        else:
                            axs[k].plot( matt.den, matt.pre_lep, linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                    else:
                        model_check.append(model)
                        if k == 0:
                            axs[k].plot( matt.den, matt.pre_lep, marker='o', linestyle=lstyle, label=model, markevery=matt.every, color=nuda.param.col[kmodel] )
                        else:
                            axs[k].plot( matt.den, matt.pre_lep, linestyle=lstyle, label=model, markevery=matt.every, color=nuda.param.col[kmodel] )
            # end of param
        # end of model
    #
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=6,frameon=False)
    #
    if pname is not None: 
        fig.savefig(pname, dpi=200)
        plt.close()

def eos_setupAMBeqi_cs2_lep_fig( pname, models1, models2, band ):
    """
    Plot the lepton contribution to the square of the sound speed in asymmetric matter at beta equilibrium.

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
    for k in range(2):
        #
        if k == 0:
            models = models1
            axs[0].text(0.02,45,'microscopic models',fontsize='10')
        if k == 1:
            models = models2
            axs[1].text(0.02,45,'phenomenological models',fontsize='10')
        #
        model_check = []
        #
        for kmodel,model in enumerate(models):
            #
            params, params_lower = nuda.matter.matter_esym_params( model = model )
            #
            for param in params:
                #
                matt = nuda.eos.setupAMBeqi( model = model, param = param )
                if nuda.env.verb_output: matt.print_outputs()
                #
                lstyle = "dashed"
                if matt.nm_e2a_int is not None and matt.sm_e2a_int is not None:
                    check = nuda.matter.setupCheck(eos=matt, band=band)
                    if check.isInside:
                        lstyle = "solid"
                #
                if matt.cs2_lep is not None: 
                    print('model:',model)
                    if model in model_check:
                        if k == 0:
                            axs[k].plot( matt.den, matt.cs2_lep, marker='o', linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                        else:
                            axs[k].plot( matt.den, matt.cs2_lep, linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                    else:
                        model_check.append(model)
                        if k == 0:
                            axs[k].plot( matt.den, matt.cs2_lep, marker='o', linestyle=lstyle, label=model, markevery=matt.every, color=nuda.param.col[kmodel] )
                        else:
                            axs[k].plot( matt.den, matt.cs2_lep, linestyle=lstyle, label=model, markevery=matt.every, color=nuda.param.col[kmodel] )
            # end of param
        # end of model
    #
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=6,frameon=False)
    #
    if pname is not None: 
        fig.savefig(pname, dpi=200)
        plt.close()


def eos_setupAMBeqi_e2a_tot_fig( pname, models1, models2, band ):
    """
    Plot the total (=nucleon+lepton) contribution to the energy per nucleon in asymmetric matter at beta equilibrium.

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
    for k in range(2):
        #
        if k == 0:
            models = models1
            axs[0].text(0.02,20,'microscopic models',fontsize='10')
        if k == 1:
            models = models2
            axs[1].text(0.02,20,'phenomenological models',fontsize='10')
        #
        model_check = []
        #
        for kmodel,model in enumerate(models):
            #
            params, params_lower = nuda.matter.matter_esym_params( model = model )
            #
            for param in params:
                #
                matt = nuda.eos.setupAMBeqi( model = model, param = param )
                if nuda.env.verb_output: matt.print_outputs()
                #
                lstyle = "dashed"
                if matt.nm_e2a_int is not None and matt.sm_e2a_int is not None:
                    check = nuda.matter.setupCheck(eos=matt, band=band)
                    if check.isInside:
                        lstyle = "solid"
                #
                if matt.e2a_int_tot is not None: 
                    print('model:',model)
                    if model in model_check:
                        if k == 0:
                            axs[k].plot( matt.den, matt.e2a_int_tot, marker='o', linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                        else:
                            axs[k].plot( matt.den, matt.e2a_int_tot, linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                    else:
                        model_check.append(model)
                        if k == 0:
                            axs[k].plot( matt.den, matt.e2a_int_tot, marker='o', linestyle=lstyle, label=model, markevery=matt.every, color=nuda.param.col[kmodel] )
                        else:
                            axs[k].plot( matt.den, matt.e2a_int_tot, linestyle=lstyle, label=model, markevery=matt.every, color=nuda.param.col[kmodel] )
            # end of param
        # end of model
    #
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=6,frameon=False)
    #
    if pname is not None: 
        fig.savefig(pname, dpi=200)
        plt.close()

def eos_setupAMBeqi_pre_tot_fig( pname, models1, models2, band ):
    """
    Plot the total (=nucleon+lepton) contribution to the pressure in asymmetric matter at beta equilibrium.

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
    for k in range(2):
        #
        if k == 0:
            models = models1
            axs[0].text(0.02,20,'microscopic models',fontsize='10')
        if k == 1:
            models = models2
            axs[1].text(0.02,20,'phenomenological models',fontsize='10')
        #
        model_check = []
        #
        for kmodel,model in enumerate(models):
            #
            params, params_lower = nuda.matter.matter_esym_params( model = model )
            #
            for param in params:
                #
                matt = nuda.eos.setupAMBeqi( model = model, param = param )
                if nuda.env.verb_output: matt.print_outputs()
                #
                lstyle = "dashed"
                if matt.nm_e2a_int is not None and matt.sm_e2a_int is not None:
                    check = nuda.matter.setupCheck(eos=matt, band=band)
                    if check.isInside:
                        lstyle = "solid"
                #
                if matt.pre_tot is not None: 
                    print('model:',model)
                    if model in model_check:
                        if k == 0:
                            axs[k].plot( matt.den, matt.pre_tot, marker='o', linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                        else:
                            axs[k].plot( matt.den, matt.pre_tot, linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                    else:
                        model_check.append(model)
                        if k == 0:
                            axs[k].plot( matt.den, matt.pre_tot, marker='o', linestyle=lstyle, label=model, markevery=matt.every, color=nuda.param.col[kmodel] )
                        else:
                            axs[k].plot( matt.den, matt.pre_tot, linestyle=lstyle, label=model, markevery=matt.every, color=nuda.param.col[kmodel] )
            # end of param
        # end of model
    #
    axs[1].errorbar( p_den, p_cen, yerr=p_std, color='k' )
    axs[1].errorbar( p_den+0.005, p_pheno_cen, yerr=p_pheno_std, color='r' )
    #
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=6,frameon=False)
    #
    if pname is not None: 
        fig.savefig(pname, dpi=200)
        plt.close()

def eos_setupAMBeqi_cs2_tot_fig( pname, models1, models2, band ):
    """
    Plot the total (=nucleon+lepton) contribution to the square of the sound speed in asymmetric matter at beta equilibrium.

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
    for k in range(2):
        #
        if k == 0:
            models = models1
            axs[0].text(0.02,20,'microscopic models',fontsize='10')
        if k == 1:
            models = models2
            axs[1].text(0.02,20,'phenomenological models',fontsize='10')
        #
        model_check = []
        #
        for kmodel,model in enumerate(models):
            #
            params, params_lower = nuda.matter.matter_esym_params( model = model )
            #
            for param in params:
                #
                matt = nuda.eos.setupAMBeqi( model = model, param = param )
                if nuda.env.verb_output: matt.print_outputs()
                #
                lstyle = "dashed"
                if matt.nm_e2a_int is not None and matt.sm_e2a_int is not None:
                    check = nuda.matter.setupCheck(eos=matt, band=band)
                    if check.isInside:
                        lstyle = "solid"
                #
                if matt.cs2_tot is not None: 
                    print('model:',model)
                    if model in model_check:
                        if k == 0:
                            axs[k].plot( matt.den, matt.cs2_tot, marker='o', linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                        else:
                            axs[k].plot( matt.den, matt.cs2_tot, linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                    else:
                        model_check.append(model)
                        if k == 0:
                            axs[k].plot( matt.den, matt.cs2_tot, marker='o', linestyle=lstyle, label=model, markevery=matt.every, color=nuda.param.col[kmodel] )
                        else:
                            axs[k].plot( matt.den, matt.cs2_tot, linestyle=lstyle, label=model, markevery=matt.every, color=nuda.param.col[kmodel] )
            # end of param
        # end of model
    #
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=6,frameon=False)
    #
    if pname is not None: 
        fig.savefig(pname, dpi=200)
        plt.close()

def eos_setupAMBeqi_eos_fig( pname, models1, models2, band ):
    """
    Plot the equation of state in asymmetric matter at beta equilibrium.

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
    for k in range(2):
        #
        if k == 0:
            models = models1
            axs[0].text(10,20,'microscopic models',fontsize='10')
            axs[0].errorbar( p_den, p_cen, yerr=p_std, color='k', linewidth = 3 )
            axs[0].errorbar( p_den+5.0, p_micro_cen, yerr=p_micro_std, color='r', linewidth = 3 )
        if k == 1:
            models = models2
            axs[1].text(10,20,'phenomenological models',fontsize='10')
            axs[1].errorbar( p_den, p_cen, yerr=p_std, color='k', linewidth = 3 )
            axs[1].errorbar( p_den+5.0, p_pheno_cen, yerr=p_pheno_std, color='r', linewidth = 3 )
        #
        model_check = []
        #
        for kmodel,model in enumerate(models):
            #
            params, params_lower = nuda.matter.matter_esym_params( model = model )
            #
            for param in params:
                #
                matt = nuda.eos.setupAMBeqi( model = model, param = param )
                if nuda.env.verb_output: matt.print_outputs()
                #
                lstyle = "dashed"
                if matt.nm_e2a_int is not None and matt.sm_e2a_int is not None:
                    check = nuda.matter.setupCheck(eos=matt, band=band)
                    if check.isInside:
                        lstyle = "solid"
                #
                if matt.pre_tot is not None: 
                    print('model:',model)
                    if model in model_check:
                        if k == 0:
                            axs[k].plot( matt.eps_tot, matt.pre_tot, marker='o', linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                        else:
                            axs[k].plot( matt.eps_tot, matt.pre_tot, linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                    else:
                        model_check.append(model)
                        if k == 0:
                            axs[k].plot( matt.eps_tot, matt.pre_tot, marker='o', linestyle=lstyle, label=model, markevery=matt.every, color=nuda.param.col[kmodel] )
                        else:
                            axs[k].plot( matt.eps_tot, matt.pre_tot, linestyle=lstyle, label=model, markevery=matt.every, color=nuda.param.col[kmodel] )
            # end of param
        # end of model
    #
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=6,frameon=False)
    #
    if pname is not None: 
        fig.savefig(pname, dpi=200)
        plt.close()

def eos_setupAMBeqi_xp_fig( pname, models1, models2, band ):
    """
    Plot the proton fraction (=xp) in asymmetric matter at beta equilibrium.

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
    for k in range(2):
        #
        if k == 0:
            models = models1
            axs[0].text(0.02,0.18,'microscopic models',fontsize='10')
        if k == 1:
            models = models2
            axs[1].text(0.02,0.18,'phenomenological models',fontsize='10')
        #
        model_check = []
        #
        for kmodel,model in enumerate(models):
            #
            params, params_lower = nuda.matter.matter_esym_params( model = model )
            #
            for param in params:
                #
                matt = nuda.eos.setupAMBeqi( model = model, param = param )
                if nuda.env.verb_output: matt.print_outputs()
                #
                lstyle = "dashed"
                if matt.nm_e2a_int is not None and matt.sm_e2a_int is not None:
                    check = nuda.matter.setupCheck(eos=matt, band=band)
                    if check.isInside:
                        lstyle = "solid"
                #
                if matt.x_p is not None: 
                    print('model:',model)
                    if model in model_check:
                        if k == 0:
                            axs[k].plot( matt.den, matt.x_p, marker='o', linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                        else:
                            axs[k].plot( matt.den, matt.x_p, linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                    else:
                        model_check.append(model)
                        if k == 0:
                            axs[k].plot( matt.den, matt.x_p, marker='o', linestyle=lstyle, label=model, markevery=matt.every, color=nuda.param.col[kmodel] )
                        else:
                            axs[k].plot( matt.den, matt.x_p, linestyle=lstyle, label=model, markevery=matt.every, color=nuda.param.col[kmodel] )
            # end of param
        # end of model
    #
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=6,frameon=False)
    #
    if pname is not None: 
    	fig.savefig(pname, dpi=200)
    	plt.close()

def eos_setupAMBeqi_xe_fig( pname, models1, models2, band ):
    """
    Plot the electron fraction (=xe) in asymmetric matter at beta equilibrium.

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
    for k in range(2):
        #
        if k == 0:
            models = models1
            axs[0].text(0.02,0.18,'microscopic models',fontsize='10')
        if k == 1:
            models = models2
            axs[1].text(0.02,0.18,'phenomenological models',fontsize='10')
        #
        model_check = []
        #
        for kmodel,model in enumerate(models):
            #
            params, params_lower = nuda.matter.matter_esym_params( model = model )
            #
            for param in params:
                #
                matt = nuda.eos.setupAMBeqi( model = model, param = param )
                if nuda.env.verb_output: matt.print_outputs()
                #
                lstyle = "dashed"
                if matt.nm_e2a_int is not None and matt.sm_e2a_int is not None:
                    check = nuda.matter.setupCheck(eos=matt, band=band)
                    if check.isInside:
                        lstyle = "solid"
                #
                if matt.x_el is not None: 
                    print('model:',model)
                    if model in model_check:
                        if k == 0:
                            axs[k].plot( matt.den, matt.x_el, marker='o', linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                        else:
                            axs[k].plot( matt.den, matt.x_el, linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                    else:
                        model_check.append(model)
                        if k == 0:
                            axs[k].plot( matt.den, matt.x_el, marker='o', linestyle=lstyle, label=model, markevery=matt.every, color=nuda.param.col[kmodel] )
                        else:
                            axs[k].plot( matt.den, matt.x_el, linestyle=lstyle, label=model, markevery=matt.every, color=nuda.param.col[kmodel] )
            # end of param
        # end of model
    #
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=6,frameon=False)
    #
    if pname is not None: 
    	fig.savefig(pname, dpi=200)
    	plt.close()

def eos_setupAMBeqi_xmu_fig( pname, models1, models2, band ):
    """
    Plot the muon fraction (=xmu) in asymmetric matter at beta equilibrium.

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
    for k in range(2):
        #
        if k == 0:
            models = models1
            axs[0].text(0.02,0.18,'microscopic models',fontsize='10')
        if k == 1:
            models = models2
            axs[1].text(0.02,0.18,'phenomenological models',fontsize='10')
        #
        model_check = []
        #
        for kmodel,model in enumerate(models):
            #
            params, params_lower = nuda.matter.matter_esym_params( model = model )
            #
            for param in params:
                #
                matt = nuda.eos.setupAMBeqi( model = model, param = param )
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
                        if k == 0:
                            axs[k].plot( matt.den, matt.x_mu, marker='o', linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                        else:
                            axs[k].plot( matt.den, matt.x_mu, linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                    else:
                        model_check.append(model)
                        if k == 0:
                            axs[k].plot( matt.den, matt.x_mu, marker='o', linestyle=lstyle, label=model, markevery=matt.every, color=nuda.param.col[kmodel] )
                        else:
                            axs[k].plot( matt.den, matt.x_mu, linestyle=lstyle, label=model, markevery=matt.every, color=nuda.param.col[kmodel] )
            # end of param
        # end of model
    #
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=6,frameon=False)
    #
    if pname is not None: 
    	fig.savefig(pname, dpi=200)
    	plt.close()
    #