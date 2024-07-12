
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plot_theory_isotopes( tables, table_ref = '1995-DZ', Zref = 50 ):
    #
    print(50*'-')
    print("Enter plot_theory_isotopes.py:")
    print(50*'-')
    #
    print('Tables:',tables)
    if table_ref in tables:
        tables.remove(table_ref)
    print('Tables:',tables)
    print('Table_ref:',table_ref)
    print('Zref:',Zref)
    #
    pname = 'figs/plot_SetupMassesTheory_Zref'+str(Zref)+'.png'
    print(f'Plot name: {pname}')
    #
    # plot
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.15, right=None, top=0.85, wspace=0.3, hspace=0.3)
    #
    axs.set_title(r'Comparison of theoretical mass models',fontsize='12')
    axs.set_ylabel(r'$E-E_{DZ}$ (MeV)',fontsize='12')
    axs.set_xlabel(r'N',fontsize='12')
    #axs.set_xlim([0, 200])
    axs.set_ylim([-500, 500])
    axs.text(60,400,'For Z='+str(Zref),fontsize='12')
    #
    # loop over the tables
    #
    mas = nuda.SetupMassesTheory( table = table_ref )
    #
    for i,table in enumerate( tables ):
        #
        N_dif, BE_dif = mas.diff( table=table, Zref = Zref)
        #
        axs.plot( N_dif, BE_dif, linestyle='solid', linewidth=1, label=mas.label)
    #
    axs.legend(loc='upper right',fontsize='10')
    #
    plt.savefig(pname)
    plt.close()
    #
    print(50*'-')
    print("Exit plot_theory_isotopes.py:")
    print(50*'-')


def plot_theory_isotopes_old( tables, table_ref = '1995-DZ', Zref = 50 ):
    #
    print(50*'-')
    print("Enter plot_theory_isotopes_old.py:")
    print(50*'-')
    #
    print('Tables:',tables)
    if table_ref in tables:
        tables.remove(table_ref)
    print('Tables:',tables)
    print('Table_ref:',table_ref)
    print('Zref:',Zref)
    #
    pname = 'figs/plot_SetupMassesTheory_Zref'+str(Zref)+'.png'
    print(f'Plot name: {pname}')
    mas_ref = nuda.SetupMassesTheory( table = table_ref )
    BE_ref = []
    N_ref = []
    for k in range(len(mas_ref.nucZ)):
        if int( mas_ref.nucZ[k] ) == Zref:
            BE_ref.append( mas_ref.nucBE[k] )
            N_ref.append( mas_ref.nucN[k] )
    print('For table_ref:',table_ref)
    print('BE_ref:',BE_ref)
    print('N_ref:',N_ref)
    #
    # plot
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.15, right=None, top=0.85, wspace=0.3, hspace=0.3)
    #
    axs.set_title(r'Comparison of theoretical mass models',fontsize='12')
    axs.set_ylabel(r'$E-E_{DZ}$ (MeV)',fontsize='12')
    axs.set_xlabel(r'N',fontsize='12')
    #axs.set_xlim([0, 200])
    axs.set_ylim([-500, 500])
    axs.text(60,400,'For Z='+str(Zref),fontsize='12')
    #
    # loop over the tables
    #
    for i,table in enumerate( tables ):
        #
        mas = nuda.SetupMassesTheory( table = table )

        BE = []
        N = []
        for k in range(len(mas.nucZ)):
            if int( mas.nucZ[k] ) == Zref:
                BE.append( mas.nucBE[k] )
                N.append( mas.nucN[k] )
        N_min = max( N[0], N_ref[0] )
        k_ref, = np.where( N_ref[:] == N_min )[0]
        k_init, = np.where( N[:] == N_min )[0]
        N_dif = []
        BE_dif = []
        for k in range(k_init,len(N)-k_init):
            k_ref += N[k] - N_ref[k_ref]
            BE_dif.append( BE[k]-BE_ref[k_ref] )
            N_dif.append( N[k] )
            k_ref += 1
        #
        axs.plot( N_dif, BE_dif, linestyle='solid', linewidth=1, label=mas.label)
    #
    axs.legend(loc='upper right',fontsize='10')
    #
    plt.savefig(pname)
    plt.close()
    #
    print(50*'-')
    print("Exit plot_theory_isotopes_old.py:")
    print(50*'-')

def main():
    #
    print(50*'-')
    print("Enter plot_SetupMassesTheory.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    tables, tables_lower = nuda.tables_masses_theory()
    #tables = [ '1995-DZ' ]
    #
    plot_theory_isotopes_old( tables, Zref = 50 )
    #
    plot_theory_isotopes( tables, Zref = 20 )
    #
    print(50*'-')
    print("Exit plot_SetupMassesTheory.py:")
    print(50*'-')
    #


    
if __name__ == "__main__":
    main()
