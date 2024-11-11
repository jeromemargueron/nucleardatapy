import os
import sys
import math
import numpy as np  # 1.15.0

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def astro_mtot():
    """
    Return a list of the astrophysical sources for which a mass is given

    :return: The list of sources.
    :rtype: list[str].
    """
    #
    if nuda.env.verb: print("\nEnter astro_mtot()")
    #
    sources = [ 'GW170817' ]
    #
    #print('sources available in the toolkit:',sources)
    sources_lower = [ item.lower() for item in sources ]
    #print('sources available in the toolkit:',sources_lower)
    #
    if nuda.env.verb: print("Exit astro_mtot()")
    #
    return sources, sources_lower

def astro_mtot_source( source ):
    """
    Return a list of observations for a given source and print them all on the prompt.

    :param source: The source for which there are different observations.
    :type source: str.
    :return: The list of observations. \
    If source == 'J1614–2230': 1, 2, 3, 4, 5.
    :rtype: list[str].
    """
    #
    if nuda.env.verb: print("\nEnter astro_masses_source()")
    #
    if source.lower()=='gw170817':
        hyps = [ 1, 2, 3, 4 ]
        #hyps = [ 'low-spin+TaylorF2', 'high-spin+TaylorF2', 'low-spin+PhenomPNRT', 'high-spin+PhenomPNRT']
    #
    #print('Hypotheses available in the toolkit:',hyps)
    #
    if nuda.env.verb: print("Exit astro_mtot_source()")
    #
    return hyps

class SetupAstroMtot():
    """
    Instantiate the total mass for a given source and hyptheses.

    This choice is defined in the variables `source` and `hyp`.

    `source` can chosen among the following ones: 'GW170817'.

    `hyp` depends on the chosen hypotheses.

    :param source: Fix the name of `source`. Default value: 'GW170817'.
    :type source: str, optional. 
    :param hyp: Fix the `hyp`. Default value: 'low-spin+TaylorF2'.
    :type hyp: str, optional. 

    **Attributes:**
    """
    def __init__(self, source = 'GW170817', hyp = 1 ):
        #
        if nuda.env.verb: print("Enter SetupAstroMtot()")
        #
        sources, sources_lower = astro_mtot()
        if source.lower() not in sources_lower:
            print('Source ',source,' is not in the list of sources.')
            print('list of sources:',sources)
            print('-- Exit the code --')
            exit()
        self.source = source
        if nuda.env.verb: print("source:",source)
        #
        hyps = astro_mtot_source( source = source )
        if hyp not in hyps:
            print('Hyp ',hyp,' is not in the list of hypotheses.')
            print('list of hyp:',hyps)
            print('-- Exit the code --')
            exit()
        self.hyp = hyp
        if nuda.env.verb: print("hyp:",hyp)
        #
        if source.lower()=='gw170817':
            file_in = nuda.param.path_data+'astro/masses/GW170817.dat'
            #if hyp=='low-spin+TaylorF2':
            if hyp == 1:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='B.P. Abbott, R. Abbott, T.D. Abbott, et al., PRL 119, 161101 (2017)'
                #: Attribute providing the label the data is references for figures.
                self.label = 'GW170817 low-spin Abbott 2017'
                #: Attribute providing additional notes about the observation.
                self.note = "write here notes about this observation."
            #elif hyp=='high-spin+TaylorF2':
            elif hyp == 2:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='B.P. Abbott, R. Abbott, T.D. Abbott, et al., PRL 119, 161101 (2017)'
                #: Attribute providing the label the data is references for figures.
                self.label = 'GW170817 high-spin Abbott 2017'
                #: Attribute providing additional notes about the observation.
                self.note = "write here notes about this observation."
            #elif hyp=='low-spin+PhenomPNRT':
            elif hyp == 3:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref=' B.P. Abbott, R. Abbott, T.D. Abbott, F. Acernese, et al., PRX 9, 011001 (2019)'
                #: Attribute providing the label the data is references for figures.
                self.label = 'GW170817 low-spin Abbott 2019'
                #: Attribute providing additional notes about the observation.
                self.note = "write here notes about this observation."
            #elif hyp=='high-spin+PhenomPNRT':
            elif hyp == 4:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref=' B.P. Abbott, R. Abbott, T.D. Abbott, F. Acernese, et al., PRX 9, 011001 (2019)'
                #: Attribute providing the label the data is references for figures.
                self.label = 'GW170817 high-spin Abbott 2019'
                #: Attribute providing additional notes about the observation.
                self.note = "write here notes about this observation."
        #
        #: Attribute the observational mass of the source.
        self.mtot = None
        #: Attribute the positive uncertainty.
        self.sig_up = None
        #: Attribute the negative uncertainty.
        self.sig_do = None
        #: Attribute latexCite.
        self.latexCite = None
        #
        with open(file_in,'r') as file:
            for line in file:
                if '#' in line: continue
                ele = line.split(',')
                #print('ele[0]:',ele[0],' hyp:',str(hyp),' ele[:]:',ele[:])
                #if ele[0].replace("'","") == str(hyp):
                if int(ele[0]) == hyp:
                    self.mtot = float(ele[2])
                    self.sig_up = float(ele[3])
                    self.sig_do = float(ele[4])
                    self.latexCite = ele[5].replace('\n','').replace(' ','')
        #
        if nuda.env.verb: print("Exit SetupAstroMtot()")
        #
    #
    def print_outputs( self ):
       """
       Method which print outputs on terminal's screen.
       """
       print("")
       #
       if nuda.env.verb: print("Enter print_outputs()")
       #
       print("- Print output:")
       print("   source:  ",self.source)
       print("   hyp:",self.hyp)
       print("   mtot:",self.mtot)
       print("   sigma(mtot):",self.sig_up,self.sig_do)
       print("   latexCite:",self.latexCite)
       print("   ref:    ",self.ref)
       print("   label:  ",self.label)
       print("   note:   ",self.note)
       #
       if nuda.env.verb: print("Exit print_outputs()")
       #

