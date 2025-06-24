import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda


def matter_setupPheno_e2a_fig(pname, model, band):
    """
    Plot nucleonic energy per particle E/A in matter.\
    The plot is 2x2 with:\
    [0,0]: E/A versus den.       [0,1]: E/A versus kfn.\
    [1,0]: E/E_NRFFG versus den. [1,1]: E/E_NRFFG versus kfn.\

    :param pname: name of the figure (*.png)
    :type pname: str.
    :param model: class of model considered.
    :type model: str.
    :param band: object instantiated on the reference band.
    :type band: object.
    :param matter: can be 'SM' or 'NM'.
    :type matter: str.

    """
    #
    print(f"Plot name: {pname}")
    matter = band.matter
    #
    # plot
    #
    fig, axs = plt.subplots(2, 2)
    fig.tight_layout()  # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust( left=0.15, bottom=0.12, right=0.95, top=0.85, wspace=0.05, hspace=0.05 )
    #
    axs[1, 0].set_xlabel(r"$n_\text{nuc}$ (fm$^{-3}$)", fontsize="14")
    axs[1, 1].set_xlabel(r"$k_{F}$ (fm$^{-1}$)", fontsize="14")
    axs[0, 0].set_xlim([0, 0.33])
    axs[1, 0].set_xlim([0, 0.33])
    axs[0, 1].set_xlim([0.5, 1.9])
    axs[1, 1].set_xlim([0.5, 1.9])
    #
    axs[0, 0].tick_params("x", labelbottom=False)
    axs[0, 1].tick_params("x", labelbottom=False)
    axs[0, 1].tick_params("y", labelleft=False)
    axs[1, 1].tick_params("y", labelleft=False)
    #
    if matter.lower() == "nm":
        axs[0, 0].set_ylabel(r"$E_\text{int,NM}/A$ (MeV)", fontsize="14")
        axs[1, 0].set_ylabel(r"$E_\text{int,NM}/E_\text{int,NM}^\text{NR FFG}$", fontsize="14")
        axs[0, 0].set_ylim([0, 30])
        axs[0, 1].set_ylim([0, 30])
        axs[1, 0].set_ylim([0.2, 0.84])
        axs[1, 1].set_ylim([0.2, 0.84])
    elif matter.lower() == "sm":
        axs[0, 0].set_ylabel(r"$E_\text{int,SM}/A$ (MeV)", fontsize="14")
        axs[1, 0].set_ylabel(r"$E_\text{int,SM}/E_\text{int,SM}^\text{NR FFG}$", fontsize="14")
        axs[0, 0].set_ylim([-20, 10])
        axs[0, 1].set_ylim([-20, 10])
        axs[1, 0].set_ylim([-2.0, 0.1])
        axs[1, 1].set_ylim([-2.0, 0.1])
    #
    params, params_lower = nuda.matter.pheno_params(model=model)
    #
    for param in params:
        #
        pheno = nuda.matter.setupPheno(model=model, param=param)
        #
        check = nuda.matter.setupCheck(eos=pheno, band=band)
        #
        if check.isInside:
            lstyle = "solid"
        else:
            lstyle = "dashed"
        #
        if matter.lower() == "nm":
            #
            if any(pheno.nm_e2a):
                if model == "Skyrme" and check.isInside:
                    axs[0, 0].plot( pheno.nm_den, pheno.nm_e2a_int, linestyle=lstyle, label=pheno.label )
                elif model == "Skyrme" and check.isOutside:
                    axs[0, 0].plot(pheno.nm_den, pheno.nm_e2a_int, linestyle=lstyle)
                else:
                    axs[0, 0].plot( pheno.nm_den, pheno.nm_e2a_int, linestyle=lstyle, label=pheno.label )
                axs[0, 1].plot(pheno.nm_kfn, pheno.nm_e2a_int, linestyle=lstyle)
                axs[1, 0].plot(
                    pheno.nm_den,
                    pheno.nm_e2a_int / nuda.effg_nr(pheno.nm_kfn),
                    linestyle=lstyle,
                )
                axs[1, 1].plot(
                    pheno.nm_kfn,
                    pheno.nm_e2a_int / nuda.effg_nr(pheno.nm_kfn),
                    linestyle=lstyle,
                )
            #
        elif matter.lower() == "sm":
            #
            if any(pheno.sm_e2a):
                if model == "Skyrme" and check.isInside:
                    axs[0, 0].plot( pheno.sm_den, pheno.sm_e2a_int, linestyle=lstyle, label=pheno.label )
                elif model == "Skyrme" and check.isOutside:
                    axs[0, 0].plot( pheno.sm_den, pheno.sm_e2a_int, linestyle=lstyle)
                else:
                    axs[0, 0].plot( pheno.sm_den, pheno.sm_e2a_int, linestyle=lstyle, label=pheno.label )
                axs[0, 1].plot(pheno.sm_kf, pheno.sm_e2a_int, linestyle=lstyle)
                axs[1, 0].plot(
                    pheno.sm_den,
                    pheno.sm_e2a_int / nuda.effg_nr(pheno.sm_kf),
                    linestyle=lstyle,
                )
                axs[1, 1].plot(
                    pheno.sm_kf,
                    pheno.sm_e2a_int / nuda.effg_nr(pheno.sm_kf),
                    linestyle=lstyle,
                )
        if nuda.env.verb_output:
            pheno.print_outputs()
    if matter.lower() == "nm":
        axs[0, 0].fill_between(
            band.den,
            y1=(band.e2a_int - band.e2a_std),
            y2=(band.e2a_int + band.e2a_std),
            color=band.color,
            alpha=band.alpha,
        )
        axs[0, 0].plot( band.den, (band.e2a_int - band.e2a_std), color="k", linestyle="dashed", zorder = 100 )
        axs[0, 0].plot( band.den, (band.e2a_int + band.e2a_std), color="k", linestyle="dashed", zorder = 100 )
        axs[0, 1].fill_between(
            band.kfn,
            y1=(band.e2a_int - band.e2a_std),
            y2=(band.e2a_int + band.e2a_std),
            color=band.color,
            alpha=band.alpha,
        )
        axs[0, 1].plot( band.kfn, (band.e2a_int - band.e2a_std), color="k", linestyle="dashed", zorder = 100 )
        axs[0, 1].plot( band.kfn, (band.e2a_int + band.e2a_std), color="k", linestyle="dashed", zorder = 100 )
        axs[1, 0].fill_between(
            band.den,
            y1=(band.e2a_int - band.e2a_std) / nuda.effg_nr(band.kfn),
            y2=(band.e2a_int + band.e2a_std) / nuda.effg_nr(band.kfn),
            color=band.color,
            alpha=band.alpha,
        )
        axs[1, 0].plot( band.den, (band.e2a_int - band.e2a_std) / nuda.effg_nr(band.kfn), color="k", linestyle="dashed", zorder = 100 )
        axs[1, 0].plot( band.den, (band.e2a_int + band.e2a_std) / nuda.effg_nr(band.kfn), color="k", linestyle="dashed", zorder = 100 )
        axs[1, 1].fill_between(
            band.kfn,
            y1=(band.e2a_int - band.e2a_std) / nuda.effg_nr(band.kfn),
            y2=(band.e2a_int + band.e2a_std) / nuda.effg_nr(band.kfn),
            color=band.color,
            alpha=band.alpha,
        )
        axs[1, 1].plot( band.kfn, (band.e2a_int - band.e2a_std) / nuda.effg_nr(band.kfn), color="k", linestyle="dashed", zorder = 100 )
        axs[1, 1].plot( band.kfn, (band.e2a_int + band.e2a_std) / nuda.effg_nr(band.kfn), color="k", linestyle="dashed", zorder = 100 )
    elif matter.lower() == "sm":
        axs[0, 0].fill_between(
            band.den,
            y1=(band.e2a_int - band.e2a_std),
            y2=(band.e2a_int + band.e2a_std),
            color=band.color,
            alpha=band.alpha,
            visible=True,
        )
        axs[0, 0].plot( band.den, (band.e2a_int - band.e2a_std), color="k", linestyle="dashed", zorder = 100 )
        axs[0, 0].plot( band.den, (band.e2a_int + band.e2a_std), color="k", linestyle="dashed", zorder = 100 )
        axs[0, 1].fill_between(
            band.kfn,
            y1=(band.e2a_int - band.e2a_std),
            y2=(band.e2a_int + band.e2a_std),
            color=band.color,
            alpha=band.alpha,
            visible=True,
        )
        axs[0, 1].plot(
            band.kfn, (band.e2a_int - band.e2a_std), color="k", linestyle="dashed", zorder = 100
        )
        axs[0, 1].plot(
            band.kfn, (band.e2a_int + band.e2a_std), color="k", linestyle="dashed", zorder = 100
        )
        axs[1, 0].fill_between(
            band.den,
            y1=(band.e2a_int - band.e2a_std) / nuda.effg_nr(band.kfn),
            y2=(band.e2a_int + band.e2a_std) / nuda.effg_nr(band.kfn),
            color=band.color,
            alpha=band.alpha,
            visible=True,
        )
        axs[1, 0].plot(
            band.den, (band.e2a_int - band.e2a_std) / nuda.effg_nr(band.kfn), color="k", linestyle="dashed", zorder = 100
        )
        axs[1, 0].plot(
            band.den, (band.e2a_int + band.e2a_std) / nuda.effg_nr(band.kfn), color="k", linestyle="dashed", zorder = 100
        )
        axs[1, 1].fill_between(
            band.kfn,
            y1=(band.e2a_int - band.e2a_std) / nuda.effg_nr(band.kfn),
            y2=(band.e2a_int + band.e2a_std) / nuda.effg_nr(band.kfn),
            color=band.color,
            alpha=band.alpha,
            visible=True,
        )
        axs[1, 1].plot( band.kfn, (band.e2a_int - band.e2a_std) / nuda.effg_nr(band.kfn), color="k", linestyle="dashed", zorder = 100 )
        axs[1, 1].plot( band.kfn, (band.e2a_int + band.e2a_std) / nuda.effg_nr(band.kfn), color="k", linestyle="dashed", zorder = 100 )
    #
    # if model != 'Skyrme':
    #    axs[0,0].legend(loc='upper right',fontsize='8', ncol=2)
    fig.legend(
        loc="upper left",
        bbox_to_anchor=(0.03, 1.0),
        columnspacing=2,
        fontsize="8",
        ncol=5,
        frameon=False,
    )
    #
    #
    if pname is not None:
        plt.savefig(pname, dpi=300)
        plt.close()
    #

