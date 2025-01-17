
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def plot_matter_NEP( pname, models ):
    #
    # plot sat in the left and sym on the right
    #
    print(f'Plot name: {pname}')
    #
    # Set figure
    #
    fig, axs = plt.subplots(5,2)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.10, bottom=0.12, right=None, top=0.98, wspace=0.3, hspace=0.3 )
    #
    axs[0,0].set_ylabel(r'$E_{sat}$')
    axs[1,0].set_ylabel(r'$n_{sat}$')
    axs[2,0].set_ylabel(r'$K_{sat}$')
    axs[3,0].set_ylabel(r'$Q_{sat}$')
    axs[4,0].set_ylabel(r'$m_{sat}^{*}$')
    axs[0,1].set_ylabel(r'$E_{sym}$')
    axs[1,1].set_ylabel(r'$L_{sym}$')
    axs[2,1].set_ylabel(r'$K_{sym}$')
    axs[3,1].set_ylabel(r'$Q_{sym}$')
    #
    # Built distribution of NEP
    #
    for model in models:
        #
        nsat = []; Esat = []; Ksat = []; Qsat = []; Zsat = []
        Esym = []; Lsym = []; Ksym = []; Qsym = []; Zsym = []
        msat = []; kappas = []; kappav = []
        params, params_lower = nuda.matter.nep_params( model = model )
        #
        for param in params:
            #
            print('param:',param)
            nep = nuda.matter.setupNEP( model = model, param = param )
            if nep.nep:
                nsat.append( nep.nsat ); Esat.append( nep.Esat ); 
                Ksat.append( nep.Ksat ); Qsat.append( nep.Qsat ); 
                Zsat.append( nep.Zsat ); msat.append( nep.msat ); 
                Esym.append( nep.Esym ); Lsym.append( nep.Lsym ); 
                Ksym.append( nep.Ksym ); Qsym.append( nep.Qsym ); 
                Zsym.append( nep.Zsym ); kappas.append( nep.kappas ); 
                kappav.append( nep.kappav ); 
            #
        axs[0,0].hist( nsat, bins=10, label=model )
        axs[1,0].hist( Esat, bins=10, label=model )
        axs[2,0].hist( Ksat, bins=10, label=model )
        axs[3,0].hist( Qsat, bins=10, label=model )
        axs[4,0].hist( msat, bins=10, label=model )
        axs[0,1].hist( Esym, bins=10, label=model )
        axs[1,1].hist( Lsym, bins=10, label=model )
        axs[2,1].hist( Ksym, bins=10, label=model )
        axs[3,1].hist( Qsym, bins=10, label=model )
    #
    axs[0,0].legend(loc='lower right',fontsize='10',ncol=2)
    #
    plt.savefig(pname)
    plt.close()

def main():
    #
    print(50*'-')
    print("Enter plot_matter_NEP.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    # list the available models
    #
    #models = [ 'Skyrme', 'ESkyrme', 'Gogny', 'Fayans', 'NLRH', 'DDRH', 'DDRHF' ]
    models, models_lower = nuda.matter.nep_models()
    #
    # plot distribution of NEP
    #
    pname = 'figs/plot_matter_NEP.png'
    plot_matter_NEP( pname, models )
    #
    print(50*'-')
    print("Exit plot_matter_NEP.py:")
    print(50*'-')
    #

    
if __name__ == "__main__":
    main()
