import os
import sys
import math
import numpy as np  # 1.15.0

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def astro_mr():
    """
    Return a list of the astrophysical sources for which a mass is given

    :return: The list of sources.
    :rtype: list[str].
    """
    #
    if nuda.env.verb: print("\nEnter astro_mr()")
    #
    sources = [ 'J0030+0451', 'J0740+6620' ]
    #
    #print('sources available in the toolkit:',sources)
    sources_lower = [ item.lower() for item in sources ]
    #print('sources available in the toolkit:',sources_lower)
    #
    if nuda.env.verb: print("Exit astro_mr()")
    #
    return sources, sources_lower

def astro_mr_source( source ):
    """
    Return a list of observations for a given source and print them all on the prompt.

    :param source: The source for which there are different observations.
    :type source: str.
    :return: The list of observations. \
    If source == 'J1614–2230': 1, 2, 3, 4, 5.
    :rtype: list[str].
    """
    #
    if nuda.env.verb: print("\nEnter astro_mr_source()")
    #
    if source.lower()=='j0030+0451':
        obss = [ 1, 2 ]
    elif source.lower()=='j0740+6620':
        obss = [ 1, 2 ]
    #
    #print('Observations available in the toolkit:',obss)
    #
    if nuda.env.verb: print("Exit astro_mr_source()")
    #
    return obss

class SetupAstroMR():
    """
    Instantiate the observational mass for a given source and obs.

    This choice is defined in the variables `source` and `obs`.

    `source` can chosen among the following ones: 'J1614–2230'.

    `obs` depends on the chosen source.

    :param source: Fix the name of `source`. Default value: 'J1614–2230'.
    :type source: str, optional. 
    :param obs: Fix the `obs`. Default value: 1.
    :type obs: str, optional. 

    **Attributes:**
    """
    def __init__(self, source = 'J0030+0451', obs = 1 ):
        #
        if nuda.env.verb: print("Enter SetupAstroMR()")
        #
        sources, sources_lower = astro_mr()
        if source.lower() not in sources_lower:
            print('Source ',source,' is not in the list of sources.')
            print('list of sources:',sources)
            print('-- Exit the code --')
            exit()
        self.source = source
        if nuda.env.verb: print("source:",source)
        #
        obss = astro_mr_source( source = source )
        if obs not in obss:
            print('Obs ',obs,' is not in the list of obs.')
            print('list of obs:',obss)
            print('-- Exit the code --')
            exit()
        self.obs = obs
        if nuda.env.verb: print("obs:",obs)
        #
        if source.lower()=='j0030+0451':
            file_in = nuda.param.path_data+'astro/NICER/J0030+0451.dat'
            if obs==1:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='M.C. Miller, F.K. Lamb, A.J. Dittmann, aet al., ApJL 887, L24 (2019).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'J0030 Miller 2019'
                #: Attribute providing additional notes about the observation.
                self.note = "write here notes about this observation."
            elif obs==2:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='T.E. Riley, A.L. Watts, S. Bogdanov, P.S. Ray, et al., ApJ 887, L21 (2019).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'J0030 Riley 2019'
                #: Attribute providing additional notes about the observation.
                self.note = "write here notes about this observation."
        elif source.lower()=='j0740+6620':
            file_in = nuda.param.path_data+'astro/NICER/J0740+6620.dat'
            if obs==1:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='M.C. Miller, F.K. Lamb, A.J. Dittmann, S. Bogdanov, et al., ApJL 918, L28 (2021).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'J0740 Miller 2021'
                #: Attribute providing additional notes about the observation.
                self.note = "write here notes about this observation."
            elif obs==2:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='T.E. Riley, A.L. Watts, P.S. Ray, S. Bogdanov, et al., ApJL 918, L27 (2021).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'J0740 Riley 2021'
                #: Attribute providing additional notes about the observation.
                self.note = "write here notes about this observation."
        #
        #: Attribute the observational mass of the source.
        self.mass = None
        #: Attribute the positive uncertainty.
        self.mass_sig_up = None
        #: Attribute the negative uncertainty.
        self.mass_sig_do = None
        #: Attribute the observational mass of the source.
        self.rad = None
        #: Attribute the positive uncertainty.
        self.rad_sig_up = None
        #: Attribute the negative uncertainty.
        self.rad_sig_do = None
        #: Attribute latexCite.
        self.latexCite = None
        #
        with open(file_in,'r') as file:
            for line in file:
                if '#' in line: continue
                ele = line.split(',')
                #print('ele[0]:',ele[0],' obs:',obs,' ele[:]:',ele[:])
                if int(ele[0]) == obs:
                    self.mass = float(ele[1])
                    self.mass_sig_up = float(ele[2])
                    self.mass_sig_do = float(ele[3])
                    self.rad = float(ele[4])
                    self.rad_sig_up = float(ele[5])
                    self.rad_sig_do = float(ele[6])
                    self.latexCite = ele[10].replace('\n','').replace(' ','')
        #
        if nuda.env.verb: print("Exit SetupAstroMR()")
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
       print("   obs:",self.obs)
       print("   mass:",self.mass)
       print("   sigma(mass):",self.mass_sig_up,self.mass_sig_do)
       print("   rad:",self.rad)
       print("   sigma(mass):",self.rad_sig_up,self.rad_sig_do)
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

