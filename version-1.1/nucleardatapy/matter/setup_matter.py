import os
import sys
import numpy as np  # 1.15.0
from scipy.interpolate import CubicSpline
from scipy.optimize import curve_fit
import random

import nucleardatapy as nuda

def uncertainty_stat(den, er="MBPT"):
    if er.lower() == "qmc":
        return 0.21 * (den / nuda.cst.nsat)
    elif er.lower() == "mbpt":
        return 0.07 * (den / nuda.cst.nsat)
    else:
        print("no model uncertainty is given")
        print("er:", er)
        print("exit()")
        exit()

def matter_micro_models():
    """
    Return a list of many-bodys (mbs) approaches available in this toolkit and print them all on the prompt.

    :return: The list of models with can be 'VAR', 'AFDMC', 'BHF', 'QMC', 'MBPT', 'NLEFT'.
    :rtype: list[str].
    """
    #
    if nuda.env.verb:
        print("\nEnter matter_micro_mbs()")
    #
    models = [ "Var", "MC", "BHF2BF", "BHF23BF", "MBPT", "NLEFT", "SCGF", "CC" ]
    models_loer = [ item.lower() for item in models ]
    #
    if nuda.env.verb:
        print("Exit matter_micro_models()")
    #
    return models, models_loer

def matter_pheno_models():
    """
    Return a list of models available in this toolkit and print them all on the prompt.

    :return: The list of models with can be 'Skyrme', 'ESkyrme', 'NLRH', 'DDRH', 'DDRHF'.
    :rtype: list[str].
    """
    #
    if nuda.env.verb: print("\nEnter matter_pheno_models()")
    #
    # models = [ 'Skyrme', 'ESkyrme', 'Gogny', 'Fayans', 'NLRH', 'DDRH', 'DDRHF' ]
    models = [ 'Skyrme', 'ESkyrme', 'NLRH', 'DDRH', 'DDRHF' ]

    #print('Phenomenological models available in the toolkit:',models)
    models_loer = [ item.lower() for item in models ]
    #
    if nuda.env.verb: print("Exit matter_pheno_models()")
    #
    return models, models_loer

def matter_models():
    """
    Return a list of models available in this toolkit and print them all on the prompt.

    :return: The list of models.
    :rtype: list[str].
    """
    #
    if nuda.env.verb: print("\nEnter matter_models()")
    #
    pheno_models, pheno_models_loer = matter_pheno_models( )
    micro_models, micro_models_loer = matter_micro_models( )
    models = pheno_models + micro_models
    models_loer = pheno_models_loer + micro_models_loer
    #
    if nuda.env.verb: print("Exit matter_models()")
    #
    return models, models_loer


def matter_params( model ):
    """
    Return a list with the name of the models available in this toolkit \
    for a given mb appoach and print them all on the prompt. 

    :param mb: The mb approach for which there are parametrizations. \
    They should be chosen among the following options: 'VAR', 'AFDMC', 'BHF', 'QMC', 'MBPT', 'NLEFT'.
    :type mb: str.
    :return: The list of parametrizations.

    """
    #
    if nuda.env.verb:
        print("\nEnter matter_micro_params( model )")
    #
    # print('mb:',mb)
    if model.lower() == 'skyrme':
        params = [ 'BSK14', 'BSK16', 'BSK17', 'BSK27', 'BSkG1', 'BSkG2', 'F-', \
            'F+', 'F0', 'FPL', 'LNS', 'LNS1', 'LNS5', 'NRAPR', 'RATP', \
            'SAMI', 'SGII', 'SIII', 'SKGSIGMA', 'SKI2', 'SKI4', 'SKMP', \
            'SKMS', 'SKO', 'SKOP', 'SKP', 'SKRSIGMA', 'SKX', 'Skz2', \
            'SLY4', 'SLY5', 'SLY230A', 'SLY230B', 'SV', 'T6', 'T44', \
            'UNEDF0', 'UNEDF1' ]
    elif model.lower() == 'eskyrme':
        params = [ 'BSk22', 'BSk24', 'BSk25', 'BSk26', 'BSk31', 'BSk32',  'BSkG3','BSkG4' ]
    elif model.lower() == 'fayans':
        params = [ 'Fy(IVP)', 'Fy(Dr,HDB)', 'Fy(std)' ]
    elif model.lower() == 'gogny':
        params = [ 'D1S', 'D1', 'D250', 'D260', 'D280', 'D300' ]
    elif model.lower() == 'nlrh':
        params = [ 'NL-SH', 'NL3', 'NL3II', 'PK1', 'PK1R', 'TM1' ]
    elif model.lower() == 'ddrh':
        params = [ 'DDME1', 'DDME2', 'DDMEd', 'PKDD', 'TW99' ]
    elif model.lower() == 'ddrhf':
        params = [ 'PKA1', 'PKO1', 'PKO2', 'PKO3' ]
    elif model.lower() == "var":
        params = ["1981-FP", "1998-APR" ]
    elif model.lower() == "mc":
        params = [
            "2008-QMCswave",
            "2009-DQMC",
            "2010-QMCAV4",
            "2012-AFDMC-1",
            "2012-AFDMC-2",
            "2012-AFDMC-3",
            "2012-AFDMC-4",
            "2012-AFDMC-5",
            "2012-AFDMC-6",
            "2012-AFDMC-7",
            "2012-AFDMCFIT-1",
            "2012-AFDMCFIT-2",
            "2012-AFDMCFIT-3",
            "2012-AFDMCFIT-4",
            "2012-AFDMCFIT-5",
            "2012-AFDMCFIT-6",
            "2012-AFDMCFIT-7",
            "2014-AFQMC",
            "2016-QMC",
            "2018-QMC",
            "2022-AFDMC",
            "2024-DMC",
        ]
    elif model.lower() == "mbpt":
    # '2010-MBPT-NM' is removed because they do not provide e2a, only pressure
        params = [
            #"2010-MBPT",
            "2013",
            "2016",
            "2019-L59",
            "2019-L69",
            "2020",
            "2024-DN2LO450",
            "2024-DN2LO500",
            "2024-DN2LOgo394",
            "2024-DN2LOgo450",
            "2024-N2LOsat",
        ]
    elif model.lower() == "nleft":
        params = [ 
            "2024"
        ]
    elif model.lower() == "bhf2bf":
        params = [
            "2024-Av8p",
            "2024-Av18",
            "2024-BONN",
            "2024-CDBONN",
            "2024-NSC97a",
            "2024-NSC97b",
            "2024-NSC97c",
            "2024-NSC97d",
            "2024-NSC97e",
            "2024-NSC97f",
            "2024-SSCV14",
        ]
    elif model.lower() == "bhf23bf":
        params = [
            "2006-Av18",
            "2024-Av8p",
            "2024-Av18",
            "2024-Av18micro",
            "2024-BONN",
            "2024-BONNBmicro",
            "2024-CDBONN",
            "2024-NSC93micro",
            "2024-NSC97a",
            "2024-NSC97b",
            "2024-NSC97c",
            "2024-NSC97d",
            "2024-NSC97e",
            "2024-NSC97f",
            "2024-SSCV14",
        ]
    elif model.lower() == "scgf":
        params = [
            "2020-N3LO414",
            "2020-N3LO450",
            "2020-N3LO500",
            "2024-DN2LO450",
            "2024-DN2LO500",
            "2024-DN2LOgo394",
            "2024-DN2LOgo450",
            "2024-N2LOsat",
        ]
    elif model.lower() == "cc":
        params = [
            "2024-DN2LO450",
            "2024-DN2LO500",
            "2024-DN2LOgo394",
            "2024-DN2LOgo450",
            "2024-N2LOsat",
        ]
    #
    params_loer = [item.lower() for item in params]
    #
    if nuda.env.verb:
        print("\nExit matter_micro_params()")
    #
    return params, params_loer

def matter_params_models( models ):
    #
    if nuda.env.verb:
        print("\nEnter matter_params_models( models )")
    #
    params = []
    for model in models:
        new_params, new_params_loer = matter_params( model )
        params.extend(new_params)
    #
    if nuda.env.verb:
        print("params available in the toolkit:", params)
    #
    params_loer = [item.lower() for item in params]
    #
    if nuda.env.verb:
        print("Exit matter_micro_params_models()")
    #
    return params, params_loer

def matter_micro_params():
    #
    if nuda.env.verb:
        print("\nEnter matter_micro_params()")
    #
    models, mmodels_loer = matter_micro_models()
    #
    params, params_loer = matter_params_models( models )
    #
    if nuda.env.verb:
        print("Exit matter_micro_params()")
    #
    return params, params_loer

def matter_params_model_matter(model, matter):
    """
    matter can be 'sm', 'SM' or 'nm', 'NM'
    """
    #
    if nuda.env.verb:
        print("\nEnter matter_params_model_matter()")
    #
    print("For model (in " + matter + "):", model)
    #
    params, params_loer = matter_params_model( model )
    #
    params2 = []
    for j, param in enumerate(params):
        if matter.upper() in param or "AM" in param:
            param2.append(param)
    #
    print("params2:", params2)
    params2_loer = [item.lower() for item in params2]
    #
    return params2, params2_loer

# Define functions for APRfit
def APRfit_compute(n, x):
    p53 = 5.0 / 3.0
    p83 = 8.0 / 3.0
    asy = 1.0 - 2.0 * x
    n2 = n * n
    G = (3.0 * np.pi**2) ** p53 / (5.0 * np.pi**2)
    Hk = (
        G
        * nuda.cst.hbc**2
        / (2.0 * nuda.cst.mnuc2_approx)
        * n**p53
        * ((1 - x) ** p53 + x**p53)
    )
    Hm = (
        G
        * (p3 * ((1 - x) ** p53 + x**p53) + p5 * ((1 - x) ** p83 + x**p83))
        * n**p83
        * np.exp(-p4 * n)
    )
    g1L = -n2 * (p1 + p2 * n + p6 * n2 + (p10 + p11 * n) * np.exp(-(p9**2) * n2))
    g2L = -n2 * (p12 / n + p7 + p8 * n + p13 * np.exp(-(p9**2) * n2))
    g1H = g1L - n2 * (p17 * (n - p19) + p21 * (n - p19) ** 2) * np.exp(p18 * (n - p19))
    g2H = g2L - n2 * (p15 * (n - p20) + p14 * (n - p20) ** 2) * np.exp(p16 * (n - p20))
    HdL = g1L * (1.0 - asy**2) + g2L * asy**2
    HdH = g1H * (1.0 - asy**2) + g2H * asy**2
    #
    HL = Hk + Hm + HdL
    HH = Hk + Hm + HdH
    #
    nt = 0.32 - 0.12 * (1 - 2 * x) ** 2  # transition density in fm^-3
    eps = np.zeros(len(n))
    for ind, den in enumerate(n):
        if den < nt:
            eps[ind] = HL[ind]
            indref = ind
        else:
            eps[ind] = HH[ind]
    return eps

def func_GCR_e2a(den, a, alfa, b, beta):
    return a * (den / nuda.cst.nsat) ** alfa + b * (den / nuda.cst.nsat) ** beta

def func_GCR_pre(den, a, alfa, b, beta):
    return den * (
        a * alfa * (den / nuda.cst.nsat) ** alfa
        + b * beta * (den / nuda.cst.nsat) ** beta
    )

def func_GCR_cs2(den, a, alfa, b, beta):
    dp_dn = (
        a * alfa * (alfa + 1.0) * (den / nuda.cst.nsat) ** alfa
        + b * beta * (beta + 1.0) * (den / nuda.cst.nsat) ** beta
    )
    h2a = (
        nuda.cst.mnuc2
        + func_GCR_e2a(den, a, alfa, b, beta)
        + func_GCR_pre(den, a, alfa, b, beta) / den
    )
    return dp_dn / h2a

def func_e2a_NLEFT2024(kfn, b, c, d):
    a = 1.0
    func = a + b * kfn + c * kfn**2 + d * kfn**3
    return func * nuda.effg_nr(kfn)

def func_pre_NLEFT2024(kfn, den, b, c, d):
    func = (
        nuda.cst.two
        + nuda.cst.three * b * kfn
        + nuda.cst.four * c * kfn**2
        + nuda.cst.five * d * kfn**3
    )
    return func * nuda.cst.third * den * nuda.effg_nr(kfn)

def func_dpredn_NLEFT2024(kfn, den, b, c, d):
    func = nuda.cst.four + 9.0 * b * kfn + 20.0 * c * kfn**2 + 25.0 * d * kfn**3
    return func_pre_NLEFT2024(kfn, den, b, c, d) / den + func * nuda.effg_nr(kfn) / 9.0


