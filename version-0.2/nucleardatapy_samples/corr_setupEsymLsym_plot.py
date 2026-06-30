
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter corr_setupEsymLsym_fig.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    nuda.create_folder_fig()
    #
    #constraints = [ '2009-HIC', '2010-RNP', '2012-FRDM', '2013-NS', '2014-IAS', '2014-IAS+RNP', \
    #         '2015-POL-208PB', '2015-POL-120SN', '2015-POL-68NI', '2017-UG', \
    #          '2021-PREXII-Reed', '2021-PREXII-Reinhard', '2021-PREXII-Zhang' ]
    #constraints = [ '2009-HIC', '2010-RNP', '2012-FRDM', '2014-IAS', '2014-IAS+RNP' ]
    constraints, constraints_lower = nuda.corr.EsymLsym_constraints()
    #
    pname = 'figs/plot_corr_setupEsymLsym.png'
    nuda.fig.corr_setupEsymLsym_fig( pname, constraints )
    #
    print(50*'-')
    print("Exit corr_setupEsymLsym_fig.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
