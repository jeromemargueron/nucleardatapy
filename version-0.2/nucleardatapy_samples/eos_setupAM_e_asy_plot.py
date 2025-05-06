
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter eos_setupAM_e_asy_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    nuda.create_folder_fig()
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

    #pheno_models, pheno_models_lower = nuda.matter.pheno_esym_models()
    pheno_models = [ 'Skyrme', 'ESkyrme', 'NLRH', 'DDRH', 'DDRHF' ]
    #
    # fix the asymmetry parameters
    #
    asys = [ 0.6, 0.7, 0.8, 0.9 ]
    #
    for asy in asys:
        #
        # plot nuclear E/A for a given asymmetric parameter asy
        #
        pname = 'figs/plot_eos_setupAM_e_asy'+str(asy)+'_nuc.png'
        nuda.fig.eos_setupAM_e_asy_nuc_fig( pname, micro_mbs, pheno_models, asy )
        #
        # plot lepton E/A for a given asymmetric parameter asy
        #
        pname = 'figs/plot_eos_setupAM_e_asy'+str(asy)+'_lep.png'
        nuda.fig.eos_setupAM_e_asy_lep_fig( pname, micro_mbs, pheno_models, asy )
        #
        # plot total (nuc+lep) E/A for a given asymmetric parameter asy
        #
        pname = 'figs/plot_eos_setupAM_e_asy'+str(asy)+'_tot.png'
        nuda.fig.eos_setupAM_e_asy_tot_fig( pname, micro_mbs, pheno_models, asy )
    #
    print(50*'-')
    print("Exit eos_setupAM_e_asy_plot.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
