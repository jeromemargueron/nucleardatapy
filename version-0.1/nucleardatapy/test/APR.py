import numpy as np
from scipy.optimize import root
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import os, sys
from scipy.interpolate import CubicSpline

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

# Define constants
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
    -382,
    89.8,
    0.457,
    -59.0,
    -19.1,
    214.6,
    -384,
    6.4,
    69,
    -33,
    0.35,
    0,
    0,
    287.0,
    -1.54,
    175.0,
    -1.45,
    0.32,
    0.195,
    0,
)

G = (3 * np.pi**2) ** (5 / 3) / (5 * np.pi**2)
hb = 197.327
m = 939
me = 0.511
mmu = 105.658


# Define functions
def Hk(n, x):
    return G * hb**2 / (2 * m) * n ** (5 / 3) * ((1 - x) ** (5 / 3) + x ** (5 / 3))


def Hm(n, x):
    return (
        G
        * (
            p3 * ((1 - x) ** (5 / 3) + x ** (5 / 3))
            + p5 * ((1 - x) ** (8 / 3) + x ** (8 / 3))
        )
        * n ** (8 / 3)
        * np.exp(-p4 * n)
    )


def g1L(n):
    return -(n**2) * (
        p1 + p2 * n + p6 * n**2 + (p10 + p11 * n) * np.exp(-(p9**2) * n**2)
    )


def g1H(n):
    return g1L(n) - n**2 * (p17 * (n - p19) + p21 * (n - p19) ** 2) * np.exp(
        p18 * (n - p19)
    )


def g2L(n):
    return -(n**2) * (p12 / n + p7 + p8 * n + p13 * np.exp(-(p9**2) * n**2))


def g2H(n):
    return g2L(n) - n**2 * (p15 * (n - p20) + p14 * (n - p20) ** 2) * np.exp(
        p16 * (n - p20)
    )


def HdL(n, x):
    return g1L(n) * (1 - (1 - 2 * x) ** 2) + g2L(n) * (1 - 2 * x) ** 2


def HdH(n, x):
    return g1H(n) * (1 - (1 - 2 * x) ** 2) + g2H(n) * (1 - 2 * x) ** 2


def HL(n, x):
    return Hk(n, x) + Hm(n, x) + HdL(n, x)


def HH(n, x):
    return Hk(n, x) + Hm(n, x) + HdH(n, x)


def EOAL(n, x):
    return HL(n, x) / n


def EOAH(n, x):
    return HH(n, x) / n


def PL(n, x):
    return n**2 * (np.gradient(EOAL(n, x), n))


def PH(n, x):
    return n**2 * (np.gradient(EOAH(n, x), n))


def mupL(n, x):
    # print("n:", n, "x:", x)
    return np.gradient(HL(n, x), n) + (1 - x) / n * np.gradient(HL(n, x), x)


def munL(n, x):
    return np.gradient(HL(n, x), n) - x / n * np.gradient(HL(n, x), x)


def mupH(n, x):
    return np.gradient(HH(n, x), n) + (1 - x) / n * np.gradient(HH(n, x), x)


def munH(n, x):
    return np.gradient(HH(n, x), n) - x / n * np.gradient(HH(n, x), x)


def kfe(n, x, y):
    return (3 * np.pi**2 * n * x * y) ** (1 / 3) * hb


def kfmu(n, x, y):
    return (3 * np.pi**2 * n * x * (1 - y)) ** (1 / 3) * hb


def kfp(n, x):
    return (3 * np.pi**2 * n * x) ** (1 / 3) * hb


def kfn(n, x):
    return (3 * np.pi**2 * n * (1 - x)) ** (1 / 3) * hb


def mue(n, x, y):
    return np.sqrt(kfe(n, x, y) ** 2 + me**2)


def pe(n, x, y):
    kfe_val = kfe(n, x, y)
    mue_val = mue(n, x, y)
    return (
        1
        / (24 * np.pi**2 * hb**3)
        * (
            kfe_val * mue_val * (2 * kfe_val**2 - 3 * me**2)
            - 3 * me**4 * np.log(me / (kfe_val + mue_val))
        )
    )


def mumu(n, x, y):
    return np.sqrt(kfmu(n, x, y) ** 2 + mmu**2)


def pmu(n, x, y):
    kfmu_val = kfmu(n, x, y)
    mumu_val = mumu(n, x, y)
    return (
        1
        / (24 * np.pi**2 * hb**3)
        * (
            kfmu_val * mumu_val * (2 * kfmu_val**2 - 3 * mmu**2)
            - 3 * mmu**4 * np.log(mmu / (kfmu_val + mumu_val))
        )
    )


def pltot(n, x, y):
    return PL(n, x) + pe(n, x, y) + pmu(n, x, y)


def phtot(n, x, y):
    return PH(n, x) + pe(n, x, y) + pmu(n, x, y)


def mulave(n, x, y):
    return (1 - x) * munL(n, x) + x * (
        mupL(n, x) + y * mue(n, x, y) + (1 - y) * mumu(n, x, y)
    )


def muhave(n, x, y):
    return (1 - x) * munH(n, x) + x * (
        mupH(n, x) + y * mue(n, x, y) + (1 - y) * mumu(n, x, y)
    )


def edenltot(n, x, y):
    return n * mulave(n, x, y) - pltot(n, x, y)


def edenhtot(n, x, y):
    return n * muhave(n, x, y) - phtot(n, x, y)


