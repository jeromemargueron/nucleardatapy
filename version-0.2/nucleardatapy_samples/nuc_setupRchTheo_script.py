
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter nuc_setupRchTheo_script.py:")
    print(50*'-')
    #
    tables, tables_lower = nuda.nuc.rch_theo_tables()
    #tables = [ '2021-BSkG1' ]
    print('tables:',tables)
    #
    Zref = 50
    #
    for table in tables:
        #
        rch = nuda.nuc.setupRchTheo( table = table )
        if nuda.env.verb_output: rch.print_outputs( )
        #Nref, Aref, Rchref = rch.Rch_isotopes( Zref = 50 )
        rchIsot = nuda.nuc.setupRchTheoIsotopes( rch, Zref = Zref )
        print('For isotopes: Zref=',Zref)
        print('N:',rchIsot.N)
        print('A:',rchIsot.A)
        print('Rch:',rchIsot.Rch)
    #
    print(50*'-')
    print("Exit nuc_setupRchTheo_script.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
