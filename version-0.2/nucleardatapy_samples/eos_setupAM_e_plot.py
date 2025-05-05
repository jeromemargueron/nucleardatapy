
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter eos_setupAM_e_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    nuda.create_folder_fig()
    #
    # list the available models
    #
    micro_models, micro_models_lower = nuda.matter.micro_esym_models()
    micro_models.remove('1998-VAR-AM-APR-fit')
    micro_models_lower.remove('1998-var-am-apr-fit')
    #micro_models = [ '1998-VAR-AM-APR' ]
    #pheno_models, pheno_models_lower = nuda.matter.pheno_esym_models()
    pheno_models = [ 'Skyrme', 'ESkyrme', 'NLRH', 'DDRH', 'DDRHF' ]
    #
    # plot E/A
    #
    pname = 'figs/plot_eos_setupAM_e.png'
    nuda.fig.eos_setupAM_e_fig( pname, micro_models, pheno_models )
    #
    print(50*'-')
    print("Exit eos_setupAM_e_plot.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
