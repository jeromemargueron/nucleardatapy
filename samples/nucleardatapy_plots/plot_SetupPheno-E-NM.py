
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter plot_SetupPheno.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    #models, models_lower = nuda.modelsPheno()
    models = [ 'Skyrme', 'NLRH', 'DDRH', 'DDRHF' ]
    #
    for model in models:
        #
        # plot name:
        #
        pname = 'figs/plot_SetupPheno-'+model+'-ENM.png'
        print(f'Plot name: {pname}')
        #
        # plot
        #
        fig, axs = plt.subplots(2,2)
        fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
        fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.98, wspace=0.2, hspace=0.2)
        #
        axs[0,0].set_ylabel(r'$E_{NM}/E_{FFG}$')
        axs[0,0].set_xlim([0, 0.3])
        axs[0,0].set_ylim([0, 1.0])
        #
        axs[1,0].set_xlabel(r'n (fm$^{-3}$)')
        axs[1,0].set_ylabel(r'$E_{NM}/A$ (MeV)')
        axs[1,0].set_xlim([0, 0.3])
        axs[1,0].set_ylim([0, 28])
        #
        #axs[0,1].set_ylabel(r'$\Delta/E_F$')
        axs[0,1].set_xlim([0.5, 3.0])
        axs[0,1].set_ylim([0, 1.0])
        #
        axs[1,1].set_xlabel(r'k_F (fm$^{-1}$)')
        #axs[1,1].set_ylabel(r'$\Delta$ (MeV)')
        axs[1,1].set_xlim([0.5, 3.0])
        axs[1,1].set_ylim([0, 28])
        #
        #keys = [ '1998-VAR-AM-APR', '2008-AFDMC-NM', '2008-QMC-NM-swave', '2008-QMC-NM-AV4', \
        #         '2009-dQMC-NM', '2010-NM-Hebeler', '2013-QMC-NM', '2014-AFQMC-NM', '2016-QMC-NM', \
        #         '2016-MBPT-AM', '2018-QMC-NM', '2020-MBPT-AM-DHSL59', '2020-MBPT-AM-DHSL69', \
        #         '2023-MBPT-AM' ]
        params, params_lower = nuda.params_pheno( model = model )
        #
        for param in params:
            #
            mic = nuda.SetupPheno( model = model, param = param )
            if any(mic.nm_e2a): 
                axs[0,0].plot( mic.nm_den, mic.nm_e2a/nuda.fermi_gas.effg(mic.nm_kfn), linestyle='solid', label=mic.label )
                axs[1,0].plot( mic.nm_den, mic.nm_e2a, linestyle='solid', label=mic.label )
                axs[0,1].plot( mic.nm_kfn, mic.nm_e2a/nuda.fermi_gas.ef(mic.nm_kfn), linestyle='solid', label=mic.label )
                axs[1,1].plot( mic.nm_kfn, mic.nm_e2a, linestyle='solid', label=mic.label )
            mic.print_outputs( )
        #
        axs[0,0].legend(loc='upper right',fontsize='xx-small')
        axs[0,1].legend(loc='upper left',fontsize='xx-small')
        #
        plt.savefig(pname)
        plt.close()

    print(50*'-')
    print("Exit plot_SetupPheno.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
