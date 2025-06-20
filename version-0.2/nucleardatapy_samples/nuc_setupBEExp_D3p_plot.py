
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter nuc_setupBEExp_D3p_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    nuda.create_folder_fig()
    #
    #tables, tables_lower = nuda.nuc.be_exp_tables()
    tables = [ 'AME' ]
    #versions, versions_lower = nuda.nuc.be_exp_versions()
    versions = [ '2020' ]
    #
    pname = 'figs/plot_nuc_setupBEExp_D3p_Zref50.png'
    nuda.fig.nuc_setupBEExp_D3p_fig( pname, tables, versions, Nref = 50 )
    #
    print(50*'-')
    print("Exit nuc_setupBEExp_D3p_plot.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