def gauss( ax, mass, sig_up, sig_do ):
    fac = math.sqrt( 2*math.pi )
    gauss = []
    for x in ax:
        if x < mass: 
            z = ( x - mass ) / sig_do
            norm = sig_do * fac
        else:
            z = ( x - mass ) / sig_up
            norm = sig_up * fac
        gauss.append( math.exp( -0.5*z**2 ) / norm )
    return gauss

class SetupAstroMtotAverage():
    """
    Instantiate the total mass for a given source and averaged over hypotheses.

    This choice is defined in the variable `source`.

    `source` can chosen among the following ones: 'GW170817'.

    :param source: Fix the name of `source`. Default value: 'GW170817'.
    :type source: str, optional. 

    **Attributes:**
    """
    def __init__(self, source = 'GW170817' ):
        #
        if nuda.env.verb: print("Enter SetupAstroMtotAverage()")
        #
        self.source = source
        self.latexCite = None
        self.ref = None
        self.label = source+' average'
        self.note = 'compute the centroid and standard deviation from the obs. data.'
        #
        hyps = astro_mtot_source( source = source )
        #
        # search for the boundary for mtot:
        mtotmin = 3.0; mtotmax = 0.0;
        for hyp in hyps:
            mtot = nuda.SetupAstroMtot( source = source, hyp = hyp )
            #mtot.print_outputs( )
            mtotdo = mtot.mtot - 3*mtot.sig_do
            mtotup = mtot.mtot + 3*mtot.sig_up
            if mtotdo < mtotmin: mtotmin = mtotdo
            if mtotup > mtotmax: mtotmax = mtotup
        #print('mtotmin:',mtotmin)
        #print('mtotmax:',mtotmax)
        # construct the distribution of observations in ay
        ax = np.linspace(mtotmin,mtotmax,300)
        #print('ax:',ax)
        ay = np.zeros(300)
        for hyp in hyps:
            #print('hyp:',hyp)
            mtot = nuda.SetupAstroMtot( source = source, hyp = hyp )
            #mtot.print_outputs( )
            ay += gauss(ax,mtot.mtot,mtot.sig_up,mtot.sig_do)
        # determine the centroid and standard deviation from the distribution of obs. 
        nor = sum( ay )
        cen = sum( ay*ax )
        std = sum ( ay*ax**2 )
        self.mtot_cen = cen / nor
        self.sig_std = round( math.sqrt( std/nor - self.mtot_cen**2 ), 3 )
        self.mtot_cen = round( self.mtot_cen, 3)
        #print('mtot:',self.mtot_cen)
        #print('std:',self.sig_std)
        #
        if nuda.env.verb: print("Exit SetupAstroMtotAverage()")
    #
    def print_outputs( self ):
       """
       Method which print outputs on terminal's screen.
       """
       print("")
       #
       if nuda.env.verb: print("Enter print_outputs()")
       #
       print("- Print output:")
       print("   source:  ",self.source)
       print("   mtot_cen:",self.mtot_cen)
       print("   sig_std:",self.sig_std)
       print("   latexCite:",self.latexCite)
       print("   ref:    ",self.ref)
       print("   label:  ",self.label)
       print("   note:   ",self.note)
       #
       if nuda.env.verb: print("Exit print_outputs()")
       #

