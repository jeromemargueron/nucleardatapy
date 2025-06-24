import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def crust_setupCrust_fig( pname, models ):
    """
    Plot hyper-nuclear chart (N versus Z).\
    The plot is 1x2 with:\
    [0]: nuclear chart.

    :param pname: name of the figure (*.png)
    :type pname: str.
    :param models: table.
    :type models: str.

    """
    #
    print(f'Plot name: {pname}')
    #
    fig, axs = plt.subplots(1,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.10, bottom=0.12, right=None, top=0.78, wspace=0.3, hspace=0.3 )
    #
    axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    axs[0].set_ylabel(r'$e_\text{int}(n_\text{nuc})$ (MeV)',fontsize='14')
    axs[0].set_xlim([1e-4, 1e-1])
    axs[0].set_ylim([-2, 10])
    axs[0].set_xscale('log')
    #
    axs[1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    axs[1].set_ylabel(r'$Z$',fontsize='14')
    axs[1].set_xlim([1e-4, 1e-1])
    axs[1].set_ylim([10, 100])
    axs[1].set_xscale('log')
    #
    for model in models:
        #
        print('model:',model)
        crust = nuda.crust.setupCrust( model = model )
        if crust.e2a_int is not None: 
            axs[0].plot( crust.den, crust.e2a_int, label=crust.label, linestyle=crust.linestyle )
        if crust.Z is not None: 
            axs[1].plot( crust.den, crust.Z, linestyle=crust.linestyle )
    #axs[0].legend(loc='upper left',fontsize='8', ncol=1)
    #axs[1].legend(loc='upper left',fontsize='8', ncol=1)
    fig.legend(loc='upper left',bbox_to_anchor=(0.08,1.01),columnspacing=2,fontsize='7.5',ncol=4,frameon=False)
    #
    if pname is not None:
    	plt.savefig(pname, dpi=200)
    	plt.close()
    #
