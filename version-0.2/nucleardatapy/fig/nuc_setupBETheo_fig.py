import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def nuc_setupBETheo_diff_fig( pname, tables, table_ref = '1995-DZ', Zref = 50 ):
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
    if table_ref in tables:
        tables.remove(table_ref)
    print('Tables:',tables)
    print('Table_ref:',table_ref)
    print('Zref:',Zref)
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.15, bottom=0.13, right=None, top=0.8)#, wspace=0.3, hspace=0.3)
    #
    #axs.set_title(r'Comparison of theoretical mass models',fontsize='12')
    axs.set_ylabel(r'$E-E_{DZ}$ (MeV)',fontsize='12')
    axs.set_xlabel(r'N',fontsize='12')
    axs.set_ylim([-5, 5])
    #axs.text(int(Zref)+5,-7,'For Z='+str(Zref),fontsize='12')
    if Zref == 50:
        axs.set_xlim( [ 40, 100 ] )
        axs.text(55,4,'For Z='+str(Zref),fontsize='12')
    elif Zref == 82:
        axs.set_xlim( [ 90, 150 ] )
        axs.text(110,4,'For Z='+str(Zref),fontsize='12')
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
    axs.scatter( N_diff, BE_diff, label='AME2020',zorder=10 )
    #
    #axs.legend(loc='upper right',fontsize='10', ncol=4)
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=4,frameon=False)
    #
    if pname is not None: 
        plt.savefig(pname, dpi=200)
        plt.close()
    #

def nuc_setupBETheo_S2n_fig( pname, tables, Zref = 50 ):
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
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    #fig.subplots_adjust(left=0.14, bottom=0.15, right=None, top=0.85, wspace=0.3, hspace=0.3)
    fig.subplots_adjust(left=0.15, bottom=0.13, right=None, top=0.8)#, wspace=0.3, hspace=0.3)
    #
    #axs.set_title(r'Comparison of theoretical mass models',fontsize='12')
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
        #
        axs.plot( s2n.S2n_N, s2n.S2n, linestyle='solid', linewidth=1, label=table )
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
    #axs.legend(loc='upper right',fontsize='10', ncol=4)
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=4,frameon=False)
    #
    if pname is not None: 
        plt.savefig(pname, dpi=200)
        plt.close()
    #

def nuc_setupBETheo_S2p_fig( pname, tables, Nref = 50 ):
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
    #fig.subplots_adjust(left=0.14, bottom=0.15, right=None, top=0.85, wspace=0.3, hspace=0.3)
    fig.subplots_adjust(left=0.15, bottom=0.13, right=None, top=0.8)#, wspace=0.3, hspace=0.3)
    #
    #axs.set_title(r'Comparison of theoretical mass models',fontsize='12')
    axs.set_ylabel(r'$S_{2p}$ (MeV)',fontsize='12')
    axs.set_xlabel(r'Z',fontsize='12')
    #axs.set_xlim([0.4*Nref, 1.3*Nref])
    axs.set_xlim([0.5*Nref, 1.05*Nref])
    #axs.set_xticks(np.arange(start=int(0.4*Nref),stop=1.3*Nref,step=5))
    axs.set_xticks(np.arange(start=int(0.5*Nref),stop=1.05*Nref,step=5))
    axs.set_ylim([0, 46])
    axs.text(int(0.7*Nref),35,'For N='+str(Nref),fontsize='12')
    #
    # loop over the tables
    #
    for i,table in enumerate( tables ):
        #
        mas = nuda.nuc.setupBETheo( table = table )
        s2p = mas.S2p( Nmin = Nref, Nmax = Nref )
        #
        axs.plot( s2p.S2p_Z, s2p.S2p, linestyle='solid', linewidth=1, label=table )
    #
    exp_table = 'AME'
    exp_version = '2020'
    mas_exp = nuda.nuc.setupBEExp( table = exp_table, version = exp_version )
    s2p_exp = mas_exp.S2p( Nmin = Nref, Nmax = Nref )
    axs.scatter( s2p_exp.S2p_Z, s2p_exp.S2p, label=exp_table+' '+exp_version )
    #
    #axs.legend(loc='upper right',fontsize='10', ncol=4)
    fig.legend(loc='upper left',bbox_to_anchor=(0.15,1.0),columnspacing=2,fontsize='8',ncol=4,frameon=False)
    #
    if pname is not None: 
        plt.savefig(pname, dpi=200)
        plt.close()
    #

