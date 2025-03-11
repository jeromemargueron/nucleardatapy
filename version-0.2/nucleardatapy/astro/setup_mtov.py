import math
import numpy as np  # 1.15.0
from scipy import special

import nucleardatapy as nuda

def compute_proba_do( amass, mass_cen, sig_up, sig_lo ):
    fac = math.sqrt( 2.0 )
    prob = []
    for m in amass:
        if m < mass_cen: 
            z = ( m - mass_cen ) / sig_lo / fac
            norm = sig_lo * fac
        else:
            z = ( m - mass_cen ) / sig_up / fac
            norm = sig_up * fac
        prob.append( 0.5 * ( special.erf(z)+1) )
    return prob

def compute_proba_up( amass, mass_cen, sig_up, sig_lo ):
    fac = math.sqrt( 2.0 )
    prob = []
    for m in amass:
        if m < mass_cen: 
            z = ( m - mass_cen ) / sig_lo / fac
            norm = sig_lo * fac
        else:
            z = ( m - mass_cen ) / sig_up / fac
            norm = sig_up * fac
        prob.append( 0.5 * ( 1-special.erf(z)) )
    return prob

class setupMtov():
    """
    Instantiate the observational mass for a given source and obs.

    This choice is defined in the variable `source`.

    `source` can chosen among the following ones: 'J1614–2230'.

    :param source: Fix the name of `source`. Default value: 'J1614–2230'.
    :type source: str, optional. 

    **Attributes:**
    """
    def __init__(self, sources_lo = np.array(['J1614–2230']), sources_up = np.array([ 'GW170817' ]) ):
        #
        if nuda.env.verb: print("Enter setupMtov()")
        #
        # lower bound from neutron star mass observation
        #
        self.sources_lo = sources_lo
        self.sources_up = sources_up
        if nuda.env.verb: print("sources_lo:",sources_lo)
        if nuda.env.verb: print("sources_up:",sources_up)
        #
        # construct the distribution of masses:
        self.mass = np.linspace(1.5,3.5,300)
        #
        nsources = len(sources_lo)
        self.proba_lo = np.zeros((nsources,300))
        self.proba_lo_tot = np.ones(300)
        self.label_lo = []
        #
        for ind,source in enumerate(sources_lo):
            #print('Call average for source:', source)
            avmass = nuda.setupMassesAverage( source = source )
            #print('End of call average')
            #avmass.print_outputs( )
            #print('source:',source,' mass:',avmass.mass_cen,' sig_std:',avmass.sig_std )
            self.proba_lo[ind] = compute_proba_do(self.mass, avmass.mass_cen, avmass.sig_std, avmass.sig_std)
            self.label_lo.append( str(source) )
            #print('proba:',self.proba[ind])
            self.proba_lo_tot = self.proba_lo_tot * self.proba_lo[ind]
            #
        self.label_lo_tot = 'Lower boundary'
        #
        # upper bound from GW observation
        #
        #sources_up = nuda.astro_mup( )[0]
        #print('Complete list of available sources_up:',sources_up)
        #
        #sources_up = [ 'GW170817', 'GW190814' ]
        #
        #print('sources_up considered:',sources_up)
        #
        nsources = len(sources_up)
        self.proba_up = np.zeros((nsources,300))
        self.proba_up_tot = np.ones(300)
        self.label_up = []
        #
        for ind,source in enumerate(sources_up):
            print('Call average for source:', source)
            hyps = nuda.astro.mup_hyps( source = source )
            if source=='GW170817': hyps = [ 3, 4 ]
            print('   hyps:',hyps)
            avmup = nuda.setupMupAverage( source = source, hyps = hyps )
            #print('End of call average')
            #avmup.print_outputs( )
            self.proba_up[ind] = compute_proba_up(self.mass, avmup.mup_cen, avmup.sig_std, avmup.sig_std)
            self.label_up.append( str(source) )
            self.proba_up_tot = self.proba_up_tot * self.proba_up[ind]
            #
        self.label_up_tot = 'Upper boundary'
        #
        self.proba_tot = self.proba_lo_tot * self.proba_up_tot
        self.label_tot = 'Total'
        #
        if nuda.env.verb: print("Exit SetupAstroMtov()")
        #
    #
    def print_output( self ):
        """
        Method which print outputs on terminal's screen.
        """
        print("")
        #
        if nuda.env.verb: print("Enter print_output()")
        #
        print("- Print output:")
        print("   sources_lo:  ",self.sources_lo)
        print("   sources_up:  ",self.sources_up)
        print("   mass:",self.mass)
        print("   proba_tot:",self.proba_tot)
        #
        if nuda.env.verb: print("Exit print_output()")
        #
    #
    def print_latex( self ):
        """
        Method which print outputs in table format (latex) on terminal's screen.
        """
        #
        if nuda.env.verb: print("Enter print_latex()")
        #
        if nuda.env.verb_latex:
            print(rf"- table: {self.sources_lo} & {self.sources_up} \\\\")
        else:
            print(rf"- No  table for sources {self.sources_lo} and {self.sources_up}. To get  table, write  'verb_latex = True' in env.py.")
        #
        if nuda.env.verb: print("Exit print_latex()")
        #
       