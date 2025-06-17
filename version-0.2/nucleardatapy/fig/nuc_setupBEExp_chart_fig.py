import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def nuc_setupBEExp_chart_lt_fig( pname, table, version, theo_tables ):
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
    print('Table:',table)
    #
    # plot
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.15, right=None, top=0.85, wspace=0.3, hspace=0.3)
    #
    axs.set_title(r''+table+' mass table version '+version)
    axs.set_ylabel(r'Z',fontsize='14')
    axs.set_xlabel(r'N',fontsize='14')
    axs.set_xlim([0, 200])
    axs.set_ylim([0, 132])
    axs.text(10,120,'Number of nuclei:')
    #
    # longlive nuclei
    #
    mas = nuda.nuc.setupBEExp( table = table, version = version )
    ustbl = mas.select( state= 'gs', interp = 'n', nucleus = 'longlive' )
    axs.scatter( ustbl.sel_nucN, ustbl.sel_nucZ, marker='s', s = 3, linewidth=0, color = 'grey', label='long-lived ('+str(ustbl.sel_nbNucSel)+')' )
    #axs.text(10,96,'long live: '+str(ustbl.sel_nbNucSel))
    #
    # shortlive nuclei
    #
    mas = nuda.nuc.setupBEExp( table = table, version = version )
    ustbl = mas.select( state= 'gs', interp = 'n', nucleus = 'shortlive' )
    axs.scatter( ustbl.sel_nucN, ustbl.sel_nucZ, marker='s', s = 3, linewidth=0, color = 'r', label='short-lived ('+str(ustbl.sel_nbNucSel)+')' )
    #axs.text(10,88,'short live: '+str(ustbl.sel_nbNucSel))
    #
    # veryshortlive nuclei
    #
    mas = nuda.nuc.setupBEExp( table = table, version = version )
    ustbl = mas.select( state= 'gs', interp = 'n', nucleus = 'veryshortlive' )
    axs.scatter( ustbl.sel_nucN, ustbl.sel_nucZ, marker='s', s = 3, linewidth=0, color = 'b', label='very-short-lived ('+str(ustbl.sel_nbNucSel)+')' )
    #axs.text(10,80,'very short live: '+str(ustbl.sel_nbNucSel))
    #
    # hypershortlive nuclei
    #
    mas = nuda.nuc.setupBEExp( table = table, version = version )
    ustbl = mas.select( state= 'gs', interp = 'n', nucleus = 'hypershortlive' )
    axs.scatter( ustbl.sel_nucN, ustbl.sel_nucZ, marker='s', s = 3, linewidth=0, color = 'g', label='hyper-short-lived ('+str(ustbl.sel_nbNucSel)+')' )
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
            axs.scatter( drip_S2n.drip_S2n_N, drip_S2n.drip_S2n_Z, marker='o', s = 3, linewidth=0, color = 'purple', label='Drip Lines' )
            legend = 1
        else:
            axs.scatter( drip_S2n.drip_S2n_N, drip_S2n.drip_S2n_Z, marker='o', s = 3, linewidth=0, color = 'purple' )
        s2p = theo.S2p( Nmin=1, Nmax = 150 )
        drip_S2p = s2p.drip_S2p( Nmin = 1, Nmax = 150 )
        axs.scatter( drip_S2p.drip_S2p_N, drip_S2p.drip_S2p_Z, marker='o', s = 3, linewidth=0, color = 'purple' )
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
    axs.text(49,120,str(ustbl.sel_nbNucSel+stbl.sel_nbNucSel))
    #
    # plot N=Z dotted line
    #
    axs.plot( [0, 130], [0, 130], linestyle='dotted', linewidth=1, color='k')
    axs.text(105,120,'N=Z')
    #
    # plot stable_fit
    #
    N, Z = nuda.stable_fit_Z( Zmin = 1, Zmax = 120 )
    axs.plot( N, Z, linestyle='dashed', linewidth=1, color='k')
    #N, Z = nuda.stable_fit_N( Nmin = 1, Nmax = 200 )
    #axs.plot( N, Z, linestyle='dashed', linewidth=1, color='r')
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
    if pname is not None: 
        plt.savefig(pname, dpi=300)
        plt.close()
    #

