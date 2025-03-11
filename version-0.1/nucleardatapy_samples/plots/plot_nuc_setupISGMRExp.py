
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
    obs = 'M12Mm1'
    #
    nucZ = [ 40, 50, 82 ]
    #
    fig, axs = plt.subplots(1,3)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.15, right=None, top=0.85, wspace=0.1, hspace=0.3)
    #
    if obs == 'M12M0':
        axs[0].set_ylabel(r'$E_{ISGMR}$ ($m_1/m_0$)')
    elif obs == 'M12Mm1':
        axs[0].set_ylabel(r'$E_{ISGMR}$ ($\sqrt{m_1/m_{-1}}$)')
    elif obs == 'M12Mm1':
        axs[0].set_ylabel(r'$E_{ISGMR}$ ($\sqrt{m_3/m_1}$)')
    #
    #axs[0].set_xlim([88, 96])
    #axs[1].set_xlim([110, 136])
    #axs[2].set_xlim([202, 210])
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
            axs[i].set_title(nuda.param.elements[nucZ[i]-1])
            axs[i].set_xlabel(r'A')
            axs[i].set_ylim([13, 18])
            if i>0: axs[i].tick_params('y', labelleft=False)
            gmrs = gmr.select( Zref = nucZ[i], obs = obs )
            x = gmrs.nucA+0.2*k*np.ones(len(gmrs.nucA))
            axs[i].errorbar( x, gmrs.cent, yerr=gmrs.erra, fmt='o', label=gmr.label )
    #
    axs[2].legend(loc='upper right',fontsize='10')
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
    tables = [ '2018-ISGMR-GARG-LATEX', '2022-ISGMR-average' ]
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
