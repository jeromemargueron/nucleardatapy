
import os
import sys
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter sample_matter_setupNEPDist.py:")
    print(50*'-')
    #
    # chose a list of models
    #
    #models = [ 'Skyrme', 'ESkyrme', 'Gogny', 'Fayans', 'NLRH', 'DDRH', 'DDRHF' ]
    #models = [ 'Skyrme' ]
    models, models_lower = nuda.matter.nep_models()
    #
    dist = nuda.matter.setupNEPDist( models )
    dist.print_outputs( )
    dist.print_latex( )
    if nuda.env.verb_output: dist.print_outputs( )
    #
    print(50*'-')
    print("Exit sample_matter_setupNEPDist.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
