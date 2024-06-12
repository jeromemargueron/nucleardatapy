import os
import sys
import numpy as np  # 1.15.0
import random

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nudy

class SetupEsymDen():
    """
    Instantiate the values of Esym and Lsym from the constraint.
    
    :param constraint: name of the model: '2008-AFDMC', ...
    :type constraint: string().
    :returns: constraint, ref, label, note, Esym, Lsym.
    """
    #
    def __init__( self, constraint = '2014-IAS' ):
        #
        if nudy.env.verb: print("Enter SetupEsymLsym()")
        #
        self.constraint = constraint
        if nudy.env.verb: print("constraint:",constraint)
        self.Esym = []
        self.Esym_err = []
        self.Lsym = []
        self.Lsym_err = []
        #
        if constraint.lower() == '2010-rnp':
            #
            file_in = os.path.join(nudy.param.path_data,'EsymLsym/2010-RNP.dat')
            if nudy.env.verb: print('Reads file:',file_in)
            self.ref = 'L.W. Chen, C.M. Ko, B.A. Li, J. Xu, Phys. Rev. C 82, 024321 (2010)'
            self.label = 'RNP-2010'
            self.note = "analysis of neutron skin thickness in Sn isotopes"
            self.Esym, Lsym_min, Lsym_max = \
                np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.Lsym = 0.5 * ( Lsym_max + Lsym_min )
            self.Lsym_err = 0.5 * ( Lsym_max - Lsym_min )
            # setup list with contour in Esym-Lsym coordinates
            self.cont_Esym = []
            self.cont_Lsym = []
            print('length(Esym)',len(self.Esym))
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
            print('coutour Esym:',self.cont_Esym)
            print('coutour Lsym:',self.cont_Lsym)
        #
        elif constraint.lower() == '2012-frdm':
            #
            file_in = os.path.join(nudy.param.path_data,'EsymLsym/2012-FRDM.dat')
            if nudy.env.verb: print('Reads file:',file_in)
            self.ref = 'P. Moller, W.D. Myers, H. Sagawa, S. Yoshida, Phys. Rev. Lett. 108, 052501 (2012)'
            self.label = 'FRDM-2012'
            self.note = "values of S0 and L inferred from finite-range droplet mass model calculations"
            self.Esym, Lsym_min, Lsym_max = \
                np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.Lsym = 0.5 * ( Lsym_max + Lsym_min )
            self.Lsym_err = 0.5 * ( Lsym_max - Lsym_min )
            # setup list with contour in Esym-Lsym coordinates
            self.cont_Esym = []
            self.cont_Lsym = []
            print('length(Esym)',len(self.Esym))
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
            print('coutour Esym:',self.cont_Esym)
            print('coutour Lsym:',self.cont_Lsym)
        #
        elif constraint.lower() == '2013-ns':
            #
            file_in = os.path.join(nudy.param.path_data,'EsymLsym/2013-NS.dat')
            if nudy.env.verb: print('Reads file:',file_in)
            self.ref = 'A.W. Steiner, J.M. Lattimer, E.F. Brown, Astrophys. J. Lett. 765, L5 (2013)'
            self.label = 'NS-2013'
            self.note = "Bayesian analysis of mass and radius measurements of NSs by considering 68\% and 96\% confidence values for L."
            self.Esym, Lsym68_min, Lsym68_max, Lsym95_min, Lsym95_max = \
                np.loadtxt( file_in, usecols=(0,1,2,3,4), unpack = True )
            self.Lsym = 0.5 * ( Lsym95_max + Lsym95_min )
            self.Lsym_err = 0.5 * ( Lsym95_max - Lsym95_min )
            # setup list with contour in Esym-Lsym coordinates
            self.cont_Esym = []
            self.cont_Lsym = []
            print('length(Esym)',len(self.Esym))
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
            print('coutour Esym:',self.cont_Esym)
            print('coutour Lsym:',self.cont_Lsym)
        #
        elif constraint.lower() == '2014-ias':
            #
            file_in = os.path.join(nudy.param.path_data,'EsymLsym/2014-IAS.dat')
            if nudy.env.verb: print('Reads file:',file_in)
            self.ref = 'Danielewicz and Lee, NPA 922, 1 (2014)'
            self.label = 'IAS-2014'
            self.note = "write here notes about this constraint."
            self.Esym, self.Lsym = \
                np.loadtxt( file_in, usecols=(0,1), unpack = True )
            # setup list with contour for IAS contraint in Esym-Lsym coordinates
            self.cont_Esym = []
            self.cont_Lsym = []
            print('length(Esym)',len(self.Esym))
            for ind,Esym in enumerate(self.Esym):
                if ind < len(self.Esym)-1:
                    self.cont_Esym.append((self.Esym[ind], self.Esym[ind+1]))
                    self.cont_Lsym.append((self.Lsym[ind], self.Lsym[ind+1]))
            self.cont_Esym.append((self.Esym[-1], self.Esym[0]))
            self.cont_Lsym.append((self.Lsym[-1], self.Lsym[0]))
            #
        elif constraint.lower() == '2014-ias+rnp':
            #
            file_in = os.path.join(nudy.param.path_data,'EsymLsym/2014-IAS+RNP.dat')
            if nudy.env.verb: print('Reads file:',file_in)
            self.ref = 'Danielewicz and Lee, NPA 922, 1 (2014)'
            self.label = 'IAS+Rnp-2014'
            self.note = "write here notes about this constraint."
            self.Esym, self.Lsym = \
                np.loadtxt( file_in, usecols=(0,1), unpack = True )
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
            self.ref = 'X. Roca-Maza, X. Vi\~nas, M. Centelles, B.K. Agrawal, G. Col\`o, N. Paar, J. Piekarewicz, D. Vretenar, Phys. Rev. C 92, 064304 (2015)'
            self.label = 'POL-2015'
            self.note = "Constraints on the electric dipole polarizability deduced in the associated Ref."
            self.Lsym = 5*random.random() + np.arange( 0.0, 130.0, 10.0 )
            POL_Esym_1 = 25.3 + 0.168 * self.Lsym
            POL_Esym_2 = 24.5 + 0.168 * self.Lsym
            POL_Esym_3 = 23.7 + 0.168 * self.Lsym
            self.Esym = POL_Esym_2
            self.Esym_err = 0.5 * ( POL_Esym_1 - POL_Esym_3 )
            #
        elif constraint.lower() == '2015-pol-120sn':
            #
            # 120Sn
            self.ref = 'X. Roca-Maza, X. Vi\~nas, M. Centelles, B.K. Agrawal, G. Col\`o, N. Paar, J. Piekarewicz, D. Vretenar, Phys. Rev. C 92, 064304 (2015)'
            self.label = 'POL-2015'
            self.note = "Constraints on the electric dipole polarizability deduced in the associated Ref."
            self.Lsym = 5*random.random() + np.arange( 0.0, 130.0, 10.0 )
            POL_Esym_1 = 26.5 + 0.17 * self.Lsym
            POL_Esym_2 = 25.4 + 0.17 * self.Lsym
            POL_Esym_3 = 24.3 + 0.17 * self.Lsym
            self.Esym = POL_Esym_2
            self.Esym_err = 0.5 * ( POL_Esym_1 - POL_Esym_3 )
            #
        elif constraint.lower() == '2015-pol-68ni':
            #
            # 68Ni
            self.ref = 'X. Roca-Maza, X. Vi\~nas, M. Centelles, B.K. Agrawal, G. Col\`o, N. Paar, J. Piekarewicz, D. Vretenar, Phys. Rev. C 92, 064304 (2015)'
            self.label = 'POL-2015'
            self.note = "Constraints on the electric dipole polarizability deduced in the associated Ref."
            self.Lsym = 5*random.random() + np.arange( 0.0, 130.0, 10.0 )
            POL_Esym_1 = 26.9 + 0.19 * self.Lsym
            POL_Esym_2 = 24.9 + 0.19 * self.Lsym
            POL_Esym_3 = 22.9 + 0.19 * self.Lsym
            self.Esym = POL_Esym_2
            self.Esym_err = 0.5 * ( POL_Esym_1 - POL_Esym_3 )
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
            kFsat = ( 3.0 * pi**2 * nsat )**0.3333
            EUGsat = (3.0/10.0) * hbc**2 / mnc2 * kFsat**2 * zeta0
            if nudy.env.verb: print('EUGsat:',EUGsat)
            #
            self.Esym = np.array([])
            self.Lsym = np.array([])
            for ut in np.arange(0.1,2.0,0.1):
                if ut > 1:
                    Qn = Qnplus
                else:
                    Qn = Qnminus
                self.Esym.append( EUGsat * ( ut + 2.0 ) / (3.0*ut**0.3333) \
                    + Kn / 18.0 * ( ut - 1.0 )**2 + Qn/81.0 * (ut - 1.0 )**3 \
                    - Esat )
                self.Lsym.append( 2.0 * EUGsat / ut**0.3333 - \
                    Kn / 3.0 * ( ut - 1.0 ) - Qn / 18.0 * (ut - 1.0 )**2 )
            #
        elif constraint.lower() == '2021-prexii-reed':
            #
            file_in = os.path.join(nudy.param.path_data,'EsymLsym/2021-PREXII-Reed.dat')
            if nudy.env.verb: print('Reads file:',file_in)
            self.ref = 'Reed et al., PRL 126, 172503 (2021)'
            self.label = 'PREXII-Reed'
            self.note = "."
            self.Esym, self.Esym_err, self.Lsym, self.Lsym_err = \
                np.loadtxt( file_in, usecols=(0,1,2,3), unpack = True )
            #
        elif constraint.lower() == '2021-prexii-reinhard':
            #
            file_in = os.path.join(nudy.param.path_data,'EsymLsym/2021-PREXII-Reinhard.dat')
            if nudy.env.verb: print('Reads file:',file_in)
            self.ref = 'Reinhard et al., PRL 127, 232501 (2021)'
            self.label = 'PREXII-Reinhard'
            self.note = "."
            self.Esym, self.Esym_err, self.Lsym, self.Lsym_err = \
                np.loadtxt( file_in, usecols=(0,1,2,3), unpack = True )
            #
        elif constraint.lower() == '2021-prexii-zhang':
            #
            file_in = os.path.join(nudy.param.path_data,'EsymLsym/2022-PREXII-Zhang.dat')
            if nudy.env.verb: print('Reads file:',file_in)
            self.ref = 'Zhang and Chen, arXiv:2207.03328 (July 2022)'
            self.label = 'PREXII-Zhang'
            self.note = "."
            self.Esym, self.Esym_err, self.Lsym, self.Lsym_err = \
                np.loadtxt( file_in, usecols=(0,1,2,3), unpack = True )
            #
        else:
            #
            print('The variable constraint:',constraint)
            print('does not fit with the options in the code')
            #
        nsat = 0.16
        PREX1_den = []
        PREX1_Esym_min = []
        PREX1_Esym_max = []
        with open('prex2.dat','w') as f:
            for k in range(-6,6):
                den = nsat + 0.01 * k
                PREX1_den.append( den )
                e_min = 100.0
                e_max = -100.0
                # loop over the empirical parameters
                for i in range(-1,2):
                    Esym = 38.1 + 4.7*i
                    for j in range(-1,2):
                        Lsym = 106 + 37*j
                        #print(i,j,Esym,Lsym)
                        esym = Esym + Lsym*(den-nsat)/(3*nsat)
                        if (esym > e_max): e_max = esym
                        if (esym < e_min): e_min = esym
                print(k,den,e_min,e_max)
                f.write(str(den)+'  '+str(e_min)+'  '+str(e_max)+'\n')
                PREX1_Esym_min.append( e_min )
                PREX1_Esym_max.append( e_max )

        if nudy.env.verb: print("Exit SetupEsymLsym()")
