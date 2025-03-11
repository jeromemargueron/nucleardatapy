
import nucleardatapy as nuda

def main():
    #
    print(50*'-')
    print("Enter corr_setupEsymDen_script.py:")
    print(50*'-')
    #
    #constraints = [ '2009-HIC', '2010-RNP', '2012-FRDM', '2013-NS', '2014-IAS', '2014-IAS+RNP', \
    #         '2015-POL-208PB', '2015-POL-120SN', '2015-POL-68NI', '2017-UG', \
    #          '2021-PREXII-Reed', '2021-PREXII-Reinhard', '2021-PREXII-Zhang' ]
    constraints, constraints_lower = nuda.corr.EsymLsym_constraints()
    print('constraints:',constraints)
    constraints = [ '2014-IAS' ]
    #
    Ksym = -100.0
    #
    for constraint in constraints:
        #
        esym = nuda.corr.setupEsymDen( constraint = constraint , Ksym=Ksym )
        #print('Esym_max:',esym.esym_e2a_max)
        #print('Esym_min:',esym.esym_e2a_min)
        if nuda.env.verb_output: esym.print_outputs()
    #
    print(50*'-')
    print("Exit corr_setupEsymDen_script.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
