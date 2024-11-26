
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plot_EOSEsym( pname, models_micro, models_pheno, band ):
    #
    # plot E/A in NM
    #
    print(f'Plot name: {pname}')
    #
    fig, axs = plt.subplots(1,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.10, bottom=0.12, right=None, top=0.98, wspace=0.3, hspace=0.3 )
    #
    axs[0].set_xlabel(r'n (fm$^{-3}$)')
    axs[0].set_ylabel(r'$e_{sym}(n)$')
    axs[0].set_xlim([0, 0.3])
    axs[0].set_ylim([0, 60])
    #
    axs[1].set_xlabel(r'n (fm$^{-3}$)')
    axs[1].set_ylabel(r'$e_{sym}(n)$')
    axs[1].set_xlim([0, 0.3])
    axs[1].set_ylim([0, 60])
    #
    for model in models_micro:
        #
        esym = nuda.eos.setupMicroEsym( model = model )
        if esym.esym is not None: 
            print('model:',model)
            if esym.marker:
                if esym.err:
                    axs[0].errorbar( esym.den, esym.esym, yerr=esym.esym_err, marker=esym.marker, linestyle=None, label=esym.label, errorevery=esym.every )
                else:
                    axs[0].plot( esym.den, esym.esym, marker=esym.marker, linestyle=None, label=esym.label, markevery=esym.every )
            else:
                if esym.err:
                    axs[0].errorbar( esym.den, esym.esym, yerr=esym.esym_err, marker=esym.marker, linestyle=esym.linestyle, label=esym.label, errorevery=esym.every )
                else:
                    axs[0].plot( esym.den, esym.esym, marker=esym.marker, linestyle=esym.linestyle, label=esym.label, markevery=esym.every )
        if nuda.env.verb: esym.print_outputs( )
    axs[0].fill_between( band.den, y1=(band.e2a-band.e2a_std), y2=(band.e2a+band.e2a_std), color=band.color, alpha=band.alpha, visible=True )
    axs[0].plot( band.den, (band.e2a-band.e2a_std), color='k', linestyle='dashed' )
    axs[0].plot( band.den, (band.e2a+band.e2a_std), color='k', linestyle='dashed' )
    axs[0].text(0.05,5,'microscopic models',fontsize='10')
    axs[0].legend(loc='upper left',fontsize='8', ncol=3)
    #
    for model in models_pheno:
        #
        params, params_lower = nuda.eos.pheno_params( model = model )
        #
        for param in params:
            #
            esym = nuda.eos.setupPhenoEsym( model = model, param = param )
            if esym.esym is not None: 
                print('model:',model,' param:',param)
                #pheno.label=None
                axs[1].plot( esym.den, esym.esym, label=pheno.label )
            if nuda.env.verb: esym.print_outputs( )
    axs[1].fill_between( band.den, y1=(band.e2a-band.e2a_std), y2=(band.e2a+band.e2a_std), color=band.color, alpha=band.alpha, visible=True )
    axs[1].plot( band.den, (band.e2a-band.e2a_std), color='k', linestyle='dashed' )
    axs[1].plot( band.den, (band.e2a+band.e2a_std), color='k', linestyle='dashed' )
    axs[1].text(0.05,5,'phenomenological models',fontsize='10')
    #axs[1].legend(loc='upper left',fontsize='8', ncol=2)
    #axs[0,1].legend(loc='upper left',fontsize='xx-small', ncol=2)
    #
    plt.savefig(pname)
    plt.close()

def main():
    #
    print(50*'-')
    print("Enter plot_EOSEsym.py:")
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
    band = nuda.eos.setupMicroBand( models, den=den, matter='ESYM' )
    #
    # list the available models
    #
    micro_models, micro_models_lower = nuda.eos.micro_models()
    pheno_models = [ 'Skyrme', 'NLRH', 'DDRH', 'DDRHF' ]
    #
    # plot Esym
    #
    pname = 'figs/plot_EOSEsym.png'
    plot_EOSEsym( pname, micro_models, pheno_models, band )
    #
    print(50*'-')
    print("Exit plot_EOSEsym.py:")
    print(50*'-')
    #

    
if __name__ == "__main__":
    main()
