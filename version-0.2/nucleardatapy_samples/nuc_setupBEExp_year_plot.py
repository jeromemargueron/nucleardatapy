
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter nuc_setupBEExp_year_plot.py:")
    print(50*'-')
    #
    # plot discovery years
    #
    # create the folder where the figures are stored
    #
    nuda.create_folder_fig()
    #
    #tables, tables_lower = nudy.tables_masses_exp()
    tables = [ 'AME' ]
    versions = [ '2020' ]
    #
    # loop over the tables
    #
    for i,table in enumerate( tables ):
        #
        version = versions[i]
        pname = 'figs/plot_nuc_setupBEExp_year_'+table+'_'+version+'.png'
        nuda.fig.nuc_setupBEExp_year_fig( pname, table, version )
    #
    print(50*'-')
    print("Exit nuc_setupBEExp_year_plot.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
