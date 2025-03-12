import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def matter_setupMicro_effmass_fig( pname, models, matter = 'NM' ):
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
    print(f'Plot name: {pname}')
    print('models:',models)
    print('matter:',matter)
    #
    fig, axs = plt.subplots(1,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.8, wspace=0.05, hspace=0.05 )
    #
    axs[0].set_ylabel(r'Landau effective mass $m^*/m$')
    axs[0].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)')
    axs[0].set_xlim([0, 0.34])
    axs[0].set_ylim([0.4, 1.2])
    #axs[0].tick_params('x', labelbottom=False)
    #
    axs[1].set_xlim([0, 2.0])
    axs[1].set_ylim([0.4, 1.2])
    #axs[1].tick_params('x', labelbottom=False)
    axs[1].tick_params('y', labelleft=False)
    axs[1].set_xlabel(r'$k_{F_n}$ (fm$^{-1}$)')
    #
    #axs[1,0].set_ylabel(r'$\Delta_{1S0}/E_F$')
    #
    for model in models:
        #
        ms = nuda.matter.setupMicroEffmass( model = model, matter = matter )
        #
        if matter.lower() == 'nm':
            if ms.nm_effmass is not None:
                if ms.nm_effmass_err is not None:
                    axs[0].errorbar( ms.nm_den, ms.nm_effmass, yerr=ms.nm_effmass_err, marker=ms.marker, markevery=ms.every, linestyle='none', label=ms.label )
                    axs[1].errorbar( ms.nm_kfn, ms.nm_effmass, yerr=ms.nm_effmass_err, marker=ms.marker, markevery=ms.every, linestyle='none' )
                else:
                    axs[0].plot( ms.nm_den, ms.nm_effmass, marker=ms.marker, markevery=ms.every, linestyle='none', label=ms.label )
                    axs[1].plot( ms.nm_kfn, ms.nm_effmass, marker=ms.marker, markevery=ms.every, linestyle='none' )
        elif matter.lower() == 'sm':
            if ms.sm_effmass is not None:
                if ms.sm_effmass_err is not None:
                    axs[0].errorbar( ms.sm_den, ms.sm_effmass, yerr=ms.sm_effmass_err, marker=ms.marker, markevery=ms.every, linestyle='none', label=ms.label )
                    axs[1].errorbar( ms.sm_kfn, ms.sm_effmass, yerr=ms.sm_effmass_err, marker=ms.marker, markevery=ms.every, linestyle='none' )
                else:
                    axs[0].plot( ms.sm_den, ms.sm_effmass, marker=ms.marker, markevery=ms.every, linestyle='none', label=ms.label )
                    axs[1].plot( ms.sm_kfn, ms.sm_effmass, marker=ms.marker, markevery=ms.every, linestyle='none' )
        if nuda.env.verb_output: ms.print_outputs( )
    #
    #axs[1,0].legend(loc='upper right',fontsize='8')
    fig.legend(loc='upper left',bbox_to_anchor=(0.08,1.0),columnspacing=2,fontsize='8',ncol=3,frameon=False)
    #
    if pname is not None:
    	plt.savefig(pname, dpi=300)
    	plt.close()
