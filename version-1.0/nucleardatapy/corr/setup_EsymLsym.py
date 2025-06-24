import os
import sys
import numpy as np  # 1.15.0
import random

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def EsymLsym_constraints():
    """
    Return a list of constraints available in this toolkit in the \
    following list: '2009-HIC', '2010-RNP', '2012-FRDM', '2013-NS', \
    '2014-IAS', '2014-IAS+RNP', '2015-POL-208Pb', '2015-POL-120Sn', \
    '2015-POL-68Ni', '2017-UG', '2021-PREXII-Reed', \
    '2021-PREXII-Reinhard', '2023-PREXII+CREX-Zhang', \
    '2023-EDF-D4', '2023-EDF-D4-IAS', '2023-EDF-D4-IAS-Rnp'; \
    and print them all on the prompt.

    :return: The list of constraints.
    :rtype: list[str].
    """
    constraints = [ '2009-HIC', '2010-RNP', '2012-FRDM', '2013-NS', '2014-IAS', '2014-IAS+RNP', \
             '2015-POL-208Pb', '2015-POL-120Sn', '2015-POL-68Ni', '2017-UG', \
              '2021-PREXII-Reed', '2021-PREXII-Reinhard', '2023-PREXII+CREX-Zhang',\
              '2023-EDF-D4', '2023-EDF-D4-IAS', '2023-EDF-D4-IAS-Rnp' ]
    #print('Constraints available in the toolkit:',constraints)
    constraints_lower = [ item.lower() for item in constraints ]
    return constraints, constraints_lower

def HIC_Esym(n,gi,csk,csp):
    n_sat = 0.16 # in fm-3
    return 0.5 * csk * (n/n_sat)**0.6666 + 0.5 * csp * (n/n_sat)**gi 

def HIC_Lsym(n,gi,csk,csp):
    n_sat = 0.16 # in fm-3
    return csk / (n/n_sat)**0.3333 + 1.5 * gi * csp * (n/n_sat)**(gi-1.0) 

def HIC_xgi(Esym):
    return 1.0 + 0.2 * ( Esym - 30.1 ) / ( 33.8 - 30.1 ) 

def HIC_Lsym_bound(Esym,gi,csk,csp):
    return HIC_Lsym(0.16,gi*HIC_xgi(Esym),csk*Esym/30.1,csp*Esym/30.1)