class SetupAstroMRAverage():
    """
    Instantiate the observational mass for a given source and averaged over obs.

    This choice is defined in the variable `source`.

    `source` can chosen among the following ones: 'J1614–2230'.

    :param source: Fix the name of `source`. Default value: 'J1614–2230'.
    :type source: str, optional. 

    **Attributes:**
    """
    def __init__(self, source = 'J1614–2230' ):
        #
        if nuda.env.verb: print("Enter SetupAstroMRAverage()")
        #
        self.source = source
        self.latexCite = None
        self.ref = None
        self.label = source+' average'
        self.note = 'compute the centroid and standard deviation from the obs. data.'
        #
        obss = astro_mr_source( source = source )
        #print('obss:',obss)
        #
        # search for the boundary for the masses:
        mmin = 3.0; mmax = 0.0;
        for obs in obss:
            mass = nuda.SetupAstroMR( source = source, obs = obs )
            #mass.print_outputs( )
            mdo = mass.mass - 3*mass.sig_do
            mup = mass.mass + 3*mass.sig_up
            if mdo < mmin: mmin = mdo
            if mup > mmax: mmax = mup
        #print('mmin:',mmin)
        #print('mmax:',mmax)
        # construct the distribution of observations in ay
        ax = np.linspace(mmin,mmax,300)
        #print('ax:',ax)
        ay = np.zeros(300)
        for obs in obss:
            mass = nuda.SetupAstroMR( source = source, obs = obs )
            #mass.print_outputs( )
            ay += gauss(ax,mass.mass,mass.sig_up,mass.sig_do)
        # determine the centroid and standard deviation from the distribution of obs. 
        nor = sum( ay )
        cen = sum( ay*ax )
        std = sum ( ay*ax**2 )
        self.mass_cen = cen / nor
        self.sig_std = round( math.sqrt( std/nor - self.mass_cen**2 ), 3 )
        self.mass_cen = round( self.mass_cen, 3)
        #print('mass:',self.mass_cen)
        #print('std:',self.sig_std)
        #
        if nuda.env.verb: print("Exit SetupAstroMRAverage()")
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
       print("   mass_cen:",self.mass_cen)
       print("   mass_sig_std:",self.mass_sig_std)
       print("   rad_cen:",self.rad_cen)
       print("   rad_sig_std:",self.rad_sig_std)
       print("   latexCite:",self.latexCite)
       print("   ref:    ",self.ref)
       print("   label:  ",self.label)
       print("   note:   ",self.note)
       #
       if nuda.env.verb: print("Exit print_outputs()")
       #

