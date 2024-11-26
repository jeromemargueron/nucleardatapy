
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter plot_eos_setupFFGNuc.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    # plot E/E_FFG in NM
    #
    pname = 'figs/plot_eos_setupFFGNuc.png'
    print(f'Plot name: {pname}')
    #
    den = 0.01+0.02*np.arange(20)
    delta0 = np.zeros(den.size)
    delta1 = np.ones(den.size)
    #
    fig, axs = plt.subplots(2,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.9, wspace=0.2, hspace=0.2 )
    #
    axs[0,0].set_ylabel(r'$e_{FFG}$')
    #axs[0,0].set_xlim([0, 0.3])
    #axs[0,0].set_ylim([0, 1.0])
    #
    axs[1,0].set_xlabel(r'n (fm$^{-3}$)')
    axs[1,0].set_ylabel(r'$p_{FFG}$ (MeV fm$^{-3}$)')
    #axs[1,0].set_xlim([0, 0.3])
    #axs[1,0].set_ylim([0, 28])
    #
    #axs[0,1].set_ylabel(r'$\Delta/E_F$')
    #axs[0,1].set_xlim([0, 0.65])
    #axs[0,1].set_ylim([0, 1.0])
    #
    axs[1,1].set_xlabel(r'k_F (fm$^{-1}$)')
    #axs[1,1].set_ylabel(r'$\Delta$ (MeV)')
    #axs[1,1].set_xlim([0, 0.65])
    #axs[1,1].set_ylim([0, 2.5])
    #
    ffg0 = nuda.eos.setupFFGNuc( den, delta0 )
    #print("den:",ffg0.den)
    #print("E/A:",ffg0.e2a)
    #print("E/A_int:",ffg0.e2a_int)
    #print("E/A_int_nr:",ffg0.e2a_int_nr)
    ffg1 = nuda.eos.setupFFGNuc( den, delta1 )
    if any(ffg0.e2a_int_nr): 
        axs[0,0].plot( ffg0.den, ffg0.e2a_int, linestyle='dotted', color=nuda.param.col[0], label=ffg0.label )
        axs[0,0].plot( ffg0.den, ffg0.e2a_int_nr, linestyle='solid', color=nuda.param.col[0], label=ffg0.label+' NR' )
        axs[1,0].plot( ffg0.den, ffg0.pre, linestyle='dotted', color=nuda.param.col[0] )
        axs[1,0].plot( ffg0.den, ffg0.pre_nr, linestyle='solid', color=nuda.param.col[0] )
        axs[0,1].plot( ffg0.kf_n, ffg0.e2a_int, linestyle='dotted', color=nuda.param.col[0] )
        axs[0,1].plot( ffg0.kf_n, ffg0.e2a_int_nr, linestyle='solid', color=nuda.param.col[0] )
        axs[1,1].plot( ffg0.kf_n, ffg0.pre, linestyle='dotted', color=nuda.param.col[0] )
        axs[1,1].plot( ffg0.kf_n, ffg0.pre_nr, linestyle='solid', color=nuda.param.col[0] )
    if nuda.env.verb_output: ffg0.print_outputs( )
    if any(ffg1.e2a_int_nr): 
        axs[0,0].plot( ffg1.den, ffg1.e2a_int, linestyle='dotted', color=nuda.param.col[1], label=ffg1.label )
        axs[0,0].plot( ffg1.den, ffg1.e2a_int_nr, linestyle='dashed', color=nuda.param.col[1], label=ffg1.label+' NR' )
        axs[1,0].plot( ffg1.den, ffg1.pre, linestyle='dotted', color=nuda.param.col[1] )
        axs[1,0].plot( ffg1.den, ffg1.pre_nr, linestyle='dashed', color=nuda.param.col[1] )
        axs[0,1].plot( ffg1.kf_n, ffg1.e2a_int, linestyle='dotted', color=nuda.param.col[1] )
        axs[0,1].plot( ffg1.kf_n, ffg1.e2a_int_nr, linestyle='dashed', color=nuda.param.col[1] )
        axs[1,1].plot( ffg1.kf_n, ffg1.pre, linestyle='dotted', color=nuda.param.col[1] )
        axs[1,1].plot( ffg1.kf_n, ffg1.pre_nr, linestyle='dashed', color=nuda.param.col[1] )
    if nuda.env.verb_output: ffg1.print_outputs( )
    #
    #axs[1,0].legend(loc='upper right',fontsize='xx-small')
    fig.legend(loc='upper left',bbox_to_anchor=(0.2,0.97),fontsize='6',ncol=4,frameon=False)
    #
    plt.savefig(pname)
    plt.close()
    #
    print(50*'-')
    print("Exit plot_eos_setupFFGNuc.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
