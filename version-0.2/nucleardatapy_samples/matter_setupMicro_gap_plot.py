
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter matter_setupMicro_gap_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    nuda.create_folder_fig()
    # 
    # ===============================
    # Neutron Matter (NM)
    # ===============================
    #
    # list the available models in NM
    #
    models, models_lower, models_all, models_all_lower = nuda.matter.micro_gap_models( matter = 'NM' )
    #
    # plot 1S0 pairing gaps in NM
    #
    pname = 'figs/plot_matter_setupMicro_gap_1s0_NM.png'
    #
    nuda.fig.matter_setupMicro_gap_1s0_fig( pname, models, matter = 'NM' )
    #
    # plot 3PF2 pairing gaps in NM
    #
    pname = 'figs/plot_matter_setupMicro_gap_3pf2_NM.png'
    #
    nuda.fig.matter_setupMicro_gap_3pf2_fig( pname, models, matter = 'NM' )
    #
    # list the available models in SM
    #
    models, models_lower, models_all, models_all_lower = nuda.matter.micro_gap_models( matter = 'SM' )
    #
    # plot 1S0 pairing gaps in SM
    #
    pname = 'figs/plot_matter_setupMicro_gap_1s0_SM.png'
    #
    nuda.fig.matter_setupMicro_gap_1s0_fig( pname, models, matter = 'SM' )
    #
    print(50*'-')
    print("Exit matter_setupMicro_gap_plot.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
