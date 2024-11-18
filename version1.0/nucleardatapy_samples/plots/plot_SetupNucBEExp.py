
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plot_shells(axs):
    #
    # plot shells for isotopes and isotones
    #
    axs.plot( [0,40], [7,7], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [0,40], [9,9], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [6,60], [19,19], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [6,60], [21,21], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [12,90], [27,27], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [12,90], [29,29], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [34,138], [49,49], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [34,138], [51,51], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [76,170], [81,81], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [76,170], [83,83], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [126,190], [127,127], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [126,190], [129,129], linestyle='dotted', linewidth=1, color='gray')
    #
    # plot shells for isotones
    #
    axs.plot( [7,7], [0,24], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [9,9], [0,24], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [19,19], [4,40], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [21,21], [4,40], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [27,27], [4,46], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [29,29], [4,46], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [49,49], [14,60], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [51,51], [14,60], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [81,81], [20,86], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [83,83], [20,86], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [127,127], [40,132], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [129,129], [40,132], linestyle='dotted', linewidth=1, color='gray')
    #
    return axs

def plot_SetupNucBEExp_chart( pname, table, version ):
    #
    print(50*'-')
    print("Enter plot_SetupNucBEExp_chart.py:")
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
    mas = nuda.SetupNucBEExp( table = table, version = version )
    ustbl = mas.select( state= 'gs', interp = 'n', nucleus = 'longlive' )
    axs.scatter( ustbl.sel_nucN, ustbl.sel_nucZ, marker='s', s = 3, linewidth=0, color = 'grey', label='longlive ('+str(ustbl.sel_nbNucSel)+')' )
    #axs.text(10,96,'long live: '+str(ustbl.sel_nbNucSel))
    #
    # shortlive nuclei
    #
    mas = nuda.SetupNucBEExp( table = table, version = version )
    ustbl = mas.select( state= 'gs', interp = 'n', nucleus = 'shortlive' )
    axs.scatter( ustbl.sel_nucN, ustbl.sel_nucZ, marker='s', s = 3, linewidth=0, color = 'r', label='shortlive ('+str(ustbl.sel_nbNucSel)+')' )
    #axs.text(10,88,'short live: '+str(ustbl.sel_nbNucSel))
    #
    # veryshortlive nuclei
    #
    mas = nuda.SetupNucBEExp( table = table, version = version )
    ustbl = mas.select( state= 'gs', interp = 'n', nucleus = 'veryshortlive' )
    axs.scatter( ustbl.sel_nucN, ustbl.sel_nucZ, marker='s', s = 3, linewidth=0, color = 'b', label='veryshortlive ('+str(ustbl.sel_nbNucSel)+')' )
    #axs.text(10,80,'very short live: '+str(ustbl.sel_nbNucSel))
    #
    # unstable nuclei:
    #
    mas = nuda.SetupNucBEExp( table = table, version = version )
    ustbl = mas.select( state= 'gs', interp = 'n', nucleus = 'unstable' )
    #axs.scatter( ustbl.sel_nucN, ustbl.sel_Z, marker='.', s = 1, linewidth=0, color = 'b' )
    axs.text(10,104,'unstable: '+str(ustbl.sel_nbNucSel))
    #
    # drip line nuclei
    #
    #drip = mas.select( state= 'gs', interp = 'n', nucleus = 'unstable' ).drip()
    drip = ustbl.drip( Zmax = 95 )
    axs.scatter( drip.drip_Nmin, drip.drip_Z, marker='s', s = 3, linewidth=0, color = 'green', label='drip line' )
    axs.scatter( drip.drip_Nmax, drip.drip_Z, marker='s', s = 3, linewidth=0, color = 'green' )
    #
    # stable nuclei:
    #
    mas = nuda.SetupNucBEExp( table = table, version = version )
    stbl = mas.select( state= 'gs', interp = 'n', nucleus = 'stable' )
    axs.scatter( stbl.sel_nucN, stbl.sel_nucZ, marker='s', s = 3, linewidth=0, color = 'k' )
    axs.text(10,112,'stable: '+str(stbl.sel_nbNucSel))
    #
    # plot N=Z dotted line
    #
    axs.plot( [0, 130], [0, 130], linestyle='dotted', linewidth=1, color='k')
    axs.text(105,120,'N=Z')
    #
    # plot stable_fit
    #
    N, Z = nuda.stable_fit()
    axs.plot( N, Z, linestyle='dashed', linewidth=1, color='k')
    #
    # plot shells for isotopes and isotones
    #
    axs = plot_shells(axs)
    #
    axs.legend(loc='lower right',fontsize='10')
    #
    plt.savefig(pname)
    plt.close()
    #
    print(50*'-')
    print("Exit plot_SetupNucBEExp_chart.py:")
    print(50*'-')

def plot_SetupNucBEExp_year( pname, table, version ):
    #
    print(50*'-')
    print("Enter plot_SetupNucBEExp_year.py:")
    print(50*'-')
    #
    print('Table:',table)
    #
    # read all the mass table:
    #
    mas = nuda.SetupNucBEExp( table = table, version = version )
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
    plt.savefig(pname)
    plt.close()
    #
    print(50*'-')
    print("Exit plot_SetupNucBEExp_year.py:")
    print(50*'-')
    #

def main():
    #
    print(50*'-')
    print("Enter plot_SetupNucBEExp.py:")
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
    # loop over the tables
    #
    for i,table in enumerate( tables ):
        #
        version = versions[i]
        # plot nuclear chart:
        pname = 'figs/plot_SetupNucBEExp_'+table+'_'+version+'.png'
        print(f'Plot name: {pname}')
        plot_SetupNucBEExp_chart( pname, table, version )
        #
        # plot discovery years:
        pname = 'figs/plot_SetupNucBEExp_'+table+'_'+version+'_year.png'
        print(f'Plot name: {pname}')
        plot_SetupNucBEExp_year( pname, table, version )
    #
    print(50*'-')
    print("Exit plot_SetupNucBEExp.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
