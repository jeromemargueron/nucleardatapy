import numpy as np
import os, sys
from scipy.interpolate import CubicSpline
import fderiv as fd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

nsat = 0.16
mnuc2 = 939.0
nesym = 20

def uncertainty_stat(den):
    return 0.07*(den/nsat)


def APR():
    file_in1 = os.path.join(nuda.param.path_data,'eos/micro/1998-VAR-NM-APR.dat')
    file_in2 = os.path.join(nuda.param.path_data,'eos/micro/1998-VAR-SM-APR.dat')
    if nuda.env.verb: print('Reads file:',file_in1)
    if nuda.env.verb: print('Reads file:',file_in2)
    ref = 'Akmal, Pandharipande and Ravenhall, Phys. Rev. C 58, 1804 (1998)'
    note = "write here notes about this EOS."
    label = 'APR-1998'
    linestyle = 'solid'
    nm_den, nm_e2a = np.loadtxt( file_in1, usecols=(0,1), unpack = True )
    sm_den, sm_e2a = np.loadtxt( file_in2, usecols=(0,1), unpack = True )
    nm_den_min = min( nm_den ); nm_den_max = max( nm_den )
    sm_den_min = min( sm_den ); sm_den_max = max( sm_den )
    nm_e2v = nm_e2a * nm_den
    sm_e2v = sm_e2a * sm_den
    nm_kfn = nuda.kf_n( nm_den )
    sm_kfn = nuda.kf_n( nuda.cst.half * sm_den )
    nm_e2a_err = np.abs( uncertainty_stat(nm_den) * nm_e2a )
    sm_e2a_err = np.abs( uncertainty_stat(sm_den) * sm_e2a )
    #
    # pressure in NM
    x = np.insert( nm_den, 0, 0.0 )
    y = np.insert( nm_e2a, 0, 0.0 )
    cs_nm_e2a = CubicSpline( x, y )
    y_err = np.insert( nm_e2a_err, 0, 0.0 )
    cs_nm_e2a_err = CubicSpline( x, y_err )
    nm_interp = interp1d(nm_den, nm_e2a, kind="cubic")
    nm_pre = nm_den**2 * cs_nm_e2a( nm_den, 1 )
    den_array = np.linspace(0.02, 0.96)
    nm_e2v_fd = nm_interp(den_array) * den_array
    nm_e2a_fd, nm_e2a_fdd = fd.fderiv(den_array, nm_interp(den_array))
    nm_pre_fd = den_array**2* nm_e2a_fd
    nm_pre_np = np.gradient(np.gradient(nm_e2a, nm_den), nm_den)
    print(nm_pre_fd, nm_pre_np)
    #y_err = np.insert( nm_e2a_err, 0, 0.0 )
    #cs_nm_e2a_err = CubicSpline( x, y_err )
    #nm_pre_err = nm_den**2 * cs_nm_e2a_err( nm_den, 1 )
    # pressure in SM
    x = np.insert( sm_den, 0, 0.0 )
    y = np.insert( sm_e2a, 0, 0.0 )
    cs_sm_e2a = CubicSpline( x, y )
    y_err = np.insert( sm_e2a_err, 0, 0.0 )
    cs_sm_e2a_err = CubicSpline( x, y_err )
    sm_pre = sm_den**2 * cs_sm_e2a( sm_den, 1 )
    sm_pre_fd, sm_pre_fdd = sm_den**2*fd.fderiv(sm_den, sm_e2a) 
    #y_err = np.insert( sm_e2a_err, 0, 0.0 )
    #cs_sm_e2a_err = CubicSpline( x, y_err )
    #sm_pre_err = sm_den**2 * cs_sm_e2a_err( sm_den, 1 )
    #
    # Symmetry energy
    esym_den_min = max( min( nm_den), min( sm_den) )
    esym_den_max = min( max( nm_den), max( sm_den) )
    esym_kf_min = nuda.kf( esym_den_min )
    esym_kf_max = nuda.kf( esym_den_max )
    #print('den_min:',den_min,' den_max:',den_max)
    #print('kf_min:',kf_min,' kf_max:',kf_max)
    kf_step = ( esym_kf_max - esym_kf_min ) / float( nesym )
    esym_kf = esym_kf_min + np.arange(nesym+1) * kf_step
    esym_den = nuda.den( esym_kf )
    #print('kf:',esym_kf)
    #print('den:',esym_den)
    esym_e2a = cs_nm_e2a( esym_den ) - cs_sm_e2a( esym_den )
    esym_e2a_err = np.sqrt( cs_nm_e2a_err( 2**nuda.cst.third * esym_kf )**2 + \
        cs_sm_e2a_err( esym_kf )**2 )
    #print('esym:',esym_e2a)
    #
    # chemical potential
    nm_chempot = ( np.array(nm_pre) + np.array(nm_e2v) ) / np.array(nm_den)
    #nm_chempot_err = ( np.array(nm_pre_err) + np.array(nm_e2v_err) ) / np.array(nm_den)
    sm_chempot = ( np.array(sm_pre) + np.array(sm_e2v) ) / np.array(sm_den)
    #sm_chempot_err = ( np.array(sm_pre_err) + np.array(sm_e2v_err) ) / np.array(nm_den)
    #
    # Speed of sound calculation
    x = np.insert( nm_den, 0, 0.0 )
    y = np.insert( nm_pre, 0, 0.0 )
    cs_nm_pre_e2a = CubicSpline( x, y )
    cs2_nm_CS = cs_nm_pre_e2a(nm_den,1)
    nm_chempot_fd = (nm_pre_fd + nm_e2v_fd)/ den_array
    cs2_nm_fd =  nm_e2a_fdd /(nm_chempot_fd + 939)
    cs2_nm_CS = cs2_nm_CS/(nm_chempot + 939)
    cs2_nm_np = nm_pre_np / (nm_chempot + 939)

    plt.plot(nm_den, cs2_nm_CS, label="CS")
    plt.plot(den_array, cs2_nm_fd, label="fderiv")
    plt.plot(nm_den, cs2_nm_np, label="np")
    plt.ylim(0,1)
    plt.legend()
    plt.show()
    


def main():
    APR()

if __name__=="__main__":
    main()