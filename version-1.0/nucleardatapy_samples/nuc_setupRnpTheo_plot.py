
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter nuc_setupRnpTheo_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    nuda.create_folder_fig()
    #
    #tables, tables_lower = nuda.nuc.isgmr_exp_tables()
    #tables = [ '2018-ISGMR-GARG-LATEX', '2022-ISGMR-average' ]
    #
    source = '48Ca'
    pname = 'figs/plot_nuc_setupRnpTheo_source'+source+'.png'
    nuda.fig.nuc_setupRnpTheo_fig( pname, source = source )
    #
    source = '208Pb'
    pname = 'figs/plot_nuc_setupRnpTheo_source'+source+'.png'
    nuda.fig.nuc_setupRnpTheo_fig( pname, source = source )
    #
    print(50*'-')
    print("Exit nuc_setupRnpTheo_plot.py:")
    print(50*'-')
    #

if __name__ == "__main__":
    main()

