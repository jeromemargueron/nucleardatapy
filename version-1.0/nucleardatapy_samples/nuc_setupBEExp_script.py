
import os
import sys
import numpy as np

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter nuc_setupBEExp_script.py:")
    print(50*'-')
    #
    #tables = [ 'AME' ]
    tables, tables_lower = nuda.nuc.be_exp_tables()
    print('tables:',tables)
    #
    for table in tables:
        #
        # Search for GS and unstable nuclei in the 'AME' '2020'
        #
        mas = nuda.nuc.setupBEExp( table = table, version = '2020' )
        print('\nFrom mass table')
        #print('A:',mas.A)
        print('number of lines:',mas.nbLine)
        print('number of nuclei:',mas.nbNuc)
        sel = mas.select( state= 'gs', interp = 'n', nucleus = 'unstable' )
        #print('A:',sel.A)
        print('After selection')
        print('number of nuclei:',sel.sel_nbNucSel)
        if nuda.env.verb_output: mas.print_outputs( )
        #
        # Search for nuclei discovered betwen 1950 and 1960
        #
        #mas = nuda.SetupMassesExp( table = table, version = '2020' )
        #print('\nFrom mass table')
        #print('number of lines:',mas.nbLine)
        #print('number of nuclei:',mas.nbNuc)
        #sel = mas.select_year( year_min=1950, year_max=1960, state= 'gs' )
        #print('After selection')
        #print('number of nuclei:',sel.sel_nbNucSel)
        #mas.print_outputs( )

    #
    print(50*'-')
    print("Exit nuc_setupBEExp_script.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
