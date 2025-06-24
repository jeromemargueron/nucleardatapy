import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def hnuc_setupRE1LExp_fig( pname, tables ):
    #
    # plot
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.15, right=0.95, top=0.95, wspace=0.3, hspace=0.3)
    #
    axs.set_ylabel(r'Removal energy $B_\Lambda$ (MeV)',fontsize='14')
    axs.set_xlabel(r'$A^{-2/3}$',fontsize='14')
    axs.set_xlim([0.0, 0.28])
    axs.set_ylim([-5.0, 32.0])
    #
    axs.plot( [0.0,0.28], [0.0,0.0], color='k', linestyle='dashed' )
    for table in tables:
        #
        hnuc = nuda.hnuc.setupRE1LExp( table = table )
        #
        lab = []
        for i in range(hnuc.nbdata):
            if hnuc.label[i] not in lab:
                lab.append(hnuc.label[i])
                axs.errorbar( hnuc.A[i]**(-0.6666), hnuc.lre[i], yerr=hnuc.lre_err[i], marker=hnuc.mark[i], color=hnuc.color[i], label=hnuc.label[i], ms=4, ls='none' )
            else:
                axs.errorbar( hnuc.A[i]**(-0.6666), hnuc.lre[i], yerr=hnuc.lre_err[i], marker=hnuc.mark[i], color=hnuc.color[i], ms=4, ls='none' )                
        #
        axs.text(0.01,26.5,'1s')
        axs.text(0.01,22,'1p')
        axs.text(0.01,17,'1d')
        axs.text(0.01,12,'1f')
        axs.text(0.01,7,'1g')
    #
    #axs.text(0.15,12,r'$K_{sym}$='+str(int(Ksym))+' MeV',fontsize='12')
    axs.legend(loc='upper right',fontsize='8',ncol=2)
    #
    if pname is not None:
    	plt.savefig(pname, dpi=200)
    	plt.close()
    #