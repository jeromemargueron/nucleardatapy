import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def corr_setupEsymLsym_fig( pname, constraints, origine ):
    """
    Plot the correlation between Esym and Lsym.\
    The plot is 1x1 with:\
    [0]: Esym - Lsym correlation plot

    :param pname: name of the figure (*.png)
    :type pname: str.
    :param constraints: list of constraints to run on.
    :type constraints: array of str.

    """
    #
    print(f'Plot name: {pname}')
    print('list of constraints:',constraints)
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=0.95, top=0.98, wspace=0.3, hspace=0.3)
    #
    if origine == 'finiteNuclei':
        axs.set_xlabel(r'$E_{\mathrm{sym},2}$ (MeV)',fontsize='14')
        axs.set_ylabel(r'$L_{\mathrm{sym},2}$ (MeV)',fontsize='14')
    elif origine == 'neutronStar':
        axs.set_xlabel(r'$E_\mathrm{sym}$ (MeV)',fontsize='14')
        axs.set_ylabel(r'$L_\mathrm{sym}$ (MeV)',fontsize='14')
    else:
        print('corr_setupEsymLsym_fig.py: origine is not well documented, origine=',origine)
        print('corr_setupEsymLsym_fig.py: exit()')
        exit()
    #
    axs.set_xlim([23, 44])
    axs.set_ylim([10, 120])
    #
    for constraint in constraints:
        #
        print('constraint:',constraint)
        el = nuda.corr.setupEsymLsym( constraint = constraint )
        if nuda.env.verb: print('Esym:',el.Esym,'+-',el.Esym_err)
        if nuda.env.verb: print('Lsym:',el.Lsym,'+-',el.Lsym_err)
        if nuda.env.verb: print('len(Esym):',el.Esym.size)
        #
        if el.plot == 'point_err_xy':
            axs.errorbar( el.Esym, el.Lsym, xerr=el.Esym_err, yerr=el.Lsym_err, linestyle='solid', label=el.label )
        elif el.plot == 'curve':
            axs.plot( el.Esym, el.Lsym, linestyle='solid', linewidth=3, label=el.label )
        elif el.plot == 'contour':
            print('plot:',el.plot)
            print('Esym:',el.Esym)
            print('Lsym:',el.Lsym)
            axs.plot( el.Esym, el.Lsym, linestyle='solid', label=el.label )
        elif el.plot == 'band_y':
            axs.fill_between( el.Esym, y1=el.Lsym-el.Lsym_err, y2=el.Lsym+el.Lsym_err, label=el.label, alpha=el.alpha )
            #axs.errorbar( el.Esym, el.Lsym, xerr=el.Esym_err, linestyle='solid', label=el.label )
        elif el.plot == 'band_x':
            axs.fill_betweenx( el.Lsym, x1=el.Esym-el.Esym_err, x2=el.Esym+el.Esym_err, label=el.label, alpha=el.alpha )
            #axs.errorbar( el.Esym, el.Lsym, yerr=el.Lsym_err, linestyle='solid', label=el.label )
        if nuda.env.verb: el.print_outputs( )
    #
    axs.legend(loc='lower right',fontsize='10')
    #
    if pname is not None:
    	plt.savefig(pname, dpi=300)
    	plt.close()