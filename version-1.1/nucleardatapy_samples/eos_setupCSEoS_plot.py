
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter eos_setupCSEoS_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    #folder='figs-new'
    folder='figs'
    nuda.create_folder_fig(folder = folder)
    #
    # ==============
    # create figure
    # ==============
    #
    pname = folder+'/plot_eos_setupCSEoS.png'
    nuda.fig.setupCSEoS_fig(pname)
    #
    print(50*'-')
    print("Exit eos_setupCSEoS_plot.py")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
