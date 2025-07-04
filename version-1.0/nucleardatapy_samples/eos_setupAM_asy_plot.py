
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter eos_setupAM_asy_plot.py:")
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
    #micro_mbs, micro_mbs_lower = nuda.matter.micro_esym_mbs()
    #micro_mbs.remove( 'BHF2' )
    #micro_mbs = [ 'VAR' ]
    #micro_mbs = [ 'BHF23' ]
    #micro_mbs = [ 'MBPT' ]
    #micro_mbs = [ 'NLEFT' ]
    micro_mbs = [ 'VAR', 'BHF23', 'MBPT', 'NLEFT' ]
    print('micro_mbs:',micro_mbs)
    #
    #pheno_models, pheno_models_lower = nuda.matter.pheno_esym_models()
    pheno_models = [ 'Skyrme', 'ESkyrme', 'NLRH', 'DDRH', 'DDRHF' ]
    #
    # fix the asymmetry parameters
    #
    asys = [ 0.6, 0.7, 0.8, 0.9 ]
    #
    for asy in asys:
        #
        # plot lepton, nuclear, and total E/A for a given asymmetric parameter asy
        #
        pname = 'figs/plot_eos_setupAM_e2a_asy'+str(asy)+'_lep.png'
        nuda.fig.eos_setupAM_e2a_asy_lep_fig( pname, micro_mbs, pheno_models, asy, band )
        #
        pname = 'figs/plot_eos_setupAM_e2a_asy'+str(asy)+'_nuc.png'
        nuda.fig.eos_setupAM_e2a_asy_nuc_fig( pname, micro_mbs, pheno_models, asy, band )
        #
        pname = 'figs/plot_eos_setupAM_e2a_asy'+str(asy)+'_tot.png'
        nuda.fig.eos_setupAM_e2a_asy_tot_fig( pname, micro_mbs, pheno_models, asy, band )
        #
        # plot pressure for a given asymmetric parameter asy
        #
        pname = 'figs/plot_eos_setupAM_pre_asy'+str(asy)+'_lep.png'
        nuda.fig.eos_setupAM_pre_asy_lep_fig( pname, micro_mbs, pheno_models, asy, band )
        #
        pname = 'figs/plot_eos_setupAM_pre_asy'+str(asy)+'_nuc.png'
        nuda.fig.eos_setupAM_pre_asy_nuc_fig( pname, micro_mbs, pheno_models, asy, band )
        #
        pname = 'figs/plot_eos_setupAM_pre_asy'+str(asy)+'_tot.png'
        nuda.fig.eos_setupAM_pre_asy_tot_fig( pname, micro_mbs, pheno_models, asy, band )
        #
        # plot cs2 for a given asymmetric parameter asy
        #
        pname = 'figs/plot_eos_setupAM_cs2_asy'+str(asy)+'_lep.png'
        nuda.fig.eos_setupAM_cs2_asy_lep_fig( pname, micro_mbs, pheno_models, asy, band )
        #
        pname = 'figs/plot_eos_setupAM_cs2_asy'+str(asy)+'_nuc.png'
        nuda.fig.eos_setupAM_cs2_asy_nuc_fig( pname, micro_mbs, pheno_models, asy, band )
        #
        pname = 'figs/plot_eos_setupAM_cs2_asy'+str(asy)+'_tot.png'
        nuda.fig.eos_setupAM_cs2_asy_tot_fig( pname, micro_mbs, pheno_models, asy, band )
    #
    print(50*'-')
    print("Exit eos_setupAM_asy_plot.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
