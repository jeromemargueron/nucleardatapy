import numpy as np
from pathlib import Path
from scipy.interpolate import interp1d
from scipy.optimize import brentq, root
from scipy.interpolate import CubicSpline, PchipInterpolator
from scipy.optimize import least_squares
from scipy.integrate import cumulative_trapezoid
import nucleardatapy as nuda
"""
class Maxwell_construction:
    def __init__(self,regions=None):
        
        self.pre_r1=np.asarray(regions['r1']['pres'])
        self.mub_r1=np.asarray(regions['r1']['mub'])
        self.pre_r2=np.asarray(regions['r2']['pres'])
        self.mub_r2=np.asarray(regions['r2']['pres'])                 
        self.check=True
"""

class Maxwell_construction:
    def __init__(self, regions):

        
        if not isinstance(regions, dict):
            raise TypeError("regions must be a dictionary.")
        required_regions = {'r1', 'r2'}
        missing_regions = required_regions - regions.keys()
        if missing_regions:
            raise ValueError(f"Missing region(s): {', '.join(sorted(missing_regions))}")
        for region in required_regions:
            if not isinstance(regions[region], dict):
                raise TypeError(f"'{region}' must contain a dictionary with 'pre' and 'mub'.")

            # Check that pressure and chemical potential are provided
            required_keys = {'pre', 'mub'}
            missing_keys = required_keys - regions[region].keys()

            if missing_keys:
                raise ValueError( f"Missing key(s) in '{region}': " f"{', '.join(sorted(missing_keys))}" )

            # Convert data to NumPy arrays
            pre = np.asarray(regions[region]['pre'], dtype=float)
            mub = np.asarray(regions[region]['mub'], dtype=float)

            # Check array dimensions
            if pre.ndim != 1 or mub.ndim != 1:
                raise ValueError(f"Pressure and mub in '{region}' must be 1D arrays.")

            # Check matching array lengths
            if pre.size != mub.size:
                raise ValueError( f"Pressure and mub in '{region}' must have the same length.")

            if pre.size == 0:
                raise ValueError(f"'{region}' contains empty data.")

            # Assign attributes
            setattr(self, f"pre_{region}", pre)
            setattr(self, f"mub_{region}", mub)

        self.check = False

    def muc_pc_intersection(self):
        
        mub1=self.mub_r1
        mub2=self.mub_r2
        pb1=self.pre_r1
        pb2=self.pre_r2
        mask1 = np.isfinite(mub1) & np.isfinite(pb1) & (mub1 > 0) & (pb1 > 0)
        mask2 = np.isfinite(mub2) & np.isfinite(pb2) & (mub2 > 0) & (pb2 > 0)

        mub1, pb1 = mub1[mask1], pb1[mask1]
        mub2, pb2 = mub2[mask2], pb2[mask2]
        idx1 = np.argsort(mub1)
        idx2 = np.argsort(mub2)

        mub1, pb1 = mub1[idx1], pb1[idx1]
        mub2, pb2 = mub2[idx2], pb2[idx2]
        logP1oflogmu1 = interp1d(np.log(mub1), np.log(pb1),kind='linear',bounds_error=False,fill_value=np.inf)
        logP2oflogmu2 = interp1d(np.log(mub2), np.log(pb2),kind='linear',bounds_error=False,fill_value=np.inf)
        
        #logP1oflogmu1 = CubicSpline(np.log(mub1), np.log(pb1),extrapolate=False)
        #logP2oflogmu2 = CubicSpline(np.log(mub2), np.log(pb2),extrapolate=False)

        mu_min = max(np.min(mub1), np.min(mub2))
        mu_max = min(np.max(mub1), np.max(mub2))

        self.mu_common_min = mu_min
        self.mu_common_max = mu_max
        def diff(mu):
            return logP1oflogmu1(np.log(mu)) - logP2oflogmu2(np.log(mu)) 
            
            
        

        mu_grid = np.geomspace(mu_min, mu_max, 500)
        diff_grid = diff(mu_grid)
        #print(mu_grid,diff_grid)
        
        idx = np.where(np.diff(np.sign(diff_grid)) <= -1.9)[0]
        if len(idx) ==0:
            self.check=False
            return None
        #print(idx,np.diff(np.sign(diff_grid)),mu_grid[idx])
        roots=[]

        try:
            roots = [brentq(diff, mu_grid[i], mu_grid[i + 1],xtol=1e-15) for i in idx]
        except ValueError:
                    pass

        """
        for i in range(len(mu_grid) - 1):
            if diff(mu_grid[i]) * diff(mu_grid[i+1]) < 0: # and len(roots)==0:
                try:
                    root = brentq(diff, mu_grid[i], mu_grid[i+1])
                    roots.append(root)
                except ValueError:
                    pass
        """
        
        roots = np.unique(np.round(roots, decimals=6))
        #print("crossing found at", roots)         
        
        
        
        
        if len(roots) == 0:
            
            self.check=False
            self.mu_c=None
            self.P_c=None
                       
            return None
            ##print("No intersection found.")
        elif  len(roots)==1:
            mu0=roots[0]
            self.mu_c=mu0
            self.P_c1=np.exp(logP1oflogmu1(np.log(mu0)))
            self.P_c2=np.exp(logP2oflogmu2(np.log(mu0))) 
            self.P_c = self.P_c1
            #print(self.P_c1,self.P_c2)
            self.check=True
            return 1
        else:
            if len(roots)>1:
                print("Multiple intersection found after which P_H(mu_H) < P_Q(mu_Q) , Considering the first one")
            mu0=roots[0]
            self.mu_c=mu0
            self.P_c1=np.exp(logP1oflogmu1(np.log(mu0)))
            self.P_c2=np.exp(logP2oflogmu2(np.log(mu0))) 
            self.P_c = self.P_c1
            self.check=True
            return 1 #self.mu_c, self.P_c,self.P_c2
  






