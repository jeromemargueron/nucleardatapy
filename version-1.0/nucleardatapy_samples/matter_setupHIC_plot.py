
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter matter_setupHIC_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    nuda.create_folder_fig()
    #
    inferences, inferences_lower = nuda.matter.hic_inferences()
    #inferences = [ '2014-IAS' ]
    #
    pname = 'figs/plot_matter_setupHIC.png'
    #
    nuda.fig.matter_setupHIC_fig( pname, inferences )
    #
    print(50*'-')
    print("Exit matter_setupHIC_plot.py:")
    print(50*'-')
    #

if __name__ == "__main__":
    main()
