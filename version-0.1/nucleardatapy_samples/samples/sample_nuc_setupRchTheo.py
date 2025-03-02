
import os
import sys
import numpy as np

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_nuc_setupRchTheo.py:")
    print(50*'-')
    #
    tables, tables_lower = nuda.nuc.rch_theo_tables()
    tables = [ '2021-BSkG1' ]
    #
    for table in tables:
        #
        rch = nuda.nuc.setupRchTheo( table = table )
        rch.print_outputs()
        Nref, Aref, Rchref = rch.Rch_isotopes( Zref = 50 )
        print('Nref:',Nref)
        print('Aref:',Aref)
        print('Rchref:',Rchref)
        if nuda.env.verb_output: rch.print_outputs( )
    #
    print(50*'-')
    print("Exit sample_nuc_setupRchTheo.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
