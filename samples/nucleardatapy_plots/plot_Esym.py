
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plot_esym( pname, models_micro, models_pheno ):
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
        mic = nuda.SetupMicro( model = model )
        if mic.esym_e2a is not None: 
            print('model:',model)
            if mic.marker:
                if mic.err:
                    axs[0].errorbar( mic.esym_den, mic.esym_e2a, yerr=mic.nm_e2a_err, marker=mic.marker, linestyle=None, label=mic.label, errorevery=mic.every )
                else:
                    axs[0].plot( mic.esym_den, mic.esym_e2a, marker=mic.marker, linestyle=None, label=mic.label, markevery=mic.every )
            else:
                if mic.err:
                    axs[0].errorbar( mic.esym_den, mic.esym_e2a, yerr=mic.esym_e2a_err, marker=mic.marker, linestyle=mic.linestyle, label=mic.label, errorevery=mic.every )
                else:
                    axs[0].plot( mic.esym_den, mic.esym_e2a, marker=mic.marker, linestyle=mic.linestyle, label=mic.label, markevery=mic.every )
        mic.print_outputs( )
    axs[0].legend(loc='upper left',fontsize='8', ncol=2)
    #
    for model in models_pheno:
        #
        params, params_lower = nuda.params_pheno( model = model )
        #
        for param in params:
            #
            pheno = nuda.SetupPheno( model = model, param = param )
            if pheno.esym_e2a is not None: 
                print('model:',model,' param:',param)
                axs[1].plot( pheno.esym_den, pheno.esym_e2a, label=pheno.label )
            pheno.print_outputs( )
    axs[1].legend(loc='upper left',fontsize='8', ncol=2)
    #axs[0,1].legend(loc='upper left',fontsize='xx-small', ncol=2)
    #
    plt.savefig(pname)
    plt.close()

def main():
    #
    print(50*'-')
    print("Enter plot_Esym.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    # list the available models
    #
    models_micro, models_lower = nuda.models_micro()
    models_pheno = [ 'Skyrme', 'NLRH', 'DDRH', 'DDRHF' ]
    #
    # plot Esym
    #
    pname = 'figs/plot_Esym.png'
    plot_esym( pname, models_micro, models_pheno )
    #
    print(50*'-')
    print("Exit plot_Esym.py:")
    print(50*'-')
    #

    
if __name__ == "__main__":
    main()
