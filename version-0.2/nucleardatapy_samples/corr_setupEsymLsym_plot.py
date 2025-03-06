
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
#plt.rcParams.update({'font.size': 16})

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda



def main():
    #
    print(50*'-')
    print("Enter plot_corr_setupEsymLsym.py:")
    print(50*'-')
    #
    # create the folder where the figures are stored
    #
    os.system('mkdir -p figs/')
    #
    #constraints = [ '2009-HIC', '2010-RNP', '2012-FRDM', '2013-NS', '2014-IAS', '2014-IAS+RNP', \
    #         '2015-POL-208PB', '2015-POL-120SN', '2015-POL-68NI', '2017-UG', \
    #          '2021-PREXII-Reed', '2021-PREXII-Reinhard', '2021-PREXII-Zhang' ]
    #constraints = [ '2009-HIC', '2010-RNP', '2012-FRDM', '2014-IAS', '2014-IAS+RNP' ]
    constraints, constraints_lower = nuda.corr.EsymLsym_constraints()
    #
    pname = 'figs/plot_corr_setupEsymLsym.png'
    plot_corr_setupEsymLsym( pname, constraints )
    #
    print(50*'-')
    print("Exit plot_corr_setupEsymLsym.py:")
    print(50*'-')
    #
    
if __name__ == "__main__":
    main()