def xeqe(n):
    return root(
        lambda x: mue(n, x, 1) + mupL(n, x) - munL(n, x), 0.1 * np.ones(len(n))
    ).x


def xleqmu(n):
    res = root(
        lambda vars: [
            mue(n, vars[0], vars[1]) + mupL(n, vars[0]) - munL(n, vars[0]),
            mue(n, vars[0], vars[1]) - mumu(n, vars[0], vars[1]),
        ],
        [0.1, 0.1],
    )
    return res.x[0]


def yleqmu(n):
    res = root(
        lambda vars: [
            mue(n, vars[0], vars[1]) + mupL(n, vars[0]) - munL(n, vars[0]),
            mue(n, vars[0], vars[1]) - mumu(n, vars[0], vars[1]),
        ],
        [0.1, 0.1],
    )
    return res.x


def xheqmu(n):
    res = root(
        lambda vars: [
            mue(n, vars[0], vars[1]) + mupH(n, vars[0]) - munH(n, vars[0]),
            mue(n, vars[0], vars[1]) - mumu(n, vars[0], vars[1]),
        ],
        [0.1, 0.1],
    )
    return res.x[0]


def yheqmu(n):
    res = root(
        lambda vars: [
            mue(n, vars[0], vars[1]) + mupH(n, vars[0]) - munH(n, vars[0]),
            mue(n, vars[0], vars[1]) - mumu(n, vars[0], vars[1]),
        ],
        [0.1, 0.1],
    )
    return res.x[1]


def ptot(n):
    if n <= 0.08:
        return psub(n)
    elif 0.08 < n < nonsetmu:
        return pltot(n, xeqe(n), 1)
    elif nonsetmu <= n < nlt:
        return pltot(n, xleqmu(n), yleqmu(n))
    elif nlt <= n < nht:
        return pltot(nlt, xlt, ylt)
    else:
        return phtot(n, xheqmu(n), yheqmu(n))


def edentot(n):
    if n <= 0.08:
        return edensub(n) - m * n
    elif 0.08 < n < nonsetmu:
        return edenltot(n, xeqe(n), 1)
    elif nonsetmu <= n < nlt:
        return edenltot(n, xleqmu(n), yleqmu(n))
    elif nlt <= n < nht:
        return n * mulave(nlt, xlt, ylt) - pltot(nlt, xlt, ylt)
    else:
        return edenhtot(n, xheqmu(n), yheqmu(n))


def ens(n):
    return edentot(n) + m * n


def pns(n):
    return ptot(n)


def logspace(b, c, i):
    return np.logspace(b, c, num=i)


def main():
    n = logspace(0.2, -10.8, 200) 
    EoverA = EOAH(n, 0.5)
    Pressure = PH(n, 0.5)
    # Read data file:
    file_in1 = os.path.join(nuda.param.path_data,'eos/micro/1998-VAR-NM-APR.dat')
    file_in2 = os.path.join(nuda.param.path_data,'eos/micro/1998-VAR-SM-APR.dat')

    nm_den, nm_e2a = np.loadtxt( file_in1, usecols=(0,1), unpack = True )
    sm_den, sm_e2a = np.loadtxt( file_in2, usecols=(0,1), unpack = True )

    # SNM calculation
    plt.plot(n, EoverA, label="Calculated")
    plt.plot(sm_den, sm_e2a, 'o', label="Data")
    plt.title("SNM")
    plt.legend()
    plt.savefig("APR-EOA-SNM.pdf")
    plt.cla()

    # PNM calculation
    EoverA_PNM = EOAH(n, 0.0)
    Pressure = PH(n, 0.0)
    plt.plot(n, EoverA_PNM, label="Calculated")
    plt.plot(nm_den, nm_e2a, 'o', label="Data")
    plt.title("PNM")
    plt.legend()
    plt.savefig("APR-EOA-PNM.pdf")
    plt.cla()

    plt.plot(n, Pressure)
    plt.savefig("APR-Press.pdf")
    plt.cla()


    # nonsetmu = root(lambda n: mue(n, xeqe(n), 1) - mmu, 0.1).x  # [0]
    # print(nonsetmu)

    # coex = root(lambda vars: [pltot(vars[0], vars[2], vars[4]) - phtot(vars[1], vars[3], vars[5]),
    #                         mulave(vars[0], vars[2], vars[4]) - muhave(vars[1], vars[3], vars[5]),
    #                         mue(vars[0], vars[2], vars[4]) - mumu(vars[0], vars[2], vars[4]),
    #                         mue(vars[1], vars[3], vars[5]) - mumu(vars[1], vars[3], vars[5]),
    #                         munL(vars[0], vars[2]) - mupL(vars[0], vars[2]) - mue(vars[0], vars[2], vars[4]),
    #                         munH(vars[1], vars[3]) - mupH(vars[1], vars[3]) - mue(vars[1], vars[3], vars[5])],
    #             [0.15, 0.25, 0.05, 0.1, 0.9, 0.5]).x

    # nlt, nht, xlt, xht, ylt, yht = coex

    # # Assuming subeos is a 2D array with the third, first, and second columns being used respectively
    # subeos = np.loadtxt("/home/constant/Desktop/beta_EOS/lowden_eos.dat")

    # edensub = interp1d(subeos[:, 2], subeos[:, 0], kind='linear')
    # psub = interp1d(subeos[:, 2], subeos[:, 1], kind='linear')


if __name__ == "__main__":
    main()
