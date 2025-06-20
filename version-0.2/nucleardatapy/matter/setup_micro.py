import numpy as np  # 1.15.0
import os
from scipy.interpolate import CubicSpline
from scipy.optimize import curve_fit
import random

import nucleardatapy as nuda


def uncertainty_stat(den, err="MBPT"):
    if err.lower() == "qmc":
        return 0.21 * (den / nuda.cst.nsat)
    elif err.lower() == "mbpt":
        return 0.07 * (den / nuda.cst.nsat)
    else:
        print("no model uncertainty is given")
        print("err:", err)
        print("exit()")
        exit()


def micro_mbs():
    """
    Return a list of many-bodys (mbs) approaches available in this toolkit and print them all on the prompt.

    :return: The list of models with can be 'VAR', 'AFDMC', 'BHF', 'QMC', 'MBPT', 'NLEFT'.
    :rtype: list[str].
    """
    #
    if nuda.env.verb:
        print("\nEnter micro_mbs()")
    #
    mbs = ["VAR", "AFDMC", "BHF2", "BHF23", "QMC", "MBPT", "NLEFT"]
    mbs_lower = [item.lower() for item in mbs]
    #
    if nuda.env.verb:
        print("Exit micro_mbs()")
    #
    return mbs, mbs_lower


def micro_models_mb(mb):
    """
    Return a list with the name of the models available in this toolkit \
    for a given mb appoach and print them all on the prompt. 

    :param mb: The mb approach for which there are parametrizations. \
    They should be chosen among the following options: 'VAR', 'AFDMC', 'BHF', 'QMC', 'MBPT', 'NLEFT'.
    :type mb: str.
    :return: The list of parametrizations.

    These models are the following ones: \
    If `mb` == 'VAR': \
    '1981-VAR-AM-FP', '1998-VAR-AM-APR', '1998-VAR-AM-APR-fit', \
    If `mb` == 'AFDMC': \
    '2012-AFDMC-NM-RES-1', '2012-AFDMC-NM-RES-2', '2012-AFDMC-NM-RES-3', '2012-AFDMC-NM-RES-4', \
    '2012-AFDMC-NM-RES-5', '2012-AFDMC-NM-RES-6', '2012-AFDMC-NM-RES-7', \
    '2012-AFDMC-NM-FIT-1', '2012-AFDMC-NM-FIT-2', '2012-AFDMC-NM-FIT-3', '2012-AFDMC-NM-FIT-4', \
    '2012-AFDMC-NM-FIT-5', '2012-AFDMC-NM-FIT-6', '2012-AFDMC-NM-FIT-7', \
    '2022-AFDMC-NM',
    If `mb` == 'BHF2': \
    '2024-BHF-AM-2BF-Av8p', '2024-BHF-AM-2BF-Av18', '2024-BHF-AM-2BF-BONN', '2024-BHF-AM-2BF-CDBONN', \
    '2024-BHF-AM-2BF-NSC97a', '2024-BHF-AM-2BF-NSC97b', '2024-BHF-AM-2BF-NSC97c', '2024-BHF-AM-2BF-NSC97d', \
    '2024-BHF-AM-2BF-NSC97e', '2024-BHF-AM-2BF-NSC97f', '2024-BHF-AM-2BF-SSCV14',\
    If `mb` == 'BHF23': \
    '2006-BHF-AM-Av18', \
    '2024-BHF-AM-23BF-Av8p', '2024-BHF-AM-23BF-Av18', '2024-BHF-AM-23BF-BONN', '2024-BHF-AM-23BF-CDBONN', \
    '2024-BHF-AM-23BF-NSC97a', '2024-BHF-AM-23BF-NSC97b', '2024-BHF-AM-23BF-NSC97c', '2024-BHF-AM-23BF-NSC97d', \
    '2024-BHF-AM-23BF-NSC97e', '2024-BHF-AM-23BF-NSC97f', '2024-BHF-AM-23BF-SSCV14',\
    '2024-BHF-AM-23BFmicro-Av18', '2024-BHF-AM-23BFmicro-BONNB', '2024-BHF-AM-23BFmicro-NSC93',\
    If `mb` == 'QMC': \
    '2008-QMC-NM-swave', '2010-QMC-NM-AV4', '2009-DLQMC-NM',  \
    '2014-AFQMC-NM', '2016-QMC-NM', \
    '2018-QMC-NM', '2024-QMC-NM', \
    If `mb` == 'MBPT': \
    '2013-MBPT-NM', '2010-MBPT-NM', '2020-MBPT-AM', '2019-MBPT-AM-L59', '2019-MBPT-AM-L69'
    If `mb` == 'NLEFT': \
    '2024-NLEFT-AM', \
    """
    #
    if nuda.env.verb:
        print("\nEnter micro_models_mb()")
    #
    # print('mb:',mb)
    if mb.lower() == "var":
        models = ["1981-VAR-AM-FP", "1998-VAR-AM-APR", "1998-VAR-AM-APR-fit"]
    elif mb.lower() == "afdmc":
        models = [
            "2012-AFDMC-NM-RES-1",
            "2012-AFDMC-NM-RES-2",
            "2012-AFDMC-NM-RES-3",
            "2012-AFDMC-NM-RES-4",
            "2012-AFDMC-NM-RES-5",
            "2012-AFDMC-NM-RES-6",
            "2012-AFDMC-NM-RES-7",
            "2012-AFDMC-NM-FIT-1",
            "2012-AFDMC-NM-FIT-2",
            "2012-AFDMC-NM-FIT-3",
            "2012-AFDMC-NM-FIT-4",
            "2012-AFDMC-NM-FIT-5",
            "2012-AFDMC-NM-FIT-6",
            "2012-AFDMC-NM-FIT-7",
            "2022-AFDMC-NM",
        ]
    elif mb.lower() == "bhf2":
        models = [
            "2024-BHF-AM-2BF-Av18",
            "2024-BHF-AM-2BF-BONN",
            "2024-BHF-AM-2BF-CDBONN",
            "2024-BHF-AM-2BF-NSC97a",
            "2024-BHF-AM-2BF-NSC97b",
            "2024-BHF-AM-2BF-NSC97c",
            "2024-BHF-AM-2BF-NSC97d",
            "2024-BHF-AM-2BF-NSC97e",
            "2024-BHF-AM-2BF-NSC97f",
        ]
        # models = [ '2024-BHF-AM-2BF-Av8p', '2024-BHF-AM-2BF-Av18', '2024-BHF-AM-2BF-BONN', '2024-BHF-AM-2BF-CDBONN', \
        #    '2024-BHF-AM-2BF-NSC97a', '2024-BHF-AM-2BF-NSC97b', '2024-BHF-AM-2BF-NSC97c', '2024-BHF-AM-2BF-NSC97d', \
        #    '2024-BHF-AM-2BF-NSC97e', '2024-BHF-AM-2BF-NSC97f', '2024-BHF-AM-2BF-SSCV14' ]
    elif mb.lower() == "bhf23":
        models = [
            "2006-BHF-AM-Av18",
            "2024-BHF-AM-23BF-Av18",
            "2024-BHF-AM-23BF-BONN",
            "2024-BHF-AM-23BF-CDBONN",
            "2024-BHF-AM-23BF-NSC97a",
            "2024-BHF-AM-23BF-NSC97b",
            "2024-BHF-AM-23BF-NSC97c",
            "2024-BHF-AM-23BF-NSC97d",
            "2024-BHF-AM-23BF-NSC97e",
            "2024-BHF-AM-23BF-NSC97f",
        ]
        # models = [ '2006-BHF-AM-Av18', '2024-BHF-AM-23BF-Av8p', '2024-BHF-AM-23BF-Av18', '2024-BHF-AM-23BF-BONN', \
        #    '2024-BHF-AM-23BF-CDBONN', '2024-BHF-AM-23BF-NSC97a', '2024-BHF-AM-23BF-NSC97b', '2024-BHF-AM-23BF-NSC97c', \
        #    '2024-BHF-AM-23BF-NSC97d', '2024-BHF-AM-23BF-NSC97e', '2024-BHF-AM-23BF-NSC97f', '2024-BHF-AM-23BF-SSCV14' ]
    elif mb.lower() == "qmc":
        models = [
            "2008-QMC-NM-swave",
            "2010-QMC-NM-AV4",
            "2009-DLQMC-NM",
            "2014-AFQMC-NM",
            "2016-QMC-NM",
            "2018-QMC-NM",
            "2024-QMC-NM",
        ]
    elif mb.lower() == "mbpt":
        models = [
            "2013-MBPT-NM",
            "2016-MBPT-AM",
            "2019-MBPT-AM-L59",
            "2019-MBPT-AM-L69",
            "2020-MBPT-AM",
        ]
    # '2010-MBPT-NM' is removed because they do not provide e2a, only pressure
    elif mb.lower() == "nleft":
        models = ["2024-NLEFT-AM"]
    #
    if nuda.env.verb:
        print("models available in the toolkit:", models)
    #
    models_lower = [item.lower() for item in models]
    #
    if nuda.env.verb:
        print("\nExit micro_models_mb()")
    #
    return models, models_lower


def micro_models_mbs(mbs):
    #
    if nuda.env.verb:
        print("\nEnter micro_models_mbs()")
    #
    # print('mbs:',mbs)
    #
    models = []
    for mb in mbs:
        new_models, new_models_lower = micro_models_mb(mb)
        models.extend(new_models)
    #
    if nuda.env.verb:
        print("models available in the toolkit:", models)
    #
    models_lower = [item.lower() for item in models]
    #
    if nuda.env.verb:
        print("Exit micro_models_mbs()")
    #
    return models, models_lower


def micro_models():
    #
    if nuda.env.verb:
        print("\nEnter micro_models()")
    #
    mbs, mbs_lower = micro_mbs()
    # print('mbs:',mbs)
    #
    models, models_lower = micro_models_mbs(mbs)
    #
    if nuda.env.verb:
        print("Exit micro_models()")
    #
    return models, models_lower

def micro_models_mb_matter(mb, matter):
    """
    matter can be 'sm', 'SM' or 'nm', 'NM'
    """
    #
    if nuda.env.verb:
        print("\nEnter micro_models_mb_matter()")
    #
    print("For mb (in " + matter + "):", mb)
    #
    models, models_lower = micro_models_mb(mb)
    #
    models2 = []
    for j, model in enumerate(models):
        if matter.upper() in model or "AM" in model:
            models2.append(model)
    #
    print("models2:", models2)
    models2_lower = [item.lower() for item in models2]
    #
    return models2, models2_lower

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


