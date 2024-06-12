import os
import sys
import numpy as np  # 1.15.0

import nucleardatapy as nudy

def kfn( den_n ):
	return (3*nudy.cst.pi2*den_n)**nudy.cst.third

def density( kfn ):
    return kfn**nudy.cst.three / ( nudy.cst.three * nudy.cst.pi2 )

def ef( kfn ):
    return nudy.cst.half * nudy.cst.h2m * kfn**2

def effg( kfn ):
    return nudy.cst.t2f * nudy.cst.half * nudy.cst.h2m * kfn**2

