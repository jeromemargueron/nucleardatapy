
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
#plt.rcParams.update({'font.size': 16})

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plot_astro_setupGW( pname, sources ):
    #
    # plot Lambda versus sources
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.14, bottom=0.07, right=None, top=0.8, wspace=0.3, hspace=0.3)
    #
    axs.set_ylabel(r'$\tilde{\Lambda}_{90\%}$',fontsize='12')
    axs.set_xlim([0.8, 2.5])
    axs.set_ylim([0, 1200])
    #
    isource = 1
    xlabel = []
    ilabel = []
    for source in sources:
        xlabel.append( source )
        ilabel.append( isource )
        #
        # get the mass associated to `source` and `obs`
        #
        hyps = nuda.astro.gw_hyps( source = source )
        print('obss:',hyps)
        #
        ihyp = 0
        for hyp in hyps:
            gw = nuda.astro.setupGW( source = source, hyp = hyp )
            if nuda.env.verb_output: gw.print_output( )
            if nuda.env.verb_table: gw.print_table( )
            axs.errorbar( isource+ihyp/10, gw.lam, yerr=np.array([(gw.lam_sig_do,gw.lam_sig_up)]).T, label=gw.label, color=nuda.param.col[isource], marker=gw.marker, linestyle = 'solid', linewidth = 1 )
            ihyp += 1
            #
        gwav = nuda.astro.setupGWAverage( source = source )
        if nuda.env.verb_output: gwav.print_output( )
        if nuda.env.verb_table: gwav.print_table( )
        axs.errorbar( isource+ihyp/10, gwav.lam_cen, yerr=gwav.lam_sig_std, ms=12, label=gwav.label, color=nuda.param.col[isource], marker='^', linestyle = 'solid', linewidth = 3 )
        #
        isource += 1
    #
    axs.set_xticks( ilabel )
    axs.set_xticklabels( xlabel )
    #axs.legend(loc='upper left',fontsize='8', ncol=2)
    #ax_right
    #ax_left
    #upper_right_display=ax_right.transAxes.transform((1,1))
    #upper_right_axes00=ax_left.transAxes.inverted().transform(upper_right_display)
    #axs.legend(loc='lower left',bbox_to_anchor=(0,1.02,upper_right_axes00[0],1),mode='expand',columnspacing=0,fontsize='8', ncol=2)
    axs.legend(loc='lower center',bbox_to_anchor=(0.5,1.01),columnspacing=2,fontsize='8', ncol=2,frameon=False)
    #
    plt.savefig(pname)
    plt.close()
    #

def main():
    #
    print(50*'-')
    print("Enter plot_astro_setupGW.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    sources = nuda.astro.gw_sources( )[0]
    print('Complete list of available sources:',sources)
    #
    sources = [ 'GW170817', 'GW190425' ]
    #
    print('sources considered:',sources)
    #
    pname = 'figs/plot_astro_setupGW.png'
    plot_astro_setupGW( pname, sources )
    #
    print(50*'-')
    print("Exit plot_astro_setupGW.py:")
    print(50*'-')
    #

if __name__ == "__main__":
    main()