class setupMicro:
    """
    Instantiate the object with microscopic results choosen \
    by the toolkit practitioner.

    This choice is defined in `model`, which can chosen among \
    the following choices: \
    '1981-VAR-AM-FP', '1998-VAR-AM-APR', '1998-VAR-AM-APR-fit', '2006-BHF-AM*', \
    '2008-QMC-NM-swave', '2010-QMC-NM-AV4', '2009-DLQMC-NM', '2010-MBPT-NM', \
    '2012-AFDMC-NM-RES-1', '2012-AFDMC-NM-RES-2', '2012-AFDMC-NM-RES-3', '2012-AFDMC-NM-RES-4', \
    '2012-AFDMC-NM-RES-5', '2012-AFDMC-NM-RES-6', '2012-AFDMC-NM-RES-7', \
    '2012-AFDMC-NM-FIT-1', '2012-AFDMC-NM-FIT-2', '2012-AFDMC-NM-FIT-3', '2012-AFDMC-NM-FIT-4', \
    '2012-AFDMC-NM-FIT-5', '2012-AFDMC-NM-FIT-6', '2012-AFDMC-NM-FIT-7', \
    '2013-MBPT-NM', '2014-AFQMC-NM', '2016-QMC-NM', '2016-MBPT-AM', \
    '2018-QMC-NM', '2019-MBPT-AM-L59', '2019-MBPT-AM-L69', \
    '2020-MBPT-AM', '2022-AFDMC-NM', '2024-NLEFT-AM', \
    '2024-BHF-AM-2BF-Av8p', '2024-BHF-AM-2BF-Av18', '2024-BHF-AM-2BF-BONN', '2024-BHF-AM-2BF-CDBONN', \
    '2024-BHF-AM-2BF-NSC97a', '2024-BHF-AM-2BF-NSC97b', '2024-BHF-AM-2BF-NSC97c', '2024-BHF-AM-2BF-NSC97d', \
    '2024-BHF-AM-2BF-NSC97e', '2024-BHF-AM-2BF-NSC97f', '2024-BHF-AM-2BF-SSCV14', \
    '2024-BHF-AM-23BF-Av8p', '2024-BHF-AM-23BF-Av18', '2024-BHF-AM-23BF-BONN', '2024-BHF-AM-23BF-CDBONN', \
    '2024-BHF-AM-23BF-NSC97a', '2024-BHF-AM-23BF-NSC97b', '2024-BHF-AM-23BF-NSC97c', '2024-BHF-AM-23BF-NSC97d', \
    '2024-BHF-AM-23BF-NSC97e', '2024-BHF-AM-23BF-NSC97f', '2024-BHF-AM-23BF-SSCV14', '2024-QMC-NM'

    :param model: Fix the name of model. Default value: '1998-VAR-AM-APR'.
    :type model: str, optional. 

    **Attributes:**
    """

    #
    def __init__(
        self, model="1998-VAR-AM-APR", var1=np.linspace(0.01, 0.4, 20), var2=0.0
    ):
        """
        Parameters
        ----------
        model : str, optional
        The model to consider. Choose between: 1998-VAR-AM-APR (default), 2008-AFDMC-NM, ...
        var1 and var2 : densities (array) and isospin asymmetry (scalar) if necessary (for interpolation function in APRfit for instance)
        var1 = np.array([0.1,0.15,0.16,0.17,0.2,0.25])
        """
        #
        if nuda.env.verb:
            print("Enter setupMicro()")
        #
        #: Attribute model.
        self.model = model
        if nuda.env.verb:
            print("model:", model)
        print("model -> ", model)
        #
        self = setupMicro.init_self(self)
        #
        # read var and define den, asy and xpr:
        self.den = var1[:]  # density n_b=n_n+n_p
        self.asy = var2  # asymmetry parameter = (n_n-n_p)/n_b
        self.kfn = nuda.kf_n((1.0 + self.asy) / 2.0 * self.den)
        self.xpr = (1.0 - self.asy) / 2.0  # proton fraction = n_p/n_b
        # print('den:',self.den)
        # print('asy:',self.asy)
        # print('xpr:',self.xpr)
        #
        models, models_lower = micro_models()
        #
        if model.lower() not in models_lower:
            print(
                "setup_micro: The model name ", model, " is not in the list of models."
            )
            print("setup_micro: list of models:", models)
            print("setup_micro: -- Exit the code --")
            exit()
        #
        # ==============================
        # Read files associated to model
        # ==============================
        #
        self.nm_rmass = nuda.cst.mnc2
        self.sm_rmass = 0.5 * (nuda.cst.mnc2 + nuda.cst.mpc2)
        self.rmass = (1.0 - self.xpr) * nuda.cst.mnc2 + self.xpr * nuda.cst.mpc2
        #
        if model.lower() == "1981-var-am-fp":
            #
            self.flag_nm = True
            self.flag_sm = True
            self.flag_kf = True
            self.flag_den = False
            #
            file_in1 = os.path.join( nuda.param.path_data, "matter/micro/1981-VAR-NM-FP.dat" )
            file_in2 = os.path.join( nuda.param.path_data, "matter/micro/1981-VAR-SM-FP.dat" )
            if nuda.env.verb: print("Reads file:", file_in1)
            if nuda.env.verb: print("Reads file:", file_in2)
            self.ref = "Friedman and Pandharipande, Nucl. Phys. A. 361, 502 (1981)"
            self.note = "write here notes about this EOS."
            self.label = "FP-1981"
            self.marker = "o"
            self.every = 1
            self.e_err = False
            self.p_err = False
            self.cs2_err = False
            self.linestyle = "solid"
            self.nm_den, self.nm_e2a_int = np.loadtxt( file_in1, usecols=(0, 1), unpack=True )
            self.sm_den, self.sm_e2a_int = np.loadtxt( file_in2, usecols=(0, 1), unpack=True )
            self.nm_e2a = self.nm_rmass + self.nm_e2a_int
            self.sm_e2a = self.sm_rmass + self.sm_e2a_int
            self.nm_eps = self.nm_e2a * self.nm_den
            self.sm_eps = self.sm_e2a * self.sm_den
            self.nm_kfn = nuda.kf_n( self.nm_den )
            self.sm_kfn = nuda.kf_n( nuda.cst.half * self.sm_den )
            self.nm_e2a_err = np.abs( uncertainty_stat(self.nm_den, err="MBPT") * self.nm_e2a_int )
            self.sm_e2a_err = np.abs( uncertainty_stat(self.sm_den, err="MBPT") * self.sm_e2a_int )
            self.nm_eps_err = self.nm_e2a_err * self.nm_den
            self.sm_eps_err = self.sm_e2a_err * self.sm_den
            #
        elif model.lower() == "1998-var-am-apr":
            #
            self.flag_nm = True
            self.flag_sm = True
            self.flag_kf = False
            self.flag_den = True
            #
            file_in1 = os.path.join( nuda.param.path_data, "matter/micro/1998-VAR-NM-APR.dat" )
            file_in2 = os.path.join( nuda.param.path_data, "matter/micro/1998-VAR-SM-APR.dat" )
            if nuda.env.verb: print("Reads file:", file_in1)
            if nuda.env.verb: print("Reads file:", file_in2)
            self.ref = ( "Akmal, Pandharipande and Ravenhall, Phys. Rev. C 58, 1804 (1998)" )
            self.note = "write here notes about this EOS."
            self.label = "APR-1998"
            self.marker = "^"
            self.every = 1
            self.e_err = False
            self.p_err = False
            self.cs2_err = False
            self.linestyle = "solid"
            self.nm_den, self.nm_e2a_int = np.loadtxt( file_in1, usecols=(0, 1), unpack=True )
            self.sm_den, self.sm_e2a_int = np.loadtxt( file_in2, usecols=(0, 1), unpack=True )
            self.nm_e2a = self.nm_rmass + self.nm_e2a_int
            self.sm_e2a = self.sm_rmass + self.sm_e2a_int
            self.nm_eps = self.nm_e2a * self.nm_den
            self.sm_eps = self.sm_e2a * self.sm_den
            self.nm_kfn = nuda.kf_n(self.nm_den)
            self.sm_kfn = nuda.kf_n(nuda.cst.half * self.sm_den)
            self.nm_e2a_err = np.abs( uncertainty_stat(self.nm_den, err="MBPT") * self.nm_e2a_int )
            self.sm_e2a_err = np.abs( uncertainty_stat(self.sm_den, err="MBPT") * self.sm_e2a_int )
            self.nm_eps_err = self.nm_e2a_err * self.nm_den
            self.sm_eps_err = self.sm_e2a_err * self.sm_den
            #
        elif model.lower() == "1998-var-am-apr-fit":
            #
            self.flag_nm = True
            self.flag_sm = True
            self.flag_kf = False
            self.flag_den = False
            #
            self.ref = ( "Akmal, Pandharipande and Ravenhall, Phys. Rev. C 58, 1804 (1998)" )
            self.note = "Use interpolation functions suggested in APR paper."
            self.label = "APR-1998-Fit"
            self.marker = "."
            self.every = 1
            self.e_err = False
            self.p_err = False
            self.cs2_err = False
            self.linestyle = "dashed"
            # Define constants for APRfit and for A18+dv+UIX*
            global p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21
            (
                p1,
                p2,
                p3,
                p4,
                p5,
                p6,
                p7,
                p8,
                p9,
                p10,
                p11,
                p12,
                p13,
                p14,
                p15,
                p16,
                p17,
                p18,
                p19,
                p20,
                p21,
            ) = (
                337.2,
                -382.0,
                89.8,
                0.457,
                -59.0,
                -19.1,
                214.6,
                -384.0,
                6.4,
                69.0,
                -33.0,
                0.35,
                0.0,
                0.0,
                287.0,
                -1.54,
                175.0,
                -1.45,
                0.32,
                0.195,
                0.0,
            )
            #
            # energy per unit volume
            self.eps_int = APRfit_compute( self.den, self.xpr )
            # energy per particle
            self.e2a_int = self.eps_int / self.den
            self.e2a = self.rmass + self.e2a_int
            self.eps = self.e2a * self.den
            self.e2a_err = np.abs( uncertainty_stat(self.den, err="MBPT") * self.e2a_int )
            self.eps_err = self.e2a_err * self.den
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
        elif model.lower() == "2006-bhf-am-av18":
            #
            self.flag_nm = True
            self.flag_sm = True
            self.flag_kf = False
            self.flag_den = True
            #
            file_in1 = os.path.join( nuda.param.path_data, "matter/micro/2006-BHF/2006-BHF-Av18-E2A-NM.dat" )
            file_in2 = os.path.join( nuda.param.path_data, "matter/micro/2006-BHF/2006-BHF-Av18-E2A-SM.dat" )
            if nuda.env.verb: print("Reads file:", file_in1)
            if nuda.env.verb: print("Reads file:", file_in2)
            self.ref = "L.G. Cao, U. Lombardo, C.W. Shen, N.V. Giai, Phys. Rev. C 73, 014313 (2006)"
            self.note = ""
            self.label = "BHF-2006-23BF-Av18"
            self.marker = "o"
            self.every = 1
            self.linestyle = "solid"
            self.e_err = False
            self.p_err = False
            self.cs2_err = False
            #
            self.nm_den, self.nm_e2a_int = np.loadtxt( file_in1, usecols=(0, 1), unpack=True )
            self.nm_kfn = nuda.kf_n(self.nm_den)
            self.nm_e2a = self.nm_rmass + self.nm_e2a_int
            self.nm_e2a_err = np.abs( uncertainty_stat(self.nm_den, err="MBPT") * self.nm_e2a_int )
            self.nm_eps = self.nm_e2a * self.nm_den
            self.nm_eps_err = self.nm_e2a_err * self.nm_den
            #
            self.sm_den, self.sm_e2a_int = np.loadtxt( file_in2, usecols=(0, 1), unpack=True )
            self.sm_kfn = nuda.kf_n(nuda.cst.half * self.sm_den)
            self.sm_e2a = self.sm_rmass + self.sm_e2a_int
            self.sm_e2a_err = np.abs( uncertainty_stat(self.sm_den, err="MBPT") * self.sm_e2a_int )
            self.sm_eps = self.sm_e2a * self.sm_den
            self.sm_eps_err = self.sm_e2a_err * self.sm_den
            #
        elif model.lower() == "2008-qmc-nm-swave":
            #
            self.flag_nm = True
            self.flag_sm = False
            self.flag_kf = True
            self.flag_den = False
            #
            file_in = os.path.join(
                nuda.param.path_data, "matter/micro/2008-QMC-NM-swave.dat"
            )
            if nuda.env.verb:
                print("Reads file:", file_in)
            self.ref = "A. Gezerlis and J. Carlson PRC 81, 025803 (2010)"
            self.note = ""
            self.label = "QMC-swave-2008"
            self.marker = "o"
            self.every = 1
            self.linestyle = "solid"
            self.e_err = True
            self.p_err = False
            self.cs2_err = False
            self.nm_kfn, gap2ef, gap2ef_err, e2effg, e2effg_err = np.loadtxt(
                file_in, usecols=(0, 1, 2, 3, 4), unpack=True
            )
            self.nm_den = nuda.den_n(self.nm_kfn)
            self.nm_e2a_int = e2effg * nuda.effg_nr(self.nm_kfn)
            self.nm_e2a = self.nm_rmass + self.nm_e2a_int
            self.nm_e2a_err = e2effg_err * nuda.effg_nr(self.nm_kfn)
            self.nm_eps = self.nm_e2a * self.nm_den
            self.nm_eps_err = self.nm_e2a_err * self.nm_den
            #
        elif model.lower() == "2009-afdmc-nm":
            #
            self.flag_nm = True
            self.flag_sm = False
            self.flag_kf = True
            self.flag_den = False
            #
            file_in = os.path.join(
                nuda.param.path_data, "matter/micro/2009-AFDMC-NM.dat"
            )
            if nuda.env.verb:
                print("Reads file:", file_in)
            self.ref = "S. Gandolfi, A.Y. Illarionov, F. Pederiva, K.E. Schmidt, S. Fantoni, Phys. Rev. C 80, 045802 (2009)."
            self.note = ""
            self.label = "AFDMC-2009"
            self.marker = "o"
            self.every = 1
            self.linestyle = "solid"
            self.e_err = True
            self.p_err = False
            self.cs2_err = False
            self.nm_kfn, self.nm_e2a_int, self.nm_e2a_err = np.loadtxt(
                file_in, usecols=(0, 1, 2), unpack=True
            )
            self.nm_den = nuda.den_n(self.nm_kfn)
            self.nm_e2a = self.nm_rmass + self.nm_e2a_int
            # self.nm_e2a_err = abs( 0.01 * self.nm_e2a )
            self.nm_eps = self.nm_e2a * self.nm_den
            self.nm_eps_err = self.nm_e2a_err * self.nm_den
            #
        elif model.lower() == "2009-dlqmc-nm":
            #
            self.flag_nm = True
            self.flag_sm = False
            self.flag_kf = True
            self.flag_den = False
            #
            file_in = os.path.join(
                nuda.param.path_data, "matter/micro/2009-dQMC-NM.dat"
            )
            if nuda.env.verb:
                print("Reads file:", file_in)
            self.ref = "T. Abe, R. Seki, Phys. Rev. C 79, 054002 (2009)"
            self.note = ""
            self.label = "dLQMC-2009"
            self.marker = "v"
            self.every = 1
            self.linestyle = "solid"
            self.e_err = True
            self.p_err = False
            self.cs2_err = False
            self.nm_kfn, gap2ef, gap2ef_err, e2effg, e2effg_err = np.loadtxt(
                file_in, usecols=(0, 1, 2, 3, 4), unpack=True
            )
            self.nm_den = nuda.den_n(self.nm_kfn)
            self.nm_e2a_int = np.array(e2effg * nuda.effg_nr(self.nm_kfn))
            self.nm_e2a = self.nm_rmass + self.nm_e2a_int
            self.nm_e2a_err = e2effg_err * nuda.effg_nr(self.nm_kfn)
            self.nm_eps = self.nm_e2a * self.nm_den
            self.nm_eps_err = self.nm_e2a_err * self.nm_den
            #
        elif model.lower() == "2010-qmc-nm-av4":
            #
            self.flag_nm = True
            self.flag_sm = False
            self.flag_kf = True
            self.flag_den = False
            #
            file_in = os.path.join(
                nuda.param.path_data, "matter/micro/2010-QMC-NM-AV4.dat"
            )
            if nuda.env.verb:
                print("Reads file:", file_in)
            self.ref = "A. Gezerlis and J. Carlson PRC 81, 025803 (2010)"
            self.note = ""
            self.label = "QMC-AV4-2008"
            self.marker = "s"
            self.every = 1
            self.e_err = True
            self.p_err = False
            self.cs2_err = False
            self.linestyle = "solid"
            self.nm_kfn, gap2ef, gap2ef_err, e2effg, e2effg_err = np.loadtxt(
                file_in, usecols=(0, 1, 2, 3, 4), unpack=True
            )
            self.nm_den = nuda.den_n(self.nm_kfn)
            self.nm_e2a_int = np.array(e2effg * nuda.effg_nr(self.nm_kfn))
            self.nm_e2a = self.nm_rmass + self.nm_e2a_int
            self.nm_e2a_err = e2effg_err * nuda.effg_nr(self.nm_kfn)
            self.nm_eps = self.nm_e2a * self.nm_den
            self.nm_eps_err = self.nm_e2a_err * self.nm_den
            #
        elif model.lower() == "2010-mbpt-nm":
            #
            self.flag_nm = True
            self.flag_sm = False
            self.flag_kf = False
            self.flag_den = False
            #
            file_in = os.path.join(
                nuda.param.path_data, "matter/micro/2010-NM-Hebeler.dat"
            )
            if nuda.env.verb:
                print("Reads file:", file_in)
            self.ref = "K. Hebeler, et al, Phys. Rev. Lett. 105, 161102 (2010)"
            self.note = "chiral NN forces with SRG and leading 3N forces."
            self.label = "MBPT-2010"
            self.marker = "s"
            self.every = 1
            self.e_err = False
            self.p_err = False
            self.cs2_err = False
            self.linestyle = "solid"
            self.nm_den, self.nm_pre = np.loadtxt(file_in, usecols=(0, 1), unpack=True)
            self.nm_kfn = nuda.kf_n(self.nm_den)
            # self.nm_pre_err = np.abs( 0.01 * self.nm_pre )
            #
            # chemical potential
            # self.nm_chempot = ( self.nm_pre + self.nm_eps ) / self.nm_den
            #
        elif "2012-afdmc-nm-res" in model.lower():
            #
            self.flag_nm = True
            self.flag_sm = False
            self.flag_kf = False
            self.flag_den = True
            #
            # We do not have the data for this model, but we have a fit of the data
            k = int(model.split(sep="-")[4])
            # print('k:',k)
            file_in = os.path.join(
                nuda.param.path_data, "matter/micro/2012-AFDMC-NM-" + str(k) + ".dat"
            )
            if nuda.env.verb:
                print("Reads file:", file_in)
            self.ref = (
                "S. Gandolfi, J. Carlson, S. Reddy, Phys. Rev. C 85, 032801(R) (2012)."
            )
            self.note = (
                "We have the data for this model, which are used for the fit in the next section."
            )
            self.label = "AFDMC-2012-" + str(k)
            self.marker = "s"
            self.every = 3
            if k == 1:
                self.every = 4
            if k == 7:
                self.every = 4
            self.e_err = True
            self.p_err = False
            self.cs2_err = False
            self.linestyle = "solid"
            # self.linestyle = 'None'
            if k in [1, 7]:
                self.nm_den, ETOT, ETOT_ERR = np.loadtxt(
                    file_in, usecols=(0, 1, 2), unpack=True
                )
            elif k in [2, 3, 4, 5, 6]:
                V0, MU, self.nm_den, ETOT, ETOT_ERR = np.loadtxt(
                    file_in, usecols=(0, 1, 2, 3, 4), unpack=True
                )
            else:
                print("The value of k is no correct ", k)
                exit()
            self.nm_kfn = nuda.kf_n(self.nm_den)
            self.nm_e2a_int = ETOT  # / 66.0
            self.nm_e2a = self.nm_rmass + self.nm_e2a_int
            self.nm_e2a_err = ETOT_ERR  # / 66.0
            self.nm_eps = self.nm_den * self.nm_e2a
            self.nm_eps_err = self.nm_den * self.nm_e2a_err
            # self.nm_pre =
            # self.nm_chempot =
            # self.nm_cs2 =
            #
        elif "2012-afdmc-nm-fit" in model.lower():
            #
            self.flag_nm = True
            self.flag_sm = False
            self.flag_kf = False
            self.flag_den = False
            #
            # We do not have the data for this model, but we have a fit of the data
            k = int(model.split(sep="-")[4])
            # print('k:',k)
            file_in = os.path.join(
                nuda.param.path_data, "matter/micro/2012-AFDMC-NM-fit.dat"
            )
            if nuda.env.verb:
                print("Reads file:", file_in)
            self.ref = (
                "S. Gandolfi, J. Carlson, S. Reddy, Phys. Rev. C 85, 032801(R) (2012)."
            )
            self.note = (
                "This is the fit using the data from the previous section."
            )
            self.label = "AFDMC-2012-" + str(k) + "-FIT"
            self.marker = "s"
            self.every = 1
            self.e_err = True
            self.p_err = False
            self.cs2_err = False
            self.linestyle = "dashed"
            ind, a, alfa, b, beta = np.loadtxt(
                file_in, usecols=(0, 1, 2, 3, 4), unpack=True
            )
            # name = np.loadtxt( file_in, usecols=(5), unpack = True )
            nmodel = np.size(alfa)
            # print('nmodel:',nmodel)
            if k < 0 or k > nmodel:
                print("issue with the model number k:", k)
                print("exit")
                exit()
            # for i in range(nmodel):
            #    print('i:',i,' ind:',ind[i],' a:',a[i],' alfa:',alfa[i],' b:',b[i],' beta:',beta[i])
            self.nm_den_fit = 0.04 + 0.45 * np.arange(self.nden + 1) / float(self.nden)
            self.nm_kfn_fit = nuda.kf_n(self.nm_den_fit)
            # energy in NM
            self.nm_e2a_int_fit = func_GCR_e2a(
                self.nm_den_fit, a[k - 1], alfa[k - 1], b[k - 1], beta[k - 1]
            )
            self.nm_e2a_fit = self.nm_rmass + self.nm_e2a_int_fit
            self.nm_e2a_fit_err = np.abs(
                uncertainty_stat(self.nm_den_fit, err="MBPT") * self.nm_e2a_fit
            )
            self.nm_eps_fit = self.nm_den_fit * self.nm_e2a_fit
            self.nm_eps_fit_err = self.nm_den_fit * self.nm_e2a_fit_err
            # pressure in NM
            self.nm_pre_fit = func_GCR_pre(
                self.nm_den_fit, a[k - 1], alfa[k - 1], b[k - 1], beta[k - 1]
            )
            # chemical potential
            #self.nm_chempot_fit = (self.nm_pre_fit + self.nm_eps_fit) / self.nm_den_fit
            # enthalpy per particle
            self.nm_h2a_fit = self.nm_e2a_fit + self.nm_pre_fit / self.nm_den_fit
            # sound speed in NM
            self.nm_cs2_fit = func_GCR_cs2(
                self.nm_den_fit, a[k - 1], alfa[k - 1], b[k - 1], beta[k - 1]
            )
            #
            self.nm_den = self.nm_den_fit
            self.nm_kfn = self.nm_kfn_fit
            self.nm_e2a_int = self.nm_e2a_fit
            self.nm_e2a = self.nm_rmass + self.nm_e2a_int
            self.nm_e2a_err = self.nm_e2a_fit_err
            self.nm_eps = self.nm_eps_fit
            self.nm_eps_err = self.nm_eps_fit_err
            self.nm_pre = self.nm_pre_fit
            #self.nm_chempot = self.nm_chempot_fit
            self.nm_cs2 = self.nm_cs2_fit
            #
        elif model.lower() == "2013-mbpt-nm":
            #
            self.flag_nm = True
            self.flag_sm = False
            self.flag_kf = False
            self.flag_den = True
            #
            file_in = os.path.join(nuda.param.path_data, "matter/micro/2013-MBPT-NM.dat")
            if nuda.env.verb:
                print("Reads file:", file_in)
            self.ref = "I. Tews et al., PRL 110, 032504 (2013)"
            self.note = "write here notes about this EOS."
            self.label = "MBPT-2013"
            self.marker = "s"
            self.every = 1
            self.linestyle = "solid"
            self.e_err = True
            self.p_err = False
            self.cs2_err = False
            (
                self.nm_den,
                self.nm_e2a_int_low,
                self.nm_e2a_int_up,
                self.nm_pre_low,
                self.nm_pre_up,
            ) = np.loadtxt(file_in, usecols=(0, 1, 2, 3, 4), unpack=True)
            self.nm_kfn = nuda.kf_n(self.nm_den)
            self.nm_e2a_int = np.array(0.5 * (self.nm_e2a_int_up + self.nm_e2a_int_low))
            self.nm_e2a = self.nm_rmass + self.nm_e2a_int
            self.nm_e2a_err = 0.5 * (self.nm_e2a_int_up - self.nm_e2a_int_low)
            self.nm_eps = self.nm_e2a * self.nm_den
            self.nm_eps_err = self.nm_e2a_err * self.nm_den
            self.nm_pre = 0.5 * (self.nm_pre_up + self.nm_pre_low)
            self.nm_pre_err = 0.5 * (self.nm_pre_up - self.nm_pre_low)
            #
            # chemical potential
            #self.nm_chempot = (
            #    np.array(self.nm_pre) + np.array(self.nm_eps)
            #) / np.array(self.nm_den)
            #self.nm_chempot_err = (
            #    np.array(self.nm_pre_err) + np.array(self.nm_eps_err)
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
        elif model.lower() == "2014-afqmc-nm":
            #
            self.flag_nm = True
            self.flag_sm = False
            self.flag_kf = True
            self.flag_den = False
            #
            file_in = os.path.join(
                nuda.param.path_data, "matter/micro/2014-AFQMC-NM.dat"
            )
            if nuda.env.verb:
                print("Reads file:", file_in)
            self.ref = "G. Wlazłowski, J.W. Holt, S. Moroz, A. Bulgac, and K.J. Roche Phys. Rev. Lett. 113, 182503 (2014)"
            self.note = "write here notes about this EOS."
            self.label = "AFQMC-2014"
            self.marker = "s"
            self.every = 1
            self.e_err = False
            self.p_err = False
            self.cs2_err = False
            self.linestyle = "solid"
            self.nm_den, self.nm_e2a_int_2bf, self.nm_e2a_int_23bf = np.loadtxt(
                file_in, usecols=(0, 1, 2), unpack=True
            )
            self.nm_kfn = nuda.kf_n(self.nm_den)
            self.nm_e2a_int = self.nm_e2a_int_23bf
            self.nm_e2a = self.nm_rmass + self.nm_e2a_int
            self.nm_e2a_err = np.abs(
                uncertainty_stat(self.nm_den, err="MBPT") * self.nm_e2a_int
            )
            # self.nm_e2a_err = np.abs( 0.01 * self.nm_e2a )
            self.nm_eps = self.nm_e2a * self.nm_den
            self.nm_eps_err = self.nm_e2a_err * self.nm_den
            #
        elif model.lower() == "2016-qmc-nm":
            #
            self.flag_nm = True
            self.flag_sm = False
            self.flag_kf = True
            self.flag_den = False
            #
            file_in = os.path.join(nuda.param.path_data, "matter/micro/2016-QMC-NM.dat")
            if nuda.env.verb:
                print("Reads file:", file_in)
            self.ref = " I. Tews, S. Gandolfi, A. Gezerlis, A. Schwenk, Phys. Rev. C 93, 024305 (2016)."
            self.note = ""
            self.label = "QMC-2016"
            self.marker = "s"
            self.linestyle = "solid"
            self.e_err = True
            self.p_err = False
            self.cs2_err = False
            self.every = 1
            self.nm_den, self.nm_e2a_int_low, self.nm_e2a_int_up = np.loadtxt(
                file_in, usecols=(0, 1, 2), unpack=True
            )
            self.nm_kfn = nuda.kf_n(self.nm_den)
            self.nm_e2a_int = np.array(0.5 * (self.nm_e2a_int_up + self.nm_e2a_int_low))
            self.nm_e2a = self.nm_rmass + self.nm_e2a_int
            self.nm_e2a_err = 0.5 * (self.nm_e2a_int_up - self.nm_e2a_int_low)
            self.nm_eps = self.nm_e2a * self.nm_den
            self.nm_eps_err = self.nm_e2a_err * self.nm_den
            #
        elif model.lower() == "2016-mbpt-am":
            #
            self.flag_nm = True
            self.flag_sm = True
            self.flag_kf = False
            self.flag_den = True
            #
            self.ref = (
                "C. Drischler, K. Hebeler, A. Schwenk, Phys. Rev. C 93, 054314 (2016)."
            )
            self.note = ""
            self.label = "MBPT-2016"
            self.marker = "s"
            self.linestyle = "solid"
            self.e_err = True
            self.p_err = False
            self.cs2_err = False
            self.every = 4
            # read the results for the 7 hamiltonians
            length = np.zeros((11), dtype=int)
            den = np.zeros((11, 35))
            e2a = np.zeros((10, 11, 35))
            e2a_up = np.zeros((11, 35))
            e2a_low = np.zeros((11, 35))
            e2a_av = np.zeros((11, 35))
            e2a_err = np.zeros((11, 35))
            for i in range(0, 11):
                beta = i / 10.0
                if i < 10:
                    file_in = os.path.join(
                        nuda.param.path_data,
                        "matter/micro/2016-MBPT-AM/EOS_spec_4_beta_0."
                        + str(i)
                        + ".txt",
                    )
                if i == 10:
                    file_in = os.path.join(
                        nuda.param.path_data,
                        "matter/micro/2016-MBPT-AM/EOS_spec_4_beta_1.0.txt",
                    )
                if nuda.env.verb:
                    print("Reads file:", file_in)
                deni, e2a_1, e2a_2, e2a_3, e2a_4, e2a_5, e2a_6, e2a_7 = np.genfromtxt(
                    file_in, usecols=(0, 1, 2, 3, 4, 5, 6, 7), comments="#", unpack=True
                )
                length[i] = len(deni)
                den[i, 0 : length[i]] = deni
                den_n = deni * (1.0 + beta) / 2.0
                e2a[1, i, 0 : length[i]] = e2a_1
                e2a[2, i, 0 : length[i]] = e2a_2
                e2a[3, i, 0 : length[i]] = e2a_3
                e2a[4, i, 0 : length[i]] = e2a_4
                e2a[5, i, 0 : length[i]] = e2a_5
                e2a[6, i, 0 : length[i]] = e2a_6
                e2a[7, i, 0 : length[i]] = e2a_7
                # performs average and compute boundaries
                e2a_up[i, 0 : length[i]] = e2a_1
                e2a_low[i, 0 : length[i]] = e2a_1
                for j in range(length[i]):
                    for k in range(2, 8):
                        if e2a[k, i, j] > e2a_up[i, j]:
                            e2a_up[i, j] = e2a[k, i, j]
                        if e2a[k, i, j] < e2a_low[i, j]:
                            e2a_low[i, j] = e2a[k, i, j]
                    e2a_av[i, j] = 0.5 * (e2a_up[i, j] + e2a_low[i, j])
                    e2a_err[i, j] = 0.5 * (e2a_up[i, j] - e2a_low[i, j])
            if nuda.env.verb:
                print("length:", length[:])
            # NM
            self.nm_den = np.array(den[10, :])
            self.nm_kfn = nuda.kf_n(self.nm_den)
            self.nm_e2a_int_up = e2a_up[10, :]
            self.nm_e2a_int_low = e2a_low[10, :]
            self.nm_e2a_int = np.array(e2a_av[10, :])
            self.nm_e2a = self.nm_rmass + self.nm_e2a_int
            self.nm_e2a_err = e2a_err[10, :]
            self.nm_eps = self.nm_e2a * self.nm_den
            self.nm_eps_err = self.nm_e2a_err * self.nm_den
            # SM
            self.sm_den = np.array(den[0, :])
            self.sm_kfn = nuda.kf_n(nuda.cst.half * self.sm_den)
            self.sm_e2a_int_up = e2a_up[0, :]
            self.sm_e2a_int_low = e2a_low[0, :]
            self.sm_e2a_int = np.array(e2a_av[0, :])
            self.sm_e2a = self.sm_rmass + self.sm_e2a_int
            self.sm_e2a_err = e2a_err[0, :]
            self.sm_eps = self.sm_e2a * self.sm_den
            self.sm_eps_err = self.sm_e2a_err * self.sm_den
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
            self.am_e2a_int_err = np.zeros((11,35))
            self.am_eps_int_av = np.zeros((11,35))
            self.am_eps_int_err = np.zeros((11,35))
            self.am_e2a_av = np.zeros((11,35))
            self.am_e2a_err = np.zeros((11,35))
            self.am_eps_av = np.zeros((11,35))
            self.am_eps_err = np.zeros((11,35))
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
                self.am_e2a_int_av[i]  = np.array(e2a_av[i, :])
                self.am_e2a_int_err[i] = np.array(e2a_err[i, :])
                self.am_eps_int_av[i]  = self.am_e2a_int_av[i]  * self.am_den[i] 
                self.am_eps_int_err[i] = self.am_e2a_int_err[i] * self.am_den[i]
                self.am_e2a_av[i]  = self.am_rmass[i] + self.am_e2a_int_av[i]
                self.am_e2a_err[i] = self.am_rmass[i] + self.am_e2a_int_err[i]
                self.am_eps_av[i]  = self.am_e2a_av[i]  * self.am_den[i] 
                self.am_eps_err[i] = self.am_e2a_err[i] * self.am_den[i]
            #
            # Note: here I define the pressure as the derivative of the centroid energy
            # It would however be better to compute the presure for each models and only
            # after that, estimate the centroid and uncertainty.
            #
        elif model.lower() == "2018-qmc-nm":
            #
            self.flag_nm = True
            self.flag_sm = False
            self.flag_kf = True
            self.flag_den = False
            #
            file_in = os.path.join(nuda.param.path_data, "matter/micro/2018-QMC-NM.dat")
            if nuda.env.verb:
                print("Reads file:", file_in)
            self.ref = "I. Tews, J. Carlson, S. Gandolfi, S. Reddy, Astroph. J. 860(2), 149 (2018)."
            self.note = ""
            self.label = "QMC-2018"
            self.marker = "s"
            self.every = 2
            self.linestyle = "solid"
            self.e_err = True
            self.p_err = False
            self.cs2_err = False
            (
                self.nm_den,
                self.nm_e2a_int_low,
                self.nm_e2a_int_up,
                self.nm_e2a_int,
                self.nm_e2a_err,
            ) = np.loadtxt(file_in, usecols=(0, 1, 2, 3, 4), unpack=True)
            self.nm_e2a = self.nm_rmass + self.nm_e2a_int
            self.nm_kfn = nuda.kf_n(self.nm_den)
            self.nm_eps = self.nm_e2a * self.nm_den
            self.nm_eps_err = self.nm_e2a_err * self.nm_den
            #
        elif model.lower() == "2019-mbpt-am-l59":
            #
            self.flag_nm = True
            self.flag_sm = True
            self.flag_kf = False
            self.flag_den = True
            #
            # here, the L59 case is compute alone, it would be interesting to compute the uncertainty
            # in the previous MBPT calculation (based on H1-H7) adding this new calculation.
            #
            file_in1 = os.path.join(
                nuda.param.path_data, "matter/micro/2019-MBPT-SM-DHSL59.dat"
            )
            file_in2 = os.path.join(
                nuda.param.path_data, "matter/micro/2019-MBPT-NM-DHSL59.dat"
            )
            if nuda.env.verb:
                print("Reads file1:", file_in1)
            if nuda.env.verb:
                print("Reads file2:", file_in2)
            self.ref = "C. Drischler, K. Hebeler, A. Schwenk, Phys. Rev. Lett. 122, 042501 (2019)"
            self.note = ""
            self.label = "MBPT-2019-L59"
            self.marker = "s"
            self.every = 2
            self.e_err = False
            self.p_err = False
            self.cs2_err = False
            self.linestyle = "solid"
            (
                self.sm_kfn,
                self.sm_den,
                Kin,
                HF_tot,
                Scnd_tot,
                Trd_tot,
                Fth_tot,
                self.sm_e2a_int,
            ) = np.loadtxt(
                file_in1, usecols=(0, 1, 2, 3, 4, 5, 6, 7), comments="#", unpack=True
            )
            self.sm_e2a = self.sm_rmass + self.sm_e2a_int
            self.sm_e2a_err = np.abs(
                uncertainty_stat(self.sm_den, err="MBPT") * self.sm_e2a_int
            )
            self.sm_eps = self.sm_e2a * self.sm_den
            self.sm_eps_err = self.sm_e2a_err * self.sm_den
            (
                self.nm_kfn,
                self.nm_den,
                Kin,
                HF_tot,
                Scnd_tot,
                Trd_tot,
                Fth_tot,
                self.nm_e2a_int,
            ) = np.loadtxt(
                file_in2, usecols=(0, 1, 2, 3, 4, 5, 6, 7), comments="#", unpack=True
            )
            self.nm_e2a = self.nm_rmass + self.nm_e2a_int
            self.nm_e2a_err = np.abs(
                uncertainty_stat(self.nm_den, err="MBPT") * self.nm_e2a_int
            )
            self.nm_eps = self.nm_e2a * self.nm_den
            self.nm_eps_err = self.nm_e2a_err * self.nm_den
            #
        elif model.lower() == "2019-mbpt-am-l69":
            #
            self.flag_nm = True
            self.flag_sm = True
            self.flag_kf = False
            self.flag_den = True
            #
            # same remarck as for L59
            #
            file_in1 = os.path.join(
                nuda.param.path_data, "matter/micro/2019-MBPT-SM-DHSL69.dat"
            )
            file_in2 = os.path.join(
                nuda.param.path_data, "matter/micro/2019-MBPT-NM-DHSL69.dat"
            )
            if nuda.env.verb:
                print("Reads file1:", file_in1)
            if nuda.env.verb:
                print("Reads file2:", file_in2)
            self.ref = "C. Drischler, K. Hebeler, A. Schwenk, Phys. Rev. Lett. 122, 042501 (2019)"
            self.note = ""
            self.label = "MBPT-2019-L69"
            self.marker = "s"
            self.every = 2
            self.e_err = False
            self.p_err = False
            self.cs2_err = False
            self.linestyle = "solid"
            (
                self.sm_kfn,
                self.sm_den,
                Kin,
                HF_tot,
                Scnd_tot,
                Trd_tot,
                Fth_tot,
                self.sm_e2a_int,
            ) = np.loadtxt(
                file_in1, usecols=(0, 1, 2, 3, 4, 5, 6, 7), comments="#", unpack=True
            )
            self.sm_e2a = self.sm_rmass + self.sm_e2a_int
            self.sm_e2a_err = np.abs(
                uncertainty_stat(self.sm_den, err="MBPT") * self.sm_e2a_int
            )
            self.sm_eps = self.sm_e2a * self.sm_den
            self.sm_eps_err = self.sm_e2a_err * self.sm_den
            (
                self.nm_kfn,
                self.nm_den,
                Kin,
                HF_tot,
                Scnd_tot,
                Trd_tot,
                Fth_tot,
                self.nm_e2a_int,
            ) = np.loadtxt(
                file_in2, usecols=(0, 1, 2, 3, 4, 5, 6, 7), comments="#", unpack=True
            )
            self.nm_e2a = self.nm_rmass + self.nm_e2a_int
            self.nm_e2a_err = np.abs(
                uncertainty_stat(self.nm_den, err="MBPT") * self.nm_e2a_int
            )
            self.nm_eps = self.nm_e2a * self.nm_den
            self.nm_eps_err = self.nm_e2a_err * self.nm_den
            #
        elif model.lower() == "2020-mbpt-am":
            #
            self.flag_nm = True
            self.flag_sm = True
            self.flag_kf = False
            self.flag_den = True
            #
            file_in1 = os.path.join(
                nuda.param.path_data, "matter/micro/2020-MBPT-SM.csv"
            )
            file_in2 = os.path.join(
                nuda.param.path_data, "matter/micro/2020-MBPT-NM.csv"
            )
            if nuda.env.verb:
                print("Reads file1:", file_in1)
            if nuda.env.verb:
                print("Reads file2:", file_in2)
            self.ref = "C. Drischler, R.J. Furnstahl, J.A. Melendez, D.R. Phillips, Phys. Rev. Lett. 125(20), 202702 (2020).; C. Drischler, J. A. Melendez, R. J. Furnstahl, and D. R. Phillips, Phys. Rev. C 102, 054315"
            self.note = ""
            self.label = "MBPT-2020"
            self.marker = "o"
            self.linestyle = "solid"
            self.every = 6
            self.e_err = True
            self.p_err = False
            self.cs2_err = False
            (
                self.sm_den,
                self.sm_e2a_lo,
                self.sm_e2a_lo_err,
                self.sm_e2a_nlo,
                self.sm_e2a_nlo_err,
                self.sm_e2a_n2lo,
                self.sm_e2a_n2lo_err,
                self.sm_e2a_n3lo,
                self.sm_e2a_n3lo_err,
            ) = np.loadtxt(
                file_in1,
                usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8),
                delimiter=",",
                comments="#",
                unpack=True,
            )
            self.sm_kfn = nuda.kf_n(nuda.cst.half * self.sm_den)
            self.sm_e2a_int = self.sm_e2a_n3lo
            self.sm_e2a = self.sm_rmass + self.sm_e2a_int
            self.sm_e2a_err = self.sm_e2a_n3lo_err
            self.sm_eps = self.sm_e2a * self.sm_den
            self.sm_eps_err = self.sm_e2a_err * self.sm_den
            (
                self.nm_den,
                self.nm_e2a_lo,
                self.nm_e2a_lo_err,
                self.nm_e2a_nlo,
                self.nm_e2a_nlo_err,
                self.nm_e2a_n2lo,
                self.nm_e2a_n2lo_err,
                self.nm_e2a_n3lo,
                self.nm_e2a_n3lo_err,
            ) = np.loadtxt(
                file_in2,
                usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8),
                delimiter=",",
                comments="#",
                unpack=True,
            )
            self.nm_kfn = nuda.kf_n(self.nm_den)
            self.nm_e2a_int = self.nm_e2a_n3lo
            self.nm_e2a = self.nm_rmass + self.nm_e2a_int
            self.nm_e2a_err = self.nm_e2a_n3lo_err
            self.nm_eps = self.nm_e2a * self.nm_den
            self.nm_eps_err = self.nm_e2a_err * self.nm_den
            #
        elif model.lower() == "2022-afdmc-nm":
            #
            self.flag_nm = True
            self.flag_sm = False
            self.flag_kf = False
            self.flag_den = True
            #
            file_in = os.path.join(
                nuda.param.path_data, "matter/micro/2022-AFDMC-NM.csv"
            )
            if nuda.env.verb:
                print("Reads file:", file_in)
            self.ref = "S. Gandolfi, G. Palkanoglou, J. Carlson, A. Gezerlis, K.E. Schmidt, Condensed Matter 7(1) (2022)."
            self.note = ""
            self.label = "AFDMC+corr.-2022"
            self.linestyle = "solid"
            self.marker = "o"
            self.linestyle = "solid"
            self.every = 1
            self.e_err = True
            self.p_err = False
            self.cs2_err = False
            # read e2a
            self.nm_kfn, e2effg, e2effg_err = np.loadtxt(
                file_in, usecols=(0, 1, 2), delimiter=",", comments="#", unpack=True
            )
            self.nm_den = nuda.den_n(self.nm_kfn)
            self.nm_e2a_int = e2effg * nuda.effg_nr(self.nm_kfn)
            self.nm_e2a = self.nm_rmass + self.nm_e2a_int
            self.nm_e2a_err = e2effg_err * nuda.effg_nr(self.nm_kfn)
            #
            self.nm_eps = self.nm_e2a * self.nm_den
            self.nm_eps_err = self.nm_e2a_err * self.nm_den
            #
        elif model.lower() == "2024-nleft-am":
            #
            # print('enter here:',model)
            self.flag_nm = True
            self.flag_sm = True
            self.flag_kf = False
            self.flag_den = False
            #
            file_in1 = os.path.join(
                nuda.param.path_data, "matter/micro/2024-NLEFT-SM.dat"
            )
            file_in2 = os.path.join(
                nuda.param.path_data, "matter/micro/2024-NLEFT-NM.dat"
            )
            if nuda.env.verb:
                print("Reads file1:", file_in1)
            if nuda.env.verb:
                print("Reads file2:", file_in2)
            self.ref = (
                "S. Elhatisari, L. Bovermann, Y.-Z. Ma et al., Nature 630, 59 (2024)."
            )
            self.note = ""
            self.label = "NLEFT-2024"
            self.marker = "s"
            self.linestyle = "solid"
            self.every = 2
            self.e_err = True
            self.p_err = False
            self.cs2_err = False
            #
            # Read SM results
            #
            (
                self.sm_A,
                self.sm_L,
                self.sm_den,
                self.sm_etot_int_2bf,
                self.sm_etot_2bf_err,
                self.sm_etot_int,
                self.sm_etot_err,
            ) = np.loadtxt(
                file_in1,
                usecols=(0, 1, 2, 3, 4, 5, 6),
                comments="#",
                unpack=True,
                delimiter=",",
            )
            self.sm_kfn = nuda.kf_n(nuda.cst.half * self.sm_den)
            self.sm_e2a_int_data = self.sm_etot_int / self.sm_A
            self.sm_e2a_err_data = self.sm_etot_err / self.sm_A
            self.sm_e2a_int_2bf_data = self.sm_etot_int_2bf / self.sm_A
            self.sm_e2a_2bf_err_data = self.sm_etot_2bf_err / self.sm_A
            self.sm_e2a_data = self.sm_rmass + self.sm_e2a_int_data
            self.sm_eps_data = self.sm_e2a_data * self.sm_den
            self.sm_eps_err_data = self.sm_e2a_err_data * self.sm_den
            # fit with EFFG
            xdata = self.sm_kfn
            ydata = self.sm_e2a_int_data
            sm_popt, sm_pcov = curve_fit(func_e2a_NLEFT2024, xdata, ydata)
            print("sm_popt:", sm_popt)
            print("sm_pcov:", sm_pcov)
            self.sm_pfit = sm_popt
            self.sm_perr = np.sqrt(np.diag(sm_pcov))
            # analyse the uncertainties for e2a, pre, cs2
            self.sm_pcerr = np.zeros((100, 3), dtype=float)
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
                b = self.sm_pfit[0] + 0.1 * (random.random() - 0.5) * self.sm_perr[0]
                c = self.sm_pfit[1] + 0.1 * (random.random() - 0.5) * self.sm_perr[1]
                d = self.sm_pfit[2] + 0.1 * (random.random() - 0.5) * self.sm_perr[2]
                self.sm_pcerr[k, 0] = b
                self.sm_pcerr[k, 1] = c
                self.sm_pcerr[k, 2] = d
                param = np.array([b, c, d])
                # e2a
                af = func_e2a_NLEFT2024(xdata, *param)
                for l, val in enumerate(af):
                    if val > self.sm_e2a_int_max[l]:
                        self.sm_e2a_int_max[l] = val
                    if val < self.sm_e2a_int_min[l]:
                        self.sm_e2a_int_min[l] = val
                self.sm_e2a_err = 0.5 * (self.sm_e2a_int_max - self.sm_e2a_int_min)
                # pre
                af = func_pre_NLEFT2024(xdata, self.sm_den, *param)
                for l, val in enumerate(af):
                    if val > self.sm_pre_max[l]:
                        self.sm_pre_max[l] = val
                    if val < self.sm_pre_min[l]:
                        self.sm_pre_min[l] = val
                self.sm_pre_err = 0.5 * (self.sm_pre_max - self.sm_pre_min)
                # dpdn
                af = func_dpredn_NLEFT2024(xdata, self.sm_den, *param)
                for l, val in enumerate(af):
                    if val > self.sm_dpredn_max[l]:
                        self.sm_dpredn_max[l] = val
                    if val < self.sm_dpredn_min[l]:
                        self.sm_dpredn_min[l] = val
                self.sm_dpredn_err = 0.5 * (self.sm_dpredn_max - self.sm_dpredn_min)
            # print('sm_pcerr:',self.sm_pcerr)
            # self.sm_e2a = self.sm_e2a_fit
            # self.sm_e2a_err = self.sm_e2a_fit_err
            self.sm_eps = self.sm_e2a * self.sm_den
            self.sm_eps_err = self.sm_e2a_err * self.sm_den
            #
            # Read NM results
            self.nm_A, self.nm_L, self.nm_den, self.nm_etot_int, self.nm_etot_err = (
                np.loadtxt(
                    file_in2,
                    usecols=(0, 1, 2, 3, 4),
                    comments="#",
                    unpack=True,
                    delimiter=",",
                )
            )
            self.nm_kfn = nuda.kf_n(self.nm_den)
            self.nm_e2a_int_data = self.nm_etot_int / self.nm_A
            self.nm_e2a_err_data = self.nm_etot_err / self.nm_A
            self.nm_e2a_data = self.nm_rmass + self.nm_e2a_int_data
            self.nm_eps_data = self.nm_e2a_data * self.nm_den
            self.nm_eps_err_data = self.nm_e2a_err_data * self.nm_den
            # fit with EFFG
            xdata = self.nm_kfn
            ydata = self.nm_e2a_int_data
            nm_popt, nm_pcov = curve_fit(func_e2a_NLEFT2024, xdata, ydata)
            print("nm_popt:", nm_popt)
            print("nm_pcov:", nm_pcov)
            self.nm_pfit = nm_popt
            self.nm_perr = np.sqrt(np.diag(nm_pcov))
            self.nm_pcerr = np.zeros((100, 3), dtype=float)
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
                b = self.nm_pfit[0] + 0.2 * (random.random() - 0.5) * self.nm_perr[0]
                c = self.nm_pfit[1] + 0.2 * (random.random() - 0.5) * self.nm_perr[1]
                d = self.nm_pfit[2] + 0.2 * (random.random() - 0.5) * self.nm_perr[2]
                self.nm_pcerr[k, 0] = b
                self.nm_pcerr[k, 1] = c
                self.nm_pcerr[k, 2] = d
                param = np.array([b, c, d])
                # e2a
                af = func_e2a_NLEFT2024(xdata, *param)
                for l, val in enumerate(af):
                    if val > self.nm_e2a_int_max[l]:
                        self.nm_e2a_int_max[l] = val
                    if val < self.nm_e2a_int_min[l]:
                        self.nm_e2a_int_min[l] = val
                self.nm_e2a_err = 0.5 * (self.nm_e2a_int_max - self.nm_e2a_int_min)
                # pre
                af = func_pre_NLEFT2024(xdata, self.nm_den, *param)
                for l, val in enumerate(af):
                    if val > self.nm_pre_max[l]:
                        self.nm_pre_max[l] = val
                    if val < self.nm_pre_min[l]:
                        self.nm_pre_min[l] = val
                self.nm_pre_err = 0.5 * (self.nm_pre_max - self.nm_pre_min)
                # dpdn
                af = func_dpredn_NLEFT2024(xdata, self.nm_den, *param)
                for l, val in enumerate(af):
                    if val > self.nm_dpredn_max[l]:
                        self.nm_dpredn_max[l] = val
                    if val < self.nm_dpredn_min[l]:
                        self.nm_dpredn_min[l] = val
                self.nm_dpredn_err = 0.5 * (self.nm_dpredn_max - self.nm_dpredn_min)
            # print('nm_pcerr:',self.nm_pcerr)
            # self.nm_e2a = self.nm_e2a_fit
            # self.nm_e2a_err = self.nm_e2a_fit_err
            self.nm_eps = self.nm_e2a * self.nm_den
            self.nm_eps_err = self.nm_e2a_err * self.nm_den
            self.nm_pre = self.nm_pre
            self.nm_pre_err = self.nm_pre_err
            self.nm_dpredn = self.nm_dpredn
            self.nm_dpredn_err = self.nm_dpredn_err
            #
            # chemical potential
            #self.nm_chempot = (
            #    np.array(self.nm_pre) + np.array(self.nm_eps)
            #) / np.array(self.nm_den)
            #self.nm_chempot_err = (
            #    np.array(self.nm_pre_err) + np.array(self.nm_eps_err)
            #) / np.array(self.nm_den)
            #self.sm_chempot = (
            #    np.array(self.sm_pre) + np.array(self.sm_eps)
            #) / np.array(self.sm_den)
            #self.sm_chempot_err = (
            #    np.array(self.sm_pre_err) + np.array(self.sm_eps_err)
            #) / np.array(self.sm_den)
            #
            # enthalpy
            self.sm_h2a = self.sm_e2a + self.sm_pre / self.sm_den
            self.sm_h2a_err = self.sm_e2a_err + self.sm_pre_err / self.sm_den
            self.nm_h2a = self.nm_e2a + self.nm_pre / self.nm_den
            self.nm_h2a_err = self.nm_e2a_err + self.nm_pre_err / self.nm_den
            #
            # sound speed
            self.sm_cs2 = self.sm_dpredn / self.sm_h2a
            self.sm_cs2_err = np.abs(self.sm_dpredn_err / self.sm_h2a) + np.abs(
                self.sm_dpredn * self.sm_h2a_err / self.sm_h2a
            )
            self.nm_cs2 = self.nm_dpredn / self.nm_h2a
            self.nm_cs2_err = np.abs(self.nm_dpredn_err / self.nm_h2a) + np.abs(
                self.nm_dpredn * self.nm_h2a_err / self.nm_h2a
            )
            #
        elif "2024-bhf-am" in model.lower():
            #
            self.flag_nm = True
            self.flag_sm = True
            self.flag_kf = False
            self.flag_den = True
            # 2BF
            if model.lower() == "2024-bhf-am-2bf-av8p":
                file_in1 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-SM-2BF/spin_isosp_Av8p2BF.dat",
                )
                file_in2 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-NM-2BF/spin_isosp_Av8p2BF.dat",
                )
                self.label = "BHF-2024-2BF-Av8p"
            elif model.lower() == "2024-bhf-am-2bf-av18":
                file_in1 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-SM-2BF/spin_isosp_Av182BF.dat",
                )
                file_in2 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-NM-2BF/spin_isosp_Av182BF.dat",
                )
                self.label = "BHF-2024-2BF-Av18"
            elif model.lower() == "2024-bhf-am-2bf-bonn":
                file_in1 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-SM-2BF/spin_isosp_BONN2BF.dat",
                )
                file_in2 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-NM-2BF/spin_isosp_BONN2BF.dat",
                )
                self.label = "BHF-2024-2BF-Bonn"
            elif model.lower() == "2024-bhf-am-2bf-cdbonn":
                file_in1 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-SM-2BF/spin_isosp_CDBONN2BF.dat",
                )
                file_in2 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-NM-2BF/spin_isosp_CDBONN2BF.dat",
                )
                self.label = "BHF-2024-2BF-CDBonn"
            elif model.lower() == "2024-bhf-am-2bf-sscv14":
                file_in1 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-SM-2BF/spin_isosp_SSCV142BF.dat",
                )
                file_in2 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-NM-2BF/spin_isosp_SSCV142BF.dat",
                )
                self.label = "BHF-2024-2BF-SSCV14"
            elif model.lower() == "2024-bhf-am-2bf-nsc97a":
                file_in1 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-SM-2BF/spin_isosp_NSC97a2BF.dat",
                )
                file_in2 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-NM-2BF/spin_isosp_NSC97a2BF.dat",
                )
                self.label = "BHF-2024-2BF-NSC97a"
            elif model.lower() == "2024-bhf-am-2bf-nsc97b":
                file_in1 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-SM-2BF/spin_isosp_NSC97b2BF.dat",
                )
                file_in2 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-NM-2BF/spin_isosp_NSC97b2BF.dat",
                )
                self.label = "BHF-2024-2BF-NSC97b"
            elif model.lower() == "2024-bhf-am-2bf-nsc97c":
                file_in1 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-SM-2BF/spin_isosp_NSC97c2BF.dat",
                )
                file_in2 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-NM-2BF/spin_isosp_NSC97c2BF.dat",
                )
                self.label = "BHF-2024-2BF-NSC97c"
            elif model.lower() == "2024-bhf-am-2bf-nsc97d":
                file_in1 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-SM-2BF/spin_isosp_NSC97d2BF.dat",
                )
                file_in2 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-NM-2BF/spin_isosp_NSC97d2BF.dat",
                )
                self.label = "BHF-2024-2BF-NSC97d"
            elif model.lower() == "2024-bhf-am-2bf-nsc97e":
                file_in1 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-SM-2BF/spin_isosp_NSC97e2BF.dat",
                )
                file_in2 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-NM-2BF/spin_isosp_NSC97e2BF.dat",
                )
                self.label = "BHF-2024-2BF-NSC97e"
            elif model.lower() == "2024-bhf-am-2bf-nsc97f":
                file_in1 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-SM-2BF/spin_isosp_NSC97f2BF.dat",
                )
                file_in2 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-NM-2BF/spin_isosp_NSC97f2BF.dat",
                )
                self.label = "BHF-2024-2BF-NSC97f"
            # 2+3BF
            elif model.lower() == "2024-bhf-am-23bf-av8p":
                file_in1 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-SM-23BF/spin_isosp_Av8p23BF.dat",
                )
                file_in2 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-NM-23BF/spin_isosp_Av8p23BF.dat",
                )
                self.label = "BHF-2024-23BF-Av8p"
            elif model.lower() == "2024-bhf-am-23bf-av18":
                file_in1 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-SM-23BF/spin_isosp_Av1823BF.dat",
                )
                file_in2 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-NM-23BF/spin_isosp_Av1823BF.dat",
                )
                self.label = "BHF-2024-23BF-Av18"
            elif model.lower() == "2024-bhf-am-23bfmicro-av18":
                file_in1 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-SM-23BF/spin_isosp_Av1823BFmicro.dat",
                )
                file_in2 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-NM-23BF/spin_isosp_Av1823BFmicro.dat",
                )
                self.label = "BHF-2024-23BFmicro-Av18"
            elif model.lower() == "2024-bhf-am-23bf-bonn":
                file_in1 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-SM-23BF/spin_isosp_BONN23BF.dat",
                )
                file_in2 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-NM-23BF/spin_isosp_BONN23BF.dat",
                )
                self.label = "BHF-2024-23BF-Bonn"
            elif model.lower() == "2024-bhf-am-23bfmicro-bonnb":
                file_in1 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-SM-23BF/spin_isosp_BONNB23BFmicro.dat",
                )
                file_in2 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-NM-23BF/spin_isosp_BONNB23BFmicro.dat",
                )
                self.label = "BHF-2024-23BFMicro-BonnB"
            elif model.lower() == "2024-bhf-am-23bf-cdbonn":
                file_in1 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-SM-23BF/spin_isosp_CDBONN23BF.dat",
                )
                file_in2 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-NM-23BF/spin_isosp_CDBONN23BF.dat",
                )
                self.label = "BHF-2024-23BF-CDBonn"
            elif model.lower() == "2024-bhf-am-23bf-sscv14":
                file_in1 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-SM-23BF/spin_isosp_SSCV1423BF.dat",
                )
                file_in2 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-NM-23BF/spin_isosp_SSCV1423BF.dat",
                )
                self.label = "BHF-2024-23BF-SSCV14"
            elif model.lower() == "2024-bhf-am-23bfmicro-nsc93":
                file_in1 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-SM-23BF/spin_isosp_NSC9323BFmicro.dat",
                )
                file_in2 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-NM-23BF/spin_isosp_NSC9323BFmicro.dat",
                )
                self.label = "BHF-2024-23BFmicro-NSC93"
            elif model.lower() == "2024-bhf-am-23bf-nsc97a":
                file_in1 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-SM-23BF/spin_isosp_NSC97a23BF.dat",
                )
                file_in2 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-NM-23BF/spin_isosp_NSC97a23BF.dat",
                )
                self.label = "BHF-2024-23BF-NSC97a"
            elif model.lower() == "2024-bhf-am-23bf-nsc97b":
                file_in1 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-SM-23BF/spin_isosp_NSC97b23BF.dat",
                )
                file_in2 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-NM-23BF/spin_isosp_NSC97b23BF.dat",
                )
                self.label = "BHF-2024-23BF-NSC97b"
            elif model.lower() == "2024-bhf-am-23bf-nsc97c":
                file_in1 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-SM-23BF/spin_isosp_NSC97c23BF.dat",
                )
                file_in2 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-NM-23BF/spin_isosp_NSC97c23BF.dat",
                )
                self.label = "BHF-2024-23BF-NSC97c"
            elif model.lower() == "2024-bhf-am-23bf-nsc97d":
                file_in1 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-SM-23BF/spin_isosp_NSC97d23BF.dat",
                )
                file_in2 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-NM-23BF/spin_isosp_NSC97d23BF.dat",
                )
                self.label = "BHF-2024-23BF-NSC9d7"
            elif model.lower() == "2024-bhf-am-23bf-nsc97e":
                file_in1 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-SM-23BF/spin_isosp_NSC97e23BF.dat",
                )
                file_in2 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-NM-23BF/spin_isosp_NSC97e23BF.dat",
                )
                self.label = "BHF-2024-23BF-NSC97e"
            elif model.lower() == "2024-bhf-am-23bf-nsc97f":
                file_in1 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-SM-23BF/spin_isosp_NSC97f23BF.dat",
                )
                file_in2 = os.path.join(
                    nuda.param.path_data,
                    "matter/micro/2024-BHF-NM-23BF/spin_isosp_NSC97f23BF.dat",
                )
                self.label = "BHF-2024-23BF-NSC97f"
            #
            if nuda.env.verb:
                print("Reads file:", file_in1)
            if nuda.env.verb:
                print("Reads file:", file_in2)
            self.ref = (
                "I. Vida\\~na, J. Margueron, H.J. Schulze, Universe 10, 5 (2024)."
            )
            self.note = ""
            self.marker = "o"
            self.linestyle = "solid"
            self.every = 2
            self.e_err = False
            self.p_err = False
            self.cs2_err = False
            #
            (
                self.sm_den,
                self.sm_vS0T0,
                self.sm_vS0T1,
                self.sm_vS1T0,
                self.sm_vS1T1,
                self.sm_vtot,
                self.sm_kin,
                self.sm_etot,
            ) = np.loadtxt(
                file_in1, usecols=(0, 1, 2, 3, 4, 5, 6, 7), comments="#", unpack=True
            )
            self.sm_den_min = min(self.sm_den)
            self.sm_den_max = max(self.sm_den)
            self.sm_kfn = nuda.kf_n(nuda.cst.half * self.sm_den)
            self.sm_kf = self.sm_kfn
            self.sm_e2a_int = self.sm_etot
            self.sm_e2a = self.sm_rmass + self.sm_e2a_int
            self.sm_e2a_err = np.abs(
                uncertainty_stat(self.sm_den, err="MBPT") * self.sm_e2a_int
            )
            self.sm_eps = self.sm_e2a * self.sm_den
            self.sm_eps_err = self.sm_e2a_err * self.sm_den
            #
            (
                self.nm_den,
                self.nm_vS0T0,
                self.nm_vS0T1,
                self.nm_vS1T0,
                self.nm_vS1T1,
                self.nm_vtot,
                self.nm_kin,
                self.nm_etot,
            ) = np.loadtxt(
                file_in2, usecols=(0, 1, 2, 3, 4, 5, 6, 7), comments="#", unpack=True
            )
            self.nm_den_min = min(self.sm_den)
            self.sm_den_max = max(self.sm_den)
            self.nm_kfn = nuda.kf_n(self.nm_den)
            self.nm_e2a_int = self.nm_etot
            self.nm_e2a = self.nm_rmass + self.nm_e2a_int
            self.nm_e2a_err = np.abs(
                uncertainty_stat(self.nm_den, err="MBPT") * self.nm_e2a_int
            )
            self.nm_eps = self.nm_e2a * self.nm_den
            self.nm_eps_err = self.nm_e2a_err * self.nm_den
            #
        elif model.lower() == "2024-qmc-nm":
            #
            self.flag_nm = True
            self.flag_sm = False
            self.flag_kf = False
            self.flag_den = True
            #
            file_in = os.path.join(nuda.param.path_data, "matter/micro/2024-DMC-NM.dat")
            if nuda.env.verb:
                print("Reads file:", file_in)
            self.ref = "I. Tews, R. Somasundaram, D. Lonardoni, H. Göttling, R. Seutin, J. Carlson, S. Gandolfi, K. Hebeler, A. Schwenk, arXiv:2407.08979 [nucl-th]"
            self.note = ""
            self.label = "QMC-2024"
            self.marker = "s"
            self.every = 1
            self.linestyle = "solid"
            self.e_err = True
            self.p_err = False
            self.cs2_err = False
            (
                self.nm_den,
                self.nm_e2a_int,
                self.nm_e2a_err_stat,
                self.nm_e2a_err_ekm,
                self.nm_e2a_err_gp,
            ) = np.loadtxt(file_in, usecols=(0, 1, 2, 3, 4), unpack=True)
            self.nm_kfn = nuda.kf_n(self.nm_den)
            self.nm_e2a = self.nm_rmass + self.nm_e2a_int
            self.nm_e2a_err = (
                self.nm_e2a_err_stat + self.nm_e2a_err_ekm + self.nm_e2a_err_gp
            )
            self.nm_eps = self.nm_e2a * self.nm_den
            self.nm_eps_err = self.nm_e2a_err * self.nm_den
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
                x = np.insert(self.nm_kfn, 0, 0.0)
                y = np.insert(self.nm_e2a_int, 0, 0.0)
                cs_nm_e2a = CubicSpline(x, y)
                self.nm_pre = np.array( nuda.cst.third * self.nm_kfn * self.nm_den * cs_nm_e2a(self.nm_kfn, 1) )
                y_err = np.insert(self.nm_e2a_err, 0, 0.0)
                cs_nm_e2a_err = CubicSpline(x, y_err)
                self.nm_pre_err = np.array( nuda.cst.third * self.nm_kfn * self.nm_den * cs_nm_e2a_err(self.nm_kfn, 1) )
                # chemical potential
                #self.nm_chempot = ( np.array(self.nm_pre) + np.array(self.nm_eps) ) / np.array(self.nm_den)
                #self.nm_chempot_err = ( np.array(self.nm_pre_err) + np.array(self.nm_eps_err) ) / np.array(self.nm_den)
                #
                # enthalpy
                self.nm_h2a = self.nm_e2a + self.nm_pre / self.nm_den
                #
                # sound speed as density derivative
                x = np.insert(self.nm_den, 0, 0.0)
                y = np.insert(self.nm_pre, 0, 0.0)
                cs_nm_pre = CubicSpline(x, y)
                self.nm_cs2 = cs_nm_pre(self.nm_den, 1) / self.nm_h2a
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
                x = np.insert(self.nm_den, 0, 0.0)
                y = np.insert(self.nm_e2a_int, 0, 0.0)
                cs_nm_e2a = CubicSpline(x, y)
                self.nm_pre = np.array(self.nm_den**2 * cs_nm_e2a(self.nm_den, 1))
                y_err = np.insert(self.nm_e2a_err, 0, 0.0)
                cs_nm_e2a_err = CubicSpline(x, y_err)
                self.nm_pre_err = self.nm_den**2 * cs_nm_e2a_err(self.nm_den, 1)
                #
                # chemical potential
                #self.nm_chempot = ( np.array(self.nm_pre) + np.array(self.nm_eps) ) / np.array(self.nm_den)
                #self.nm_chempot_err = ( np.array(self.nm_pre_err) + np.array(self.nm_eps_err) ) / np.array(self.nm_den)
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
            #
        if self.flag_sm:
            #
            if self.flag_kf:
                #
                # pressure in SM
                x = np.insert(self.sm_kfn, 0, 0.0)
                y = np.insert(self.sm_e2a_int, 0, 0.0)
                cs_sm_e2a = CubicSpline(x, y)
                self.sm_pre = np.array( nuda.cst.third * self.sm_kfn * self.sm_den * cs_sm_e2a(self.sm_kfn, 1) )
                y_err = np.insert(self.sm_e2a_err, 0, 0.0)
                cs_sm_e2a_err = CubicSpline(x, y_err)
                self.sm_pre_err = ( nuda.cst.third * self.sm_kfn * self.sm_den * cs_sm_e2a_err(self.sm_kfn, 1) )
                #
                # chemical potential
                #self.sm_chempot = ( np.array(self.sm_pre) + np.array(self.sm_eps) ) / np.array(self.sm_den)
                #self.sm_chempot_err = ( np.array(self.sm_pre_err) + np.array(self.sm_eps_err) ) / np.array(self.sm_den)
                #
                # enthalpy
                self.sm_h2a = self.sm_e2a + self.sm_pre / self.sm_den
                #
                # sound speed as density derivative
                x = np.insert(self.sm_den, 0, 0.0)
                y = np.insert(self.sm_pre, 0, 0.0)
                cs_sm_pre = CubicSpline(x, y)
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
                x = np.insert(self.sm_den, 0, 0.0)
                y = np.insert(self.sm_e2a_int, 0, 0.0)
                cs_sm_e2a = CubicSpline(x, y)
                self.sm_pre = np.array( self.sm_den**2 * cs_sm_e2a(self.sm_den, 1) )
                y_err = np.insert(self.sm_e2a_err, 0, 0.0)
                cs_sm_e2a_err = CubicSpline(x, y_err)
                self.sm_pre_err = self.sm_den**2 * cs_sm_e2a_err(self.sm_den, 1)
                #
                # chemical potential
                #self.sm_chempot = ( np.array(self.sm_pre) + np.array(self.sm_eps) ) / np.array(self.sm_den)
                #self.sm_chempot_err = ( np.array(self.sm_pre_err) + np.array(self.sm_eps_err) ) / np.array(self.sm_den)
                #
                # enthalpy
                self.sm_h2a = self.sm_e2a + self.sm_pre / self.sm_den
                #
                # sound speed
                #x = np.insert(self.sm_den, 0, 0.0)
                y = np.insert(self.sm_pre, 0, 0.0)
                cs_sm_pre = CubicSpline(x, y)
                self.sm_cs2 = cs_sm_pre(self.sm_den, 1) / self.sm_h2a
                #
            #
        #
        # ==============================
        # END OF
        # Compute thermodynamic quantities
        # ==============================
        #
        self.den_unit = "fm$^{-3}$"
        self.kf_unit = "fm$^{-1}$"
        self.e2a_unit = "MeV"
        self.eps_unit = "MeV fm$^{-3}$"
        self.pre_unit = "MeV fm$^{-3}$"
        #
        if nuda.env.verb:
            print("Exit setupMicro()")
        #

    def print_outputs(self):
        """
        Method which print outputs on terminal's screen.
        """
        #
        if nuda.env.verb:
            print("Enter print_outputs()")
        #
        print("- Print output:")
        print("   model:", self.model)
        print("   ref:  ", self.ref)
        print("   label:", self.label)
        print("   note: ", self.note)
        print("   self.sm_den: ", self.sm_den)
        print("   self.sm_effmass: ", self.sm_effmass)
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
        if self.sm_e2a_err is not None:
            print(f"   sm_e2a_err: {np.round(self.sm_e2a_err,3)} in {self.e2a_unit}")
        if self.sm_e2a_fit is not None:
            print(f"   sm_e2a_fit: {np.round(self.sm_e2a_fit,3)} in {self.e2a_unit}")
        if self.sm_e2a_fit_err is not None:
            print(
                f"   sm_e2a_fit_err: {np.round(self.sm_e2a_fit_err,3)} in {self.e2a_unit}"
            )
        if self.sm_eps is not None:
            print(f"   sm_eps: {np.round(self.sm_eps,3)} in {self.eps_unit}")
        if self.sm_eps_err is not None:
            print(f"   sm_eps_err: {np.round(self.sm_eps_err,3)} in {self.eps_unit}")
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
        if self.nm_e2a_err is not None:
            print(f"   nm_e2a_err: {np.round(self.nm_e2a_err,3)} in {self.e2a_unit}")
        if self.nm_e2a_fit is not None:
            print(f"   nm_e2a_fit: {np.round(self.nm_e2a_fit,3)} in {self.e2a_unit}")
        if self.nm_e2a_fit_err is not None:
            print(f"   nm_e2a_fit_err: {np.round(self.nm_e2a_fit_err,3)} in {self.e2a_unit}" )
        if self.nm_eps is not None:
            print(f"   nm_eps: {np.round(self.nm_eps,3)} in {self.eps_unit}")
        if self.nm_eps_err is not None:
            print(f"   nm_eps_err: {np.round(self.nm_eps_err,3)} in {self.eps_unit}")
        if self.nm_pre is not None:
            print(f"   nm_pre: {np.round(self.nm_pre,3)} in {self.pre_unit}")
        if self.nm_cs2 is not None:
            print(f"   nm_cs2: {np.round(self.nm_cs2,3)}")
        #
        if nuda.env.verb:
            print("Exit print_outputs()")
        #

    def init_self(self):
        """
        Initialize variables in self.
        """
        #
        if nuda.env.verb:
            print("Enter init_self()")
        #
        #: Attribute the number of points for the density.
        self.nden = 10
        #: Attribute providing the full reference to the paper to be citted.
        self.ref = ""
        #: Attribute providing additional notes about the data.
        self.note = ""
        #: Attribute the plot linestyle.
        self.linestyle = None
        #: Attribute the plot to discriminate True uncertainties from False ones.
        self.err = False
        #: Attribute the plot label data.
        self.label = ""
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
        #: Attribute the neutron matter chemical potential.
        #self.nm_chempot = None
        #: Attribute the uncertainty in the neutron matter chemical potential.
        #self.nm_chempot_err = None
        #: Attribute the symmetric matter chemical potential.
        #self.sm_chempot = None
        #: Attribute the uncertainty in the symmetric matter chemical potential.
        #self.sm_chempot_err = None
        #: Attribute the neutron matter effective mass.
        self.nm_effmass = None
        #: Attribute the symmetric matter effective mass.
        self.sm_effmass = None
        #: Attribute the neutron matter energy per particle.
        self.nm_e2a = None
        #: Attribute the uncertainty in the neutron matter energy per particle.
        self.nm_e2a_err = None
        #: Attribute the neutron matter energy per particle (fit).
        self.nm_e2a_fit = None
        #: Attribute the uncertainty in the neutron matter energy per particle (fit).
        self.nm_e2a_fit_err = None
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
        self.sm_e2a_err = None
        #: Attribute the symmetric matter energy per particle (fit).
        self.sm_e2a_fit = None
        #: Attribute the uncertainty in the symmetric matter energy per particle (fit).
        self.sm_e2a_fit_err = None
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
        self.nm_eps_err = None
        #: Attribute the symmetric matter energy per unit volume.
        self.sm_eps = None
        #: Attribute the uncertainty in the symmetric matter energy per unit volume.
        self.sm_eps_err = None
        #: Attribute the neutron matter pressure.
        self.nm_pre = None
        #: Attribute the uncertainty in the neutron matter pressure.
        self.nm_pre_err = None
        #: Attribute the neutron matter sound speed.
        self.nm_cs2 = None
        #: Attribute the uncertainty in the neutron matter sound speed.
        self.nm_cs2_err = None
        #: Attribute the symmetric matter pressure.
        self.sm_pre = None
        #: Attribute the uncertainty in the symmetric matter pressure.
        self.sm_pre_err = None
        #: Attribute the symmetric matter sound speed.
        self.sm_cs2 = None
        #: Attribute the uncertainty in the symmetric matter sound speed.
        self.sm_cs2_err = None
        #
        if nuda.env.verb:
            print("Exit init_self()")
        #
        return self
