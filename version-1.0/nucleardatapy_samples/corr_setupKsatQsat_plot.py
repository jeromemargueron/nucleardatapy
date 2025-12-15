
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
#plt.rcParams.update({'font.size': 16})

import nucleardatapy as nuda


def main():
    #
    print(50*'-')
    print("Enter corr_setupKsatQsat_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    #folder='figs-new'
    folder='figs'
    nuda.create_folder_fig(folder = folder)
    #
    #constraints = [ '1991-Pearson', 'EDF-SKY', 'EDF-ESKY', 'EDF-DDRH', \
    #           'EDF-NLRH', 'EDF-DDRHF', 'EDF-Gogny' ]
    #constraints = [ '1991-Pearson', 'EDF-SKY', 'EDF-SKY2', 'EDF-ESKY', 'EDF-DDRH', \
    #           'EDF-NLRH', 'EDF-DDRHF', 'EDF-Gogny', \
    #           'EDF-xEFT' ]
    constraints, constraints_lower = nuda.corr.KsatQsat_constraints()
    #
    pname = folder+'/plot_corr_setupKsatQsat.png'
    nuda.fig.corr_setupKsatQsat_fig( pname, constraints )
    #
    constraints = [ 'EDF-SKY', 'EDF-ESKY', 'EDF-Gogny', 'EDF-Fayans' ]
    pname = folder+'/plot_corr_setupKsatQsat-2.png'
    nuda.fig.corr_setupKsatQsat_fig( pname, constraints )
    #
    constraints = [ 'EDF-SKY', 'EDF-ESKY', 'EDF-Gogny', 'EDF-Fayans', \
               'EDF-DDRH', 'EDF-NLRH', 'EDF-DDRHF', 'EDF-xEFT' ]
    pname = folder+'/plot_corr_setupKsatQsat-3.png'
    nuda.fig.corr_setupKsatQsat_fig( pname, constraints )
    #
    constraints = [ 'EDF-SKY', 'EDF-ESKY', 'EDF-Gogny', 'EDF-Fayans', \
               'EDF-DDRH', 'EDF-NLRH', 'EDF-DDRHF', 'EDF-xEFT', \
               '1991-Pearson' ]
    pname = folder+'/plot_corr_setupKsatQsat-4.png'
    nuda.fig.corr_setupKsatQsat_fig( pname, constraints )
    #
    constraints = [ 'EDF-SKY', 'EDF-ESKY', 'EDF-Gogny', 'EDF-Fayans', \
               'EDF-DDRH', 'EDF-NLRH', 'EDF-DDRHF', 'EDF-xEFT', \
               '1991-Pearson', '2025-MK-95', '2025-MK-90', '2025-MK-67' ]
    pname = folder+'/plot_corr_setupKsatQsat-5.png'
    nuda.fig.corr_setupKsatQsat_fig( pname, constraints )
    #
    constraints = [ 'EDF-SKY', 'EDF-ESKY', 'EDF-Gogny', 'EDF-Fayans', \
               'EDF-DDRH', 'EDF-NLRH', 'EDF-DDRHF', 'EDF-xEFT', \
               '1991-Pearson', '2025-MK-95', '2025-MK-90', '2025-MK-67', 'EDF-GSKY' ]
    pname = folder+'/plot_corr_setupKsatQsat-6.png'
    nuda.fig.corr_setupKsatQsat_fig( pname, constraints )
    #
    print(50*'-')
    print("Exit corr_setupKsatQsat_plot.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
