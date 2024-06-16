import os
import sys
import numpy as np

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nudy

def print_outputs_micro(obj):
    """
    Print outputs on terminal's screen.
    """
    print("")
    #
    if nudy.env.verb: print("Enter print_outputs_micro()")
    #
    print("- Print output:")
    print("   model:",obj.model)
    print("   ref:",obj.ref)
    print("   label:",obj.label)
    print("   note:",obj.note)
    if any(obj.sm_den): print(f"   sm_den: {np.round(obj.sm_den,2)} in {obj.den_unit}")
    if any(obj.sm_kfn): print(f"   sm_kfn: {np.round(obj.sm_kfn,2)} in {obj.kfn_unit}")
    if any(obj.sm_e2a): print(f"   sm_e2a: {np.round(obj.sm_e2a,2)} in {obj.e2a_unit}")
    if any(obj.sm_e2a_err): print(f"   sm_e2a_err: {np.round(obj.sm_e2a_err,2)} in {obj.e2a_unit}")
    if any(obj.nm_den): print(f"   nm_den: {np.round(obj.nm_den,2)} in {obj.den_unit}")
    if any(obj.nm_kfn): print(f"   nm_kfn: {np.round(obj.nm_kfn,2)} in {obj.kfn_unit}")
    if any(obj.nm_e2a): print(f"   nm_e2a: {np.round(obj.nm_e2a,2)} in {obj.e2a_unit}")
    if any(obj.nm_e2a_err): print(f"   nm_e2a_err: {np.round(obj.nm_e2a_err,2)} in {obj.e2a_unit}")
    if any(obj.nm_gap): print(f"   nm_gap: {np.round(obj.nm_gap,2)} in {obj.gap_unit}")
    #
    if nudy.env.verb: print("Exit print_outputs_micro()")
    #

def print_outputs_pheno(obj):
    """
    Print outputs on terminal's screen.
    """
    print("")
    #
    if nudy.env.verb: print("Enter print_outputs_pheno()")
    #
    print("- Print output:")
    print("   model:",obj.model)
    print("   param:",obj.param)
    #print("   ref:",obj.ref)
    print("   label:",obj.label)
    #print("   note:",obj.note)
    if any(obj.sm_den): print(f"   sm_den: {np.round(obj.sm_den,2)} in {obj.den_unit}")
    if any(obj.sm_kfn): print(f"   sm_kfn: {np.round(obj.sm_kfn,2)} in {obj.kfn_unit}")
    if any(obj.sm_e2a): print(f"   sm_e2a: {np.round(obj.sm_e2a,2)} in {obj.e2a_unit}")
    if any(obj.nm_den): print(f"   nm_den: {np.round(obj.nm_den,2)} in {obj.den_unit}")
    if any(obj.nm_kfn): print(f"   nm_kfn: {np.round(obj.nm_kfn,2)} in {obj.kfn_unit}")
    if any(obj.nm_e2a): print(f"   nm_e2a: {np.round(obj.nm_e2a,2)} in {obj.e2a_unit}")
    if any(obj.nm_gap): print(f"   nm_gap: {np.round(obj.nm_gap,2)} in {obj.gap_unit}")
    #
    if nudy.env.verb: print("Exit print_outputs_pheno()")
    #

def print_outputs_EsymLsym(obj):
    """
    Print outputs on terminal's screen.
    """
    print("")
    #
    if nudy.env.verb: print("Enter print_outputs_EsymLsym()")
    #
    print("   constraint:",obj.constraint)
    print("   ref:",obj.ref)
    print("   label:",obj.label)
    print("   note:",obj.note)
    if obj.Esym.size==1 and obj.Esym_err.size==1 and obj.Lsym_err.size==1: 
        print('errorbar x and y')
    elif any(obj.Esym) and any(obj.Esym_err): 
        print('errorbar x')
    elif any(obj.Esym) and any(obj.Lsym_err): 
        print('errorbar y')
    elif any(obj.Esym): 
        print('plot')
    #
    if nudy.env.verb: print("Exit print_outputs_EsymLsym()")
    #

def print_outputs_isgmr( obj ):
    """
    Print outputs on terminal's screen.
    """
    print("")
    #
    if nudy.env.verb: print("Enter print_outputs_isgmr()")
    #
    print("- Print output:")
    print("   table:",obj.table)
    print("   ref:",obj.ref)
    print("   label:",obj.label)
    print("   note:",obj.note)
    if any(obj.Z): print(f"   Z: {obj.Z}")
    if any(obj.A): print(f"   A: {obj.A}")
    if any(obj.E_cen): print(f"   E: {obj.E_cen}")
    if any(obj.E_errp): print(f"   E_errp: {obj.E_errp}")
    if any(obj.E_errm): print(f"   E_errm: {obj.E_errm}")
    #
    if nudy.env.verb: print("Exit print_outputs_isgmr()")
    #

