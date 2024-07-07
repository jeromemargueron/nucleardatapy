import os
import sys
import numpy as np
import matplotlib.pyplot as plt

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plotMicro_band( pname, models ):
    #
    # plot e in NM
    #
    print(f'Plot name: {pname}')
    #
    #den = 0.03*np.arange(13)
    #
    fig, axs = plt.subplots(1,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.10, bottom=0.12, right=None, top=0.98, wspace=0.3, hspace=0.3 )
    #
    axs[0].set_xlabel(r'n (fm$^{-3}$)',fontsize='14')
    axs[0].set_ylabel(r'$E_{NM}$',fontsize='14')
    axs[0].set_xlim([0, 0.2])
    axs[0].set_ylim([0, 20])
    #
    axs[1].set_xlabel(r'n (fm$^{-3}$)',fontsize='14')
    axs[1].set_ylabel(r'$E_{NM}/E_{FFG}$',fontsize='14')
    axs[1].set_xlim([0, 0.2])
    axs[1].set_ylim([0.2, 0.9])
    #
    for model in models:
        #
        mic = nuda.SetupMicro( model = model )
        mic.print_outputs( )
        if mic.nm_e2a is not None: 
            print('model:',model)
            axs[0].errorbar( mic.nm_den, mic.nm_e2a, yerr= mic.nm_e2a_err, linestyle=mic.linestyle, label=mic.label, errorevery=mic.every )
            axs[1].errorbar( mic.nm_den, mic.nm_e2a/nuda.effg(mic.nm_kfn), yerr= mic.nm_e2a_err/nuda.effg(mic.nm_kfn), linestyle=mic.linestyle, label=mic.label, errorevery=mic.every )
    band = nuda.SetupMicroBand( models )
    axs[0].fill_between( band.nm_den, y1=band.nm_e2a-band.nm_e2a_std, y2=band.nm_e2a+band.nm_e2a_std, color=band.color, alpha=band.alpha )
    axs[1].fill_between( band.nm_den, y1=(band.nm_e2a-band.nm_e2a_std)/nuda.effg(band.nm_kfn), y2=(band.nm_e2a+band.nm_e2a_std)/nuda.effg(band.nm_kfn), color=band.color, alpha=band.alpha )
    #
    axs[1].legend(loc='upper left',fontsize='12', ncol=1)
    #
    plt.savefig(pname)
    plt.close()

def main():
    #
    print(50*'-')
    print("Enter plot_SetupMicroBand.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    models = [ '2016-MBPT-AM', '2016-QMC-NM', '2020-MBPT-AM' ]
    #
    # plot errors in NM
    #
    pname = 'figs/plot_SetupMicro_band_NM.png'
    plotMicro_band( pname, models )
    #
    print(50*'-')
    print("Exit plot_SetupMicroBand.py:")
    print(50*'-')
    #

    
if __name__ == "__main__":
    main()

