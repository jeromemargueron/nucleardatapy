
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def plot_nuc_setupBEExp_D3p_n( tables, versions, Zref = 50 ):
    #
    print('Tables:',tables)
    print('Zref:',Zref)
    #
    pname = 'figs/plot_nuc_setupBEExp_D3p_Zref'+str(Zref)+'.png'
    print(f'Plot name: {pname}')
    #
    # plot
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.14, bottom=0.15, right=None, top=0.85, wspace=0.3, hspace=0.3)
    #
    axs.set_title(r'Experimental mass tables',fontsize='12')
    axs.set_ylabel(r'$\Delta_{3p}$ (MeV)',fontsize='12')
    axs.set_xlabel(r'N',fontsize='12')
    axs.set_xlim([Zref-5, int(1.85*Zref)])
    axs.set_xticks(np.arange(start=Zref-5,stop=2*Zref,step=5))
    #axs.set_ylim([-10, 10])
    axs.text(int(Zref),1.0,'For Z='+str(Zref),fontsize='12')
    #
    # loop over the tables
    #
    for i,table in enumerate( tables ):
        #
        version = versions[i]
        # plot nuclear chart:
        mas_exp = nuda.nuc.setupBEExp( table = table, version = version )
        d3p_exp = mas_exp.D3p_n( Zmin = Zref, Zmax = Zref )
        axs.scatter( d3p_exp.D3p_n_N_even, d3p_exp.D3p_n_even, label=table+' '+version+'(even)' )
        axs.scatter( d3p_exp.D3p_n_N_odd,  d3p_exp.D3p_n_odd,  label=table+' '+version+'(odd)' )
    #
    axs.legend(loc='upper right',fontsize='10', ncol=1)
    #
    plt.savefig(pname, dpi=200)
    plt.close()
    #

def plot_nuc_setupBEExp_D3p_p( tables, versions, Nref = 50 ):
    #
    print('Tables:',tables)
    print('Nref:',Nref)
    #
    pname = 'figs/plot_nuc_setupBEExp_D3p_Nref'+str(Nref)+'.png'
    print(f'Plot name: {pname}')
    #
    # plot
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.14, bottom=0.15, right=None, top=0.85, wspace=0.3, hspace=0.3)
    #
    axs.set_title(r'Experimental mass tables',fontsize='12')
    axs.set_ylabel(r'$\Delta_{3p}$ (MeV)',fontsize='12')
    axs.set_xlabel(r'Z',fontsize='12')
    axs.set_xlim([0.4*Nref, 1.2*Nref])
    axs.set_xticks(np.arange(start=int(0.4*Nref),stop=1.2*Nref,step=5))
    #axs.set_ylim([-10, 10])
    axs.text(int(0.7*Nref),1.4,'For N='+str(Nref),fontsize='12')
    #
    # loop over the tables
    #
    for i,table in enumerate( tables ):
        #
        version = versions[i]
        # plot nuclear chart:
        mas_exp = nuda.nuc.setupBEExp( table = table, version = version )
        d3p_exp = mas_exp.D3p_p( Nmin = Nref, Nmax = Nref )
        axs.scatter( d3p_exp.D3p_p_Z_even, d3p_exp.D3p_p_even, label=table+' '+version+'(even)' )
        axs.scatter( d3p_exp.D3p_p_Z_odd,  d3p_exp.D3p_p_odd,  label=table+' '+version+'(odd)' )
    #
    axs.legend(loc='upper right',fontsize='10', ncol=1)
    #
    plt.savefig(pname, dpi=200)
    plt.close()
    #

def main():
    #
    print(50*'-')
    print("Enter plot_nuc_setupBEExp_D3p.py:")
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
    plot_nuc_setupBEExp_D3p_n( tables, versions, Zref = 50 )
    #
    plot_nuc_setupBEExp_D3p_n( tables, versions, Zref = 20 )
    #
    plot_nuc_setupBEExp_D3p_p( tables, versions, Nref = 50 )
    #
    plot_nuc_setupBEExp_D3p_p( tables, versions, Nref = 20 )
    #
    print(50*'-')
    print("Exit plot_nuc_setupBEExp_D3p.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
