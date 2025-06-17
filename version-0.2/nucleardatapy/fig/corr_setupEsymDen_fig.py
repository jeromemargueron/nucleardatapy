import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def corr_setupEsymDen_fig( pname, constraints, Ksym, origine ):
    """
    Plot upper boundaries for the tov mass.\
    The plot is 1x1 with:\
    [0]: upper boundary for the mass versus sources.

    :param pname: name of the figure (*.png)
    :type pname: str.
    :param sources: array of sources.
    :type sources: array of str.

    """
    #
    print(f'Plot name: {pname}')
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=0.95, top=0.98, wspace=0.3, hspace=0.3)
    #
    axs.set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)',fontsize='14')
    if origine == 'finiteNuclei':
        axs.set_ylabel(r'$e_{\text{sym},2}(n_\text{nuc})$ (MeV)',fontsize='14')
    elif origine == 'neutronStar':
        axs.set_ylabel(r'$e_\text{sym}(n_\text{nuc})$ (MeV)',fontsize='14')
    else:
        print('corr_setupEsymDen_fig.py: origine is not well documented, origine=',origine)
        print('corr_setupEsymDen_fig.py: exit()')
        exit()
    axs.set_xlim([0.09, 0.27])
    axs.set_ylim([10, 60])
    #
    for constraint in constraints:
        #
        esym = nuda.corr.setupEsymDen( constraint = constraint , Ksym=Ksym )
        #
        #print('Den:',esym.esym_den)
        #print('Esym_max:',esym.esym_e2a_max)
        #print('Esym_min:',esym.esym_e2a_min)
        #
        if esym.plot:
            axs.fill_between( esym.esym_den, y1=esym.esym_e2a_min, y2=esym.esym_e2a_max, label=esym.label, alpha=esym.alpha )
    #
    axs.text(0.15,12,r'$K_\text{sym}$='+str(int(Ksym))+' MeV',fontsize='14')
    axs.legend(loc='lower right',fontsize='9')
    #
    if pname is not None:
    	plt.savefig(pname, dpi=200)
    	plt.close()
    #