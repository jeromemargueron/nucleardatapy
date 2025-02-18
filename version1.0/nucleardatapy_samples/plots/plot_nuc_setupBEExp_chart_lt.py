
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def plot_nuc_setupBEExp_chart_lt( pname, table, version, theo_tables ):
    #
    print(50*'-')
    print("Enter plot_nuc_setupBEExp_chart_lt.py:")
    print(50*'-')
    #
    print('Table:',table)
    #
    # plot
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.15, right=None, top=0.85, wspace=0.3, hspace=0.3)
    #
    axs.set_title(r''+table+' mass table version '+version)
    axs.set_ylabel(r'Z')
    axs.set_xlabel(r'N')
    axs.set_xlim([0, 200])
    axs.set_ylim([0, 132])
    axs.text(10,120,'Number of nuclei:')
    #
    # longlive nuclei
    #
    mas = nuda.nuc.setupBEExp( table = table, version = version )
    ustbl = mas.select( state= 'gs', interp = 'n', nucleus = 'longlive' )
    axs.scatter( ustbl.sel_nucN, ustbl.sel_nucZ, marker='s', s = 3, linewidth=0, color = 'grey', label='longlive ('+str(ustbl.sel_nbNucSel)+')' )
    #axs.text(10,96,'long live: '+str(ustbl.sel_nbNucSel))
    #
    # shortlive nuclei
    #
    mas = nuda.nuc.setupBEExp( table = table, version = version )
    ustbl = mas.select( state= 'gs', interp = 'n', nucleus = 'shortlive' )
    axs.scatter( ustbl.sel_nucN, ustbl.sel_nucZ, marker='s', s = 3, linewidth=0, color = 'r', label='shortlive ('+str(ustbl.sel_nbNucSel)+')' )
    #axs.text(10,88,'short live: '+str(ustbl.sel_nbNucSel))
    #
    # veryshortlive nuclei
    #
    mas = nuda.nuc.setupBEExp( table = table, version = version )
    ustbl = mas.select( state= 'gs', interp = 'n', nucleus = 'veryshortlive' )
    axs.scatter( ustbl.sel_nucN, ustbl.sel_nucZ, marker='s', s = 3, linewidth=0, color = 'b', label='veryshortlive ('+str(ustbl.sel_nbNucSel)+')' )
    #axs.text(10,80,'very short live: '+str(ustbl.sel_nbNucSel))
    #
    # unstable nuclei:
    #
    mas = nuda.nuc.setupBEExp( table = table, version = version )
    ustbl = mas.select( state= 'gs', interp = 'n', nucleus = 'unstable' )
    #axs.scatter( ustbl.sel_nucN, ustbl.sel_Z, marker='.', s = 1, linewidth=0, color = 'b' )
    axs.text(10,104,'unstable: '+str(ustbl.sel_nbNucSel))
    #
    # drip line nuclei
    #
    legend = 0
    for i,theo_table in enumerate( theo_tables ):
        theo = nuda.nuc.setupBETheo( table = theo_table )
        s2n = theo.S2n( Zmin=1, Zmax = 95 )
        drip_S2n = s2n.drip_S2n( Zmin = 1, Zmax = 95 )
        if legend == 0:
            axs.scatter( drip_S2n.drip_S2n_N, drip_S2n.drip_S2n_Z, marker='o', s = 3, linewidth=0, color = 'green', label='Drip Lines' )
            legend = 1
        else:
            axs.scatter( drip_S2n.drip_S2n_N, drip_S2n.drip_S2n_Z, marker='o', s = 3, linewidth=0, color = 'green' )
        s2p = theo.S2p( Nmin=1, Nmax = 150 )
        drip_S2p = s2p.drip_S2p( Nmin = 1, Nmax = 150 )
        axs.scatter( drip_S2p.drip_S2p_N, drip_S2p.drip_S2p_Z, marker='o', s = 3, linewidth=0, color = 'green' )
    #
    # First and last isotopes
    #
    #iso = ustbl.isotopes( Zmin=1, Zmax = 95 )
    #axs.scatter( iso.isotopes_Nmin, iso.isotopes_Z, marker='s', s = 3, linewidth=0, color = 'green', label='Isotope bounds' )
    #axs.scatter( iso.isotopes_Nmax, iso.isotopes_Z, marker='s', s = 3, linewidth=0, color = 'green' )
    #
    # stable nuclei:
    #
    mas = nuda.nuc.setupBEExp( table = table, version = version )
    stbl = mas.select( state= 'gs', interp = 'n', nucleus = 'stable' )
    axs.scatter( stbl.sel_nucN, stbl.sel_nucZ, marker='s', s = 3, linewidth=0, color = 'k' )
    axs.text(10,112,'stable: '+str(stbl.sel_nbNucSel))
    #
    axs.text(60,120,str(ustbl.sel_nbNucSel+stbl.sel_nbNucSel))
    #
    # plot N=Z dotted line
    #
    axs.plot( [0, 130], [0, 130], linestyle='dotted', linewidth=1, color='k')
    axs.text(105,120,'N=Z')
    #
    # plot stable_fit
    #
    N, Z = nuda.stable_fit( Zmin = 1, Zmax = 120 )
    axs.plot( N, Z, linestyle='dashed', linewidth=1, color='k')
    #
    # plot shells for isotopes and isotones
    #
    axs = nuda.nuc.plot_shells(axs)
    #
    # set legend
    #
    axs.legend(loc='lower right',fontsize='10')
    #
    # set plot name and close
    #
    plt.savefig(pname, dpi=300)
    plt.close()
    #
    print(50*'-')
    print("Exit plot_SetupNucBEExp_chart_lt.py:")
    print(50*'-')

def main():
    #
    print(50*'-')
    print("Enter plot_nuc_setupBEExp_chart_lt.py:")
    print(50*'-')
    #
    # plot nuclear chart lt=life time
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    # Experimental mass tables
    #
    #tables, tables_lower = nudy.tables_masses_exp()
    tables = [ 'AME' ]
    versions = [ '2020' ]
    #
    # Theoretical mass tables
    #
    #theo_tables, theo_tables_lower = nuda.nuc.be_theo_tables()
    theo_tables = [ '2013-HFB22', '2013-HFB23', '2013-HFB24', '2013-HFB25', \
    '2013-HFB26', '2021-BSkG1', '2022-BSkG2', '2023-BSkG3' ]
    #
    # loop over the tables
    #
    for i,table in enumerate( tables ):
        #
        version = versions[i]
        pname = 'figs/plot_nuc_setupBEExp_chart_lt_'+table+'_'+version+'.png'
        print(f'Plot name: {pname}')
        plot_nuc_setupBEExp_chart_lt( pname, table, version, theo_tables )
        #
    #
    print(50*'-')
    print("Exit plot_nuc_setupBEExp_chart_lt.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
