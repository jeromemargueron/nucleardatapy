
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
    # list the available models in NM
    #
    models, models_lower, models_all, models_all_lower = nuda.matter.micro_effmass_models( matter = 'NM' )
    #
    # plot effective mass
    #
    pname = 'figs/plot_matter_setupMicro_effmass.png'
    #
    nuda.plot.matter_setupMicro_effmass_fig( pname, models )
    #
    print(50*'-')
    print("Exit matter_setupMicro_effmass_plot.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
