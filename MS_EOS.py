#######################################
# Muller Serot Equation of State: PNM, SNM, Beta-equilibrated.
# Author: Sudhanva Lalit
# Last edited: 26 November 2024
#######################################
import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import pylab
from scipy.interpolate import CubicSpline
import os
import sys

# constants
hc = 197.33
pi = np.pi
pi2 = pi * pi
n0 = 0.16
msom = 0.6
knm = 230 / hc
eoa = -16.0 / hc
esym = 30.0 / hc
# masses
mst, mn, ms, mr, mw, mmu = 0.4814, 4.7585, 3.3446, 3.9021, 3.9679, 0.53720
me = 2.5897e-3
ms2 = ms * ms
mr2 = mr * mr
mw2 = mw * mw
mmu2 = mmu * mmu
# other constants
zeta = 1e-4
xi = 1.0
Ls = 0.0
Lv = 0.0  # 0.0


# define functions for solving integrals
def fg(data):
    gam, g, ms, kf, efs = data
    r = (kf + efs) / ms
    # print("r=", r, kf, efs, ms)
    return g * gam / (2.0 * pi2) * 0.5 * ms * (kf * efs - ms**2 * np.log(r))


# energy -- Needs to be replaced with just an integral
def feden(gam, kf, ms):
    if kf > 1e-12:
        if ms == 0.0:
            return gam / (2.0 * pi) * kf**4 / 4.0
        else:
            ef = np.sqrt(kf * kf + ms * ms)
            r = (kf + ef) / ms
            term = 2.0 * kf * ef**3 - kf * ef * ms**2 - ms**4 * np.log(r)
            return gam / (2.0 * pi * pi * 8.0) * term
    return 0.0


def fpres(gam, kf, ms):
    if kf > 1e-12:
        if ms == 0.0:
            return gam / (2.0 * pi) * kf**4 / 12.0
        else:
            ef = np.sqrt(kf * kf + ms * ms)
            r = (kf + ef) / ms
            term = 2.0 * kf**3 * ef - 3.0 * kf * ef * ms**2 + 3.0 * ms**4 * np.log(r)
            return gam / (2.0 * pi * pi * 24.0) * term
    else:
        return 0.0


def fcn(xf, *args):
    zeta, xi = args
    # xf is an input vector
    (cs2, cw2, b, c) = xf
    obt = 1.0 / 3.0
    ome = cw2 * n0
    dome = cw2
    phi = mn * (1.0 - msom)
    mns = mn * msom

    # momenta and energy
    gam = 4.0
    kf = (1.5 * pi * pi * n0) ** (1 / 3)
    efs = np.sqrt(kf**2 + mns**2)
    rhos = gam / (4.0 * pi * pi) * mns * (kf * efs - mns**2 * np.log((kf + efs) / mns))

    if zeta != 0.0:
        cq = 8.0 / (9.0 * cw2**3 * n0**2 * zeta)
        lr = 3 * n0 / zeta
        lr13 = lr ** (obt)
        sqt = np.sqrt(1 + cq)
        fir = (1 + sqt) ** obt
        sec = abs(1 - sqt) ** obt
        ome = lr13 * (fir - sec)
        dome = 1 / (1 / cw2 + zeta / 2 * ome**2)

    kbar = 2.0 * b * mn
    lbar = 6.0 * c
    us = kbar / 6.0 * phi**3 + lbar / 24.0 * phi**4
    duds = kbar / 2.0 * phi**2 + lbar / 6.0 * phi**3
    uv = -zeta / 24.0 * ome**4

    eq1 = phi / cs2 + duds - rhos
    eps = (
        phi**2 / (2.0 * cs2)
        + ome * n0
        - ome**2 / (2.0 * cw2)
        + us
        + uv
        + feden(gam, kf, mns)
    )
    eq2 = eps / n0 - mn - eoa
    eq3 = -(phi**2) / (2.0 * cs2) + ome**2 / (2.0 * cw2) - us - uv + fpres(gam, kf, mns)
    # knm equation
    one = 1.0 / cs2 + kbar * phi + lbar / 2.0 * phi**2
    two = 3.0 / mns * rhos
    tri = 3.0 * n0 / efs
    denr = one + two - tri
    #
    aknm = 9.0 * n0 * (dome + kf**2 / (3.0 * efs * n0) - (mns / efs) ** 2 / denr)
    eq4 = aknm - knm
    return np.array([eq1, eq2, eq3, eq4], dtype=np.float64)


