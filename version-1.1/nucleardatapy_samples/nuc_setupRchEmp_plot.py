
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter nuc_setupRchEmp_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    #folder='figs-new'
    folder='figs'
    nuda.create_folder_fig(folder = folder)
    #
    tables, tables_lower = nuda.nuc.rch_theo_tables()
    table_exp = '2013-Angeli'
    #
    pname = folder+'/plot_nuc_setupRchEmp.png'
    #
    nuda.fig.nuc_setupRchEmp_fig( pname, tables, table_exp )
    #
    print(50*'-')
    print("Exit nuc_setupRchEmp_plot.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
