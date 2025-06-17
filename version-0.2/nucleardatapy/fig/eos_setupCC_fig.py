import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def eos_setupCC_eos_fig( pname, band, crust_model, core_kind, core_model, core_param, connect, boundaries ):
    """
    Plot the EoS with crust and core parts.\
    The plot is 1x1.

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
    print(f'Plot name: {pname}')
    #
    p_den = 312.0
    p_cen = 12.5
    p_std = 11.0
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=0.95, top=0.90, wspace=0.05, hspace=0.05 )
    #
    axs.set_xlabel(r'$\epsilon_\text{tot}$ (MeV fm$^{-3}$)')
    axs.set_ylabel(r'$p_\text{tot}$ (MeV fm$^{-3}$)')
    axs.set_xlim([0, 350])
    axs.set_ylim([-2, 30])
    #axs.set_tick_params('y', right=True)
    #axs.set_tick_params('x', top=True)
    #axs.set_xscale('log')
    #axs.set_yscale('log')
    #
    eos_cc = nuda.eos.setupCC( crust_model = crust_model, core_kind=core_kind, core_model = core_model, core_param = core_param, connect = connect, boundaries = boundaries )
    #
    if core_kind == 'micro':
        eos = nuda.eos.setupAMBeq( model = core_model, kind = core_kind )
    elif core_kind == 'pheno':
        eos = nuda.eos.setupAMBeq( model = core_model, param = core_param, kind = core_kind )
    else:
        print('eos_setupCC_fig.py: core_kind ',core_kind,' is ill defined.')
        print('eos_setupCC_fig.py: -- Exit the code --')
        exit()
    #        
    check = nuda.matter.setupCheck( eos = eos, band = band )
    #
    if check.isInside:
        lstyle = 'solid'
    else:
        lstyle = 'dashed'
    #
    if eos_cc.pre is not None: 
        axs.plot( eos_cc.eps, eos_cc.pre, marker='o', linestyle=lstyle, markevery=eos_cc.every )
    #
    axs.errorbar( p_den, p_cen, yerr=p_std, color='k', linewidth = 3 )
    #
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=5,frameon=False)
    #
    if pname is not None: 
        plt.savefig(pname, dpi=200)
        plt.close()
    #