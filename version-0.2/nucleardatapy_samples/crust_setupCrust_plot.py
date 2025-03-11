
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter crust_setupCrust_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    nuda.create_folder_fig()
    #
    # list the available models
    #
    models, models_lower = nuda.crust.crust_models()
    #
    # plot crust
    #
    pname = 'figs/plot_crust_setupCrust.png'
    nuda.plot.crust_setupCrust_fig( pname, models )
    #
    print(50*'-')
    print("Exit crust_setupCrust_plot.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
