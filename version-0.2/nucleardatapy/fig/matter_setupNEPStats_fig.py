import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda


def matter_setupNEPStats_fig(pname, models):
    """
    Plot nucleonic energy per particle E/A in matter.\
    The plot is 5x2 with:\
    [0,0]: E/A versus den (micro). [0,1]: E/A versus den (pheno).\

    :param pname: name of the figure (*.png)
    :type pname: str.
    :param models: models to run on.
    :type models: array of str.

    """
    #
    print(f"Plot name: {pname}")
    #
    fig, axs = plt.subplots(5, 2)
    fig.tight_layout()  # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust( left=0.12, bottom=0.06, right=0.95, top=0.9, wspace=0.3, hspace=0.4 )
    #
    axs[0, 0].set_ylabel(r"$E_\text{sat}$")
    axs[0, 0].set_xlim([-16.5, -15])
    axs[1, 0].set_ylabel(r"$n_\text{sat}$")
    axs[1, 0].set_xlim([0.14, 0.18])
    axs[2, 0].set_ylabel(r"$K_\text{sat}$")
    axs[2, 0].set_xlim([180, 360])
    axs[3, 0].set_ylabel(r"$Q_\text{sat}$")
    axs[3, 0].set_xlim([-1000, 1000])
    axs[4, 0].set_ylabel(r"$m_\text{sat}^{*}/m$")
    axs[4, 0].set_xlim([0.35, 1.2])
    axs[0, 1].set_ylabel(r"$E_\text{sym}$")
    axs[0, 1].set_xlim([26, 40])
    axs[1, 1].set_ylabel(r"$L_\text{sym}$")
    axs[1, 1].set_xlim([0, 120])
    axs[2, 1].set_ylabel(r"$K_\text{sym}$")
    axs[2, 1].set_xlim([-400, 220])
    axs[3, 1].set_ylabel(r"$Q_\text{sym}$")
    axs[3, 1].set_xlim([-50, 900])
    axs[4, 1].set_ylabel(r"$\Delta m_\text{sat}^{*}/m$")
    axs[4, 1].set_xlim([-0.5, 1.1])
    #
    # Built distribution of NEP
    #
    for model in models:
        #
        dist = nuda.matter.setupNEPStat_model(model)
        #
        xbins = np.arange(-16.5, -15.0, 0.15)
        if len(dist.Esat) != 0:
            axs[0, 0].hist(dist.Esat, bins=xbins, alpha=0.5, weights=1/len(dist.Esat) * np.ones(len(dist.Esat)) )
        xbins = np.arange(0.14, 0.18, 0.004)
        if len(dist.nsat) != 0:
            axs[1, 0].hist(dist.nsat, bins=xbins, alpha=0.5, weights=1/len(dist.nsat) * np.ones(len(dist.nsat)) )
        xbins = np.arange(180, 320, 20)
        if len(dist.Ksat) != 0:
            axs[2, 0].hist(dist.Ksat, bins=xbins, alpha=0.5, weights=1/len(dist.Ksat) * np.ones(len(dist.Ksat)), label=model )
        xbins = np.arange(-1000, 1000, 200)
        if len(dist.Qsat) != 0:
            axs[3, 0].hist(dist.Qsat, bins=xbins, alpha=0.5, weights=1/len(dist.Qsat) * np.ones(len(dist.Qsat)) )
        xbins = np.arange(0.5, 1.2, 0.1)
        if len(dist.msat) != 0:
            axs[4, 0].hist(dist.msat, bins=xbins, alpha=0.5, weights=1/len(dist.msat) * np.ones(len(dist.msat)) )
        xbins = np.arange(25, 40, 1.0)
        if len(dist.Esym) != 0:
            axs[0, 1].hist(dist.Esym, bins=xbins, alpha=0.5, weights=1/len(dist.Esym) * np.ones(len(dist.Esym)) )
        xbins = np.arange(0, 120, 10)
        if len(dist.Lsym) != 0:
            axs[1, 1].hist(dist.Lsym, bins=xbins, alpha=0.5, weights=1/len(dist.Lsym) * np.ones(len(dist.Lsym)) )
        xbins = np.arange(-400, 400, 100)
        if len(dist.Ksym) != 0:
            axs[2, 1].hist(dist.Ksym, bins=xbins, alpha=0.5, weights=1/len(dist.Ksym) * np.ones(len(dist.Ksym)) )
        xbins = np.arange(0, 1100, 100)
        if len(dist.Qsym) != 0:
            axs[3, 1].hist(dist.Qsym, bins=xbins, alpha=0.5, weights=1/len(dist.Qsym) * np.ones(len(dist.Qsym)) )
        xbins = np.arange(-0.6, 1.0, 0.1)
        if len(dist.Dmsat) != 0:
            axs[4, 1].hist(dist.Dmsat, bins=xbins, alpha=0.5, weights=1/len(dist.Dmsat) * np.ones(len(dist.Dmsat)) )
    #
    # axs[0,0].legend(loc='lower right',fontsize='10',ncol=2)
    fig.legend(
        loc="upper left",
        bbox_to_anchor=(0.02, 0.99),
        columnspacing=2,
        fontsize="7.5",
        ncol=7,
        frameon=False,
    )
    #
    if pname is not None:
        plt.savefig(pname, dpi=300)
        plt.close()
