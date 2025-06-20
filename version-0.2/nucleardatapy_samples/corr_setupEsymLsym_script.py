
import numpy as np

import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter corr_setupEsymLsym_script.py:")
    print(50*'-')
    #
    #constraints = [ '2009-HIC', '2010-RNP', '2012-FRDM', '2013-NS', '2014-IAS', '2014-IAS+RNP', \
    #         '2015-POL-208PB', '2015-POL-120SN', '2015-POL-68NI', '2017-UG', \
    #          '2021-PREXII-Reed', '2021-PREXII-Reinhard', '2021-PREXII-Zhang' ]
    constraints, constraints_lower = nuda.corr.EsymLsym_constraints()
    constraints.remove('2013-NS'); constraints.remove('2017-UG')
    #
    # constraints from finite nuclei
    #
    for constraint in constraints:
        #
        corr = nuda.corr.setupEsymLsym( constraint = constraint )
        #print('Esym:',mic.cont_Esym)
        #print('Lsym:',mic.cont_Lsym)
        if nuda.env.verb_output: corr.print_outputs( )
    #
    # constraint from neutron stars
    #
    constraints = [ '2013-NS', '2017-UG' ]
    #
    for constraint in constraints:
        #
        corr = nuda.corr.setupEsymLsym( constraint = constraint )
        #print('Esym:',mic.cont_Esym)
        #print('Lsym:',mic.cont_Lsym)
        if nuda.env.verb_output: corr.print_outputs( )
    #
    print(50*'-')
    print("Exit corr_setupEsymLsym_script.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
