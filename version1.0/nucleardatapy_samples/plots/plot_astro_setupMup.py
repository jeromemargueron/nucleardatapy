
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
#plt.rcParams.update({'font.size': 16})

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plot_astro_setupMup( pname, sources ):
    #
    # plot upper mass versus sources
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.8, wspace=0.3, hspace=0.3)
    #
    axs.set_ylabel(r'M (M$_\odot$)',fontsize='12')
    axs.set_xlim([0.8, 2.5])
    axs.set_ylim([2.4, 3.4])
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
        hyps = nuda.astro.mup_hyps( source = source )
        print('source:',source)
        print('hyps:',hyps)
        #
        ihyp = 0
        for hyp in hyps:
            mup = nuda.astro.setupMup( source = source, hyp = hyp )
            if nuda.env.verb_output: mup.print_output( )
            if nuda.env.verb_table: mup.print_table( )
            axs.errorbar( isource+ihyp/10, mup.mup, yerr=np.array([(mup.sig_do,mup.sig_up)]).T, label=mup.label, color=nuda.param.col[isource], marker=mup.marker, linestyle = 'solid', linewidth = 1 )
            ihyp += 1
            #
        if source=='GW170817': hyps = [ 3, 4 ]
        mupav = nuda.astro.setupMupAverage( source = source, hyps = hyps )
        if nuda.env.verb_output: mupav.print_output( )
        if nuda.env.verb_table: mupav.print_table( )
        axs.errorbar( isource+ihyp/10, mupav.mup_cen, yerr=mupav.sig_std, label=mupav.label, color=nuda.param.col[isource], marker='o', linestyle = 'solid', linewidth = 3 )
        #
        isource += 1
    #
    axs.set_xticks( ilabel )
    axs.set_xticklabels( xlabel )
    #
    #axs.legend(loc='upper left',fontsize='8', ncol=2)
    axs.legend(loc='lower center',bbox_to_anchor=(0.5,1.01),columnspacing=2,fontsize='8',ncol=2,frameon=False)
    #
    plt.savefig(pname, dpi=200)
    plt.close()
    #

def main():
    #
    print(50*'-')
    print("Enter plot_astro_setupMup.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    sources, sources_lower = nuda.astro.mup_sources( )
    print('Complete list of available sources:',sources)
    #
    sources = [ 'GW170817', 'GW190814' ]
    #
    print('sources considered:',sources)
    #
    pname = 'figs/plot_astro_setupMup.png'
    plot_astro_setupMup( pname, sources )
    #
    print(50*'-')
    print("Exit plot_astro_setupMup.py:")
    print(50*'-')
    #

if __name__ == "__main__":
    main()
