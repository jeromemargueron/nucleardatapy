
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter eos_setupAMi_plot.py:")
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
    # plot E/A
    #
    pname = folder+'/plot_eos_setupAMi_e2a.png'
    nuda.fig.eos_setupAMi_e2a_fig( pname, models1, models2, band )
    #
    # plot pressure
    #
    pname = folder+'/plot_eos_setupAMi_pre.png'
    nuda.fig.eos_setupAMi_pre_fig( pname, models1, models2, band )
    #
    # plot sound speed
    #
    pname = folder+'/plot_eos_setupAMi_cs2.png'
    nuda.fig.eos_setupAMi_cs2_fig( pname, models1, models2, band )
    #
    print(50*'-')
    print("Exit eos_setupAMi_plot.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
