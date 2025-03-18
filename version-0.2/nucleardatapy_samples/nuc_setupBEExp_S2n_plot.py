
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter nuc_setupBEExp_S2n_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    nuda.create_folder_fig()
    #
    #tables, tables_lower = nudy.tables_masses_exp()
    tables = [ 'AME' ]
    versions = [ '2020' ]
    #
    pname = 'figs/plot_nuc_setupBEExp_S2n_Nref50.png'
    nuda.fig.nuc_setupBEExp_S2n_fig( pname, tables, versions, Zref = 50 )
    #
    pname = 'figs/plot_nuc_setupBEExp_S2n_Nref20.png'
    nuda.fig.nuc_setupBEExp_S2n_fig( pname, tables, versions, Zref = 20 )
    #
    print(50*'-')
    print("Exit nuc_setupBEExp_S2n_plot.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
