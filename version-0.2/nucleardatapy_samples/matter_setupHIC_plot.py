
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
    constraints, constraints_lower = nuda.matter.hic_constraints()
    #constraints = [ '2014-IAS' ]
    #
    pname = 'figs/plot_matter_setupHIC.png'
    #
    nuda.plot.matter_setupHIC_fig( pname, constraints )
    #
    print(50*'-')
    print("Exit matter_setupHIC_plot.py:")
    print(50*'-')
    #

if __name__ == "__main__":
    main()
