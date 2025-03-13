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
    fig, axs = plt.subplots(1,3)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.15, right=None, top=0.9, wspace=0.35, hspace=0.3)
    #
    axs[0].set_title(r'Zr')
    axs[0].set_ylabel(r'$R_{ch}$')
    axs[0].set_xlabel(r'A')
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
    for table in tables:
        #
        rch = nuda.nuc.setupRchTheo( table = table )
        #
        Zref = 40
        print('For Zref:',Zref)
        #Nref, Aref, Rchref = rch.Rch_isotopes( Zref = Zref )
        rchIsot = nuda.nuc.setupRchTheoIsotopes( rch, Zref = Zref )
        #print('Nref:',Nref)
        #print('Aref:',Aref)
        #print('Rchref:',Rchref)
        #if any(Nref): 
        #axs[0].plot( Aref, Rchref, label=rch.label )
        axs[0].plot( rchIsot.A, rchIsot.Rch, label=rch.label )
        #
        Zref = 50
        print('For Zref:',Zref)
        #Nref, Aref, Rchref = rch.Rch_isotopes( Zref = Zref )
        rchIsot = nuda.nuc.setupRchTheoIsotopes( rch, Zref = Zref )
        #print('Nref:',Nref)
        #print('Aref:',Aref)
        #print('Rchref:',Rchref)
        #if any(Nref): 
        #axs[1].plot( Aref, Rchref, label=rch.label )
        axs[1].plot( rchIsot.A, rchIsot.Rch )
        #
        Zref = 82
        print('For Zref:',Zref)
        #Nref, Aref, Rchref = rch.Rch_isotopes( Zref = Zref )
        rchIsot = nuda.nuc.setupRchTheoIsotopes( rch, Zref = Zref )
        #print('Nref:',Nref)
        #print('Aref:',Aref)
        #print('Rchref:',Rchref)
        #if any(Nref): 
        #axs[2].plot( Aref, Rchref, label=rch.label )
        axs[2].plot( rchIsot.A, rchIsot.Rch )
    #
    #Nref_exp, Aref_exp, Rchref_exp, Rchref_err_exp = rch_exp.Rch_isotopes( Zref = 40 )
    rchIsot = nuda.nuc.setupRchExpIsotopes( rch_exp, Zref = 40 )
    axs[0].errorbar( rchIsot.A, rchIsot.Rch, yerr=rchIsot.Rch_err, fmt='o', label=rchIsot.label )
    #Nref_exp, Aref_exp, Rchref_exp, Rchref_err_exp = rch_exp.Rch_isotopes( Zref = 50 )
    rchIsot = nuda.nuc.setupRchExpIsotopes( rch_exp, Zref = 50 )
    axs[1].errorbar( rchIsot.A, rchIsot.Rch, yerr=rchIsot.Rch_err, fmt='o', label=rchIsot.label )
    #Nref_exp, Aref_exp, Rchref_exp, Rchref_err_exp = rch_exp.Rch_isotopes( Zref = 82 )
    rchIsot = nuda.nuc.setupRchExpIsotopes( rch_exp, Zref = 82 )
    axs[2].errorbar( rchIsot.A, rchIsot.Rch, yerr=rchIsot.Rch_err, fmt='o', label=rchIsot.label )
    #axs.text(0.15,12,r'$K_{sym}$='+str(int(Ksym))+' MeV',fontsize='12')
    axs[0].legend(loc='upper left',fontsize='7',frameon=False)
    axs[1].legend(loc='upper left',fontsize='7',frameon=False)
    axs[2].legend(loc='upper left',fontsize='7',frameon=False)
    #axs[0].legend(loc='upper left',bbox_to_anchor=(0.1,0.9),columnspacing=2,fontsize='10',ncol=2,frameon=False)
    #fig.legend(loc='upper left',bbox_to_anchor=(0.1,1.0),columnspacing=2,fontsize='7',ncol=4,frameon=False)
    #
    if pname is not None:
    	plt.savefig(pname, dpi=200)
    	plt.close()
    #