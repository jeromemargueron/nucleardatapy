import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def eos_setupCSEoS_pvse_fig( pname ):
    """
    Plot the EoS with crust and core parts.

    The plot is 1x1.

    [0]: pressure as a function of the energy density.

    :param pname: name of the figure (*.png)
    :type pname: str.
    """
    #
    print(f'Plot name: {pname}')
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=0.95, top=0.95, wspace=0.05, hspace=0.05 )
    #
    axs.set_xlabel(r'$\epsilon_\text{tot}$ (MeV fm$^{-3}$)',fontsize='14')
    axs.set_ylabel(r'$p_\text{tot}$ (MeV fm$^{-3}$)',fontsize='14')
    #axs.set_xlim([1.e-2, 2.e3])
    #axs.set_ylim([1.e-5, 2.e3])
    #axs.set_tick_params('y', right=True)
    #axs.set_tick_params('x', top=True)
    axs.set_xscale('log')
    axs.set_yscale('log')
    #
    # check the core EOS against the band in NM
    #
    eos = nuda.eos.setupCSEoS(nuclear_unit=True)
    eos.Final_EoS()
    #
    if eos.pre_tot is not None:
        axs.plot( eos.eps_tot, eos.pre_tot )
    #
    fig.legend(loc='upper left',bbox_to_anchor=(0.2,0.9),fontsize='10')
    #fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=3,frameon=False)
    #
    if pname is not None: 
        fig.savefig(pname, dpi=200)
        plt.close()
    #