class MixedInterpolatePhase:
    """
    Construct a polynomial mixed phase between two EoS regions.

    Each region must provide:
        pres : pressure
        mub  : baryon chemical potential

    It should also provide either:
        nb   : baryon number density
    or:
        eps  : energy density, allowing nb = (eps + pres) / mub

    All quantities must use consistent units.
    """

    def __init__(self, regions,muc=None,Pc=None):
        self.check_MIM=False

        if not isinstance(regions, dict):
            raise TypeError("regions must be a dictionary.")

        required_regions = {"r1", "r2"}
        missing_regions = required_regions - regions.keys()

        if missing_regions:
            raise ValueError(
                f"Missing region(s): {', '.join(sorted(missing_regions))}"
            )

        self.regions = {}

        for region in required_regions:

            if not isinstance(regions[region], dict):
                raise TypeError(
                    f"'{region}' must contain a dictionary."
                )

            values = regions[region]

            required_keys = {"pre", "mub"}
            missing_keys = required_keys - values.keys()

            if missing_keys:
                raise ValueError(
                    f"Missing key(s) in '{region}': "
                    f"{', '.join(sorted(missing_keys))}"
                )

            pre = np.asarray(values["pre"], dtype=float)
            mub = np.asarray(values["mub"], dtype=float)

            if pre.ndim != 1 or mub.ndim != 1:
                raise ValueError(
                    f"Pressure and mub in '{region}' must be 1D arrays."
                )

            if pre.size != mub.size:
                raise ValueError(
                    f"Pressure and mub in '{region}' must have the same length."
                )

            if pre.size < 2:
                raise ValueError(
                    f"'{region}' requires at least two data points."
                )

            if not np.all(np.isfinite(pre)) or not np.all(np.isfinite(mub)):
                raise ValueError(
                    f"'{region}' contains non-finite pressure or mub values."
                )

            if np.any(pre <= 0) or np.any(mub <= 0):
                raise ValueError(
                    f"'{region}' requires positive pressure and mub "
                    "for log-log interpolation."
                )

            # Obtain baryon density.
            if "den" in values:

                den = np.asarray(values["den"], dtype=float)

                if den.ndim != 1 or den.size != pre.size:
                    raise ValueError(    f"'den' in '{region}' must be a 1D array,with the same length as 'pres'." )

            elif "eps" in values:

                eps = np.asarray(values["eps"], dtype=float)

                if eps.ndim != 1 or eps.size != pre.size:
                    raise ValueError(f"'eps' in '{region}' must be a 1D array with the same length as 'pres'.")

                # Thermodynamic relation: mu_B = (eps + P) / nb
                den = (eps + pre) / mub

            else:
                spline = CubicSpline(np.log(mub),np.log(pre),extrapolate=False,)
                den = (pre / mub) * spline.derivative()(np.log(mub))



            if (not np.all(np.isfinite(den)) or np.any(den <= 0) ):
                raise ValueError(f"'den' in '{region}' must contain finite positive values.")

            # Sort by chemical potential.
            order = np.argsort(mub)

            mub = mub[order]
            pre = pre[order]
            den = den[order]

            if np.any(np.diff(mub) <= 0):
                raise ValueError(f"'mub' in '{region}' must contain unique values." )

            # Store the region data.
            self.regions[region] = {
                "pre": pre.copy(),
                "mub": mub.copy(),
                "den": den.copy(),
            }

            setattr(self, f"pre_{region}", pre.copy())
            setattr(self, f"mub_{region}", mub.copy())
            setattr(self, f"den_{region}", den.copy())

            # Log-log cubic spline: nb(mub).
            self.regions[region]["nb_spline"] = CubicSpline(np.log(mub),np.log(den), extrapolate=False)
            self.regions[region]["pre_spline"] = CubicSpline(np.log(mub),np.log(pre), extrapolate=False)
            
        self.muc = muc
        self.Pc = Pc

        # Allowed chemical-potential interval
        self.mu_min = np.min(self.regions["r1"]["mub"])
        self.mu_max = np.max(self.regions["r2"]["mub"])

        # Pressure limits
        self.P_min = np.min(self.regions["r1"]["pre"])
        self.P_max = np.max(self.regions["r2"]["pre"])

        # Pressure on the straight line at mu_c
        self.P_line_c = self.P_min + ((self.P_max - self.P_min)/ (self.mu_max - self.mu_min)) * (self.muc - self.mu_min)
        self.DeltaP_max_geom = max(0.0, (self.P_line_c - self.Pc) / self.Pc)
        if self.DeltaP_max_geom <=0.:
            
            return None
        #print(self.Pc,self.DeltaP_max_geom)

        


    def den_from_mub(self, region, mub):
        """Return baryon density at the specified chemical potential."""

        values = self.regions[region]
        mub_data = values["mub"]

        if not mub_data[0] <= mub <= mub_data[-1]:
            return np.inf
            #raise ValueError(f"mub={mub} lies outside the interpolation range")

        return np.exp(values["nb_spline"](np.log(mub)))

    def pressure_from_mub(self, region, mub):
        """Interpolate pressure as a function of chemical potential."""

        values = self.regions[region]
        mub_data = values["mub"]

        if not mub_data[0] <= mub <= mub_data[-1]:
            return np.inf
            #raise ValueError(f"mub={mub} lies outside the interpolation range")

        return np.exp(values["pre_spline"](np.log(mub)))
        
        
        
        
        
    def Pre_MIM_den_MIM_and_eps_MIM(self,mu_evaluate,alpha1,alpha2):
        
        pre = alpha2 * (mu_evaluate- self.muc)**2+ alpha1 * ((mu_evaluate - self.muc))+ self.PM0

        
        den = 2.0 * alpha2 * ((mu_evaluate - self.muc))+ alpha1
        
        eps= (mu_evaluate *den - pre )
        #print(mu_evaluate,muc,alpha1,alpha2,PM0,pre,eps,den)
        return  den, pre, eps
        

    def find_boundaries(self, x_deltaP=0.0,muH_guess=None, muQ_guess=None):
        """
        Solve the four mixed-phase matching equations.

        Unknowns:
            mu_H, mu_Q, alpha_1, alpha_2

        DeltaP is dimensionless, with Delta P = Delta p * Pc.
        """

        if self.Pc <= 0 or self.muc <= 0:
            raise ValueError("Pc and muc must be positive.")

                   
            
        
        
        DeltaP= x_deltaP * self.DeltaP_max_geom

        PM0 = (1.0 + DeltaP) * self.Pc
        self.PM0= PM0
        
        #print(DeltaP)
        
        

        def equations(x):

            muH, muQ, alpha1, alpha2 = x

            PM_H = (alpha2 * (muH - self.muc)**2+ alpha1 * (muH - self.muc)+ PM0)

            PM_Q = (alpha2 * (muQ - self.muc)**2+ alpha1 * (muQ - self.muc)+ PM0)

            nM_H = 2.0 * alpha2 * (muH - self.muc) + alpha1
            nM_Q = 2.0 * alpha2 * (muQ - self.muc) + alpha1

            PH = self.pressure_from_mub("r1", muH)
            PQ = self.pressure_from_mub("r2", muQ)

            nH = self.den_from_mub("r1", muH)
            nQ = self.den_from_mub("r2", muQ)

            return [PH - PM_H, PQ - PM_Q,nH - nM_H,nQ - nM_Q]

        #solution = root(equations,[muH_guess, muQ_guess, 0.0, 0.0])
        
        
        # Chemical-potential bounds
        muH_min = self.mub_r1.min()
        muQ_max = self.mub_r2.max()

        lower_bounds = [muH_min, self.muc, -np.inf, -np.inf]
        upper_bounds = [self.muc, muQ_max, np.inf, np.inf]

        # Initial guesses must lie within the bounds
        muH_guess = 0.5 * (muH_min + self.muc)
        muQ_guess = 0.5 * (self.muc + muQ_max)

        x0 = [muH_guess, muQ_guess, 0.0, 0.0]
        
        try:
            solution = least_squares( equations,x0=x0,bounds=(lower_bounds, upper_bounds),xtol=1e-13,ftol=1e-13, gtol=1e-15,  max_nfev=10000, )
        except:
            return None

        if not solution.success:
            self.check_MIM=False
            return None
            #raise RuntimeError(f"Mixed-phase solver failed: {solution.message}")
            
            
        
        muH, muQ, alpha1, alpha2 = solution.x
        
        #solution = root(equations,[muH, muQ, alpha1, alpha2]) ## Sometimes, the least square does not work effectively
        
        #if not solution.success:
            #self.check_MIM=False
            #return None

        

        muH, muQ, alpha1, alpha2 = solution.x

        if not muH < self.muc < muQ:
            self.check_MIM=False
            return None
            #raise ValueError("The solution does not satisfy mu_H < muc < mu_Q." )

        residuals = equations(solution.x)

        if not np.all(np.isfinite(residuals)):
            self.check_MIM=False
            return None
            #raise RuntimeError("Non-finite residuals in the solution.")
            
        nM_H = 2.0 * alpha2 * (muH - self.muc) + alpha1
        nM_Q = 2.0 * alpha2 * (muQ - self.muc) + alpha1
        PM_H = (alpha2 * (muH - self.muc)**2+ alpha1 * (muH - self.muc)+ PM0)

        PM_Q = (alpha2 * (muQ - self.muc)**2+ alpha1 * (muQ - self.muc)+ PM0)
        self.check_MIM=True


        return {
            "mu_H": muH,
            "mu_Q": muQ,
            "alpha1": alpha1,
            "alpha2": alpha2,
            "P_H": self.pressure_from_mub("r1", muH),
            "P_Q": self.pressure_from_mub("r2", muQ),
            "n_H": self.den_from_mub("r1", muH),
            "n_Q": self.den_from_mub("r2", muQ),
            "nM_Q": nM_Q,
            "nM_H": nM_H,
            "PM_Q": PM_Q,
            "PM_H":PM_H,            
            "residuals": np.asarray(residuals),
        }





