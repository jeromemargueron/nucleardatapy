
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("This is an exemple showning how to employ the toolkit:")
    print(50*'-')
    #
    models = [ '1981-VAR-AM-FP', '1998-VAR-AM-APR', '2016-QMC-NM', '2016-MBPT-AM', \
             '2018-QMC-NM', '2023-MBPT-AM' ]
    #
    for model in models:
        #
        micro = nuda.matter.setupMicro( model = model )
        micro.print_outputs()
    #
    print(50*'-')
    print("End of the example")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
