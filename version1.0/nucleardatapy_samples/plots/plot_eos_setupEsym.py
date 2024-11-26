
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
#plt.rcParams.update({'font.size': 16})

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plot_eos_setupEsym( pname, constraints, Ksym ):
    #
    # plot
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.98, wspace=0.3, hspace=0.3)
    #
    axs.set_xlabel(r'$n$ (fm$^{-3}$)',fontsize='12')
    axs.set_ylabel(r'$E_{\mathrm{sym}}$ (MeV)',fontsize='12')
    axs.set_xlim([0.09, 0.27])
    axs.set_ylim([10, 60])
    #
    for constraint in constraints:
        #
        esym = nuda.eos.setupEsym( constraint = constraint , Ksym=Ksym )
        #
        print('Den:',esym.esym_den)
        print('Esym_max:',esym.esym_e2a_max)
        print('Esym_min:',esym.esym_e2a_min)
        #
        if esym.plot:
            axs.fill_between( esym.esym_den, y1=esym.esym_e2a_min, y2=esym.esym_e2a_max, label=esym.label, alpha=esym.alpha )
    #
    axs.text(0.15,12,r'$K_{sym}$='+str(int(Ksym))+' MeV',fontsize='12')
    axs.legend(loc='lower right',fontsize='8')
    #
    plt.savefig(pname)
    plt.close()
    #

def main():
    #
    print(50*'-')
    print("Enter plot_eos_setupEsymDen.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    constraints, constraints_lower = nuda.corr.EsymLsym_constraints()
    #constraints = [ '2014-IAS' ]
    #
    Ksyms = [ -200.0, 0.0, 200 ]
    #
    for Ksym in Ksyms:
        #
        pname = 'figs/plot_eos_setupEsym_'+str(int(Ksym))+'.png'
        #
        plot_eos_setupEsym( pname, constraints, Ksym )
    #
    print(50*'-')
    print("Exit plot_eos_setupEsym.py:")
    print(50*'-')
    #

if __name__ == "__main__":
    main()
