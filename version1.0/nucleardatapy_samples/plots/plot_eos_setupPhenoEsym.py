
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plot_eos_setupPhenoEsym( pname, models, band ):
    #
    # plot symmetry energy
    #
    print(f'Plot name: {pname}')
    print('models:',models)
    #
    fig, axs = plt.subplots(2,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.8, wspace=0.2, hspace=0.2 )
    #
    axs[0,0].set_ylabel(r'$E_\mathrm{sym}$ (MeV)')
    axs[0,0].set_xlim([0, 0.3])
    axs[0,0].set_ylim([0, 50])
    #
    axs[0,1].set_xlim([0.5, 2.0])
    axs[0,1].set_ylim([0, 50])
    #
    axs[1,0].set_ylabel(r'$E_\mathrm{sym}/E_\mathrm{sym, FFG}$')
    axs[1,0].set_xlabel(r'n (fm$^{-3}$)')
    axs[1,0].set_xlim([0, 0.3])
    axs[1,0].set_ylim([1, 4])
    #
    axs[1,1].set_xlabel(r'$k_F$ (fm$^{-1}$)')
    axs[1,1].set_xlim([0.5, 2.0])
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
            #
            #print("esym:",esym.esym)
            #print("den:",esym.den)
            if esym.esym is not None:
                print("esym_err:",esym.esym_err)
                if esym.esym_err is not None:
                    if not nuda.eos.checkPheno(esym,band,'Esym'):
                        axs[0,0].errorbar( esym.den, esym.esym, yerr=esym.esym_err, marker=esym.marker, linestyle='none', errorevery=esym.every )
                    else:
                        axs[0,0].errorbar( esym.den, esym.esym, yerr=esym.esym_err, marker=esym.marker, linestyle='none', errorevery=esym.every, label=esym.label )
                    axs[0,1].errorbar( esym.kf,  esym.esym, yerr=esym.esym_err, marker=esym.marker, linestyle='none', errorevery=esym.every )
                    axs[1,0].errorbar( esym.den, esym.esym/nuda.esymffg_nr(esym.kf), yerr=esym.esym_err/nuda.esymffg_nr(esym.kf), marker=esym.marker, linestyle='none', errorevery=esym.every )
                    axs[1,1].errorbar( esym.kf,  esym.esym/nuda.esymffg_nr(esym.kf), yerr=esym.esym_err/nuda.esymffg_nr(esym.kf), marker=esym.marker, linestyle='none', errorevery=esym.every )
                else:
                    if not nuda.eos.checkPheno(esym,band,'Esym'):
                        axs[0,0].plot( esym.den, esym.esym, marker=esym.marker, linestyle='dotted' )
                        axs[0,1].plot( esym.kf,  esym.esym, marker=esym.marker, linestyle='dotted' )
                        axs[1,0].plot( esym.den, esym.esym/nuda.esymffg_nr(esym.kf), marker=esym.marker, linestyle='dotted' )
                        axs[1,1].plot( esym.kf,  esym.esym/nuda.esymffg_nr(esym.kf), marker=esym.marker, linestyle='dotted' )
                    else:
                        axs[0,0].plot( esym.den, esym.esym, marker=esym.marker, linestyle=esym.linestyle, label=esym.label )
                        axs[0,1].plot( esym.kf,  esym.esym, marker=esym.marker, linestyle=esym.linestyle )
                        axs[1,0].plot( esym.den, esym.esym/nuda.esymffg_nr(esym.kf), marker=esym.marker, linestyle=esym.linestyle )
                        axs[1,1].plot( esym.kf,  esym.esym/nuda.esymffg_nr(esym.kf), marker=esym.marker, linestyle=esym.linestyle )
            if nuda.env.verb_output: esym.print_outputs( )
            #
        axs[0,0].fill_between( band.den, y1=(band.e2a-band.e2a_std), y2=(band.e2a+band.e2a_std), color=band.color, alpha=band.alpha, visible=True  )
        axs[0,0].plot( band.den, (band.e2a-band.e2a_std), color='k', linestyle='dashed', visible=True  )
        axs[0,0].plot( band.den, (band.e2a+band.e2a_std), color='k', linestyle='dashed', visible=True  )
        axs[0,1].fill_between( band.kfn, y1=(band.e2a-band.e2a_std), y2=(band.e2a+band.e2a_std), color=band.color, alpha=band.alpha, visible=True  )
        axs[0,1].plot( band.kfn, (band.e2a-band.e2a_std), color='k', linestyle='dashed', visible=True  )
        axs[0,1].plot( band.kfn, (band.e2a+band.e2a_std), color='k', linestyle='dashed', visible=True  )
        axs[1,0].fill_between( band.den, y1=(band.e2a-band.e2a_std)/nuda.esymffg_nr(band.kfn), y2=(band.e2a+band.e2a_std)/nuda.esymffg_nr(band.kfn), color=band.color, alpha=band.alpha, visible=True  )
        axs[1,0].plot( band.den, (band.e2a-band.e2a_std)/nuda.esymffg_nr(band.kfn), color='k', linestyle='dashed', visible=True  )
        axs[1,0].plot( band.den, (band.e2a+band.e2a_std)/nuda.esymffg_nr(band.kfn), color='k', linestyle='dashed', visible=True  )
        axs[1,1].fill_between( band.kf, y1=(band.e2a-band.e2a_std)/nuda.esymffg_nr(band.kfn), y2=(band.e2a+band.e2a_std)/nuda.esymffg_nr(band.kfn), color=band.color, alpha=band.alpha, visible=True  )
        axs[1,1].plot( band.kfn, (band.e2a-band.e2a_std)/nuda.esymffg_nr(band.kfn), color='k', linestyle='dashed', visible=True  )
        axs[1,1].plot( band.kfn, (band.e2a+band.e2a_std)/nuda.esymffg_nr(band.kfn), color='k', linestyle='dashed', visible=True  )

    #
    axs[0,0].plot( esym.den, nuda.esymffg_nr(esym.kf), linestyle='dashed' )
    axs[0,1].plot( esym.kf,  nuda.esymffg_nr(esym.kf), linestyle='dashed' )

    #axs[1,0].legend(loc='upper right',fontsize='8')
    fig.legend(loc='upper left',bbox_to_anchor=(0.1,1.0),columnspacing=2,fontsize='8',ncol=4,frameon=False)
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
    # 
    # ===============================
    # Symmetry Energy
    # ===============================
    #
    # Compute the band for Esym
    #
    den = np.array([0.04,0.06,0.08,0.1,0.12,0.14,0.16])
    bmodels = [ '2016-MBPT-AM', '2020-MBPT-AM' ]
    bandEsym = nuda.eos.setupMicroBand( bmodels, den=den, matter='ESYM' )
    #
    # list the available (phenomenological) models
    #
    models, models_lower = nuda.eos.pheno_esym_models()
    #
    # plot symmetry energy
    #
    pname = 'figs/plot_eos_setupPhenoEsym.png'
    #
    plot_eos_setupPhenoEsym( pname, models, bandEsym )
    #
    print(50*'-')
    print("Exit plot_eos_setupPhenoEsym.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
