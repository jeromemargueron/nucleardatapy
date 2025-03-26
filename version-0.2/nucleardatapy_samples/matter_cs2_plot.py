import numpy as np
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter matter_cs2_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    nuda.create_folder_fig()
    #
    # fix the uncertainty band
    #
    den = np.array([0.04,0.06,0.08,0.1,0.12,0.14,0.16])
    models = [ '2016-MBPT-AM', '2020-MBPT-AM' ]
    band = nuda.matter.setupMicroBand( models, den=den, matter='NM' )
    #
    # list the available models
    #
    micro_models, micro_models_lower = nuda.matter.micro_models()
    pheno_models = [ 'Skyrme', 'ESkyrme', 'NLRH', 'DDRH', 'DDRHF' ]
    #
    # plot Esym
    #
    pname = 'figs/plot_matter_cs2.png'
    nuda.fig.matter_cs2_fig( pname, micro_models, pheno_models, band )
    #
    print(50*'-')
    print("Exit matter_cs2_fig.py:")
    print(50*'-')
    #

if __name__ == "__main__":
    main()
