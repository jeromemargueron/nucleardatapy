
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter eos_setupCCi_script.py:")
    print(50*'-')
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
    core_models, core_models_lower = nuda.matter.matter_models()
    print('List of core_models:',core_models)
    core_models = [ 'Var' ]
    #core_params, core_params_lower = nuda.matter.matter_esym_params( model = model )
    #print('List of core_params:',core_params)
    core_params = [ '1998-APR' ]
    #
    # ==============
    # connection
    # ==============
    #
    connect = 'density'
    emp = None
    #emp = 'simple'
    #emp = 'Steiner'
    boundaries = [ 0.016, 0.16 ] # in units of fm-3
    #connect = 'epsilon'
    #boundaries = [ 15.0, 150.0 ] # in units of MeV fm-3
    #connect = 'pressure'
    #boundaries = [ 1.0, 20.0 ] # in units of MeV fm-3
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
                eos_cc = nuda.eos.setupCCi( crust_model = crust_model, core_model = core_model, core_param = core_param, connect = connect, boundaries = boundaries )
                if nuda.env.verb_output: eos_cc.print_outputs( )
                #
            #
        #
    #
    print(50*'-')
    print("Exit eos_setupCCi_script.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
