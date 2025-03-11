import os
import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter hnuc_setupChart_fig.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    nuda.create_folder_fig()
    #
    #tables, tables_lower = nuda.hnuc.be1L_exp_tables()
    table1L = '2016-1L-GHM'
    table2L = '2013-2L-Ahn'
    table1Xi = '2015-1Xi-Nakazawa'
    #
    pname = 'figs/plot_hnuc_setupChart.png'
    #
    nuda.plot.hnuc_setupChart_fig( pname, table1L, table2L, table1Xi )
    #
    print(50*'-')
    print("Exit hnuc_setupChart_fig.py:")
    print(50*'-')
    #

    
if __name__ == "__main__":
    main()