def fcns(x, *args):
    (sig, ome) = x
    barn, gs, gw, b, c, gam1, zeta, xi = args
    gw2 = gw * gw
    kf = (1.5 * pi2 * barn) ** (1 / 3)
    mns = mn - gs * sig
    efs = np.sqrt(kf**2 + mns**2)
    fgar = [gam1, gs, mns, kf, efs]
    fgs = fg(fgar)
    #
    duds = b * mn * gs**3 * sig**2 + c * gs**4 * sig**3
    # equations
    eq1 = ms2 * sig + duds - fgs
    eq2 = mw2 * ome - gw * barn + zeta * gw2**2 * ome**3 / 6.0
    return np.array([eq1, eq2], dtype=np.float64)


def plot(data, **kwargs):
    xl = kwargs["xlabel"]
    yl = kwargs["ylabel"]
    fl = kwargs["filename"]
    ttl = kwargs["title"]
    fig = pylab.figure(figsize=(11, 11), dpi=600)
    ax1 = fig.add_subplot(111)
    [ax1.plot(data[0], data[i + 1], label=ttl) for i in range(len(data) - 1)]
    # ax1.plot(data[0], data[1], '-b', label=ttl)

    pylab.xlabel(xl, fontsize=24)
    pylab.ylabel(yl, fontsize=24)
    ax1.tick_params(
        direction="inout", length=10, width=2, colors="k", grid_color="k", labelsize=24
    )
    pylab.legend(loc="upper left", fontsize=24)
    pylab.ylim(auto=True)
    pylab.xlim(auto=True)
    pylab.savefig(fl)


def grcalc(data, fields):
    gs, gw, Ls, Lv = data
    sign0, omen0, mnsn0 = fields
    kf = (1.5 * pi2 * n0) ** (1 / 3)
    kf2 = kf * kf
    efs = np.sqrt(kf2 + mnsn0**2)
    t1 = Ls * (gs * sign0) ** 2
    t2 = Lv * (gw * omen0) ** 2
    fsfw = t1 + t2
    gomr2 = 1.0 / (n0 / 8.0 / (esym - kf2 / (6.0 * efs)) - 2.0 * fsfw)
    gr2 = gomr2 * mr2
    gr = np.sqrt(gr2)
    return gr


def SNM_EOS(data):
    rhomin, rhomax, gs, gw, b, c, gam, zeta, xi = data
    # print(zeta, xi)
    nb = np.linspace(rhomin, rhomax, 150)
    eps = np.zeros_like(nb)
    pres = np.zeros_like(nb)
    kf = (1.5 * pi2 * n0) ** (1 / 3)
    sig = 0
    ome = 0
    sign0 = 0
    mnsn0 = 0
    omen0 = 0
    for i in range(len(nb)):
        ls = (nb[i], gs, gw, b, c, gam, zeta, xi)
        if i == 0:
            xs = (0.01 * mn / gs, gw * nb[i] / mw2)
        xs = fsolve(fcns, xs, args=ls)
        sig = xs[0]
        ome = xs[1]
        mns = mn - gs * sig
        if nb[i] == 0.16:
            sign0 = sig
            omen0 = ome
            mnsn0 = mns
        # gwom = hc * gw * ome
        us = b / 3.0 * mn * (gs * sig) ** 3 + c / 4.0 * (gs * sig) ** 4
        uv = zeta / 8.0 * (gw * ome) ** 4
        edenb = (
            0.5 * (ms * sig) ** 2
            + 0.5 * (mw * ome) ** 2
            + us
            + uv
            + feden(gam, kf, mns)
        )
        eps[i] = edenb * hc
        enrp = (edenb / nb[i] - mn) * hc
        presb = (
            -0.5 * (ms * sig) ** 2
            + 0.5 * (mw * ome) ** 2
            - us
            + uv / 3.0
            + fpres(gam, kf, mns)
        )
        pres[i] = presb * hc
    # Evaluate speed of sound:
    presInterp = CubicSpline(nb, pres)
    epsInterp = CubicSpline(nb, eps)
    cs2 = presInterp(nb, 1) / epsInterp(nb, 1)
    return np.array([nb, eps, pres, cs2]), np.array([sign0, omen0, mnsn0])


