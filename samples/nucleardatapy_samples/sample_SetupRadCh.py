
import os
import sys
import numpy as np

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nudy

def main():
    #
    print(50*'-')
    print("Enter sample_SetupRadCh.py:")
    print(50*'-')
    #
    #tables = [ '2013-Angeli' ]
    tables, tables_lower = nudy.tables_rad_ch()
    #
    for table in tables:
        #
        gmr = nudy.SetupRadCh( table = table )
        nudy.print_outputs_rad_ch( gmr )
    #
    print(50*'-')
    print("Exit sample_SetupRadCh.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
