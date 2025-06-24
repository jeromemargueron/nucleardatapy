
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter nuc_setupBETheo_script.py:")
    print(50*'-')
    #
    tables, tables_lower = nuda.nuc.be_theo_tables()
    #tables = [ '2023-BSkG3' ]
    #
    for table in tables:
        #
        # Search for GS and unstable nuclei in the theory mass table
        #
        mas = nuda.nuc.setupBETheo( table = table )
        if nuda.env.verb_output: mas.print_outputs( )
    #
    # illustration of the use of diff to compute the difference
    # between two models
    #
    print('\nDifference between two mass models\n')
    #
    # first define the reference model:
    mas = nuda.nuc.setupBETheo( table = '1995-DZ' )
    # second compute the different with another model:
    Zref = 50
    N_diff, A_diff, BE_diff, BE2A_diff = mas.diff( table = '1995-ETFSI', Zref = Zref )
    print('For Zref=',Zref)
    print('N_diff:',N_diff)
    print('BE2A_diff:',BE2A_diff)
    #
    # illustration of the use of diff_exp to compute the difference
    # between the experimental measurement and the reference model
    #
    print('\nDifference with experimental masses\n')
    #
    # first define the reference model:
    mas = nuda.nuc.setupBETheo( table = '1995-DZ' )
    # second compute the different with experimental masses:
    Zref = 50
    N_diff, A_diff, BE_diff, BE2A_diff = mas.diff_exp( table_exp = 'AME', version_exp = '2020', Zref = Zref )
    print('For Zref=',Zref)
    print('N_diff:',N_diff)
    print('BE2A_diff:',BE2A_diff)
    #
    print(50*'-')
    print("Exit setupBETheo_script_nuc.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
