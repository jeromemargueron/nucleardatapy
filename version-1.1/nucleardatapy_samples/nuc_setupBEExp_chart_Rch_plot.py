
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter nuc_setupBEExp_chart_Rch_plot.py:")
    print(50*'-')
    #
    # plot nuclear chart lt=life time
    #
    # create the folder where the figures are stored
    #
    #folder='figs-new'
    folder='figs'
    nuda.create_folder_fig(folder = folder)
    #
    # Experimental mass tables
    #
    #tables, tables_lower = nudy.tables_masses_exp()
    tables = [ 'AME' ]
    versions = [ '2020' ]
    #
    # Charge radius experimental table
    #
    Rch_tables, Rch_tables_lower = nuda.nuc.rch_exp_tables()
    Rch_table = '2013-Angeli'
    #
    # loop over the tables
    #
    for i,table in enumerate( tables ):
        #
        version = versions[i]
        pname = folder+'/plot_nuc_setupBEExp_chart_Rch_'+table+'_'+version+'.png'
        print(f'Plot name: {pname}')
        nuda.fig.nuc_setupBEExp_chart_Rch_fig( pname, table, version, Rch_table )
        #
    #
    print(50*'-')
    print("Exit nuc_setupBEExp_chart_Rch_plot.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
