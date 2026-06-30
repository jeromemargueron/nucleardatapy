
import numpy as np
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter eos_setupAMLeq_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    nuda.create_folder_fig()
    #
    # fix the uncertainty band
    #
    den = np.array([0.04,0.06,0.08,0.1,0.12,0.14,0.16])
    models = [ '2016-MBPT-AM', '2016-QMC-NM', '2020-MBPT-AM' ]
    band = nuda.matter.setupMicroBand( models, den=den, matter='NM' )
    #
    # list the available models
    #
    #micro_mbs, micro_mbs_lower = nuda.matter.micro_esym_mbs()
    #micro_mbs.remove( 'BHF2' )
    #micro_mbs = [ 'VAR' ]
    micro_mbs = [ 'VAR', 'BHF23', 'MBPT', 'NLEFT' ]
    #
    #pheno_models, pheno_models_lower = nuda.matter.pheno_esym_models()
    pheno_models = [ 'Skyrme', 'ESkyrme', 'NLRH', 'DDRH', 'DDRHF' ]
    #
    # plot particle fractions
    #
    pname = 'figs/plot_eos_setupAMLeq_xe.png'
    nuda.fig.eos_setupAMLeq_xe_fig( pname, micro_mbs, pheno_models, band )
    #
    pname = 'figs/plot_eos_setupAMLeq_xmu.png'
    nuda.fig.eos_setupAMLeq_xmu_fig( pname, micro_mbs, pheno_models, band )
    #
    micro_models = [ ]
    pheno_models = [ 'DDRHF' ]
    pname = 'figs/plot_eos_setupAMLeq_xexmu.png'
    nuda.fig.eos_setupAMLeq_xexmu_fig( pname, micro_mbs, pheno_models, band )
    #
    print(50*'-')
    print("Exit eos_setupAMLeq_plot.py:")
    print(50*'-')
    #

if __name__ == "__main__":
    main()
