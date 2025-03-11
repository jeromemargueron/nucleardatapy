
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter astro_setupMup_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    nuda.create_folder_fig()
    #
    sources, sources_lower = nuda.astro.mup_sources( )
    print('Complete list of available sources:',sources)
    #
    sources = [ 'GW170817', 'GW190814' ]
    #
    print('sources considered:',sources)
    #
    pname = 'figs/plot_astro_setupMup.png'
    nuda.plot.astro_setupMup_fig( pname, sources )
    #
    print(50*'-')
    print("Exit astro_setupMup_plot.py:")
    print(50*'-')
    #

if __name__ == "__main__":
    main()
