
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter eos_setupAMLeq_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    nuda.create_folder_fig()
    #
    # list the available models
    #
    #micro_models, micro_models_lower = nuda.matter.micro_esym_models()
    #micro_models.remove('1998-VAR-AM-APR-fit')
    #micro_models_lower.remove('1998-var-am-apr-fit')
    #micro_models = [ '1998-VAR-AM-APR' ]

    micro_mbs, micro_mbs_lower = nuda.matter.micro_esym_mbs()
    micro_mbs.remove( 'BHF2' )
    #micro_mbs = [ 'VAR' ]

    pheno_models, pheno_models_lower = nuda.matter.pheno_esym_models()
    #pheno_models = [ 'Skyrme', 'ESkyrme', 'NLRH', 'DDRH', 'DDRHF' ]
    #
    # plot Esym
    #
    pname = 'figs/plot_eos_setupAMLeq_xe.png'
    nuda.fig.eos_setupAMLeq_xe_fig( pname, micro_mbs, pheno_models )
    #
    pname = 'figs/plot_eos_setupAMLeq_xmu.png'
    nuda.fig.eos_setupAMLeq_xmu_fig( pname, micro_mbs, pheno_models )
    #
    micro_models = [ ]
    pheno_models = [ 'DDRHF' ]
    pname = 'figs/plot_eos_setupAMLeq_xexmu.png'
    nuda.fig.eos_setupAMLeq_xexmu_fig( pname, micro_mbs, pheno_models )
    #
    print(50*'-')
    print("Exit eos_setupAMLeq_plot.py:")
    print(50*'-')
    #

if __name__ == "__main__":
    main()
