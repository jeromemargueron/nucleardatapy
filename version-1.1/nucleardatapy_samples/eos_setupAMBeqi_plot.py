
import numpy as np
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter eos_setupAMBeqi_plot.py:")
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
    #models = [ 'Skyrme', 'ESkyrme', 'NLRH', 'DDRH', 'DDRHF', 'Var', 'BHF23BF', 'MBPT', 'NLEFT', 'SCGF', 'CC' ]
    models1, models1_lower = nuda.matter.matter_micro_models()
    models2, models2_lower = nuda.matter.matter_pheno_models()
    #
    # plot energy per particle
    #
    pname = folder+'/plot_eos_setupAMBeqi_e2a_nuc.png'
    nuda.fig.eos_setupAMBeqi_e2a_nuc_fig( pname, models1, models2, band )
    #
    pname = folder+'/plot_eos_setupAMBeqi_e2a_lep.png'
    nuda.fig.eos_setupAMBeqi_e2a_lep_fig( pname, models1, models2, band )
    #
    pname = folder+'/plot_eos_setupAMBeqi_e2a_tot.png'
    nuda.fig.eos_setupAMBeqi_e2a_tot_fig( pname, models1, models2, band )
    #
    # plot pressure
    #
    pname = folder+'/plot_eos_setupAMBeqi_pre_nuc.png'
    nuda.fig.eos_setupAMBeqi_pre_nuc_fig( pname, models1, models2, band )
    #
    pname = folder+'/plot_eos_setupAMBeqi_pre_lep.png'
    nuda.fig.eos_setupAMBeqi_pre_lep_fig( pname, models1, models2, band )
    #
    pname = folder+'/plot_eos_setupAMBeqi_pre_tot.png'
    nuda.fig.eos_setupAMBeqi_pre_tot_fig( pname, models1, models2, band )
    #
    # plot sound speed
    #
    pname = folder+'/plot_eos_setupAMBeqi_cs2_nuc.png'
    nuda.fig.eos_setupAMBeqi_cs2_nuc_fig( pname, models1, models2, band )
    #
    pname = folder+'/plot_eos_setupAMBeqi_cs2_lep.png'
    nuda.fig.eos_setupAMBeqi_cs2_lep_fig( pname, models1, models2, band )
    #
    pname = folder+'/plot_eos_setupAMBeqi_cs2_tot.png'
    nuda.fig.eos_setupAMBeqi_cs2_tot_fig( pname, models1, models2, band )
    #
    # plot the eos
    #
    pname = folder+'/plot_eos_setupAMBeqi_eos.png'
    nuda.fig.eos_setupAMBeqi_eos_fig( pname, models1, models2, band )
    #
    # plot particle fractions
    #
    pname = folder+'/plot_eos_setupAMBeqi_xp.png'
    nuda.fig.eos_setupAMBeqi_xp_fig( pname, models1, models2, band )
    #
    pname = folder+'/plot_eos_setupAMBeqi_xe.png'
    nuda.fig.eos_setupAMBeqi_xe_fig( pname, models1, models2, band )
    #
    pname = folder+'/plot_eos_setupAMBeqi_xmu.png'
    nuda.fig.eos_setupAMBeqi_xmu_fig( pname, models1, models2, band )
    #
    print(50*'-')
    print("Exit eos_setupAMBeqi_plot.py:")
    print(50*'-')
    #

if __name__ == "__main__":
    main()
