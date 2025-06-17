import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def nuc_setupRchExp_fig( pname, tables ):
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
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.15, right=None, top=0.85, wspace=0.3, hspace=0.3)
    #
    axs.set_ylabel(r'$R_{ch}$ (fm)',fontsize='14')
    axs.set_xlabel(r'N',fontsize='14')
    axs.set_xlim([10, 140])
    axs.set_ylim([3.2, 5.8])
    #
    Zrefs = [ 20, 28, 40, 50, 60, 70, 82 ]
    #
    for table in tables:
        #
        rch = nuda.nuc.setupRchExp( table = table )
        #
        for Zref in Zrefs:
            print('For Zref:',Zref)
            rchIsot = nuda.nuc.setupRchExpIsotopes( rch, Zref = Zref )
            axs.errorbar( rchIsot.N, rchIsot.Rch, yerr=rchIsot.Rch_err, fmt='s', markersize=3, label=nuda.param.elements[int(Zref)-1] )
            #axs.errorbar( rchIsot.N, rchIsot.Rch, yerr=rchIsot.Rch_err, fmt='o', label=rchIsot.label )
    #
    #axs.text(0.15,12,r'$K_{sym}$='+str(int(Ksym))+' MeV',fontsize='12')
    axs.legend(loc='upper left',fontsize='8')
    #
    if pname is not None:
    	plt.savefig(pname, dpi=200)
    	plt.close()
    #

def nuc_setupRchExp_3Zref_fig( pname, tables ):
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
    fig, axs = plt.subplots(1,3)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.15, right=None, top=0.85, wspace=0.3, hspace=0.3)
    #
    axs[0].set_title(r'Zr')
    axs[0].set_ylabel(r'$R_{ch}$')
    axs[0].set_xlabel(r'A')
    axs[0].set_xlim([88, 96])
    axs[0].set_ylim([4.2, 4.5])
    #
    axs[1].set_title(r'Sn')
    axs[1].set_xlabel(r'A')
    axs[1].set_xlim([110, 136])
    axs[1].set_ylim([4.5, 4.8])
    #
    axs[2].set_title(r'Pb')
    axs[2].set_xlabel(r'A')
    axs[2].set_xlim([202, 210])
    axs[2].set_ylim([5.4, 5.6])
    #
    for table in tables:
        #
        rch = nuda.nuc.setupRchExp( table = table )
        #
        Zref = 40
        print('For Zref:',Zref)
        #Nref, Aref, Rchref, Rchref_err = rch.Rch_isotopes( Zref = Zref )
        rchIsot = nuda.nuc.setupRchExpIsotopes( rch, Zref = Zref )
        #print('Nref:',Nref)
        #print('Aref:',Aref)
        #print('Rchref:',Rchref)
        #print('Rchref_err:',Rchref_err)
        #if any(Nref): 
        #axs[0].errorbar( Aref, Rchref, yerr=Rchref_err, fmt='o', label=rch.label )
        axs[0].errorbar( rchIsot.A, rchIsot.Rch, yerr=rchIsot.Rch_err, fmt='o', label=rch.label )
        #
        Zref = 50
        print('For Zref:',Zref)
        #Nref, Aref, Rchref, Rchref_err = rch.Rch_isotopes( Zref = Zref )
        rchIsot = nuda.nuc.setupRchExpIsotopes( rch, Zref = Zref )
        #print('Nref:',Nref)
        #print('Aref:',Aref)
        #print('Rchref:',Rchref)
        #print('Rchref_err:',Rchref_err)
        #if any(Nref): 
        #axs[1].errorbar( Aref, Rchref, yerr=Rchref_err, fmt='o', label=rch.label )
        axs[1].errorbar( rchIsot.A, rchIsot.Rch, yerr=rchIsot.Rch_err, fmt='o' )
        #
        Zref = 82
        print('For Zref:',Zref)
        #Nref, Aref, Rchref, Rchref_err = rch.Rch_isotopes( Zref = Zref )
        rchIsot = nuda.nuc.setupRchExpIsotopes( rch, Zref = Zref )
        #print('Nref:',Nref)
        #print('Aref:',Aref)
        #print('Rchref:',Rchref)
        #print('Rchref_err:',Rchref_err)
        #if any(Nref): 
        #axs[2].errorbar( Aref, Rchref, yerr=Rchref_err, fmt='o', label=rch.label )
        axs[2].errorbar( rchIsot.A, rchIsot.Rch, yerr=rchIsot.Rch_err, fmt='o' )
    #
    #axs.text(0.15,12,r'$K_{sym}$='+str(int(Ksym))+' MeV',fontsize='12')
    axs[0].legend(loc='upper left',fontsize='8')
    #
    if pname is not None:
        plt.savefig(pname, dpi=200)
        plt.close()
    #
