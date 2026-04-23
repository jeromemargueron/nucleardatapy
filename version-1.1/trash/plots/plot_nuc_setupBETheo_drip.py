
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plot_nuc_setupBETheo_S2n( tables, Zref = 50 ):
    #
    print('Tables:',tables)
    print('Zref:',Zref)
    #
    pname = 'figs/plot_nuc_setupBETheo_S2n_Zref'+str(Zref)+'.png'
    print(f'Plot name: {pname}')
    #
    # plot
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.14, bottom=0.15, right=None, top=0.85, wspace=0.3, hspace=0.3)
    #
    axs.set_title(r'Comparison of theoretical mass models',fontsize='12')
    axs.set_ylabel(r'$S_{2n}$ (MeV)',fontsize='12')
    axs.set_xlabel(r'N',fontsize='12')
    axs.set_xlim([Zref-5, int(2.3*Zref)])
    axs.set_xticks(np.arange(start=Zref-5,stop=2.3*Zref,step=5))
    axs.set_ylim([0, 40])
    axs.text(int(Zref),10,'For Z='+str(Zref),fontsize='12')
    #
    # loop over the tables
    #
    for i,table in enumerate( tables ):
        #
        mas = nuda.nuc.setupBETheo( table = table )
        s2n = mas.S2n( Zmin = Zref, Zmax = Zref )
        drip_S2n = s2n.drip_S2n( Zmin = Zref, Zmax = Zref )
        #
        axs.plot( drip_S.S2n_N, drip_S.S2n, linestyle='solid', linewidth=1, label=table )
    #
    exp_table = 'AME'
    exp_version = '2020'
    mas_exp = nuda.nuc.setupBEExp( table = exp_table, version = exp_version )
    s2n_exp = mas_exp.S2n( Zmin = Zref, Zmax = Zref )
    axs.scatter( s2n_exp.S2n_N, s2n_exp.S2n, label=exp_table+' '+exp_version )
    #axs.plot( s2n_exp.S2n_N, s2n_exp.S2n, linestyle='solid', linewidth=1, label=exp_table+' '+exp_version )
    #N_diff, A_diff, BE_diff, BE_diff = mas.diff_exp( table_exp = 'AME', version_exp = '2020', Zref = Zref )
    #axs.scatter( N_diff, BE_diff, label='AME2020' )
    #
    axs.legend(loc='upper right',fontsize='10', ncol=4)
    #
    plt.savefig(pname, dpi=200)
    plt.close()
    #

def main():
    #
    print(50*'-')
    print("Enter plot_nuc_setupBETheo_S2n.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    tables, tables_lower = nuda.nuc.be_theo_tables()
    #tables = [ '1995-DZ' ]
    #
    plot_nuc_setupBETheo_S2n( tables, Zref = 50 )
    #
    plot_nuc_setupBETheo_S2n( tables, Zref = 20 )
    #
    print(50*'-')
    print("Exit plot_nuc_setupBETheo_S2n.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
