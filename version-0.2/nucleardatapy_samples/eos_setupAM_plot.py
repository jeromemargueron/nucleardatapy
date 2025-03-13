
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter eos_setupAM_e_fig.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    nuda.create_folder_fig()
    #
    # fix the asymmetry parameter
    #
    asy = 0.5
    #
    # fix the uncertainty band
    #
    #den = np.array([0.04,0.06,0.08,0.1,0.12,0.14,0.16])
    #models = [ '2016-MBPT-AM', '2020-MBPT-AM' ]
    #band = nuda.SetupEOSMicroBand( models, den=den, matter='ESYM' )
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
    # plot E/A for a given asymmetric parameter asy
    #
    pname = 'figs/plot_eos_setupAM_e.png'
    nuda.fig.eos_setupAM_e_fig( pname, micro_models, pheno_models, asy )
    #
    print(50*'-')
    print("Exit eos_setupAM_e_fig.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
