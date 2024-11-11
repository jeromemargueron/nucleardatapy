
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
#plt.rcParams.update({'font.size': 16})

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plot_astro_gw( pname, sources ):
    #
    # plot
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.98, wspace=0.3, hspace=0.3)
    #
    #axs.set_xlabel(r'$n$ (fm$^{-3}$)',fontsize='12')
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
        hyps = nuda.astro_gw_source( source = source )
        print('obss:',hyps)
        #
        ihyp = 0
        for hyp in hyps:
            gw = nuda.SetupAstroGW( source = source, hyp = hyp )
            #gw.print_outputs( )
            #
            axs.errorbar( isource+ihyp/10, gw.lam, yerr=np.array([(gw.lam_sig_do,gw.lam_sig_up)]).T, label=gw.label, color=nuda.param.col[isource], marker='s', linestyle = 'solid', linewidth = 1 )
            #axs.errorbar( isource+iobs/10, mass.mass, yerr=np.array([(mass.sig_low,mass.sig_low)]).T,  fmt='r^', linestyle = 'solid', linewidth = 1, alpha=0.6 )
            #
            ihyp += 1
        avgw = nuda.SetupAstroGWAverage( source = source )
        avgw.print_outputs( )
        axs.errorbar( isource+ihyp/10, avgw.lam_cen, yerr=avgw.lam_sig_std, label=avgw.label, color=nuda.param.col[isource], marker='o', linestyle = 'solid', linewidth = 3 )
        #
        isource += 1
    #
    axs.set_xticks( ilabel )
    axs.set_xticklabels( xlabel )
    #axs.text(0.15,12,r'$K_{sym}$='+str(int(Ksym))+' MeV',fontsize='12')
    axs.legend(loc='upper left',fontsize='8', ncol=2)
    #
    plt.savefig(pname)
    plt.close()
    #

def main():
    #
    print(50*'-')
    print("Enter plot_SetupAstroGW.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    sources = nuda.astro_gw( )[0]
    print('Complete list of available sources:',sources)
    #
    sources = [ 'GW170817', 'GW190425' ]
    #
    print('sources considered:',sources)
    #
    pname = 'figs/plot_SetupAstroGW.png'
    plot_astro_gw( pname, sources )
    #
    print(50*'-')
    print("Exit plot_SetupAstroGW.py:")
    print(50*'-')
    #

if __name__ == "__main__":
    main()
