
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter matter_setupPhenoEsym_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    nuda.create_folder_fig()
    # 
    # ===============================
    # Symmetry Energy
    # ===============================
    #
    # Compute the band for Esym
    #
    den = np.array([0.04,0.06,0.08,0.1,0.12,0.14,0.16])
    bmodels = [ '2016-MBPT-AM', '2020-MBPT-AM' ]
    bandEsym = nuda.matter.setupMicroBand( bmodels, den=den, matter='ESYM' )
    #
    # list the available (phenomenological) models
    #
    models, models_lower = nuda.matter.pheno_esym_models()
    #
    # plot symmetry energy
    #
    pname = 'figs/plot_matter_setupPhenoEsym.png'
    #
    nuda.plot.matter_setupPhenoEsym_fig( pname, models, bandEsym )
    #
    print(50*'-')
    print("Exit matter_setupPhenoEsym_plot.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
