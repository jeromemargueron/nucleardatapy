
import os
import sys
import numpy as np

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_nuc_setupISGMRExp.py:")
    print(50*'-')
    #
    #tables = [ '2010-ISGMR-LI', '2018-ISGMR-GARG' ]
    #tables, tables_lower = nuda.nuc.isgmr_exp_tables()
    tables = [ '2010-ISGMR-LI' ]
    #tables = [ '2018-ISGMR-GARG' ]
    #tables = [ '2018-ISGMR-GARG-LATEX' ]
    #
    for table in tables:
        #
        print('\ntable',table)
        gmr = nuda.nuc.setupISGMRExp( table = table )
        if nuda.env.verb_output: gmr.print_outputs( )
    #
    print(50*'-')
    print("Exit sample_nuc_setupISGMRExp.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
