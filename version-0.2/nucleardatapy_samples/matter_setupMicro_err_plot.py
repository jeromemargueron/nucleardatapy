

import nucleardatapy as nuda


def main():
    #
    print(50*'-')
    print("Enter matter_setupMicro_err_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    nuda.create_folder_fig()
    #
    models = [ '2013-QMC-NM', '2016-MBPT-AM', '2016-QMC-NM', '2020-MBPT-AM', '2024-QMC-NM' ]
    #
    # plot errors in NM
    #
    pname = 'figs/plot_matter_setupMicro_err_NM.png'
    nuda.plot.matter_setupMicro_err_NM_fig( pname, models )
    #
    print(50*'-')
    print("Exit matter_setupMicro_err_plot.py:")
    print(50*'-')
    #

    
if __name__ == "__main__":
    main()

