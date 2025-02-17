
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
    #axs[0].set_ylim([15, 18.5])
    #
    axs[1].set_title(r'Sn')
    axs[1].set_xlabel(r'A')
    #axs[1].set_xlim([110, 136])
    #axs[1].set_ylim([14, 16.5])
    #
    axs[2].set_title(r'Pb')
    axs[2].set_xlabel(r'A')
    #axs[2].set_xlim([202, 210])
    #axs[2].set_ylim([13, 14])
    #
    for table in tables:
        #
        print('Table:',table)
        gmr = nuda.nuc.setupISGMRExp( table = table )
        #print('A[gmr.Z==40]:',gmr.A[gmr.Z==40])
        #print('E_cen[gmr.Z==40]:',gmr.E_cen[gmr.Z==40])
        #print('E_errp[gmr.Z==40]:',gmr.E_errp[gmr.Z==40])
        print('For Z = 40, A = ',gmr.isgmr['40']['A'])
        if any(gmr.isgmr['40']):
            for A in gmr.isgmr['40']['A']:
                print('A=',A)
                if gmr.isgmr['40'][str(A)]['M12Mm1']['cent']:
                    print('isgmr:',gmr.isgmr['40'][str(A)]['M12Mm1']['cent'])
                    for k in range(len(gmr.isgmr['40'][str(A)]['M12Mm1']['cent'])):
                        print('k=',k,gmr.isgmr['40'][str(A)]['M12Mm1']['cent'][k])
                if isinstance(gmr.isgmr['40'][str(A)]['M12Mm1']['cent'],float):
                    nucA = np.array( gmr.isgmr['40']['A'], dtype=float )
                    cent = np.array( gmr.isgmr['40'][str(A)]['M12Mm1']['cent'], dtype=float )
                    errp = np.array( gmr.isgmr['40'][str(A)]['M12Mm1']['errp'], dtype=float )
                    errm = np.array( gmr.isgmr['40'][str(A)]['M12Mm1']['errm'], dtype=float )
                    print('A:',nucA)
                    print('cent:',cent)
                    print('errp:',errp)
                    print('errm:',errm)
                    axs[0].errorbar( nucA, cent, yerr=errp, fmt='o', label=gmr.label )
                    #axs[0].errorbar( nucA, cent, yerr=[ errp, -errm ],fmt='o', label=gmr.label )
        print('For Z = 50, A = ',gmr.isgmr['50']['A'])
        if any(gmr.isgmr['50']): 
            for A in gmr.isgmr['50']['A']:
                print('isgmr:',gmr.isgmr['40'][str(A)]['M12Mm1']['cent'])
                if isinstance(gmr.isgmr['50'][str(A)]['M12Mm1']['cent'],float):
                    nucA = gmr.isgmr['50']['A']
                    cent = gmr.isgmr['50'][str(A)]['M12Mm1']['cent']
                    errp = gmr.isgmr['50'][str(A)]['M12Mm1']['errp']
                    errm = gmr.isgmr['50'][str(A)]['M12Mm1']['errm']
                    print('A:',nucA)
                    print('cent:',cent)
                    print('errp:',errp)
                    print('errm:',errm)
                    axs[1].errorbar( nucA, cent, yerr=errp, fmt='o', label=gmr.label )
                    #axs[1].errorbar( nucA, cent, yerr=[ errp, errm ],fmt='o', label=gmr.label )
        print('For Z = 82, A = ',gmr.isgmr['82']['A'])
        if any(gmr.isgmr['82']): 
            for A in gmr.isgmr['82']['A']:
                print('isgmr:',gmr.isgmr['40'][str(A)]['M12Mm1']['cent'])
                if isinstance(gmr.isgmr['82'][str(A)]['M12Mm1']['cent'],float):             
                    nucA = gmr.isgmr['82']['A']
                    cent = gmr.isgmr['82'][str(A)]['M12Mm1']['cent']
                    errp = gmr.isgmr['82'][str(A)]['M12Mm1']['errp']
                    errm = gmr.isgmr['82'][str(A)]['M12Mm1']['errm']
                    print('A:',nucA)
                    print('cent:',cent)
                    print('errp:',errp)
                    print('errm:',errm)
                    axs[2].errorbar( nucA, cent, yerr=errp, fmt='o', label=gmr.label )
                    #axs[2].errorbar( nucA, cent, yerr=[ errp, errm ],fmt='o', label=gmr.label )
    #
    axs[0].legend(loc='upper right',fontsize='xx-small')
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
    tables = [ '2018-ISGMR-GARG-LATEX' ]
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
