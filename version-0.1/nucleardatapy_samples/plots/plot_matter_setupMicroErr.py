
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plot_matter_setupMicroErr( pname, models ):
    #
    # plot err/e in NM
    #
    print(f'Plot name: {pname}')
    #
    den = 0.03*np.arange(13)
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.98, wspace=0.2, hspace=0.2 )
    #
    axs.set_xlabel(r'n (fm$^{-3}$)',fontsize='12')
    axs.set_ylabel(r'$\Delta E_{NM}/E_{NM}$',fontsize='12')
    axs.set_xlim([0, 0.4])
    axs.set_ylim([0, 0.3])
    #
    for model in models:
        #
        mic = nuda.matter.setupMicro( model = model )
        if nuda.env.verb_output: mic.print_outputs( )
        if mic.nm_e2a is not None:
            print('model:',model)
            axs.plot( mic.nm_den, mic.nm_e2a_err/mic.nm_e2a, marker=mic.marker, markevery=mic.every, linestyle=mic.linestyle, label=mic.label )
    #axs.plot( den, nuda.matter.uncertainty_stat(den), linestyle='dashed', linewidth=3, label='fit (MBPT)' )
    axs.plot( den, nuda.matter.uncertainty_stat(den,err='MBPT'), linestyle='dashed', linewidth=3, label='fit (MBPT)' )
    axs.plot( den, nuda.matter.uncertainty_stat(den,err='QMC'),  linestyle='dashed', linewidth=3, label='fit (QMC)' )
    #
    axs.legend(loc='upper left',fontsize='12', ncol=3)
    #
    plt.savefig(pname, dpi=200)
    plt.close()

def main():
    #
    print(50*'-')
    print("Enter plot_matter_setupMicroErr.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    models = [ '2013-QMC-NM', '2016-MBPT-AM', '2016-QMC-NM', '2020-MBPT-AM', '2024-QMC-NM',]
    #
    # plot errors in NM
    #
    pname = 'figs/plot_matter_setupMicro_NM_err.png'
    plot_matter_setupMicroErr( pname, models )
    #
    print(50*'-')
    print("Exit plot_matter_setupMicroErr.py:")
    print(50*'-')
    #

    
if __name__ == "__main__":
    main()

