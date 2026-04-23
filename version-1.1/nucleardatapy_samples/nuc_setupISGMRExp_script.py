
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter nuc_setupISGMRExp_script.py:")
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
    print("Exit nuc_setupISGMRExp_script.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
