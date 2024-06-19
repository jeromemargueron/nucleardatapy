
import os
import sys
import numpy as np

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nudy

def main():
    #
    print(50*'-')
    print("Enter sample_SetupMasses.py:")
    print(50*'-')
    #
    tables = [ 'AME' ]
    #tables, tables_lower = nudy.tables_masses()
    #
    for table in tables:
        #
        mas = nudy.SetupMasses( table = table, version = '2020' )
        print('From mass table')
        #print('A:',mas.A)
        print('number of lines:',mas.nbLine)
        print('number of nuclei:',mas.nbNuc)
        sel = mas.select( state= 'gs', interp = 'n', nucleus = 'unstable' )
        #print('A:',sel.A)
        print('After selection')
        print('number of nuclei:',sel.sel_nbNucSel)
        mas.print_outputs( )
    #
    print(50*'-')
    print("Exit sample_SetupMasses.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
