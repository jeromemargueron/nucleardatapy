
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
#plt.rcParams.update({'font.size': 16})

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nudy

def main():
    #
    print(50*'-')
    print("Enter plot_SetupEsymLsym.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    # plot name:
    #
    pname = 'figs/plot_SetupEsymLsym.png'
    print(f'Plot name: {pname}')
    #
    # plot
    #
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=None, top=0.98, wspace=0.3, hspace=0.3)
    #
    axs.set_xlabel(r'$E_{\mathrm{sym},2}$ (MeV)')
    axs.set_ylabel(r'$L_{\mathrm{sym},2}$ (MeV)')
    axs.set_xlim([22, 44])
    axs.set_ylim([10, 120])
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
    #constraints = [ '2009-HIC', '2010-RNP', '2012-FRDM', '2013-NS', '2014-IAS', '2014-IAS+RNP', \
    #         '2015-POL-208PB', '2015-POL-120SN', '2015-POL-68NI', '2017-UG', \
    #          '2021-PREXII-Reed', '2021-PREXII-Reinhard', '2021-PREXII-Zhang' ]
    #constraints = [ '2009-HIC', '2010-RNP', '2012-FRDM', '2014-IAS', '2014-IAS+RNP' ]
    constraints, constraints_lower = nudy.constraints_EsymLsym()
    #
    for constraint in constraints:
        #
        #print('constraint:',key)
        el = nudy.SetupEsymLsym( constraint = constraint )
        print('Esym:',el.Esym,'+-',el.Esym_err)
        print('Lsym:',el.Lsym,'+-',el.Lsym_err)
        print('len(Esym):',el.Esym.size)
        if el.Esym.size==1 and el.Esym_err.size==1 and el.Lsym_err.size==1: 
            axs.errorbar( el.Esym, el.Lsym, xerr=el.Esym_err, yerr=el.Lsym_err, linestyle='solid', label=el.label )
        elif any(el.Esym) and any(el.Esym_err): 
            axs.errorbar( el.Esym, el.Lsym, xerr=el.Esym_err, linestyle='solid', label=el.label )
            #print('errorbar x')
        elif any(el.Esym) and any(el.Lsym_err): 
            axs.errorbar( el.Esym, el.Lsym, yerr=el.Lsym_err, linestyle='solid', label=el.label )
            #print('errorbar y')
        elif any(el.Esym): 
            axs.plot( el.Esym, el.Lsym, linestyle='solid', label=el.label )
            #print('plot')
        el.print_outputs( )
    #
    axs.legend(loc='upper left',fontsize='xx-small')
    #
    plt.savefig(pname)
    plt.close()

    print(50*'-')
    print("Exit plot_SetupEsymLsym.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
