
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter matter_Esym_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    nuda.create_folder_fig()
    #
    # fix the uncertainty band
    #
    den = np.array([0.04,0.06,0.08,0.1,0.12,0.14,0.16])
    models = [ '2016-MBPT-AM', '2020-MBPT-AM' ]
    band = nuda.matter.setupMicroBand( models, den=den, matter='ESYM' )
    #
    # list the available models
    #
    micro_mbs, micro_mbs_lower = nuda.matter.micro_esym_mbs()    
    pheno_models = [ 'Skyrme', 'NLRH', 'DDRH', 'DDRHF' ]
    #
    # plot Esym
    #
    pname = 'figs/plot_matter_Esym.png'
    nuda.plot.matter_Esym_fig( pname, micro_mbs, pheno_models, band )
    #
    print(50*'-')
    print("Exit matter_Esym_plot.py:")
    print(50*'-')
    #

    
if __name__ == "__main__":
    main()
