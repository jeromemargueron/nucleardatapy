import numpy as np

import numpy as np
from scipy.integrate import cumulative_trapezoid


class Random_speed_of_sound:
    """
    Construct an EoS from a randomly generated piecewise-linear
    speed-of-sound-squared profile.

    Parameters
    ----------
    den_min : float
        Starting density [fm^-3].

    den_max : float
        Maximum density [fm^-3].

    n_random : int
        Number of random interior density nodes above den_min.

    n_eos : int
        Target number of density points in the complete EoS.

    cs2_tr : float
        Known speed of sound squared at den_min.

    mu0 : float
        Known baryon chemical potential at den_min [MeV].

    pre0 : float
        Known pressure at den_min [MeV fm^-3].

    eps0 : float
        Known energy density at den_min [MeV fm^-3].

    seed : int or None
        Random seed for reproducibility.

    Notes
    -----
    The endpoint den_max is included as a node and is assigned
    a randomly generated cs2 value.

    The random interior nodes and the endpoint are generated
    above the known starting point.

    Natural units are used, with c = 1.
    """

    def __init__(self, **kwargs):

        # --------------------------------------------------
        # 1. Input parameters
        # --------------------------------------------------
        self.den_tr = kwargs.get("den_tr",0.2)
        self.den_max = kwargs.get("den_max",2.0)

        self.n_random = kwargs.get("n_random", 11)
        self.n_eos = kwargs.get("n_eos", 60)
        self.seed = kwargs.get("seed", None)

        self.cs2_tr = kwargs.get("cs2_tr")
        self.mu_tr = kwargs.get("mu_tr")
        self.pre_tr = kwargs.get("pre_tr")
        self.eps_tr = kwargs.get("eps_tr")
        self.eos_data = None
        
        self.full_outputs = kwargs.get("full_outputs")

        
        if self.den_tr is None or self.den_max is None:
            raise ValueError("Specify den_tr and den_max.")       

        if self.cs2_tr is None:
            raise ValueError("Specify cs2_tr.")

        if not 0 <= self.cs2_tr <= 1:
            print(self.cs2_tr)
            raise ValueError("Require 0 <= cs2_tr <= 1.")

        if self.mu_tr is None or self.pre_tr is None or self.eps_tr is None:
            raise ValueError("Specify mu0, pre0, and eps0.")

        #if any(self.mu_tr <= 0 or self.pre_tr<=0 or self.eps_tr<=0) :
            #raise ValueError("mu0,pre0,eps0, must be positive.")
        
        rng = np.random.default_rng(self.seed)

        den_interior = rng.uniform(self.den_tr,self.den_max,self.n_random)

        # Starting point is known.
        # The maximum-density endpoint is also included.
        self.den_random = np.sort(np.concatenate(([self.den_tr],den_interior,[self.den_max])))
        self.den_random = np.unique(self.den_random)
        self.cs2_random = np.concatenate(([self.cs2_tr],rng.uniform(0.0, 1.0, len(self.den_random) - 1)))
        self.den_cs2_pair = np.column_stack((self.den_random,self.cs2_random))
        
    def _construct_density_mesh(self):
        dn = np.diff(self.den_random)
        n_intervals = len(dn)
        n_segments_total = max(self.n_eos - 1, n_intervals )
        remaining = n_segments_total - n_intervals
        weights = dn / np.sum(dn)
        raw = remaining * weights
        extra = np.floor(raw).astype(int)
        n_left = remaining - np.sum(extra)
        if n_left > 0:
            order = np.argsort(raw - extra)[::-1]
            extra[order[:n_left]] += 1
        n_segments = 1 + extra
        meshes = []
    

        for i in range(n_intervals):

            ni = self.den_random[i]
            nj = self.den_random[i + 1]

            mesh_i = np.linspace( ni, nj, n_segments[i] + 1  )

            if i > 0:
                mesh_i = mesh_i[1:]
            meshes.append(mesh_i)

        self.den = np.concatenate(meshes)
        self.n_segments = n_segments

    # ======================================================
    # Reconstruct the EoS interval by interval
    # ======================================================
    def _construct_eos(self):

        den_all = []
        cs2_all = []
        mu_all = []
        pre_all = []
        eps_all = []

        mu_left = self.mu_tr
        pre_left = self.pre_tr
        eps_left = self.eps_tr

        for i in range(len(self.den_random) - 1):

            ni = self.den_random[i]
            nj = self.den_random[i + 1]

            ci = self.cs2_random[i]
            cj = self.cs2_random[i + 1]

            # Local density mesh, including both endpoints.
            n = np.linspace(ni, nj, self.n_segments[i] + 1)

            # Linear sound-speed profile.
            slope = (cj - ci) / (nj - ni)
            cs2 = ci + slope * (n - ni)

            # Chemical potential from the analytic integral.
            integral = ((ci - slope * ni) * np.log(n / ni) + slope * (n - ni) )

            mu = mu_left * np.exp(integral)

            # Integrate pressure and energy density.
            pre = pre_left + cumulative_trapezoid(cs2 * mu, n, initial=0.0  )

            eps = eps_left + cumulative_trapezoid( mu, n, initial=0.0 )
            start = 0 if i == 0 else 1

            den_all.extend(n[start:])
            cs2_all.extend(cs2[start:])
            mu_all.extend(mu[start:])
            pre_all.extend(pre[start:])
            eps_all.extend(eps[start:])

            # Carry the right endpoint into the next interval.
            mu_left = mu[-1]
            pre_left = pre[-1]
            eps_left = eps[-1]

        self.den = np.asarray(den_all)
        self.cs2 = np.asarray(cs2_all)
        self.mu = np.asarray(mu_all)
        self.pre = np.asarray(pre_all)
        self.eps = np.asarray(eps_all)

        self.eos = np.column_stack((
            self.den, self.cs2, self.mu, self.pre, self.eps
        ))
    def get_eos(self):
        
        self._construct_density_mesh()
        self._construct_eos()
        if self.den is None:
            return None
        if  self.pre is None:
            return None
            
        if self.eps is None:
            return None
        self.eos_data = { "den": self.den,"pre": self.pre,"eps": self.eps }
        self.all_data=self.eos_data
        self.all_data["cs2"]=self.cs2
        self.all_data["mu"]= self.mu  
        
        if self.full_outputs :
            return self.all_data
        else:
            return self.eos_data
       
