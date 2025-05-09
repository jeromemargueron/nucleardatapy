
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter nuc_setupRchExp_script.py:")
    print(50*'-')
    #
    #tables = [ '2013-Angeli' ]
    tables, tables_lower = nuda.nuc.rch_exp_tables()
    #
    Zref = 50
    #
    for table in tables:
        #
        rch = nuda.nuc.setupRchExp( table = table )
        if nuda.env.verb_output: rch.print_outputs( )
        #Nref, Aref, Rchref, Rchref_err = rch.Rch_isotopes( Zref = 50 )
        rchIsot = nuda.nuc.setupRchExpIsotopes( rch, Zref = Zref )
        print('For isotopes: Zref=',Zref)
        print('N:',rchIsot.N)
        print('A:',rchIsot.A)
        print('Rch:',rchIsot.Rch)
        print('Rch_err:',rchIsot.Rch_err)
    #
    print(50*'-')
    print("Exit nuc_setupRchExp_script.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
