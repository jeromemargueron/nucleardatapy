
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter matter_setupNEPStats_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    nuda.create_folder_fig()
    #
    # list the available models
    #
    models, models_lower = nuda.matter.nep_models()
    #models = [ 'Skyrme', 'GSkyrme', 'ESkyrme', 'Gogny', 'Fayans', 'NLRH', 'DDRH', 'DDRHF' ]
    #
    # plot distribution of NEP
    #
    pname = 'figs/plot_matter_setupNEPStats.png'
    nuda.fig.matter_setupNEPStats_fig( pname, models )
    #
    print(50*'-')
    print("Exit matter_setupNEPStats_plot.py:")
    print(50*'-')
    #

    
if __name__ == "__main__":
    main()
