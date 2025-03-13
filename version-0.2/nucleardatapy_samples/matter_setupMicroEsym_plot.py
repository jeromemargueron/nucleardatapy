
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter matter_setupMicroEsym_plot.py:")
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
    # list the available (microscopic) models
    #
    models, models_lower = nuda.matter.micro_esym_models()
    models.remove('1998-VAR-AM-APR-fit')
    models_lower.remove('1998-var-am-apr-fit')
    #
    # plot symmetry energy
    #
    pname = 'figs/plot_matter_setupMicroEsym.png'
    #
    nuda.fig.matter_setupMicroEsym_fig( pname, models, bandEsym )
    #
    print(50*'-')
    print("Exit matter_setupMicroEsym_plot.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
