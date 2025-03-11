
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter matter_setupMicro_LP_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    nuda.create_folder_fig()
    #
    # list the available models
    #
    models, models_lower = nuda.matter.micro_LP_models()
    #
    # plot Landau Parameters L=0 in SM
    #
    pname = 'figs/plot_matter_setupMicro_LP0_SM.png'
    #
    nuda.plot.matter_setupMicro_LP_fig( pname, models, matter = 'SM', ell = 0 )
    #
    # plot Landau Parameters L=1 in SM
    #
    #pname = 'figs/plot_matter_setupMicro_LP1_SM.png'
    #
    #nuda.plot.matter_setupMicro_LP_fig( pname, models, matter = 'SM', ell = 1 )
    #
    # plot Landau Parameters L=0 in NM
    #
    pname = 'figs/plot_matter_setupMicro_LP0_NM.png'
    #
    nuda.plot.matter_setupMicro_LP_fig( pname, models, matter = 'NM', ell = 0 )
    #
    print(50*'-')
    print("Exit matter_setupMicro_LP_plot.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
