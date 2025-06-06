import os
import sys
import math
import numpy as np  # 1.15.0

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda


def crust_models():
    """
    Return a list of the tables available in this toolkit for the experimental masses and
    print them all on the prompt. These tables are the following
    ones: 'Negele-Vautheron-1973'.

    :return: The list of tables.
    :rtype: list[str].
    """
    #
    if nuda.env.verb: print("\nEnter models_crust()")
    #
    models = [ '1973-Negele-Vautherin', '2020-MVCD-D1S', '2020-MVCD-D1M', '2020-MVCD-D1MS',\
    '2022-crustGMRS-BSK14', '2022-crustGMRS-BSK16', '2022-crustGMRS-DHSL59', '2022-crustGMRS-DHSL69',\
    '2022-crustGMRS-F0', '2022-crustGMRS-H1', '2022-crustGMRS-H2', '2022-crustGMRS-H3', \
    '2022-crustGMRS-H4', '2022-crustGMRS-H5', '2022-crustGMRS-H7', '2022-crustGMRS-LNS5', \
    '2022-crustGMRS-RATP', '2022-crustGMRS-SGII', '2022-crustGMRS-SLY5' ]
    #
    #print('crust models available in the toolkit:',models)
    models_lower = [ item.lower() for item in models ]
    #print('crust models available in the toolkit:',models_lower)
    #
    if nuda.env.verb: print("Exit crust_models()")
    #
    return models, models_lower


