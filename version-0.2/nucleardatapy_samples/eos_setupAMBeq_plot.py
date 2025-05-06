
import os
import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter plot_eos_setupAMBeq.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    # fix the uncertainty band
    #
    #den = np.array([0.04,0.06,0.08,0.1,0.12,0.14,0.16])
    #models = [ '2016-MBPT-AM', '2020-MBPT-AM' ]
    #band = nuda.SetupEOSMicroBand( models, den=den, matter='ESYM' )
    #
    # list the available models
    #
    #micro_models, micro_models_lower = nuda.matter.micro_esym_models()
    #micro_models.remove('1998-VAR-AM-APR-fit')
    #micro_models_lower.remove('1998-var-am-apr-fit')
    #micro_models = [ '1998-VAR-AM-APR' ]

    micro_mbs, micro_mbs_lower = nuda.matter.micro_esym_mbs()
    micro_mbs.remove( 'BHF2' )
    #micro_mbs = [ 'VAR' ]

    pheno_models, pheno_models_lower = nuda.matter.pheno_esym_models()
    #pheno_models = [ 'Skyrme', 'ESkyrme', 'NLRH', 'DDRH', 'DDRHF' ]
    #
    # plot energy per particle
    #
    pname = 'figs/plot_eos_setupAMBeq_e2a_nuc.png'
    nuda.fig.eos_setupAMBeq_e2a_nuc_fig( pname, micro_mbs, pheno_models )
    #
    pname = 'figs/plot_eos_setupAMBeq_e2a_lep.png'
    nuda.fig.eos_setupAMBeq_e2a_lep_fig( pname, micro_mbs, pheno_models )
    #
    pname = 'figs/plot_eos_setupAMBeq_e2a_tot.png'
    nuda.fig.eos_setupAMBeq_e2a_tot_fig( pname, micro_mbs, pheno_models )
    #
    # plot pressure
    #
    pname = 'figs/plot_eos_setupAMBeq_pre_nuc.png'
    nuda.fig.eos_setupAMBeq_pre_nuc_fig( pname, micro_mbs, pheno_models )
    #
    pname = 'figs/plot_eos_setupAMBeq_pre_lep.png'
    nuda.fig.eos_setupAMBeq_pre_lep_fig( pname, micro_mbs, pheno_models )
    #
    pname = 'figs/plot_eos_setupAMBeq_pre_tot.png'
    nuda.fig.eos_setupAMBeq_pre_tot_fig( pname, micro_mbs, pheno_models )
    #
    # plot particle fractions
    #
    pname = 'figs/plot_eos_setupAMBeq_xp.png'
    nuda.fig.eos_setupAMBeq_xp_fig( pname, micro_mbs, pheno_models )
    #
    pname = 'figs/plot_eos_setupAMBeq_xe.png'
    nuda.fig.eos_setupAMBeq_xe_fig( pname, micro_mbs, pheno_models )
    #
    pname = 'figs/plot_eos_setupAMBeq_xmu.png'
    nuda.fig.eos_setupAMBeq_xmu_fig( pname, micro_mbs, pheno_models )
    #
    print(50*'-')
    print("Exit plot_eos_setupAMBeq.py:")
    print(50*'-')
    #

if __name__ == "__main__":
    main()
