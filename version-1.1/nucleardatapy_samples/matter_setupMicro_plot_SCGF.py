
import numpy as np
import matplotlib.pyplot as plt

import nucleardatapy as nuda

def matter_setupMicro_fig( pname, mb, models, band, matter ):
    """
    Plot nucleonic energy per particle E/A in matter.\
    The plot is 2x1 with:\
    [0,0]: E/A versus den.\
    [1,0]: E/E_NRFFG versus den.\

    :param pname: name of the figure (*.png)
    :type pname: str.
    :param mb: many-body (mb) approach considered.
    :type mb: str.
    :param models: models to run on.
    :type models: array of str.
    :param band: object instantiated on the reference band.
    :type band: object.
    :param matter: can be 'SM' or 'NM'.
    :type matter: str.

    """
    #
    print(f'Plot name: {pname}')
    matter = band.matter
    #
    fig, axs = plt.subplots(2,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.12, right=0.95, top=0.85, wspace=0.05, hspace=0.05 )
    #
    axs[1].set_xlabel(r'$n_\text{nuc}$ (fm$^{-3}$)', fontsize = '14' )
    axs[0].tick_params('x', labelbottom=False)
    axs[0].set_xlim([0, 0.18])
    axs[1].set_xlim([0, 0.18])
    if matter.lower() == 'nm':
        axs[0].set_ylabel(r'$E_\text{int,NM}/A$ (MeV)', fontsize = '14' )
        axs[1].set_ylabel(r'$p_\text{NM}$ (MeV fm$^{-3}$)', fontsize = '14' )
        axs[0].set_ylim([-18, 20])
        axs[1].set_ylim([-1.0, 3.0])
        delta = 1.0
    elif matter.lower() == 'sm':
        axs[0].set_ylabel(r'$E_\text{int,SM}/A$ (MeV)', fontsize = '14' )
        axs[1].set_ylabel(r'$p_\text{SM}$ (MeV fm$^{-3})$', fontsize = '14' )
        axs[0].set_ylim([-18, 20])
        axs[1].set_ylim([-1.0, 3.0])
        delta = 0.0
    #
    for model in models:
        #
        mic = nuda.matter.setupMicro( model = model, var2 = delta )
        if nuda.env.verb_output: mic.print_outputs( )
        #
        print('model:',model,' delta:',delta)
        #
        check = nuda.matter.setupCheck( eos = mic, band = band )
        #
        if check.isInside:
            lstyle = 'solid'
        else:
            lstyle = 'dashed'
        #
        print('=> model (no err):',model,mic.e_err)
        if matter.lower() == 'nm':
            axs[0].plot( mic.nm_den, mic.nm_e2a_int, marker=mic.marker, linestyle=lstyle, markevery=mic.every, label=mic.model )
            axs[1].plot( mic.nm_den, mic.nm_pre_n3lo, marker=mic.marker, linestyle=lstyle, markevery=mic.every )
        elif matter.lower() == 'sm':
            axs[0].plot( mic.sm_den, mic.sm_e2a_int, marker=mic.marker, linestyle=lstyle, markevery=mic.every, label=mic.model )
            axs[1].plot( mic.sm_den, mic.sm_pre_n3lo, marker=mic.marker, linestyle=lstyle, markevery=mic.every )
        #
    axs[0].fill_between( band.den, y1=(band.e2a_int-band.e2a_std), y2=(band.e2a_int+band.e2a_std), color=band.color, alpha=band.alpha, visible=True )
    axs[0].plot( band.den, (band.e2a_int-band.e2a_std), color='k', linestyle='dashed' )
    axs[0].plot( band.den, (band.e2a_int+band.e2a_std), color='k', linestyle='dashed' )
    #
    fig.legend(loc='upper left',bbox_to_anchor=(0.1,1.0),fontsize='8',ncol=4,frameon=False)
    #
    if pname is not None: 
        plt.savefig(pname, dpi=300)
        plt.close()

def main():
    #
    print(50*'-')
    print("Enter matter_setupMicro_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    folder='figs-new'
    nuda.create_folder_fig(folder = folder)
    #
    # list the different matter cases investigated
    #
    matters = [ 'NM', 'SM' ]
    #
    for matter in matters:
        #
        # create the groups of figures
        #
        #mbs, mbs_lower = nuda.matter.micro_mbs()
        #mbs = [ 'VAR' ]
        #mbs = [ 'MBPT' ]
        #mbs = [ 'NLEFT' ]
        #mbs = [ 'AFDMC' ]
        #mbs = [ 'QMC' ]
        #mbs = [ 'VAR', 'AFDMC', 'BHF23', 'QMC', 'MBPT', 'NLEFT' ]
        if matter.lower() == 'nm':
            mbs = [ 'SCGF' ]
        elif matter.lower() == 'sm':
            mbs = [ 'SCGF' ]
        print('mbs:',mbs)
        #
        # fix the reference band in SM and NM
        #
        if matter.lower() == 'nm':
            bmodels = [ '2016-MBPT-AM', '2016-QMC-NM', '2020-MBPT-AM' ]
        elif matter.lower() == 'sm':
            bmodels = [ '2016-MBPT-AM', '2020-MBPT-AM' ]
        #
        den = np.array([0.08,0.1,0.12,0.14,0.16])
        band = nuda.matter.setupMicroBand( bmodels, matter = matter, den = den  )
        #
        # plot E/A in matter grouped by mb
        #
        for mb in mbs:
            #
            print('For mb:',mb)
            #
            # list the available models in mb
            #
            models, models_lower = nuda.matter.micro_models_mb_matter( mb, matter = matter )
            #
            models2 = []
            for model in models:
                if '2020-' in model:
                    models2.append(model)
            models = models2
            print('models:',models)
            if models:
                print('there are models')
            if not models:
                print('there are no models')
                continue
            #
            pname = folder+'/plot_matter_setupMicro_'+matter+'_'+mb+'.png'
            matter_setupMicro_fig( pname, mb, models, band, matter )
            #
    #
    print(50*'-')
    print("Exit matter_setupMicro_plot.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
