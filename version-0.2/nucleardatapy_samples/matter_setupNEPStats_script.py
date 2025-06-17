
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter matter_setupNEPStats_script.py:")
    print(50*'-')
    #
    # chose a list of models
    #
    #models = [ 'Skyrme', 'GSkyrme', 'ESkyrme', 'Gogny', 'Fayans', 'NLRH', 'DDRH', 'DDRHF' ]
    models, models_lower = nuda.matter.nep_models()
    #models = [ 'DDRHF' ]
    #
    dist = nuda.matter.setupNEPStat_models( models )
    dist.print_outputs( )
    dist.print_latex( )
    if nuda.env.verb_output: dist.print_outputs( )
    #
    print(50*'-')
    print("Exit matter_setupNEPStats_script.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
