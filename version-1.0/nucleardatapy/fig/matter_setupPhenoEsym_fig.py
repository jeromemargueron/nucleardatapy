import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda


def matter_setupPhenoEsym_fig(pname, models, band):
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
    print(f"Plot name: {pname}")
    #
    fig, axs = plt.subplots(2, 2)
    fig.tight_layout()  # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust( left=0.12, bottom=0.12, right=0.95, top=0.9, wspace=0.05, hspace=0.05 )
    #
    axs[0, 0].set_ylabel(r"$E_\mathrm{sym}$ (MeV)")
    axs[0, 0].set_xlim([0, 0.33])
    axs[0, 0].set_ylim([0, 50])
    axs[0, 0].tick_params("x", labelbottom=False)
    #
    axs[0, 1].set_xlim([0.5, 2.0])
    axs[0, 1].set_ylim([0, 50])
    axs[0, 1].tick_params("x", labelbottom=False)
    axs[0, 1].tick_params("y", labelleft=False)
    #
    axs[1, 0].set_ylabel(r"$E_\mathrm{sym}/E_\mathrm{sym, FFG}$")
    axs[1, 0].set_xlabel(r"$n_\mathrm{nuc}$ (fm$^{-3}$)")
    axs[1, 0].set_xlim([0, 0.33])
    axs[1, 0].set_ylim([1, 3.6])
    #
    axs[1, 1].set_xlabel(r"$k_F$ (fm$^{-1}$)")
    axs[1, 1].set_xlim([0.5, 2.0])
    axs[1, 1].set_ylim([1, 3.6])
    axs[1, 1].tick_params("y", labelleft=False)
    #
    for model in models:
        #
        params, params_lower = nuda.matter.pheno_params(model=model)
        #
        for param in params:
            #
            print("in Sample: model, param", model, param)
            pheno = nuda.matter.setupPhenoEsym(model=model, param=param)
            if nuda.env.verb_output:
                pheno.print_outputs()
            #
            check = nuda.matter.setupCheck(eos=pheno, band=band)
            #
            if check.isInside:
                lstyle = "solid"
            else:
                lstyle = "dashed"
            #
            # print("esym:",pheno.esym)
            # print("den:",pheno.den)
            if pheno.esym is not None:
                print("esym_err:", pheno.esym_err)
                if pheno.esym_err is None:
                    if check.isInside:
                        axs[0, 0].plot(
                            pheno.den,
                            pheno.esym,
                            marker=pheno.marker,
                            linestyle=lstyle,
                            label=pheno.label,
                        )
                    else:
                        axs[0, 0].plot(
                            pheno.den, pheno.esym, marker=pheno.marker, linestyle=lstyle
                        )
                    axs[0, 1].plot(
                        pheno.kf, pheno.esym, marker=pheno.marker, linestyle=lstyle
                    )
                    axs[1, 0].plot(
                        pheno.den,
                        pheno.esym / nuda.esymffg_nr(pheno.kf),
                        marker=pheno.marker,
                        linestyle=lstyle,
                    )
                    axs[1, 1].plot(
                        pheno.kf,
                        pheno.esym / nuda.esymffg_nr(pheno.kf),
                        marker=pheno.marker,
                        linestyle=lstyle,
                    )
                else:
                    axs[0, 0].errorbar(
                        pheno.den,
                        pheno.esym,
                        yerr=pheno.esym_err,
                        marker=pheno.marker,
                        linestyle=lstyle,
                        errorevery=pheno.every,
                        label=pheno.label,
                    )
                    axs[0, 1].errorbar(
                        pheno.kf,
                        pheno.esym,
                        yerr=pheno.esym_err,
                        marker=pheno.marker,
                        linestyle=lstyle,
                        errorevery=pheno.every,
                    )
                    axs[1, 0].errorbar(
                        pheno.den,
                        pheno.esym / nuda.esymffg_nr(pheno.kf),
                        yerr=pheno.esym_err / nuda.esymffg_nr(pheno.kf),
                        marker=pheno.marker,
                        linestyle=lstyle,
                        errorevery=pheno.every,
                    )
                    axs[1, 1].errorbar(
                        pheno.kf,
                        pheno.esym / nuda.esymffg_nr(pheno.kf),
                        yerr=pheno.esym_err / nuda.esymffg_nr(pheno.kf),
                        marker=pheno.marker,
                        linestyle=lstyle,
                        errorevery=pheno.every,
                    )
            #
        axs[0, 0].fill_between(
            band.den,
            y1=(band.e2a - band.e2a_std),
            y2=(band.e2a + band.e2a_std),
            color=band.color,
            alpha=band.alpha,
            visible=True,
        )
        axs[0, 0].plot(
            band.den,
            (band.e2a - band.e2a_std),
            color="k",
            linestyle="dashed",
            visible=True, zorder = 100
        )
        axs[0, 0].plot(
            band.den,
            (band.e2a + band.e2a_std),
            color="k",
            linestyle="dashed",
            visible=True, zorder = 100
        )
        axs[0, 1].fill_between(
            band.kfn,
            y1=(band.e2a - band.e2a_std),
            y2=(band.e2a + band.e2a_std),
            color=band.color,
            alpha=band.alpha,
            visible=True,
        )
        axs[0, 1].plot(
            band.kfn,
            (band.e2a - band.e2a_std),
            color="k",
            linestyle="dashed",
            visible=True, zorder = 100
        )
        axs[0, 1].plot(
            band.kfn,
            (band.e2a + band.e2a_std),
            color="k",
            linestyle="dashed",
            visible=True, zorder = 100
        )
        axs[1, 0].fill_between(
            band.den,
            y1=(band.e2a - band.e2a_std) / nuda.esymffg_nr(band.kfn),
            y2=(band.e2a + band.e2a_std) / nuda.esymffg_nr(band.kfn),
            color=band.color,
            alpha=band.alpha,
            visible=True,
        )
        axs[1, 0].plot(
            band.den,
            (band.e2a - band.e2a_std) / nuda.esymffg_nr(band.kfn),
            color="k",
            linestyle="dashed",
            visible=True, zorder = 100
        )
        axs[1, 0].plot(
            band.den,
            (band.e2a + band.e2a_std) / nuda.esymffg_nr(band.kfn),
            color="k",
            linestyle="dashed",
            visible=True, zorder = 100
        )
        axs[1, 1].fill_between(
            band.kf,
            y1=(band.e2a - band.e2a_std) / nuda.esymffg_nr(band.kfn),
            y2=(band.e2a + band.e2a_std) / nuda.esymffg_nr(band.kfn),
            color=band.color,
            alpha=band.alpha,
            visible=True,
        )
        axs[1, 1].plot(
            band.kfn,
            (band.e2a - band.e2a_std) / nuda.esymffg_nr(band.kfn),
            color="k",
            linestyle="dashed",
            visible=True, zorder = 100
        )
        axs[1, 1].plot(
            band.kfn,
            (band.e2a + band.e2a_std) / nuda.esymffg_nr(band.kfn),
            color="k",
            linestyle="dashed",
            visible=True, zorder = 100
        )
    # FFG symmetry energy
    #axs[0, 0].plot(pheno.den, nuda.esymffg_nr(pheno.kf), linestyle="dotted")
    #axs[0, 1].plot(pheno.kf, nuda.esymffg_nr(pheno.kf), linestyle="dotted")

    # axs[1,0].legend(loc='upper right',fontsize='8')
    fig.legend(
        loc="upper left",
        bbox_to_anchor=(0.1, 1.0),
        columnspacing=2,
        fontsize="8",
        ncol=4,
        frameon=False,
    )
    #
    if pname is not None:
        plt.savefig(pname, dpi=300)
        plt.close()
    #
