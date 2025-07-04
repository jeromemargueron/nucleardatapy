
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter eos_setupCC_script.py:")
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
    core_kind = 'micro'
    #core_kind = 'pheno'
    #
    if core_kind == 'micro':
        core_models, core_models_lower = nuda.matter.micro_esym_models()
        print('List of core_models:',core_models)
        core_models = [ '1998-VAR-AM-APR' ]
        core_params = [ None ]
    elif core_kind == 'pheno':
        core_models, core_models_lower = nuda.matter.pheno_esym_models()
        print('List of core_models:',core_models)
        core_models = [ 'Skyrme' ]
        core_params, core_params_lower = nuda.matter.pheno_esym_params( model = model )
        print('List of core_params:',core_params)
        core_params = [ 'SLy5' ]
    else:
        print('eos_setupCC_script.py: core_kind ',core_kind,' is ill defined.')
        print('eos_setupCC_script.py: -- Exit the code --')
        exit()
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
                eos_cc = nuda.eos.setupCC( crust_model = crust_model, core_kind=core_kind, core_model = core_model, core_param = core_param, connect = connect, boundaries = boundaries )
                if nuda.env.verb_output: eos_cc.print_outputs( )
                #
            #
        #
    #
    print(50*'-')
    print("Exit eos_setupCC_script.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
