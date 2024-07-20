
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def plot_NEP( pname, models_micro, models_pheno ):
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
    axs[4,0].set_ylabel(r'$m_{sat}^*$')
    axs[0,1].set_ylabel(r'$E_{sym}$')
    axs[1,1].set_ylabel(r'$L_{sym}$')
    axs[2,1].set_ylabel(r'$K_{sym}$')
    axs[3,1].set_ylabel(r'$Q_{sym}$')
    #
    # Built distribution of NEP
    #
    for model in models_pheno:
        #
        nsat = []; Esat = []; Ksat = []; Qsat = []; Zsat = []
        Esym = []; Lsym = []; Ksym = []; Qsym = []; Zsym = []
        msat = []; kappas = []; kappav = []
        params, params_lower = nuda.params_pheno_matter( model = model )
        #
        for param in params:
            #
            print('param:',param)
            pheno = nuda.SetupPhenoMatter( model = model, param = param )
            if pheno.nep:
                nsat.append( pheno.nsat ); Esat.append( pheno.Esat ); 
                Ksat.append( pheno.Ksat ); Qsat.append( pheno.Qsat ); 
                Zsat.append( pheno.Zsat ); msat.append( pheno.msat ); 
                Esym.append( pheno.Esym ); Lsym.append( pheno.Lsym ); 
                Ksym.append( pheno.Ksym ); Qsym.append( pheno.Qsym ); 
                Zsym.append( pheno.Zsym ); kappas.append( pheno.kappas ); 
                kappav.append( pheno.kappav ); 
            #
        #if model == 'Skyrme':
        #    Esat = np.array( Esat ) / 10.0
        #    nsat = np.array( nsat ) / 10.0
        #    Ksat = np.array( Ksat ) / 10.0
        #    Qsat = np.array( Qsat ) / 10.0
        #    Zsat = np.array( Zsat ) / 10.0
        #    Esym = np.array( Esym ) / 10.0
        #    Lsym = np.array( Lsym ) / 10.0
        #    Ksym = np.array( Ksym ) / 10.0
        #    Qsym = np.array( Qsym ) / 10.0
        #    Zsym = np.array( Zsym ) / 10.0
        #    msat = np.array( msat ) / 10.0
        #    kappas = np.array( kappas ) / 10.0
        #    kappav = np.array( kappav ) / 10.0
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
    print("Enter plot_NEP.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    # list the available models
    #
    models_micro, models_lower = nuda.models_micro_matter()
    models_pheno = [ 'Skyrme', 'NLRH', 'DDRH', 'DDRHF' ]
    #
    # plot distribution of NEP
    #
    pname = 'figs/plot_NEP.png'
    plot_NEP( pname, models_micro, models_pheno )
    #
    print(50*'-')
    print("Exit plot_NEP.py:")
    print(50*'-')
    #

    
if __name__ == "__main__":
    main()
