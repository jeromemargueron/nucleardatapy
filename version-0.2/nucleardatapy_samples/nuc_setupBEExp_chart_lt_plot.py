
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter nuc_setupBEExp_chart_lt_plot.py:")
    print(50*'-')
    #
    # plot nuclear chart lt=life time
    #
    # create the folder where the figures are stored
    #
    nuda.create_folder_fig()
    #
    # Experimental mass tables
    #
    #tables, tables_lower = nudy.tables_masses_exp()
    tables = [ 'AME' ]
    versions = [ '2020' ]
    #
    # Theoretical mass tables (for models predicting driplines)
    #
    #theo_tables, theo_tables_lower = nuda.nuc.be_theo_tables()
    theo_tables = [ '2013-HFB22', '2013-HFB23', '2013-HFB24', '2013-HFB25', \
    '2013-HFB26', '2021-BSkG1', '2022-BSkG2', '2023-BSkG3' ]
    #
    # loop over the tables
    #
    for i,table in enumerate( tables ):
        #
        version = versions[i]
        pname = 'figs/plot_nuc_setupBEExp_chart_lt_'+table+'_'+version+'.png'
        print(f'Plot name: {pname}')
        nuda.fig.nuc_setupBEExp_chart_lt_fig( pname, table, version, theo_tables )
        #
    #
    print(50*'-')
    print("Exit nuc_setupBEExp_chart_lt_plot.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
