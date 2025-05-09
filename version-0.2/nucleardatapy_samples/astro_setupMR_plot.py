
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter astro_setupMR_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    nuda.create_folder_fig()
    #
    sources, sources_lower = nuda.astro.mr_sources( )
    print('Complete list of available sources:',sources)
    #
    sources = [ 'J0030+0451', 'J0740+6620', 'J0437-4715' ]
    sources_av = [ 'J0030+0451', 'J0740+6620' ]
    #
    print('sources considered:',sources)
    #
    pname = 'figs/plot_astro_setupMR.png'
    nuda.fig.astro_setupMR_fig( pname, sources, sources_av )
    #
    print(50*'-')
    print("Exit astro_setupMR_plot.py:")
    print(50*'-')
    #

if __name__ == "__main__":
    main()
