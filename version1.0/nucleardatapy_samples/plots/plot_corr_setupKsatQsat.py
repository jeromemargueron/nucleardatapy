
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
#plt.rcParams.update({'font.size': 16})

import nucleardatapy as nuda

def plot_corr_setupKsatQsat( pname, constraints ):
    #
    # plot name:
    #
    print(f'Plot name: {pname}')
    #
    # plot
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.15, bottom=0.12, right=None, top=0.98, wspace=0.3, hspace=0.3)
    #
    axs.set_xlabel(r'$K_\mathrm{sat}$ (MeV)')
    axs.set_ylabel(r'$Q_\mathrm{sat}$ (MeV)')
    axs.set_xlim([190, 360])
    axs.set_ylim([-1000, 1500])
    #axs.tick_params(labelbottom=True, labeltop=False, labelleft=True, labelright=False,
    #                 bottom=True, top=True, left=True, right=True)
#    axs.xaxis.set_major_locator(MultipleLocator(5))
    #axs.xaxis.set_major_formatter(FormatStrFormatter('%d'))
#    axs.xaxis.set_minor_locator(MultipleLocator(1))
#    axs.yaxis.set_major_locator(MultipleLocator(20))
#    axs.yaxis.set_minor_locator(MultipleLocator(5))
#    axs.tick_params(axis = 'both', which='major', length=10, width=1, direction='inout', right = True, left = True, bottom = True, top = True)
#    axs.tick_params(axis = 'both', which='minor', length=5,  width=1, direction='in', right = True, left = True, bottom = True, top = True )
    #
    for constraint in constraints:
        #
        print('constraint:',constraint)
        kq = nuda.corr.setupKsatQsat( constraint = constraint )
        if nuda.env.verb: print('Ksat:',kq.Ksat)
        if nuda.env.verb: print('Qsat:',kq.Qsat)
        if nuda.env.verb: print('len(Ksat):',kq.Ksat.size)
        #
        axs.scatter( kq.Ksat, kq.Qsat, label=kq.label )
        axs.plot( kq.Ksat, nuda.corr.flinear(kq.Ksat,kq.m,kq.c) )
        #
        if nuda.env.verb: kq.print_outputs( )
    #
    axs.legend(loc='upper left',ncol=3, fontsize='9')
    #
    plt.savefig(pname)
    plt.close()

def main():
    #
    print(50*'-')
    print("Enter plot_corr_setupKsatQsat.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    #constraints = [ '2024-DFT-SKY', '2024-DFT-ESKY', '2024-DFT-DDRH', \
    #           '2024-DFT-NLRH', '2024-DFT-DDRHF', '2024-DFT-Gogny', \
    #           '2024-DFT-xEFT' ]
    constraints, constraints_lower = nuda.corr.KsatQsat_constraints()
    #
    pname = 'figs/plot_corr_setupKsatQsat.png'
    plot_corr_setupKsatQsat( pname, constraints )
    #
    print(50*'-')
    print("Exit plot_corr_setupKsatQsat.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
