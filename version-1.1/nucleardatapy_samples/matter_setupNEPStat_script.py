
import os
import sys
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter matter_setupNEPStat_script.py:")
    print(50*'-')
    #
    # list the available models
    #
    #models = [ 'Skyrme', 'GSkyrme', 'ESkyrme', 'Gogny', 'Fayans', 'NLRH', 'DDRH', 'DDRHF' ]
    models, models_lower = nuda.matter.nep_models()
    print('Available models:',models)
    #
    # choose a given model
    #
    model = 'Skyrme'
    dist = nuda.matter.setupNEPStat_model( model )
    dist.print_latex( )
    if nuda.env.verb_output: dist.print_outputs( )
    #
    model = 'GSkyrme'
    dist = nuda.matter.setupNEPStat_model( model )
    dist.print_latex( )
    if nuda.env.verb_output: dist.print_outputs( )
    #
    model = 'ESkyrme'
    dist = nuda.matter.setupNEPStat_model( model )
    dist.print_latex( )
    if nuda.env.verb_output: dist.print_outputs( )
    #
    model = 'NLRH'
    dist = nuda.matter.setupNEPStat_model( model )
    dist.print_latex( )
    if nuda.env.verb_output: dist.print_outputs( )
    #
    model = 'DDRH'
    dist = nuda.matter.setupNEPStat_model( model )
    dist.print_latex( )
    if nuda.env.verb_output: dist.print_outputs( )
    #
    model = 'DDRHF'
    dist = nuda.matter.setupNEPStat_model( model )
    dist.print_latex( )
    if nuda.env.verb_output: dist.print_outputs( )
    #
    print(50*'-')
    print("Exit matter_setupNEPStat_script.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
