
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
#plt.rcParams.update({'font.size': 16})

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plot_astro_setupMR( pname, sources ):
    #
    # plot Mass versus Radius
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.98, wspace=0.3, hspace=0.3)
    #
    axs.set_xlabel(r'$R$ (km)',fontsize='12')
    axs.set_ylabel(r'M (M$_\odot$)',fontsize='12')
    axs.set_xlim([10, 17])
    axs.set_ylim([0.8, 2.6])
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
        obss = nuda.astro.mr_obss( source = source )
        print(f'source: {source}, obss: {obss}')
        #
        iobs = 0
        for obs in obss:
            mr = nuda.astro.setupMR( source = source, obs = obs )
            if nuda.env.verb_output: mr.print_output( )
            if nuda.env.verb_table: mr.print_table( )
            axs.errorbar( mr.rad, mr.mass, xerr=np.array([(mr.rad_sig_do,mr.rad_sig_up)]).T, yerr=np.array([(mr.mass_sig_do,mr.mass_sig_up)]).T, label=mr.label, color=nuda.param.col[isource], marker=mr.marker, linestyle = 'solid', linewidth = 1 )
            iobs += 1
            #
        mrav = nuda.astro.setupMRAverage( source = source )
        if nuda.env.verb_output: mrav.print_output( )
        if nuda.env.verb_table: mrav.print_table( )
        axs.errorbar( mrav.rad_cen, mrav.mass_cen, xerr=mrav.rad_sig_std, yerr=mrav.mass_sig_std, ms=12, label=mrav.label, color=nuda.param.col[isource], marker='^', linestyle = 'solid', linewidth = 3 )
        isource += 1
    #
    axs.legend(loc='upper left',fontsize='8', ncol=2)
    #
    plt.savefig(pname)
    plt.close()
    #

def main():
    #
    print(50*'-')
    print("Enter plot_astro_setupMR.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    sources = nuda.astro.mr_sources( )[0]
    print('Complete list of available sources:',sources)
    #
    sources = [ 'J0030+0451', 'J0740+6620' ]
    #
    print('sources considered:',sources)
    #
    pname = 'figs/plot_astro_setupMR.png'
    plot_astro_setupMR( pname, sources )
    #
    print(50*'-')
    print("Exit plot_astro_setupMR.py:")
    print(50*'-')
    #

if __name__ == "__main__":
    main()
