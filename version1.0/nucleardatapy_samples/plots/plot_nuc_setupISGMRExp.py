
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plot_nuc_setupISGMRExp( pname, tables ):
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
    #axs[0].set_xlim([88, 96])
    axs[0].set_ylim([13, 18])
    #
    axs[1].set_title(r'Sn')
    axs[1].set_xlabel(r'A')
    #axs[1].set_xlim([110, 136])
    axs[1].set_ylim([13, 18])
    #
    axs[2].set_title(r'Pb')
    axs[2].set_xlabel(r'A')
    #axs[2].set_xlim([202, 210])
    axs[2].set_ylim([13, 18])
    #
    nucZ = [ 40, 50, 82 ]
    #
    for k,table in enumerate( tables ):
        #
        print('Table:',table)
        gmr = nuda.nuc.setupISGMRExp( table = table )
        #print('A[gmr.Z==40]:',gmr.A[gmr.Z==40])
        #print('E_cen[gmr.Z==40]:',gmr.E_cen[gmr.Z==40])
        #print('E_errp[gmr.Z==40]:',gmr.E_errp[gmr.Z==40])
        for i in [0,1,2]:
            print('For Z = ',nucZ[i])
            nucA = []; cent = []; errp = []; errm = [];
            for ind,A in enumerate(gmr.isgmr['A']):
                if int( gmr.isgmr['Z'][ind] ) == nucZ[i] and gmr.isgmr['M12Mm1'][ind] is not None:
                    nucA.append( int(A)+0.2*k )
                    cent.append( float( gmr.isgmr['M12Mm1'][ind] ) )
                    errp.append( float( gmr.isgmr['M12Mm1_errp'][ind] ) )
                    errm.append( float( gmr.isgmr['M12Mm1_errm'][ind] ) )
            print('A:',nucA)
            print('cent:',cent)
            print('errp:',errp)
            print('errm:',errm)
            axs[i].errorbar( nucA, cent, yerr=errp, fmt='o', label=gmr.label )
    #
    axs[2].legend(loc='upper right',fontsize='xx-small')
    #
    plt.savefig(pname, dpi=200)
    plt.close()

def main():
    #
    print(50*'-')
    print("Enter plot_nuc_setupISGMRExp.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    #tables, tables_lower = nuda.nuc.isgmr_exp_tables()
    tables = [ '2010-ISGMR-LI', '2018-ISGMR-GARG-LATEX' ]
    #
    pname = 'figs/plot_nuc_setupISGMRExp.png'
    #
    plot_nuc_setupISGMRExp( pname, tables )
    #
    print(50*'-')
    print("Exit plot_nuc_setupISGMRExp.py:")
    print(50*'-')
    #

if __name__ == "__main__":
    main()
