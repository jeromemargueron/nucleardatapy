import numpy as np
import matplotlib.pyplot as plt

# plt.rcParams.update({'font.size': 16})
# Set clean font settings
# Set 'DejaVu Sans' as the font
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.family"] = "serif"
plt.rcParams["mathtext.fontset"] = "stixsans"
plt.rcParams["font.serif"] = ["Times New Roman"] + plt.rcParams["font.serif"]

import nucleardatapy as nuda


def matter_setupHIC_fig(pname, inferences):
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
    fig.subplots_adjust( left=0.10, bottom=0.12, right=0.95, top=0.98, wspace=0.25, hspace=0.05 )
    #
    # axs[0,0].set_xlabel(r'$n$ (fm$^{-3}$)',fontsize='12')
    # axs[0,1].set_xlabel(r'$n$ (fm$^{-3}$)',fontsize='12')
    axs[1, 0].set_xlabel(r"$n_\text{nuc}$ (fm$^{-3}$)", fontsize="12")
    axs[1, 1].set_xlabel(r"$n_\text{nuc}$ (fm$^{-3}$)", fontsize="12")
    #
    axs[0, 0].set_ylabel(r"$p_\mathrm{SM}(n_\text{nuc})$ (MeV fm$^{-3}$)", fontsize="12")
    axs[0, 1].set_ylabel(r"$e_\mathrm{SM}(n_\text{nuc})$ (MeV)", fontsize="12")
    axs[1, 0].set_ylabel(r"$p_\mathrm{NM}(n_\text{nuc})$ (MeV fm$^{-3}$)", fontsize="12")
    axs[1, 1].set_ylabel(r"$e_\text{sym}(n_\text{nuc})$ (MeV)", fontsize="12")
    #
    axs[0, 0].set_xlim([0.16, 0.8])
    axs[0, 0].set_ylim([0.5, 400])
    axs[0, 1].set_xlim([0.0, 0.44])
    axs[0, 1].set_ylim([-18, 20])
    axs[1, 0].set_xlim([0.16, 0.8])
    axs[1, 0].set_ylim([0.5, 400])
    axs[1, 1].set_xlim([0.0, 0.44])
    axs[1, 1].set_ylim([0.0, 80])
    #
    axs[0, 0].set_yscale("log")
    axs[1, 0].set_yscale("log")
    #
    axs[0, 0].tick_params("x", labelbottom=False)
    axs[0, 1].tick_params("x", labelbottom=False)
    #
    for inference in inferences:
        #
        print("inference:", inference)
        hic = nuda.matter.setupHIC( inference = inference )
        #
        if hic.sm_pre is not None:
            axs[0, 0].fill_between(
                hic.den_pre,
                y1=hic.sm_pre_lo,
                y2=hic.sm_pre_up,
                label=hic.label,
                alpha=hic.alpha * 0.8,
                color=hic.color,
            )
        #
        if hic.sm_e2a_int_lo is not None:
            axs[0, 1].fill_between(
                hic.den_e2a,
                y1=hic.sm_e2a_int_lo,
                y2=hic.sm_e2a_int_up,
                label=hic.label,
                alpha=hic.alpha,
                color="magenta",
            )
        #
        if hic.nm_pre is not None:
            axs[1, 0].fill_between(
                hic.den_pre,
                y1=hic.nm_pre_lo,
                y2=hic.nm_pre_up,
                label=hic.label_so,
                alpha=0.2,
                color="b",
            )
            axs[1, 0].fill_between(
                hic.den_pre,
                y1=hic.nm_pre_st_lo,
                y2=hic.nm_pre_st_up,
                label=hic.label_st,
                alpha=0.2,
                color="g",
            )
        #
        if hic.esym is not None and hic.den_err:
            axs[1, 1].errorbar(
                hic.den_esym,
                hic.esym,
                xerr=hic.den_esym_err,
                yerr=hic.esym_err,
                fmt="o",
                label=hic.label,
                color=hic.color,
                capsize=2,
                capthick=1,
                elinewidth=1,
                markersize=3,
            )
        #
        if hic.esym is not None and not hic.den_err:
            axs[1, 1].fill_between(
                hic.den_esym,
                y1=hic.esym_lo,
                y2=hic.esym_up,
                label=hic.label,
                alpha=hic.alpha * 0.7,
                color=hic.color,
            )
        #
    #
    # axs.text(0.15,12,r'$K_{sym}$='+str(int(Ksym))+' MeV',fontsize='12')
    axs[0, 0].legend(loc="lower right", fontsize="8")
    axs[0, 1].legend(loc="upper left", fontsize="8")
    axs[1, 0].legend(loc="lower right", fontsize="8")
    axs[1, 1].legend(loc="lower right", fontsize="8")
    #
    if pname is not None:
        plt.savefig(pname, dpi=300)
        plt.close()
    #