def MS_EOS(data, fields):
    rhomin, rhomax, gs, gw, b, c, gam1, Ls, Lv, zeta, xi = data
    nb = np.linspace(rhomin, rhomax, 150)
    eps = np.zeros_like(nb)
    pres = np.zeros_like(nb)
    coups = (gs, gw, Ls, Lv)
    gr = grcalc(coups, fields)
    # print("Gr:", gs, gw, gr, b, c, gam1)
    for i in range(len(nb)):
        ls = (nb[i], gs, gw, gr, b, c, gam1, Ls, Lv, zeta, xi)
        if i == 0:
            # xs = np.ones(7) * 0.1
            xs = (
                0.01 * mn / gs,
                gw * nb[i] / mw2,
                -gr * nb[i] / (2.0 * mr2),
                (3.0 * pi2 * nb[i]) ** (1 / 2),
                1e-5,
                1e-5,
                1e-5,
            )
        xs = fsolve(EoS_func, xs, args=ls)
        sig = xs[0]
        ome = xs[1]
        rho = xs[2]
        kfn = xs[3]
        kfp = xs[4]
        kfe = xs[5]
        kfmu = xs[6]
        # print("sig", xs)
        mns = mn - gs * sig
        #     #
        efns = np.sqrt(kfn * kfn + mns * mns)
        efps = np.sqrt(kfp * kfp + mns * mns)
        #     #
        mun = gw * ome - 0.5 * gr * rho + efns
        mup = gw * ome - 0.5 * gr * rho + efps
        mue = mun - mup
        # mue = kfe
        #     # Mass fractions
        nmu = kfmu**3 / (3.0 * pi2)
        ne = kfe**3 / (3.0 * pi2)
        nn = kfn**3 / (3.0 * pi2)
        npr = kfp**3 / (3.0 * pi2)
        #
        us = b / 3.0 * mn * (gs * sig) ** 3 + c / 4.0 * (gs * sig) ** 4
        uv = zeta / 8.0 * (gw * ome) ** 4
        ur = xi / 8.0 * (gr * rho) ** 4
        epsmix1 = gr**2 * rho**2 * gw**2 * ome**2 * Lv
        epsmix2 = gr**2 * rho**2 * (Ls * gs**2 * sig**2 + Lv * gw**2 * ome**2)
        epsmix = epsmix1 + 2.0 * epsmix2
        edenb = (
            0.5 * (ms * sig) ** 2
            + 0.5 * (mw * ome) ** 2
            + 0.5 * (mr * rho) ** 2
            + us
            + uv
            + ur
            + epsmix
            + feden(gam1, kfn, mns)
            + feden(gam1, kfp, mns)
        )
        edenl = feden(gam1, kfe, 0.0) + feden(gam1, kfmu, mmu)
        eps[i] = (edenb + edenl) * hc
        enrp = (eps[i] / nb[i] - mn) * hc
        presb = (
            -0.5 * (ms * sig) ** 2
            + 0.5 * (mw * ome) ** 2
            + 0.5 * (mr * rho) ** 2
            - us
            + uv / 3.0
            + ur / 3.0
            + fpres(gam1, kfn, mns)
            + fpres(gam1, kfp, mns)
            + fpres(gam1, kfe, 0.0)
            + fpres(gam1, kfmu, mmu)
            + epsmix2
        )
        pres[i] = presb * hc
    # Evaluate speed of sound:
    # presInterp = CubicSpline(nb, pres)
    # epsInterp = CubicSpline(nb, eps)
    presDeriv = np.gradient(pres, nb)
    epsDeriv = np.gradient(eps, nb)
    cs2 = presDeriv / epsDeriv
    print("Success, MS EOS file created")
    return np.array([nb, eps, pres, cs2])