class setupMatter():
    """
    Instantiate the object with results based on phenomenological\
    interactions and choosen by the toolkit practitioner. \
    This choice is defined in the variables `model` and `param`.
    
    :param model: Fix the name of model: 'Skyrme', 'NLRH', \
    'DDRH', 'DDRHF'. Default value: 'Skyrme'.
    :type model: str, optional. 
    :param param: Fix the parameterization associated to model. \
    Default value: 'SLY5'.
    :type param: str, optional. 

    **Attributes:**
    """
    #
    def __init__( self, model = 'Skyrme', param = 'SLY5', var1=np.linspace(0.01, 0.4, 20), var2=0.0 ):
        """
        Parameters
        ----------
        model : str, optional
        The model to consider. Choose between: 1998-VAR-AM-APR (default), 2008-AFDMC-NM, ...
        var1 and var2 : densities (array) and isospin asymmetry (scalar) if necessary (for interpolation function in APRfit for instance)
        var1 = np.array([0.1,0.15,0.16,0.17,0.2,0.25])
        """
        #
        if nuda.env.verb: print("\nEnter setupMatter()")
        #
        #: Attribute model.
        self.model = model
        self.model_lo = model.lower()
        if nuda.env.verb: print("model:",model)
        print("-> model:",model)
        #
        #: Attribute param.
        self.param = param
        self.param_lo = param.lower()
        #print("-> param:",param)
        if nuda.env.verb: print("param:",param)
        print("-> param:",param)
        #
        self = setupMatter.init_self( self )
        #
        # read var and define den, asy and xpr (for fit only):
        self.den = var1[:]  # density n_b=n_n+n_p
        self.asy = var2  # asymmetry parameter = (n_n-n_p)/n_b
        self.kfn = nuda.kf_n((1.0 + self.asy) / 2.0 * self.den)
        self.xpr = (1.0 - self.asy) / 2.0  # proton fraction = n_p/n_b
        # print('den:',self.den)
        # print('asy:',self.asy)
        # print('xpr:',self.xpr)
        #
        models, models_loer = matter_models( )
        #print(f'models: {models}')
        #
        if model.lower() not in models_loer:
            print('In setupMatter(): The model name ',model,' is not in the list of models.')
            print('In setupMatter(): list of models:',models)
            print('-- Exit the code --')
            exit()
        #
        params, params_loer = matter_params( model = model )
        #
        self.nm_rmass = nuda.cst.mnc2
        self.sm_rmass = 0.5 * ( nuda.cst.mnc2 + nuda.cst.mpc2 )
        self.rmass = (1.0-self.xpr) * nuda.cst.mnc2 + self.xpr * nuda.cst.mpc2
        #
        if self.param_lo not in params_loer:
            print('In setupMatter(): The param set ',self.param,' is not in the list of param.')
            print('In setupMatter(): list of param:',params)
            print('-- Exit the code --')
            exit()
        #
        file_SM = os.path.join(nuda.param.path_data,'matter/type/'+self.model+'/'+self.param+'-SM.dat')
        file_NM = os.path.join(nuda.param.path_data,'matter/type/'+self.model+'/'+self.param+'-NM.dat')
        if os.path.exists(file_SM):
            self.flag_sm = True
        else:
            self.flag_sm = False
        if os.path.exists(file_NM):
            self.flag_nm = True
        else:
            self.flag_nm = False
        if nuda.env.verb: print('Reads file_SM:',file_SM)
        if nuda.env.verb: print('Reads file_NM:',file_NM)
        #
        #: Attribute providing the label the data is references for figures.
        self.label = self.param
        #
        if self.model_lo == 'skyrme':
            #
            self.flag_kf = False
            self.flag_den = True
            #
            #: Attribute providing the full reference to the paper to be citted.
            #self.ref = ''
            #: Attribute providing additional notes about the data.
            self.note = "write here notes about this EOS."
            if os.path.exists(file_SM):
                self.sm_den, self.sm_kfn, self.sm_e2a_int, self.sm_pre, a, self.sm_cs2 = np.loadtxt( file_SM, usecols=(0,1,2,3,4,5), comments='#', unpack = True )
            if os.path.exists(file_NM):
                self.nm_den, self.nm_kfn, self.nm_e2a_int, self.nm_pre, a, self.nm_cs2 = np.loadtxt( file_NM, usecols=(0,1,2,3,4,5), comments='#', unpack = True )
            self.sm_e2a = self.sm_rmass + self.sm_e2a_int
            self.nm_e2a = self.nm_rmass + self.nm_e2a_int
            self.sm_eps = self.sm_e2a * self.sm_den
            self.nm_eps = self.nm_e2a * self.nm_den
            #self.sm_kf = self.sm_kfn
            # pressure in SM
            x = np.insert( self.sm_den, 0, 0.0 )
            y = np.insert( self.sm_e2a_int, 0, 0.0 )
            cs_sm_e2a = CubicSpline( x, y )
            self.sm_pre = np.array( self.sm_den**2 * cs_sm_e2a( self.sm_den, 1) )
            # pressure in NM
            x = np.insert( self.nm_den, 0, 0.0 )
            y = np.insert( self.nm_e2a_int, 0, 0.0 )
            cs_nm_e2a = CubicSpline( x, y )
            self.nm_pre = np.array( self.nm_den**2 * cs_nm_e2a( self.nm_den, 1) )
            # enthalpy
            self.sm_h2a = self.sm_e2a + self.sm_pre / self.sm_den
            self.nm_h2a = self.nm_e2a + self.nm_pre / self.nm_den
            # sound speed in SM
            x = np.insert(self.sm_den, 0, 0.0)
            y = np.insert(self.sm_pre, 0, 0.0)
            cs_sm_pre = CubicSpline(x, y)
            self.sm_cs2 = cs_sm_pre(self.sm_den, 1) / self.sm_h2a
            # sound speed in NM
            x = np.insert(self.nm_den, 0, 0.0)
            y = np.insert(self.nm_pre, 0, 0.0)
            cs_nm_pre = CubicSpline(x, y)
            self.nm_cs2 = cs_nm_pre(self.nm_den, 1) / self.nm_h2a
            #
        elif self.model_lo == 'eskyrme':
            #
            self.flag_kf = False
            self.flag_den = True
            #
            #: Attribute providing the full reference to the paper to be citted.
            #self.ref = ''
            #: Attribute providing additional notes about the data.
            self.note = "write here notes about this EOS."
            if os.path.exists(file_SM):
                self.sm_den, self.sm_e2a_int, self.sm_pre = np.loadtxt( file_SM, usecols=(0,1,2), comments='#', unpack = True )
            if os.path.exists(file_NM):
                self.nm_den, self.nm_e2a_int, self.nm_pre = np.loadtxt( file_NM, usecols=(0,1,2), comments='#', unpack = True )
            self.sm_e2a = self.sm_rmass + self.sm_e2a_int
            self.nm_e2a = self.nm_rmass + self.nm_e2a_int
            self.sm_eps = self.sm_e2a * self.sm_den
            self.nm_eps = self.nm_e2a * self.nm_den
            self.sm_kf = self.sm_kfn
            self.sm_kfn = nuda.kf_n( nuda.cst.half * self.sm_den )
            self.nm_kfn = nuda.kf_n( self.nm_den )
            #self.sm_kf = self.sm_kfn
            # enthalpy
            self.sm_h2a = self.sm_e2a + self.sm_pre / self.sm_den
            self.nm_h2a = self.nm_e2a + self.nm_pre / self.nm_den
            # sound speed in SM
            x = np.insert( self.sm_den, 0, 0.0 )
            y = np.insert( self.sm_pre, 0, 0.0 )
            cs_sm_pre = CubicSpline( x, y )
            self.sm_cs2 = cs_sm_pre( self.sm_den, 1) / self.sm_h2a
            # sound speed in NM
            x = np.insert( self.nm_den, 0, 0.0 )
            y = np.insert( self.nm_pre, 0, 0.0 )
            cs_nm_pre = CubicSpline( x, y )
            self.nm_cs2 = cs_nm_pre( self.nm_den, 1) / self.nm_h2a
            #
        elif self.model_lo == 'gogny':
            #
            pass
            #
        elif self.model_lo == 'fayans':
            #
            pass
            #
        elif self.model_lo == 'nlrh':
            #
            self.flag_kf = False
            self.flag_den = True
            #
            #self.ref = ''
            self.note = "write here notes about this EOS."
            if os.path.exists(file_SM):
                self.sm_den, self.sm_kfn, self.sm_e2a_int, self.sm_pre, self.sm_cs2_data = np.loadtxt( file_SM, usecols=(0,1,2,3,4), comments='#', unpack = True )
            if os.path.exists(file_NM):
                self.nm_den, self.nm_kfn, self.nm_e2a_int, self.nm_pre, self.nm_cs2_data = np.loadtxt( file_NM, usecols=(0,1,2,3,4), comments='#', unpack = True )
            self.sm_e2a = self.sm_rmass + self.sm_e2a_int
            self.nm_e2a = self.nm_rmass + self.nm_e2a_int
            self.sm_eps = self.sm_e2a * self.sm_den
            self.nm_eps = self.nm_e2a * self.nm_den
            #self.sm_kf = self.sm_kfn
            # enthalpy
            self.sm_h2a = self.sm_e2a + self.sm_pre / self.sm_den
            self.nm_h2a = self.nm_e2a + self.nm_pre / self.nm_den
            # sound speed in SM
            x = np.insert( self.sm_den, 0, 0.0 )
            y = np.insert( self.sm_pre, 0, 0.0 )
            cs_sm_pre = CubicSpline( x, y )
            self.sm_cs2 = cs_sm_pre( self.sm_den, 1) / self.sm_h2a
            # sound speed in NM
            x = np.insert( self.nm_den, 0, 0.0 )
            y = np.insert( self.nm_pre, 0, 0.0 )
            cs_nm_pre = CubicSpline( x, y )
            self.nm_cs2 = cs_nm_pre( self.nm_den, 1) / self.nm_h2a
            #
        elif self.model_lo == 'ddrh':
            #
            self.flag_kf = False
            self.flag_den = True
            #
            #self.ref = ''
            self.note = "write here notes about this EOS."
            if os.path.exists(file_SM):
                self.sm_den, self.sm_kfn, self.sm_e2a_int, self.sm_pre, self.sm_cs2_data = np.loadtxt( file_SM, usecols=(0,1,2,3,4), comments='#', unpack = True )
            if os.path.exists(file_NM):
                self.nm_den, self.nm_kfn, self.nm_e2a_int, self.nm_pre, self.nm_cs2_data = np.loadtxt( file_NM, usecols=(0,1,2,3,4), comments='#', unpack = True )
            self.sm_e2a = self.sm_rmass + self.sm_e2a_int
            self.nm_e2a = self.nm_rmass + self.nm_e2a_int
            self.sm_eps = self.sm_e2a * self.sm_den
            self.nm_eps = self.nm_e2a * self.nm_den
            #self.sm_kf = self.sm_kfn
            # enthalpy
            self.sm_h2a = self.sm_e2a + self.sm_pre / self.sm_den
            self.nm_h2a = self.nm_e2a + self.nm_pre / self.nm_den
            # sound speed in SM
            x = np.insert( self.sm_den, 0, 0.0 )
            y = np.insert( self.sm_pre, 0, 0.0 )
            cs_sm_pre = CubicSpline( x, y )
            self.sm_cs2 = cs_sm_pre( self.sm_den, 1) / self.sm_h2a
            # sound speed in NM
            x = np.insert( self.nm_den, 0, 0.0 )
            y = np.insert( self.nm_pre, 0, 0.0 )
            cs_nm_pre = CubicSpline( x, y )
            self.nm_cs2 = cs_nm_pre( self.nm_den, 1) / self.nm_h2a
            #
        elif self.model_lo == 'ddrhf':
            #
            self.flag_kf = False
            self.flag_den = True
            #
            #self.ref = ''
            self.note = "write here notes about this EOS."
            if os.path.exists(file_SM):
                self.sm_den, self.sm_kfn, self.sm_e2a_int, self.sm_pre, self.sm_cs2_data = np.loadtxt( file_SM, usecols=(0,1,2,3,4), comments='#', unpack = True )
            if os.path.exists(file_NM):
                self.nm_den, self.nm_kfn, self.nm_e2a_int, self.nm_pre, self.nm_cs2_data = np.loadtxt( file_NM, usecols=(0,1,2,3,4), comments='#', unpack = True )
            self.sm_e2a = self.sm_rmass + self.sm_e2a_int
            self.nm_e2a = self.nm_rmass + self.nm_e2a_int 
            self.sm_eps = self.sm_e2a * self.sm_den
            self.nm_eps = self.nm_e2a * self.nm_den
            #self.sm_kf = self.sm_kfn
            # enthalpy
            self.sm_h2a = self.sm_e2a + self.sm_pre / self.sm_den
            self.nm_h2a = self.nm_e2a + self.nm_pre / self.nm_den
            # sound speed in SM
            x = np.insert( self.sm_den, 0, 0.0 )
            y = np.insert( self.sm_pre, 0, 0.0 )
            cs_sm_pre = CubicSpline( x, y )
            self.sm_cs2 = cs_sm_pre( self.sm_den, 1) / self.sm_h2a
            # sound speed in NM
            x = np.insert( self.nm_den, 0, 0.0 )
            y = np.insert( self.nm_pre, 0, 0.0 )
            cs_nm_pre = CubicSpline( x, y )
            self.nm_cs2 = cs_nm_pre( self.nm_den, 1) / self.nm_h2a
            #
        elif self.model_lo == 'var':
            #
            if self.param_lo == "1981-fp":
                #
                self.flag_kf = True
                self.flag_den = False
                #
                self.ref = "Friedman and Pandharipande, Nucl. Phys. A. 361, 502 (1981)"
                self.note = "write here notes about this EOS."
                self.marker = "o"
                self.every = 1
                self.e_er = False
                self.p_er = False
                self.cs2_er = False
                self.linestyle = "solid"
                if os.path.exists(file_SM):
                    self.sm_den, self.sm_e2a_int = np.loadtxt( file_SM, usecols=(0, 1), unpack=True )
                if os.path.exists(file_NM):
                    self.nm_den, self.nm_e2a_int = np.loadtxt( file_NM, usecols=(0, 1), unpack=True )
                self.nm_e2a = self.nm_rmass + self.nm_e2a_int
                self.sm_e2a = self.sm_rmass + self.sm_e2a_int
                self.nm_eps = self.nm_e2a * self.nm_den
                self.sm_eps = self.sm_e2a * self.sm_den
                self.nm_kfn = nuda.kf_n( self.nm_den )
                self.sm_kfn = nuda.kf_n( nuda.cst.half * self.sm_den )
                self.nm_e2a_er = np.abs( uncertainty_stat(self.nm_den, er="MBPT") * self.nm_e2a_int )
                self.sm_e2a_er = np.abs( uncertainty_stat(self.sm_den, er="MBPT") * self.sm_e2a_int )
                self.nm_eps_er = self.nm_e2a_er * self.nm_den
                self.sm_eps_er = self.sm_e2a_er * self.sm_den
                #
            elif self.param_lo == "1998-apr":
                #
                self.flag_kf = False
                self.flag_den = True
                #
                self.ref = ( "Akmal, Pandharipande and Ravenhall, Phys. Rev. C 58, 1804 (1998)" )
                self.note = "write here notes about this EOS."
                self.label = "APR-1998"
                self.marker = "^"
                self.every = 1
                self.e_er = False
                self.p_er = False
                self.cs2_er = False
                self.linestyle = "solid"
                if os.path.exists(file_SM):
                    self.sm_den, self.sm_e2a_int = np.loadtxt( file_SM, usecols=(0, 1), unpack=True )
                if os.path.exists(file_NM):
                    self.nm_den, self.nm_e2a_int = np.loadtxt( file_NM, usecols=(0, 1), unpack=True )
                self.nm_e2a = self.nm_rmass + self.nm_e2a_int
                self.sm_e2a = self.sm_rmass + self.sm_e2a_int
                self.nm_eps = self.nm_e2a * self.nm_den
                self.sm_eps = self.sm_e2a * self.sm_den
                self.nm_kfn = nuda.kf_n(self.nm_den)
                self.sm_kfn = nuda.kf_n(nuda.cst.half * self.sm_den)
                self.nm_e2a_er = np.abs( uncertainty_stat(self.nm_den, er="MBPT") * self.nm_e2a_int )
                self.sm_e2a_er = np.abs( uncertainty_stat(self.sm_den, er="MBPT") * self.sm_e2a_int )
                self.nm_eps_er = self.nm_e2a_er * self.nm_den
                self.sm_eps_er = self.sm_e2a_er * self.sm_den
                #
            elif self.param_lo == "1998-aprfit":
                #
                self.flag_nm = True
                self.flag_sm = True
                self.flag_kf = False
                self.flag_den = False
                #
                self.ref = ( "Akmal, Pandharipande and Ravenhall, Phys. Rev. C 58, 1804 (1998)" )
                self.note = "Use interpolation functions suggested in APR paper."
                self.marker = "."
                self.every = 1
                self.e_er = False
                self.p_er = False
                self.cs2_er = False
                self.linestyle = "dashed"
                # Define constants for APRfit and for A18+dv+UIX*
                global p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21
                ( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21 ) = ( 337.2, -382.0, 89.8, 0.457, -59.0, -19.1, 214.6, -384.0, 6.4, 69.0, -33.0, 0.35, 0.0, 0.0, 287.0, -1.54, 175.0, -1.45, 0.32, 0.195, 0.0 )
                #
                # energy per unit volume
                self.eps_int = APRfit_compute( self.den, self.xpr )
                # energy per particle
                self.e2a_int = self.eps_int / self.den
                self.e2a = self.rmass + self.e2a_int
                self.eps = self.e2a * self.den
                self.e2a_er = np.abs( uncertainty_stat(self.den, er="MBPT") * self.e2a_int )
                self.eps_er = self.e2a_er * self.den
                # pressure as the first derivative of E/A
                cs_e2a = CubicSpline( self.den, self.e2a_int )
                # pre = n**2 * np.gradient( e2a, n)
                self.pre = self.den**2 * cs_e2a( self.den, 1 )
                # chemical potential
                #self.chempot = ( self.eps + self.pre ) / self.den
                # enthalpy
                self.h2a = self.e2a + self.pre / self.den
                # sound speed
                cs_pre = CubicSpline( self.den, self.pre )
                self.cs2 = cs_pre( self.den, 1 ) / self.h2a
            #
        elif self.model_lo == 'mc':
            #
            if self.param_lo == "2008-qmcswave":
                #
                self.flag_kf = True
                self.flag_den = False
                #
                self.ref = "A. Gezerlis and J. Carlson PRC 81, 025803 (2010)"
                self.note = ""
                self.marker = "o"
                self.every = 1
                self.linestyle = "solid"
                self.e_er = True
                self.p_er = False
                self.cs2_er = False
                if os.path.exists(file_NM):
                    self.nm_kfn, gap2ef, gap2ef_er, e2effg, e2effg_er = np.loadtxt(file_NM, usecols=(0, 1, 2, 3, 4), unpack=True )
                self.nm_den = nuda.den_n(self.nm_kfn)
                self.nm_e2a_int = e2effg * nuda.effg_nr(self.nm_kfn)
                self.nm_e2a = self.nm_rmass + self.nm_e2a_int
                self.nm_e2a_er = e2effg_er * nuda.effg_nr(self.nm_kfn)
                self.nm_eps = self.nm_e2a * self.nm_den
                self.nm_eps_er = self.nm_e2a_er * self.nm_den
                #
            elif self.param_lo == "2009-afdmc":
                #
                self.flag_kf = True
                self.flag_den = False
                #
                self.ref = "S. Gandolfi, A.Y. Illarionov, F. Pederiva, K.E. Schmidt, S. Fantoni, Phys. Rev. C 80, 045802 (2009)."
                self.note = ""
                self.marker = "o"
                self.every = 1
                self.linestyle = "solid"
                self.e_er = True
                self.p_er = False
                self.cs2_er = False
                if os.path.exists(file_NM):
                    self.nm_kfn, self.nm_e2a_int, self.nm_e2a_er = np.loadtxt(file_NM, usecols=(0, 1, 2), unpack=True )
                self.nm_den = nuda.den_n(self.nm_kfn)
                self.nm_e2a = self.nm_rmass + self.nm_e2a_int
                # self.nm_e2a_er = abs( 0.01 * self.nm_e2a )
                self.nm_eps = self.nm_e2a * self.nm_den
                self.nm_eps_er = self.nm_e2a_er * self.nm_den
                #
            elif self.param_lo == "2009-dqmc":
                #
                self.flag_kf = True
                self.flag_den = False
                #
                self.ref = "T. Abe, R. Seki, Phys. Rev. C 79, 054002 (2009)"
                self.note = ""
                self.marker = "v"
                self.every = 1
                self.linestyle = "solid"
                self.e_er = True
                self.p_er = False
                self.cs2_er = False
                if os.path.exists(file_NM):
                    self.nm_kfn, gap2ef, gap2ef_er, e2effg, e2effg_er = np.loadtxt(file_NM, usecols=(0, 1, 2, 3, 4), unpack=True )
                self.nm_den = nuda.den_n(self.nm_kfn)
                self.nm_e2a_int = np.array(e2effg * nuda.effg_nr(self.nm_kfn))
                self.nm_e2a = self.nm_rmass + self.nm_e2a_int
                self.nm_e2a_er = e2effg_er * nuda.effg_nr(self.nm_kfn)
                self.nm_eps = self.nm_e2a * self.nm_den
                self.nm_eps_er = self.nm_e2a_er * self.nm_den
                #
            elif self.param_lo == "2010-qmcav4":
                #
                self.flag_kf = True
                self.flag_den = False
                #
                self.ref = "A. Gezerlis and J. Carlson PRC 81, 025803 (2010)"
                self.note = ""
                self.marker = "s"
                self.every = 1
                self.linestyle = "solid"
                self.e_er = True
                self.p_er = False
                self.cs2_er = False
                if os.path.exists(file_NM):
                    self.nm_kfn, gap2ef, gap2ef_er, e2effg, e2effg_er = np.loadtxt( file_NM, usecols=(0, 1, 2, 3, 4), unpack=True )
                self.nm_den = nuda.den_n(self.nm_kfn)
                self.nm_e2a_int = np.array(e2effg * nuda.effg_nr(self.nm_kfn))
                self.nm_e2a = self.nm_rmass + self.nm_e2a_int
                self.nm_e2a_er = e2effg_er * nuda.effg_nr(self.nm_kfn)
                self.nm_eps = self.nm_e2a * self.nm_den
                self.nm_eps_er = self.nm_e2a_er * self.nm_den
                #
            elif "2012-afdmc-" in self.param_lo:
                #
                self.flag_kf = False
                self.flag_den = True
                #
                #print(f'param: {self.param}')
                #print(f'param.split: {self.param.split(sep="-")}')
                k = int(self.param.split(sep="-")[2])
                #print('k:',k)
                #
                self.ref = "S. Gandolfi, J. Carlson, S. Reddy, Phys. Rev. C 85, 032801(R) (2012)."
                self.note = "We have the data for this model, which are used for the fit in the next section."
                self.marker = "s"
                self.every = 3
                if k == 1:
                    self.every = 4
                if k == 7:
                    self.every = 4
                self.e_er = True
                self.p_er = False
                self.cs2_er = False
                self.linestyle = "solid"
                # self.linestyle = 'None'
                if k in [1, 7]:
                    if os.path.exists(file_NM):
                        self.nm_den, ETOT, ETOT_er = np.loadtxt( file_NM, usecols=(0, 1, 2), unpack=True )
                elif k in [2, 3, 4, 5, 6]:
                    if os.path.exists(file_NM):
                        V0, MU, self.nm_den, ETOT, ETOT_er = np.loadtxt( file_NM, usecols=(0, 1, 2, 3, 4), unpack=True )
                else:
                    print("The value of k is no correct ", k)
                    exit()
                self.nm_kfn = nuda.kf_n(self.nm_den)
                self.nm_e2a_int = ETOT  # / 66.0
                self.nm_e2a = self.nm_rmass + self.nm_e2a_int
                self.nm_e2a_er = ETOT_er  # / 66.0
                self.nm_eps = self.nm_den * self.nm_e2a
                self.nm_eps_er = self.nm_den * self.nm_e2a_er
                # self.nm_pre =
                # self.nm_chempot =
                # self.nm_cs2 =
                #
            elif "2012-afdmcfit-" in self.param_lo:
                #
                self.flag_kf = False
                self.flag_den = False
                #
                self.ref = "S. Gandolfi, J. Carlson, S. Reddy, Phys. Rev. C 85, 032801(R) (2012)."
                self.note = "This is the fit using the data from the previous section."
                self.marker = "s"
                self.every = 1
                self.e_er = True
                self.p_er = False
                self.cs2_er = False
                self.linestyle = "dashed"
                if os.path.exists(file_NM):
                    ind, a, alfa, b, beta = np.loadtxt( file_NM, usecols=(0, 1, 2, 3, 4), unpack=True )
                nmodel = 7
                self.nm_den_fit = 0.04 + 0.45 * np.arange(self.nden + 1) / float(self.nden)
                self.nm_kfn_fit = nuda.kf_n(self.nm_den_fit)
                # energy in NM
                self.nm_e2a_int_fit = func_GCR_e2a( self.nm_den_fit, a, alfa, b, beta )
                self.nm_e2a_fit = self.nm_rmass + self.nm_e2a_int_fit
                self.nm_e2a_fit_er = np.abs( uncertainty_stat(self.nm_den_fit, er="MBPT") * self.nm_e2a_fit )
                self.nm_eps_fit = self.nm_den_fit * self.nm_e2a_fit
                self.nm_eps_fit_er = self.nm_den_fit * self.nm_e2a_fit_er
                # pressure in NM
                self.nm_pre_fit = func_GCR_pre( self.nm_den_fit, a, alfa, b, beta )
                # chemical potential
                #self.nm_chempot_fit = (self.nm_pre_fit + self.nm_eps_fit) / self.nm_den_fit
                # enthalpy per particle
                self.nm_h2a_fit = self.nm_e2a_fit + self.nm_pre_fit / self.nm_den_fit
                # sound speed in NM
                self.nm_cs2_fit = func_GCR_cs2( self.nm_den_fit, a, alfa, b, beta )
                #
                self.nm_den = self.nm_den_fit
                self.nm_kfn = self.nm_kfn_fit
                self.nm_e2a_int = self.nm_e2a_fit
                self.nm_e2a = self.nm_rmass + self.nm_e2a_int
                self.nm_e2a_er = self.nm_e2a_fit_er
                self.nm_eps = self.nm_eps_fit
                self.nm_eps_er = self.nm_eps_fit_er
                self.nm_pre = self.nm_pre_fit
                #self.nm_chempot = self.nm_chempot_fit
                self.nm_cs2 = self.nm_cs2_fit
                #
            elif self.param_lo == "2014-afqmc":
                #
                self.flag_kf = True
                self.flag_den = False
                #
                self.ref = "G. Wlazłowski, J.W. Holt, S. Moroz, A. Bulgac, and K.J. Roche Phys. Rev. Lett. 113, 182503 (2014)"
                self.note = "write here notes about this EOS."
                self.marker = "s"
                self.every = 1
                self.e_er = False
                self.p_er = False
                self.cs2_er = False
                self.linestyle = "solid"
                if os.path.exists(file_NM):
                    self.nm_den, self.nm_e2a_int_2bf, self.nm_e2a_int_23bf = np.loadtxt( file_NM, usecols=(0, 1, 2), unpack=True )
                self.nm_kfn = nuda.kf_n(self.nm_den)
                self.nm_e2a_int = self.nm_e2a_int_23bf
                self.nm_e2a = self.nm_rmass + self.nm_e2a_int
                self.nm_e2a_er = np.abs( uncertainty_stat(self.nm_den, er="MBPT") * self.nm_e2a_int )
                # self.nm_e2a_er = np.abs( 0.01 * self.nm_e2a )
                self.nm_eps = self.nm_e2a * self.nm_den
                self.nm_eps_er = self.nm_e2a_er * self.nm_den
                #
            elif self.param_lo == "2016-qmc":
                #
                self.flag_kf = True
                self.flag_den = False
                #
                self.ref = " I. Tews, S. Gandolfi, A. Gezerlis, A. Schwenk, Phys. Rev. C 93, 024305 (2016)."
                self.note = ""
                self.marker = "s"
                self.linestyle = "solid"
                self.e_er = True
                self.p_er = False
                self.cs2_er = False
                self.every = 1
                if os.path.exists(file_NM):
                    self.nm_den, self.nm_e2a_int_lo, self.nm_e2a_int_up = np.loadtxt( file_NM, usecols=(0, 1, 2), unpack=True )
                self.nm_kfn = nuda.kf_n(self.nm_den)
                self.nm_e2a_int = np.array(0.5 * (self.nm_e2a_int_up + self.nm_e2a_int_lo))
                self.nm_e2a = self.nm_rmass + self.nm_e2a_int
                self.nm_e2a_er = 0.5 * (self.nm_e2a_int_up - self.nm_e2a_int_lo)
                self.nm_eps = self.nm_e2a * self.nm_den
                self.nm_eps_er = self.nm_e2a_er * self.nm_den
                #
            elif self.param_lo == "2018-qmc":
                #
                self.flag_kf = True
                self.flag_den = False
                #
                self.ref = "I. Tews, J. Carlson, S. Gandolfi, S. Reddy, Astroph. J. 860(2), 149 (2018)."
                self.note = ""
                self.marker = "s"
                self.every = 2
                self.linestyle = "solid"
                self.e_er = True
                self.p_er = False
                self.cs2_er = False
                if os.path.exists(file_NM):
                    self.nm_den, self.nm_e2a_int_lo, self.nm_e2a_int_up, self.nm_e2a_int, self.nm_e2a_er = np.loadtxt( file_NM, usecols=(0, 1, 2, 3, 4), unpack=True )
                self.nm_e2a = self.nm_rmass + self.nm_e2a_int
                self.nm_kfn = nuda.kf_n(self.nm_den)
                self.nm_eps = self.nm_e2a * self.nm_den
                self.nm_eps_er = self.nm_e2a_er * self.nm_den
                #
            elif self.param_lo == "2022-afdmc":
                #
                self.flag_kf = False
                self.flag_den = True
                #
                self.ref = "S. Gandolfi, G. Palkanoglou, J. Carlson, A. Gezerlis, K.E. Schmidt, Condensed Matter 7(1) (2022)."
                self.note = ""
                self.linestyle = "solid"
                self.marker = "o"
                self.linestyle = "solid"
                self.every = 1
                self.e_er = True
                self.p_er = False
                self.cs2_er = False
                # read e2a
                if os.path.exists(file_NM):
                    self.nm_kfn, e2effg, e2effg_er = np.loadtxt( file_NM, usecols=(0, 1, 2), delimiter=" ", comments="#", unpack=True )
                self.nm_den = nuda.den_n(self.nm_kfn)
                self.nm_e2a_int = e2effg * nuda.effg_nr(self.nm_kfn)
                self.nm_e2a = self.nm_rmass + self.nm_e2a_int
                self.nm_e2a_er = e2effg_er * nuda.effg_nr(self.nm_kfn)
                #
                self.nm_eps = self.nm_e2a * self.nm_den
                self.nm_eps_er = self.nm_e2a_er * self.nm_den
                #
            elif self.param_lo == "2024-dmc":
                #
                self.flag_kf = False
                self.flag_den = True
                #
                self.ref = "I. Tews, R. Somasundaram, D. Lonardoni, H. Göttling, R. Seutin, J. Carlson, S. Gandolfi, K. Hebeler, A. Schwenk, arXiv:2407.08979 [nucl-th]"
                self.note = ""
                self.marker = "s"
                self.every = 1
                self.linestyle = "solid"
                self.e_er = True
                self.p_er = False
                self.cs2_er = False
                if os.path.exists(file_NM):
                    self.nm_den, self.nm_e2a_int, self.nm_e2a_er_stat, self.nm_e2a_er_ekm, self.nm_e2a_er_gp = np.loadtxt( file_NM, usecols=(0, 1, 2, 3, 4), unpack=True )
                self.nm_kfn = nuda.kf_n(self.nm_den)
                self.nm_e2a = self.nm_rmass + self.nm_e2a_int
                self.nm_e2a_er = self.nm_e2a_er_stat + self.nm_e2a_er_ekm + self.nm_e2a_er_gp
                self.nm_eps = self.nm_e2a * self.nm_den
                self.nm_eps_er = self.nm_e2a_er * self.nm_den
                #
            #
        elif self.model_lo == 'mbpt':
            #
            if self.param_lo == "2010":
                #
                self.flag_kf = False
                self.flag_den = False
                #
                self.ref = "K. Hebeler, et al, Phys. Rev. Lett. 105, 161102 (2010)"
                self.note = "chiral NN forces with SRG and leading 3N forces."
                self.marker = "s"
                self.every = 1
                self.e_er = False
                self.p_er = False
                self.cs2_er = False
                self.linestyle = "solid"
                if os.path.exists(file_NM):
                    self.nm_den, self.nm_pre = np.loadtxt( file_NM, usecols=(0, 1), unpack=True )
                self.nm_kfn = nuda.kf_n(self.nm_den)
                # self.nm_pre_er = np.abs( 0.01 * self.nm_pre )
                #
                # chemical potential
                # self.nm_chempot = ( self.nm_pre + self.nm_eps ) / self.nm_den
                #
            elif self.param_lo == "2013":
                #
                self.flag_kf = False
                self.flag_den = True
                #
                self.ref = "I. Tews et al., PRL 110, 032504 (2013)"
                self.note = "write here notes about this EOS."
                self.marker = "s"
                self.every = 1
                self.linestyle = "solid"
                self.e_er = True
                self.p_er = False
                self.cs2_er = False
                if os.path.exists(file_NM):
                    self.nm_den, self.nm_e2a_int_lo, self.nm_e2a_int_up, self.nm_pre_lo, self.nm_pre_up = np.loadtxt( file_NM, usecols=(0, 1, 2, 3, 4), unpack=True )
                self.nm_kfn = nuda.kf_n(self.nm_den)
                self.nm_e2a_int = np.array(0.5 * (self.nm_e2a_int_up + self.nm_e2a_int_lo))
                self.nm_e2a = self.nm_rmass + self.nm_e2a_int
                self.nm_e2a_er = 0.5 * (self.nm_e2a_int_up - self.nm_e2a_int_lo)
                self.nm_eps = self.nm_e2a * self.nm_den
                self.nm_eps_er = self.nm_e2a_er * self.nm_den
                self.nm_pre = 0.5 * (self.nm_pre_up + self.nm_pre_lo)
                self.nm_pre_er = 0.5 * (self.nm_pre_up - self.nm_pre_lo)
                #
                # chemical potential
                #self.nm_chempot = (
                #    np.array(self.nm_pre) + np.array(self.nm_eps)
                #) / np.array(self.nm_den)
                #self.nm_chempot_er = (
                #    np.array(self.nm_pre_er) + np.array(self.nm_eps_er)
                #) / np.array(self.nm_den)
                #
                # enthalpy
                self.nm_h2a = self.nm_e2a + self.nm_pre / self.nm_den
                #
                # sound speed
                x = np.insert(self.nm_den, 0, 0.0)
                y = np.insert(self.nm_pre, 0, 0.0)
                cs_nm_pre = CubicSpline(x, y)
                self.nm_cs2 = cs_nm_pre(self.nm_den, 1) / self.nm_h2a
                #
            elif self.param_lo == "2016":
                #
                self.flag_kf = False
                self.flag_den = True
                #
                self.ref = "C. Drischler, K. Hebeler, A. Schwenk, Phys. Rev. C 93, 054314 (2016)."
                self.note = ""
                self.marker = "s"
                self.linestyle = "solid"
                self.e_er = True
                self.p_er = False
                self.cs2_er = False
                self.every = 4
                # read the results for the 7 hamiltonians
                length = np.zeros((11), dtype=int)
                den = np.zeros((11, 35))
                e2a = np.zeros((10, 11, 35))
                e2a_up = np.zeros((11, 35))
                e2a_lo = np.zeros((11, 35))
                e2a_av = np.zeros((11, 35))
                e2a_er = np.zeros((11, 35))
                for i in range(0, 11):
                    file_in = os.path.join( nuda.param.path_data, "matter/type/MBPT/2016-AM-0."+str(i)+".dat" )
                    if i ==0:
                        file_in = os.path.join( nuda.param.path_data, "matter/type/MBPT/2016-SM.dat" )
                    if i ==10:
                        file_in = os.path.join( nuda.param.path_data, "matter/type/MBPT/2016-NM.dat" )
                    if nuda.env.verb: print("Reads file:", file_in)
                    deni, e2a_1, e2a_2, e2a_3, e2a_4, e2a_5, e2a_6, e2a_7 = np.genfromtxt( file_in, usecols=(0, 1, 2, 3, 4, 5, 6, 7), comments="#", unpack=True )
                    length[i] = len(deni)
                    den[i, 0 : length[i]] = deni
                    den_n = deni * (1.0 + 0.1*i) / 2.0
                    e2a[1, i, 0 : length[i]] = e2a_1
                    e2a[2, i, 0 : length[i]] = e2a_2
                    e2a[3, i, 0 : length[i]] = e2a_3
                    e2a[4, i, 0 : length[i]] = e2a_4
                    e2a[5, i, 0 : length[i]] = e2a_5
                    e2a[6, i, 0 : length[i]] = e2a_6
                    e2a[7, i, 0 : length[i]] = e2a_7
                    # performs average and compute boundaries
                    e2a_up[i, 0 : length[i]] = e2a_1
                    e2a_lo[i, 0 : length[i]] = e2a_1
                    for j in range(length[i]):
                        for k in range(2, 8):
                            if e2a[k, i, j] > e2a_up[i, j]:
                                e2a_up[i, j] = e2a[k, i, j]
                            if e2a[k, i, j] < e2a_lo[i, j]:
                                e2a_lo[i, j] = e2a[k, i, j]
                        e2a_av[i, j] = 0.5 * (e2a_up[i, j] + e2a_lo[i, j])
                        e2a_er[i, j] = 0.5 * (e2a_up[i, j] - e2a_lo[i, j])
                if nuda.env.verb:
                    print("length:", length[:])
                # NM
                self.nm_den = np.array(den[10, :])
                self.nm_kfn = nuda.kf_n(self.nm_den)
                self.nm_e2a_int_up = e2a_up[10, :]
                self.nm_e2a_int_lo = e2a_lo[10, :]
                self.nm_e2a_int = np.array(e2a_av[10, :])
                self.nm_e2a = self.nm_rmass + self.nm_e2a_int
                self.nm_e2a_er = e2a_er[10, :]
                self.nm_eps = self.nm_e2a * self.nm_den
                self.nm_eps_er = self.nm_e2a_er * self.nm_den
                # SM
                self.sm_den = np.array(den[0, :])
                self.sm_kfn = nuda.kf_n(nuda.cst.half * self.sm_den)
                self.sm_e2a_int_up = e2a_up[0, :]
                self.sm_e2a_int_lo = e2a_lo[0, :]
                self.sm_e2a_int = np.array(e2a_av[0, :])
                self.sm_e2a = self.sm_rmass + self.sm_e2a_int
                self.sm_e2a_er = e2a_er[0, :]
                self.sm_eps = self.sm_e2a * self.sm_den
                self.sm_eps_er = self.sm_e2a_er * self.sm_den
                # AM
                self.am_den = np.zeros((11,35))
                self.am_xn = np.zeros((11))
                self.am_xp = np.zeros((11))
                self.am_kfn = np.zeros((11,35))
                self.am_rmass = np.zeros((11))
                self.am_e2a_int = np.zeros((11,8,35))
                self.am_eps_int = np.zeros((11,8,35))
                self.am_e2a = np.zeros((11,8,35))
                self.am_eps = np.zeros((11,8,35))
                self.am_e2a_int_av = np.zeros((11,35))
                self.am_e2a_int_er = np.zeros((11,35))
                self.am_eps_int_av = np.zeros((11,35))
                self.am_eps_int_er = np.zeros((11,35))
                self.am_e2a_av = np.zeros((11,35))
                self.am_e2a_er = np.zeros((11,35))
                self.am_eps_av = np.zeros((11,35))
                self.am_eps_er = np.zeros((11,35))
                for i in range(0, 11):
                    self.am_den[i] = np.array(den[i, :])
                    self.am_xn[i] = 0.5*(1.0+i/10.0)
                    self.am_xp[i] = 0.5*(1.0-i/10.0)
                    self.am_kfn[i] = nuda.kf_n( self.am_xn[i] * self.am_den[i] )
                    self.am_rmass[i] = self.am_xn[i] * nuda.cst.mnc2 + self.am_xp[i] * nuda.cst.mpc2
                    for j in range(1, 8):
                        self.am_e2a_int[i,j] = np.array(e2a[j,i,:])
                        self.am_eps_int[i,j] = self.am_e2a_int[i,j] * self.am_den[i]
                        self.am_e2a[i,j] = self.am_rmass[i] + self.am_e2a_int[i,j]
                        self.am_eps[i,j] = self.am_e2a[i,j] * self.am_den[i]
                    self.am_e2a_int_av[i] = np.array(e2a_av[i, :])
                    self.am_e2a_int_er[i] = np.array(e2a_er[i, :])
                    self.am_eps_int_av[i] = self.am_e2a_int_av[i] * self.am_den[i] 
                    self.am_eps_int_er[i] = self.am_e2a_int_er[i] * self.am_den[i]
                    self.am_e2a_av[i] = self.am_rmass[i] + self.am_e2a_int_av[i]
                    self.am_e2a_er[i] = self.am_rmass[i] + self.am_e2a_int_er[i]
                    self.am_eps_av[i] = self.am_e2a_av[i] * self.am_den[i] 
                    self.am_eps_er[i] = self.am_e2a_er[i] * self.am_den[i]
                #
                # Note: here I define the pressure as the derivative of the centroid energy
                # It would however be better to compute the presure for each models and only
                # after that, estimate the centroid and uncertainty.
                #
            elif self.param_lo == "2019-l59" or self.param_lo == "2019-l69":
                #
                self.flag_kf = False
                self.flag_den = True
                #
                # here, the L59 case is compute alone, it would be interesting to compute the uncertainty
                # in the previous MBPT calculation (based on H1-H7) adding this new calculation.
                #
                self.ref = "C. Drischler, K. Hebeler, A. Schwenk, Phys. Rev. Lett. 122, 042501 (2019)"
                self.note = ""
                self.marker = "s"
                self.every = 2
                self.e_er = False
                self.p_er = False
                self.cs2_er = False
                self.linestyle = "solid"
                if os.path.exists(file_SM):
                    self.sm_kfn, self.sm_den, Kin, HF_tot, Scnd_tot, Trd_tot, Fth_tot, self.sm_e2a_int = np.loadtxt( file_SM, usecols=(0, 1, 2, 3, 4, 5, 6, 7), comments="#", unpack=True )
                self.sm_e2a = self.sm_rmass + self.sm_e2a_int
                self.sm_e2a_er = np.abs( uncertainty_stat(self.sm_den, er="MBPT") * self.sm_e2a_int )
                self.sm_eps = self.sm_e2a * self.sm_den
                self.sm_eps_er = self.sm_e2a_er * self.sm_den
                if os.path.exists(file_NM):
                    self.nm_kfn, self.nm_den, Kin, HF_tot, Scnd_tot, Trd_tot, Fth_tot, self.nm_e2a_int = np.loadtxt( file_NM, usecols=(0, 1, 2, 3, 4, 5, 6, 7), comments="#", unpack=True )
                self.nm_e2a = self.nm_rmass + self.nm_e2a_int
                self.nm_e2a_er = np.abs( uncertainty_stat(self.nm_den, er="MBPT") * self.nm_e2a_int )
                self.nm_eps = self.nm_e2a * self.nm_den
                self.nm_eps_er = self.nm_e2a_er * self.nm_den
                #
            elif self.param_lo == "2020":
                #
                self.flag_kf = False
                self.flag_den = True
                #
                self.ref = "C. Drischler, R.J. Furnstahl, J.A. Melendez, D.R. Phillips, Phys. Rev. Lett. 125(20), 202702 (2020).; C. Drischler, J. A. Melendez, R. J. Furnstahl, and D. R. Phillips, Phys. Rev. C 102, 054315"
                self.note = ""
                self.marker = "o"
                self.linestyle = "solid"
                self.every = 6
                self.e_er = True
                self.p_er = False
                self.cs2_er = False
                if os.path.exists(file_SM):
                    self.sm_den, self.sm_e2a_lo, self.sm_e2a_lo_er, self.sm_e2a_nlo, self.sm_e2a_nlo_er, self.sm_e2a_n2lo, self.sm_e2a_n2lo_er, self.sm_e2a_n3lo, self.sm_e2a_n3lo_er = np.loadtxt( file_SM, usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8), delimiter=" ", comments="#", unpack=True )
                self.sm_kfn = nuda.kf_n(nuda.cst.half * self.sm_den)
                self.sm_e2a_int = self.sm_e2a_n3lo
                self.sm_e2a = self.sm_rmass + self.sm_e2a_int
                self.sm_e2a_er = self.sm_e2a_n3lo_er
                self.sm_eps = self.sm_e2a * self.sm_den
                self.sm_eps_er = self.sm_e2a_er * self.sm_den
                if os.path.exists(file_NM):
                    self.nm_den, self.nm_e2a_lo, self.nm_e2a_lo_er, self.nm_e2a_nlo, self.nm_e2a_nlo_er, self.nm_e2a_n2lo, self.nm_e2a_n2lo_er, self.nm_e2a_n3lo, self.nm_e2a_n3lo_er = np.loadtxt( file_NM, usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8), delimiter=" ", comments="#", unpack=True )
                self.nm_kfn = nuda.kf_n(self.nm_den)
                self.nm_e2a_int = self.nm_e2a_n3lo
                self.nm_e2a = self.nm_rmass + self.nm_e2a_int
                self.nm_e2a_er = self.nm_e2a_n3lo_er
                self.nm_eps = self.nm_e2a * self.nm_den
                self.nm_eps_er = self.nm_e2a_er * self.nm_den
                #
            elif "2024-" in self.param_lo :
                #
                self.flag_kf = False
                self.flag_den = True
                #
                if self.param_lo == "2024-dn2lo450":
                    cols_sm=(0,3)
                    cols_nm=(0,2)
                elif self.param_lo == "2024-dn2lo500":
                    cols_sm=(0,3)
                    cols_nm=(0,2)
                elif self.param_lo == "2024-dn2logo394":
                    cols_sm=(0,3)
                    cols_nm=(0,2)
                elif self.param_lo == "2024-dn2logo450":
                    cols_sm=(0,3)
                    cols_nm=(0,3)
                elif self.param_lo == "2024-n2losat":
                    cols_sm=(0,3)
                    cols_nm=(0,2)
                self.ref = "F. Marino, W.G. Jiang, and S.J. Novario, Phys. Rev. C 110, 054322 (2024)."
                self.note = "We consider MBPT(3) when possible, otherwise MBPT(2)."
                self.model = model
                self.marker = "x"
                self.linestyle = "solid"
                self.every = 1
                self.e_er = False
                self.p_er = False
                self.cs2_er = False
                self.sm_den, self.sm_e2a_n2lo = np.loadtxt( file_SM, usecols=cols_sm, comments="#", unpack=True )
                self.sm_e2a_int = self.sm_e2a_n2lo
                self.nm_den, self.nm_e2a_n2lo = np.loadtxt( file_NM, usecols=cols_nm, comments="#", unpack=True )
                self.nm_e2a_int = self.nm_e2a_n2lo
                #
                self.nm_e2a = self.nm_rmass + self.nm_e2a_int
                self.sm_e2a = self.sm_rmass + self.sm_e2a_int
                self.nm_eps = self.nm_e2a * self.nm_den
                self.sm_eps = self.sm_e2a * self.sm_den
                self.nm_kfn = nuda.kf_n( self.nm_den )
                self.sm_kfn = nuda.kf_n( nuda.cst.half * self.sm_den )
                self.nm_e2a_er = np.abs( uncertainty_stat(self.nm_den, er="MBPT") * self.nm_e2a_int )
                self.sm_e2a_er = np.abs( uncertainty_stat(self.sm_den, er="MBPT") * self.sm_e2a_int )
                self.nm_eps_er = self.nm_e2a_er * self.nm_den
                self.sm_eps_er = self.sm_e2a_er * self.sm_den
                #
            #
        elif model.lower() == 'nleft':
            #
            if self.param_lo == "2024":
                #
                self.flag_kf = False
                self.flag_den = False
                #
                self.ref = "S. Elhatisari, L. Bovermann, Y.-Z. Ma et al., Nature 630, 59 (2024)."
                self.note = ""
                self.marker = "s"
                self.linestyle = "solid"
                self.every = 2
                self.e_er = True
                self.p_er = False
                self.cs2_er = False
                #
                # Read SM results
                #
                if os.path.exists(file_SM):
                    self.sm_A, self.sm_L, self.sm_den, self.sm_etot_int_2bf, self.sm_etot_2bf_er, self.sm_etot_int, self.sm_etot_er = np.loadtxt( file_SM, usecols=(0, 1, 2, 3, 4, 5, 6), comments="#", unpack=True, delimiter="," )
                self.sm_kfn = nuda.kf_n(nuda.cst.half * self.sm_den)
                self.sm_e2a_int_data = self.sm_etot_int / self.sm_A
                self.sm_e2a_er_data = self.sm_etot_er / self.sm_A
                self.sm_e2a_int_2bf_data = self.sm_etot_int_2bf / self.sm_A
                self.sm_e2a_2bf_er_data = self.sm_etot_2bf_er / self.sm_A
                self.sm_e2a_data = self.sm_rmass + self.sm_e2a_int_data
                self.sm_eps_data = self.sm_e2a_data * self.sm_den
                self.sm_eps_er_data = self.sm_e2a_er_data * self.sm_den
                # fit with EFFG
                xdata = self.sm_kfn
                ydata = self.sm_e2a_int_data
                sm_popt, sm_pcov = curve_fit(func_e2a_NLEFT2024, xdata, ydata)
                print("sm_popt:", sm_popt)
                print("sm_pcov:", sm_pcov)
                self.sm_pfit = sm_popt
                self.sm_per = np.sqrt(np.diag(sm_pcov))
                # analyse the uncertainties for e2a, pre, cs2
                self.sm_pcer = np.zeros((100, 3), dtype=float)
                self.sm_e2a_int = func_e2a_NLEFT2024(xdata, *self.sm_pfit)
                self.sm_e2a = self.sm_rmass + self.sm_e2a_int
                self.sm_e2a_int_min = self.sm_e2a_int.copy()
                self.sm_e2a_int_max = self.sm_e2a_int.copy()
                self.sm_pre = func_pre_NLEFT2024(xdata, self.sm_den, *self.sm_pfit)
                self.sm_pre_min = self.sm_pre.copy()
                self.sm_pre_max = self.sm_pre.copy()
                self.sm_dpredn = func_dpredn_NLEFT2024(xdata, self.sm_den, *self.sm_pfit)
                self.sm_dpredn_min = self.sm_dpredn.copy()
                self.sm_dpredn_max = self.sm_dpredn.copy()
                for k in range(100):
                    b = self.sm_pfit[0] + 0.1 * (random.random() - 0.5) * self.sm_per[0]
                    c = self.sm_pfit[1] + 0.1 * (random.random() - 0.5) * self.sm_per[1]
                    d = self.sm_pfit[2] + 0.1 * (random.random() - 0.5) * self.sm_per[2]
                    self.sm_pcer[k, 0] = b
                    self.sm_pcer[k, 1] = c
                    self.sm_pcer[k, 2] = d
                    param = np.array([b, c, d])
                    # e2a
                    af = func_e2a_NLEFT2024(xdata, *param)
                    for l, val in enumerate(af):
                        if val > self.sm_e2a_int_max[l]:
                            self.sm_e2a_int_max[l] = val
                        if val < self.sm_e2a_int_min[l]:
                            self.sm_e2a_int_min[l] = val
                    self.sm_e2a_er = 0.5 * (self.sm_e2a_int_max - self.sm_e2a_int_min)
                    # pre
                    af = func_pre_NLEFT2024(xdata, self.sm_den, *param)
                    for l, val in enumerate(af):
                        if val > self.sm_pre_max[l]:
                            self.sm_pre_max[l] = val
                        if val < self.sm_pre_min[l]:
                            self.sm_pre_min[l] = val
                    self.sm_pre_er = 0.5 * (self.sm_pre_max - self.sm_pre_min)
                    # dpdn
                    af = func_dpredn_NLEFT2024(xdata, self.sm_den, *param)
                    for l, val in enumerate(af):
                        if val > self.sm_dpredn_max[l]:
                            self.sm_dpredn_max[l] = val
                        if val < self.sm_dpredn_min[l]:
                            self.sm_dpredn_min[l] = val
                    self.sm_dpredn_er = 0.5 * (self.sm_dpredn_max - self.sm_dpredn_min)
                # print('sm_pcer:',self.sm_pcer)
                # self.sm_e2a = self.sm_e2a_fit
                # self.sm_e2a_er = self.sm_e2a_fit_er
                self.sm_eps = self.sm_e2a * self.sm_den
                self.sm_eps_er = self.sm_e2a_er * self.sm_den
                #
                # Read NM results
                if os.path.exists(file_NM):
                    self.nm_A, self.nm_L, self.nm_den, self.nm_etot_int, self.nm_etot_er = np.loadtxt( file_NM, usecols=(0, 1, 2, 3, 4), comments="#", unpack=True, delimiter="," )
                self.nm_kfn = nuda.kf_n(self.nm_den)
                self.nm_e2a_int_data = self.nm_etot_int / self.nm_A
                self.nm_e2a_er_data = self.nm_etot_er / self.nm_A
                self.nm_e2a_data = self.nm_rmass + self.nm_e2a_int_data
                self.nm_eps_data = self.nm_e2a_data * self.nm_den
                self.nm_eps_er_data = self.nm_e2a_er_data * self.nm_den
                # fit with EFFG
                xdata = self.nm_kfn
                ydata = self.nm_e2a_int_data
                nm_popt, nm_pcov = curve_fit(func_e2a_NLEFT2024, xdata, ydata)
                print("nm_popt:", nm_popt)
                print("nm_pcov:", nm_pcov)
                self.nm_pfit = nm_popt
                self.nm_per = np.sqrt(np.diag(nm_pcov))
                self.nm_pcer = np.zeros((100, 3), dtype=float)
                self.nm_e2a_int = func_e2a_NLEFT2024(xdata, *self.nm_pfit)
                self.nm_e2a = self.nm_rmass + self.nm_e2a_int
                self.nm_e2a_int_min = self.nm_e2a_int.copy()
                self.nm_e2a_int_max = self.nm_e2a_int.copy()
                self.nm_pre = func_pre_NLEFT2024(xdata, self.nm_den, *self.nm_pfit)
                self.nm_pre_min = self.nm_pre.copy()
                self.nm_pre_max = self.nm_pre.copy()
                self.nm_dpredn = func_dpredn_NLEFT2024(xdata, self.nm_den, *self.nm_pfit)
                self.nm_dpredn_min = self.nm_dpredn.copy()
                self.nm_dpredn_max = self.nm_dpredn.copy()
                for k in range(100):
                    b = self.nm_pfit[0] + 0.2 * (random.random() - 0.5) * self.nm_per[0]
                    c = self.nm_pfit[1] + 0.2 * (random.random() - 0.5) * self.nm_per[1]
                    d = self.nm_pfit[2] + 0.2 * (random.random() - 0.5) * self.nm_per[2]
                    self.nm_pcer[k, 0] = b
                    self.nm_pcer[k, 1] = c
                    self.nm_pcer[k, 2] = d
                    param = np.array([b, c, d])
                    # e2a
                    af = func_e2a_NLEFT2024(xdata, *param)
                    for l, val in enumerate(af):
                        if val > self.nm_e2a_int_max[l]:
                            self.nm_e2a_int_max[l] = val
                        if val < self.nm_e2a_int_min[l]:
                            self.nm_e2a_int_min[l] = val
                    self.nm_e2a_er = 0.5 * (self.nm_e2a_int_max - self.nm_e2a_int_min)
                    # pre
                    af = func_pre_NLEFT2024(xdata, self.nm_den, *param)
                    for l, val in enumerate(af):
                        if val > self.nm_pre_max[l]:
                            self.nm_pre_max[l] = val
                        if val < self.nm_pre_min[l]:
                            self.nm_pre_min[l] = val
                    self.nm_pre_er = 0.5 * (self.nm_pre_max - self.nm_pre_min)
                    # dpdn
                    af = func_dpredn_NLEFT2024(xdata, self.nm_den, *param)
                    for l, val in enumerate(af):
                        if val > self.nm_dpredn_max[l]:
                            self.nm_dpredn_max[l] = val
                        if val < self.nm_dpredn_min[l]:
                            self.nm_dpredn_min[l] = val
                    self.nm_dpredn_er = 0.5 * (self.nm_dpredn_max - self.nm_dpredn_min)
                # print('nm_pcer:',self.nm_pcer)
                # self.nm_e2a = self.nm_e2a_fit
                # self.nm_e2a_er = self.nm_e2a_fit_er
                self.nm_eps = self.nm_e2a * self.nm_den
                self.nm_eps_er = self.nm_e2a_er * self.nm_den
                self.nm_pre = self.nm_pre
                self.nm_pre_er = self.nm_pre_er
                self.nm_dpredn = self.nm_dpredn
                self.nm_dpredn_er = self.nm_dpredn_er
                #
                # chemical potential
                #self.nm_chempot = (
                #    np.array(self.nm_pre) + np.array(self.nm_eps)
                #) / np.array(self.nm_den)
                #self.nm_chempot_er = (
                #    np.array(self.nm_pre_er) + np.array(self.nm_eps_er)
                #) / np.array(self.nm_den)
                #self.sm_chempot = (
                #    np.array(self.sm_pre) + np.array(self.sm_eps)
                #) / np.array(self.sm_den)
                #self.sm_chempot_er = (
                #    np.array(self.sm_pre_er) + np.array(self.sm_eps_er)
                #) / np.array(self.sm_den)
                #
                # enthalpy
                self.sm_h2a = self.sm_e2a + self.sm_pre / self.sm_den
                self.sm_h2a_er = self.sm_e2a_er + self.sm_pre_er / self.sm_den
                self.nm_h2a = self.nm_e2a + self.nm_pre / self.nm_den
                self.nm_h2a_er = self.nm_e2a_er + self.nm_pre_er / self.nm_den
                #
                # sound speed
                self.sm_cs2 = self.sm_dpredn / self.sm_h2a
                self.sm_cs2_er = np.abs(self.sm_dpredn_er / self.sm_h2a) + np.abs(
                    self.sm_dpredn * self.sm_h2a_er / self.sm_h2a )
                self.nm_cs2 = self.nm_dpredn / self.nm_h2a
                self.nm_cs2_er = np.abs(self.nm_dpredn_er / self.nm_h2a) + np.abs(
                    self.nm_dpredn * self.nm_h2a_er / self.nm_h2a )
                #
            #
        elif self.model_lo == 'bhf2bf' or self.model_lo == 'bhf23bf':
            #
            if self.param_lo == "2006-av18":
                #
                self.flag_kf = False
                self.flag_den = True
                #
                self.ref = "L.G. Cao, U. Lombardo, C.W. Shen, N.V. Giai, Phys. Rev. C 73, 014313 (2006)"
                self.note = ""
                self.marker = "o"
                self.every = 1
                self.linestyle = "solid"
                self.e_er = False
                self.p_er = False
                self.cs2_er = False
                #
                if os.path.exists(file_NM):
                    self.nm_den, self.nm_e2a_int = np.loadtxt( file_NM, usecols=(0, 1), unpack=True )
                self.nm_kfn = nuda.kf_n(self.nm_den)
                self.nm_e2a = self.nm_rmass + self.nm_e2a_int
                self.nm_e2a_er = np.abs( uncertainty_stat(self.nm_den, er="MBPT") * self.nm_e2a_int )
                self.nm_eps = self.nm_e2a * self.nm_den
                self.nm_eps_er = self.nm_e2a_er * self.nm_den
                #
                if os.path.exists(file_SM):
                    self.sm_den, self.sm_e2a_int = np.loadtxt( file_SM, usecols=(0, 1), unpack=True )
                self.sm_kfn = nuda.kf_n(nuda.cst.half * self.sm_den)
                self.sm_e2a = self.sm_rmass + self.sm_e2a_int
                self.sm_e2a_er = np.abs( uncertainty_stat(self.sm_den, er="MBPT") * self.sm_e2a_int )
                self.sm_eps = self.sm_e2a * self.sm_den
                self.sm_eps_er = self.sm_e2a_er * self.sm_den
                #
            elif "2024" in self.param_lo:
                #
                self.flag_kf = False
                self.flag_den = True
                #
                self.ref = "I. Vida\\~na, J. Margueron, H.J. Schulze, Universe 10, 5 (2024)."
                self.note = ""
                self.marker = "o"
                self.linestyle = "solid"
                self.every = 2
                self.e_er = False
                self.p_er = False
                self.cs2_er = False
                #
                if os.path.exists(file_SM):
                    self.sm_den, self.sm_vS0T0, self.sm_vS0T1, self.sm_vS1T0, self.sm_vS1T1, self.sm_vtot, self.sm_kin, self.sm_etot = np.loadtxt( file_SM, usecols=(0, 1, 2, 3, 4, 5, 6, 7), comments="#", unpack=True )
                self.sm_den_min = min(self.sm_den)
                self.sm_den_max = max(self.sm_den)
                self.sm_kfn = nuda.kf_n(nuda.cst.half * self.sm_den)
                self.sm_kf = self.sm_kfn
                self.sm_e2a_int = self.sm_etot
                self.sm_e2a = self.sm_rmass + self.sm_e2a_int
                self.sm_e2a_er = np.abs( uncertainty_stat(self.sm_den, er="MBPT") * self.sm_e2a_int )
                self.sm_eps = self.sm_e2a * self.sm_den
                self.sm_eps_er = self.sm_e2a_er * self.sm_den
                #
                if os.path.exists(file_NM):
                    self.nm_den, self.nm_vS0T0, self.nm_vS0T1, self.nm_vS1T0, self.nm_vS1T1, self.nm_vtot, self.nm_kin, self.nm_etot = np.loadtxt( file_NM, usecols=(0, 1, 2, 3, 4, 5, 6, 7), comments="#", unpack=True )
                self.nm_den_min = min(self.sm_den)
                self.sm_den_max = max(self.sm_den)
                self.nm_kfn = nuda.kf_n(self.nm_den)
                self.nm_e2a_int = self.nm_etot
                self.nm_e2a = self.nm_rmass + self.nm_e2a_int
                self.nm_e2a_er = np.abs( uncertainty_stat(self.nm_den, er="MBPT") * self.nm_e2a_int )
                self.nm_eps = self.nm_e2a * self.nm_den
                self.nm_eps_er = self.nm_e2a_er * self.nm_den
                #
            #
        elif self.model_lo == 'scgf':
            #
            if "2020" in self.param_lo:
                #
                self.flag_kf = False
                self.flag_den = True
                #
                self.ref = "A. Rios, Front. Phys. 8 387 (2020)"
                self.note = ""
                self.marker = "+"
                self.linestyle = "solid"
                self.every = 1
                self.e_er = False
                self.p_er = False
                self.cs2_er = False
                if os.path.exists(file_SM):
                    self.sm_den, self.sm_chempot_n3lo, self.sm_e2a_n3lo, self.sm_pre_n3lo = np.loadtxt( file_SM, usecols=(0, 2, 3, 6), comments="#", unpack=True )
                self.sm_e2a_int = self.sm_e2a_n3lo
                if os.path.exists(file_NM):
                    self.nm_den, self.nm_chempot_n3lo, self.nm_e2a_n3lo, self.nm_pre_n3lo = np.loadtxt( file_NM, usecols=(0, 2, 3, 6), comments="#", unpack=True )
                self.nm_e2a_int = self.nm_e2a_n3lo
                #
                self.nm_e2a = self.nm_rmass + self.nm_e2a_int
                self.sm_e2a = self.sm_rmass + self.sm_e2a_int
                self.nm_eps = self.nm_e2a * self.nm_den
                self.sm_eps = self.sm_e2a * self.sm_den
                self.nm_kfn = nuda.kf_n( self.nm_den )
                self.sm_kfn = nuda.kf_n( nuda.cst.half * self.sm_den )
                self.nm_e2a_er = np.abs( uncertainty_stat(self.nm_den, er="MBPT") * self.nm_e2a_int )
                self.sm_e2a_er = np.abs( uncertainty_stat(self.sm_den, er="MBPT") * self.sm_e2a_int )
                self.nm_eps_er = self.nm_e2a_er * self.nm_den
                self.sm_eps_er = self.sm_e2a_er * self.sm_den
                #
            elif "2024" in self.param_lo:
                #
                self.flag_kf = False
                self.flag_den = True
                #
                if self.param_lo == "2024-dn2lo450":
                    cols_sm=(0,7)
                    cols_nm=(0,5)
                elif self.param_lo == "2024-dn2lo500":
                    cols_sm=(0,7)
                    cols_nm=(0,5)
                elif self.param_lo == "2024-dn2logo394":
                    cols_sm=(0,7)
                    cols_nm=(0,5)
                elif self.param_lo == "2024-dn2logo450":
                    cols_sm=(0,7)
                    cols_nm=(0,7)
                elif self.param_lo == "2024-n2losat":
                    cols_sm=(0,7)
                    cols_nm=(0,7)
                self.ref = "F. Marino, W.G. Jiang, and S.J. Novario, Phys. Rev. C 110, 054322 (2024)."
                self.note = "We consider ADC(3)-D when possible, otherwise ADC(3)"
                self.marker = "x"
                self.linestyle = "solid"
                self.every = 1
                self.e_er = False
                self.p_er = False
                self.cs2_er = False
                if os.path.exists(file_SM):
                    self.sm_den, self.sm_e2a_n2lo = np.loadtxt( file_SM, usecols=cols_sm, comments="#", unpack=True )
                self.sm_e2a_int = self.sm_e2a_n2lo
                if os.path.exists(file_NM):
                    self.nm_den, self.nm_e2a_n2lo = np.loadtxt( file_NM, usecols=cols_nm, comments="#", unpack=True )
                self.nm_e2a_int = self.nm_e2a_n2lo
                #
                self.nm_e2a = self.nm_rmass + self.nm_e2a_int
                self.sm_e2a = self.sm_rmass + self.sm_e2a_int
                self.nm_eps = self.nm_e2a * self.nm_den
                self.sm_eps = self.sm_e2a * self.sm_den
                self.nm_kfn = nuda.kf_n( self.nm_den )
                self.sm_kfn = nuda.kf_n( nuda.cst.half * self.sm_den )
                self.nm_e2a_er = np.abs( uncertainty_stat(self.nm_den, er="MBPT") * self.nm_e2a_int )
                self.sm_e2a_er = np.abs( uncertainty_stat(self.sm_den, er="MBPT") * self.sm_e2a_int )
                self.nm_eps_er = self.nm_e2a_er * self.nm_den
                self.sm_eps_er = self.sm_e2a_er * self.sm_den
                #
            #
        elif self.model_lo == 'cc':
            #
            if "2024" in self.param_lo:
                #
                self.flag_kf = False
                self.flag_den = True
                #
                if self.param_lo == "2024-dn2lo450":
                    cols_sm=(0,5)
                    cols_nm=(0,4)
                elif self.param_lo == "2024-dn2lo500":
                    cols_sm=(0,5)
                    cols_nm=(0,4)
                elif self.param_lo == "2024-dn2logo394":
                    cols_sm=(0,5)
                    cols_nm=(0,4)
                elif self.param_lo == "2024-dn2logo450":
                    cols_sm=(0,5)
                    cols_nm=(0,5)
                elif self.param_lo == "2024-n2losat":
                    cols_sm=(0,5)
                    cols_nm=(0,5)
                self.ref = "F. Marino, W.G. Jiang, and S.J. Novario, Phys. Rev. C 110, 054322 (2024)."
                self.note = "we consider CCD(T)"
                self.marker = "x"
                self.linestyle = "solid"
                self.every = 1
                self.e_er = False
                self.p_er = False
                self.cs2_er = False
                if os.path.exists(file_SM):
                    self.sm_den, self.sm_e2a_n2lo = np.loadtxt( file_SM, usecols=cols_sm, comments="#", unpack=True )
                self.sm_e2a_int = self.sm_e2a_n2lo
                if os.path.exists(file_NM):
                    self.nm_den, self.nm_e2a_n2lo = np.loadtxt( file_NM, usecols=cols_nm, comments="#", unpack=True )
                self.nm_e2a_int = self.nm_e2a_n2lo
                #
                self.nm_e2a = self.nm_rmass + self.nm_e2a_int
                self.sm_e2a = self.sm_rmass + self.sm_e2a_int
                self.nm_eps = self.nm_e2a * self.nm_den
                self.sm_eps = self.sm_e2a * self.sm_den
                self.nm_kfn = nuda.kf_n( self.nm_den )
                self.sm_kfn = nuda.kf_n( nuda.cst.half * self.sm_den )
                self.nm_e2a_er = np.abs( uncertainty_stat(self.nm_den, er="MBPT") * self.nm_e2a_int )
                self.sm_e2a_er = np.abs( uncertainty_stat(self.sm_den, er="MBPT") * self.sm_e2a_int )
                self.nm_eps_er = self.nm_e2a_er * self.nm_den
                self.sm_eps_er = self.sm_e2a_er * self.sm_den
            #
        #
        # ==============================
        # END OF
        # Read files associated to model
        # ==============================
        #
        # ==============================
        # Compute thermodynamic quantities
        # ==============================
        #
        print('flag_nm:',self.flag_nm)
        print('flag_sm:',self.flag_sm)
        print('flag_kf:',self.flag_kf)
        print('flag_den:',self.flag_den)
        #
        if self.flag_nm:
            #
            if self.flag_kf:
                #
                # pressure in NM
                x = self.nm_kfn; y = self.nm_e2a_int; 
                cs_nm_e2a = CubicSpline(x, y)
                self.nm_pre = np.array( nuda.cst.third * self.nm_kfn * self.nm_den * cs_nm_e2a( x, 1 ) )
                if self.nm_e2a_er is not None:
                    y_er = self.nm_e2a_er
                    cs_nm_e2a_er = CubicSpline(x, y_er)
                    self.nm_pre_er = np.array( nuda.cst.third * self.nm_kfn * self.nm_den * cs_nm_e2a_er( x, 1 ) )
                # chemical potential
                self.nm_chempot = ( np.array(self.nm_pre) + np.array(self.nm_eps) ) / np.array(self.nm_den)
                if self.nm_pre_er is not None:
                    self.nm_chempot_er = ( np.array(self.nm_pre_er) + np.array(self.nm_eps_er) ) / np.array(self.nm_den)
                #
                # enthalpy
                self.nm_h2a = self.nm_e2a + self.nm_pre / self.nm_den
                #
                # sound speed as density derivative
                x = self.nm_den; y = self.nm_pre
                cs_nm_pre = CubicSpline( x, y )
                self.nm_cs2 = cs_nm_pre( x, 1 ) / self.nm_h2a
                #
                # sound speed as kF derivative
                #x = np.insert(self.nm_kfn, 0, 0.0)
                #y = np.insert(self.nm_pre, 0, 0.0)
                #cs_nm_pre = CubicSpline(x, y)
                #self.nm_cs2 = nuda.cst.third * self.nm_kfn / self.nm_den * cs_nm_pre(self.nm_den, 1) / self.nm_h2a
                #
                # calculate the last element for cs2 since the derivative is numerical
                #y = np.insert(self.nm_cs2, 0, 0.0)
                #cs_nm_cs2 = CubicSpline(x[:-2], y[:-2])
                #self.nm_cs2[-1] = cs_nm_cs2(self.nm_den[-1])
                #
            if self.flag_den:
                #
                # pressure in NM
                x = self.nm_den; y = self.nm_e2a_int; 
                cs_nm_e2a = CubicSpline(x, y)
                self.nm_pre = np.array(self.nm_den**2 * cs_nm_e2a(x, 1))
                if "2020-scgf-am" in model.lower():
                    self.nm_pre = self.nm_pre_n3lo
                if self.nm_e2a_er is not None:
                    y_er = self.nm_e2a_er
                    cs_nm_e2a_er = CubicSpline(x, y_er)
                    self.nm_pre_er = self.nm_den**2 * cs_nm_e2a_er(x, 1)
                #
                # chemical potential
                self.nm_chempot = ( np.array(self.nm_pre) + np.array(self.nm_eps) ) / np.array( x )
                if self.nm_pre_er is not None:
                    self.nm_chempot_er = ( np.array(self.nm_pre_er) + np.array(self.nm_eps_er) ) / np.array( x )
                if "2020-scgf-am" in model.lower():
                    self.nm_chempot = self.nm_chempot_n3lo
                #
                # enthalpy
                self.nm_h2a = self.nm_e2a + self.nm_pre / x
                #
                # sound speed
                y = self.nm_pre
                cs_nm_pre = CubicSpline( x, y )
                self.nm_cs2 = cs_nm_pre( x, 1 ) / self.nm_h2a
                #
            #
        if self.flag_sm:
            #
            if self.flag_kf:
                #
                # pressure in SM
                x = self.sm_kfn; y = self.sm_e2a_int; 
                cs_sm_e2a = CubicSpline( x, y )
                self.sm_pre = np.array( nuda.cst.third * self.sm_kfn * self.sm_den * cs_sm_e2a( x, 1 ) )
                if self.sm_e2a_er is not None:
                    y_er = self.sm_e2a_er
                    cs_sm_e2a_er = CubicSpline(x, y_er)
                    self.sm_pre_er = ( nuda.cst.third * self.sm_kfn * self.sm_den * cs_sm_e2a_er( x, 1 ) )
                #
                # chemical potential
                self.sm_chempot = ( np.array(self.sm_pre) + np.array(self.sm_eps) ) / np.array(self.sm_den)
                if self.sm_pre_er is not None:
                    self.sm_chempot_er = ( np.array(self.sm_pre_er) + np.array(self.sm_eps_er) ) / np.array(self.sm_den)
                #
                # enthalpy
                self.sm_h2a = self.sm_e2a + self.sm_pre / self.sm_den
                #
                # sound speed as density derivative
                #x = np.insert(self.sm_den, 0, 0.0)
                #y = np.insert(self.sm_pre, 0, 0.0)
                x = self.sm_den; y = self.sm_pre
                cs_sm_pre = CubicSpline( x, y )
                self.sm_cs2 = cs_sm_pre(self.sm_den, 1) / self.sm_h2a
                #
                # sound speed as kF derivative
                #x = np.insert(self.nm_kfn, 0, 0.0)
                #y = np.insert(self.sm_pre, 0, 0.0)
                #cs_sm_pre = CubicSpline(x, y)
                #self.sm_cs2 = np.array( nuda.cst.third * self.sm_kfn / self.sm_den * cs_sm_pre(self.sm_den, 1) / self.sm_h2a )
                #
            if self.flag_den:
                #
                # pressure in NM
                x = self.sm_den; y = self.sm_e2a_int
                cs_sm_e2a = CubicSpline( x, y )
                self.sm_pre = np.array( self.sm_den**2 * cs_sm_e2a( x, 1 ) )
                if "2020-scgf-am" in model.lower():
                    self.sm_pre = self.sm_pre_n3lo
                if self.sm_e2a_er is not None:
                    y_er = self.sm_e2a_er
                    cs_sm_e2a_er = CubicSpline(x, y_er)
                    self.sm_pre_er = self.sm_den**2 * cs_sm_e2a_er(self.sm_den, 1)
                #
                # chemical potential
                self.sm_chempot = ( np.array(self.sm_pre) + np.array(self.sm_eps) ) / np.array( x )
                if self.sm_pre_er is not None:
                    self.sm_chempot_er = ( np.array(self.sm_pre_er) + np.array(self.sm_eps_er) ) / np.array( x )
                if "2020-scgf-am" in model.lower():
                    self.sm_chempot = self.sm_chempot_n3lo
                #
                # enthalpy
                self.sm_h2a = self.sm_e2a + self.sm_pre / self.sm_den
                #
                # sound speed
                y = self.sm_pre
                cs_sm_pre = CubicSpline( x, y )
                self.sm_cs2 = cs_sm_pre( x, 1 ) / self.sm_h2a
                #
            #
        #
        # ==============================
        # END OF
        # Compute thermodynamic quantities
        # ==============================
        #
        self.den_unit = 'fm$^{-3}$'
        self.kf_unit  = 'fm$^{-1}$'
        self.e2a_unit = 'MeV'
        self.eps_unit = "MeV fm$^{-3}$"
        self.pre_unit = 'MeV fm$^{-3}$'
        self.gap_unit = 'MeV'
        #
        if nuda.env.verb: print("Exit SetupMatter()")
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
        print("   model:",self.model)
        print("   param:",self.param)
        print("   ref:",self.ref)
        print("   label:",self.label)
        #print("   note:",self.note)
        print("   self.sm_den: ", self.sm_den)
        print("   self.sm_effmass: ", self.sm_effmass)
        if any(self.sm_den): print(f"   sm_den: {np.round(self.sm_den,2)} in {self.den_unit}")
        if any(self.sm_kfn): print(f"   sm_kfn: {np.round(self.sm_kfn,2)} in {self.kfn_unit}")
        if any(self.sm_e2a): print(f"   sm_e2a: {np.round(self.sm_e2a,2)} in {self.e2a_unit}")
        if any(self.sm_cs2): print(f"   sm_cs2: {np.round(self.sm_cs2,2)}")
        if any(self.nm_den): print(f"   nm_den: {np.round(self.nm_den,2)} in {self.den_unit}")
        if any(self.nm_kfn): print(f"   nm_kfn: {np.round(self.nm_kfn,2)} in {self.kfn_unit}")
        if any(self.nm_e2a): print(f"   nm_e2a: {np.round(self.nm_e2a,2)} in {self.e2a_unit}")
        if any(self.nm_cs2): print(f"   nm_cs2: {np.round(self.nm_cs2,2)}")
        if any(self.nm_gap): print(f"   nm_gap: {np.round(self.nm_gap,2)} in {self.gap_unit}")
        # if any(self.sm_den): print(f"   sm_den: {np.round(self.sm_den,3)} in {self.den_unit}")
        if self.den is not None:
            print(f"   den: {np.round(self.den,3)} in {self.den_unit}")
        if self.kfn is not None:
            print(f"   kfn: {np.round(self.den,3)} in {self.kf_unit}")
        if self.asy is not None:
            print(f"   asy: {np.round(self.asy,3)}")
        if self.e2a is not None:
            print(f"   e2a: {np.round(self.e2a,3)} in {self.e2a_unit}")
        if self.eps is not None:
            print(f"   eps: {np.round(self.eps,3)} in {self.eps_unit}")
        if self.pre is not None:
            print(f"   pre: {np.round(self.pre,3)} in {self.pre_unit}")
        if self.cs2 is not None:
            print(f"   cs2: {np.round(self.cs2,2)}")
        if self.sm_den is not None:
            print(f"   sm_den: {np.round(self.sm_den,3)} in {self.den_unit}")
        if self.sm_kfn is not None:
            print(f"   sm_kfn: {np.round(self.sm_kfn,3)} in {self.kf_unit}")
        #if self.sm_chempot is not None:
        #    print(f"   sm_chempot: {np.round(self.sm_chempot,3)} in {self.e2a_unit}")
        if self.sm_effmass is not None:
            print(f"   sm_effmass: {np.round(self.sm_effmass,3)}")
        if self.sm_e2a is not None:
            print(f"   sm_e2a: {np.round(self.sm_e2a,3)} in {self.e2a_unit}")
        if self.sm_e2a_er is not None:
            print(f"   sm_e2a_er: {np.round(self.sm_e2a_er,3)} in {self.e2a_unit}")
        if self.sm_e2a_fit is not None:
            print(f"   sm_e2a_fit: {np.round(self.sm_e2a_fit,3)} in {self.e2a_unit}")
        if self.sm_e2a_fit_er is not None:
            print(
                f"   sm_e2a_fit_er: {np.round(self.sm_e2a_fit_er,3)} in {self.e2a_unit}"
            )
        if self.sm_eps is not None:
            print(f"   sm_eps: {np.round(self.sm_eps,3)} in {self.eps_unit}")
        if self.sm_eps_er is not None:
            print(f"   sm_eps_er: {np.round(self.sm_eps_er,3)} in {self.eps_unit}")
        if self.sm_pre is not None:
            print(f"   sm_pre: {np.round(self.sm_pre,3)} in {self.pre_unit}")
        if self.sm_cs2 is not None:
            print(f"   sm_cs2: {np.round(self.sm_cs2,3)}")
            #
        if self.nm_den is not None:
            print(f"   nm_den: {np.round(self.nm_den,3)} in {self.den_unit}")
        if self.nm_kfn is not None:
            print(f"   nm_kfn: {np.round(self.nm_kfn,3)} in {self.kf_unit}")
        #if self.nm_chempot is not None:
        #    print(f"   nm_chempot: {np.round(self.nm_chempot,3)} in {self.e2a_unit}")
        if self.nm_effmass is not None:
            print(f"   nm_effmass: {np.round(self.nm_effmass,3)}")
        if self.nm_e2a is not None:
            print(f"   nm_e2a: {np.round(self.nm_e2a,3)} in {self.e2a_unit}")
        if self.nm_e2a_er is not None:
            print(f"   nm_e2a_er: {np.round(self.nm_e2a_er,3)} in {self.e2a_unit}")
        if self.nm_e2a_fit is not None:
            print(f"   nm_e2a_fit: {np.round(self.nm_e2a_fit,3)} in {self.e2a_unit}")
        if self.nm_e2a_fit_er is not None:
            print(f"   nm_e2a_fit_er: {np.round(self.nm_e2a_fit_er,3)} in {self.e2a_unit}" )
        if self.nm_eps is not None:
            print(f"   nm_eps: {np.round(self.nm_eps,3)} in {self.eps_unit}")
        if self.nm_eps_er is not None:
            print(f"   nm_eps_er: {np.round(self.nm_eps_er,3)} in {self.eps_unit}")
        if self.nm_pre is not None:
            print(f"   nm_pre: {np.round(self.nm_pre,3)} in {self.pre_unit}")
        if self.nm_cs2 is not None:
            print(f"   nm_cs2: {np.round(self.nm_cs2,3)}")
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
        #: Attribute the number of points for the density.
        self.nden = 10
        #: Attribute providing the full reference to the paper to be citted.
        self.ref = ''
        #: Attribute providing additional notes about the data.
        self.note = ''
        #: Attribute the plot linestyle.
        self.linestyle = None
        #: Attribute the plot to discriminate True uncertainties from False ones.
        self.er = False
        #: Attribute the plot label data.
        self.label = ''
        #: Attribute the plot marker.
        self.marker = None
        #: Attribute the plot every data.
        self.every = 1
        #
        #: Attribute the matter density.
        self.den = None
        #: Attribute the neutron Fermi momentum.
        self.kfn = None
        #: Attribute the matter asymmetry parameter (n_n-n_p)/(n_n+n_p).
        self.asy = None
        #: Attribute the energy per particle.
        self.e2a = None
        #: Attribute the energy per unit volume.
        self.eps = None
        #: Attribute the pressure.
        self.pre = None
        #: Attribute the sound speed.
        self.cs2 = None
        #: Attribute the neutron matter density.
        self.nm_den = None
        #: Attribute the symmetric matter density.
        self.sm_den = None
        #: Attribute the minimum of the neutron matter density.
        self.nm_den_min = None
        #: Attribute the minimum of the symmetric matter density.
        self.sm_den_min = None
        #: Attribute the maximum of the neutron matter density.
        self.nm_den_max = None
        #: Attribute the maximum of the symmetric matter density.
        self.sm_den_max = None
        #: Attribute the neutron matter neutron Fermi momentum.
        self.nm_kfn = None
        #: Attribute the symmetric matter neutron Fermi momentum.
        self.sm_kfn = None
        #: Attribute the symmetric matter Fermi momentum.
        self.nm_kf = None
        #: Attribute the symmetric matter Fermi momentum.
        self.sm_kf = None

        #: Attribute the neutron matter density.
        self.nm_den = []
        #: Attribute the symmetric matter density.
        self.sm_den = []
        #: Attribute the neutron matter neutron Fermi momentum.
        self.nm_kfn = []
        #: Attribute the symmetric matter neutron Fermi momentum.
        self.sm_kfn = []
        #: Attribute the symmetric matter Fermi momentum.
        self.sm_kf = []
        #: Attribute the neutron matter internal energy per particle.
        self.nm_e2a_int = []
        #: Attribute the symmetric matter internal energy per particle.
        self.sm_e2a_int = []
        #: Attribute the neutron matter energy per particle.
        self.nm_e2a = []
        #: Attribute the symmetric matter energy per particle.
        self.sm_e2a = []
        #: Attribute the neutron matter pairing gap.
        self.nm_gap = []
        #: Attribute the symmetric matter pairing gap.
        self.sm_gap = []
        #: Attribute the neutron matter pressure.
        self.nm_pre = []
        #: Attribute the symmetric matter pressure.
        self.sm_pre = []
        #: Attribute the neutron matter enthalpy per particle.
        self.nm_h2a = []
        #: Attribute the symmetric matter enthalpy per particle.
        self.sm_h2a = []
        #: Attribute the symmetric matter enthalpy density.
        self.sm_h2v = []
        #: Attribute the neutron matter enthalpy density.
        self.nm_h2v = []
        #: Attribute the neutron matter sound speed (c_s/c)^2.
        self.nm_cs2 = []
        #: Attribute the symmetric matter sound speed (c_s/c)^2.
        self.sm_cs2 = []

        #: Attribute the neutron matter chemical potential.
        #self.nm_chempot = None
        #: Attribute the uncertainty in the neutron matter chemical potential.
        #self.nm_chempot_er = None
        #: Attribute the symmetric matter chemical potential.
        #self.sm_chempot = None
        #: Attribute the uncertainty in the symmetric matter chemical potential.
        #self.sm_chempot_er = None
        #: Attribute the neutron matter effective mass.
        self.nm_effmass = None
        #: Attribute the symmetric matter effective mass.
        self.sm_effmass = None
        #: Attribute the neutron matter energy per particle.
        self.nm_e2a = None
        #: Attribute the uncertainty in the neutron matter energy per particle.
        self.nm_e2a_er = None
        #: Attribute the neutron matter energy per particle (fit).
        self.nm_e2a_fit = None
        #: Attribute the uncertainty in the neutron matter energy per particle (fit).
        self.nm_e2a_fit_er = None
        #: Attribute the neutron matter potential per particle in the (S=0,T=0) channel.
        self.nm_vS0T0 = None
        #: Attribute the neutron matter potential per particle in the (S=0,T=1) channel.
        self.nm_vS0T1 = None
        #: Attribute the neutron matter potential per particle in the (S=1,T=0) channel.
        self.nm_vS1T0 = None
        #: Attribute the neutron matter potential per particle in the (S=1,T=1) channel.
        self.nm_vS1T1 = None
        #: Attribute the neutron matter total potential per particle.
        self.nm_vtot = None
        #: Attribute the symmetric matter energy per particle.
        self.sm_e2a = None
        #: Attribute the uncertainty in the symmetric matter energy per particle.
        self.sm_e2a_er = None
        #: Attribute the symmetric matter energy per particle (fit).
        self.sm_e2a_fit = None
        #: Attribute the uncertainty in the symmetric matter energy per particle (fit).
        self.sm_e2a_fit_er = None
        #: Attribute the symmetric matter energy per particle in the (S=0,T=0) channel.
        self.sm_vS0T0 = None
        #: Attribute the symmetric matter energy per particle in the (S=0,T=1) channel.
        self.sm_vS0T1 = None
        #: Attribute the symmetric matter energy per particle in the (S=1,T=0) channel.
        self.sm_vS1T0 = None
        #: Attribute the symmetric matter energy per particle in the (S=1,T=1) channel.
        self.sm_vS1T1 = None
        #: Attribute the symmetric matter total potential per particle.
        self.sm_vtot = None
        #: Attribute the neutron matter energy per unit volume.
        self.nm_eps = None
        #: Attribute the uncertainty in the neutron matter energy per unit volume.
        self.nm_eps_er = None
        #: Attribute the symmetric matter energy per unit volume.
        self.sm_eps = None
        #: Attribute the uncertainty in the symmetric matter energy per unit volume.
        self.sm_eps_er = None
        #: Attribute the neutron matter pressure.
        self.nm_pre = None
        #: Attribute the uncertainty in the neutron matter pressure.
        self.nm_pre_er = None
        #: Attribute the neutron matter sound speed.
        self.nm_cs2 = None
        #: Attribute the uncertainty in the neutron matter sound speed.
        self.nm_cs2_er = None
        #: Attribute the symmetric matter pressure.
        self.sm_pre = None
        #: Attribute the uncertainty in the symmetric matter pressure.
        self.sm_pre_er = None
        #: Attribute the symmetric matter sound speed.
        self.sm_cs2 = None
        #: Attribute the uncertainty in the symmetric matter sound speed.
        self.sm_cs2_er = None

        #
        if nuda.env.verb: print("Exit init_self()")
        #
        return self


