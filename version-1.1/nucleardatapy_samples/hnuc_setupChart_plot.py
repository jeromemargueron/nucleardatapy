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
    #folder='figs-new'
    folder='figs'
    nuda.create_folder_fig(folder = folder)
    #
    #tables, tables_lower = nuda.hnuc.be1L_exp_tables()
    tables1L = [ '2016-1L-GHM' ]
    #table2L = '2013-2L-Ahn'
    tables2L = [ '1991-2L-Yamamoto', '2013-2L-Ahn', '2019-2L-Ekawa' ]
    tables1Xi = [ '2015-1Xi-Nakazawa' ]
    #
    pname = folder+'/plot_hnuc_setupChart.png'
    #
    nuda.fig.hnuc_setupChart_fig( pname, tables1L, tables2L, tables1Xi )
    #
    print(50*'-')
    print("Exit hnuc_setupChart_fig.py:")
    print(50*'-')
    #

    
if __name__ == "__main__":
    main()
