
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
    #constraints = [ '2024-DFT-SKY', '2024-DFT-SKY2', '2024-DFT-ESKY', '2024-DFT-DDRH', \
    #           '2024-DFT-NLRH', '2024-DFT-DDRHF', '2024-DFT-Gogny', \
    #           '2024-DFT-xEFT' ]
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
