
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plotPheno_NM( models, band ):
    #
    #
    for model in models:
        #
        # plot name:
        #
        pname = 'figs/plot_SetupPheno-'+model+'-E-NM.png'
        print(f'Plot name: {pname}')
        #
        # plot
        #
        fig, axs = plt.subplots(2,2)
        fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
        fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.98, wspace=0.2, hspace=0.2)
        #
        axs[0,0].set_ylabel(r'$E_{NM}/E_{FFG}$',fontsize='12')
        axs[0,0].set_xlim([0, 0.3])
        axs[0,0].set_ylim([0, 1.0])
        #
        axs[1,0].set_xlabel(r'n (fm$^{-3}$)',fontsize='12')
        axs[1,0].set_ylabel(r'$E_{NM}/A$ (MeV)',fontsize='12')
        axs[1,0].set_xlim([0, 0.3])
        axs[1,0].set_ylim([0, 28])
        #
        #axs[0,1].set_ylabel(r'$\Delta/E_F$')
        axs[0,1].set_xlim([0.5, 3.0])
        axs[0,1].set_ylim([0, 1.0])
        #
        axs[1,1].set_xlabel(r'k_F (fm$^{-1}$)',fontsize='12')
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
            pheno = nuda.SetupPheno( model = model, param = param )
            if any(pheno.nm_e2a): 
                axs[0,0].plot( pheno.nm_den, pheno.nm_e2a/nuda.effg(pheno.nm_kfn), linestyle='solid', label=pheno.label )
                axs[1,0].plot( pheno.nm_den, pheno.nm_e2a, linestyle='solid', label=pheno.label )
                axs[0,1].plot( pheno.nm_kfn, pheno.nm_e2a/nuda.eF_n(pheno.nm_kfn), linestyle='solid', label=pheno.label )
                axs[1,1].plot( pheno.nm_kfn, pheno.nm_e2a, linestyle='solid', label=pheno.label )
            pheno.print_outputs( )
        axs[0,0].fill_between( band.nm_den, y1=(band.nm_e2a-band.nm_e2a_std)/nuda.effg(band.nm_kfn), y2=(band.nm_e2a+band.nm_e2a_std)/nuda.effg(band.nm_kfn), color=band.color, alpha=band.alpha )
        axs[1,0].fill_between( band.nm_den, y1=(band.nm_e2a-band.nm_e2a_std), y2=(band.nm_e2a+band.nm_e2a_std), color=band.color, alpha=band.alpha )
        axs[0,1].fill_between( band.nm_kfn, y1=(band.nm_e2a-band.nm_e2a_std)/nuda.eF_n(band.nm_kfn), y2=(band.nm_e2a+band.nm_e2a_std)/nuda.eF_n(band.nm_kfn), color=band.color, alpha=band.alpha )
        axs[1,1].fill_between( band.nm_kfn, y1=(band.nm_e2a-band.nm_e2a_std), y2=(band.nm_e2a+band.nm_e2a_std), color=band.color, alpha=band.alpha )        
        #
        axs[0,0].legend(loc='upper right',fontsize='8', ncol=2)
        #axs[0,1].legend(loc='upper left',fontsize='xx-small')
        #
        plt.savefig(pname)
        plt.close()
    #

def plotPheno_SM( models ):
    #
    for model in models:
        #
        # plot name:
        #
        pname = 'figs/plot_SetupPheno-'+model+'-E-SM.png'
        print(f'Plot name: {pname}')
        #
        # plot
        #
        fig, axs = plt.subplots(2,2)
        fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
        fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.98, wspace=0.2, hspace=0.2)
        #
        axs[0,0].set_ylabel(r'$E_{SM}/E_{FFG}$',fontsize='12')
        axs[0,0].set_xlim([0, 0.3])
        axs[0,0].set_ylim([-1.0, 0.5])
        #
        axs[1,0].set_xlabel(r'n (fm$^{-3}$)',fontsize='12')
        axs[1,0].set_ylabel(r'$E_{SM}/A$ (MeV)',fontsize='12')
        axs[1,0].set_xlim([0, 0.3])
        axs[1,0].set_ylim([-20, 20])
        #
        axs[0,1].set_xlim([0.5, 3.0])
        axs[0,1].set_ylim([-1.0, 0.5])
        #
        axs[1,1].set_xlabel(r'k_F (fm$^{-1}$)',fontsize='12')
        axs[1,1].set_xlim([0.5, 3.0])
        axs[1,1].set_ylim([-20, 20])
        #
        params, params_lower = nuda.params_pheno( model = model )
        #
        for param in params:
            #
            pheno = nuda.SetupPheno( model = model, param = param )
            if any(pheno.sm_e2a): 
                axs[0,0].plot( pheno.sm_den, pheno.sm_e2a/nuda.effg(pheno.sm_kfn), linestyle='solid', label=pheno.label )
                axs[1,0].plot( pheno.sm_den, pheno.sm_e2a, linestyle='solid', label=pheno.label )
                axs[0,1].plot( pheno.sm_kfn, pheno.sm_e2a/nuda.eF_n(pheno.sm_kfn), linestyle='solid', label=pheno.label )
                axs[1,1].plot( pheno.sm_kfn, pheno.sm_e2a, linestyle='solid', label=pheno.label )
            pheno.print_outputs( )
        #
        axs[0,0].legend(loc='upper right',fontsize='8', ncol=2)
        #axs[0,1].legend(loc='upper left',fontsize='xx-small')
        #
        plt.savefig(pname)
        plt.close()
    #

def main():
    #
    print(50*'-')
    print("Enter plot_SetupPheno-E.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    # fix the uncertainty band
    #
    bmodels = [ '2016-MBPT-AM', '2016-QMC-NM', '2020-MBPT-AM' ]
    #
    band = nuda.SetupMicroBand( bmodels )
    #
    # create the models for the figures
    #
    #models, models_lower = nuda.modelsPheno()
    models = [ 'Skyrme', 'NLRH', 'DDRH', 'DDRHF' ]
    #
    # plot E/A in NM
    #
    plotPheno_NM( models, band )
    #
    # plot E/A in SM
    #
    plotPheno_SM( models )
    #
    print(50*'-')
    print("Exit plot_SetupPheno-E.py:")
    print(50*'-')
    #

    
if __name__ == "__main__":
    main()

