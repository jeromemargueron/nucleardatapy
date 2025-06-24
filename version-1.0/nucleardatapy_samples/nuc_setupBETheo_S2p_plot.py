
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter nuc_setupBETheo_S2p_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    nuda.create_folder_fig()
    #
    tables, tables_lower = nuda.nuc.be_theo_tables()
    #tables = [ '1995-DZ' ]
    tables.remove( '1988-GK' )
    #
    pname = 'figs/plot_nuc_setupBETheo_S2p_Nref50.png'
    nuda.fig.nuc_setupBETheo_S2p_fig( pname, tables, Nref = 50 )
    #
    print(50*'-')
    print("Exit nuc_setupBETheo_S2p_plot.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
