import numpy as np
import nucleardatapy as nuda
import numpy as np
import matplotlib.pyplot as plt

from scipy.interpolate import ( CubicSpline, PchipInterpolator,  UnivariateSpline )


NVcrust=nuda.crust.setupCrust( model = '1973-Negele-Vautherin' )

nB = np.asarray(NVcrust.den, dtype=float)
eps = np.asarray(NVcrust.eps_tot, dtype=float)

x = np.insert(NVcrust.den, 0, 0.0)
y = np.insert(NVcrust.eps_tot, 0, 0.0)
cs_eps_tot = CubicSpline(x,y)
pre_tot = np.array(NVcrust.den* cs_eps_tot(NVcrust.den, 1)-NVcrust.eps_tot)



mask = ( np.isfinite(nB) & np.isfinite(eps) & (nB > 0) & (eps > 0))

nB = nB[mask]
eps = eps[mask]

order = np.argsort(nB)
nB = nB[order]
eps = eps[order]

logn = np.log(nB)
loge = np.log(eps)


# A. Cubic spline
spline = CubicSpline(logn, loge, extrapolate=False)

# B. PCHIP
PCHIP = PchipInterpolator(logn, loge, extrapolate=False)

# C. Smoothing spline
smooth = UnivariateSpline(logn, loge, s=0, k=3)

fig = plt.figure(figsize=(7, 6))

interpolations = [spline, PCHIP, smooth]
labels = ['Cubic Spline (log n - log eps)', 'PCHIP (log n - log eps)', 'Smoothing Spline (log n - log eps)']
markers = ['s', 'o', '^']
sizes = [55, 45, 35]

for i, interpolation in enumerate(interpolations):

    # Interpolate energy density in log-log space
    eps_interp = np.exp(interpolation(logn))

    # Derivative: d(log(eps))/d(log(n))
    dlogeps_dlogn = interpolation.derivative()(logn)

    # Calculate d(eps)/dn
    deps_dn = eps_interp / nB * dlogeps_dlogn

    # Thermodynamic pressure
    pressure = nB * deps_dn - eps_interp

    # Check for negative pressure
    negative = pressure < 0

    if np.any(negative):
        print(f"\n{labels[i]}: negative pressure found")
        print(pressure[negative])
        print("Negative pressure found at densities:")
        print(nB[negative])

    # Scatter plot with different marker shapes and sizes
    plt.scatter(nB,pressure,label=labels[i],marker=markers[i],s=sizes[i],alpha=0.8)

plt.loglog(nB,pre_tot,label='Cubic Spline (n-eps), has 0 starting point)')

plt.text( 0.05, 0.95, r'$P = n_B \frac{d\varepsilon}{dn_B} - \varepsilon$', transform=plt.gca().transAxes, fontsize=14, verticalalignment='top')
plt.xscale('log')
#plt.yscale('symlog')
#plt.ylim(-1e-3,6e-1)
plt.yscale('log')
plt.xlabel(r'$n_B \ [\rm fm^{-3}]$',size=14)
plt.ylabel(r'$P\ \ [\rm MeV fm^{-3}]$',size=15)
plt.legend()
plt.minorticks_on()
plt.tick_params(labelsize=17)
fig.savefig('NV_Pressure_Derivative_using_energy_density.png',bbox_inches='tight')
    
    
nB = np.asarray(NVcrust.den, dtype=float)
e2a = np.asarray(NVcrust.e2a_tot, dtype=float)
mask = ( np.isfinite(nB) & np.isfinite(e2a) & (nB > 0) & (eps > 0))

nB = nB[mask]
e2a = e2a[mask]

order = np.argsort(nB)
nB = nB[order]
e2a = e2a[order]

logn = np.log(nB)
loge2a = np.log(e2a)


# A. Cubic spline
spline = CubicSpline(logn, loge2a, extrapolate=False)

# B. PCHIP
PCHIP = PchipInterpolator(logn, loge2a, extrapolate=False)

# C. Smoothing spline
smooth = UnivariateSpline(logn, loge2a, s=0, k=3)

fig = plt.figure(figsize=(8, 5))

interpolations = [spline, PCHIP, smooth]
labels = ['Cubic Spline (log n- log e)', 'PCHIP (log n- log e)', 'Smoothing Spline (log n- log e)']
markers = ['s', 'o', '^']
sizes = [55, 45, 35]

for i, interpolation in enumerate(interpolations):

    # Interpolate energy density in log-log space
    e2a_interp = np.exp(interpolation(logn))

    # Derivative: d(log(eps))/d(log(n))
    dloge2a_dlogn = interpolation.derivative()(logn)

    # Calculate d(eps)/dn
    de2a_dn = e2a_interp / nB * dloge2a_dlogn

    # Thermodynamic pressure
    pressure = nB**2 * de2a_dn

    # Check for negative pressure
    negative = pressure < 0

    if np.any(negative):
        print(f"\n{labels[i]}: negative pressure found using EbyA")
        print(pressure[negative])
        print("Negative pressure found at densities:")
        print(nB[negative])

    # Scatter plot with different marker shapes and sizes
    plt.scatter(nB,pressure,label=labels[i],marker=markers[i],s=sizes[i],alpha=0.8)



x = NVcrust.den
y = NVcrust.e2a_tot
cs_e2a_tot = CubicSpline(x,y)
pre_tot2 = NVcrust.den**2 * cs_e2a_tot(NVcrust.den, 1)
print("relative error in Pressure from n-E/A interpolation and n-eps interpolation, without log scaling",np.abs((pre_tot2-pre_tot))/pre_tot)
plt.loglog(nB,pre_tot2,label='Cubic Spline  n-e, no 0 starting point')
plt.loglog(nB,pre_tot,'--',label='Cubic Spline (n-eps), has 0 starting point)')

plt.text( 0.85, 0.25, r'$P = n_B^2 \frac{de}{dn_B}$', transform=plt.gca().transAxes, fontsize=14, verticalalignment='top')

plt.xscale('log')
#plt.yscale('symlog')
#plt.ylim(-1e-3,6e-1)
plt.yscale('log')
plt.xlabel(r'$n_B \ [\rm fm^{-3}]$',size=14)
plt.ylabel(r'$P\ \ [\rm MeV fm^{-3}]$',size=15)
plt.legend()
plt.minorticks_on()
plt.tick_params(labelsize=17)
fig.savefig('NV_Pressure_Using_EbyA.png',bbox_inches='tight')
    
