
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plot_hnuc_setupSPEExp( pname, tables ):
    #
    # plot
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.15, right=None, top=0.85, wspace=0.3, hspace=0.3)
    #
    axs.set_ylabel(r'Binding Energy (MeV)')
    axs.set_xlabel(r'$A^{-2/3}$')
    axs.set_xlim([0.0, 0.28])
    axs.set_ylim([-5.0, 35.0])
    #
    axs.plot( [0.0,0.28], [0.0,0.0], color='k', linestyle='dashed' )
    for table in tables:
        #
        hnuc = nuda.hnuc.setupSPEExp( table = table )
        #
        #if any(Nref): 
        #print('A:',hnuc.nucA)
        #print('spe:',hnuc.nucspe)
        #print('label:',hnuc.label)
        #print('ell:',hnuc.spe.keys())
        #print('ell min:',min(hnuc.spe.keys()))
        #print('ell max:',max(hnuc.spe.keys()))
        #lmin = min(hnuc.spe.keys())
        #lmax = max(hnuc.spe.keys())
        for ell in range(hnuc.lmin,hnuc.lmax+1):
            x = np.array( hnuc.A[ell], dtype=float)
            y = np.array( hnuc.spe[ell], dtype=float)
            dy = np.array( hnuc.spe_err[ell], dtype=float)
            if ell == 0:
                axs.errorbar( x**(-0.6666), -y, yerr=dy, marker=hnuc.marker[ell], color=hnuc.color, label=hnuc.label, ms=4, ls='none' )
            else:
                axs.errorbar( x**(-0.6666), -y, yerr=dy, marker=hnuc.marker[ell], color=hnuc.color, ms=4, ls='none' )
        #
    #
    #axs.text(0.15,12,r'$K_{sym}$='+str(int(Ksym))+' MeV',fontsize='12')
    axs.legend(loc='upper right',fontsize='8',ncol=2)
    #
    plt.savefig(pname)
    plt.close()
    #


def main():
    #
    print(50*'-')
    print("Enter plot_hnuc_setupSPEExp.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    tables, tables_lower = nuda.hnuc.spe_exp_tables()
    #
    pname = 'figs/plot_hnuc_setupSPEExp.png'
    #
    plot_hnuc_setupSPEExp( pname, tables )
    #
    print(50*'-')
    print("Exit plot_hnuc_setupSPEExp.py:")
    print(50*'-')
    #

    
if __name__ == "__main__":
    main()
