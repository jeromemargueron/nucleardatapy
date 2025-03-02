
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plot_nuc_setupRchExp( pname, tables ):
    #
    # plot
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
        Nref, Aref, Rchref, Rchref_err = rch.Rch_isotopes( Zref = Zref )
        print('Nref:',Nref)
        print('Aref:',Aref)
        print('Rchref:',Rchref)
        print('Rchref_err:',Rchref_err)
        #if any(Nref): 
        axs[0].errorbar( Aref, Rchref, yerr=Rchref_err, fmt='o', label=rch.label )
        #
        Zref = 50
        print('For Zref:',Zref)
        Nref, Aref, Rchref, Rchref_err = rch.Rch_isotopes( Zref = Zref )
        print('Nref:',Nref)
        print('Aref:',Aref)
        print('Rchref:',Rchref)
        print('Rchref_err:',Rchref_err)
        #if any(Nref): 
        axs[1].errorbar( Aref, Rchref, yerr=Rchref_err, fmt='o', label=rch.label )
        #
        Zref = 82
        print('For Zref:',Zref)
        Nref, Aref, Rchref, Rchref_err = rch.Rch_isotopes( Zref = Zref )
        print('Nref:',Nref)
        print('Aref:',Aref)
        print('Rchref:',Rchref)
        print('Rchref_err:',Rchref_err)
        #if any(Nref): 
        axs[2].errorbar( Aref, Rchref, yerr=Rchref_err, fmt='o', label=rch.label )
    #
    #axs.text(0.15,12,r'$K_{sym}$='+str(int(Ksym))+' MeV',fontsize='12')
    axs[0].legend(loc='upper left',fontsize='8')
    #
    plt.savefig(pname, dpi=200)
    plt.close()
    #


def main():
    #
    print(50*'-')
    print("Enter plot_nuc_setupRchExp.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    tables, tables_lower = nuda.nuc.rch_exp_tables()
    #
    pname = 'figs/plot_nuc_setupRchExp.png'
    #
    plot_nuc_setupRchExp( pname, tables )
    #
    print(50*'-')
    print("Exit plot_nuc_setupRchExp.py:")
    print(50*'-')
    #

    
if __name__ == "__main__":
    main()
