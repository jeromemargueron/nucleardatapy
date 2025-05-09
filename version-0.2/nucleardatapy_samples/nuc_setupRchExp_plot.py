
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter nuc_setupRchExp_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    nuda.create_folder_fig()
    #
    tables, tables_lower = nuda.nuc.rch_exp_tables()
    #
    pname = 'figs/plot_nuc_setupRchExp.png'
    #
    nuda.fig.nuc_setupRchExp_fig( pname, tables )
    #
    print(50*'-')
    print("Exit nuc_setupRchExp_plot.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