class setupEsymLsym():
    """
    Instantiate the values of Esym and Lsym from the constraint.

    The name of the constraint to be chosen in the \
    following list: '2009-HIC', '2010-RNP', '2012-FRDM', '2013-NS', \
    '2014-IAS', '2014-IAS+RNP', '2015-POL-208Pb', '2015-POL-120Sn', \
    '2015-POL-68Ni', '2017-UG', '2021-PREXII-Reed', \
    '2021-PREXII-Reinhard', '2021-PREXII+CREX-Zhang',\
    '2023-EDF-D4', '2023-EDF-D4-IAS', '2023-EDF-D4-IAS-Rnp'.

    :param constraint: Fix the name of `constraint`. Default value: '2014-IAS'.
    :type constraint: str, optional.

    **Attributes:**
    """
    #
    def __init__( self, constraint = '2014-IAS' ):
        #
        if nuda.env.verb: print("Enter setupEsymLsym()")
        #: Attribute constraint.
        self.constraint = constraint
        if nuda.env.verb: print("constraint:",constraint)
        #
        self = setupEsymLsym.init_self( self )
        #
        constraints, constraints_lower = EsymLsym_constraints()
        #
        if constraint.lower() not in constraints_lower:
            print('setup_EsymLsym.py: The constraint ',constraint,' is not in the list of constraints.')
            print('setup_EsymLsym.py: list of constraints:',constraints)
            print('setup_EsymLsym.py: -- Exit the code --')
            exit()
        #
        if constraint.lower() == '2009-hic':
            #: Attribute providing the full reference to the paper to be citted.
            self.ref = 'Tsang et al., PRL 102, 122701 (2009)'
            #: Attribute providing the label the data is references for figures.
            self.label = 'HIC-2009'
            #: Attribute providing additional notes about the constraint.
            self.note = "constraints inferred from the study of isospin diffusion in HICs"
            csk = 25.0 # MeV
            csp = 35.2 # MeV
            csk2 = csk * 28 / 30.1
            csp2 = csp * 28 / 30.1
            if nuda.env.verb: print('At 28 MeV')
            if nuda.env.verb: print('HIC: Esym(gi):', HIC_Esym(0.16,0.35,csk2,csp2), HIC_Esym(0.16,1.05,csk2,csp2) )
            if nuda.env.verb: print('HIC: Lsym(gi):', HIC_Lsym(0.16,0.35*HIC_xgi(28.0),csk2,csp2), HIC_Lsym(0.16,1.05*HIC_xgi(28.0),csk2,csp2) )
            if nuda.env.verb: print('At 30.1 MeV')
            if nuda.env.verb: print('HIC: Esym(gi):', HIC_Esym(0.16,0.35,csk,csp), HIC_Esym(0.16,1.05,csk,csp) )
            if nuda.env.verb: print('HIC: Lsym(gi):', HIC_Lsym(0.16,0.35,csk,csp), HIC_Lsym(0.16,1.05,csk,csp) )
            if nuda.env.verb: print('At 33.8 MeV')
            csk2 = csk * 33.8 / 30.1
            csp2 = csp * 33.8 / 30.1
            if nuda.env.verb: print('HIC: Esym(gi):', HIC_Esym(0.16,0.35,csk2,csp2), HIC_Esym(0.16,1.05,csk2,csp2) )
            if nuda.env.verb: print('HIC: Lsym(gi):', HIC_Lsym(0.16,0.35*HIC_xgi(33.8),csk2,csp2), HIC_Lsym(0.16,1.05*HIC_xgi(33.8),csk2,csp2) )
            #
            # setup list with contour for HIC contraint in Esym-Lsym coordinates
            #
            self.Esym = np.arange( 25.0, 40.0, 1.0 ) # aEsym
            Lsym1 = HIC_Lsym_bound(self.Esym,0.35,csk,csp)
            Lsym2 = HIC_Lsym_bound(self.Esym,1.05,csk,csp)
            self.Lsym = 0.5 * ( Lsym1 + Lsym2 )
            self.Lsym_err = 0.5 * abs( Lsym1 - Lsym2 )
            self.Lsym_min = self.Lsym - self.Lsym_err
            self.Lsym_max = self.Lsym + self.Lsym_err
            self.plot = 'band_y'
            self.alpha = 0.5
            #
            self.cont_Esym = []
            self.cont_Lsym = []
            for index in np.arange(0,len(self.Esym)-1):
                self.cont_Esym.append((self.Esym[index], self.Esym[index+1]))
                self.cont_Lsym.append((HIC_Lsym_bound(self.Esym[index],0.35,csk,csp), HIC_Lsym_bound(self.Esym[index+1],0.35,csk,csp)))
            self.cont_Esym.append((self.Esym[-1], self.Esym[-1]))
            self.cont_Lsym.append((HIC_Lsym_bound(self.Esym[-1],0.35,csk,csp), HIC_Lsym_bound(self.Esym[-1],1.05,csk,csp)))
    #print('np.arrange2:',np.arange(len(aEsym)-1,0,-1))
            for index in np.arange(len(self.Esym)-1,0,-1):
                self.cont_Esym.append((self.Esym[index], self.Esym[index-1]))
                self.cont_Lsym.append((HIC_Lsym_bound(self.Esym[index],1.05,csk,csp), HIC_Lsym_bound(self.Esym[index-1],1.05,csk,csp)))
            self.cont_Esym.append((self.Esym[0], self.Esym[0]))
            self.cont_Lsym.append((HIC_Lsym_bound(self.Esym[0],1.05,csk,csp), HIC_Lsym_bound(self.Esym[0],0.35,csk,csp)))
            #
        elif constraint.lower() == '2010-rnp':
            #
            file_in = os.path.join(nuda.param.path_data,'corr/EsymLsym/2010-RNP.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'L.W. Chen, C.M. Ko, B.A. Li, J. Xu, Phys. Rev. C 82, 024321 (2010)'
            self.label = 'RNP-2010'
            self.note = "analysis of neutron skin thickness in Sn isotopes"
            self.Esym, Lsym_min, Lsym_max = \
                np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.Lsym = 0.5 * ( Lsym_max + Lsym_min )
            self.Lsym_err = 0.5 * ( Lsym_max - Lsym_min )
            self.Lsym_min = self.Lsym - self.Lsym_err
            self.Lsym_max = self.Lsym + self.Lsym_err
            self.plot = 'band_y'
            self.alpha = 0.5

            # setup list with contour in Esym-Lsym coordinates
            self.cont_Esym = []
            self.cont_Lsym = []
            #print('length(Esym)',len(self.Esym))
            for ind,Esym in enumerate(self.Esym):
                if ind < len(self.Esym)-1:
                    self.cont_Esym.append((self.Esym[ind], self.Esym[ind+1]))
                    self.cont_Lsym.append((Lsym_max[ind], Lsym_max[ind+1]))
            self.cont_Esym.append((self.Esym[-1], self.Esym[-1]))
            self.cont_Lsym.append((Lsym_max[-1], Lsym_min[-1]))
            for ind in np.arange(len(self.Esym)-1,0,-1):
                self.cont_Esym.append((self.Esym[ind], self.Esym[ind-1]))
                self.cont_Lsym.append((Lsym_min[ind], Lsym_min[ind-1]))
            self.cont_Esym.append((self.Esym[0], self.Esym[0]))
            self.cont_Lsym.append((Lsym_min[0], Lsym_max[0]))
            #print('coutour Esym:',self.cont_Esym)
            #print('coutour Lsym:',self.cont_Lsym)
        #
        elif constraint.lower() == '2012-frdm':
            #
            file_in = os.path.join(nuda.param.path_data,'corr/EsymLsym/2012-FRDM.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'P. Moller, W.D. Myers, H. Sagawa, S. Yoshida, Phys. Rev. Lett. 108, 052501 (2012)'
            self.label = 'FRDM-2012'
            self.note = "values of S0 and L inferred from finite-range droplet mass model calculations"
            self.Esym, Lsym_min, Lsym_max = \
                np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.Lsym = 0.5 * ( Lsym_max + Lsym_min )
            self.Lsym_err = 0.5 * ( Lsym_max - Lsym_min )
            self.Lsym_min = self.Lsym - self.Lsym_err
            self.Lsym_max = self.Lsym + self.Lsym_err
            self.plot = 'band_y'
            self.alpha = 0.5

            # setup list with contour in Esym-Lsym coordinates
            self.cont_Esym = []
            self.cont_Lsym = []
            #print('length(Esym)',len(self.Esym))
            for ind,Esym in enumerate(self.Esym):
                if ind < len(self.Esym)-1:
                    self.cont_Esym.append((self.Esym[ind], self.Esym[ind+1]))
                    self.cont_Lsym.append((Lsym_max[ind], Lsym_max[ind+1]))
            self.cont_Esym.append((self.Esym[-1], self.Esym[-1]))
            self.cont_Lsym.append((Lsym_max[-1], Lsym_min[-1]))
            for ind in np.arange(len(self.Esym)-1,0,-1):
                self.cont_Esym.append((self.Esym[ind], self.Esym[ind-1]))
                self.cont_Lsym.append((Lsym_min[ind], Lsym_min[ind-1]))
            self.cont_Esym.append((self.Esym[0], self.Esym[0]))
            self.cont_Lsym.append((Lsym_min[0], Lsym_max[0]))
            #print('coutour Esym:',self.cont_Esym)
            #print('coutour Lsym:',self.cont_Lsym)
        #
        elif constraint.lower() == '2013-ns':
            #
            file_in = os.path.join(nuda.param.path_data,'corr/EsymLsym/2013-NS.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'A.W. Steiner, J.M. Lattimer, E.F. Brown, Astrophys. J. Lett. 765, L5 (2013)'
            self.label = 'NS-2013'
            self.note = "Bayesian analysis of mass and radius measurements of NSs by considering 68\\% and 96\\% confidence values for L."
            self.Esym, Lsym68_min, Lsym68_max, Lsym95_min, Lsym95_max = \
                np.loadtxt( file_in, usecols=(0,1,2,3,4), unpack = True )
            self.Lsym = 0.5 * ( Lsym95_max + Lsym95_min )
            self.Lsym_err = 0.5 * ( Lsym95_max - Lsym95_min )
            self.Lsym_min = self.Lsym - self.Lsym_err
            self.Lsym_max = self.Lsym + self.Lsym_err
            self.plot = 'band_y'
            self.alpha = 0.5

            # setup list with contour in Esym-Lsym coordinates
            self.cont_Esym = []
            self.cont_Lsym = []
            #print('length(Esym)',len(self.Esym))
            for ind,Esym in enumerate(self.Esym):
                if ind < len(self.Esym)-1:
                    self.cont_Esym.append((self.Esym[ind], self.Esym[ind+1]))
                    self.cont_Lsym.append((Lsym95_max[ind], Lsym95_max[ind+1]))
            self.cont_Esym.append((self.Esym[-1], self.Esym[-1]))
            self.cont_Lsym.append((Lsym95_max[-1], Lsym95_min[-1]))
            for ind in np.arange(len(self.Esym)-1,0,-1):
                self.cont_Esym.append((self.Esym[ind], self.Esym[ind-1]))
                self.cont_Lsym.append((Lsym95_min[ind], Lsym95_min[ind-1]))
            self.cont_Esym.append((self.Esym[0], self.Esym[0]))
            self.cont_Lsym.append((Lsym95_min[0], Lsym95_max[0]))
            #print('coutour Esym:',self.cont_Esym)
            #print('coutour Lsym:',self.cont_Lsym)
        #
        elif constraint.lower() == '2014-ias':
            #
            file_in = os.path.join(nuda.param.path_data,'corr/EsymLsym/2014-IAS-err.dat')
            #file_in = os.path.join(nuda.param.path_data,'EsymLsym/2014-IAS.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'Danielewicz and Lee, NPA 922, 1 (2014)'
            self.label = 'IAS-2014'
            self.note = "Constraints from IAS."
            #self.Lsym, self.Esym = \
            #    np.loadtxt( file_in, usecols=(0,1), unpack = True )
            #self.plot = 'contour'
            self.Esym, self.Lsym, self.Lsym_err = \
                np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.Lsym_min = self.Lsym - self.Lsym_err
            self.Lsym_max = self.Lsym + self.Lsym_err
            self.plot = 'band_y'
            self.alpha = 0.5

            # setup list with contour for IAS contraint in Esym-Lsym coordinates
            self.cont_Esym = []
            self.cont_Lsym = []
            #print('length(Esym)',len(self.Esym))
            for ind,Esym in enumerate(self.Esym):
                if ind < len(self.Esym)-1:
                    self.cont_Esym.append((self.Esym[ind], self.Esym[ind+1]))
                    self.cont_Lsym.append((self.Lsym[ind], self.Lsym[ind+1]))
            self.cont_Esym.append((self.Esym[-1], self.Esym[0]))
            self.cont_Lsym.append((self.Lsym[-1], self.Lsym[0]))
            #
        elif constraint.lower() == '2014-ias+rnp':
            #
            file_in = os.path.join(nuda.param.path_data,'corr/EsymLsym/2014-IAS+RNP-err.dat')
            #file_in = os.path.join(nuda.param.path_data,'corr/EsymLsym/2014-IAS+RNP.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'Danielewicz and Lee, NPA 922, 1 (2014)'
            self.label = 'IAS+Rnp-2014'
            self.note = "Constraints from IAS + neutron skin (Rnp)."
            self.Esym, self.Lsym, self.Lsym_err = \
                np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.Lsym_min = self.Lsym - self.Lsym_err
            self.Lsym_max = self.Lsym + self.Lsym_err
            self.plot = 'band_y'
            self.alpha = 0.5
            #self.Lsym, self.Esym = \
            #    np.loadtxt( file_in, usecols=(0,1), unpack = True )
            #self.plot = 'contour'

            # setup list with contour for IAS contraint in Esym-Lsym coordinates
            self.cont_Esym = []
            self.cont_Lsym = []
            for ind,Esym in enumerate(self.Esym):
            #for index in np.arange(0,len(self.Esym)-1):
                if ind < len(self.Esym)-1:
                    self.cont_Esym.append((self.Esym[ind], self.Esym[ind+1]))
                    self.cont_Lsym.append((self.Lsym[ind], self.Lsym[ind+1]))
            self.cont_Esym.append((self.Esym[-1], self.Esym[0]))
            self.cont_Lsym.append((self.Lsym[-1], self.Lsym[0]))
            #
        elif constraint.lower() == '2015-pol-208pb':
            #
            # 208Pb
            self.ref = 'X. Roca-Maza, X. Vi\\~nas, M. Centelles, B.K. Agrawal, G. Col\\`o, N. Paar, J. Piekarewicz, D. Vretenar, Phys. Rev. C 92, 064304 (2015)'
            self.label = 'POL-2015'
            self.note = "Constraints on the electric dipole polarizability deduced in the associated Ref."
            self.Lsym = 5*random.random() + np.arange( 0.0, 130.0, 10.0 )
            POL_Esym_1 = 25.3 + 0.168 * self.Lsym
            POL_Esym_2 = 24.5 + 0.168 * self.Lsym
            POL_Esym_3 = 23.7 + 0.168 * self.Lsym
            self.Esym = POL_Esym_2
            self.Esym_err = 0.5 * ( POL_Esym_1 - POL_Esym_3 )
            self.Esym_min = self.Esym - self.Esym_err
            self.Esym_max = self.Esym + self.Esym_err
            self.plot = 'band_x'
            self.alpha = 0.5
            #
        elif constraint.lower() == '2015-pol-120sn':
            #
            # 120Sn
            self.ref = 'X. Roca-Maza, X. Vi\\~nas, M. Centelles, B.K. Agrawal, G. Col\\`o, N. Paar, J. Piekarewicz, D. Vretenar, Phys. Rev. C 92, 064304 (2015)'
            self.label = 'POL-2015'
            self.note = "Constraints on the electric dipole polarizability deduced in the associated Ref."
            self.Lsym = 5*random.random() + np.arange( 0.0, 130.0, 10.0 )
            POL_Esym_1 = 26.5 + 0.17 * self.Lsym
            POL_Esym_2 = 25.4 + 0.17 * self.Lsym
            POL_Esym_3 = 24.3 + 0.17 * self.Lsym
            self.Esym = POL_Esym_2
            self.Esym_err = 0.5 * ( POL_Esym_1 - POL_Esym_3 )
            self.Esym_min = self.Esym - self.Esym_err
            self.Esym_max = self.Esym + self.Esym_err
            self.plot = 'band_x'
            self.alpha = 0.5
            #
        elif constraint.lower() == '2015-pol-68ni':
            #
            # 68Ni
            self.ref = 'X. Roca-Maza, X. Vi\\~nas, M. Centelles, B.K. Agrawal, G. Col\\`o, N. Paar, J. Piekarewicz, D. Vretenar, Phys. Rev. C 92, 064304 (2015)'
            self.label = 'POL-2015'
            self.note = "Constraints on the electric dipole polarizability deduced in the associated Ref."
            self.Lsym = 5*random.random() + np.arange( 0.0, 130.0, 10.0 )
            POL_Esym_1 = 26.9 + 0.19 * self.Lsym
            POL_Esym_2 = 24.9 + 0.19 * self.Lsym
            POL_Esym_3 = 22.9 + 0.19 * self.Lsym
            self.Esym = POL_Esym_2
            self.Esym_err = 0.5 * ( POL_Esym_1 - POL_Esym_3 )
            self.Esym_min = self.Esym - self.Esym_err
            self.Esym_max = self.Esym + self.Esym_err
            self.plot = 'band_x'
            self.alpha = 0.5
            #
        elif constraint.lower() == '2017-ug':
            #
            self.ref = 'I. Tews, J.M. Lattimer, A. Ohnishi, E.E. Kolomeitsev, Astrophys. J. 848, 105 (2017)'
            self.label = 'UG-2017'
            self.note = "Unitary Gas bound on symmetry energy parameters: only values of (S0, L) to the right of the curve are permitted."
            # Unitary gaz limit
            Esat = -15.5 # MeV
            nsat = 0.157 # fm-3
            Ksat = 270 # MeV
            Kn = Ksat
            Ksym = 0 # MeV
            Qnplus = 0 # MeV
            Qnminus = -750 # MeV
            zeta0 = 0.365
            #
            kFsat = ( 3.0 * nuda.cst.pi2 * nsat )**0.3333
            EUGsat = (3.0/10.0) * nuda.cst.hbc**2 / nuda.cst.mnuc2 * kFsat**2 * zeta0
            if nuda.env.verb: print('EUGsat:',EUGsat)
            #
            self.Esym = np.array([])
            self.Lsym = np.array([])
            for ut in np.arange(0.1,2.0,0.1):
                if ut > 1:
                    Qn = Qnplus
                else:
                    Qn = Qnminus
                self.Esym = np.append( self.Esym, EUGsat * ( ut + 2.0 ) / (3.0*ut**0.3333) \
                    + Kn / 18.0 * ( ut - 1.0 )**2 + Qn/81.0 * (ut - 1.0 )**3 \
                    - Esat )
                self.Lsym = np.append( self.Lsym, 2.0 * EUGsat / ut**0.3333 - \
                    Kn / 3.0 * ( ut - 1.0 ) - Qn / 18.0 * (ut - 1.0 )**2 )
            self.plot = 'curve'
            #
        elif constraint.lower() == '2021-prexii-reed':
            #
            file_in = os.path.join(nuda.param.path_data,'corr/EsymLsym/2021-PREXII-Reed.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'Reed et al., PRL 126, 172503 (2021)'
            self.label = 'PREXII-Reed-2021'
            self.note = "."
            self.Esym, self.Esym_err, self.Lsym, self.Lsym_err = \
                np.loadtxt( file_in, usecols=(0,1,2,3), unpack = True )
            self.Lsym_min = self.Lsym - self.Lsym_err
            self.Lsym_max = self.Lsym + self.Lsym_err
            self.plot = 'point_err_xy'
            #
        elif constraint.lower() == '2021-prexii-reinhard':
            #
            file_in = os.path.join(nuda.param.path_data,'corr/EsymLsym/2021-PREXII-Reinhard.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'Reinhard et al., PRL 127, 232501 (2021)'
            self.label = 'PREXII-Reinhard-2021'
            self.note = "."
            self.Esym, self.Esym_err, self.Lsym, self.Lsym_err = \
                np.loadtxt( file_in, usecols=(0,1,2,3), unpack = True )
            self.Lsym_min = self.Lsym - self.Lsym_err
            self.Lsym_max = self.Lsym + self.Lsym_err
            self.plot = 'point_err_xy'
            #
        elif constraint.lower() == '2023-prexii+crex-zhang':
            #
            file_in = os.path.join(nuda.param.path_data,'corr/EsymLsym/2023-PREXII-Zhang.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'Z. Zhang, L.W. Chen, Phys. Rev. C 108, 024317 (2023).'
            self.label = 'PREXII+CREX-Zhang-2023'
            self.note = "."
            self.Esym, self.Esym_err, self.Lsym, self.Lsym_err = \
                np.loadtxt( file_in, usecols=(0,1,2,3), unpack = True )
            self.Lsym_min = self.Lsym - self.Lsym_err
            self.Lsym_max = self.Lsym + self.Lsym_err
            self.plot = 'point_err_xy'
            #
        elif constraint.lower() == '2023-edf-d4':
            #
            self.ref = 'B.V. Carlson, M. Dutra, O. Lourenco, K. Margueron, Phys. Rev. C 107, 0353805 (2022).'
            self.label = 'EDF(D4)-2023'
            self.note = "."
            # D4:
            self.Esym = [ 29.85, 31.97, 33.06, 37.26, 39.42, 38.58, 36.44, 30.97, 29.85 ]
            self.Lsym = [ 50.3, 45.36, 55.45, 99.14, 126.6, 124.57, 115.71, 61.79, 50.3 ]
            self.plot = 'contour'
            #
        elif constraint.lower() == '2023-edf-d4-ias':
            #
            self.ref = 'B.V. Carlson, M. Dutra, O. Lourenco, K. Margueron, Phys. Rev. C 107, 0353805 (2022).'
            self.label = 'EDF(D4+IAS)-2023'
            self.note = "."
            # D4+IAS:
            self.Esym = [ 29.85, 31.97, 33.06, 33.96, 34.54, 30.97, 29.85 ]
            self.Lsym = [ 50.3, 45.36, 55.45, 71.55, 88.03, 61.79, 50.3 ]
            self.plot = 'contour'
            #
        elif constraint.lower() == '2023-edf-d4-ias-rnp':
            #
            self.ref = 'B.V. Carlson, M. Dutra, O. Lourenco, K. Margueron, Phys. Rev. C 107, 0353805 (2022).'
            self.label = 'EDF(D4+IAS+Rnp)-2023'
            self.note = "."
            # D4sym (D4+IAS+\Delta r_{np}):
            self.Esym = [ 29.85, 32.01, 32.54, 32.74, 31.98, 30.97, 29.85 ]
            self.Lsym = [ 50.3, 48.15, 61.52, 70.45, 67.44, 61.79, 50.3 ]
            self.plot = 'contour'
            #
        else:
            #
            print('setup_EsymLsym.py: The variable constraint:',constraint)
            print('setup_EsymLsym.py: does not fit with the options in the code')

        if nuda.env.verb: print("Exit setupEsymLsym()")
    #
    def print_outputs( self ):
        """
        Method which print outputs on terminal's screen.
        """
        print("")
        #
        if nuda.env.verb: print("Enter print_outputs()")
        #
        print("   constraint:",self.constraint)
        print("   ref:",self.ref)
        print("   label:",self.label)
        print("   note:",self.note)
        print("   plot:",self.plot)
        #
        if nuda.env.verb: print("Exit print_outputs()")
        #
    def init_self( self ):
        """
        Initialize variables in self.
        """
        #
        if nuda.env.verb: print("Enter init_self()")
        #
        #: Attribute providing the full reference to the paper to be citted.
        self.ref = None
        #: Attribute providing the label the data is references for figures.
        self.label = None
        #: Attribute providing additional notes about the constraint.
        self.note = None
        #: Attribute the plot alpha
        self.alpha = 0.5
        self.plot = None
        #
        #: Attribute Esym.
        self.Esym = None
        #: Attribute max of Esym.
        self.Esym_max = None
        #: Attribute min of Esym.
        self.Esym_min = None
        #: Attribute with uncertainty in Esym.
        self.Esym_err = None
        #: Attribute Lsym.
        self.Lsym = None
        #: Attribute max of Lsym.
        self.Lsym_max = None
        #: Attribute min of Lsym.
        self.Lsym_min = None
        #: Attribute with uncertainty in Lsym.
        self.Lsym_err = None
        #
        if nuda.env.verb: print("Exit init_self()")
        #
        return self        
