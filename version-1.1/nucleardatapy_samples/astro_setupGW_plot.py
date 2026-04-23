
import numpy as np

import nucleardatapy as nuda

def main():
    """Sample script to plot gravitational wave sources."""
    #
    print(50*'-')
    print("Enter astro_setupGW_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    #folder='figs-new'
    folder='figs'
    nuda.create_folder_fig(folder = folder)
    #
    sources, sources_small = nuda.astro.gw_sources( )
    print('Complete list of available sources:',sources)
    #
    sources = [ 'GW170817', 'GW190425' ]
    #
    print('sources considered:',sources)
    #
    pname = folder+'/plot_astro_setupGW.png'
    nuda.fig.astro_setupGW_fig( pname, sources )
    #
    print(50*'-')
    print("Exit astro_setupGW_plot.py:")
    print(50*'-')
    #

if __name__ == "__main__":
    main()
