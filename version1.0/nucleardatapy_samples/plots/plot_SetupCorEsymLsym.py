
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
#plt.rcParams.update({'font.size': 16})

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter plot_SetupCorEsymLsym.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    # plot name:
    #
    pname = 'figs/plot_SetupCorEsymLsym.png'
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
    axs.set_xlim([23, 44])
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
    constraints, constraints_lower = nuda.CorEsymLsym_constraints()
    #
    for constraint in constraints:
        #
        #print('constraint:',key)
        el = nuda.SetupCorEsymLsym( constraint = constraint )
        print('Esym:',el.Esym,'+-',el.Esym_err)
        print('Lsym:',el.Lsym,'+-',el.Lsym_err)
        print('len(Esym):',el.Esym.size)


        if el.plot == 'point_err_xy':
            axs.errorbar( el.Esym, el.Lsym, xerr=el.Esym_err, yerr=el.Lsym_err, linestyle='solid', label=el.label )
        elif el.plot == 'curve':
            axs.plot( el.Esym, el.Lsym, linestyle='solid', linewidth=3, label=el.label )
        elif el.plot == 'contour':
            axs.plot( el.Esym, el.Lsym, linestyle='solid', label=el.label )
        elif el.plot == 'band_y':
            axs.fill_between( el.Esym, y1=el.Lsym-el.Lsym_err, y2=el.Lsym+el.Lsym_err, label=el.label, alpha=el.alpha )
            #axs.errorbar( el.Esym, el.Lsym, xerr=el.Esym_err, linestyle='solid', label=el.label )
        elif el.plot == 'band_x':
            axs.fill_betweenx( el.Lsym, x1=el.Esym-el.Esym_err, x2=el.Esym+el.Esym_err, label=el.label, alpha=el.alpha )
            #axs.errorbar( el.Esym, el.Lsym, yerr=el.Lsym_err, linestyle='solid', label=el.label )
        el.print_outputs( )
    #
    axs.legend(loc='lower right',fontsize='8')
    #
    plt.savefig(pname)
    plt.close()

    print(50*'-')
    print("Exit plot_SetupCorEsymLsym.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
