import os
import sys
import numpy as np
import matplotlib.pyplot as plt

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plot_matter_setupMicroBand( pname, models, den, matter ):
    #
    # plot e in NM
    #
    print(f'Plot name: {pname}')
    #
    #den = 0.03*np.arange(13)
    #
    fig, axs = plt.subplots(1,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.15, bottom=0.12, right=None, top=0.98, wspace=0.38, hspace=0.3 )
    #
    axs[0].set_xlabel(r'n (fm$^{-3}$)',fontsize='14')
    axs[0].set_xlim([0, 0.2])
    #
    axs[1].set_xlabel(r'n (fm$^{-3}$)',fontsize='14')
    axs[1].set_xlim([0, 0.2])
    #
    if matter.lower() == 'nm':
        axs[0].set_ylabel(r'$E_{NM}$',fontsize='14')
        axs[1].set_ylabel(r'$E_{NM}/E_{NM,FFG}$',fontsize='14')
        axs[0].set_ylim([0, 20])
        axs[1].set_ylim([0.2, 0.9])
    elif matter.lower() == 'sm':
        axs[0].set_ylabel(r'$E_{SM}$',fontsize='14')
        axs[1].set_ylabel(r'$E_{SM}/E_{SM,FFG}$',fontsize='14')
        axs[0].set_ylim([-20, 0])
        axs[1].set_ylim([-1.0, 0.0])
    elif matter.lower() == 'esym':
        axs[0].set_ylabel(r'$E_{sym}$',fontsize='14')
        axs[1].set_ylabel(r'$E_{sym}/E_{sym,FFG}$',fontsize='14')
        axs[0].set_ylim([0, 50])
        axs[1].set_ylim([1.5, 2.8])
    #
    for model in models:
        #
        mic = nuda.matter.setupMicro( model = model )
        if nuda.env.verb_output: mic.print_outputs( )
        if mic.nm_e2a is not None: 
            print('model:',model)
            if matter.lower() == 'nm':
                axs[0].errorbar( mic.nm_den, mic.nm_e2a, yerr= mic.nm_e2a_err, linestyle=mic.linestyle, label=mic.label, errorevery=mic.every )
                axs[1].errorbar( mic.nm_den, mic.nm_e2a/nuda.effg_nr(mic.nm_kfn), yerr= mic.nm_e2a_err/nuda.effg_nr(mic.nm_kfn), linestyle=mic.linestyle, label=mic.label, errorevery=mic.every )
            elif matter.lower() == 'sm':
                axs[0].errorbar( mic.sm_den, mic.sm_e2a, yerr= mic.sm_e2a_err, linestyle=mic.linestyle, label=mic.label, errorevery=mic.every )
                axs[1].errorbar( mic.sm_den, mic.sm_e2a/nuda.effg_nr(mic.sm_kfn), yerr= mic.sm_e2a_err/nuda.effg_nr(mic.sm_kfn), linestyle=mic.linestyle, label=mic.label, errorevery=mic.every )
            elif matter.lower() == 'esym':
                esym = nuda.matter.setupMicroEsym( model = model )
                axs[0].errorbar( esym.den, esym.esym, yerr= esym.esym_err, linestyle=esym.linestyle, label=esym.label, errorevery=esym.every )
                axs[1].errorbar( esym.den, esym.esym/nuda.esymffg_nr(esym.kf), yerr= esym.esym_err/nuda.esymffg_nr(esym.kf), linestyle=esym.linestyle, label=esym.label, errorevery=esym.every )
    #
    band = nuda.matter.setupMicroBand( models, den=den, matter=matter )
    #
    axs[0].fill_between( band.den, y1=band.e2a-band.e2a_std, y2=band.e2a+band.e2a_std, color=band.color, alpha=band.alpha )
    if matter.lower() == 'nm':
        axs[1].fill_between( band.den, y1=(band.e2a-band.e2a_std)/nuda.effg_nr(band.kfn), y2=(band.e2a+band.e2a_std)/nuda.effg_nr(band.kfn), color=band.color, alpha=band.alpha )
    elif matter.lower() == 'sm':
        axs[1].fill_between( band.den, y1=(band.e2a-band.e2a_std)/nuda.effg_nr(band.kf), y2=(band.e2a+band.e2a_std)/nuda.effg_nr(band.kf), color=band.color, alpha=band.alpha )
    elif matter.lower() == 'esym':
        axs[1].fill_between( band.den, y1=(band.e2a-band.e2a_std)/nuda.esymffg_nr(band.kf), y2=(band.e2a+band.e2a_std)/nuda.esymffg_nr(band.kf), color=band.color, alpha=band.alpha )
    #
    if matter.lower() == 'nm':
        axs[1].legend(loc='upper left',fontsize='12', ncol=1)
    elif matter.lower() == 'sm':
        axs[1].legend(loc='upper left',fontsize='12', ncol=1)
    elif matter.lower() == 'esym':
        axs[0].legend(loc='upper left',fontsize='12', ncol=1)
    #
    plt.savefig(pname, dpi=200)
    plt.close()

def main():
    #
    print(50*'-')
    print("Enter plot_matter_setupMicroBand.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    # plot E/A + band for NM
    #
    den = np.array([0.04,0.06,0.08,0.1,0.12,0.14,0.16])
    models = [ '2016-MBPT-AM', '2016-QMC-NM', '2020-MBPT-AM' ]
    pname = 'figs/plot_matter_setupMicroBand_NM.png'
    plot_matter_setupMicroBand( pname, models, den=den, matter='NM' )
    #
    # plot E/A + band for SM
    #
    models = [ '2016-MBPT-AM', '2020-MBPT-AM' ]
    pname = 'figs/plot_matter_setupMicroBand_SM.png'
    plot_matter_setupMicroBand( pname, models, den=den, matter='SM' )
    #
    # plot Esym + band for SM
    #
    models = [ '2016-MBPT-AM', '2020-MBPT-AM' ]
    pname = 'figs/plot_matter_setupMicroBand_Esym.png'
    plot_matter_setupMicroBand( pname, models, den=den, matter='ESYM' )
    #
    print(50*'-')
    print("Exit plot_matter_setupMicroBand.py:")
    print(50*'-')
    #

    
if __name__ == "__main__":
    main()

