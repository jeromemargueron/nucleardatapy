import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

#
# xe at micro-equilibrium
#
asy = 0.5

def eos_setupAMi_e2a_asy_lep_fig( pname, models1, models2, asy, band ):
    """
    Plot the leptonic contribution to the energy per nucleon in asymmetric matter controlled by the variable `asy` (defined as (N-Z)/A).

    The plot is 1x2 with:

    [0]: microscopic models. [1]: phenomenologic models.

    :param pname: name of the figure (*.png)
    :type pname: str.
    :param models1: array of models.
    :type models1: array of str.
    :param models2: array of models.
    :type models2: array of str.
    :param asy: asymmetry parameter defined as (N-Z)/A.
    :type asy: real.
    :param band: object instantiated on the reference band.
    :type band: object.
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
    for k in range(2):
        #
        if k == 0:
            models = models1
            axs[0].text(0.02,-8,'microscopic models',fontsize='10')
            axs[0].text(0.02,-9.5,r'for $\delta=$'+str(asy),fontsize='10')
        if k == 1:
            models = models2
            axs[1].text(0.02,-8,'phenomenological models',fontsize='10')
            axs[1].text(0.02,-9.5,r'for $\delta=$'+str(asy),fontsize='10')
        #
        model_check = []
        #
        for kmodel,model in enumerate(models):
            #
            params, params_lower = nuda.matter.matter_esym_params( model = model )
            #
            for param in params:
                #
                matt = nuda.eos.setupAMi( model = model, param = param, asy = asy )
                if nuda.env.verb_output: matt.print_outputs()
                #
                lstyle = "dashed"
                if matt.nm_e2a_int is not None and matt.sm_e2a_int is not None:
                    check = nuda.matter.setupCheck(eos=matt, band=band)
                    if check.isInside:
                        lstyle = "solid"
                #
                if matt.e2a_lep is not None:
                    print('model:',model,' param:',param)
                    print('den:',matt.den)
                    print('e2a_lep:',matt.e2a_lep)
                    if model in model_check:
                        axs[k].plot( matt.den, matt.e2a_lep, marker='o', linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                    else:
                        model_check.append(model)
                        axs[k].plot( matt.den, matt.e2a_lep, marker='o', linestyle=lstyle, label=model, markevery=matt.every, color=nuda.param.col[kmodel] )
            # end of param
        # end of model
    #
    #axs[1].legend(loc='upper left',fontsize='8', ncol=2)
    #axs[0,1].legend(loc='upper left',fontsize='xx-small', ncol=2)
    #axs[1].legend(loc='lower center',bbox_to_anchor=(0.5,1.02),mode='expand',columnspacing=0,fontsize='8', ncol=2,frameon=False)
    #fig.legend(loc='lower center',bbox_to_anchor=(0.5,1.02),mode='expand',columnspacing=0,fontsize='8', ncol=2,frameon=False)
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=5,frameon=False)
    #
    if pname is not None: 
        fig.savefig(pname, dpi=200)
        plt.close()
    #

def eos_setupAMi_pre_asy_lep_fig( pname, models1, models2, asy, band ):
    """
    Plot the leptonic contribution to the pressure in asymmetric matter controlled by the variable `asy` (defined as (N-Z)/A).

    The plot is 1x2 with:

    [0]: microscopic models. [1]: phenomenologic models.

    :param pname: name of the figure (*.png)
    :type pname: str.
    :param models1: array of models.
    :type models1: array of str.
    :param models2: array of models.
    :type models2: array of str.
    :param asy: asymmetry parameter defined as (N-Z)/A.
    :type asy: real.
    :param band: object instantiated on the reference band.
    :type band: object.
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
    for k in range(2):
        #
        if k == 0:
            models = models1
            axs[0].text(0.02,-8,'microscopic models',fontsize='10')
            axs[0].text(0.02,-9.5,r'for $\delta=$'+str(asy),fontsize='10')
        if k == 1:
            models = models2
            axs[1].text(0.02,-8,'phenomenological models',fontsize='10')
            axs[1].text(0.02,-9.5,r'for $\delta=$'+str(asy),fontsize='10')
        #
        model_check = []
        #
        for kmodel,model in enumerate(models):
            #
            params, params_lower = nuda.matter.matter_esym_params( model = model )
            #
            for param in params:
                #
                matt = nuda.eos.setupAMi( model = model, param = param, asy = asy )
                if nuda.env.verb_output: matt.print_outputs()
                #
                lstyle = "dashed"
                if matt.nm_e2a_int is not None and matt.sm_e2a_int is not None:
                    check = nuda.matter.setupCheck(eos=matt, band=band)
                    if check.isInside:
                        lstyle = "solid"
                #
                if matt.pre_lep is not None:
                    print('model:',model,' param:',param)
                    print('den:',matt.den)
                    print('pre_lep:',matt.pre_lep)
                    if model in model_check:
                        axs[k].plot( matt.den, matt.pre_lep, marker='o', linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                    else:
                        model_check.append(model)
                        axs[k].plot( matt.den, matt.pre_lep, marker='o', linestyle=lstyle, label=model, markevery=matt.every, color=nuda.param.col[kmodel] )
            # end of param
        # end of model
    #
    #axs[1].legend(loc='upper left',fontsize='8', ncol=2)
    #axs[0,1].legend(loc='upper left',fontsize='xx-small', ncol=2)
    #axs[1].legend(loc='lower center',bbox_to_anchor=(0.5,1.02),mode='expand',columnspacing=0,fontsize='8', ncol=2,frameon=False)
    #fig.legend(loc='lower center',bbox_to_anchor=(0.5,1.02),mode='expand',columnspacing=0,fontsize='8', ncol=2,frameon=False)
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=5,frameon=False)
    #
    if pname is not None: 
        fig.savefig(pname, dpi=200)
        plt.close()
    #

