import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda


def matter_setupMicro_band_fig(pname, models, den, matter):
    """
    Plot the correlation between Esym and Lsym.\
    The plot is 1x1 with:\
    [0]: Esym - Lsym correlation plot

    :param pname: name of the figure (*.png)
    :type pname: str.
    :param constraints: list of constraints to run on.
    :type constraints: array of str.

    """
    #
    print(f"Plot name: {pname}")
    #
    # den = 0.03*np.arange(13)
    #
    fig, axs = plt.subplots(1, 2)
    fig.tight_layout()  # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust( left=0.15, bottom=0.12, right=0.95, top=0.98, wspace=0.38, hspace=0.3 )
    #
    axs[0].set_xlabel(r"$n_\text{nuc}$ (fm$^{-3}$)", fontsize="14")
    axs[0].set_xlim([0, 0.2])
    #
    axs[1].set_xlabel(r"$n_\text{nuc}$ (fm$^{-3}$)", fontsize="14")
    axs[1].set_xlim([0, 0.2])
    #
    if matter.lower() == "nm":
        axs[0].set_ylabel(r"$E_\text{int,NM}$", fontsize="14")
        axs[1].set_ylabel(r"$E_\text{int,NM}/E_\text{int,NM}^\text{NR FFG}$", fontsize="14")
        axs[0].set_ylim([0, 20])
        axs[1].set_ylim([0.2, 0.9])
    elif matter.lower() == "sm":
        axs[0].set_ylabel(r"$E_\text{int,SM}$", fontsize="14")
        axs[1].set_ylabel(r"$E_\text{int,SM}/E_\text{int,SM}^\text{NR FFG}$", fontsize="14")
        axs[0].set_ylim([-20, 0])
        axs[1].set_ylim([-1.0, 0.0])
    elif matter.lower() == "esym":
        axs[0].set_ylabel(r"$E_\text{sym}$", fontsize="14")
        axs[1].set_ylabel(r"$E_\text{sym}/E_\text{sym}^\text{NR FFG}$", fontsize="14")
        axs[0].set_ylim([0, 50])
        axs[1].set_ylim([1.5, 2.8])
    #
    for model in models:
        #
        mic = nuda.matter.setupMicro(model=model)
        if nuda.env.verb_output:
            mic.print_outputs()
        #
        if mic.nm_e2a_int is not None:
            print("model:", model)
            if matter.lower() == "nm":
                axs[0].errorbar(
                    mic.nm_den,
                    mic.nm_e2a_int,
                    yerr=mic.nm_e2a_err,
                    linestyle=mic.linestyle,
                    label=mic.label,
                    errorevery=mic.every,
                )
                axs[1].errorbar(
                    mic.nm_den,
                    mic.nm_e2a_int / nuda.effg_nr(mic.nm_kfn),
                    yerr=mic.nm_e2a_err / nuda.effg_nr(mic.nm_kfn),
                    linestyle=mic.linestyle,
                    label=mic.label,
                    errorevery=mic.every,
                )
            elif matter.lower() == "sm":
                axs[0].errorbar(
                    mic.sm_den,
                    mic.sm_e2a_int,
                    yerr=mic.sm_e2a_err,
                    linestyle=mic.linestyle,
                    label=mic.label,
                    errorevery=mic.every,
                )
                axs[1].errorbar(
                    mic.sm_den,
                    mic.sm_e2a_int / nuda.effg_nr(mic.sm_kfn),
                    yerr=mic.sm_e2a_err / nuda.effg_nr(mic.sm_kfn),
                    linestyle=mic.linestyle,
                    label=mic.label,
                    errorevery=mic.every,
                )
            elif matter.lower() == "esym":
                esym = nuda.matter.setupMicroEsym(model=model)
                axs[0].errorbar(
                    esym.den,
                    esym.esym,
                    yerr=esym.esym_err,
                    linestyle=esym.linestyle,
                    label=esym.label,
                    errorevery=esym.every,
                )
                axs[1].errorbar(
                    esym.den,
                    esym.esym / nuda.esymffg_nr(esym.kf),
                    yerr=esym.esym_err / nuda.esymffg_nr(esym.kf),
                    linestyle=esym.linestyle,
                    label=esym.label,
                    errorevery=esym.every,
                )
    #
    band = nuda.matter.setupMicroBand(models, den=den, matter=matter)
    #
    axs[0].fill_between(
        band.den,
        y1=band.e2a_int - band.e2a_std,
        y2=band.e2a_int + band.e2a_std,
        color=band.color,
        alpha=band.alpha,
    )
    if matter.lower() == "nm":
        axs[1].fill_between(
            band.den,
            y1=(band.e2a_int - band.e2a_std) / nuda.effg_nr(band.kfn),
            y2=(band.e2a_int + band.e2a_std) / nuda.effg_nr(band.kfn),
            color=band.color,
            alpha=band.alpha,
        )
    elif matter.lower() == "sm":
        axs[1].fill_between(
            band.den,
            y1=(band.e2a_int - band.e2a_std) / nuda.effg_nr(band.kf),
            y2=(band.e2a_int + band.e2a_std) / nuda.effg_nr(band.kf),
            color=band.color,
            alpha=band.alpha,
        )
    elif matter.lower() == "esym":
        axs[1].fill_between(
            band.den,
            y1=(band.e2a_int - band.e2a_std) / nuda.esymffg_nr(band.kf),
            y2=(band.e2a_int + band.e2a_std) / nuda.esymffg_nr(band.kf),
            color=band.color,
            alpha=band.alpha,
        )
    #
    if matter.lower() == "nm":
        axs[1].legend(loc="upper left", fontsize="12", ncol=1)
    elif matter.lower() == "sm":
        axs[1].legend(loc="upper left", fontsize="12", ncol=1)
    elif matter.lower() == "esym":
        axs[0].legend(loc="upper left", fontsize="12", ncol=1)
    #
    if pname is not None:
        plt.savefig(pname, dpi=200)
        plt.close()
