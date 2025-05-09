
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter nuc_setupRnpExp_script.py:")
    print(50*'-')
    #
    sources, sources_lower = nuda.nuc.rnp_exp( )
    print('Complete list of available sources:', sources )
    #
    sources = ['48Ca', '208Pb']
    #
    print('sources considered:',sources)
    #
    for source in sources:
        #
        # get the neutron skin associated to `source` and `cal`
        # 
        cals = nuda.nuc.rnp_exp_source( source = source )
        print(f'source: {source}, cals: {cals}')
        #
        for cal in cals:
            rnp = nuda.nuc.setupRnpExp( source = source, cal = cal )
            rnp.print_outputs( )
            #
    #
    print(50*'-')
    print("Exit nuc_setupRnpExp_script.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
