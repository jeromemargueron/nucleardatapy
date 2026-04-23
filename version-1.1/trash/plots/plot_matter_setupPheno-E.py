
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plot_matter_setupPheno_E( models, band, matter ):
    #
    for model in models:
        #
        # plot name:
        #
        pname = 'figs/plot_matter_setupPheno-'+model+'-E-'+matter+'.png'
        print(f'Plot name: {pname}')
        #
        # plot
        #
        fig, axs = plt.subplots(2,2)
        fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
        fig.subplots_adjust(left=0.15, bottom=0.12, right=None, top=0.88, wspace=0.05, hspace=0.05)
        #
        axs[0,0].set_xlim([0, 0.33])
        axs[1,0].set_xlabel(r'n (fm$^{-3}$)',fontsize='12')
        axs[1,0].set_xlim([0, 0.33])
        axs[0,1].set_xlim([0.5, 1.5])
        axs[1,1].set_xlabel(r'$k_F$ (fm$^{-1}$)',fontsize='12')
        axs[1,1].set_xlim([0.5, 1.5])
        #
        axs[0,0].tick_params('x', labelbottom=False)
        axs[0,1].tick_params('x', labelbottom=False)
        axs[0,1].tick_params('y', labelleft=False)
        axs[1,1].tick_params('y', labelleft=False)
        #
        if matter.lower() == 'nm':
            axs[0,0].set_ylabel(r'$E_{NM}/A$ (MeV)',fontsize='12')
            axs[0,0].set_ylim([0, 35])
            axs[0,1].set_ylim([0, 15])
            axs[1,0].set_ylabel(r'$E_{NM}/E_{FFG,NM}$',fontsize='12')
            axs[1,0].set_ylim([0.2, 0.84])
            axs[1,1].set_ylim([0.2, 0.84])
        elif matter.lower() == 'sm':
            axs[0,0].set_ylabel(r'$E_{SM}/A$ (MeV)',fontsize='12')
            axs[0,0].set_ylim([-20, 10])
            axs[0,1].set_ylim([-20, 10])
            axs[1,0].set_ylabel(r'$E_{SM}/E_{FFG,SM}$',fontsize='12')
            axs[1,0].set_ylim([-2.0, 0.1])
            axs[1,1].set_ylim([-2.0, 0.1])
        #
        params, params_lower = nuda.matter.pheno_params( model = model )
        #
        for param in params:
            #
            pheno = nuda.matter.setupPheno( model = model, param = param )
            if matter.lower() == 'nm':
                if any(pheno.nm_e2a): 
                    if model == 'Skyrme' and not nuda.matter.checkPheno(pheno,band,matter):
                        axs[0,0].plot( pheno.nm_den, pheno.nm_e2a, linestyle='solid' )
                    else:
                        axs[0,0].plot( pheno.nm_den, pheno.nm_e2a, linestyle='solid', label=pheno.label )
                        #print('model:',model,' param:',param,' inside band')
                    axs[0,1].plot( pheno.nm_kfn, pheno.nm_e2a, linestyle='solid' )
                    axs[1,0].plot( pheno.nm_den, pheno.nm_e2a/nuda.effg_nr(pheno.nm_kfn), linestyle='solid' )
                    axs[1,1].plot( pheno.nm_kfn, pheno.nm_e2a/nuda.effg_nr(pheno.nm_kfn), linestyle='solid' )
            elif matter.lower() == 'sm':
                if any(pheno.sm_e2a): 
                    if model == 'Skyrme' and not nuda.matter.checkPheno(pheno,band,matter):
                        axs[0,0].plot( pheno.sm_den, pheno.sm_e2a, linestyle='solid' )
                    else:
                        axs[0,0].plot( pheno.sm_den, pheno.sm_e2a, linestyle='solid', label=pheno.label )
                        #print('model:',model,' param:',param,' inside band')
                    #axs[0,0].plot( pheno.sm_den, pheno.sm_e2a, linestyle='solid', label=pheno.label )
                    axs[0,1].plot( pheno.sm_kf, pheno.sm_e2a, linestyle='solid' )
                    axs[1,0].plot( pheno.sm_den, pheno.sm_e2a/nuda.effg_nr(pheno.sm_kf), linestyle='solid' )
                    axs[1,1].plot( pheno.sm_kf, pheno.sm_e2a/nuda.effg_nr(pheno.sm_kf), linestyle='solid' )
            if nuda.env.verb_output: pheno.print_outputs( )
        if matter.lower() == 'nm':
            axs[0,0].fill_between( band.den, y1=(band.e2a-band.e2a_std), y2=(band.e2a+band.e2a_std), color=band.color, alpha=band.alpha )
            axs[0,0].plot( band.den, (band.e2a-band.e2a_std), color='k', linestyle='dashed' )
            axs[0,0].plot( band.den, (band.e2a+band.e2a_std), color='k', linestyle='dashed' )
            axs[0,1].fill_between( band.kfn, y1=(band.e2a-band.e2a_std), y2=(band.e2a+band.e2a_std), color=band.color, alpha=band.alpha )
            axs[0,1].plot( band.kfn, (band.e2a-band.e2a_std), color='k', linestyle='dashed' )
            axs[0,1].plot( band.kfn, (band.e2a+band.e2a_std), color='k', linestyle='dashed' )
            axs[1,0].fill_between( band.den, y1=(band.e2a-band.e2a_std)/nuda.effg_nr(band.kfn), y2=(band.e2a+band.e2a_std)/nuda.effg_nr(band.kfn), color=band.color, alpha=band.alpha )
            axs[1,0].plot( band.den, (band.e2a-band.e2a_std)/nuda.effg_nr(band.kfn), color='k', linestyle='dashed' )
            axs[1,0].plot( band.den, (band.e2a+band.e2a_std)/nuda.effg_nr(band.kfn), color='k', linestyle='dashed' )
            axs[1,1].fill_between( band.kfn, y1=(band.e2a-band.e2a_std)/nuda.effg_nr(band.kfn), y2=(band.e2a+band.e2a_std)/nuda.effg_nr(band.kfn), color=band.color, alpha=band.alpha )
            axs[1,1].plot( band.kfn, (band.e2a-band.e2a_std)/nuda.effg_nr(band.kfn), color='k', linestyle='dashed' )
            axs[1,1].plot( band.kfn, (band.e2a+band.e2a_std)/nuda.effg_nr(band.kfn), color='k', linestyle='dashed' )
        elif matter.lower() == 'sm':
            axs[0,0].fill_between( band.den, y1=(band.e2a-band.e2a_std), y2=(band.e2a+band.e2a_std), color=band.color, alpha=band.alpha, visible=True )
            axs[0,0].plot( band.den, (band.e2a-band.e2a_std), color='k', linestyle='dashed' )
            axs[0,0].plot( band.den, (band.e2a+band.e2a_std), color='k', linestyle='dashed' )
            axs[0,1].fill_between( band.kfn, y1=(band.e2a-band.e2a_std), y2=(band.e2a+band.e2a_std), color=band.color, alpha=band.alpha, visible=True )
            axs[0,1].plot( band.kfn, (band.e2a-band.e2a_std), color='k', linestyle='dashed' )
            axs[0,1].plot( band.kfn, (band.e2a+band.e2a_std), color='k', linestyle='dashed' )
            axs[1,0].fill_between( band.den, y1=(band.e2a-band.e2a_std)/nuda.effg_nr(band.kfn), y2=(band.e2a+band.e2a_std)/nuda.effg_nr(band.kfn), color=band.color, alpha=band.alpha, visible=True )
            axs[1,0].plot( band.den, (band.e2a-band.e2a_std)/nuda.effg_nr(band.kfn), color='k', linestyle='dashed' )
            axs[1,0].plot( band.den, (band.e2a+band.e2a_std)/nuda.effg_nr(band.kfn), color='k', linestyle='dashed' )
            axs[1,1].fill_between( band.kfn, y1=(band.e2a-band.e2a_std)/nuda.effg_nr(band.kfn), y2=(band.e2a+band.e2a_std)/nuda.effg_nr(band.kfn), color=band.color, alpha=band.alpha, visible=True )
            axs[1,1].plot( band.kfn, (band.e2a-band.e2a_std)/nuda.effg_nr(band.kfn), color='k', linestyle='dashed' )
            axs[1,1].plot( band.kfn, (band.e2a+band.e2a_std)/nuda.effg_nr(band.kfn), color='k', linestyle='dashed' )
        #
        #if model != 'Skyrme':
        #    axs[0,0].legend(loc='upper right',fontsize='8', ncol=2)
        fig.legend(loc='upper left',bbox_to_anchor=(0.1,1.0),columnspacing=2,fontsize='8',ncol=4,frameon=False)
        #
        #
        plt.savefig(pname, dpi=300)
        plt.close()
    #

def main():
    #
    print(50*'-')
    print("Enter plot_matter_setupPheno_E.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    # fix the uncertainty band
    #
    den = np.array([0.04,0.06,0.08,0.1,0.12,0.14,0.16])
    bmodels = [ '2016-MBPT-AM', '2016-QMC-NM', '2020-MBPT-AM' ]
    bandNM = nuda.matter.setupMicroBand( bmodels, den=den, matter='NM' )
    #
    bmodels = [ '2016-MBPT-AM', '2020-MBPT-AM' ]
    bandSM = nuda.matter.setupMicroBand( bmodels, den=den, matter='SM' )
    #
    # create the models for the figures
    #
    #models, models_lower = nuda.modelsPheno()
    models = [ 'Skyrme', 'ESkyrme', 'NLRH', 'DDRH', 'DDRHF' ]
    #
    # plot E/A in NM
    #
    matter='NM'
    plot_matter_setupPheno_E( models, bandNM, matter )
    #
    # plot E/A in SM
    #
    matter='SM'
    plot_matter_setupPheno_E( models, bandSM, matter )
    #
    print(50*'-')
    print("Exit plot_matter_setupPheno_E.py:")
    print(50*'-')
    #

if __name__ == "__main__":
    main()

