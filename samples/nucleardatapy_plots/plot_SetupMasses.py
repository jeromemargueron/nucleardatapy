
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter plot_SetupMasses.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    tables = [ 'AME' ]
    #tables, tables_lower = nudy.tables_masses()
    version = '2020' 
    #
    for table in tables:
        #
        print('Table:',table)
        #
        # plot name:
        #
        pname = 'figs/plot_SetupMasses'+table+'.png'
        print(f'Plot name: {pname}')
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
        mas = nuda.SetupMasses( table = table, version = version )
        # plot mass table for unstable nuclei:
        ustbl = mas.select( state= 'gs', interp = 'n', nucleus = 'unstable' )
        axs.scatter( ustbl.sel_N, ustbl.sel_Z, marker='.', s = 1, linewidth=0, color = 'b' )
        axs.text(10,110,'Number of unstable nuclei:'+str(ustbl.sel_nbNucSel))
        # drip line nuclei
        #drip = mas.select( state= 'gs', interp = 'n', nucleus = 'unstable' ).drip()
        drip = ustbl.drip( Zmax = 95 )
        axs.scatter( drip.drip_Nmin, drip.drip_Z, marker='s', s = 1, linewidth=0, color = 'green' )
        axs.scatter( drip.drip_Nmax, drip.drip_Z, marker='s', s = 1, linewidth=0, color = 'green' )
        # plot mass table for stable nuclei:
        stbl = mas.select( state= 'gs', interp = 'n', nucleus = 'stable' )
        axs.scatter( stbl.sel_N, stbl.sel_Z, marker='s', s = 1, linewidth=0, color = 'k' )
        axs.text(10,120,'Number of stable nuclei:'+str(stbl.sel_nbNucSel))
        #axs.scatter( sel.N, sel.Z, marker='.', s = 1, alpha = 0.3 )
        #nudy.print_outputs_isgmr( gmr )
        # plot N=Z dotted line
        axs.plot( [0, 130], [0, 130], linestyle='dotted', linewidth=1, color='k')
        axs.text(105,120,'N=Z')
        # plot stable_fit
        N, Z = nuda.stable_fit()
        axs.plot( N, Z, linestyle='dashed', linewidth=1, color='k')
        # plot shells
        # for isotopes
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
        # for isotones
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
    #axs.legend(loc='upper right',fontsize='xx-small')
    #
    plt.savefig(pname)
    plt.close()

    print(50*'-')
    print("Exit plot_SetupMasses.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