def nuc_setupBETheo_D3n_fig( pname, tables, Zref = 50 ):
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
    print(f'Plot name: {pname}')
    #
    # plot
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    #fig.subplots_adjust(left=0.14, bottom=0.15, right=None, top=0.85, wspace=0.3, hspace=0.3)
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.8)#, wspace=0.3, hspace=0.3)
    #
    #axs.set_title(r'Comparison of theoretical mass models',fontsize='12')
    axs.set_ylabel(r'$\Delta_{3,n}$ (MeV)',fontsize='12')
    axs.set_xlabel(r'N',fontsize='12')
    axs.set_xlim([Zref-5, int(2.3*Zref)])
    axs.set_xticks(np.arange(start=Zref-5,stop=2.3*Zref,step=5))
    axs.set_ylim([0, 4])
    axs.text(int(Zref)+10,3.5,'For Z='+str(Zref),fontsize='12')
    #
    # loop over the tables
    #
    for i,table in enumerate( tables ):
        #
        mas = nuda.nuc.setupBETheo( table = table )
        d3p = mas.D3n( Zmin = Zref, Zmax = Zref )
        #
        axs.plot( d3p.D3n_N_even, d3p.D3n_even, linestyle='solid', linewidth=1, label=table+'(even)' )
    #
    exp_table = 'AME'
    exp_version = '2020'
    mas_exp = nuda.nuc.setupBEExp( table = exp_table, version = exp_version )
    d3n_exp = mas_exp.D3n( Zmin = Zref, Zmax = Zref )
    axs.scatter( d3n_exp.D3n_N_even, d3n_exp.D3n_even, label=exp_table+' '+exp_version+'(even)' )
    #
    #axs.legend(loc='upper right',fontsize='10', ncol=4)
    fig.legend(loc='upper left',bbox_to_anchor=(0.1,1.0),columnspacing=2,fontsize='7',ncol=4,frameon=False)
    #
    if pname is not None: 
        plt.savefig(pname, dpi=200)
        plt.close()
    #

def nuc_setupBETheo_D3p_fig( pname, tables, Nref = 50 ):
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
    pname = 'figs/plot_nuc_setupBETheo_D3p_Nref'+str(Nref)+'.png'
    #
    # plot
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    #fig.subplots_adjust(left=0.14, bottom=0.15, right=None, top=0.85, wspace=0.3, hspace=0.3)
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.8)#, wspace=0.3, hspace=0.3)
    #
    #axs.set_title(r'Comparison of theoretical mass models',fontsize='12')
    axs.set_ylabel(r'$\Delta_{3,p}$ (MeV)',fontsize='12')
    axs.set_xlabel(r'Z',fontsize='12')
    axs.set_xlim([0.4*Nref, 1.1*Nref])
    axs.set_xticks(np.arange(start=int(0.4*Nref),stop=1.2*Nref,step=5))
    axs.set_ylim([0, 4])
    axs.text(int(0.7*Nref),3.5,'For N='+str(Nref),fontsize='12')
    #
    # loop over the tables
    #
    for i,table in enumerate( tables ):
        #
        mas = nuda.nuc.setupBETheo( table = table )
        d3p = mas.D3p( Nmin = Nref, Nmax = Nref )
        #
        axs.plot( d3p.D3p_Z_even, d3p.D3p_even, linestyle='solid', linewidth=1, label=table+'(even)' )
    #
    exp_table = 'AME'
    exp_version = '2020'
    mas_exp = nuda.nuc.setupBEExp( table = exp_table, version = exp_version )
    d3p_exp = mas_exp.D3p( Nmin = Nref, Nmax = Nref )
    axs.scatter( d3p_exp.D3p_Z_even, d3p_exp.D3p_even, label=exp_table+' '+exp_version+'(even)' )
    #
    #axs.legend(loc='upper right',fontsize='8', ncol=4)
    fig.legend(loc='upper left',bbox_to_anchor=(0.1,1.0),columnspacing=2,fontsize='7',ncol=4,frameon=False)
    #
    #
    if pname is not None: 
        plt.savefig(pname, dpi=200)
        plt.close()

    #