class HyperbolicInterpolatePhase:

    def __init__(self, regions, n1, n2, N=501):

        self.n1, self.n2 = n1, n2
        self.nbar = 0.5 * (n1 + n2)
        self.Gamma = 0.5 * (n2 - n1)

        for key in ("r1", "r2"):

            r = regions[key]

            den = np.asarray(r["den"], dtype=float)
            pre = np.asarray(r["pre"], dtype=float)
            eps = np.asarray(r["eps"], dtype=float)

            idx = np.argsort(den)
            den, pre, eps = den[idx], pre[idx], eps[idx]

            if np.any(den <= 0) or np.any(pre <= 0) or np.any(eps <= 0):
                raise ValueError(
                    f"{key}: den, pre, and eps must be positive."
                )

            setattr(
                self, f"pre_{key}",
                PchipInterpolator(np.log(den), np.log(pre))
            )
            setattr(
                self, f"eps_{key}",
                PchipInterpolator(np.log(den), np.log(eps))
            )

            setattr(self, f"den_range_{key}", (den[0], den[-1]))

        for key in ("r1", "r2"):
            lo, hi = getattr(self, f"den_range_{key}")
            if n1 < lo or n2 > hi:
                raise ValueError(
                    f"{key} does not cover the density interval [{n1}, {n2}]."
                )

        if N < 3 or N % 2 == 0:
            raise ValueError("N must be odd and >= 3.")

        self.den = np.linspace(n1, n2, N)

    def construct(self):

        den = self.den
        x = (den - self.nbar) / self.Gamma

        # Pure-phase EoSs
        pre_H = np.exp(self.pre_r1(np.log(den)))
        pre_Q = np.exp(self.pre_r2(np.log(den)))

        eps_H = np.exp(self.eps_r1(np.log(den)))
        eps_Q = np.exp(self.eps_r2(np.log(den)))

        # Boundary checks
        pre_1, pre_2 = pre_H[0], pre_Q[-1]
        eps_1, eps_2 = eps_H[0], eps_Q[-1]

        mu_1 = (eps_1 + pre_1) / self.n1
        mu_2 = (eps_2 + pre_2) / self.n2

        if not (pre_1 < pre_2  and eps_1 < eps_2 and mu_1 < mu_2):
            return None

        # Hyperbolic interpolation
        f_plus = 0.5 * (1 + np.tanh(x))
        f_minus = 1 - f_plus

        g = 0.5 / self.Gamma / np.cosh(x)**2

        pre = pre_H * f_minus + pre_Q * f_plus

        # Energy-density correction
        integrand = (eps_H - eps_Q) * g / den

        i = len(den) // 2
        integral = np.zeros_like(den)

        integral[i+1:] = cumulative_trapezoid( integrand[i:], den[i:] )

        integral[:i] = -cumulative_trapezoid( integrand[:i+1][::-1], den[:i+1][::-1] )[::-1]

        eps = eps_H * f_minus + eps_Q * f_plus + den * integral

        # Baryon chemical potential
        mub = (eps + pre) / den

        return {
            "den": den[::10],
            "pre": pre[::10],
            "eps": eps[::10],
            "mub": mub[::10],
            "P_H":pre_H[::10],
            "P_Q":pre_Q[::10],
        }
        
        
        
        
