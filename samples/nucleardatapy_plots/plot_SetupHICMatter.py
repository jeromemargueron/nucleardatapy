
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
#plt.rcParams.update({'font.size': 16})

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plot_hic_matter( pname, constraints ):
    #
    # plot
    #
    fig, axs = plt.subplots(1,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.98, wspace=0.3, hspace=0.3)
    #
    axs[0].set_xlabel(r'$n$ (fm$^{-3}$)',fontsize='12')
    axs[1].set_xlabel(r'$n$ (fm$^{-3}$)',fontsize='12')
    axs[0].set_ylabel(r'$E/A_{SM}$ (MeV)',fontsize='12')
    axs[1].set_ylabel(r'$p_{SM}$ (MeV fm${-3}$)',fontsize='12')
    #axs.set_xlim([0.09, 0.27])
    #axs.set_ylim([10, 60])
    #
    for constraint in constraints:
        #
        hic = nuda.SetupHICMatter( constraint = constraint )
        #
        if hic.sm_e2a is not None:
            axs[0].fill_between( hic.den, y1=hic.sm_e2a_lo, y2=hic.sm_e2a_up, label=hic.label, alpha=hic.alpha )
        if hic.sm_pre is not None:
            axs[1].fill_between( hic.den, y1=hic.sm_pre_lo, y2=hic.sm_pre_up, label=hic.label, alpha=hic.alpha )
    #
    #axs.text(0.15,12,r'$K_{sym}$='+str(int(Ksym))+' MeV',fontsize='12')
    axs[0].legend(loc='lower right',fontsize='8')
    axs[1].legend(loc='lower right',fontsize='8')
    #
    plt.savefig(pname)
    plt.close()
    #

def main():
    #
    print(50*'-')
    print("Enter plot_SetupHICMatter.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    constraints, constraints_lower = nuda.constraints_HIC_matter()
    #constraints = [ '2014-IAS' ]
    #
    pname = 'figs/plot_SetupHICMatter.png'
    #
    plot_hic_matter( pname, constraints )
    #
    print(50*'-')
    print("Exit plot_SetupHICMatter.py:")
    print(50*'-')
    #

    
if __name__ == "__main__":
    main()
