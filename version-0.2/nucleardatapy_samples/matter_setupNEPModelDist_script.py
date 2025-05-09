
import os
import sys
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter matter_setupNEPModelDist_script.py:")
    print(50*'-')
    #
    # list the available models
    #
    #models = [ 'Skyrme', 'ESkyrme', 'Gogny', 'Fayans', 'NLRH', 'DDRH', 'DDRHF' ]
    models, models_lower = nuda.matter.nep_models()
    #
    # chose a given model
    #
    model = 'Skyrme'
    dist = nuda.matter.setupNEPModelDist( model )
    dist.print_latex( )
    if nuda.env.verb_output: dist.print_outputs( )
    #
    model = 'ESkyrme'
    dist = nuda.matter.setupNEPModelDist( model )
    dist.print_latex( )
    if nuda.env.verb_output: dist.print_outputs( )
    #
    model = 'NLRH'
    dist = nuda.matter.setupNEPModelDist( model )
    dist.print_latex( )
    if nuda.env.verb_output: dist.print_outputs( )
    #
    model = 'DDRH'
    dist = nuda.matter.setupNEPModelDist( model )
    dist.print_latex( )
    if nuda.env.verb_output: dist.print_outputs( )
    #
    model = 'DDRHF'
    dist = nuda.matter.setupNEPModelDist( model )
    dist.print_latex( )
    if nuda.env.verb_output: dist.print_outputs( )
    #
    print(50*'-')
    print("Exit matter_setupNEPModelDist_script.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
