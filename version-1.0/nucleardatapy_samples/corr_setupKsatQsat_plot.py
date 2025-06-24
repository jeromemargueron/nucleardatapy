
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
    nuda.create_folder_fig()
    #
    #constraints = [ '1991-Pearson', 'EDF-SKY', 'EDF-ESKY', 'EDF-DDRH', \
    #           'EDF-NLRH', 'EDF-DDRHF', 'EDF-Gogny' ]
    #constraints = [ '1991-Pearson', 'EDF-SKY', 'EDF-SKY2', 'EDF-ESKY', 'EDF-DDRH', \
    #           'EDF-NLRH', 'EDF-DDRHF', 'EDF-Gogny', \
    #           'EDF-xEFT' ]
    constraints, constraints_lower = nuda.corr.KsatQsat_constraints()
    #
    pname = 'figs/plot_corr_setupKsatQsat.png'
    nuda.fig.corr_setupKsatQsat_fig( pname, constraints )
    #
    print(50*'-')
    print("Exit corr_setupKsatQsat_plot.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
