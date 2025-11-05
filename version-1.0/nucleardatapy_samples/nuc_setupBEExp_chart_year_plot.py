
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter nuc_setupBEExp_chart_year_plot.py:")
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
    # loop over the tables
    #
    for i,table in enumerate( tables ):
        #
        version = versions[i]
        years = range(1880,2060,20)
        print('years[0]:',years[0])
        print('years[1]:',years[1])
        print('len(years):',len(years))
        for ind,year in enumerate(years):
            #
            if ind >= len(years)-1:
                break
            year_min=years[ind]
            year_max=years[ind+1]-1
            print('year:',year,ind)
            pname = folder+'/plot_nuc_setupBEExp_chart_year_'+table+'_'+version+'_y'+str(year)+'.png'
            print(f'Plot name: {pname}')
            #
            # year selection
            #
            mas = nuda.nuc.setupBEExp( table = table, version = version )
            sYear = mas.select_year( year_min=year_min, year_max=year_max, state = 'gs' )
            #
            nuda.fig.nuc_setupBEExp_chart_year_fig( pname, sYear, year_min, year_max )
            #
        #
    #
    print(50*'-')
    print("Exit nuc_setupBEExp_chart_year_plot.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
