
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
#plt.rcParams.update({'font.size': 16})

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plot_astro_masses( pname, sources ):
    #
    # plot Masses versus sources
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.98, wspace=0.3, hspace=0.3)
    #
    axs.set_ylabel(r'M (M$_\odot$)',fontsize='12')
    axs.set_xlim([0.8, 5.5])
    axs.set_ylim([1.4, 3.4])
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
        obss = nuda.astro_masses_source( source = source )
        print(f'source: {source}, obss: {obss}')
        #
        iobs = 0
        for obs in obss:
            m = nuda.SetupAstroMasses( source = source, obs = obs )
            m.print_output( )
            m.print_table( )
            axs.errorbar( isource+iobs/10, m.mass, yerr=np.array([(m.sig_do,m.sig_up)]).T, label=m.label, color=nuda.param.col[isource], marker='s', linestyle = 'solid', linewidth = 1 )
            iobs += 1
            #
        mav = nuda.SetupAstroMassesAverage( source = source )
        mav.print_output( )
        mav.print_table( )
        axs.errorbar( isource+iobs/10, mav.mass_cen, yerr=mav.sig_std, label=mav.label, color=nuda.param.col[isource], marker='o', linestyle = 'solid', linewidth = 3 )
        isource += 1
    #
    axs.set_xticks( ilabel )
    axs.set_xticklabels( xlabel )
    axs.legend(loc='upper left',fontsize='8', ncol=2)
    #
    plt.savefig(pname)
    plt.close()
    #

def main():
    #
    print(50*'-')
    print("Enter plot_SetupAstroMasses.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    sources = nuda.astro_masses( )[0]
    print('Complete list of available sources:',sources)
    #
    sources = [ 'J1614–2230', 'J0348+0432', 'J2215+5135', 'J1600+3053', 'J0740+6620' ]
    #
    print('sources considered:',sources)
    #
    pname = 'figs/plot_SetupAstroMasses.png'
    plot_astro_masses( pname, sources )
    #
    print(50*'-')
    print("Exit plot_SetupAstroMasses.py:")
    print(50*'-')
    #

if __name__ == "__main__":
    main()
