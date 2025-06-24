import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda


def matter_setupMicro_err_NM_fig(pname, models):
    """
    Plot uncertainties (err) estimated by different authors in NM.\
    The plot is 1x1 with:\
    [0]: uncertainty for E/A versus den.

    :param pname: name of the figure (*.png)
    :type pname: str.
    :param models: array of models.
    :type models: array of str.

    """
    #
    print(f"Plot name: {pname}")
    #
    den = 0.03 * np.arange(13)
    #
    fig, axs = plt.subplots(1, 1)
    fig.tight_layout()  # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(
        left=0.12, bottom=0.12, right=None, top=0.98, wspace=0.2, hspace=0.2
    )
    #
    axs.set_xlabel(r"$n_\text{nuc}$ (fm$^{-3}$)", fontsize="14")
    axs.set_ylabel(r"$\Delta E_{int,NM}/E_{int,NM}$", fontsize="14")
    axs.set_xlim([0, 0.37])
    axs.set_ylim([0, 0.5])
    #
    for model in models:
        #
        mic = nuda.matter.setupMicro(model=model)
        if nuda.env.verb_output:
            mic.print_outputs()
        if mic.nm_e2a is not None:
            print("model:", model)
            axs.plot(
                mic.nm_den,
                mic.nm_e2a_err / mic.nm_e2a_int,
                marker=mic.marker,
                markevery=mic.every,
                linestyle=mic.linestyle,
                label=mic.label,
            )
    # axs.plot( den, nuda.matter.uncertainty_stat(den), linestyle='dashed', linewidth=3, label='fit (MBPT)' )
    axs.plot(
        den,
        nuda.matter.uncertainty_stat(den, err="MBPT"),
        linestyle="dashed",
        linewidth=3,
        label="fit (MBPT)",
    )
    axs.plot(
        den,
        nuda.matter.uncertainty_stat(den, err="QMC"),
        linestyle="dashed",
        linewidth=3,
        label="fit (QMC)",
    )
    #
    axs.legend(loc="upper left", fontsize="12", ncol=3)
    #
    if pname is not None:
        plt.savefig(pname, dpi=200)
        plt.close()
