
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter matter_setupHIC_script.py:")
    print(50*'-')
    #
    inferences, inferences_lower = nuda.matter.hic_inferences()
    #
    for inference in inferences:
        #
        print('inference:',inference)
        hic = nuda.matter.setupHIC( inference = inference )
        if nuda.env.verb_output: hic.print_outputs( )
    #
    print(50*'-')
    print("Exit matter_setupHIC_script.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
