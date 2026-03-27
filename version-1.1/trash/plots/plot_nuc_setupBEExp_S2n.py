
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def plot_nuc_setupBEExp_S2n( tables, versions, Zref = 50 ):
    #
    print('Tables:',tables)
    print('Zref:',Zref)
    #
    pname = 'figs/plot_nuc_setupBEExp_S2n_Zref'+str(Zref)+'.png'
    print(f'Plot name: {pname}')
    #
    # plot
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.14, bottom=0.15, right=None, top=0.85, wspace=0.3, hspace=0.3)
    #
    axs.set_title(r'Experimental mass tables',fontsize='12')
    axs.set_ylabel(r'$S_{2n}$ (MeV)',fontsize='12')
    axs.set_xlabel(r'N',fontsize='12')
    axs.set_xlim([Zref-5, int(1.85*Zref)])
    axs.set_xticks(np.arange(start=Zref-5,stop=2*Zref,step=5))
    #axs.set_ylim([-10, 10])
    axs.text(int(Zref),10,'For Z='+str(Zref),fontsize='12')
    #
    # loop over the tables
    #
    for i,table in enumerate( tables ):
        #
        version = versions[i]
        # plot nuclear chart:
        mas_exp = nuda.nuc.setupBEExp( table = table, version = version )
        s2n_exp = mas_exp.S2n( Zmin = Zref, Zmax = Zref )
        axs.scatter( s2n_exp.S2n_N, s2n_exp.S2n, label=table+' '+version )
        #axs.plot( s2n_exp.S2n_N, s2n_exp.S2n, linestyle='solid', linewidth=1, label=exp_table+' '+exp_version )
    #
    axs.legend(loc='upper right',fontsize='10', ncol=1)
    #
    plt.savefig(pname, dpi=200)
    plt.close()
    #

def main():
    #
    print(50*'-')
    print("Enter plot_nuc_setupBEExp_S2n.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    #tables, tables_lower = nudy.tables_masses_exp()
    tables = [ 'AME' ]
    versions = [ '2020' ]
    #
    plot_nuc_setupBEExp_S2n( tables, versions, Zref = 50 )
    #
    plot_nuc_setupBEExp_S2n( tables, versions, Zref = 20 )
    #
    print(50*'-')
    print("Exit plot_nuc_setupBEExp_S2n.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
