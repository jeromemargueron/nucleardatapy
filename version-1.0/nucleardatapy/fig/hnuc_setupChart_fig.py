import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def hnuc_setupChart_fig( pname, table1L, table2L, table1Xi ):
    """
    Plot hyper-nuclear chart (N versus Z).\
    The plot is 1x1 with:\
    [0]: nuclear chart.

    :param pname: name of the figure (*.png)
    :type pname: str.
    :param table1L: table.
    :type table1L: str.
    :param table2L: table.
    :type table2L: str.
    :param table1Xi: table.
    :type table1Xi: str.

    """
    #
    print(f'Plot name: {pname}')
    #
    hnuc1L = nuda.hnuc.setupRE1LExp( table = table1L )
    hnuc2L = nuda.hnuc.setupRE2LExp( table = table2L )
    hnuc1Xi = nuda.hnuc.setupRE1XiExp( table = table1Xi )
    #
    # plot
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.15, right=None, top=0.95, wspace=0.3, hspace=0.3)
    #
    axs.set_ylabel(r'Proton number $Z$ (log scale)',fontsize='14')
    axs.set_xlabel(r'Neutron number $N$ (log scale)',fontsize='14')
    axs.set_yscale('log')
    axs.set_xscale('log')
    axs.set_xlim([0.8, 140])
    axs.set_ylim([0.8, 90.0])
    #
    axs.scatter( hnuc1L.N,      hnuc1L.Z,      marker='s', s=12, color=nuda.param.col[0], label=r'1$\Lambda$ from table '+table1L )
    axs.scatter( hnuc2L.N+0.05, hnuc2L.Z+0.05, marker='s', s=12, color=nuda.param.col[1], label=r'2$\Lambda$ from table '+table2L )
    axs.scatter( hnuc1Xi.N+0.1, hnuc1Xi.Z+0.1, marker='s', s=12, color=nuda.param.col[2], label=r'1$\Xi^{-}$ from table '+table1Xi )
    #
    #axs.text(0.15,12,r'$K_{sym}$='+str(int(Ksym))+' MeV',fontsize='12')
    axs.legend(loc='lower right',fontsize='11',ncol=1)
    #
    axs.text(1.1,60,'Chart of hypernuclides in nuda toolkit',fontsize='14')
    #
    if pname is not None:
    	plt.savefig(pname, dpi=200)
    	plt.close()
    #
