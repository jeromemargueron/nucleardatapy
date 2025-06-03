
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter matter_setupNEPDist_script.py:")
    print(50*'-')
    #
    # chose a list of models
    #
    #models = [ 'Skyrme', 'ESkyrme', 'Gogny', 'Fayans', 'NLRH', 'DDRH', 'DDRHF' ]
    models = [ 'ESkyrme' ]
    #models, models_lower = nuda.matter.nep_models()
    #
    dist = nuda.matter.setupNEPDist( models )
    dist.print_outputs( )
    dist.print_latex( )
    if nuda.env.verb_output: dist.print_outputs( )
    #
    print(50*'-')
    print("Exit matter_setupNEPDist_script.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
