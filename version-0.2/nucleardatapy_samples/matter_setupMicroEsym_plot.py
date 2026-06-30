
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter matter_setupMicroEsym_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    nuda.create_folder_fig()
    # 
    # ===============================
    # Symmetry Energy
    # ===============================
    #
    # Compute the band for Esym
    #
    den = np.array([0.06,0.08,0.1,0.12,0.14,0.16])
    bmodels = [ '2016-MBPT-AM', '2020-MBPT-AM' ]
    bandEsym = nuda.matter.setupMicroBand( bmodels, den=den, matter='ESYM' )
    #
    # list the available models
    #
    #micro_mbs, micro_mbs_lower = nuda.matter.micro_mbs()
    #micro_mbs.remove( 'BHF2' )
    #micro_mbs = [ 'VAR' ]
    #micro_mbs = [ 'MBPT' ]
    micro_mbs = [ 'VAR', 'BHF23', 'MBPT', 'NLEFT' ]
    #
    # plot symmetry energy
    #
    pname = 'figs/plot_matter_setupMicroEsym.png'
    #
    nuda.fig.matter_setupMicroEsym_fig( pname, micro_mbs, bandEsym )
    #
    print(50*'-')
    print("Exit matter_setupMicroEsym_plot.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
