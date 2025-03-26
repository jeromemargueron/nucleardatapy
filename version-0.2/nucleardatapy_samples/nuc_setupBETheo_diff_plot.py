
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter nuc_setupBETheo_diff_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    nuda.create_folder_fig()
    #
    tables, tables_lower = nuda.nuc.be_theo_tables()
    #tables = [ '1995-DZ' ]
    #
    pname = 'figs/plot_nuc_setupBETheo_diff_Zref50.png'
    nuda.fig.nuc_setupBETheo_diff_fig( pname, tables, Zref = 50 )
    #
    pname = 'figs/plot_nuc_setupBETheo_diff_Zref82.png'
    nuda.fig.nuc_setupBETheo_diff_fig( pname, tables, Zref = 82 )
    #
    print(50*'-')
    print("Exit nuc_setupBETheo_diff_plot.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
