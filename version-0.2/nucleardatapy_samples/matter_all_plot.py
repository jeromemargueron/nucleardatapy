
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter matter_all_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    nuda.create_folder_fig()
    #
    # fix the uncertainty band to check (and select models)
    #
    den = np.array([0.08,0.1,0.12,0.14,0.16])
    bmodels = [ '2016-MBPT-AM', '2016-QMC-NM', '2020-MBPT-AM' ]
    band_check = nuda.matter.setupMicroBand( bmodels, matter = 'NM', den = den  )
    #
    # list the different matter cases investigated
    #
    matters = [ 'NM', 'SM' ]
    #
    for matter in matters:
        #
        # create the groups of figures
        #
        #micro_mbs, micro_mbs_lower = nuda.matter.micro_mbs()
        #micro_mbs = [ 'VAR' ]
        #micro_mbs = [ 'MBPT' ]
        #micro_mbs = [ 'NLEFT' ]
        #micro_mbs = [ 'AFDMC' ]
        #micro_mbs = [ 'QMC' ]
        #micro_mbs = [ 'VAR', 'AFDMC', 'BHF23', 'QMC', 'MBPT', 'NLEFT' ]
        if matter.lower() == 'nm':
            micro_mbs = [ 'VAR', 'BHF23', 'MBPT', 'NLEFT', 'AFDMC', 'QMC' ]
        elif matter.lower() == 'sm':
            micro_mbs = [ 'VAR', 'BHF23', 'MBPT', 'NLEFT' ]
        print('micro_mbs:',micro_mbs)
        #
        #pheno_models, pheno_models_lower = nuda.matter.pheno_esym_models()
        pheno_models = [ 'Skyrme', 'ESkyrme', 'NLRH', 'DDRH', 'DDRHF' ]
        #
        # fix the uncertainty band to plot
        #
        if matter.lower() == 'nm':
            bmodels = [ '2016-MBPT-AM', '2016-QMC-NM', '2020-MBPT-AM' ]
        elif matter.lower() == 'sm':
            bmodels = [ '2016-MBPT-AM', '2020-MBPT-AM' ]
        band_plot = nuda.matter.setupMicroBand( bmodels, matter = matter, den = den  )
        #
        # plot e2a in SM and NM
        #
        pname = 'figs/plot_matter_all_e2a_'+matter+'.png'
        nuda.fig.matter_all_e2a_fig( pname, micro_mbs, pheno_models, band_plot, band_plot, matter )
        #
        # plot pre in SM and NM
        #
        pname = 'figs/plot_matter_all_pre_'+matter+'.png'
        nuda.fig.matter_all_pre_fig( pname, micro_mbs, pheno_models, band_check, matter )
        #
        # plot eos in SM and NM
        #
        pname = 'figs/plot_matter_all_eos_'+matter+'.png'
        nuda.fig.matter_all_eos_fig( pname, micro_mbs, pheno_models, band_check, matter )
        #
        # plot cs2 in SM and NM
        #
        pname = 'figs/plot_matter_all_cs2_'+matter+'.png'
        nuda.fig.matter_all_cs2_fig( pname, micro_mbs, pheno_models, band_check, matter )
        #

    #
    # plot Esym
    #
    den = np.array([0.08,0.1,0.12,0.14,0.16])
    bmodels = [ '2016-MBPT-AM', '2020-MBPT-AM' ]
    band_plot = nuda.matter.setupMicroBand( bmodels, matter = 'ESYM', den = den  )
    #
    #micro_mbs, micro_mbs_lower = nuda.matter.micro_esym_mbs()    
    #micro_mbs.remove( 'BHF2' )
    micro_mbs = [ 'VAR', 'BHF23', 'MBPT', 'NLEFT' ]
    #
    #pheno_models, pheno_models_lower = nuda.matter.pheno_esym_models()
    pheno_models = [ 'Skyrme', 'ESkyrme', 'NLRH', 'DDRH', 'DDRHF' ]
    #
    pname = 'figs/plot_matter_all_Esym.png'
    nuda.fig.matter_all_Esym_fig( pname, micro_mbs, pheno_models, band_plot, band_plot )

#    pname = 'figs/plot_matter_ESM.png'
#    nuda.fig.matter_ESM_fig( pname, micro_mbs, pheno_models, band )
    #
    print(50*'-')
    print("Exit matter_all_plot.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
