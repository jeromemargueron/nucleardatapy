
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter matter_setupMicro_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    nuda.create_folder_fig()
    #
    # create the groups of figures
    #
    mbs, mbs_lower = nuda.matter.micro_mbs()
    #mbs = [ 'VAR', 'AFDMC', 'BHF', 'QMC', 'MBPT', 'NLEFT' ]
    #mbs = [ 'VAR' ]
    #mbs = [ 'NLEFT' ]
    print('mbs:',mbs)
    #
    # list the different matter cases investigated
    #
    matters = [ 'NM', 'SM' ]
    #
    for matter in matters:
        #
        # fix the uncertainty band in NM
        #
        if matter.lower() == 'nm':
            bmodels = [ '2016-MBPT-AM', '2016-QMC-NM', '2020-MBPT-AM' ]
        elif matter.lower() == 'sm':
            bmodels = [ '2016-MBPT-AM', '2020-MBPT-AM' ]
        #
        band = nuda.matter.setupMicroBand( bmodels, matter=matter  )
        #
        # plot E/A in matter grouped by mb
        #
        for mb in mbs:
            #
            print('For mb:',mb)
            #
            # list the available models in mb
            #
            models, models_lower = nuda.matter.micro_models_mb_matter( mb, matter = matter )
            #
            pname = 'figs/plot_matter_setupMicro_e2a_'+matter+'_'+mb+'.png'
            #
            nuda.fig.matter_setupMicro_E_fig( pname, mb, models, band, matter )
            #
    #
    print(50*'-')
    print("Exit matter_setupMicro_plot.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
