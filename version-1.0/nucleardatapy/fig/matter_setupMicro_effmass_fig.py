import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda


def matter_setupMicro_effmass_fig(pname, models, matter="NM"):
    """
    Plot the effective mass as function of the density and Fermi momentum.\
    The plot is 1x2 with:\
    [0]: effmass(den)
    [1]: effmass(kF)

    :param pname: name of the figure (*.png)
    :type pname: str.
    :param models: list of models to run on.
    :type models: array of str.
    :param matter: chose between 'SM' and 'NM' (default).
    :type matter: str.
    """
    #
    print(f"Plot name: {pname}")
    print("models:", models)
    print("matter:", matter)
    #
    fig, axs = plt.subplots(1, 2)
    fig.tight_layout()  # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust( left=0.12, bottom=0.12, right=0.95, top=0.85, wspace=0.05, hspace=0.05 )
    #
    axs[0].set_ylabel(r"Landau effective mass $m^*/m$", fontsize='14')
    axs[0].set_xlabel(r"$n_\text{nuc}$ (fm$^{-3}$)", fontsize='14')
    # axs[0].tick_params('x', labelbottom=False)
    #
    # axs[1].tick_params('x', labelbottom=False)
    axs[1].tick_params("y", labelleft=False)
    axs[1].set_xlabel(r"$k_{F}$ (fm$^{-1}$)", fontsize='14')
    #
    if matter.lower() == "nm":
        axs[0].set_xlim([0, 0.34])
        axs[0].set_ylim([0.6, 1.1])
        axs[1].set_xlim([0, 2.0])
        axs[1].set_ylim([0.6, 1.1])
    elif matter.lower() == "sm":
        axs[0].set_xlim([0, 0.34])
        axs[0].set_ylim([0.6, 1.1])
        axs[1].set_xlim([0, 2.0])
        axs[1].set_ylim([0.6, 1.1])
    elif matter.lower() == "am":
        axs[0].set_xlim([0.05, 0.27])
        axs[0].set_ylim([0.7, 1.0])
        axs[1].set_xlim([0.7, 1.8])
        axs[1].set_ylim([0.7, 1.0])
    #
    # axs[1,0].set_ylabel(r'$\Delta_{1S0}/E_F$')
    #
    for model in models:
        #
        ms = nuda.matter.setupMicroEffmass(model=model, matter=matter)
        #
        lstyle = None
        #
        axs[0].text(0.08, 0.75, "in " + matter)
        axs[1].text(0.90, 0.75, "in " + matter)
        if matter.lower() == "nm":
            if ms.nm_effmass is not None:
                if ms.nm_effmass_err is not None:
                    axs[0].errorbar(
                        ms.nm_den,
                        ms.nm_effmass,
                        yerr=ms.nm_effmass_err,
                        marker=ms.marker,
                        markevery=ms.every,
                        linestyle=lstyle,
                        label=ms.label,
                    )
                    axs[1].errorbar(
                        ms.nm_kfn,
                        ms.nm_effmass,
                        yerr=ms.nm_effmass_err,
                        marker=ms.marker,
                        markevery=ms.every,
                        linestyle=lstyle,
                    )
                else:
                    axs[0].plot(
                        ms.nm_den,
                        ms.nm_effmass,
                        marker=ms.marker,
                        markevery=ms.every,
                        linestyle=lstyle,
                        label=ms.label,
                    )
                    axs[1].plot(
                        ms.nm_kfn,
                        ms.nm_effmass,
                        marker=ms.marker,
                        markevery=ms.every,
                        linestyle=lstyle,
                    )
        elif matter.lower() == "sm":
            if ms.sm_effmass is not None:
                if ms.sm_effmass_err is not None:
                    axs[0].errorbar(
                        ms.sm_den,
                        ms.sm_effmass,
                        yerr=ms.sm_effmass_err,
                        marker=ms.marker,
                        markevery=ms.every,
                        linestyle=lstyle,
                        label=ms.label,
                    )
                    axs[1].errorbar(
                        ms.sm_kfn,
                        ms.sm_effmass,
                        yerr=ms.sm_effmass_err,
                        marker=ms.marker,
                        markevery=ms.every,
                        linestyle=lstyle,
                    )
                else:
                    axs[0].plot(
                        ms.sm_den,
                        ms.sm_effmass,
                        marker=ms.marker,
                        markevery=ms.every,
                        linestyle=lstyle,
                        label=ms.label,
                    )
                    axs[1].plot(
                        ms.sm_kfn,
                        ms.sm_effmass,
                        marker=ms.marker,
                        markevery=ms.every,
                        linestyle=lstyle,
                    )
        elif matter.lower() == "am":
            if ms.sm_effmass_n is not None:
                if ms.sm_effmass_err is not None:
                    axs[0].errorbar(
                        ms.sm_den,
                        ms.sm_effmass,
                        yerr=ms.sm_effmass_err,
                        marker=ms.marker,
                        markevery=ms.every,
                        linestyle=lstyle,
                        label=ms.label,
                    )
                    axs[1].errorbar(
                        ms.sm_kfn,
                        ms.sm_effmass,
                        yerr=ms.sm_effmass_err,
                        marker=ms.marker,
                        markevery=ms.every,
                        linestyle=lstyle,
                    )
                else:
                    ms_n_00, ms_p_00 = nuda.matter.effmass_emp( ms.sm_den, 0.0, mb="BHF" )
                    ms_n_02, ms_p_02 = nuda.matter.effmass_emp( ms.am02_den, 0.2, mb="BHF" )
                    ms_n_04, ms_p_04 = nuda.matter.effmass_emp( ms.am04_den, 0.4, mb="BHF" )
                    axs[0].plot(
                        ms.sm_den,
                        ms.sm_effmass_n,
                        marker="^",
                        color=nuda.param.col[1],
                        markevery=ms.every,
                        linestyle=lstyle,
                        label=ms.label + "(neutrons)",
                    )
                    axs[0].plot(
                        ms.am02_den,
                        ms.am02_effmass_n,
                        marker="^",
                        color=nuda.param.col[1],
                        markevery=ms.every,
                        linestyle=lstyle,
                    )
                    axs[0].plot(
                        ms.am04_den,
                        ms.am04_effmass_n,
                        marker="^",
                        color=nuda.param.col[1],
                        markevery=ms.every,
                        linestyle=lstyle,
                    )
                    axs[0].plot(
                        ms.sm_den,
                        ms.sm_effmass_p,
                        marker="v",
                        color=nuda.param.col[2],
                        markevery=ms.every,
                        linestyle=lstyle,
                        label=ms.label + "(protons)",
                    )
                    axs[0].plot(
                        ms.am02_den,
                        ms.am02_effmass_p,
                        marker="v",
                        color=nuda.param.col[2],
                        markevery=ms.every,
                        linestyle=lstyle,
                    )
                    axs[0].plot(
                        ms.am04_den,
                        ms.am04_effmass_p,
                        marker="v",
                        color=nuda.param.col[2],
                        markevery=ms.every,
                        linestyle=lstyle,
                    )
                    axs[0].plot(
                        ms.sm_den,
                        ms_n_00,
                        color=nuda.param.col[1],
                        linestyle="dotted",
                        label="Fit(neutrons)",
                    )
                    axs[0].plot( ms.am02_den, ms_n_02, color=nuda.param.col[1], linestyle="dotted" )
                    axs[0].plot( ms.am04_den, ms_n_04, color=nuda.param.col[1], linestyle="dotted" )
                    axs[0].plot( ms.sm_den, ms_p_00, color=nuda.param.col[2], linestyle="dotted", label="Fit(protons)" )
                    axs[0].plot( ms.am02_den, ms_p_02, color=nuda.param.col[2], linestyle="dotted" )
                    axs[0].plot( ms.am04_den, ms_p_04, color=nuda.param.col[2], linestyle="dotted" )
                    axs[1].plot(
                        ms.sm_kfn,
                        ms.sm_effmass_n,
                        marker="^",
                        color=nuda.param.col[1],
                        markevery=ms.every,
                        linestyle=lstyle,
                    )
                    axs[1].plot(
                        ms.am02_kfn,
                        ms.am02_effmass_n,
                        marker="^",
                        color=nuda.param.col[1],
                        markevery=ms.every,
                        linestyle=lstyle,
                    )
                    axs[1].plot(
                        ms.am04_kfn,
                        ms.am04_effmass_n,
                        marker="^",
                        color=nuda.param.col[1],
                        markevery=ms.every,
                        linestyle=lstyle,
                    )
                    axs[1].plot(
                        ms.sm_kfn,
                        ms.sm_effmass_p,
                        marker="v",
                        color=nuda.param.col[2],
                        markevery=ms.every,
                        linestyle=lstyle,
                    )
                    axs[1].plot(
                        ms.am02_kfn,
                        ms.am02_effmass_p,
                        marker="v",
                        color=nuda.param.col[2],
                        markevery=ms.every,
                        linestyle=lstyle,
                    )
                    axs[1].plot(
                        ms.am04_kfn,
                        ms.am04_effmass_p,
                        marker="v",
                        color=nuda.param.col[2],
                        markevery=ms.every,
                        linestyle=lstyle,
                    )
                    axs[1].plot( ms.sm_kfn, ms_n_00, color=nuda.param.col[1], linestyle="dotted" )
                    axs[1].plot( ms.am02_kfn, ms_n_02, color=nuda.param.col[1], linestyle="dotted" )
                    axs[1].plot( ms.am04_kfn, ms_n_04, color=nuda.param.col[1], linestyle="dotted" )
                    axs[1].plot( ms.sm_kfn, ms_p_00, color=nuda.param.col[2], linestyle="dotted" )
                    axs[1].plot( ms.am02_kfn, ms_p_02, color=nuda.param.col[2], linestyle="dotted" )
                    axs[1].plot( ms.am04_kfn, ms_p_04, color=nuda.param.col[2], linestyle="dotted" )
                    axs[0].text(0.23, 0.84, r"$\delta=0.4$", rotation=0)
                    axs[0].text(0.23, 0.81, r"$\delta=0.2$", rotation=0)
                    axs[0].text(0.23, 0.785, "SM", rotation=0)
                    axs[0].text(0.23, 0.76, r"$\delta=0.2$", rotation=0)
                    axs[0].text(0.23, 0.74, r"$\delta=0.4$", rotation=0)
                    axs[1].text(0.90, 0.92, "SM", rotation=0)
                    axs[1].text(0.90, 0.94, r"$\delta=0.2$", rotation=0)
                    axs[1].text(0.95, 0.96, r"$\delta=0.4$", rotation=0)
        if nuda.env.verb_output:
            ms.print_outputs()
    #
    # axs[1,0].legend(loc='upper right',fontsize='8')
    fig.legend(
        loc="upper left",
        bbox_to_anchor=(0.08, 1.0),
        columnspacing=2,
        fontsize="8",
        ncol=3,
        frameon=False,
    )
    #
    if pname is not None:
        plt.savefig(pname, dpi=300)
        plt.close()
    #