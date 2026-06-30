
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter matter_setupNEPModelDist_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    nuda.create_folder_fig()
    #
    # list the available models
    #
    #models = [ 'Skyrme', 'ESkyrme', 'Gogny', 'Fayans', 'NLRH', 'DDRH', 'DDRHF' ]
    models, models_lower = nuda.matter.nep_models()
    #
    # plot distribution of NEP
    #
    pname = 'figs/plot_matter_setupNEPModelDist.png'
    nuda.fig.matter_setupNEPModelDist_fig( pname, models )
    #
    print(50*'-')
    print("Exit matter_setupNEPModelDist_plot.py:")
    print(50*'-')
    #

    
if __name__ == "__main__":
    main()