def matter_setupPheno_pre_fig(pname, model, band):
    """
    Plot nucleonic pressure in matter.\
    The plot is 2x2 with:\
    [0,0]: pre versus den.           [0,1]: pre versus kfn.\
    [1,0]: pre/pre_NRFFG versus den. [1,1]: pre/pre_NRFFG versus kfn.\

    :param pname: name of the figure (*.png)
    :type pname: str.
    :param model: class of model considered.
    :type model: str.
    :param band: object instantiated on the reference band.
    :type band: object.
    :param matter: can be 'SM' or 'NM'.
    :type matter: str.

    """
    #
    print(f"Plot name: {pname}")
    matter = band.matter
    #
    # plot
    #
    fig, axs = plt.subplots(2, 2)
    fig.tight_layout()  # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(
        left=0.15, bottom=0.12, right=0.95, top=0.88, wspace=0.05, hspace=0.05
    )
    #
    axs[1, 0].set_xlabel(r"$n_\text{nuc}$ (fm$^{-3}$)", fontsize="14")
    axs[1, 1].set_xlabel(r"$k_{F_n}$ (fm$^{-1}$)", fontsize="14")
    axs[0, 0].set_xlim([0, 0.33])
    axs[1, 0].set_xlim([0, 0.33])
    axs[0, 1].set_xlim([0.5, 1.9])
    axs[1, 1].set_xlim([0.5, 1.9])
    #
    axs[0, 0].tick_params("x", labelbottom=False)
    axs[0, 1].tick_params("x", labelbottom=False)
    axs[0, 1].tick_params("y", labelleft=False)
    axs[1, 1].tick_params("y", labelleft=False)
    #
    if matter.lower() == "nm":
        axs[0, 0].set_ylabel(r"$p_\text{NM}$ (MeV fm$^{-3}$)", fontsize="14")
        axs[1, 0].set_ylabel(r"$p_\text{NM}/p_\text{NRFFG,NM}$", fontsize="14")
        axs[0, 0].set_ylim([-2, 30])
        axs[0, 1].set_ylim([-2, 30])
        axs[1, 0].set_ylim([-0.2, 0.84])
        axs[1, 1].set_ylim([-0.2, 0.84])
    elif matter.lower() == "sm":
        axs[0, 0].set_ylabel(r"$p_\text{SM}$ (MeV fm$^{-3})", fontsize="14")
        axs[1, 0].set_ylabel(r"$p_\text{SM}/p_\text{NRFFG,SM}$", fontsize="14")
        axs[0, 0].set_ylim([-5, 10])
        axs[0, 1].set_ylim([-5, 10])
        axs[1, 0].set_ylim([-1.5, 0.5])
        axs[1, 1].set_ylim([-1.5, 0.5])
    #
    params, params_lower = nuda.matter.pheno_params(model=model)
    #
    for param in params:
        #
        pheno = nuda.matter.setupPheno(model=model, param=param)
        #
        check = nuda.matter.setupCheck(eos=pheno, band=band)
        #
        if check.isInside:
            lstyle = "solid"
        else:
            lstyle = "dashed"
        #
        if matter.lower() == "nm":
            if any(pheno.nm_pre):
                if model == "Skyrme" and check.isInside:
                    axs[0, 0].plot( pheno.nm_den, pheno.nm_pre, linestyle=lstyle, label=pheno.label )
                elif model == "Skyrme" and check.isOutside:
                    axs[0, 0].plot( pheno.nm_den, pheno.nm_pre, linestyle=lstyle )
                else:
                    axs[0, 0].plot( pheno.nm_den, pheno.nm_pre, linestyle=lstyle, label=pheno.label )
                axs[0, 1].plot(pheno.nm_kfn, pheno.nm_pre, linestyle=lstyle)
                axs[1, 0].plot( pheno.nm_den, pheno.nm_pre / nuda.pre_nr(pheno.nm_kfn), linestyle=lstyle )
                axs[1, 1].plot( pheno.nm_kfn, pheno.nm_pre / nuda.pre_nr(pheno.nm_kfn), linestyle=lstyle )
        elif matter.lower() == "sm":
            if any(pheno.sm_pre):
                if model == "Skyrme" and check.isInside:
                    axs[0, 0].plot( pheno.sm_den, pheno.sm_pre, linestyle=lstyle, label=pheno.label )
                elif model == "Skyrme" and check.isOutside:
                    axs[0, 0].plot(pheno.sm_den, pheno.sm_pre, linestyle=lstyle)
                else:
                    axs[0, 0].plot( pheno.sm_den, pheno.sm_pre, linestyle=lstyle, label=pheno.label )
                axs[0, 1].plot( pheno.sm_kf, pheno.sm_pre, linestyle=lstyle )
                axs[1, 0].plot( pheno.sm_den, pheno.sm_pre / nuda.pre_nr(pheno.sm_kf), linestyle=lstyle )
                axs[1, 1].plot( pheno.sm_kf, pheno.sm_pre / nuda.pre_nr(pheno.sm_kf), linestyle=lstyle )
        if nuda.env.verb_output: pheno.print_outputs()
        #
    #
    # if model != 'Skyrme':
    #    axs[0,0].legend(loc='upper right',fontsize='8', ncol=2)
    fig.legend(
        loc="upper left",
        bbox_to_anchor=(0.1, 1.0),
        columnspacing=2,
        fontsize="8",
        ncol=4,
        frameon=False,
    )
    #
    #
    if pname is not None:
        plt.savefig(pname, dpi=300)
        plt.close()
    #

