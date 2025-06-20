import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def nuc_setupISGMRExp_fig( pname, tables ):
    """
    Plot nuclear chart (N versus Z).\
    The plot is 1x1 with:\
    [0]: nuclear chart.

    :param pname: name of the figure (*.png)
    :type pname: str.
    :param table: table.
    :type table: str.
    :param version: version of table to run on.
    :type version: str.
    :param theo_tables: object instantiated on the reference band.
    :type theo_tables: object.

    """
    #
    print(f'Plot name: {pname}')
    #
    obs = 'M12Mm1'
    #
    nucZ = [ 40, 50, 82 ]
    #
    fig, axs = plt.subplots(1,3)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.15, right=0.95, top=0.85, wspace=0.1, hspace=0.3)
    #
    if obs == 'M12M0':
        axs[0].set_ylabel(r'$E_{ISGMR}$ from $m_1/m_0$ (MeV)',fontsize='14')
    elif obs == 'M12Mm1':
        axs[0].set_ylabel(r'$E_{ISGMR}$ from $\sqrt{m_1/m_{-1}}$ (MeV)',fontsize='14')
    elif obs == 'M12Mm1':
        axs[0].set_ylabel(r'$E_{ISGMR}$ from $\sqrt{m_3/m_1}$ (MeV)',fontsize='14')
    #
    for k,table in enumerate( tables ):
        #
        print('Table:',table)
        gmr = nuda.nuc.setupISGMRExp( table = table )
        for i in [0,1,2]:
            print('For Z = ',nucZ[i])
            axs[i].set_title(nuda.param.elements[nucZ[i]-1])
            axs[i].set_xlabel(r'A',fontsize='14')
            axs[i].set_ylim([13, 18])
            if i>0: axs[i].tick_params('y', labelleft=False)
            gmrs = gmr.select( Zref = nucZ[i], obs = obs )
            x = gmrs.nucA+0.2*k*np.ones(len(gmrs.nucA))
            axs[i].errorbar( x, gmrs.cent, yerr=gmrs.erra, fmt='o', label=gmr.label )
    #
    axs[2].legend(loc='upper right',fontsize='10')
    #
    if pname is not None: 
    	plt.savefig(pname, dpi=200)
    	plt.close()
    #