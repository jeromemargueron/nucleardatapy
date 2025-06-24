import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda


def matter_setupMicro_LP_fig( pname, models, matter="SM", ell=0 ):
    """
    Plot nucleonic energy per particle E/A in matter.\
    The plot is 2x2 with:\
    [0,0]: E/A versus den.       [0,1]: E/A versus kfn.\
    [1,0]: E/E_NRFFG versus den. [1,1]: E/E_NRFFG versus kfn.\

    :param pname: name of the figure (*.png)
    :type pname: str.
    :param models: models to run on.
    :type models: array of str.
    :param matter: can be 'SM' (default) or 'NM'.
    :type matter: str.
    :param ell: Value of the angular momentum L of the Landau residual parameter. Can be 0 (default) or 1.
    :type ell: int.

    """
    #
    print(f"Plot name: {pname}")
    #
    if matter.lower() == "sm":
        fig, axs = plt.subplots(2, 2)
        fig.subplots_adjust( left=0.12, bottom=0.12, right=0.98, top=0.98, wspace=0.15, hspace=0.05 )
    elif matter.lower() == "nm":
        fig, axs = plt.subplots(1, 2)
        fig.subplots_adjust( left=0.12, bottom=0.12, right=0.98, top=0.98, wspace=0.15, hspace=0.05 )
    else:
        print("matter_setupMicro_LP_fig: issue with matter:", matter)
        print("matter_setupMicro_LP_fig: --- exit() ---")
        exit()
    #
    #
    if matter.lower() == "sm":
        axs[0, 0].set_xlim([0, 2.0])
        axs[0, 0].set_ylim([-2.1, 1.6])
        if ell == 0:
            axs[0, 0].set_ylabel(r"$F_0$", fontsize='14')
        if ell == 1:
            axs[0, 0].set_ylabel(r"$F_1$", fontsize='14')
        axs[0, 0].tick_params("x", labelbottom=False)
        if ell == 0:
            axs[0, 1].set_ylabel(r"$G_0$", fontsize='14')
        if ell == 1:
            axs[0, 1].set_ylabel(r"$G_1$", fontsize='14')
        axs[0, 1].set_xlim([0, 2.0])
        axs[0, 1].set_ylim([-2.1, 1.6])
        axs[0, 1].tick_params("x", labelbottom=False)
        axs[0, 1].tick_params("y", labelleft=False)
        if ell == 0:
            axs[1, 0].set_ylabel(r"$F_0^\prime$", fontsize='14')
        if ell == 1:
            axs[1, 0].set_ylabel(r"$F_1^\prime$", fontsize='14')
        axs[1, 0].set_xlabel(r"$k_{F}$ (fm$^{-1}$)", fontsize='14')
        axs[1, 0].set_xlim([0, 2.0])
        axs[1, 0].set_ylim([-1.1, 2.6])
        if ell == 0:
            axs[1, 1].set_ylabel(r"$G_0^\prime$", fontsize='14')
        if ell == 1:
            axs[1, 1].set_ylabel(r"$G_1^\prime$", fontsize='14')
        axs[1, 1].set_xlabel(r"$k_{F}$ (fm$^{-1}$)", fontsize='14')
        axs[1, 1].set_xlim([0, 2.0])
        axs[1, 1].set_ylim([-1.1, 2.6])
        axs[1, 1].tick_params("y", labelleft=False)
    elif matter.lower() == "nm":
        if ell == 0:
            axs[0].set_ylabel(r"$F_0$", fontsize='14')
        if ell == 1:
            axs[0].set_ylabel(r"$F_1$", fontsize='14')
        axs[0].set_xlabel(r"$k_{F}$ (fm$^{-1}$)", fontsize='14')
        axs[0].set_xlim([0, 2.0])
        axs[0].set_ylim([-1.1, 1.1])
        if ell == 0:
            axs[1].set_ylabel(r"$G_0$", fontsize='14')
        if ell == 1:
            axs[1].set_ylabel(r"$G_1$", fontsize='14')
        axs[1].set_xlabel(r"$k_{F}$ (fm$^{-1}$)", fontsize='14')
        axs[1].set_xlim([0, 2.0])
        axs[1].set_ylim([-1.1, 1.1])
        axs[1].tick_params("y", labelleft=False)
    #
    for model in models:
        #
        mic = nuda.matter.setupMicroLP(model=model)
        #
        if matter in model:
            print("\nmodel:", model, "\n")
            if mic.err:
                if matter.lower() == "sm" and mic.sm_LP["F"][ell] is not None:
                    axs[0, 0].errorbar(
                        mic.sm_kfn,
                        mic.sm_LP["F"][ell],
                        yerr=mic.sm_LP_F_err[ell],
                        marker=mic.marker,
                        linestyle="none",
                        label=mic.label,
                    )
                    axs[0, 1].errorbar(
                        mic.sm_kfn,
                        mic.sm_LP["G"][ell],
                        yerr=mic.sm_LP_G_err[ell],
                        marker=mic.marker,
                        linestyle="none",
                        label=mic.label,
                    )
                    axs[1, 0].errorbar(
                        mic.sm_kfn,
                        mic.sm_LP["Fp"][ell],
                        yerr=mic.sm_LP_Fp_err[ell],
                        marker=mic.marker,
                        linestyle="none",
                        label=mic.label,
                    )
                    axs[1, 1].errorbar(
                        mic.sm_kfn,
                        mic.sm_LP["Gp"][ell],
                        yerr=mic.sm_LP_Gp_err[ell],
                        marker=mic.marker,
                        linestyle="none",
                        label=mic.label,
                    )
                elif matter.lower() == "nm" and mic.nm_LP["F"][ell] is not None:
                    axs[0].errorbar(
                        mic.nm_kfn,
                        mic.nm_LP["F"][ell],
                        marker=mic.marker,
                        linestyle="none",
                        label=mic.label,
                    )
                    axs[1].errorbar(
                        mic.nm_kfn,
                        mic.nm_LP["G"][ell],
                        marker=mic.marker,
                        linestyle="none",
                        label=mic.label,
                    )
            else:
                if matter.lower() == "sm" and mic.sm_LP["F"][ell] is not None:
                    axs[0, 0].plot(
                        mic.sm_kfn,
                        mic.sm_LP["F"][ell],
                        marker=mic.marker,
                        linestyle=mic.linestyle,
                        markevery=mic.every,
                        label=mic.label,
                    )
                    axs[0, 1].plot(
                        mic.sm_kfn,
                        mic.sm_LP["G"][ell],
                        marker=mic.marker,
                        linestyle=mic.linestyle,
                        markevery=mic.every,
                        label=mic.label,
                    )
                    axs[1, 0].plot(
                        mic.sm_kfn,
                        mic.sm_LP["Fp"][ell],
                        marker=mic.marker,
                        linestyle=mic.linestyle,
                        markevery=mic.every,
                        label=mic.label,
                    )
                    axs[1, 1].plot(
                        mic.sm_kfn,
                        mic.sm_LP["Gp"][ell],
                        marker=mic.marker,
                        linestyle=mic.linestyle,
                        markevery=mic.every,
                        label=mic.label,
                    )
                elif matter.lower() == "nm" and mic.nm_LP["F"][ell] is not None:
                    axs[0].plot(
                        mic.nm_kfn,
                        mic.nm_LP["F"][ell],
                        marker=mic.marker,
                        linestyle=mic.linestyle,
                        markevery=mic.every,
                        label=mic.label,
                    )
                    axs[1].plot(
                        mic.nm_kfn,
                        mic.nm_LP["G"][ell],
                        marker=mic.marker,
                        linestyle=mic.linestyle,
                        markevery=mic.every,
                        label=mic.label,
                    )
        #
        if nuda.env.verb_output:
            mic.print_outputs()
        #
    #
    if matter.lower() == "sm":
        axs[1, 0].legend(loc="upper left", fontsize="6", ncol=2)
    elif matter.lower() == "nm":
        axs[0].legend(loc="upper left", fontsize="8", ncol=1)
    #
    if pname is not None:
        plt.savefig(pname, dpi=300)
        plt.close()
    #
