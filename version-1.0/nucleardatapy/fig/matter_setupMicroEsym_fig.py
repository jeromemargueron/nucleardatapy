import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda


def matter_setupMicroEsym_fig(pname, mbs, band):
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
    axs[0, 0].set_ylabel(r"$E_\mathrm{sym}$ (MeV)", fontsize="14")
    axs[0, 0].set_xlim([0, 0.33])
    axs[0, 0].set_ylim([0, 50])
    axs[0, 0].tick_params("x", labelbottom=False)
    #
    axs[0, 1].set_xlim([0.5, 2.0])
    axs[0, 1].set_ylim([0, 50])
    axs[0, 1].tick_params("x", labelbottom=False)
    axs[0, 1].tick_params("y", labelleft=False)
    #
    axs[1, 0].set_ylabel(r"$E_\mathrm{sym}/E_\mathrm{sym, FFG, NR}$", fontsize="14")
    axs[1, 0].set_xlabel(r"$n_\mathrm{nuc}$ (fm$^{-3}$)", fontsize="14")
    axs[1, 0].set_xlim([0,   0.33])
    axs[1, 0].set_ylim([1.5, 3.6])
    #
    axs[1, 1].set_xlabel(r"$k_F$ (fm$^{-1}$)", fontsize="14")
    axs[1, 1].set_xlim([0.5, 2.0])
    axs[1, 1].set_ylim([1.5, 3.6])
    axs[1, 1].tick_params("y", labelleft=False)
    #
    mb_check = []
    #
    for kmb, mb in enumerate(mbs):
        #
        models, models_lower = nuda.matter.micro_models_mb(mb)
        #
        for model in models:
            #
            print("in Sample: model", model)
            #
            micro = nuda.matter.setupMicroEsym(model=model)
            if nuda.env.verb:
                micro.print_outputs()
            #
            micro = nuda.matter.setupMicroEsym(model=model)
            if nuda.env.verb_output:
                micro.print_outputs()
            #
            check = nuda.matter.setupCheck(eos=micro, band=band)
            #
            if check.isInside:
                lstyle = "solid"
            else:
                lstyle = "dashed"
            #
            if micro.esym is not None:
                # if '2024-BHF' in model and (kmb % 4 != 0.0): continue
                if mb in mb_check:
                    if micro.esym_err is None:
                        axs[0, 0].plot(
                            micro.den,
                            micro.esym,
                            marker=micro.marker,
                            markevery=micro.every,
                            linestyle=lstyle,
                            color=nuda.param.col[kmb],
                        )
                        axs[0, 1].plot(
                            micro.kf,
                            micro.esym,
                            marker=micro.marker,
                            markevery=micro.every,
                            linestyle=lstyle,
                            color=nuda.param.col[kmb],
                        )
                        axs[1, 0].plot(
                            micro.den,
                            micro.esym / nuda.esymffg_nr(micro.kf),
                            marker=micro.marker,
                            markevery=micro.every,
                            linestyle=lstyle,
                            color=nuda.param.col[kmb],
                        )
                        axs[1, 1].plot(
                            micro.kf,
                            micro.esym / nuda.esymffg_nr(micro.kf),
                            marker=micro.marker,
                            markevery=micro.every,
                            linestyle=lstyle,
                            color=nuda.param.col[kmb],
                        )
                    else:
                        axs[0, 0].errorbar(
                            micro.den,
                            micro.esym,
                            yerr=micro.esym_err,
                            marker=micro.marker,
                            markevery=micro.every,
                            linestyle=lstyle,
                            errorevery=micro.every,
                            color=nuda.param.col[kmb],
                        )
                        axs[0, 1].errorbar(
                            micro.kf,
                            micro.esym,
                            yerr=micro.esym_err,
                            marker=micro.marker,
                            markevery=micro.every,
                            linestyle=lstyle,
                            errorevery=micro.every,
                            color=nuda.param.col[kmb],
                        )
                        axs[1, 0].errorbar(
                            micro.den,
                            micro.esym / nuda.esymffg_nr(micro.kf),
                            yerr=micro.esym_err / nuda.esymffg_nr(micro.kf),
                            marker=micro.marker,
                            markevery=micro.every,
                            linestyle=lstyle,
                            errorevery=micro.every,
                            color=nuda.param.col[kmb],
                        )
                        axs[1, 1].errorbar(
                            micro.kf,
                            micro.esym / nuda.esymffg_nr(micro.kf),
                            yerr=micro.esym_err / nuda.esymffg_nr(micro.kf),
                            marker=micro.marker,
                            markevery=micro.every,
                            linestyle=lstyle,
                            errorevery=micro.every,
                            color=nuda.param.col[kmb],
                        )
                else:
                    mb_check.append(mb)
                    if micro.esym_err is None:
                        axs[0, 0].plot(
                            micro.den,
                            micro.esym,
                            marker=micro.marker,
                            markevery=micro.every,
                            linestyle=lstyle,
                            color=nuda.param.col[kmb],
                            label=mb,
                        )
                        axs[0, 1].plot(
                            micro.kf,
                            micro.esym,
                            marker=micro.marker,
                            markevery=micro.every,
                            linestyle=lstyle,
                            color=nuda.param.col[kmb],
                        )
                        axs[1, 0].plot(
                            micro.den,
                            micro.esym / nuda.esymffg_nr(micro.kf),
                            marker=micro.marker,
                            markevery=micro.every,
                            linestyle=lstyle,
                            color=nuda.param.col[kmb],
                        )
                        axs[1, 1].plot(
                            micro.kf,
                            micro.esym / nuda.esymffg_nr(micro.kf),
                            marker=micro.marker,
                            markevery=micro.every,
                            linestyle=lstyle,
                            color=nuda.param.col[kmb],
                        )
                    else:
                        axs[0, 0].errorbar(
                            micro.den,
                            micro.esym,
                            yerr=micro.esym_err,
                            marker=micro.marker,
                            markevery=micro.every,
                            linestyle=lstyle,
                            errorevery=micro.every,
                            color=nuda.param.col[kmb],
                            label=mb,
                        )
                        axs[0, 1].errorbar(
                            micro.kf,
                            micro.esym,
                            yerr=micro.esym_err,
                            marker=micro.marker,
                            markevery=micro.every,
                            linestyle=lstyle,
                            errorevery=micro.every,
                            color=nuda.param.col[kmb],
                        )
                        axs[1, 0].errorbar(
                            micro.den,
                            micro.esym / nuda.esymffg_nr(micro.kf),
                            yerr=micro.esym_err / nuda.esymffg_nr(micro.kf),
                            marker=micro.marker,
                            markevery=micro.every,
                            linestyle=lstyle,
                            errorevery=micro.every,
                            color=nuda.param.col[kmb],
                        )
                        axs[1, 1].errorbar(
                            micro.kf,
                            micro.esym / nuda.esymffg_nr(micro.kf),
                            yerr=micro.esym_err / nuda.esymffg_nr(micro.kf),
                            marker=micro.marker,
                            markevery=micro.every,
                            linestyle=lstyle,
                            errorevery=micro.every,
                            color=nuda.param.col[kmb],
                        )

    # FFG symmetry energy
    #axs[0, 0].plot(micro.den, nuda.esymffg_nr(micro.kf), linestyle="dotted")
    #axs[0, 1].plot(micro.kf, nuda.esymffg_nr(micro.kf), linestyle="dotted")

    axs[0, 0].fill_between(
        band.den,
        y1=(band.e2a - band.e2a_std),
        y2=(band.e2a + band.e2a_std),
        color=band.color,
        alpha=band.alpha,
        visible=True,
    )
    axs[0, 0].plot(
        band.den, (band.e2a - band.e2a_std), color="k", linestyle="dashed", visible=True, zorder = 100 )
    axs[0, 0].plot(
        band.den, (band.e2a + band.e2a_std), color="k", linestyle="dashed", visible=True, zorder = 100 )
    axs[0, 1].fill_between(
        band.kfn,
        y1=(band.e2a - band.e2a_std),
        y2=(band.e2a + band.e2a_std),
        color=band.color,
        alpha=band.alpha,
        visible=True,
    )
    axs[0, 1].plot(
        band.kfn, (band.e2a - band.e2a_std), color="k", linestyle="dashed", visible=True, zorder = 100 )
    axs[0, 1].plot(
        band.kfn, (band.e2a + band.e2a_std), color="k", linestyle="dashed", visible=True, zorder = 100 )
    axs[1, 0].fill_between(
        band.den,
        y1=(band.e2a - band.e2a_std) / nuda.esymffg_nr(band.kf),
        y2=(band.e2a + band.e2a_std) / nuda.esymffg_nr(band.kf),
        color=band.color,
        alpha=band.alpha,
        visible=True,
    )
    axs[1, 0].plot(
        band.den, (band.e2a - band.e2a_std) / nuda.esymffg_nr(band.kf),
        color="k", linestyle="dashed", visible=True, zorder = 100 )
    axs[1, 0].plot(
        band.den, (band.e2a + band.e2a_std) / nuda.esymffg_nr(band.kf),
        color="k", linestyle="dashed", visible=True, zorder = 100 )
    axs[1, 1].fill_between(
        band.kfn,
        y1=(band.e2a - band.e2a_std) / nuda.esymffg_nr(band.kf),
        y2=(band.e2a + band.e2a_std) / nuda.esymffg_nr(band.kf),
        color=band.color,
        alpha=band.alpha,
        visible=True,
    )
    axs[1, 1].plot(
        band.kfn, (band.e2a - band.e2a_std) / nuda.esymffg_nr(band.kf),
        color="k", linestyle="dashed", visible=True, zorder = 100 )
    axs[1, 1].plot(
        band.kfn, (band.e2a + band.e2a_std) / nuda.esymffg_nr(band.kf),
        color="k", linestyle="dashed", visible=True, zorder = 100 )

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