
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plot_nuc_setupBETheo_S2p( tables, Nref = 50 ):
    #
    print('Tables:',tables)
    print('Nref:',Nref)
    #
    pname = 'figs/plot_nuc_setupBETheo_S2p_Nref'+str(Nref)+'.png'
    print(f'Plot name: {pname}')
    #
    # plot
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    #fig.subplots_adjust(left=0.14, bottom=0.15, right=None, top=0.85, wspace=0.3, hspace=0.3)
    fig.subplots_adjust(left=0.15, bottom=0.13, right=None, top=0.8)#, wspace=0.3, hspace=0.3)
    #
    #axs.set_title(r'Comparison of theoretical mass models',fontsize='12')
    axs.set_ylabel(r'$S_{2p}$ (MeV)',fontsize='12')
    axs.set_xlabel(r'Z',fontsize='12')
    #axs.set_xlim([0.4*Nref, 1.3*Nref])
    axs.set_xlim([0.5*Nref, 1.05*Nref])
    #axs.set_xticks(np.arange(start=int(0.4*Nref),stop=1.3*Nref,step=5))
    axs.set_xticks(np.arange(start=int(0.5*Nref),stop=1.05*Nref,step=5))
    axs.set_ylim([0, 46])
    axs.text(int(0.7*Nref),35,'For N='+str(Nref),fontsize='12')
    #
    # loop over the tables
    #
    for i,table in enumerate( tables ):
        #
        mas = nuda.nuc.setupBETheo( table = table )
        s2p = mas.S2p( Nmin = Nref, Nmax = Nref )
        #
        axs.plot( s2p.S2p_Z, s2p.S2p, linestyle='solid', linewidth=1, label=table )
    #
    exp_table = 'AME'
    exp_version = '2020'
    mas_exp = nuda.nuc.setupBEExp( table = exp_table, version = exp_version )
    s2p_exp = mas_exp.S2p( Nmin = Nref, Nmax = Nref )
    axs.scatter( s2p_exp.S2p_Z, s2p_exp.S2p, label=exp_table+' '+exp_version )
    #
    #axs.legend(loc='upper right',fontsize='10', ncol=4)
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=4,frameon=False)
    #
    plt.savefig(pname, dpi=200)
    plt.show()
    plt.close()
    #

def main():
    #
    print(50*'-')
    print("Enter plot_nuc_setupBETheo_S2p.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    tables, tables_lower = nuda.nuc.be_theo_tables()
    #tables = [ '1995-DZ' ]
    #
    plot_nuc_setupBETheo_S2p( tables, Nref = 50 )
    #
    plot_nuc_setupBETheo_S2p( tables, Nref = 82 )
    #
    print(50*'-')
    print("Exit plot_nuc_setupBETheo_S2p.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
