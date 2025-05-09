import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def nuc_setupBEExp_year_fig( pname, table, version ):
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
    print(50*'-')
    print("Enter nuc_setupBEExp_year_fig.py:")
    print(50*'-')
    #
    print(f'Plot name: {pname}')
    #
    print('Table:',table)
    #
    # read all the mass table:
    #
    mas = nuda.nuc.setupBEExp( table = table, version = version )
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
    if pname is not None: 
        plt.savefig(pname, dpi=200)
        plt.close()
    #
    print(50*'-')
    print("Exit nuc_setupBEExp_year_fig.py:")
    print(50*'-')
    #

def nuc_setupBEExp_S2n_fig( pname, tables, versions, Zref = 50 ):
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
    print('Tables:',tables)
    print('Zref:',Zref)
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.14, bottom=0.15, right=None, top=0.85, wspace=0.3, hspace=0.3)
    #
    axs.set_title(r'Experimental mass tables',fontsize='12')
    axs.set_ylabel(r'$S_{2n}$ (MeV)',fontsize='12')
    axs.set_xlabel(r'N',fontsize='12')
    axs.set_xlim([Zref-5, int(1.85*Zref)])
    axs.set_xticks(np.arange(start=Zref-5,stop=2*Zref,step=5))
    #axs.set_ylim([-10, 10])
    axs.text(int(Zref),10,'For Z='+str(Zref),fontsize='12')
    #
    # loop over the tables
    #
    for i,table in enumerate( tables ):
        #
        version = versions[i]
        # plot nuclear chart:
        mas_exp = nuda.nuc.setupBEExp( table = table, version = version )
        s2n_exp = mas_exp.S2n( Zmin = Zref, Zmax = Zref )
        axs.scatter( s2n_exp.S2n_N, s2n_exp.S2n, label=table+' '+version )
        #axs.plot( s2n_exp.S2n_N, s2n_exp.S2n, linestyle='solid', linewidth=1, label=exp_table+' '+exp_version )
    #
    axs.legend(loc='upper right',fontsize='10', ncol=1)
    #
    if pname is not None: 
        plt.savefig(pname, dpi=200)
        plt.close()
    #

def nuc_setupBEExp_S2p_fig( pname, tables, versions, Nref = 50 ):
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
    print('Tables:',tables)
    print('Nref:',Nref)
    #
    print(f'Plot name: {pname}')
    #
    # plot
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.14, bottom=0.15, right=None, top=0.85, wspace=0.3, hspace=0.3)
    #
    axs.set_title(r'Experimental mass tables',fontsize='12')
    axs.set_ylabel(r'$S_{2p}$ (MeV)',fontsize='12')
    axs.set_xlabel(r'Z',fontsize='12')
    axs.set_xlim([0.4*Nref, 1.2*Nref])
    axs.set_xticks(np.arange(start=int(0.4*Nref),stop=1.2*Nref,step=5))
    #axs.set_ylim([-10, 10])
    axs.text(int(0.7*Nref),10,'For N='+str(Nref),fontsize='12')
    #
    # loop over the tables
    #
    for i,table in enumerate( tables ):
        #
        version = versions[i]
        # plot nuclear chart:
        mas_exp = nuda.nuc.setupBEExp( table = table, version = version )
        s2p_exp = mas_exp.S2p( Nmin = Nref, Nmax = Nref )
        axs.scatter( s2p_exp.S2p_Z, s2p_exp.S2p, label=table+' '+version )
    #
    axs.legend(loc='upper right',fontsize='10', ncol=1)
    #
    if pname is not None: 
        plt.savefig(pname, dpi=200)
        plt.close()
    #

def nuc_setupBEExp_D3n_fig( pname, tables, versions, Zref = 50 ):
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
    print('Tables:',tables)
    print('Zref:',Zref)
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
        d3n_exp = mas_exp.D3n( Zmin = Zref, Zmax = Zref )
        axs.scatter( d3n_exp.D3n_N_even, d3n_exp.D3n_even, label=table+' '+version+'(even)' )
        axs.scatter( d3n_exp.D3n_N_odd,  d3n_exp.D3n_odd,  label=table+' '+version+'(odd)' )
    #
    axs.legend(loc='upper right',fontsize='10', ncol=1)
    #
    if pname is not None: 
        plt.savefig(pname, dpi=200)
        plt.close()
    #

def nuc_setupBEExp_D3p_fig( pname, tables, versions, Nref = 50 ):
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
    print('Tables:',tables)
    print('Nref:',Nref)
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
        d3p_exp = mas_exp.D3p( Nmin = Nref, Nmax = Nref )
        axs.scatter( d3p_exp.D3p_Z_even, d3p_exp.D3p_even, label=table+' '+version+'(even)' )
        axs.scatter( d3p_exp.D3p_Z_odd,  d3p_exp.D3p_odd,  label=table+' '+version+'(odd)' )
    #
    axs.legend(loc='upper right',fontsize='10', ncol=1)
    #
    if pname is not None: 
        plt.savefig(pname, dpi=200)
        plt.close()
    #