import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import nucleardatapy as nuda

mpl.use("Agg")  # Use a non-interactive backend

def matter_setupFFGNuc_EP_fig(
    pname, mss=[1.0], den=np.linspace(0.01, 0.35, 10), kf=np.linspace(0.5, 2.0, 10)
):
    """
    Plot nucleonic FFG energy per particle E/A and pressure in NM and SM.\
    The plot is 2x2 with:\
    [0,0]: E/A versus den.     [0,1]: E/A versus kfn.\
    [1,0]: pre versus den.     [1,1]: pre versus kfn.\

    :param pname: name of the figure (*.png)
    :type pname: str.
    :param den: density.
    :type den: float or numpy vector of real numbers.
    :param kfn: neutron Fermi momentum.
    :type kfn: float or numpy vector of real numbers.

    """
    #
    print(f"Plot name: {pname}")
    #
    denkf = nuda.matter.den(kf)
    delta0 = np.zeros(den.size)
    delta1 = np.ones(den.size)
    #
    fig, axs = plt.subplots(2, 2)
    fig.tight_layout()  # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust( left=0.12, bottom=0.12, right=None, top=0.9, wspace=0.05, hspace=0.05 )
    #
    axs[0, 0].set_ylabel(r"$e^\text{FFG}_\text{int}$ (MeV)")
    axs[0, 0].set_xlim([0, 0.33])
    axs[0, 0].set_ylim([0, 100])
    axs[0, 0].tick_params("x", labelbottom=False)
    #
    axs[1, 0].set_xlabel(r"$n_\text{nuc}$ (fm$^{-3}$)")
    axs[1, 0].set_ylabel(r"$p^\text{FFG}$ (MeV fm$^{-3}$)")
    axs[1, 0].set_xlim([0, 0.33])
    axs[1, 0].set_ylim([0, 23])
    #
    # axs[0,1].set_ylabel(r'$\Delta/E_F$')
    #axs[0, 1].set_xlim([0.5, 2.0])
    #axs[0, 1].set_ylim([0, 100])
    axs[0, 1].tick_params("y", labelleft=False)
    axs[0, 1].tick_params("x", labelbottom=False)
    #
    axs[1, 1].set_xlabel(r"$k_{F}$ (fm$^{-1}$)")
    # axs[1,1].set_ylabel(r'$\Delta$ (MeV)')
    #axs[1, 1].set_xlim([0.5, 2.0])
    #axs[1, 1].set_ylim([0, 23])
    axs[1, 1].tick_params("y", labelleft=False)
    #
    for ims, ms in enumerate(mss):
        ffg0 = nuda.matter.setupFFGNuc(den, delta0, ms)
        ffg0kf = nuda.matter.setupFFGNuc(denkf, delta0, ms)
        ffg1 = nuda.matter.setupFFGNuc(den, delta1, ms)
        ffg1kf = nuda.matter.setupFFGNuc(denkf, delta1, ms)
        #
        if any(ffg0.e2a_int_nr):
            print(r"plot $\delta=0$ (SM)")
            if ims == 0:
                axs[0, 0].plot(
                    ffg0.den,
                    ffg0.e2a_int,
                    linestyle="solid",
                    color=nuda.param.col[0],
                    label=ffg0.label,
                )
                axs[0, 0].plot(
                    ffg0.den,
                    ffg0.e2a_int_nr,
                    linestyle="None",
                    marker="o",
                    color=nuda.param.col[0],
                    label="NR" + ffg0.label,
                )
            else:
                axs[0, 0].plot(
                    ffg0.den, ffg0.e2a_int, linestyle="solid", color=nuda.param.col[0]
                )
                axs[0, 0].plot(
                    ffg0.den,
                    ffg0.e2a_int_nr,
                    linestyle="None",
                    marker="o",
                    color=nuda.param.col[0],
                )
            axs[1, 0].plot(
                ffg0.den, ffg0.pre, linestyle="solid", color=nuda.param.col[0]
            )
            axs[1, 0].plot(
                ffg0.den,
                ffg0.pre_nr,
                linestyle="None",
                marker="o",
                color=nuda.param.col[0],
            )
            axs[0, 1].plot(
                ffg0kf.kf_nuc, ffg0kf.e2a_int, linestyle="solid", color=nuda.param.col[0]
            )
            axs[0, 1].plot(
                ffg0kf.kf_nuc,
                ffg0kf.e2a_int_nr,
                linestyle="None",
                marker="o",
                color=nuda.param.col[0],
            )
            axs[1, 1].plot(
                ffg0kf.kf_nuc, ffg0kf.pre, linestyle="solid", color=nuda.param.col[0]
            )
            axs[1, 1].plot(
                ffg0kf.kf_nuc,
                ffg0kf.pre_nr,
                linestyle="None",
                marker="o",
                color=nuda.param.col[0],
            )
        if nuda.env.verb_output:
            ffg0.print_outputs()
        if any(ffg1.e2a_int_nr):
            print(r"plot $\delta=1$ (NM)")
            if ims == 0:
                axs[0, 0].plot(
                    ffg1.den,
                    ffg1.e2a_int,
                    linestyle="dashed",
                    color=nuda.param.col[1],
                    label=ffg1.label,
                )
                axs[0, 0].plot(
                    ffg1.den,
                    ffg1.e2a_int_nr,
                    linestyle="None",
                    marker="o",
                    color=nuda.param.col[1],
                    label="NR" + ffg1.label,
                )
            else:
                axs[0, 0].plot(
                    ffg1.den, ffg1.e2a_int, linestyle="dashed", color=nuda.param.col[1]
                )
                axs[0, 0].plot(
                    ffg1.den,
                    ffg1.e2a_int_nr,
                    linestyle="None",
                    marker="o",
                    color=nuda.param.col[1],
                )
            axs[1, 0].plot(
                ffg1.den, ffg1.pre, linestyle="dashed", color=nuda.param.col[1]
            )
            axs[1, 0].plot(
                ffg1.den,
                ffg1.pre_nr,
                linestyle="None",
                marker="o",
                color=nuda.param.col[1],
            )
            axs[0, 1].plot(
                ffg1kf.kf_nuc, ffg1kf.e2a_int, linestyle="dashed", color=nuda.param.col[1]
            )
            axs[0, 1].plot(
                ffg1kf.kf_nuc,
                ffg1kf.e2a_int_nr,
                linestyle="None",
                marker="o",
                color=nuda.param.col[1],
            )
            axs[1, 1].plot(
                ffg1kf.kf_nuc, ffg1kf.pre, linestyle="dashed", color=nuda.param.col[1]
            )
            axs[1, 1].plot(
                ffg1kf.kf_nuc,
                ffg1kf.pre_nr,
                linestyle="None",
                marker="o",
                color=nuda.param.col[1],
            )
        if nuda.env.verb_output:
            ffg1.print_outputs()
        #
    axs[0, 0].text(0.2, 16, r"$m=$" + str(mss[0]) + "$m_N$", rotation=8)
    axs[0, 0].text(0.2, 32, r"$m=$" + str(mss[1]) + "$m_N$", rotation=13)
    axs[0, 0].text(0.2, 50, r"$m=$" + str(mss[2]) + "$m_N$", rotation=20)
    # axs[1,0].legend(loc='upper right',fontsize='xx-small')
    fig.legend(
        loc="upper left",
        bbox_to_anchor=(0.2, 0.97),
        fontsize="6",
        ncol=4,
        frameon=False,
    )
    #
    if pname is not None:
        plt.savefig(pname, dpi=300)
        plt.close()
    #


