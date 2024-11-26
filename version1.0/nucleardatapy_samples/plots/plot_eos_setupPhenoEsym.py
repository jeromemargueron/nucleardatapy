
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plot_eos_setupPhenoEsym( pname, models ):
    #
    # plot symmetry energy
    #
    print(f'Plot name: {pname}')
    print('models:',models)
    #
    fig, axs = plt.subplots(2,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.98, wspace=0.2, hspace=0.2 )
    #
    axs[0,0].set_ylabel(r'$E_\mathrm{sym}$ (MeV)')
    axs[0,0].set_xlim([0, 0.5])
    axs[0,0].set_ylim([0, 80])
    #
    axs[0,1].set_xlim([0, 2.0])
    axs[0,1].set_ylim([0, 80])
    #
    axs[1,0].set_ylabel(r'$E_\mathrm{sym}/E_\mathrm{sym, FFG}$')
    axs[1,0].set_xlabel(r'n (fm$^{-3}$)')
    axs[1,0].set_xlim([0, 0.5])
    axs[1,0].set_ylim([1, 4])
    #
    axs[1,1].set_xlabel(r'$k_F$ (fm$^{-1}$)')
    axs[1,1].set_xlim([0, 2.0])
    axs[1,1].set_ylim([1, 4])
    #
    for model in models:
        #
        params, params_lower = nuda.eos.pheno_params( model = model )
        #
        for param in params:
            #
            print('in Sample: model, param',model,param)
            esym = nuda.eos.setupPhenoEsym( model = model, param = param )
            #pheno.print_outputs( )
            #
            print("esym:",esym.esym)
            print("den:",esym.den)
            if esym.esym is not None:
                print("esym_err:",esym.esym_err)
                if esym.esym_err is not None:
                    axs[0,0].errorbar( esym.den, esym.esym, yerr=esym.esym_err, marker=esym.marker, linestyle='none', label=esym.label )
                    axs[0,1].errorbar( esym.kf,  esym.esym, yerr=esym.esym_err, marker=esym.marker, linestyle='none', label=esym.label )
                    axs[1,0].errorbar( esym.den, esym.esym/nuda.esymffg(esym.kf), yerr=esym.esym_err/nuda.esymffg(esym.kf), marker=esym.marker, linestyle='none', label=esym.label )
                    axs[1,1].errorbar( esym.kf,  esym.esym/nuda.esymffg(esym.kf), yerr=esym.esym_err/nuda.esymffg(esym.kf), marker=esym.marker, linestyle='none', label=esym.label )
                else:
                    axs[0,0].plot( esym.den, esym.esym, marker=esym.marker, linestyle=esym.linestyle, label=esym.label )
                    axs[0,1].plot( esym.kf,  esym.esym, marker=esym.marker, linestyle=esym.linestyle, label=esym.label )
                    axs[1,0].plot( esym.den, esym.esym/nuda.esymffg(esym.kf), marker=esym.marker, linestyle=esym.linestyle, label=esym.label )
                    axs[1,1].plot( esym.kf,  esym.esym/nuda.esymffg(esym.kf), marker=esym.marker, linestyle=esym.linestyle, label=esym.label )
            #esym.print_outputs( )
    #
    axs[0,0].plot( esym.den, nuda.esymffg(esym.kf), linestyle='dashed' )
    axs[0,1].plot( esym.kf,  nuda.esymffg(esym.kf), linestyle='dashed' )
    axs[1,0].legend(loc='upper right',fontsize='8')
    #
    plt.savefig(pname)
    plt.close()

def main():
    #
    print(50*'-')
    print("Enter plot_eos_setupPhenoEsym.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    # 
    # ===============================
    # Neutron Matter (NM)
    # ===============================
    #
    # list the available models
    #
    models, models_lower = nuda.eos.pheno_esym_models()
    #
    # plot symmetry energy
    #
    pname = 'figs/plot_eos_setupPhenoEsym.png'
    #
    plot_eos_setupPhenoEsym( pname, models )
    #
    print(50*'-')
    print("Exit plot_eos_setupPhenoEsym.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
