import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def matter_setupMicro_gap_1s0_fig(pname, models, matter="NM"):
    """
    Plot the correlation between Esym and Lsym.\
    The plot is 2x2 with:\
    [0,0]: Esym - Lsym correlation plot

    :param pname: name of the figure (*.png)
    :type pname: str.
    :param constraints: list of constraints to run on.
    :type constraints: array of str.

    """
    #
    print(f"Plot name: {pname}")
    #
    print("models:", models)
    #
    fig, axs = plt.subplots(2, 2)
    fig.subplots_adjust( left=0.12, bottom=0.12, right=0.95, top=0.85, wspace=0.05, hspace=0.05 )
    #
    axs[0,0].set_ylabel(r"$\Delta_{1S0}$ (MeV)", fontsize="14")
    axs[0,0].set_xlim([0, 0.09])
    axs[0,0].set_ylim([0, 3.0])
    axs[0,0].tick_params("x", labelbottom=False)
    #
    axs[0,1].set_xlim([0, 1.6])
    axs[0,1].set_ylim([0, 3.0])
    axs[0,1].tick_params("x", labelbottom=False)
    axs[0,1].tick_params("y", labelleft=False)
    #
    axs[1,0].set_ylabel(r"$\Delta_{1S0}/E_F$", fontsize="14")
    axs[1,0].set_xlabel(r"$n_\text{nuc}$ (fm$^{-3}$)", fontsize="14")
    axs[1,0].set_xlim([0, 0.09])
    axs[1,0].set_ylim([0, 0.65])
    #
    axs[1,1].set_xlabel(r"$k_{F}$ (fm$^{-1}$)", fontsize="14")
    axs[1,1].set_xlim([0, 1.6])
    axs[1,1].set_ylim([0, 0.65])
    axs[1,1].tick_params("y", labelleft=False)
    #
    for model in models:
        #
        gap = nuda.matter.setupMicroGap(model=model, matter=matter)
        #
        if matter.lower() == "nm":
            if gap.nm_gap_1s0 is not None:
                if gap.nm_gap_1s0_err is not None:
                    axs[0, 0].errorbar(gap.nm_den_1s0, gap.nm_gap_1s0, yerr=gap.nm_gap_1s0_err,
                        marker=gap.marker, markevery=gap.every, linestyle=gap.lstyle, label=gap.label )
                    axs[0, 1].errorbar(gap.nm_kfn_1s0, gap.nm_gap_1s0, yerr=gap.nm_gap_1s0_err,
                        marker=gap.marker, markevery=gap.every, linestyle=gap.lstyle )
                    axs[1, 0].errorbar(gap.nm_den_1s0, gap.nm_gap_1s0 / nuda.eF_n(gap.nm_kfn_1s0), yerr=gap.nm_gap_1s0_err / nuda.eF_n(gap.nm_kfn_1s0),
                        marker=gap.marker, markevery=gap.every, linestyle=gap.lstyle )
                    axs[1, 1].errorbar(gap.nm_kfn_1s0, gap.nm_gap_1s0 / nuda.eF_n(gap.nm_kfn_1s0), yerr=gap.nm_gap_1s0_err / nuda.eF_n(gap.nm_kfn_1s0),
                        marker=gap.marker, markevery=gap.every, linestyle=gap.lstyle )
                else:
                    axs[0, 0].plot(gap.nm_den_1s0, gap.nm_gap_1s0,
                        marker=gap.marker, markevery=gap.every, linestyle=gap.lstyle, label=gap.label)
                    axs[0, 1].plot(gap.nm_kfn_1s0, gap.nm_gap_1s0,
                        marker=gap.marker, markevery=gap.every, linestyle=gap.lstyle )
                    axs[1, 0].plot(gap.nm_den_1s0, gap.nm_gap_1s0 / nuda.eF_n(gap.nm_kfn_1s0),
                        marker=gap.marker, markevery=gap.every, linestyle=gap.lstyle )
                    axs[1, 1].plot(gap.nm_kfn_1s0, gap.nm_gap_1s0 / nuda.eF_n(gap.nm_kfn_1s0),
                        marker=gap.marker, markevery=gap.every, linestyle=gap.lstyle )
        elif matter.lower() == "sm":
            if gap.sm_gap_1s0 is not None:
                if gap.sm_gap_1s0_err is not None:
                    axs[0, 0].errorbar(gap.sm_den_1s0, gap.sm_gap_1s0, yerr=gap.sm_gap_1s0_err,
                        marker=gap.marker, markevery=gap.every, linestyle=gap.lstyle, label=gap.label )
                    axs[0, 1].errorbar(gap.sm_kfn_1s0, gap.sm_gap_1s0, yerr=gap.sm_gap_1s0_err,
                        marker=gap.marker, markevery=gap.every, linestyle=gap.lstyle )
                    axs[1, 0].errorbar(gap.sm_den_1s0, gap.sm_gap_1s0 / (2*nuda.eF_n(gap.sm_kfn_1s0)), yerr=gap.sm_gap_1s0_err / nuda.eF_n(gap.sm_kfn_1s0),
                        marker=gap.marker, markevery=gap.every, linestyle=gap.lstyle )
                    axs[1, 1].errorbar(gap.sm_kfn_1s0, gap.sm_gap_1s0 / (2*nuda.eF_n(gap.sm_kfn_1s0)), yerr=gap.sm_gap_1s0_err / nuda.eF_n(gap.sm_kfn_1s0),
                        marker=gap.marker, markevery=gap.every, linestyle=gap.lstyle )
                else:
                    axs[0, 0].plot(gap.sm_den_1s0, gap.sm_gap_1s0,
                        marker=gap.marker, markevery=gap.every, linestyle=gap.lstyle, label=gap.label )
                    axs[0, 1].plot(gap.sm_kfn_1s0, gap.sm_gap_1s0,
                        marker=gap.marker, markevery=gap.every, linestyle=gap.lstyle )
                    axs[1, 0].plot(gap.sm_den_1s0, gap.sm_gap_1s0 / (2*nuda.eF_n(gap.sm_kfn_1s0)),
                        marker=gap.marker, markevery=gap.every, linestyle=gap.lstyle )
                    axs[1, 1].plot(gap.sm_kfn_1s0, gap.sm_gap_1s0 / (2*nuda.eF_n(gap.sm_kfn_1s0)),
                        marker=gap.marker, markevery=gap.every, linestyle=gap.lstyle )
        if nuda.env.verb_output:
            gap.print_outputs()
    #
    # axs[1,0].legend(loc='upper right',fontsize='8')
    fig.legend(loc="upper left", bbox_to_anchor=(0.1, 1.0), columnspacing=2, fontsize="8", ncol=3, frameon=False )
    #
    if pname is not None:
        plt.savefig(pname, dpi=300)
        plt.close()