class setupCrust():
    """
    Instantiate the properties of the crust for the existing models.

    This choice is defined in the variable `crust`.

    `crust` can chosen among the following ones: 'Negele-Vautherin-1973'.

    :param crust: Fix the name of `crust`. Default value: 'Negele-Vautherin-1973'.
    :type crust: str, optional. 

    **Attributes:**
    """
    def __init__(self, model = '1973-Negele-Vautherin'):
        #
        if nuda.env.verb: print("Enter setupCrusts()")
        #
        models, models_lower = crust_models()
        if model.lower() not in models_lower:
            print('Crust model ',model,' is not in the list of crusts.')
            print('list of crust models:',models)
            print('-- Exit the code --')
            exit()
        self.model = model
        if nuda.env.verb: print("model:",model)
        #
        # initialize self
        #
        self = setupCrust.init_self( self )
        #
        if model.lower()=='1973-negele-vautherin':
            #
            file_in = nuda.param.path_data+'crust/1973-Negele-Vautherin.dat'
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref= 'Negele and Vautherin, Nuc. Phys. A 207, 298 (1973).'
            self.note = "write here notes about this EOS."
            self.label = 'NV-1973'
            self.linestyle = 'solid'
            self.latexCite = 'JWNegele:1973'
            self.ncl = 0.17 # in fm-3
            self.den_cgs, self.N, self.Z, self.mu_n, self.mu_p, self.n_g, self.xpn_bound, self.e2a_int2, \
                self.e2a_int_g = np.loadtxt( file_in, usecols=(0,1,2,3,4,5,6,7,8), unpack = True )
            self.den = self.den_cgs * 1.e-39 # in fm-3
            self.N = np.array([ int(item) for item in self.N ])
            self.Z = np.array([ int(item) for item in self.Z ])
            self.A = self.N + self.Z
            self.Z_bound = self.Z
            self.N_bound = [ int(item) for item in ( self.Z_bound * self.xpn_bound ) ]
            self.A_bound = self.Z_bound + self.N_bound
            self.xp = self.Z / self.A
            self.xn = self.N / self.A
            self.xp_bound = self.Z_bound / self.A_bound
            self.xn_bound = self.N_bound / self.A_bound
            self.I_bound = ( self.N_bound - self.Z_bound ) / self.A_bound
            self.N_g = self.N - self.N_bound
            # cluster volume and radius
            self.Vcl = 2 * self.Z_bound / ( (1-self.I_bound) * self.ncl )
            self.Rcl = ( 3 / ( 4 * nuda.cst.pi ) * self.Vcl )**nuda.cst.third
            # unbound (gas) neutrons
            self.VWS = self.Vcl + self.N_g / self.n_g
            self.RWS = ( 3 / ( 4 * nuda.cst.pi ) * self.VWS )**nuda.cst.third
            # volume fraction
            self.u = self.Vcl / self.VWS
            #
            self.e2a_tot = self.e2a_int2 + nuda.cst.mnuc2
            self.e2a_rm = self.xn * nuda.cst.mnc2 + self.xp * ( nuda.cst.mpc2 + nuda.cst.mec2 )
            self.e2a_int = self.e2a_tot - self.e2a_rm
            #
        elif '2020-mvcd' in model.lower():
            #
            # Note: N_bound or N_g cannot be determined from the tables (Jerome).
            # It is right?
            #
            if model.lower()=='2020-mvcd-d1s':
                file_in = nuda.param.path_data+'crust/2020-MVCD-D1S.dat'
                self.label = 'MVCD-D1S-2020'
            elif model.lower()=='2020-mvcd-d1m':
                file_in = nuda.param.path_data+'crust/2020-MVCD-D1M.dat'
                self.label = 'MVCD-D1M-2020'
            elif model.lower()=='2020-mvcd-d1ms':
                file_in = nuda.param.path_data+'crust/2020-MVCD-D1MS.dat'
                self.label = 'MVCD-D1M$^*$-2020'
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'C. Mondal, X. Viñas, M. Centelles, and J.N. De, Phys. Rev. C 102, 015802 (2020).'
            self.note = "semiclassical variational Wigner-Kirkwood method along with shell and pairing corrections calculated with the Strutinsky integral method and the BCS approximation."
            self.linestyle = 'dashed'
            self.latexCite = 'CMondal:2020'
            self.ncl = 0.16 # in fm-3
            self.den, self.RWS, self.N, self.Z, self.e2a_int2, self.pre, self.mu_n, self.mu_p, self.mu_e \
                = np.loadtxt( file_in, usecols=(0,1,2,3,4,5,6,7,8), unpack = True )
            self.den_cgs = self.den / 1.e-39 # in cm-3
            self.N = np.array([ int(item) for item in self.N ])
            self.Z = np.array([ int(item) for item in self.Z ])
            self.A = self.N + self.Z
            self.xp = self.Z / self.A
            self.xn = self.N / self.A
            #self.N_bound = [ int(item) for item in self.Z * self.xpn_bound ]
            #self.xn_bound = self.N_bound / self.A
            #self.N_g = self.N - self.N_bound
            self.e2a_tot = self.e2a_int2 + nuda.cst.mnuc2_approx
            self.e2a_rm = self.xn * nuda.cst.mnc2 + self.xp * ( nuda.cst.mpc2 + nuda.cst.mec2 )
            self.e2a_int = self.e2a_tot - self.e2a_rm
            #
        elif '2022-crustgmrs' in model.lower():
            #
            #
            if model.lower()=='2022-crustgmrs-bsk14':
                file_in = nuda.param.path_data+'crust/2022-crustGMRS-BSK14.dat'
                self.label = 'GMRS BSK14 2022'
                # Outer-Inner Crust (OIC) Transition :
                self.nb_oic = 2.5617840312066730E-004 # in fm-3
                self.rho_oic = 7.1679927159410228 # in MeV/fm3
                self.pre_oic = 5.2333969704018517E-004 # in MeV/fm3
                self.mu_n_oic = 2.7005802403942604E-004 # in MeV
                # Crust-Core Transition:
                self.nb_cc = 7.6209998100288209E-002 # in fm-3
                self.rho_cc = 15.799976089478367 # in MeV/fm3
                self.pre_cc = 0.32687267610704895 # in MeV/fm3
                self.mu_n_cc = 7.6209998100288209E-002 # in MeV
            elif model.lower()=='2022-crustgmrs-bsk16':
                file_in = nuda.param.path_data+'crust/2022-crustGMRS-BSK16.dat'
                self.label = 'GMRS BSK16 2022'
                # Outer-Inner Crust (OIC) Transition :
                self.nb_oic = 2.5282142292259004E-004 # in fm-3
                self.rho_oic = 7.1476234649744690 # in MeV/fm3
                self.pre_oic = 5.1738808103152147E-004 # in MeV/fm3
                self.mu_n_oic = 2.6651916429173218E-004 # in MeV
                # Crust-Core Transition:
                self.nb_cc = 8.4609997888086361E-002 # in fm-3
                self.rho_cc = 16.920900617363277 # in MeV/fm3
                self.pre_cc = 0.36795626298336570 # in MeV/fm3
                self.mu_n_cc = 8.4609997888086361E-002 # in MeV
            elif model.lower()=='2022-crustgmrs-dhsl59':
                file_in = nuda.param.path_data+'crust/2022-crustGMRS-DHSL59.dat'
                self.label = 'GMRS DHSL59 2022'
                # Outer-Inner Crust (OIC) Transition :
                self.nb_oic = 2.6651916429173218E-004 # in fm-3
                self.rho_oic = 7.7840639496076998 # in MeV/fm3
                self.pre_oic = 6.3684106061817061E-004 # in MeV/fm3
                self.mu_n_oic = 2.8095904260657669E-004 # in MeV
                # Crust-Core Transition:
                self.nb_cc = 7.2109998203862921E-002 # in fm-3
                self.rho_cc = 17.733669529186933 # in MeV/fm3
                self.pre_cc = 0.33617646422062142 # in MeV/fm3
                self.mu_n_cc = 7.2109998203862921E-002 # in MeV
            elif model.lower()=='2022-crustgmrs-dhsl69':
                file_in = nuda.param.path_data+'crust/2022-crustGMRS-DHSL69.dat'
                self.label = 'GMRS DHSL69 2022'
                # Outer-Inner Crust (OIC) Transition :
                self.nb_oic = 2.4301212474202996E-004 # in fm-3
                self.rho_oic = 7.3077129271105594 # in MeV/fm3
                self.pre_oic = 5.6022465054447420E-004 # in MeV/fm3
                self.mu_n_oic = 2.5617840312066730E-004 # in MeV
                # Crust-Core Transition:
                self.nb_cc = 7.3209998176074584E-002 # in fm-3
                self.rho_cc = 17.399615979167670 # in MeV/fm3
                self.pre_cc = 0.38035277580973315 # in MeV/fm3
                self.mu_n_cc = 7.3209998176074584E-002 # in MeV
            elif model.lower()=='2022-crustgmrs-f0':
                file_in = nuda.param.path_data+'crust/2022-crustGMRS-F0.dat'
                self.label = 'GMRS F0 2022'
                # Outer-Inner Crust (OIC) Transition :
                self.nb_oic = 2.4950843283419027E-004 # in fm-3
                self.rho_oic = 7.0656453875088161 # in MeV/fm3
                self.pre_oic = 5.1979526696749431E-004 # in MeV/fm3
                self.mu_n_oic = 2.6302667801639999E-004 # in MeV
                # Crust-Core Transition:
                self.nb_cc = 8.3309997920927123E-002 # in fm-3
                self.rho_cc = 18.078177464065167 # in MeV/fm3
                self.pre_cc = 0.33181818756433845 # in MeV/fm3
                self.mu_n_cc = 8.3309997920927123E-002 # in MeV
            elif model.lower()=='2022-crustgmrs-h1':
                file_in = nuda.param.path_data+'crust/2022-crustGMRS-H1.dat'
                self.label = 'GMRS H1 2022'
                # Outer-Inner Crust (OIC) Transition :
                self.nb_oic = 2.5957995753211628E-004 # in fm-3
                self.rho_oic = 7.0757265666560816 # in MeV/fm3
                self.pre_oic = 5.2925404120069590E-004 # in MeV/fm3
                self.mu_n_oic = 2.7364387300962906E-004 # in MeV
                # Crust-Core Transition:
                self.nb_cc = 9.5909997602624350E-002 # in fm-3
                self.rho_cc = 17.803660783830789 # in MeV/fm3
                self.pre_cc = 0.48159809254574409 # in MeV/fm3
                self.mu_n_cc = 9.5909997602624350E-002 # in MeV
            elif model.lower()=='2022-crustgmrs-h2':
                file_in = nuda.param.path_data+'crust/2022-crustGMRS-H2.dat'
                self.label = 'GMRS H2 2022'
                # Outer-Inner Crust (OIC) Transition :
                self.nb_oic = 2.4301212474202996E-004 # in fm-3
                self.rho_oic = 6.7775868042313050 # in MeV/fm3
                self.pre_oic = 5.0750488249204384E-004 # in MeV/fm3
                self.mu_n_oic = 2.5617840312066730E-004 # in MeV
                # Crust-Core Transition:
                self.nb_cc = 9.2909997678410725E-002 # in fm-3
                self.rho_cc = 17.632170792314291 # in MeV/fm3
                self.pre_cc = 0.48032175761400209 # in MeV/fm3
                self.mu_n_cc = 9.2909997678410725E-002 # in MeV
            elif model.lower()=='2022-crustgmrs-h3':
                file_in = nuda.param.path_data+'crust/2022-crustGMRS-H3.dat'
                self.label = 'GMRS H3 2022'
                # Outer-Inner Crust (OIC) Transition :
                self.nb_oic = 2.4623885640591057E-004 # in fm-3
                self.rho_oic = 6.9757456948608496 # in MeV/fm3
                self.pre_oic = 5.2473617319924773E-004 # in MeV/fm3
                self.mu_n_oic = 2.5957995753211628E-004 # in MeV
                # Crust-Core Transition:
                self.nb_cc = 8.4509997890612573E-002 # in fm-3
                self.rho_cc = 17.236262111228385 # in MeV/fm3
                self.pre_cc = 0.40705940455120337 # in MeV/fm3
                self.mu_n_cc = 8.4509997890612573E-002 # in MeV
            elif model.lower()=='2022-crustgmrs-h4':
                file_in = nuda.param.path_data+'crust/2022-crustGMRS-H4.dat'
                self.label = 'GMRS H4 2022'
                # Outer-Inner Crust (OIC) Transition :
                self.nb_oic = 2.5282142292259004E-004 # in fm-3
                self.rho_oic = 7.1798191275380834 # in MeV/fm3
                self.pre_oic = 5.4763060342489047E-004 # in MeV/fm3
                self.mu_n_oic = 2.6651916429173218E-004 # in MeV
                # Crust-Core Transition:
                self.nb_cc = 9.0609997736513612E-002 # in fm-3
                self.rho_cc = 18.131463559875652 # in MeV/fm3
                self.pre_cc = 0.47616516763123967 # in MeV/fm3
                self.mu_n_cc = 9.0609997736513612E-002 # in MeV
            elif model.lower()=='2022-crustgmrs-h5':
                file_in = nuda.param.path_data+'crust/2022-crustGMRS-H5.dat'
                self.label = 'GMRS H5 2022'
                # Outer-Inner Crust (OIC) Transition :
                self.nb_oic = 2.8468963604916567E-004 # in fm-3
                self.rho_oic = 7.9585404850864840 # in MeV/fm3
                self.pre_oic = 6.7714839441802323E-004 # in MeV/fm3
                self.mu_n_oic = 3.0011398166037865E-004 # in MeV
                # Crust-Core Transition:
                self.nb_cc = 8.7009997827457261E-002 # in fm-3
                self.rho_cc = 19.069132247958592 # in MeV/fm3
                self.pre_cc = 0.46337573665856840 # in MeV/fm3
                self.mu_n_cc = 8.7009997827457261E-002 # in MeV
            elif model.lower()=='2022-crustgmrs-h7':
                file_in = nuda.param.path_data+'crust/2022-crustGMRS-H7.dat'
                self.label = 'GMRS H7 2022'
                # Outer-Inner Crust (OIC) Transition :
                self.nb_oic = 3.2914459584803760E-004 # in fm-3
                self.rho_oic = 8.4098882517442597 # in MeV/fm3
                self.pre_oic = 8.5126111019145174E-004 # in MeV/fm3
                self.mu_n_oic = 3.4697748949628541E-004 # in MeV
                # Crust-Core Transition:
                self.nb_cc = 8.3109997925979548E-002 # in fm-3
                self.rho_cc = 19.885261960955020 # in MeV/fm3
                self.pre_cc = 0.48143960493062543 # in MeV/fm3
                self.mu_n_cc = 8.3109997925979548E-002 # in MeV
            elif model.lower()=='2022-crustgmrs-lns5':
                file_in = nuda.param.path_data+'crust/2022-crustGMRS-LNS5.dat'
                self.label = 'GMRS LNS5 2022'
                # Outer-Inner Crust (OIC) Transition :
                self.nb_oic = 2.6651916429173218E-004 # in fm-3
                self.rho_oic = 7.2220830810240075 # in MeV/fm3
                self.pre_oic = 5.3768304050759832E-004 # in MeV/fm3
                self.mu_n_oic = 2.8095904260657669E-004 # in MeV
                # Crust-Core Transition:
                self.nb_cc = 7.0409998246808533E-002 # in fm-3
                self.rho_cc = 14.391278079363289 # in MeV/fm3
                self.pre_cc = 0.26627562388273884 # in MeV/fm3
                self.mu_n_cc = 7.0409998246808533E-002 # in MeV
            elif model.lower()=='2022-crustgmrs-ratp':
                file_in = nuda.param.path_data+'crust/2022-crustGMRS-RATP.dat'
                self.label = 'GMRS RATP 2022'
                # Outer-Inner Crust (OIC) Transition :
                self.nb_oic = 2.5617840312066730E-004 # in fm-3
                self.rho_oic = 7.1702995055472227 # in MeV/fm3
                self.pre_oic = 5.1984846488072468E-004 # in MeV/fm3
                self.mu_n_oic = 2.7005802403942604E-004 # in MeV
                # Crust-Core Transition:
                self.nb_cc = 8.6009997852719386E-002 # in fm-3
                self.rho_cc = 16.557394274307612 # in MeV/fm3
                self.pre_cc = 0.35277408994086884 # in MeV/fm3
                self.mu_n_cc = 8.6009997852719386E-002 # in MeV
            elif model.lower()=='2022-crustgmrs-sgii':
                file_in = nuda.param.path_data+'crust/2022-crustGMRS-SGII.dat'
                self.label = 'GMRS SGII 2022'
                # Outer-Inner Crust (OIC) Transition :
                self.nb_oic = 2.6651916429173218E-004 # in fm-3
                self.rho_oic = 7.2454048591257214 # in MeV/fm3
                self.pre_oic = 5.3291857700309511E-004 # in MeV/fm3
                self.mu_n_oic = 2.8095904260657669E-004 # in MeV
                # Crust-Core Transition:
                self.nb_cc = 6.5309998375645370E-002 # in fm-3
                self.rho_cc = 13.413876317015074 # in MeV/fm3
                self.pre_cc = 0.20198467236572187 # in MeV/fm3
                self.mu_n_cc = 6.5309998375645370E-002 # in MeV
            elif model.lower()=='2022-crustgmrs-sly5':
                file_in = nuda.param.path_data+'crust/2022-crustGMRS-SLY5.dat'
                self.label = 'GMRS SLy5 2022'
                # Outer-Inner Crust (OIC) Transition :
                self.nb_oic = 2.4623885640591057E-004 # in fm-3
                self.rho_oic = 7.0872886477160133 # in MeV/fm3
                self.pre_oic = 5.1240271689332565E-004 # in MeV/fm3
                self.mu_n_oic = 2.5957995753211628E-004 # in MeV
                # Crust-Core Transition:
                self.nb_cc = 7.6309998097761997E-002 # in fm-3
                self.rho_cc = 17.103178025699933 # in MeV/fm3
                self.pre_cc = 0.31728157118252842 # in MeV/fm3
                self.mu_n_cc = 7.6309998097761997E-002 # in MeV
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'G. Grams, J. Margueron, R. Somasundaram, and S. Reddy, EPJA 58, 56 (2022).'
            self.note = "."
            self.linestyle = 'dotted'
            self.latexCite = 'GGrams:2022'
            self.den, self.Acl, self.Zcl, self.ncl, self.xe, self.ng, self.VWS, self.e2a_int2, self.pre, self.mu_n, self.mu_p \
                = np.loadtxt( file_in, usecols=(0,1,2,3,4,5,6,7,8,9,10), unpack = True )
            self.den_cgs = self.den / 1.e-39 # in cm-3
            # bound nucleons
            self.A_bound = np.array([ int(item) for item in self.Acl ])
            self.Z_bound = np.array([ int(item) for item in self.Zcl ])
            self.N_bound = self.A_bound - self.Z_bound
            self.I_bound = ( self.N_bound - self.Z_bound ) / self.A_bound
            self.xn_bound = self.N_bound / self.A_bound
            self.xp_bound = self.Z_bound / self.A_bound
            # cluster volume and radius
            self.Vcl = 2 * self.Z_bound / ( (1-self.I_bound) * self.ncl )
            self.Rcl = ( 3 / ( 4 * nuda.cst.pi ) * self.Vcl )**nuda.cst.third
            # volume fraction
            self.u = self.Vcl / self.VWS
            # unbound (gas) neutrons
            self.RWS = ( 3 / ( 4 * nuda.cst.pi ) * self.VWS )**nuda.cst.third
            self.N_g = self.ng * ( self.VWS - self.Vcl )
            # total number of nucleons
            self.Z = self.Z_bound
            self.N = self.N_bound + self.N_g
            self.A = self.A_bound + self.N_g
            self.xn = self.N / self.A
            self.xp = self.Z / self.A
            # energy
            self.e2a_tot = self.e2a_int2 + nuda.cst.mnc2
            self.e2a_rm = self.xn * nuda.cst.mnc2 + self.xp * ( nuda.cst.mpc2 + nuda.cst.mec2 )
            self.e2a_int = self.e2a_tot - self.e2a_rm
            # electrons
            self.mu_e = self.mu_n - self.mu_p
    #
    def print_outputs( self ):
       """
       Method which print outputs on terminal's screen.
       """
       print("")
       #
       if nuda.env.verb: print("Enter print_outputs()")
       #
       print("- Print output:")
       print("   modcrust:",self.modcrust)
       print("   ref:     ",self.ref)
       print("   label:   ",self.label)
       print("   note:    ",self.note)
       if self.den is not None: print(f"   den: {self.den}")
       if self.A is not None: print(f"   A: {self.A}")
       if self.Z is not None: print(f"   Z: {self.Z}")
       if self.N is not None: print(f"   N: {self.N}")
       if self.N_bound is not None: print(f"   N_bound: {self.N_bound}")
       if self.N_g is not None: print(f"   N_g: {self.N_g}")
       if self.mu_n is not None: print(f"   mu_n(MeV): {self.mu_n}")
       if self.mu_p is not None: print(f"   mu_p(MeV): {self.mu_p}")
       if self.den_g is not None: print(f"   den_g(fm-3): {self.den_g}")
       if self.RWS is not None: print(f"   RWS(fm): {np.round(self.RWS,3)}")
       if self.xpn_bound is not None: print(f"   xpn_bound: {self.xpn_bound}")
       if self.e2a_tot is not None: print(f"   e2a_tot(MeV): {np.round(self.e2a_tot,3)}")
       if self.e2a_rm is not None: print(f"   e2a_rm(MeV): {np.round(self.e2a_rm,3)}")
       if self.e2a_int2 is not None: print(f"   e2a_int2(MeV): {np.round(self.e2a_int2,3)}")
       if self.e2a_int is not None: print(f"   e2a_int(MeV): {np.round(self.e2a_int,3)}")
       if self.e2a_int_g is not None: print(f"   e2a_int_g(MeV): {np.round(self.e2a_int_g,3)}")
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
        #: Attribute the density of the system (in cm^-3).
        self.den_cgs = None
        #: Attribute the density of the system (in fm^-3).
        self.den = None
        #: Attribute A_bound (mass of the cluster).
        self.A_bound = None
        #: Attribute Z_bound (charge of the cluster).
        self.Z_bound = None
        #: Attribute N_bound (number of neutrons in the cluster).
        self.N_bound = None
        #: Attribute N_g (number of neutrons in the gas).
        self.N_g = None
        #: Attribute n_g (neutron density in the gas).
        self.n_g = None
        #: Attribute A (total number of nucleons of the WS cell).
        self.A = None
        #: Attribute Z (total number of protons of the WS cell).
        self.Z = None
        #: Attribute N (total number of neutrons of the WS cell).
        self.N = None
        #: Attribute the fraction of neutrons.
        self.xn = None
        #: Attribute the fraction of bound neutrons.
        self.xn_bound = None
        #: Attribute the fraction of protons.
        self.xp = None
        #: Attribute the fraction of bound protons.
        self.xp_bound = None
        #: Attribute the asymmetry parameter for bound particles.
        self.I_bound = None
        #: Attribute the approximate ratio of proton to neutron in the nucleus.
        self.xpn_bound = None
        #: Attribute the neutron chemical potential (in MeV).
        self.mu_n = None
        #: Attribute the proton chemical potential (in MeV).
        self.mu_p = None
        #: Attribute the approximate density of neutron in the gas (in fm-3).
        self.den_g = None
        #: Attribute the radius of the cluster (in fm).
        self.Rcl = None
        #: Attribute the radius of the WS cell (in fm).
        self.RWS = None
        #: Attribute the rest mass energy (in MeV).
        self.e2a_rm = None
        #: Attribute the energy minus the neutron mass (in MeV).
        self.e2a_int2 = None
        #: Attribute the internal energy (in MeV).
        self.e2a_int = None
        #: Attribute the internal energy of the gas component (in MeV).
        self.e2a_int_g = None
        #
        self.ref = None
        self.note = None
        self.label = None
        self.linestyle = None
        self.latexCite = None
        #
        if nuda.env.verb: print("Exit init_self()")
        #
        return self        

