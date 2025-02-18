
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plot_nuc_setupBEExp_year( pname, table, version ):
    #
    print(50*'-')
    print("Enter plot_nuc_setupBEExp_year.py:")
    print(50*'-')
    #
    print('Table:',table)
    #
    # read all the mass table:
    #
    mas = nuda.nuc.setupBEExp( table = table, version = version )
    #
    # plot
    #
    fig, axs = plt.subplots(1,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.15, right=None, top=0.85, wspace=0.2, hspace=0.2)
    #
    axs[0].set_title(r''+table+' mass table version '+version)
    axs[0].set_ylabel(r'number of discovered nuclei')
    axs[0].set_xlabel(r'year')
    axs[0].set_xlim([1890, 2020])
    #axs.set_yscale('log')
    axs[0].set_ylim([0, 250])
    #axs.text(10,120,'Number of nuclei:')
    #
    axs[0].hist( mas.nucYear, bins=100 )
    #axs.hist( mas.year, bins=100, linestyle='solid', linewidth=1, color='k')
    #axs.plot( mas.dist_year*10, mas.dist_nbNuc, linestyle='solid', linewidth=1, color='k')
    #
    axs[1].set_title(r''+table+' mass table version '+version)
    axs[1].set_xlabel(r'year')
    axs[1].set_xlim([2000, 2020])
    axs[1].set_ylim([0, 100])
    axs[1].hist( mas.nucYear, bins=100 )
    #
    #axs.legend(loc='lower right',fontsize='10')
    #
    plt.savefig(pname, dpi=200)
    plt.close()
    #
    print(50*'-')
    print("Exit plot_nuc_setupBEExp_year.py:")
    print(50*'-')
    #

def main():
    #
    print(50*'-')
    print("Enter plot_nuc_setupBEExp_year.py:")
    print(50*'-')
    #
    # plot discovery years
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    #tables, tables_lower = nudy.tables_masses_exp()
    tables = [ 'AME' ]
    versions = [ '2020' ]
    #
    # loop over the tables
    #
    for i,table in enumerate( tables ):
        #
        version = versions[i]
        #
        pname = 'figs/plot_nuc_setupBEExp_year_'+table+'_'+version+'.png'
        print(f'Plot name: {pname}')
        plot_nuc_setupBEExp_year( pname, table, version )
    #
    print(50*'-')
    print("Exit plot_nuc_setupBEExp_year.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
