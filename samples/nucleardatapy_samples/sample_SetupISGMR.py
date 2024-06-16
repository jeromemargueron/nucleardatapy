
import os
import sys
import numpy as np

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nudy

def main():
    #
    print(50*'-')
    print("Enter sample_SetupISGMR.py:")
    print(50*'-')
    #
    #tables = [ '2010-ISGMR_LI', '2018-ISGMR-GARG' ]
    tables, tables_lower = nudy.tables_isgmr()
    #
    for table in tables:
        #
        gmr = nudy.SetupISGMR( table = table )
        nudy.print_outputs_isgmr( gmr )
    #
    print(50*'-')
    print("Exit sample_SetupISGMR.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
