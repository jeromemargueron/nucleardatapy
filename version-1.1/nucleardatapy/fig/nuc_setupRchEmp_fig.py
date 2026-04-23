import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def nuc_setupRchEmp_fig( pname, formulas, table_exp ):
    """
    Plot the empirical charge radii and compare to the experimental value.

    The plot is 1x1 with:

    [0]: Rch as a function of N.

    :param pname: name of the figure (*.png)
    :type pname: str.
    :param formulas: empirical formulas.
    :type formulas: array of str.
    :param table_exp: experimental table.
    :type table_exp: str.
    """
    #
    print(f'Plot name: {pname}')
    #
    rch_exp = nuda.nuc.setupRchExp( table = table_exp )
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.15, right=None, top=0.9, wspace=0.35, hspace=0.3)
    #
    axs.set_ylabel(r'$R_{ch}$ (fm)',fontsize='14')
    axs.set_xlabel(r'N',fontsize='14')
    axs.set_xlim([10, 160])
    axs.set_ylim([3.0, 6.5])
    #
    Zrefs = [ 20, 28, 40, 50, 60, 70, 82, 90 ]
    #
    for indZ,Zref in enumerate(Zrefs):
        #
        rchExpIsot = nuda.nuc.setupRchExpIsotopes( rch_exp, Zref = Zref )
        nucN = rchExpIsot.N
        nucA = rchExpIsot.A
        nucZ = rchExpIsot.Z
        #
        clas  = nuda.nuc.setupRchEmp( nucA, nucZ, formula = 'classic' )
        npp   = nuda.nuc.setupRchEmp( nucA, nucZ, formula = '1994-NPP' )
        angel = nuda.nuc.setupRchEmp( nucA, nucZ, formula = '2004-Angeli' )
        baks1 = nuda.nuc.setupRchEmp( nucA, nucZ, formula = '2013-BAKS-1' )
        baks3 = nuda.nuc.setupRchEmp( nucA, nucZ, formula = '2013-BAKS-3' )
        #
        if indZ == 0:
            axs.errorbar( nucN, rchExpIsot.Rch, yerr=rchExpIsot.Rch_err, color='k', fmt='s', markersize=3, label=table_exp )
            axs.plot( nucN, clas.nucRch, linestyle='dashed', color='k', label=clas.label )
            axs.plot( nucN, npp.nucRch, linestyle='dashed', color='red', label=npp.label )
            axs.plot( nucN, angel.nucRch, linestyle='dashed', color='blue', label=angel.label )
            axs.plot( nucN, baks1.nucRch, linestyle='dotted', color='k', label=baks1.label )
            axs.plot( nucN, baks3.nucRch, linestyle='dotted', color='red', label=baks3.label )
        else:
            axs.errorbar( nucN, rchExpIsot.Rch, yerr=rchExpIsot.Rch_err, color='k', fmt='s', markersize=3 )
            axs.plot( nucN, clas.nucRch, linestyle='dashed', color='k' )
            axs.plot( nucN, npp.nucRch, linestyle='dashed', color='red' )
            axs.plot( nucN, angel.nucRch, linestyle='dashed', color='blue' )
            axs.plot( nucN, baks1.nucRch, linestyle='dotted', color='k' )
            axs.plot( nucN, baks3.nucRch, linestyle='dotted', color='red' )
    #
    axs.legend(loc='lower right',fontsize='10',ncol=2,frameon=False)
    #
    axs.text( 50,3.7,'Ca')
    axs.text( 70,4.2,'Ni')
    axs.text( 95,4.6,'Zr')
    axs.text(118,5.0,'Sn')
    axs.text( 50,4.8,'Nd')
    axs.text( 62,5.1,'Yb')
    axs.text( 88,5.3,'Pb')
    axs.text(120,5.7,'Ac')
    #
    if pname is not None:
        plt.savefig(pname, dpi=200)
        plt.close()
    #