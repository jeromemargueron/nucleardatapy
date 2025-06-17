
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter corr_setupEsymDen_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    nuda.create_folder_fig()
    #
    constraints, constraints_lower = nuda.corr.EsymLsym_constraints()
    constraints.remove('2013-NS'); constraints.remove('2017-UG')
    constraints.remove('2023-EDF-D4'); constraints.remove('2023-EDF-D4-IAS'); constraints.remove('2023-EDF-D4-IAS-Rnp');
    constraints.remove('2015-POL-208Pb'); constraints.remove('2015-POL-120Sn'); constraints.remove('2015-POL-68Ni')
    #constraints = [ '2014-IAS' ]
    #
    Ksyms = [ -200.0, 0.0, 200 ]
    #
    for Ksym in Ksyms:
        #
        pname = 'figs/plot_corr_setupEsym2Den_'+str(int(Ksym))+'.png'
        #
        nuda.fig.corr_setupEsymDen_fig( pname, constraints, Ksym, origine='finiteNuclei' )
    #
    print(50*'-')
    print("Exit corr_setupEsymDen_plot.py:")
    print(50*'-')
    #

if __name__ == "__main__":
    main()
