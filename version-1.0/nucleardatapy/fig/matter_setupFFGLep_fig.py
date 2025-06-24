import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import nucleardatapy as nuda

mpl.use("Agg")  # Use a non-interactive backend

def matter_setupFFGLep_fig( pname, den_el=None, den_mu1=None, den_mu2=None, den_mu3=None ):
    """
    Plot leptonic FFG energy per particle E/A and pressure in NM and SM.\
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
    if den_el is None: den_el=np.linspace(0.01, 0.1, num=20)
    if den_mu1 is None: den_mu1 = 0.1*np.linspace(0.01, 0.1, num=20) 
    if den_mu2 is None: den_mu2 = 0.2*np.linspace(0.01, 0.1, num=20) 
    if den_mu3 is None: den_mu3 = 0.5*np.linspace(0.01, 0.1, num=20) 
    #
    fig, axs = plt.subplots(2, 1)
    fig.tight_layout()  # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust( left=0.12, bottom=0.12, right=None, top=0.9, wspace=0.05, hspace=0.05 )
    #
    axs[0].set_ylabel(r"$e^\text{FFG}$ (MeV)", fontsize="14")
    axs[0].set_xlim([0, 0.1])
    axs[0].set_ylim([0, 200])
    axs[0].tick_params("x", labelbottom=False)
    #
    axs[1].set_xlabel(r"$n_\text{el}$ (fm$^{-3}$)", fontsize="14")
    axs[1].set_ylabel(r"$p^\text{FFG}$ (MeV fm$^{-3}$)", fontsize="14")
    axs[1].set_xlim([0, 0.1])
    axs[1].set_ylim([-0.01, 6])
    #
    lep1 = nuda.matter.setupFFGLep( den_el=den_el, den_mu=den_mu1 )
    lep2 = nuda.matter.setupFFGLep( den_el=den_el, den_mu=den_mu2 )
    lep3 = nuda.matter.setupFFGLep( den_el=den_el, den_mu=den_mu3 )
    #
    if any(lep1.e2n_el):
        print(r"plot $\delta=0$ (SM)")
        axs[0].plot( lep1.den_el, lep1.e2n_el, linestyle="solid",  color=nuda.param.col[0], label='electrons' )
        axs[0].plot( lep1.den_el, lep1.e2n_mu, linestyle="dashed", color=nuda.param.col[1], label='muons (10%)' )
        axs[0].plot( lep1.den_el, lep2.e2n_mu, linestyle="dashed", color=nuda.param.col[2], label='muons (20%)' )
        axs[0].plot( lep1.den_el, lep3.e2n_mu, linestyle="dashed", color=nuda.param.col[3], label='muons (50%)' )
        axs[1].plot( lep1.den_el, lep1.pre_el, linestyle="solid",  color=nuda.param.col[0] )
        axs[1].plot( lep1.den_el, lep1.pre_mu, linestyle="dashed", color=nuda.param.col[1] )
        axs[1].plot( lep1.den_el, lep2.pre_mu, linestyle="dashed", color=nuda.param.col[2] )
        axs[1].plot( lep1.den_el, lep3.pre_mu, linestyle="dashed", color=nuda.param.col[3] )
        if nuda.env.verb_output: lep.print_outputs()
        #
    #axs[0, 0].text(0.2, 16, r"$m=$" + str(mss[0]) + "$m_N$", rotation=8)
    #axs[0, 0].text(0.2, 32, r"$m=$" + str(mss[1]) + "$m_N$", rotation=13)
    #axs[0, 0].text(0.2, 50, r"$m=$" + str(mss[2]) + "$m_N$", rotation=20)
    axs[0].legend(loc='lower right',fontsize='10')
    #fig.legend( loc="upper left", bbox_to_anchor=(0.2, 0.97), fontsize="6", ncol=4, frameon=False )
    #
    if pname is not None:
        plt.savefig(pname, dpi=300)
        plt.close()
    #