def EoS_func(x, *data):
    for i in range(3, 7):
        if x[i] < 0:
            x[i] = 0.0
    (sig, ome, rho, kfn, kfp, kfe, kfmu) = x
    barn, gs, gw, gr, b, c, gam1, Ls, Lv, zeta, xi = data
    gw2 = gw * gw
    tpi2 = 3 * pi**2
    # number densitites
    nn = kfn**3 / tpi2
    npr = kfp**3 / tpi2
    ne = kfe**3 / tpi2
    nmu = kfmu**3 / tpi2
    #
    mns = mn - gs * sig
    # Energies
    efns = np.sqrt(kfn * kfn + mns * mns)
    efps = np.sqrt(kfp * kfp + mns * mns)
    # chemical potentials
    mun = gw * ome - 0.5 * gr * rho + efns
    mup = gw * ome + 0.5 * gr * rho + efps
    mue = kfe
    mumu = np.sqrt(kfmu * kfmu + mmu**2)
    # integrals
    fgn = fg((gam1, gs, mns, kfn, efns))
    fgp = fg((gam1, gs, mns, kfp, efps))
    #
    duds = b * mn * gs**3 * sig**2 + c * gs**4 * sig**3
    dvds = zeta / 2 * gw2**2 * ome**3
    #
    mixs = 2.0 * gr**2 * rho**2 * Ls * gs**2 * sig
    mixw = 2.0 * gr**2 * rho**2 * Lv * gw**2 * ome
    mixr = 2.0 * gr**2 * rho * (Ls * gs**2 * sig**2 + Lv * gw**2 * ome**2)
    # equations
    eq1 = ms2 * sig + duds - (fgn + fgp) - mixs
    eq2 = mw2 * ome - gw * (nn + npr) + zeta * gw**4 * ome**3 / 6.0 + mixw
    eq3 = mr2 * rho - 0.5 * gr * (npr - nn) + xi * gr**4 * rho**3 / 6 + mixr
    #
    eq4 = mun - mup - mue  # charge neutrality
    eq5 = barn - (nn + npr)
    eq6 = npr - (ne + nmu)
    eq7 = kfmu
    if mue > mmu:
        eq7 = mue - mumu
    return np.array([eq1, eq2, eq3, eq4, eq5, eq6, eq7], dtype=np.float64)


def main():
    gam = 4.0
    gam1 = 2.0
    xf = (10.0, 10.0, 2e-3, 2e-3)
    ls = (zeta, xi)
    # find coupling constants
    [cs2, cw2, b, c] = fsolve(fcn, xf, args=ls)
    gs2 = cs2 * ms2
    gw2 = cw2 * mw2
    gs = np.sqrt(gs2)
    gw = np.sqrt(gw2)
    rhomin = np.float64(0.02)
    rhomax = np.float64(3.0)
    scvein = (rhomin, rhomax, gs, gw, b, c, gam, zeta, xi)
    snmEOS, fields = SNM_EOS(scvein)
    nameList = "nb (fm^-1)   E (MeV)     P (MeV/fm^3)    cs2"
    # np.savetxt("MS_SNM.dat", snmEOS.T, fmt="%.6e", header=nameList)
    nb, eps, pres, speedOfSound = snmEOS
    scvein = (rhomin, rhomax, gs, gw, b, c, gam1, Ls, Lv, zeta, xi)
    fullEOS = MS_EOS(scvein, fields)
    np.savetxt("MS_EOS.dat", fullEOS.T, fmt="%.6e", header=nameList)


if __name__ == "__main__":
    main()
