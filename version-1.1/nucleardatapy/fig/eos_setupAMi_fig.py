import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def eos_setupAMi_e2a_fig( pname, models1, models2, band ):
    """
    Plot the nucleon, lepton and total (nucleon+leptonic) contribution to the energy per nucleon in asymmetric matter.

    The plot is 2x3 with:

    [0,0]: microscopic models (nucleon).  [0,1]: phenomenologic models (nucleon).

    [1,0]: microscopic models (lepton).   [1,1]: phenomenologic models (lepton).

    [2,0]: microscopic models (total).    [2,1]: phenomenologic models (total).

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
    model_check = []
    #
    for asy in asys:
        #
        print('asy:',asy)
        #
        for k in range(2):
            #
            if k == 0:
                models = models1
                axs[0,0].text(0.02,0,'microscopic models',fontsize='10')
            if k == 1:
                models = models2
                axs[0,1].text(0.02,0,'phenomenological models',fontsize='10')
            #
            #model_check = []
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
                            axs[0,k].plot( matt.den, matt.e2a_lep, marker='o', linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                            axs[1,k].plot( matt.den, matt.e2a_int_nuc, marker='o', linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                            axs[2,k].plot( matt.den, matt.e2a_int_tot, marker='o', linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                        else:
                            model_check.append(model)
                            axs[0,k].plot( matt.den, matt.e2a_lep, marker='o', linestyle=lstyle, label=model, markevery=matt.every, color=nuda.param.col[kmodel] )
                            axs[1,k].plot( matt.den, matt.e2a_int_nuc, marker='o', linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                            axs[2,k].plot( matt.den, matt.e2a_int_tot, marker='o', linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                # end of param
            # end of model
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
        fig.savefig(pname, dpi=200)
        plt.close()
    #

def eos_setupAMi_pre_fig( pname, models1, models2, band ):
    """
    Plot the nucleon, lepton and total (nucleon+leptonic) contribution to the pressure in asymmetric matter.

    The plot is 2x3 with:

    [0,0]: microscopic models (nucleon).  [0,1]: phenomenologic models (nucleon).

    [1,0]: microscopic models (lepton).   [1,1]: phenomenologic models (lepton).

    [2,0]: microscopic models (total).    [2,1]: phenomenologic models (total).

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
    model_check = []
    #
    for asy in asys:
        #
        print('asy:',asy)
        #
        for k in range(2):
            #
            if k == 0:
                models = models1
                axs[0,0].text(0.02,3.5,'microscopic models',fontsize='10')
            if k == 1:
                models = models2
                axs[0,1].text(0.02,3.5,'phenomenological models',fontsize='10')
            #
            #model_check = []
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
                        print('e2a_lep:',matt.pre_lep)
                        if model in model_check:
                            axs[0,k].plot( matt.den, matt.pre_lep, marker='o', linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                            axs[1,k].plot( matt.den, matt.pre_nuc, marker='o', linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                            axs[2,k].plot( matt.den, matt.pre_tot, marker='o', linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                        else:
                            model_check.append(model)
                            axs[0,k].plot( matt.den, matt.pre_lep, marker='o', linestyle=lstyle, label=model, markevery=matt.every, color=nuda.param.col[kmodel] )
                            axs[1,k].plot( matt.den, matt.pre_nuc, marker='o', linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                            axs[2,k].plot( matt.den, matt.pre_tot, marker='o', linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                # end of param
            # end of model
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

def eos_setupAMi_cs2_fig( pname, models1, models2, band ):
    """
    Plot the nucleon, lepton and total (nucleon+leptonic) contribution to the square of the sound speed in asymmetric matter.
    
    The plot is 2x3 with:

    [0,0]: microscopic models (nucleon).  [0,1]: phenomenologic models (nucleon).

    [1,0]: microscopic models (lepton).   [1,1]: phenomenologic models (lepton).

    [2,0]: microscopic models (total).    [2,1]: phenomenologic models (total).

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
    model_check = []
    #
    for asy in asys:
        #
        print('asy:',asy)
        #
        for k in range(2):
            #
            if k == 0:
                models = models1
                axs[0,0].text(0.02,0.45,'microscopic models',fontsize='10')
            if k == 1:
                models = models2
                axs[0,1].text(0.02,0.45,'phenomenological models',fontsize='10')
            #
            #model_check = []
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
                        print('e2a_lep:',matt.pre_lep)
                        if model in model_check:
                            axs[0,k].plot( matt.den, matt.cs2_lep, marker='o', linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                            axs[1,k].plot( matt.den, matt.cs2_nuc, marker='o', linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                            axs[2,k].plot( matt.den, matt.cs2_tot, marker='o', linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                        else:
                            model_check.append(model)
                            axs[0,k].plot( matt.den, matt.cs2_lep, marker='o', linestyle=lstyle, label=model, markevery=matt.every, color=nuda.param.col[kmodel] )
                            axs[1,k].plot( matt.den, matt.cs2_nuc, marker='o', linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                            axs[2,k].plot( matt.den, matt.cs2_tot, marker='o', linestyle=lstyle, markevery=matt.every, color=nuda.param.col[kmodel] )
                # end of param
            # end of model
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