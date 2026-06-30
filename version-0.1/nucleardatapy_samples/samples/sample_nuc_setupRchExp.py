
import os
import sys
import numpy as np

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_nuc_setupRchExp.py:")
    print(50*'-')
    #
    #tables = [ '2013-Angeli' ]
    tables, tables_lower = nuda.nuc.rch_exp_tables()
    #
    for table in tables:
        #
        rch = nuda.nuc.setupRchExp( table = table )
        Nref, Aref, Rchref, Rchref_err = rch.Rch_isotopes( Zref = 50 )
        print('Nref:',Nref)
        print('Aref:',Aref)
        print('Rchref:',Rchref)
        print('Rchref_err:',Rchref_err)
        if nuda.env.verb_output: rch.print_outputs( )
    #
    print(50*'-')
    print("Exit sample_nuc_setupRchExp.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
