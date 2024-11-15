
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
#plt.rcParams.update({'font.size': 16})

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plot_astro_mup( pname, sources ):
    #
    # plot
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.98, wspace=0.3, hspace=0.3)
    #
    #axs.set_xlabel(r'$n$ (fm$^{-3}$)',fontsize='12')
    axs.set_ylabel(r'M (M$_\odot$)',fontsize='12')
    axs.set_xlim([0.8, 3.5])
    axs.set_ylim([2.0, 3.8])
    #
    isource = 1
    xlabel = []
    ilabel = []
    for source in sources:
        xlabel.append( source )
        ilabel.append( isource )
        #
        # get mup associated to `source` and `hyp`
        #
        hyps = nuda.astro_mup_source( source = source )
        print('hyps:',hyps)
        #
        ihyp = 0
        for hyp in hyps:
            mup = nuda.SetupAstroMup( source = source, hyp = hyp )
            #mass.print_outputs( )
            #
            axs.errorbar( isource+ihyp/10, mup.mup, yerr=np.array([(mup.sig_do,mup.sig_up)]).T, label=mup.label, color=nuda.param.col[isource], marker='s', linestyle = 'solid', linewidth = 1 )
            #
            ihyp += 1
        avmup = nuda.SetupAstroMupAverage( source = source )
        #avmass.print_outputs( )
        axs.errorbar( isource+ihyp/10, avmup.mup_cen, yerr=avmup.sig_std, label=avmup.label, color=nuda.param.col[isource], marker='o', linestyle = 'solid', linewidth = 3 )
        #
        isource += 1
    #
    axs.set_xticks( ilabel )
    axs.set_xticklabels( xlabel )
    #
    axs.legend(loc='upper left',fontsize='8', ncol=2)
    #
    plt.savefig(pname)
    plt.close()
    #

def main():
    #
    print(50*'-')
    print("Enter plot_SetupAstroMup.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    sources = nuda.astro_mup( )[0]
    print('Complete list of available sources:',sources)
    #
    sources = [ 'GW170817', 'GW190814' ]
    #
    print('sources considered:',sources)
    #
    pname = 'figs/plot_SetupAstroMup.png'
    plot_astro_mup( pname, sources )
    #
    print(50*'-')
    print("Exit plot_SetupAstroMup.py:")
    print(50*'-')
    #

if __name__ == "__main__":
    main()
