
import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter matter_preNM_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    nuda.create_folder_fig()
    #
    # fix the uncertainty band
    #
    den = np.array([0.08,0.1,0.12,0.14,0.16])
    models = [ '2016-MBPT-AM', '2016-QMC-NM', '2020-MBPT-AM' ]
    band = nuda.matter.setupMicroBand( models, den=den, matter='NM' )
    #
    # list the available models
    #
    #micro_mbs, micro_mbs_lower = nuda.matter.micro_mbs()
    #micro_mbs.remove( 'BHF2' )
    #micro_mbs = [ 'VAR' ]
    #micro_mbs = [ 'BHF23' ]
    #micro_mbs = [ 'MBPT' ]
    #micro_mbs = [ 'NLEFT' ]
    #micro_mbs = [ 'AFDMC' ]
    #micro_mbs = [ 'QMC' ]
    micro_mbs = [ 'VAR', 'BHF23', 'MBPT', 'NLEFT', 'AFDMC', 'QMC' ]
    print('micro_mbs:',micro_mbs)
    #
    #pheno_models, pheno_models_lower = nuda.matter.pheno_esym_models()
    pheno_models = [ 'Skyrme', 'ESkyrme', 'NLRH', 'DDRH', 'DDRHF' ]
    #
    # plot pressure
    #
    pname = 'figs/plot_matter_preNM.png'
    nuda.fig.matter_preNM_fig( pname, micro_mbs, pheno_models, band )
    #
    print(50*'-')
    print("Exit matter_preNM_plot.py:")
    print(50*'-')
    #

    
if __name__ == "__main__":
    main()
