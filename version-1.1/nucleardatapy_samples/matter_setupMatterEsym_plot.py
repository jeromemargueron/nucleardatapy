
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter matter_setupMatterEsym_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    #folder='figs-new'
    folder='figs'
    nuda.create_folder_fig(folder = folder)
    # 
    # ===============================
    # Symmetry Energy
    # ===============================
    #
    # Compute the band for Esym
    #
    den = np.array([0.08,0.1,0.12,0.14,0.16])
    bmodels = [ '2016-MBPT-AM', '2020-MBPT-AM' ]
    bandEsym = nuda.matter.setupMicroBand( bmodels, den=den, matter='ESYM' )
    #
    # list the available (phenomenological) models
    #
    #models, models_lower = nuda.matter.matter_models()
    models = [ 'Skyrme', 'ESkyrme', 'NLRH', 'DDRH', 'DDRHF', 'Var', 'MC', 'MBPT', 'NLEFT', 'BHF2BF', 'BHF23BF', 'SCGF', 'CC' ]
    #models = [ 'Skyrme' ]
    #models = [ 'ESkyrme' ]
    #models = [ 'NLRH' ]
    #models = [ 'DDRH' ]
    #models = [ 'DDRHF' ]
    #models = [ 'Var' ]
    #models = [ 'MC' ]
    #models = [ 'MBPT' ]
    #models = [ 'NLEFT' ]
    #models = [ 'BHF2BF' ]
    #models = [ 'BHF23BF' ]
    #models = [ 'SCGF' ]
    #models = [ 'CC' ]
    #
    # plot symmetry energy
    #
    for model in models:
        #
        pname = folder+'/plot_matter_setupMattterEsym'+model+'.png'
        #
        nuda.fig.matter_setupMatterEsym_fig( pname, model, bandEsym )
    #
    print(50*'-')
    print("Exit matter_setupMatterEsym_plot.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
