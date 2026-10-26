
import numpy as np
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter eos_setupCCi_plot.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    #folder='figs-new'
    folder='figs'
    nuda.create_folder_fig(folder = folder)
    #
    # ==============
    # band for the check
    # ==============
    #
    den = np.array([0.08,0.1,0.12,0.14,0.16])
    models = [ '2016-MBPT-AM', '2016-QMC-NM', '2020-MBPT-AM' ]
    band = nuda.matter.setupMicroBand( models, den=den, matter='NM' )
    #
    # ==============
    # crust models
    # ==============
    #
    crust_models, crust_models_lower = nuda.crust.crust_models()
    print('List of crust_models:',crust_models)
    crust_models = [ '2022-GMRS-H4' ]
    #
    # ==============
    # core models
    # ==============
    #
    #core_models, core_models_lower = nuda.matter.matter_esym_models()
    #core_models = [ 'Skyrme', 'ESkyrme', 'NLRH', 'DDRH', 'DDRHF', 'Var', 'BHF23BF', 'MBPT', 'NLEFT', 'SCGF', 'CC' ]
    core_models = [ 'Skyrme' ]
    #core_params, core_params_lower = nuda.matter.matter_esym_params( model = core_models[0] )
    core_params = [ 'SLy5' ]
    #print('List of core_params:',core_params)
    #
    # ==============
    # connection
    # ==============
    #
    #connect = 'density'
    emp = None
    #emp = 'simple'
    #emp = 'Steiner'
    #boundaries = [ 0.016, 0.16 ] # in units of fm-3
    connect = 'epsilon'
    boundaries = [ 15.0, 150.0 ] # in units of MeV fm-3
    #connect = 'pressure'
    #boundaries = [ 0.1, 1.0 ] # in units of MeV fm-3
    #
    for crust_model in crust_models:
        #
        print('For crust_model:',crust_model)
        #
        for core_model in core_models:
            #
            print('For core_model:',core_model)
            #
            for core_param in core_params:
                #
                # check pressure: pre(n)
                #
                if core_param is not None:
                    if emp is not None:
                        pname = folder+'/plot_eos_setupCCi_checkpre_'+crust_model+'_'+core_model+'_'+core_param+'_'+connect+'_'+emp+'.png'
                    else:
                        pname = folder+'/plot_eos_setupCCi_checkpre_'+crust_model+'_'+core_model+'_'+core_param+'_'+connect+'.png'
                else:
                    if emp is not None:
                        pname = folder+'/plot_eos_setupCCi_checkpre_'+crust_model+'_'+core_model+'_'+connect+'_'+emp+'.png'
                    else:
                        pname = folder+'/plot_eos_setupCCi_checkpre_'+crust_model+'_'+core_model+'_'+connect+'.png'
                nuda.fig.eos_setupCCi_checkpre_fig( pname, band, crust_model = crust_model, core_model = core_model, core_param = core_param, connect = connect, boundaries = boundaries, emp = emp )
                #
                # check EoS: pre(eps)
                #
                if core_param is not None:
                    if emp is not None:
                        pname = folder+'/plot_eos_setupCCi_checkeos_'+crust_model+'_'+core_model+'_'+core_param+'_'+connect+'_'+emp+'.png'
                    else:
                        pname = folder+'/plot_eos_setupCCi_checkeos_'+crust_model+'_'+core_model+'_'+core_param+'_'+connect+'.png'
                else:
                    if emp is not None:
                        pname = folder+'/plot_eos_setupCCi_checkeos_'+crust_model+'_'+core_model+'_'+connect+'_'+emp+'.png'
                    else:
                        pname = folder+'/plot_eos_setupCCi_checkeos_'+crust_model+'_'+core_model+'_'+connect+'.png'
                nuda.fig.eos_setupCCi_checkeos_fig( pname, band, crust_model = crust_model, core_model = core_model, core_param = core_param, connect = connect, boundaries = boundaries, emp = emp )
                #
                # show EoS: pre(eps)
                #
                if core_param is not None:
                    pname = folder+'/plot_eos_setupCCi_eos_'+crust_model+'_'+core_model+'_'+core_param+'.png'
                else:
                    pname = folder+'/plot_eos_setupCCi_eos_'+crust_model+'_'+core_model+'.png'
                nuda.fig.eos_setupCCi_eos_fig( pname, band, crust_model = crust_model, core_model = core_model, core_param = core_param )
                #
            #
        #
    #
    print(50*'-')
    print("Exit eos_setupCCi_plot.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
