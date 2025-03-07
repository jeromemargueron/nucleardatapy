
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter matter_setupMicro_LP_script.py:")
    print(50*'-')
    #
    models, models_lower = nuda.matter.micro_LP_models()
    #
    for model in models:
        #
        print('Model:',model)
        lp = nuda.matter.setupMicroLP( model = model )
        print('LP in SM:')
        print('kfn:',lp.sm_kfn)
        print('F0:',lp.sm_LP['F'][0])
        print('G0:',lp.sm_LP['G'][0])
        print('LP in NM:')
        print('kfn:',lp.nm_kfn)
        print('F0:',lp.nm_LP['F'][0])
        print('G0:',lp.nm_LP['G'][0])
        if nuda.env.verb_output: lp.print_outputs( )
    #
    print(50*'-')
    print("Exit matter_setupMicro_LP_script.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
