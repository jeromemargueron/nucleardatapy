import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda


def matter_setupMatterEsym_fig(pname, model, band):
    """
    Plot the symmetry energy esym for phenomenologic models.

    The plot is 2x2 with:

    [0,0]: esym function of the density.          [0,1]: esym function of the Fermi momentum.

    [0,0]: esym/esym,FFG function of the density. [0,1]: esym/esym,FFG function of the Fermi momentum.

    :param pname: name of the figure (*.png)
    :type pname: str.
    :param model: model.
    :type model: array of str.
    :param band: object instantiated on the reference band.
    :type band: object.
    """
    #
    print(f"Plot name: {pname}")
    #
    fig, axs = plt.subplots(2, 2)
    fig.tight_layout()  # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust( left=0.12, bottom=0.12, right=0.95, top=0.88, wspace=0.05, hspace=0.05 )
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
    params, params_lower = nuda.matter.matter_esym_params(model=model)
    #
    for param in params:
        #
        print("in Sample: model, param", model, param)
        matt = nuda.matter.setupMatterEsym(model=model, param=param)
        if nuda.env.verb_output: matt.print_outputs()
        #
        lstyle = "dashed"
        if matt.nm_e2a_int is not None and matt.sm_e2a_int is not None:
            check = nuda.matter.setupCheck(eos=matt, band=band)
            if check.isInside:
                lstyle = "solid"
        #
        # print("esym:",pheno.esym)
        # print("den:",pheno.den)
        if matt.esym is not None:
            print("esym_err:", matt.esym_err)
            if matt.esym_err is None:
                if check.isInside:
                    axs[0, 0].plot( matt.den, matt.esym, marker=matt.marker, linestyle=lstyle, label=matt.label )
                else:
                    axs[0, 0].plot( matt.den, matt.esym, marker=matt.marker, linestyle=lstyle )
                axs[0, 1].plot( matt.kfn, matt.esym, marker=matt.marker, linestyle=lstyle )
                axs[1, 0].plot( matt.den, matt.esym / nuda.esymffg_nr(matt.kfn), marker=matt.marker, linestyle=lstyle )
                axs[1, 1].plot( matt.kfn, matt.esym / nuda.esymffg_nr(matt.kfn), marker=matt.marker, linestyle=lstyle )
            else:
                axs[0, 0].errorbar( matt.den, matt.esym, yerr=matt.esym_err, marker=matt.marker, linestyle=lstyle, errorevery=matt.every, label=matt.label )
                axs[0, 1].errorbar( matt.kfn, matt.esym, yerr=matt.esym_err, marker=matt.marker, linestyle=lstyle, errorevery=matt.every )
                axs[1, 0].errorbar( matt.den, matt.esym / nuda.esymffg_nr(matt.kfn), yerr=matt.esym_err / nuda.esymffg_nr(matt.kfn), marker=matt.marker, linestyle=lstyle, errorevery=matt.every )
                axs[1, 1].errorbar( matt.kfn, matt.esym / nuda.esymffg_nr(matt.kfn), yerr=matt.esym_err / nuda.esymffg_nr(matt.kfn), marker=matt.marker, linestyle=lstyle, errorevery=matt.every )
        #
    axs[0, 0].fill_between( band.den, y1=(band.e2a_int - band.e2a_std), y2=(band.e2a_int + band.e2a_std), color=band.color, alpha=band.alpha, visible=True )
    axs[0, 0].plot( band.den, (band.e2a_int - band.e2a_std), color="k", linestyle="dashed", visible=True, zorder = 100 )
    axs[0, 0].plot( band.den, (band.e2a_int + band.e2a_std), color="k", linestyle="dashed", visible=True, zorder = 100 )
    axs[0, 1].fill_between( band.kfn, y1=(band.e2a_int - band.e2a_std), y2=(band.e2a_int + band.e2a_std), color=band.color, alpha=band.alpha, visible=True )
    axs[0, 1].plot( band.kfn, (band.e2a_int - band.e2a_std), color="k", linestyle="dashed", visible=True, zorder = 100 )
    axs[0, 1].plot( band.kfn, (band.e2a_int + band.e2a_std), color="k", linestyle="dashed", visible=True, zorder = 100 )
    axs[1, 0].fill_between( band.den, y1=(band.e2a_int - band.e2a_std) / nuda.esymffg_nr(band.kfn), y2=(band.e2a_int + band.e2a_std) / nuda.esymffg_nr(band.kfn), color=band.color, alpha=band.alpha, visible=True )
    axs[1, 0].plot( band.den, (band.e2a_int - band.e2a_std) / nuda.esymffg_nr(band.kfn), color="k", linestyle="dashed", visible=True, zorder = 100 )
    axs[1, 0].plot( band.den, (band.e2a_int + band.e2a_std) / nuda.esymffg_nr(band.kfn), color="k", linestyle="dashed", visible=True, zorder = 100 )
    axs[1, 1].fill_between( band.kf, y1=(band.e2a_int - band.e2a_std) / nuda.esymffg_nr(band.kfn), y2=(band.e2a_int + band.e2a_std) / nuda.esymffg_nr(band.kfn), color=band.color, alpha=band.alpha, visible=True )
    axs[1, 1].plot( band.kfn, (band.e2a_int - band.e2a_std) / nuda.esymffg_nr(band.kfn), color="k", linestyle="dashed", visible=True, zorder = 100 )
    axs[1, 1].plot( band.kfn, (band.e2a_int + band.e2a_std) / nuda.esymffg_nr(band.kfn), color="k", linestyle="dashed", visible=True, zorder = 100 )
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
        fig.savefig(pname, dpi=300)
        plt.close()
    #
