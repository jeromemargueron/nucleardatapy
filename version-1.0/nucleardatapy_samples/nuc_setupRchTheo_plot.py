
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter nuc_setupRchTheo_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    nuda.create_folder_fig()
    #
    tables, tables_lower = nuda.nuc.rch_theo_tables()
    table_exp = '2013-Angeli'
    #
    pname = 'figs/plot_nuc_setupRchTheo.png'
    #
    nuda.fig.nuc_setupRchTheo_fig( pname, tables, table_exp )
    #
    print(50*'-')
    print("Exit nuc_setupRchTheo_plot.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
