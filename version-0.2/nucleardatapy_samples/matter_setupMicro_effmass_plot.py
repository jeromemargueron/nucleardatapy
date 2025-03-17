
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter matter_setupMicro_effmass_plot.py:")
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
    # plot effective mass in NM
    #
    models, models_lower, models_all, models_all_lower = nuda.matter.micro_effmass_models( matter = 'NM' )
    #
    pname = 'figs/plot_matter_setupMicro_effmass_NM.png'
    #
    nuda.fig.matter_setupMicro_effmass_fig( pname, models, matter = 'NM' )
    #
    # plot effective mass in SM
    #
    models, models_lower, models_all, models_all_lower = nuda.matter.micro_effmass_models( matter = 'SM' )
    #
    pname = 'figs/plot_matter_setupMicro_effmass_SM.png'
    #
    nuda.fig.matter_setupMicro_effmass_fig( pname, models, matter = 'SM' )
    #
    # plot effective mass in AM
    #
    models, models_lower, models_all, models_all_lower = nuda.matter.micro_effmass_models( matter = 'AM' )
    #
    pname = 'figs/plot_matter_setupMicro_effmass_AM.png'
    #
    nuda.fig.matter_setupMicro_effmass_fig( pname, models, matter = 'AM' )
    #
    print(50*'-')
    print("Exit matter_setupMicro_effmass_plot.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
