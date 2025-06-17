import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def nuc_setupRchTheo_fig( pname, tables, table_exp ):
    """
    Plot nuclear chart (N versus Z).\
    The plot is 1x1 with:\
    [0]: nuclear chart.

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
    for indT,table in enumerate(tables):
        #
        rch = nuda.nuc.setupRchTheo( table = table )
        #
        for indZ,Zref in enumerate(Zrefs):
            print('For Zref:',Zref)
            rchIsot = nuda.nuc.setupRchTheoIsotopes( rch, Zref = Zref )
            if indZ == 0:
                axs.plot( rchIsot.N, rchIsot.Rch, color=nuda.param.col[indT], label=rch.label )
            else:
                axs.plot( rchIsot.N, rchIsot.Rch, color=nuda.param.col[indT] )                
            #if indT == 0 and indZ == 0:
            #    axs.plot( rchIsot.N, nuda.nuc.rch_emp( rchIsot.A, rchIsot.Z, 'classic' ), linestyle='dashed', color='k', label='empirical(classic)' )
            #else:
            #    axs.plot( rchIsot.N, nuda.nuc.rch_emp( rchIsot.A, rchIsot.Z, 'classic' ), linestyle='dashed', color='k' )
            #
    #
    for indZ,Zref in enumerate(Zrefs):
        rchExpIsot = nuda.nuc.setupRchExpIsotopes( rch_exp, Zref = Zref )
        if indZ == 0:
            axs.errorbar( rchExpIsot.N, rchExpIsot.Rch, yerr=rchExpIsot.Rch_err, color='k', fmt='s', markersize=3, label=table_exp )
            axs.plot( rchExpIsot.N, nuda.nuc.rch_emp( rchExpIsot.A, rchExpIsot.Z, 'classic' ), linestyle='dashed', color='k', label='empirical(classic)' )
            axs.plot( rchExpIsot.N, nuda.nuc.rch_emp( rchExpIsot.A, rchExpIsot.Z, '1994-NPP' ), linestyle='dashed', color='red', label='empirical(NPP-1994)' )
            axs.plot( rchExpIsot.N, nuda.nuc.rch_emp( rchExpIsot.A, rchExpIsot.Z, '2013-BAKS-1' ), linestyle='dotted', color='k', label='empirical(BAKS-1-2013)' )
            axs.plot( rchExpIsot.N, nuda.nuc.rch_emp( rchExpIsot.A, rchExpIsot.Z, '2013-BAKS-3' ), linestyle='dotted', color='red', label='empirical(BAKS-3-2013)' )
        else:
            axs.errorbar( rchExpIsot.N, rchExpIsot.Rch, yerr=rchExpIsot.Rch_err, color='k', fmt='s', markersize=3 )
            axs.plot( rchExpIsot.N, nuda.nuc.rch_emp( rchExpIsot.A, rchExpIsot.Z, 'classic' ), linestyle='dashed', color='k' )
            axs.plot( rchExpIsot.N, nuda.nuc.rch_emp( rchExpIsot.A, rchExpIsot.Z, '1994-NPP' ), linestyle='dashed', color='red' )
            axs.plot( rchExpIsot.N, nuda.nuc.rch_emp( rchExpIsot.A, rchExpIsot.Z, '2013-BAKS-1' ), linestyle='dotted', color='k' )
            axs.plot( rchExpIsot.N, nuda.nuc.rch_emp( rchExpIsot.A, rchExpIsot.Z, '2013-BAKS-3' ), linestyle='dotted', color='red' )
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

def nuc_setupRchTheo_3Zref_fig( pname, tables, table_exp ):
    """
    Plot nuclear chart (N versus Z).\
    The plot is 1x1 with:\
    [0]: nuclear chart.

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
    rch_exp = nuda.nuc.setupRchExp( table = table_exp )
    #
    fig, axs = plt.subplots(1,3)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.15, right=None, top=0.9, wspace=0.35, hspace=0.3)
    #
    axs[0].set_title(r'Zr')
    axs[0].set_ylabel(r'$R_{ch}$ (fm)',fontsize='14')
    axs[0].set_xlabel(r'A',fontsize='14')
    axs[0].set_xlim([88, 98])
    axs[0].set_ylim([4.25, 4.45])
    #
    axs[1].set_title(r'Sn')
    axs[1].set_xlabel(r'A')
    axs[1].set_xlim([110, 136])
    axs[1].set_ylim([4.55, 4.75])
    #
    axs[2].set_title(r'Pb')
    axs[2].set_xlabel(r'A')
    axs[2].set_xlim([202, 210])
    axs[2].set_ylim([5.45, 5.55])
    #
    Zrefs = [ 40, 50, 82 ]
    for table in tables:
        #
        rch = nuda.nuc.setupRchTheo( table = table )
        #
        for ind,Zref in enumerate(Zrefs):
            print('For Zref:',Zref)
            rchIsot = nuda.nuc.setupRchTheoIsotopes( rch, Zref = Zref )
            axs[ind].plot( rchIsot.A, rchIsot.Rch, label=rch.label )
            rchIsot = nuda.nuc.setupRchExpIsotopes( rch_exp, Zref = 40 )
            axs[ind].errorbar( rchIsot.A, rchIsot.Rch, yerr=rchIsot.Rch_err, fmt='o', label=rchIsot.label )
            axs[ind].legend(loc='upper left',fontsize='7',frameon=False)
    #
    if pname is not None:
    	plt.savefig(pname, dpi=200)
    	plt.close()
    #