def matter_setupMicro_gap_3pf2_fig(pname, models, matter="NM"):
    """
    Plot the correlation between Esym and Lsym.\
    The plot is 2x2 with:\
    [0,0]: Esym - Lsym correlation plot

    :param pname: name of the figure (*.png)
    :type pname: str.
    :param constraints: list of constraints to run on.
    :type constraints: array of str.

    """
    #
    print(f"Plot name: {pname}")
    #
    # plot 3PF2 pairing gap in NM
    print("models:", models)
    #
    fig, axs = plt.subplots(2, 2)
    fig.tight_layout()  # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=0.95, top=0.85, wspace=0.05, hspace=0.05 )
    #
    axs[0, 0].set_ylabel(r"$\Delta_{3PF2}$ (MeV)", fontsize="14")
    axs[0, 0].set_xlim([0, 0.38])
    axs[0, 0].set_ylim([0, 0.6])
    axs[0, 0].tick_params("x", labelbottom=False)
    #
    axs[0, 1].set_xlim([0.6, 2.3])
    axs[0, 1].set_ylim([0, 0.6])
    axs[0, 1].tick_params("x", labelbottom=False)
    axs[0, 1].tick_params("y", labelleft=False)
    #
    axs[1, 0].set_ylabel(r"$100\times \Delta_{3PF2}/E_F$", fontsize="14")
    axs[1, 0].set_xlabel(r"$n_\text{nuc}$ (fm$^{-3}$)", fontsize="14")
    axs[1, 0].set_xlim([0, 0.38])
    axs[1, 0].set_ylim([0, 0.78])
    #
    axs[1, 1].set_xlabel(r"$k_{F}$ (fm$^{-1}$)", fontsize="14")
    axs[1, 1].set_xlim([0.6, 2.3])
    axs[1, 1].set_ylim([0, 0.78])
    axs[1, 1].tick_params("y", labelleft=False)
    #
    for model in models:
        #
        gap = nuda.matter.setupMicroGap(model=model, matter=matter)
        #
        if matter.lower() == "nm":
            if gap.nm_gap_3pf2 is not None:
                if gap.nm_gap_3pf2_err is not None:
                    axs[0, 0].errorbar(
                        gap.nm_den_3pf2,
                        gap.nm_gap_3pf2,
                        yerr=gap.nm_gap_3pf2_err,
                        marker=gap.marker,
                        markevery=gap.every,
                        linestyle=gap.lstyle,
                        label=gap.label,
                    )
                    axs[0, 1].errorbar(
                        gap.nm_kfn_3pf2,
                        gap.nm_gap_3pf2,
                        yerr=gap.nm_gap_3pf2_err,
                        marker=gap.marker,
                        markevery=gap.every,
                        linestyle=gap.lstyle,
                    )
                    axs[1, 0].errorbar(
                        gap.nm_den_3pf2,
                        100 * gap.nm_gap_3pf2 / nuda.eF_n(gap.nm_kfn_3pf2),
                        yerr=gap.nm_gap_3pf2_err / nuda.eF_n(gap.nm_kfn_3pf2),
                        marker=gap.marker,
                        markevery=gap.every,
                        linestyle=gap.lstyle,
                    )
                    axs[1, 1].errorbar(
                        gap.nm_kfn_3pf2,
                        100 * gap.nm_gap_3pf2 / nuda.eF_n(gap.nm_kfn_3pf2),
                        yerr=gap.nm_gap_3pf2_err / nuda.eF_n(gap.nm_kfn_3pf2),
                        marker=gap.marker,
                        markevery=gap.every,
                        linestyle=gap.lstyle,
                    )
                else:
                    axs[0, 0].plot(
                        gap.nm_den_3pf2,
                        gap.nm_gap_3pf2,
                        marker=gap.marker,
                        markevery=gap.every,
                        linestyle=gap.lstyle,
                        label=gap.label,
                    )
                    axs[0, 1].plot(
                        gap.nm_kfn_3pf2,
                        gap.nm_gap_3pf2,
                        marker=gap.marker,
                        markevery=gap.every,
                        linestyle=gap.lstyle,
                    )
                    axs[1, 0].plot(
                        gap.nm_den_3pf2,
                        100 * gap.nm_gap_3pf2 / nuda.eF_n(gap.nm_kfn_3pf2),
                        marker=gap.marker,
                        markevery=gap.every,
                        linestyle=gap.lstyle,
                    )
                    axs[1, 1].plot(
                        gap.nm_kfn_3pf2,
                        100 * gap.nm_gap_3pf2 / nuda.eF_n(gap.nm_kfn_3pf2),
                        marker=gap.marker,
                        markevery=gap.every,
                        linestyle=gap.lstyle,
                    )
        elif matter.lower() == "sm":
            if gap.sm_gap_3pf2 is not None:
                if gap.sm_gap_3pf2_err is not None:
                    axs[0, 0].errorbar(
                        gap.sm_den_3pf2,
                        gap.sm_gap_3pf2,
                        yerr=gap.sm_gap_3pf2_err,
                        marker=gap.marker,
                        markevery=gap.every,
                        linestyle=gap.lstyle,
                        label=gap.label,
                    )
                    axs[0, 1].errorbar(
                        gap.sm_kfn_3pf2,
                        gap.sm_gap_3pf2,
                        yerr=gap.sm_gap_3pf2_err,
                        marker=gap.marker,
                        markevery=gap.every,
                        linestyle=gap.lstyle,
                    )
                    axs[1, 0].errorbar(
                        gap.sm_den_3pf2,
                        100 * gap.sm_gap_3pf2 / (2*nuda.eF_n(gap.sm_kfn_3pf2)),
                        yerr=gap.sm_gap_3pf2_err / (2*nuda.eF_n(gap.sm_kfn_3pf2)),
                        marker=gap.marker,
                        markevery=gap.every,
                        linestyle=gap.lstyle,
                    )
                    axs[1, 1].errorbar(
                        gap.sm_kfn_3pf2,
                        100 * gap.sm_gap_3pf2 / (2*nuda.eF_n(gap.sm_kfn_3pf2)),
                        yerr=gap.sm_gap_3pf2_err / (2*nuda.eF_n(gap.sm_kfn_3pf2)),
                        marker=gap.marker,
                        markevery=gap.every,
                        linestyle=gap.lstyle,
                    )
                else:
                    axs[0, 0].plot(
                        gap.sm_den_3pf2,
                        gap.sm_gap_3pf2,
                        marker=gap.marker,
                        markevery=gap.every,
                        linestyle=gap.lstyle,
                        label=gap.label,
                    )
                    axs[0, 1].plot(
                        gap.sm_kfn_3pf2,
                        gap.sm_gap_3pf2,
                        marker=gap.marker,
                        markevery=gap.every,
                        linestyle=gap.lstyle,
                    )
                    axs[1, 0].plot(
                        gap.sm_den_3pf2,
                        100 * gap.sm_gap_3pf2 / (2*nuda.eF_n(gap.sm_kfn_3pf2)),
                        marker=gap.marker,
                        markevery=gap.every,
                        linestyle=gap.lstyle,
                    )
                    axs[1, 1].plot(
                        gap.sm_kfn_3pf2,
                        100 * gap.sm_gap_3pf2 / (2*nuda.eF_n(gap.sm_kfn_3pf2)),
                        marker=gap.marker,
                        markevery=gap.every,
                        linestyle=gap.lstyle,
                    )
        if nuda.env.verb_output:
            gap.print_outputs()
    #
    # axs[1,0].legend(loc='upper right',fontsize='8')
    fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.95), columnspacing=2, fontsize="8", ncol=3, frameon=False )
    #
    if pname is not None:
        plt.savefig(pname, dpi=300)
        plt.close()
    #
