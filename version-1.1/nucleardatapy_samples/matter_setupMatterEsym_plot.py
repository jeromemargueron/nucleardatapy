
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
    models, models_lower = nuda.matter.matter_esym_models()
    #
    # plot symmetry energy
    #
    pname = folder+'/plot_matter_setupMattterEsym.png'
    #
    nuda.fig.matter_setupMatterEsym_fig( pname, models, bandEsym )
    #
    print(50*'-')
    print("Exit matter_setupMatterEsym_plot.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
