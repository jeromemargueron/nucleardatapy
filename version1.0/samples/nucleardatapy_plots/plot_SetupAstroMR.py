
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
#plt.rcParams.update({'font.size': 16})

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plot_astro_mr( pname, sources ):
    #
    # plot
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.98, wspace=0.3, hspace=0.3)
    #
    axs.set_xlabel(r'$R$ (km)',fontsize='12')
    axs.set_ylabel(r'M (M$_\odot$)',fontsize='12')
    #axs.set_xlim([0.8, 5.5])
    #axs.set_ylim([1.4, 3.4])
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
        obss = nuda.astro_mr_source( source = source )
        print('obss:',obss)
        #
        iobs = 0
        for obs in obss:
            mr = nuda.SetupAstroMR( source = source, obs = obs )
            #mass.print_outputs( )
            #
            axs.errorbar( mr.rad, mr.mass, yerr=np.array([(mr.mass_sig_do,mr.mass_sig_up)]).T, label=mr.label, color=nuda.param.col[isource], marker='s', linestyle = 'solid', linewidth = 1 )
            #axs.errorbar( isource+iobs/10, mass.mass, yerr=np.array([(mass.sig_low,mass.sig_low)]).T,  fmt='r^', linestyle = 'solid', linewidth = 1, alpha=0.6 )
            #
            iobs += 1
        #avmass = nuda.SetupAstroMRAverage( source = source )
        #avmass.print_outputs( )
        #axs.errorbar( isource+iobs/10, avmass.mass_cen, yerr=avmass.sig_std, label=avmass.label, color=nuda.param.col[isource], marker='o', linestyle = 'solid', linewidth = 3 )
        #
        isource += 1
    #
    #axs.set_xticks( ilabel )
    #axs.set_xticklabels( xlabel )
    #axs.text(0.15,12,r'$K_{sym}$='+str(int(Ksym))+' MeV',fontsize='12')
    axs.legend(loc='upper left',fontsize='8', ncol=2)
    #
    plt.savefig(pname)
    plt.close()
    #

def main():
    #
    print(50*'-')
    print("Enter plot_SetupAstroMR.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    sources = nuda.astro_mr( )[0]
    print('Complete list of available sources:',sources)
    #
    sources = [ 'J0030+0451', 'J0740+6620' ]
    #
    print('sources considered:',sources)
    #
    pname = 'figs/plot_SetupAstroMR.png'
    plot_astro_mr( pname, sources )
    #
    print(50*'-')
    print("Exit plot_SetupAstroMR.py:")
    print(50*'-')
    #

if __name__ == "__main__":
    main()
