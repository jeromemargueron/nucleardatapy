
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter nuc_setupISGMRExp_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    nuda.create_folder_fig()
    #
    #tables, tables_lower = nuda.nuc.isgmr_exp_tables()
    tables = [ '2010-ISGMR-LI', '2018-ISGMR-GARG', '2022-ISGMR-average' ]
    #
    pname = 'figs/plot_nuc_setupISGMRExp.png'
    #
    nuda.fig.nuc_setupISGMRExp_fig( pname, tables )
    #
    print(50*'-')
    print("Exit nuc_setupISGMRExp_plot.py:")
    print(50*'-')
    #

if __name__ == "__main__":
    main()
