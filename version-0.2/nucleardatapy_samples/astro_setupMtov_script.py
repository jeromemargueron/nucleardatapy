
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter astro_setupMtot_script.py:")
    print(50*'-')
    #
    # sources down
    #
    sources_do, sources_do_lower = nuda.astro.masses_sources( )
    print('Complete list of available sources_low:',sources_do)
    #
    sources_do = [ 'J1614–2230', 'J0348+0432', 'J2215+5135', 'J1600+3053', 'J0740+6620' ]
    #sources_do = [ 'J1614–2230', 'J1600+3053', 'J0740+6620' ]
    #
    print('sources_low considered:',sources_do)
    #
    # sources up
    #
    sources_up, sources_up_lower = nuda.astro.mup_sources( )
    print('Complete list of available sources_up:',sources_up)
    #
    #sources_up = [ 'GW170817' ]
    #
    print('sources_up considered:',sources_up)
    #
    # compute the distribution
    #
    prob = nuda.astro.setupMtov( sources_do, sources_up )
    if nuda.env.verb_output: prob.print_output( )
    if nuda.env.verb_latex: prob.print_latex( )
    #
    print(50*'-')
    print("Exit astro_setupMtov_script.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
