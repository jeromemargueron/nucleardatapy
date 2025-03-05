
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter astro_setupMtov_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    nuda.create_folder_fig()
    #
    # sources low
    #
    sources_do, sources_do_lower = nuda.astro.masses_sources( )
    print('Complete list of available sources_lo:',sources_lo)
    #
    sources_lo1 = [ 'J1614–2230', 'J0348+0432', 'J2215+5135', 'J1600+3053', 'J0740+6620' ]
    sources_lo2 = [ 'J1614–2230', 'J0348+0432', 'J0740+6620' ]
    #
    print('sources_low considered:',sources_lo2)
    #
    # sources up
    #
    sources_up1, sources_up_lower = nuda.astro.mup_sources( )
    print('Complete list of available sources_up1:',sources_up1)
    #
    sources_up2 = [ 'GW170817' ]
    #
    print('sources_up2 considered:',sources_up2)
    #
    sources_up3 = [ ]
    #
    print('sources_up3 considered:',sources_up3)
    #
    # plot the results:
    #
    pname = 'figs/plot_astro_setupMtov.png'
    nuda.plot.astro_setupMtov_fig( pname, sources_lo1, sources_lo2, sources_up1, sources_up2, sources_up3 )
    #
    print(50*'-')
    print("Exit astro_setupMtov_plot.py:")
    print(50*'-')
    #

if __name__ == "__main__":
    main()
