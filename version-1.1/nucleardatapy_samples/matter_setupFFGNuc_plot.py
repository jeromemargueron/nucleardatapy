
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter matter_setupFFGNuc_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    #folder='figs-new'
    folder='figs'
    nuda.create_folder_fig(folder = folder)
    #
    den = np.linspace(0.01,0.35,10)
    kf  = np.linspace(0.5,2.0,10)
    mss = [ 1.0, 0.6, 0.4 ]
    #mss = [ 1.0, 0.7 ]
    #
    pname = folder+'/plot_matter_setupFFGNuc_EP.png'
    nuda.fig.matter_setupFFGNuc_EP_fig( pname, den = den, kf = kf, mss = mss )
    #
    pname = folder+'/plot_matter_setupFFGNuc_EOS.png'
    nuda.fig.matter_setupFFGNuc_EOS_fig( pname, den = den, mss = mss )
    #
    print(50*'-')
    print("Exit matter_setupFFGNuc_plot.py:")
    print(50*'-')
    #

if __name__ == "__main__":
    main()