class QM_linear:
    def __init__(self, parameters, den_max=None):
        self.den_H_pt, self.eps_H_pt, self.Pre_pt, self.deltan, self.alpha, self.mu_pt = parameters
        #self.den_sat = cst.nsat
        self.den_max = 20. * nuda.cst.nsat if den_max is None else den_max
        self.check_Qmlinear = False

    def liner_EoS(self):
        self.den_Q_pt = self.den_H_pt + self.deltan
        self.eps_Q_pt = self.den_Q_pt * self.mu_pt - self.Pre_pt
        self.deltaE = self.eps_Q_pt - self.eps_H_pt

        if self.deltaE <= 0. or self.alpha <= 0. or self.deltan < 0. or self.den_max <= self.den_Q_pt:
            return None

        eps_star = self.eps_H_pt + self.deltaE - self.Pre_pt / self.alpha
        self.den_QM = np.linspace(self.den_Q_pt, self.den_max, 100)

        eps1 = self.alpha / (self.alpha + 1.) * eps_star
        eps2 = self.eps_H_pt + self.deltaE - self.alpha / (self.alpha + 1.) * eps_star
        self.eps_QM = eps1 + eps2 * (self.den_QM / self.den_Q_pt)**(self.alpha + 1.)
        self.pre_QM = self.alpha * self.eps_QM - self.alpha * eps_star

        if not np.all(np.isfinite(self.pre_QM)) or np.any(self.pre_QM <= 0.):
            return None
        if not np.all(np.isfinite(self.eps_QM)) or np.any(self.eps_QM <= 0.):
            return None
        if not np.all(np.isfinite(self.den_QM)) or np.any(self.den_QM <= 0.):
            return None

        self.mu_QM = (self.pre_QM + self.eps_QM) / self.den_QM
        self.check_Qmlinear = True
        return self#.den_QM, self.pre_QM, self.eps_QM
        
 


