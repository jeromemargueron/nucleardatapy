
import os
import sys
import numpy as np

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_SetupMassesTheory.py:")
    print(50*'-')
    #
    #tables = [ '1995-DZ' ]
    tables, tables_lower = nuda.tables_masses_theory()
    #
    for table in tables:
        #
        # Search for GS and unstable nuclei in the 'AME' '2020'
        #
        mas = nuda.SetupMassesTheory( table = table )
        mas.print_outputs( )
    #
    # illustration of the use of diff to compute the difference
    # between two models
    #
    print('\nDifference between two mass models\n')
    #
    # first define the reference model:
    mas = nuda.SetupMassesTheory( table = '1995-DZ' )
    # second compute the different with another model:
    Zref = 50
    N_diff, A_diff, BE_diff, BE2A_diff = mas.diff( table = '1995-ETFSI', Zref = Zref )
    print('For Zref=',Zref)
    print('N_diff:',N_diff)
    print('BE2A_diff:',BE2A_diff)
    #
    #
    # illustration of the use of diff_exp to compute the difference
    # between the experimental measurement and the reference model
    #
    print('\nDifference with experimental masses\n')
    #
    # first define the reference model:
    mas = nuda.SetupMassesTheory( table = '1995-DZ' )
    # second compute the different with experimental masses:
    Zref = 50
    N_diff, A_diff, BE_diff, BE2A_diff = mas.diff_exp( table_exp = 'AME', version_exp = '2020', Zref = Zref )
    print('For Zref=',Zref)
    print('N_diff:',N_diff)
    print('BE2A_diff:',BE2A_diff)
    #
    print(50*'-')
    print("Exit sample_SetupMasses.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
