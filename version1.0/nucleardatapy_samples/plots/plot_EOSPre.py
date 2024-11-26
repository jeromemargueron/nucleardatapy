
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['font.family'] = 'serif'
plt.rcParams['mathtext.fontset'] = 'stixsans'
plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plot_EOSpre( pname, micro_models, pheno_models, band ):
    #
    # plot pre in NM
    #
    print(f'Plot name: {pname}')
    #
    fig, axs = plt.subplots(1,2, figsize=(8,8))
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.10, bottom=0.08, right=None, top=0.62, wspace=0.3, hspace=0.3 )
    #
    axs[0].set_xlabel(r'n (fm$^{-3}$)')
    axs[0].set_ylabel(r'$p_{NM}(n)$')
    axs[0].set_xlim([0, 0.3])
    axs[0].set_ylim([0, 20])
    #
    axs[1].set_xlabel(r'n (fm$^{-3}$)')
    axs[1].set_ylabel(r'$p_{NM}(n)$')
    axs[1].set_xlim([0, 0.3])
    axs[1].set_ylim([0, 20])
    #
    for model in micro_models:
        #
        mic = nuda.SetupEOSMicro( model = model )
        if mic.nm_pre is not None: 
            print('model:',model)
            if mic.marker:
                if mic.err:
                    axs[0].errorbar( mic.nm_den, mic.nm_pre, yerr=mic.nm_pre_err, marker=mic.marker, linestyle=None, label=mic.label, errorevery=mic.every )
                else:
                    axs[0].plot( mic.nm_den, mic.nm_pre, marker=mic.marker, linestyle=None, label=mic.label, markevery=mic.every )
            else:
                if mic.err:
                    axs[0].errorbar( mic.nm_den, mic.nm_pre, yerr=mic.nm_pre_err, marker=mic.marker, linestyle=mic.linestyle, label=mic.label, errorevery=mic.every )
                else:
                    axs[0].plot( mic.nm_den, mic.nm_pre, marker=mic.marker, linestyle=mic.linestyle, label=mic.label, markevery=mic.every )
        mic.print_outputs( )
    #axs[0].fill_between( band.den, y1=(band.pre-band.pre_std), y2=(band.pre+band.pre_std), color=band.color, alpha=band.alpha, visible=True )
    #axs[0].plot( band.den, (band.pre-band.pre_std), color='k', linestyle='dashed' )
    #axs[0].plot( band.den, (band.pre+band.pre_std), color='k', linestyle='dashed' )
    axs[0].set_title('microscopic models',fontsize='10')
    #axs[0].legend(loc='upper left',fontsize='8', ncol=3)
    #fig.legend(loc='upper center', fontsize='8', ncol=4, bbox_to_anchor=(0.5, 1.00), 
    #       columnspacing=0.5, frameon=False)    

    #
    for model in pheno_models:
        #
        params, params_lower = nuda.eos_pheno_params( model = model )
        #
        for param in params:
            #
            pheno = nuda.SetupEOSPheno( model = model, param = param )
            if pheno.nm_pre is not None: 
                print('model:',model,' param:',param)
                #pheno.label=None
                axs[1].plot( pheno.nm_den, pheno.nm_pre, label=pheno.label )
            pheno.print_outputs( )
    #axs[1].fill_between( band.den, y1=(band.e2a-band.e2a_std), y2=(band.e2a+band.e2a_std), color=band.color, alpha=band.alpha, visible=True )
    #axs[1].plot( band.den, (band.e2a-band.e2a_std), color='k', linestyle='dashed' )
    #axs[1].plot( band.den, (band.e2a+band.e2a_std), color='k', linestyle='dashed' )
    axs[1].set_title('phenomenological models',fontsize='10')
    fig.legend(loc='upper center', fontsize='8', ncol=6, bbox_to_anchor=(0.5, 1.00), 
           columnspacing=0.45, frameon=False) 
    #axs[1].legend(loc='upper left',fontsize='8', ncol=2)
    #axs[0,1].legend(loc='upper left',fontsize='xx-small', ncol=2)
    #
    plt.savefig(pname)
    plt.close()

def main():
    #
    print(50*'-')
    print("Enter plot_EOSPre.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    # fix the uncertainty band
    #
    den = np.array([0.04,0.06,0.08,0.1,0.12,0.14,0.16])
    models = [ '2016-MBPT-AM', '2020-MBPT-AM' ]
    band = nuda.SetupEOSMicroBand( models, den=den, matter='NM' )
    #
    # list the available models
    #
    micro_models, micro_models_lower = nuda.eos_micro_models()
    pheno_models = [ 'Skyrme', 'NLRH', 'DDRH', 'DDRHF' ]
    #
    # plot Esym
    #
    pname = 'figs/plot_EOSPre.png'
    plot_EOSpre( pname, micro_models, pheno_models, band )
    #
    print(50*'-')
    print("Exit plot_EOSPre.py:")
    print(50*'-')
    #

    
if __name__ == "__main__":
    main()
