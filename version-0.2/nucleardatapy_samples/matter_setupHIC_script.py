
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter matter_setupHIC_script.py:")
    print(50*'-')
    #
    constraints, constraints_lower = nuda.matter.hic_constraints()
    #
    for constraint in constraints:
        #
        print('constraint:',constraint)
        hic = nuda.matter.setupHIC( constraint = constraint )
        if nuda.env.verb_output: hic.print_outputs( )
    #
    print(50*'-')
    print("Exit matter_setupHIC_script.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
