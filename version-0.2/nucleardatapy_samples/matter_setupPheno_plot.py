
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter matter_setupPheno_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    nuda.create_folder_fig()
    #
    # create the models for the figures
    #
    #models, models_lower = nuda.modelsPheno()
    models = [ 'Skyrme', 'ESkyrme', 'NLRH', 'DDRH', 'DDRHF' ]
    #models = [ 'Skyrme' ]
    #
    print('models:',models)
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
        den = np.array([0.06,0.08,0.1,0.12,0.14,0.16])
        band = nuda.matter.setupMicroBand( bmodels, den=den, matter = matter )
        #
        # plot E/A in matter grouped by mb
        #
        for model in models:
            #
            print('For model:',model)
            #
            pname = 'figs/plot_matter_setupPheno_e2a_'+matter+'_'+model+'.png'
            #
            nuda.fig.matter_setupPheno_E_fig( pname, model, band )

    #
    print(50*'-')
    print("Exit matter_setupPheno_plot.py:")
    print(50*'-')
    #

if __name__ == "__main__":
    main()

