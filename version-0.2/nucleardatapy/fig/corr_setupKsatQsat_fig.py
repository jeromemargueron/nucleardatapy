import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def corr_setupKsatQsat_fig( pname, constraints ):
    """
    Plot the correlation between Ksat and Qsat.\
    The plot is 1x1 with:\
    [0]: Ksat - Qsat correlation plot

    :param pname: name of the figure (*.png)
    :type pname: str.
    :param constraints: list of constraints to run on.
    :type constraints: array of str.

    """
    #
    print(f'Plot name: {pname}')
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.15, bottom=0.12, right=0.95, top=0.98, wspace=0.3, hspace=0.3)
    #
    axs.set_xlabel(r'$K_\mathrm{sat}$ (MeV)',fontsize='14')
    axs.set_ylabel(r'$Q_\mathrm{sat}$ (MeV)',fontsize='14')
    axs.set_xlim([100, 360])
    axs.set_ylim([-2500, 2200])
    #axs.tick_params(labelbottom=True, labeltop=False, labelleft=True, labelright=False,
    #                 bottom=True, top=True, left=True, right=True)
#    axs.xaxis.set_major_locator(MultipleLocator(5))
    #axs.xaxis.set_major_formatter(FormatStrFormatter('%d'))
#    axs.xaxis.set_minor_locator(MultipleLocator(1))
#    axs.yaxis.set_major_locator(MultipleLocator(20))
#    axs.yaxis.set_minor_locator(MultipleLocator(5))
#    axs.tick_params(axis = 'both', which='major', length=10, width=1, direction='inout', right = True, left = True, bottom = True, top = True)
#    axs.tick_params(axis = 'both', which='minor', length=5,  width=1, direction='in', right = True, left = True, bottom = True, top = True )
    #
    for k,constraint in enumerate(constraints):
        #
        print('constraint:',constraint)
        kq = nuda.corr.setupKsatQsat( constraint = constraint )
        if nuda.env.verb: print('Ksat:',kq.Ksat)
        if nuda.env.verb: print('Qsat:',kq.Qsat)
        if nuda.env.verb: print('len(Ksat):',kq.Ksat.size)
        #
        #if k == 2:
        #    kk = 0
        #else:
        #    kk = k
        if k == 5 or k == 9 or k == 10 or k == 11: 
            lstyle = 'dashed'
        else:
            lstyle = 'solid'
        if kq.Ksat is not None:
            axs.scatter( kq.Ksat, kq.Qsat, label=kq.label, color = nuda.param.col[k], marker = kq.marker )
        if kq.Ksat_lin is not None:
            axs.plot( kq.Ksat_lin, kq.Qsat_lin, color = nuda.param.col[k], linestyle = lstyle )
        if kq.Ksat_band is not None:
            axs.fill_between( kq.Ksat_band, kq.Qsat_lo, kq.Qsat_up, label=kq.label, color = nuda.param.col[k], alpha = 0.2 )
        #
        if nuda.env.verb: kq.print_outputs( )
    #
    axs.legend(loc='upper left',ncol=4, fontsize='10')
    #
    if pname is not None: 
        plt.savefig(pname, dpi=200)
        plt.close()