def nuc_setupBEExp_chart_year_fig( pname, sYear, year_min, year_max ):
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
    #print('Table:',table)
    #
    # plot
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.15, right=None, top=0.85, wspace=0.3, hspace=0.3)
    #
    #axs.set_title(r''+table+' mass table version '+version)
    axs.set_ylabel(r'Z')
    axs.set_xlabel(r'N')
    axs.set_xlim([0, 200])
    axs.set_ylim([0, 132])
    #axs.text(10,120,'Number of nuclei:')
    axs.text(10,100,'Year: '+str(year_min)+' to '+str(year_max))
    #
    # nuclei given in argument: sYear
    #
    axs.scatter( sYear.sel_N, sYear.sel_Z, marker='s', s = 3, linewidth=0, color = 'grey' )
    #
    # First and last isotopes
    #
    #iso = ustbl.isotopes( Zmin=1, Zmax = 95 )
    #axs.scatter( iso.isotopes_Nmin, iso.isotopes_Z, marker='s', s = 3, linewidth=0, color = 'green', label='Isotope bounds' )
    #axs.scatter( iso.isotopes_Nmax, iso.isotopes_Z, marker='s', s = 3, linewidth=0, color = 'green' )
    #
    # plot N=Z dotted line
    #
    axs.plot( [0, 130], [0, 130], linestyle='dotted', linewidth=1, color='k')
    axs.text(105,120,'N=Z')
    #
    # plot stable_fit
    #
    N, Z = nuda.stable_fit_Z( Zmin = 1, Zmax = 120 )
    axs.plot( N, Z, linestyle='dashed', linewidth=1, color='k')
    N, Z = nuda.stable_fit_N( Nmin = 1, Nmax = 170 )
    axs.plot( N, Z, linestyle='dashed', linewidth=1, color='r')
    #
    # plot shells for isotopes and isotones
    #
    axs = nuda.nuc.plot_shells(axs)
    #
    # set legend
    #
    #axs.legend(loc='lower right',fontsize='10')
    #
    # set plot name and close
    #
    if pname is not None: 
        plt.savefig(pname, dpi=300)
        plt.close()
    #

def nuc_setupBEExp_chart_Rch_fig( pname, table, version, Rch_table ):
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
    print('Table:',table)
    #
    # plot
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.15, right=None, top=0.85, wspace=0.3, hspace=0.3)
    #
    axs.set_title(r''+table+' mass table version '+version+' + '+Rch_table+' charge radius table')
    axs.set_ylabel(r'Z')
    axs.set_xlabel(r'N')
    axs.set_xlim([0, 200])
    axs.set_xticks([0,25,50,75,100,125,150,175,200])
    axs.set_ylim([0, 132])
    axs.set_yticks([0,20,40,60,80,100,120])
    axs.text(10,120,'Number of nuclei:')
    #
    # First and last isotopes
    #
    mas = nuda.nuc.setupBEExp( table = table, version = version )
    ustbl = mas.select( state= 'gs', interp = 'n', nucleus = 'unstable' )
    iso = ustbl.isotopes( Zmin=1, Zmax = 95 )
    axs.scatter( iso.isotopes_Nmin, iso.isotopes_Z, marker='s', s = 3, linewidth=0, color = 'green', label='AME boundaries' )
    axs.scatter( iso.isotopes_Nmax, iso.isotopes_Z, marker='s', s = 3, linewidth=0, color = 'green' )
    #
    # stable nuclei:
    #
    mas = nuda.nuc.setupBEExp( table = table, version = version )
    stbl = mas.select( state= 'gs', interp = 'n', nucleus = 'stable' )
    axs.scatter( stbl.sel_nucN, stbl.sel_nucZ, marker='s', s = 3, linewidth=0, color = 'k' )
    axs.text(10,112,'stable: '+str(stbl.sel_nbNucSel))
    axs.text(60,120,str(ustbl.sel_nbNucSel+stbl.sel_nbNucSel))
    #
    # Charge radii:
    #
    rch = nuda.nuc.setupRchExp( table = Rch_table )
    axs.scatter( rch.nucN, rch.nucZ, marker='s', s = 3, linewidth=0, color = 'blue', label = 'charge radii' )
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
    if pname is not None: 
        plt.savefig(pname, dpi=300)
        plt.close()
    #

