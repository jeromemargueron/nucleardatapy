import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter matter_setupMicro_band_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    nuda.create_folder_fig()
    #
    # plot E/A + band for NM
    #
    den = np.array([0.06,0.08,0.1,0.12,0.14,0.16])
    models = [ '2016-MBPT-AM', '2016-QMC-NM', '2020-MBPT-AM' ]
    pname = 'figs/plot_matter_setupMicroBand_NM.png'
    nuda.fig.matter_setupMicro_band_fig( pname, models, den=den, matter='NM' )
    #
    # plot E/A + band for SM
    #
    models = [ '2016-MBPT-AM', '2020-MBPT-AM' ]
    pname = 'figs/plot_matter_setupMicroBand_SM.png'
    nuda.fig.matter_setupMicro_band_fig( pname, models, den=den, matter='SM' )
    #
    # plot Esym + band for SM
    #
    models = [ '2016-MBPT-AM', '2020-MBPT-AM' ]
    pname = 'figs/plot_matter_setupMicroBand_Esym.png'
    nuda.fig.matter_setupMicro_band_fig( pname, models, den=den, matter='ESYM' )
    #
    print(50*'-')
    print("Exit matter_setupMicro_band_plot.py:")
    print(50*'-')
    #

if __name__ == "__main__":
    main()