"""    
eos = Random_speed_of_sound(
    den_tr=0.5,
    den_max=2.,
    n_random=10,
    n_eos=60,
    cs2_tr=0.25,
    mu_tr=1100.0,
    pre_tr=50.0,
    eps_tr=500.0,
    seed=123
)

eos.get_eos()
# Random nodes and their sound speeds
print(eos.den_cs2_pair)

# Reconstructed EoS
den = eos.den
cs2 = eos.cs2
mu = eos.mu
pre = eos.pre
eps = eos.eps


import matplotlib.pyplot as plt

# Plot chemical potential
plt.figure(figsize=(8, 5))

plt.plot(eos.den, eos.mu,label=r"$\mu(n)$")
plt.plot(eos.den, (eos.pre+eos.eps)/eos.den,label=r"$\mu(n)$")

# Mark random density nodes
#plt.scatter(eos.den_random,eos.cs2_random * 0 + [ eos.mu[np.argmin(np.abs(eos.den - n))]  for n in eos.den_random],marker="o",label="Random density nodes")

plt.xlabel(r"Density $n$ [fm$^{-3}$]")
plt.ylabel(r"Chemical potential $\mu$ [MeV]")
plt.title("Chemical potential")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 5))

plt.plot(eos.den, eos.cs2,label=r"$c^2(n)$")
plt.scatter(eos.den_random, eos.cs2_random,label=r"$c^2$")

# Mark random density nodes
#plt.scatter(eos.den_random,eos.cs2_random * 0 + [ eos.mu[np.argmin(np.abs(eos.den - n))]  for n in eos.den_random],marker="o",label="Random density nodes")

plt.xlabel(r"Density $n$ [fm$^{-3}$]")
plt.ylabel(r"$c^2_s$")
#plt.title("Chemical potential")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


import numpy as np

mu_thermo = (eos.eps + eos.pre) / eos.den

print("Segment | Density | mu | (eps + pre)/den | Difference")

for i, n in enumerate(eos.den_random):
    j = np.argmin(np.abs(eos.den - n))

    print(
        f"{i:3d} | "
        f"{n:.6f} | "
        f"{eos.mu[j]:.6f} | "
        f"{mu_thermo[j]:.6f} | "
        f"{mu_thermo[j] - eos.mu[j]:.6e}"
    )
    
"""
