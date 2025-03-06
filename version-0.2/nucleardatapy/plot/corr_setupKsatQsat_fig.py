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
    fig.subplots_adjust(left=0.15, bottom=0.12, right=None, top=0.98, wspace=0.3, hspace=0.3)
    #
    axs.set_xlabel(r'$K_\mathrm{sat}$ (MeV)')
    axs.set_ylabel(r'$Q_\mathrm{sat}$ (MeV)')
    axs.set_xlim([190, 360])
    axs.set_ylim([-1000, 1500])
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
        if k == 2:
            kk = 0
        else:
            kk = k
        axs.scatter( kq.Ksat, kq.Qsat, label=kq.label, color=nuda.param.col[kk], marker=kq.marker )
        x = np.linspace(min(kq.Ksat),max(kq.Ksat),10)
        if k == 3 or k == 4 or k == 5:
            axs.plot( x, nuda.corr.flinear(x,kq.m,kq.c), color=nuda.param.col[kk], linestyle='dashed' )
        else:
            axs.plot( x, nuda.corr.flinear(x,kq.m,kq.c), color=nuda.param.col[kk], linestyle='solid' )
        #
        if nuda.env.verb: kq.print_outputs( )
    #
    axs.legend(loc='upper left',ncol=3, fontsize='9')
    #
    if pname is not None: 
        plt.savefig(pname, dpi=200)
        plt.close()
