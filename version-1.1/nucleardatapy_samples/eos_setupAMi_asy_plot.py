
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter eos_setupAMi_asy_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    #folder='figs-new'
    folder='figs'
    nuda.create_folder_fig(folder = folder)
    #
    # fix the uncertainty band
    #
    den = np.array([0.08,0.1,0.12,0.14,0.16])
    models = [ '2016-MBPT-AM', '2016-QMC-NM', '2020-MBPT-AM' ]
    band = nuda.matter.setupMicroBand( models, den=den, matter='NM' )
    #
    # list the available models
    #
    #models, models_lower = nuda.matter.matter_esym_models()
    models = [ 'Skyrme', 'ESkyrme', 'NLRH', 'DDRH', 'DDRHF', 'Var', 'BHF23BF', 'MBPT', 'NLEFT', 'SCGF', 'CC' ]
    models1, models1_lower = nuda.matter.matter_micro_models()
    models2, models2_lower = nuda.matter.matter_pheno_models()
    #
    # fix the asymmetry parameters
    #
    asys = [ 0.6, 0.7, 0.8, 0.9 ]
    #
    for asy in asys:
        #
        # plot lepton, nuclear, and total E/A for a given asymmetric parameter asy
        #
        pname = folder+'/plot_eos_setupAMi_e2a_asy'+str(asy)+'_lep.png'
        nuda.fig.eos_setupAMi_e2a_asy_lep_fig( pname, models1, models2, asy, band )
        #
        pname = folder+'/plot_eos_setupAMi_e2a_asy'+str(asy)+'_nuc.png'
        nuda.fig.eos_setupAMi_e2a_asy_nuc_fig( pname, models1, models2, asy, band )
        #
        pname = folder+'/plot_eos_setupAMi_e2a_asy'+str(asy)+'_tot.png'
        nuda.fig.eos_setupAMi_e2a_asy_tot_fig( pname, models1, models2, asy, band )
        #
        # plot pressure for a given asymmetric parameter asy
        #
        pname = folder+'/plot_eos_setupAMi_pre_asy'+str(asy)+'_lep.png'
        nuda.fig.eos_setupAMi_pre_asy_lep_fig( pname, models1, models2, asy, band )
        #
        pname = folder+'/plot_eos_setupAMi_pre_asy'+str(asy)+'_nuc.png'
        nuda.fig.eos_setupAMi_pre_asy_nuc_fig( pname, models1, models2, asy, band )
        #
        pname = folder+'/plot_eos_setupAMi_pre_asy'+str(asy)+'_tot.png'
        nuda.fig.eos_setupAMi_pre_asy_tot_fig( pname, models1, models2, asy, band )
        #
        # plot cs2 for a given asymmetric parameter asy
        #
        pname = folder+'/plot_eos_setupAMi_cs2_asy'+str(asy)+'_lep.png'
        nuda.fig.eos_setupAMi_cs2_asy_lep_fig( pname, models1, models2, asy, band )
        #
        pname = folder+'/plot_eos_setupAMi_cs2_asy'+str(asy)+'_nuc.png'
        nuda.fig.eos_setupAMi_cs2_asy_nuc_fig( pname, models1, models2, asy, band )
        #
        pname = folder+'/plot_eos_setupAMi_cs2_asy'+str(asy)+'_tot.png'
        nuda.fig.eos_setupAMi_cs2_asy_tot_fig( pname, models1, models2, asy, band )
    #
    print(50*'-')
    print("Exit eos_setupAMi_asy_plot.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
