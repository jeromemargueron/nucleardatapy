
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter hnuc_setupRE1LExp_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    #folder='figs-new'
    folder='figs'
    nuda.create_folder_fig(folder = folder)
    #
    tables, tables_lower = nuda.hnuc.re1L_exp_tables()
    #
    pname = folder+'/plot_hnuc_setupRE1LExp.png'
    #
    nuda.fig.hnuc_setupRE1LExp_fig( pname, tables )
    #
    print(50*'-')
    print("Exit hnuc_setupRE1LExp_plot.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
