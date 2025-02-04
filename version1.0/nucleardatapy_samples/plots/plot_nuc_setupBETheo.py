
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plot_nuc_setupBETheo_isotopes( tables, table_ref = '1995-DZ', Zref = 50 ):
    #
    print('Tables:',tables)
    if table_ref in tables:
        tables.remove(table_ref)
    print('Tables:',tables)
    print('Table_ref:',table_ref)
    print('Zref:',Zref)
    #
    pname = 'figs/plot_nuc_setupBETheo_Zref'+str(Zref)+'.png'
    print(f'Plot name: {pname}')
    #
    # plot
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.14, bottom=0.15, right=None, top=0.85, wspace=0.3, hspace=0.3)
    #
    axs.set_title(r'Comparison of theoretical mass models',fontsize='12')
    axs.set_ylabel(r'$E-E_{DZ}$ (MeV)',fontsize='12')
    axs.set_xlabel(r'N',fontsize='12')
    #axs.set_xlim([0, 200])
    axs.set_ylim([-10, 10])
    axs.text(int(Zref),400,'For Z='+str(Zref),fontsize='12')
    #
    # loop over the tables
    #
    mas = nuda.nuc.setupBETheo( table = table_ref )
    #
    for i,table in enumerate( tables ):
        #
        N_diff, A_diff, BE_diff, BE2A_diff = mas.diff( table = table, Zref = Zref )
        #
        axs.plot( N_diff, BE_diff, linestyle='solid', linewidth=1, label=table )
    #
    N_diff, A_diff, BE_diff, BE_diff = mas.diff_exp( table_exp = 'AME', version_exp = '2020', Zref = Zref )
    axs.scatter( N_diff, BE_diff, label='AME2020' )
    #
    axs.legend(loc='upper right',fontsize='10', ncol=4)
    #
    plt.savefig(pname, dpi=200)
    plt.close()
    #

def main():
    #
    print(50*'-')
    print("Enter plot_nuc_setupBETheo.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    tables, tables_lower = nuda.nuc.be_theo_tables()
    #tables = [ '1995-DZ' ]
    #
    plot_nuc_setupBETheo_isotopes( tables, Zref = 50 )
    #
    plot_nuc_setupBETheo_isotopes( tables, Zref = 20 )
    #
    print(50*'-')
    print("Exit plot_nuc_setupBETheo.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