def matter_setupPheno_cs2_fig(pname, model, band):
    """
    Plot nucleonic sound speed in matter.\
    The plot is 1x2 with:\
    [0]: cs2 versus den.    [1]: cs2 versus kfn.\

    :param pname: name of the figure (*.png)
    :type pname: str.
    :param model: class of model considered.
    :type model: str.
    :param band: object instantiated on the reference band.
    :type band: object.
    :param matter: can be 'SM' or 'NM'.
    :type matter: str.

    """
    #
    print(f"Plot name: {pname}")
    matter = band.matter
    #
    # plot
    #
    fig, axs = plt.subplots(1, 2)
    fig.tight_layout()  # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(
        left=0.15, bottom=0.12, right=0.95, top=0.88, wspace=0.05, hspace=0.05
    )
    #
    axs[0].set_xlabel(r"$n_\text{nuc}$ (fm$^{-3}$)", fontsize="14")
    axs[1].set_xlabel(r"$k_{F_n}$ (fm$^{-1}$)", fontsize="14")
    axs[0].set_xlim([0, 0.33])
    axs[1].set_xlim([0.5, 1.9])
    #
    axs[1].tick_params("y", labelleft=False)
    #
    if matter.lower() == "nm":
        axs[0].set_ylabel(r"$c_\text{s,NM}^2/c^2$", fontsize="14")
        axs[0].set_ylim([-0.05, 0.3])
        axs[1].set_ylim([-0.05, 0.3])
    elif matter.lower() == "sm":
        axs[0].set_ylabel(r"$c_\text{s,SM}^2/c^2$", fontsize="14")
        axs[0].set_ylim([-0.05, 0.2])
        axs[1].set_ylim([-0.05, 0.2])
    #
    params, params_lower = nuda.matter.pheno_params(model=model)
    #
    for param in params:
        #
        pheno = nuda.matter.setupPheno(model=model, param=param)
        #
        check = nuda.matter.setupCheck(eos=pheno, band=band)
        #
        if check.isInside:
            lstyle = "solid"
        else:
            lstyle = "dashed"
        #
        if matter.lower() == "nm":
            #
            if any(pheno.nm_cs2):
                #
                if model == "Skyrme" and check.isInside:
                    axs[0].plot( pheno.nm_den[:-1], pheno.nm_cs2[:-1], linestyle=lstyle, label=pheno.label )
                elif model == "Skyrme" and check.isOutside:
                    axs[0].plot( pheno.nm_den[:-1], pheno.nm_cs2[:-1], linestyle=lstyle )
                else:
                    axs[0].plot( pheno.nm_den[:-1], pheno.nm_cs2[:-1], linestyle=lstyle, label=pheno.label )
                axs[1].plot( pheno.nm_kfn[:-1], pheno.nm_cs2[:-1], linestyle=lstyle )
                #
            #
        elif matter.lower() == "sm":
            #
            if any(pheno.sm_pre):
                if model == "Skyrme" and check.isInside:
                    axs[0].plot( pheno.sm_den[:-1], pheno.sm_cs2[:-1], linestyle=lstyle, label=pheno.label )
                elif model == "Skyrme" and check.isOutside:
                    axs[0].plot( pheno.sm_den[:-1], pheno.sm_cs2[:-1], linestyle=lstyle )
                else:
                    axs[0].plot( pheno.sm_den[:-1], pheno.sm_cs2[:-1], linestyle=lstyle, label=pheno.label )
                axs[1].plot( pheno.sm_kf[:-1], pheno.sm_cs2[:-1], linestyle=lstyle )
        if nuda.env.verb_output: pheno.print_outputs()
        #
    #
    fig.legend(
        loc="upper left",
        bbox_to_anchor=(0.1, 1.0),
        columnspacing=2,
        fontsize="8",
        ncol=4,
        frameon=False,
    )
    #
    #
    if pname is not None:
        plt.savefig(pname, dpi=300)
        plt.close()
    #