def matter_setupFFGNuc_EOS_fig(pname, mss=[1.0], den=np.linspace(0.01, 0.35, 10)):
    """
    Plot nucleonic FFG EOS in NM and SM.\
    The plot is 1x2 with:\
    [0]: EOS (pre) versus energy density rho.\
    [1]: Sound speed c_s^2 versus energy density rho.\

    :param pname: name of the figure (*.png)
    :type pname: str.
    :param den: density.
    :type den: float or numpy vector of real numbers.

    """
    #
    print(f"Plot name: {pname}")
    #
    delta0 = np.zeros(den.size)
    delta1 = np.ones(den.size)
    #
    fig, axs = plt.subplots(2, 1)
    fig.tight_layout()  # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust( left=0.12, bottom=0.12, right=None, top=0.9, wspace=0.05, hspace=0.05 )
    #
    axs[0].set_ylabel(r"$p^\text{FFG}$ (MeV fm$^{-3}$)", fontsize="14")
    axs[0].set_xlim([0, 360])
    axs[0].set_ylim([0, 20])
    axs[0].tick_params("x", labelbottom=False)
    #
    axs[1].set_xlabel(r"$\epsilon^\text{FFG}$ (MeV fm$^{-3}$)", fontsize="14")
    axs[1].set_ylabel(r"$(c^\text{FFG}_\text{s}/c)^2$", fontsize="14")
    axs[1].set_xlim([0, 360])
    axs[1].set_ylim([0, 0.28])
    #
    for ims, ms in enumerate(mss):
        ffg0 = nuda.matter.setupFFGNuc(den, delta0, ms)
        ffg1 = nuda.matter.setupFFGNuc(den, delta1, ms)
        #
        if any(ffg0.e2a_int_nr):
            print(r"plot $\delta=0$ (SM)")
            if ims == 0:
                axs[0].plot(
                    ffg0.eps,
                    ffg0.pre,
                    linestyle="solid",
                    color=nuda.param.col[0],
                    label=ffg0.label,
                )
                axs[0].plot(
                    ffg0.eps,
                    ffg0.pre_nr,
                    linestyle="None",
                    marker="o",
                    color=nuda.param.col[0],
                    label="NR" + ffg0.label,
                )
            else:
                axs[0].plot(
                    ffg0.eps, ffg0.pre, linestyle="solid", color=nuda.param.col[0]
                )
                axs[0].plot(
                    ffg0.eps,
                    ffg0.pre_nr,
                    linestyle="None",
                    marker="o",
                    color=nuda.param.col[0],
                )
            axs[1].plot(ffg0.eps, ffg0.cs2, linestyle="solid", color=nuda.param.col[0])
            axs[1].plot(
                ffg0.eps,
                ffg0.cs2_nr,
                linestyle="None",
                marker="o",
                color=nuda.param.col[0],
            )
        if nuda.env.verb_output:
            ffg0.print_outputs()
        if any(ffg1.e2a_int_nr):
            print(r"plot $\delta=1$ (NM)")
            if ims == 0:
                axs[0].plot(
                    ffg1.eps,
                    ffg1.pre,
                    linestyle="dashed",
                    color=nuda.param.col[1],
                    label=ffg1.label,
                )
                axs[0].plot(
                    ffg1.eps,
                    ffg1.pre_nr,
                    linestyle="None",
                    marker="o",
                    color=nuda.param.col[1],
                    label="NR" + ffg1.label,
                )
            else:
                axs[0].plot(
                    ffg1.eps, ffg1.pre, linestyle="dashed", color=nuda.param.col[1]
                )
                axs[0].plot(
                    ffg1.eps,
                    ffg1.pre_nr,
                    linestyle="None",
                    marker="o",
                    color=nuda.param.col[1],
                )
            axs[1].plot(ffg1.eps, ffg1.cs2, linestyle="dashed", color=nuda.param.col[1])
            axs[1].plot(
                ffg1.eps,
                ffg1.cs2_nr,
                linestyle="None",
                marker="o",
                color=nuda.param.col[1],
            )
        if nuda.env.verb_output:
            ffg1.print_outputs()
        #
    axs[1].text(300, 0.07, r"$m=$" + str(mss[0]) + "$m_N$", rotation=3)
    axs[1].text(240, 0.12, r"$m=$" + str(mss[1]) + "$m_N$", rotation=4)
    axs[1].text(180, 0.20, r"$m=$" + str(mss[2]) + "$m_N$", rotation=5)
    # axs[1,0].legend(loc='upper right',fontsize='xx-small')
    fig.legend(
        loc="upper left",
        bbox_to_anchor=(0.15, 0.97),
        fontsize="8",
        ncol=4,
        frameon=False,
    )
    #
    if pname is not None:
        plt.savefig(pname, dpi=300)
        plt.close()
    #
