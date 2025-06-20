import os
import sys
import numpy as np  # 1.15.0
import random

import nucleardatapy as nuda

class setupEsymDen():
    """
    Instantiate the values of Esym and Lsym from the constraint.
    
    :param constraint: name of the model: '2014-IAS', ...
    :type constraint: str.
    :returns: constraint, ref, label, note, Esym, Lsym.
    """
    #
    def __init__( self, constraint = '2014-IAS', Ksym = 0.0 ):
        #
        if nuda.env.verb: print("Enter setupEsymDen()")
        #
        #: Attribute the constraint
        self.constraint = constraint
        if nuda.env.verb: print("constraint:",constraint)
        #
        constraints, constraints_lower = nuda.corr.EsymLsym_constraints()
        #
        if constraint.lower() not in constraints_lower:
            print('The constraint ',constraint,' is not in the list of constraints.')
            print('list of constraints:',constraints)
            print('-- Exit the code --')
            exit()
        #
        el = nuda.corr.setupEsymLsym( constraint = constraint )
        self.ref = el.ref
        self.label = el.label
        self.note = el.note
        self.alpha = el.alpha
        self.plot = False
        #print('Esym:',el.Esym)
        #print('Lsym_min:',el.Lsym_min)
        #print('Lsym_max:',el.Lsym_max)
        #cons.print_outputs( )
        #
        nden = 10
        den = 0.1 + 0.16 * np.arange(nden+1) / float( nden )
        self.esym_den = den
        #
        if el.plot == 'band_y':
            #
            self.plot = True
            #
            e_min = 100.0 * np.ones( (np.size(den)) )
            e_max = -100.0 * np.ones( (np.size(den)) )
            for i,Esym in enumerate(el.Esym):
                for j,Lsym in enumerate(el.Lsym_min):
                    esym = Esym + Lsym*(den-nuda.cst.nsat)/(3*nuda.cst.nsat) + 0.5*Ksym*(den-nuda.cst.nsat)**2/(3*nuda.cst.nsat)**2
                    for k,vden in enumerate(den):
                        if esym[k] > e_max[k]: 
                            e_max[k] = esym[k]
                        if esym[k] < e_min[k]: 
                            e_min[k] = esym[k]
                for j,Lsym in enumerate(el.Lsym_max):
                    esym = Esym + Lsym*(den-nuda.cst.nsat)/(3*nuda.cst.nsat) + 0.5*Ksym*(den-nuda.cst.nsat)**2/(3*nuda.cst.nsat)**2
                    for k,vden in enumerate(den):
                        if esym[k] > e_max[k]: 
                            e_max[k] = esym[k]
                        if esym[k] < e_min[k]: 
                            e_min[k] = esym[k]
            #: Attribute the minimal symmetry energy 
            self.esym_e2a_min = e_min
            #: Attribute the maximal symmetry energy 
            self.esym_e2a_max = e_max
            #
        elif el.plot == 'band_x':
            #
            self.plot = True
            #
            e_min = 100.0 * np.ones( (np.size(den)) )
            e_max = -100.0 * np.ones( (np.size(den)) )
            for i,Lsym in enumerate(el.Lsym):
                for j,Esym in enumerate(el.Esym_min):
                    esym = Esym + Lsym*(den-nuda.cst.nsat)/(3*nuda.cst.nsat) + 0.5*Ksym*(den-nuda.cst.nsat)**2/(3*nuda.cst.nsat)**2
                    for k,vden in enumerate(den):
                        if esym[k] > e_max[k]: 
                            e_max[k] = esym[k]
                        if esym[k] < e_min[k]: 
                            e_min[k] = esym[k]
                for j,Esym in enumerate(el.Esym_max):
                    esym = Esym + Lsym*(den-nuda.cst.nsat)/(3*nuda.cst.nsat) + 0.5*Ksym*(den-nuda.cst.nsat)**2/(3*nuda.cst.nsat)**2
                    for k,vden in enumerate(den):
                        if esym[k] > e_max[k]: 
                            e_max[k] = esym[k]
                        if esym[k] < e_min[k]: 
                            e_min[k] = esym[k]
            #: Attribute the minimal symmetry energy 
            self.esym_e2a_min = e_min
            #: Attribute the maximal symmetry energy 
            self.esym_e2a_max = e_max
            #
        elif el.plot == 'point_err_xy':
            #
            self.plot = True
            #
            e_min = 100.0 * np.ones( (np.size(den)) )
            e_max = -100.0 * np.ones( (np.size(den)) )
            Lsyms = [ el.Lsym-el.Lsym_err, el.Lsym, el.Lsym+el.Lsym_err ]
            Esyms = [ el.Esym-el.Esym_err, el.Esym, el.Esym+el.Esym_err ]
            for Esym in Esyms:
                for Lsym in Lsyms:
                    esym = Esym + Lsym*(den-nuda.cst.nsat)/(3*nuda.cst.nsat) + 0.5*Ksym*(den-nuda.cst.nsat)**2/(3*nuda.cst.nsat)**2
                    for k,vden in enumerate(den):
                        if esym[k] > e_max[k]: 
                            e_max[k] = esym[k]
                        if esym[k] < e_min[k]: 
                            e_min[k] = esym[k]
            #: Attribute the minimal symmetry energy 
            self.esym_e2a_min = e_min
            #: Attribute the maximal symmetry energy 
            self.esym_e2a_max = e_max
            #
        else:
            #
            print('No Esyn(n) construction for constraint:',constraint)
            self.esym_den = None
            self.esym_e2a_min = None
            self.esym_e2a_max = None
            #
        #
        if nuda.env.verb: print("Exit setupEsymDen()")
    #
    def print_outputs( self ):
        """
        Method which print outputs on terminal's screen.
        """
        print("")
        #
        if nuda.env.verb: print("Enter print_outputs()")
        #
        print("   constraint:",self.constraint)
        print("   ref:",self.ref)
        print("   label:",self.label)
        print("   note:",self.note)
        print("   plot:",self.plot)
        print("   den: ",np.round(self.esym_den,2))
        print("   max: ",np.round(self.esym_e2a_max,2))
        print("   min: ",np.round(self.esym_e2a_min,2))
        #
        if nuda.env.verb: print("Exit print_outputs()")
        #