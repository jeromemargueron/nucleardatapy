
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
    # list the different matter cases investigated
    #
    matters = [ 'NM', 'SM' ]
    #
    for matter in matters:
        #
        # create the groups of figures
        #
        #mbs, mbs_lower = nuda.matter.micro_mbs()
        #mbs = [ 'VAR' ]
        #mbs = [ 'MBPT' ]
        #mbs = [ 'NLEFT' ]
        #mbs = [ 'AFDMC' ]
        #mbs = [ 'QMC' ]
        #mbs = [ 'VAR', 'AFDMC', 'BHF23', 'QMC', 'MBPT', 'NLEFT' ]
        if matter.lower() == 'nm':
            mbs = [ 'VAR', 'BHF2', 'BHF23', 'MBPT', 'NLEFT', 'AFDMC', 'QMC' ]
        elif matter.lower() == 'sm':
            mbs = [ 'VAR', 'BHF2', 'BHF23', 'MBPT', 'NLEFT' ]
        print('mbs:',mbs)
        #
        # fix the uncertainty band in SM and NM
        #
        if matter.lower() == 'nm':
            bmodels = [ '2016-MBPT-AM', '2016-QMC-NM', '2020-MBPT-AM' ]
        elif matter.lower() == 'sm':
            bmodels = [ '2016-MBPT-AM', '2020-MBPT-AM' ]
        #
        den = np.array([0.08,0.1,0.12,0.14,0.16])
        band = nuda.matter.setupMicroBand( bmodels, matter = matter, den = den  )
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
            print('models:',models)
            if models:
                print('there are models')
            if not models:
                print('there are no models')
                continue
            # remove FIT from AFDMC for the plot:
            if mb == 'AFDMC':
                models2 = []
                for model in models:
                    if 'FIT' not in model:
                        models2.append( model )
                models = models2
                print('AFDMC')
                print('models:',models)
            #
            pname = 'figs/plot_matter_setupMicro_e2a_'+matter+'_'+mb+'.png'
            nuda.fig.matter_setupMicro_e2a_fig( pname, mb, models, band )
            #
            pname = 'figs/plot_matter_setupMicro_pre_'+matter+'_'+mb+'.png'
            nuda.fig.matter_setupMicro_pre_fig( pname, mb, models, band )
            #
            pname = 'figs/plot_matter_setupMicro_cs2_'+matter+'_'+mb+'.png'
            nuda.fig.matter_setupMicro_cs2_fig( pname, mb, models, band )
            #
    #
    print(50*'-')
    print("Exit matter_setupMicro_plot.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
