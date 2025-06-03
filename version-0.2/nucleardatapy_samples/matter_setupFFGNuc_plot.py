
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
    nuda.create_folder_fig()
    #
    den = np.linspace(0.01,2.0,30)
    kfn = np.linspace(0.5,2.0,30)
    mss = [ 1.0, 1., 1. ]
    #mss = [ 1.0, 0.7 ]
    #
    pname = 'figs/plot_matter_setupFFGNuc_EP.png'
    nuda.fig.matter_setupFFGNuc_EP_fig( pname, den = den, kfn = kfn, mss = mss )
    #
    pname = 'figs/plot_matter_setupFFGNuc_EOS.png'
    nuda.fig.matter_setupFFGNuc_EOS_fig( pname, den = den, mss = mss )
    #
    print(50*'-')
    print("Exit matter_setupFFGNuc_plot.py:")
    print(50*'-')
    #

if __name__ == "__main__":
    main()
