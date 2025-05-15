
import numpy as np
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter eos_setupAMBeq_plot.py:")
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
    micro_mbs = [ 'VAR', 'BHF23', 'MBPT', 'NLEFT' ]
    #
    #pheno_models, pheno_models_lower = nuda.matter.pheno_esym_models()
    pheno_models = [ 'Skyrme', 'ESkyrme', 'NLRH', 'DDRH', 'DDRHF' ]
    #
    # plot energy per particle
    #
    pname = 'figs/plot_eos_setupAMBeq_e2a_nuc.png'
    nuda.fig.eos_setupAMBeq_e2a_nuc_fig( pname, micro_mbs, pheno_models, band )
    #
    pname = 'figs/plot_eos_setupAMBeq_e2a_lep.png'
    nuda.fig.eos_setupAMBeq_e2a_lep_fig( pname, micro_mbs, pheno_models, band )
    #
    pname = 'figs/plot_eos_setupAMBeq_e2a_tot.png'
    nuda.fig.eos_setupAMBeq_e2a_tot_fig( pname, micro_mbs, pheno_models, band )
    #
    # plot pressure
    #
    pname = 'figs/plot_eos_setupAMBeq_pre_nuc.png'
    nuda.fig.eos_setupAMBeq_pre_nuc_fig( pname, micro_mbs, pheno_models, band )
    #
    pname = 'figs/plot_eos_setupAMBeq_pre_lep.png'
    nuda.fig.eos_setupAMBeq_pre_lep_fig( pname, micro_mbs, pheno_models, band )
    #
    pname = 'figs/plot_eos_setupAMBeq_pre_tot.png'
    nuda.fig.eos_setupAMBeq_pre_tot_fig( pname, micro_mbs, pheno_models, band )
    #
    # plot particle fractions
    #
    pname = 'figs/plot_eos_setupAMBeq_eos.png'
    nuda.fig.eos_setupAMBeq_eos_fig( pname, micro_mbs, pheno_models, band )
    #
    # plot particle fractions
    #
    pname = 'figs/plot_eos_setupAMBeq_xp.png'
    nuda.fig.eos_setupAMBeq_xp_fig( pname, micro_mbs, pheno_models, band )
    #
    pname = 'figs/plot_eos_setupAMBeq_xe.png'
    nuda.fig.eos_setupAMBeq_xe_fig( pname, micro_mbs, pheno_models, band )
    #
    pname = 'figs/plot_eos_setupAMBeq_xmu.png'
    nuda.fig.eos_setupAMBeq_xmu_fig( pname, micro_mbs, pheno_models, band )
    #
    print(50*'-')
    print("Exit eos_setupAMBeq_plot.py:")
    print(50*'-')
    #

if __name__ == "__main__":
    main()