def eos_setupAMi_cs2_asy_lep_fig( pname, models1, models2, asy, band ):
    """
    Plot the leptonic contribution to the square of the sound speed in asymmetric matter controlled by the variable `asy` (defined as (N-Z)/A).

    The plot is 1x2 with:

    [0]: microscopic models. [1]: phenomenologic models.

    :param pname: name of the figure (*.png)
    :type pname: str.
    :param models1: array of models.
    :type models1: array of str.
    :param models2: array of models.
    :type models2: array of str.
    :param asy: asymmetry parameter defined as (N-Z)/A.
    :type asy: real.
    :param band: object instantiated on the reference band.
    :type band: object.
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
    for k in range(2):
        #
        if k == 0:
            models = models1
            axs[0].text(0.02,-8,'microscopic models',fontsize='10')
            axs[0].text(0.02,-9.5,r'for $\delta=$'+str(asy),fontsize='10')
        if k == 1:
            models = models2
            axs[1].text(0.02,-8,'phenomenological models',fontsize='10')
            axs[1].text(0.02,-9.5,r'for $\delta=$'+str(asy),fontsize='10')
        #
        model_check = []
        #
        for kmodel,model in enumerate(models):
            #
            params, params_lower = nuda.matter.matter_esym_params( model = model )
            #
            for param in params:
                #
                matt = nuda.eos.setupAMi( model = model, param = param, asy = asy )
                if nuda.env.verb_output: matt.print_outputs()
                #
                lstyle = "dashed"
                if matt.nm_e2a_int is not None and matt.sm_e2a_int is not None:
                    check = nuda.matter.setupCheck(eos=matt, band=band)
                    if check.isInside:
                        lstyle = "solid"
                #
                if matt.cs2_lep is not None:
                    print('model:',model,' param:',param)
                    print('den:',matt.den)
                    print('cs2_lep:',matt.cs2_lep)
                    if model in model_check:
                        axs[k].plot( matt.den, matt.cs2_lep, marker='o', linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                    else:
                        model_check.append(model)
                        axs[k].plot( matt.den, matt.cs2_lep, marker='o', linestyle=lstyle, label=model, markevery=matt.every, color=nuda.param.col[kmodel] )
            # end of param
        # end of model
    #
    #axs[1].legend(loc='upper left',fontsize='8', ncol=2)
    #axs[0,1].legend(loc='upper left',fontsize='xx-small', ncol=2)
    #axs[1].legend(loc='lower center',bbox_to_anchor=(0.5,1.02),mode='expand',columnspacing=0,fontsize='8', ncol=2,frameon=False)
    #fig.legend(loc='lower center',bbox_to_anchor=(0.5,1.02),mode='expand',columnspacing=0,fontsize='8', ncol=2,frameon=False)
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=5,frameon=False)
    #
    if pname is not None: 
        fig.savefig(pname, dpi=200)
        plt.close()
    #