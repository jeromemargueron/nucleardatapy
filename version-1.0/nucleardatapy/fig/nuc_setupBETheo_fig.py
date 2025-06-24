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
    axs.set_ylabel(r'$E-E_{DZ}$ (MeV)',fontsize='14')
    axs.set_xlabel(r'N',fontsize='14')
    axs.set_ylim([-5, 5])
    #axs.text(int(Zref)+5,-7,'For Z='+str(Zref),fontsize='12')
    if Zref == 50:
        axs.set_xlim( [ 40, 100 ] )
        axs.text(55,4,'For Z='+str(Zref),fontsize='14')
    elif Zref == 82:
        axs.set_xlim( [ 90, 150 ] )
        axs.text(110,4,'For Z='+str(Zref),fontsize='14')
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
    axs.set_ylabel(r'$S_{2n}$ (MeV)',fontsize='14')
    axs.set_xlabel(r'N',fontsize='14')
    axs.set_xlim([Zref-5, int(2.3*Zref)])
    axs.set_xticks(np.arange(start=Zref-5,stop=2.3*Zref,step=5))
    axs.set_ylim([-40, 0])
    axs.text(int(Zref),-10,'For Z='+str(Zref),fontsize='14')
    #
    # loop over the tables
    #
    for i,table in enumerate( tables ):
        #
        mas = nuda.nuc.setupBETheo( table = table )
        mas2 = mas.isotopes( Zref = Zref )
        s2n = mas2.S2n( Zref = Zref )
        #
        axs.plot( s2n.S2n_N, s2n.S2n_E, linestyle='solid', linewidth=1, label=table )
    #
    exp_table = 'AME'
    exp_version = '2020'
    #
    mas_exp = nuda.nuc.setupBEExp( table = exp_table, version = exp_version )
    mas_exp2 = mas_exp.select( state = 'gs', interp = 'n' )
    mas_exp3 = mas_exp2.isotopes( Zref = Zref )
    s2n_exp = mas_exp3.S2n( Zref = Zref )
    #
    axs.errorbar( s2n_exp.S2n_N, s2n_exp.S2n_E, yerr=s2n_exp.S2n_E_err, fmt='o', label=exp_table+' '+exp_version )
    #axs.scatter( s2n_exp.S2n_N, s2n_exp.S2n_E, label=exp_table+' '+exp_version )
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
    axs.set_ylabel(r'$S_{2p}$ (MeV)',fontsize='14')
    axs.set_xlabel(r'Z',fontsize='14')
    #axs.set_xlim([0.4*Nref, 1.3*Nref])
    axs.set_xlim([0.5*Nref, 1.05*Nref])
    #axs.set_xticks(np.arange(start=int(0.4*Nref),stop=1.3*Nref,step=5))
    axs.set_xticks(np.arange(start=int(0.5*Nref),stop=1.05*Nref,step=5))
    axs.set_ylim([-46, 0])
    axs.text(int(0.7*Nref),-35,'For N='+str(Nref),fontsize='14')
    #
    # loop over the tables
    #
    for i,table in enumerate( tables ):
        #
        mas = nuda.nuc.setupBETheo( table = table )
        mas2 = mas.isotones( Nref = Nref )
        s2p = mas2.S2p( Nref = Nref )
        #
        axs.plot( s2p.S2p_Z, s2p.S2p_E, linestyle='solid', linewidth=1, label=table )
    #
    exp_table = 'AME'
    exp_version = '2020'
    mas_exp = nuda.nuc.setupBEExp( table = exp_table, version = exp_version )
    mas_exp2 = mas_exp.select( state = 'gs', interp = 'n' )
    mas_exp3 = mas_exp2.isotones( Nref = Nref )
    s2p_exp = mas_exp3.S2p( Nref = Nref )
    #
    axs.errorbar( s2p_exp.S2p_Z, s2p_exp.S2p_E, yerr=s2p_exp.S2p_E_err, fmt='o', label=exp_table+' '+exp_version )
    #axs.scatter( s2p_exp.S2p_Z, s2p_exp.S2p_E, label=exp_table+' '+exp_version )
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
    axs.set_ylabel(r'$\Delta_{3n}$ (MeV)',fontsize='12')
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
        mas2 = mas.isotopes( Zref = Zref )
        D3n = mas2.D3n( Zref = Zref )
        #
        axs.plot( D3n.D3n_N_even, D3n.D3n_E_even, linestyle='solid', linewidth=1, label=table+'(even)' )
    #
    exp_table = 'AME'
    exp_version = '2020'
    #
    mas_exp = nuda.nuc.setupBEExp( table = exp_table, version = exp_version )
    mas_exp2 = mas_exp.select( state = 'gs', interp = 'n' )
    mas_exp3 = mas_exp2.isotopes( Zref = Zref )
    D3n_exp = mas_exp3.D3n( Zref = Zref )
    axs.errorbar( D3n_exp.D3n_N_even, D3n_exp.D3n_E_even, yerr=D3n_exp.D3n_E_err_even, fmt='o', label=exp_table+' '+exp_version+'(even)' )
    #axs.scatter( D3n_exp.D3n_N_even, D3n_exp.D3n_E_even, label=exp_table+' '+exp_version+'(even)' )
    #
    # empirical relations:
    axs.plot( D3n.D3n_N_even, nuda.nuc.delta_emp(D3n.D3n_N_even,Zref,formula='classic'), linestyle='solid', linewidth=3, label='classic' )
    axs.plot( D3n.D3n_N_even, nuda.nuc.delta_emp(D3n.D3n_N_even,Zref,formula='Vogel'), linestyle='solid', linewidth=3, label='Vogel' )
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
    axs.set_ylabel(r'$\Delta_{3p}$ (MeV)',fontsize='12')
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
        mas2 = mas.isotones( Nref = Nref )
        D3p = mas2.D3p( Nref = Nref )
        #
        axs.plot( D3p.D3p_Z_even, D3p.D3p_E_even, linestyle='solid', linewidth=1, label=table+'(even)' )
    #
    exp_table = 'AME'
    exp_version = '2020'
    #
    mas_exp = nuda.nuc.setupBEExp( table = exp_table, version = exp_version )
    mas_exp2 = mas_exp.select( state = 'gs', interp = 'n' )
    mas_exp3 = mas_exp2.isotones( Nref = Nref )
    D3p_exp = mas_exp3.D3p( Nref = Nref )
    axs.errorbar( D3p_exp.D3p_Z_even, D3p_exp.D3p_E_even, yerr=D3p_exp.D3p_E_err_even, fmt='o', label=exp_table+' '+exp_version+'(even)' )
    #axs.scatter( D3p_exp.D3p_Z_even, D3p_exp.D3p_E_even, label=exp_table+' '+exp_version+'(even)' )
    #
    # empirical relations:
    axs.plot( D3p.D3p_Z_even, nuda.nuc.delta_emp(Nref,D3p.D3p_Z_even,formula='classic'), linestyle='solid', linewidth=3, label='classic' )
    axs.plot( D3p.D3p_Z_even, nuda.nuc.delta_emp(Nref,D3p.D3p_Z_even,formula='Vogel'), linestyle='solid', linewidth=3, label='Vogel' )
    #
    #axs.legend(loc='upper right',fontsize='8', ncol=4)
    fig.legend(loc='upper left',bbox_to_anchor=(0.1,1.0),columnspacing=2,fontsize='7',ncol=4,frameon=False)
    #
    if pname is not None: 
        plt.savefig(pname, dpi=200)
        plt.close()

    #

