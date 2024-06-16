
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nudy

def main():
    #
    print(50*'-')
    print("Enter plot_SetupISGMR.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    # plot name:
    #
    pname = 'figs/plot_SetupISGMR.png'
    print(f'Plot name: {pname}')
    #
    # plot
    #
    fig, axs = plt.subplots(1,3)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.15, right=None, top=0.85, wspace=0.3, hspace=0.3)
    #
    axs[0].set_title(r'Zr')
    axs[0].set_ylabel(r'$E_{ISGMR}$')
    axs[0].set_xlabel(r'A')
    axs[0].set_xlim([88, 96])
    axs[0].set_ylim([15, 18.5])
    #
    axs[1].set_title(r'Sn')
    axs[1].set_xlabel(r'A')
    axs[1].set_xlim([110, 136])
    axs[1].set_ylim([14, 16.5])
    #
    axs[2].set_title(r'Pb')
    axs[2].set_xlabel(r'A')
    axs[2].set_xlim([202, 210])
    axs[2].set_ylim([13, 14])
    #
    tables, tables_lower = nudy.tables_isgmr()
    #
    for table in tables:
        #
        print('Table:',table)
        gmr = nudy.SetupISGMR( table = table )
        #print('A[gmr.Z==40]:',gmr.A[gmr.Z==40])
        #print('E_cen[gmr.Z==40]:',gmr.E_cen[gmr.Z==40])
        #print('E_errp[gmr.Z==40]:',gmr.E_errp[gmr.Z==40])
        if any(gmr.E_cen[gmr.Z==40]): axs[0].errorbar( gmr.A[gmr.Z==40], gmr.E_cen[gmr.Z==40], yerr=[gmr.E_errp[gmr.Z==40],gmr.E_errm[gmr.Z==40]], fmt='o', label=gmr.label )
        if any(gmr.E_cen[gmr.Z==50]): axs[1].errorbar( gmr.A[gmr.Z==50], gmr.E_cen[gmr.Z==50], yerr=[gmr.E_errp[gmr.Z==50],gmr.E_errm[gmr.Z==50]], fmt='o', label=gmr.label )
        if any(gmr.E_cen[gmr.Z==82]): axs[2].errorbar( gmr.A[gmr.Z==82], gmr.E_cen[gmr.Z==82], yerr=[gmr.E_errp[gmr.Z==82],gmr.E_errm[gmr.Z==82]], fmt='o', label=gmr.label )
        nudy.print_outputs_isgmr( gmr )
    #
    axs[0].legend(loc='upper right',fontsize='xx-small')
    #
    plt.savefig(pname)
    plt.close()

    print(50*'-')
    print("Exit plot_SetupISGMR.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
