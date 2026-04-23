
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter nuc_setupRchEmp_script.py:")
    print(50*'-')
    #
    formulas, formulas_lower = nuda.nuc.rch_emp_formulas()
    print('formulas:',formulas)
    #
    Z = 50
    N = 70
    A = N + Z
    print('For isotope: Z:',Z,' N:',N)
    #
    for formula in formulas:
        #
        print(' formula:',formula)
        rch = nuda.nuc.setupRchEmp( A, Z, formula = formula )
        if nuda.env.verb_output: rch.print_outputs( )
        print('Rch:',rch.nucRch[0])
    #
    print(50*'-')
    print("Exit nuc_setupRchEmp_script.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
