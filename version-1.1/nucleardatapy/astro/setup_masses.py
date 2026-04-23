import math
import numpy as np  # 1.15.0

import nucleardatapy as nuda

def masses_sources():
    """
    Return a list of the astrophysical sources for which a mass is given

    :return: The list of sources.
    :rtype: list[str].
    """
    #
    if nuda.env.verb: print("\nEnter masses_sources()")
    #
    sources = [ 'J1614–2230', 'J0348+0432', 'J2215+5135', 'J0740+6620', 'J1600+3053' ]
    #
    #print('sources available in the toolkit:',sources)
    sources_lower = [ item.lower() for item in sources ]
    #print('sources available in the toolkit:',sources_lower)
    #
    if nuda.env.verb: print("Exit masses_sources()")
    #
    return sources, sources_lower

def masses_obss( source ):
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
    if source.lower()=='j1614–2230':
        obss = [ 1, 2, 3, 4, 5 ]
    elif source.lower()=='j0348+0432':
        obss = [ 1 ]
    elif source.lower()=='j2215+5135':
        obss = [ 1 ]
    elif source.lower()=='j0740+6620':
        obss = [ 1, 2, 3 ]
    elif source.lower()=='j1600+3053':
        obss = [ 1 ]
    #
    #print('Observations available in the toolkit:',obss)
    #
    if nuda.env.verb: print("Exit masses_obss()")
    #
    return obss

class setupMasses():
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
    def __init__(self, source = 'J1614–2230', obs = 1 ):
        #
        if nuda.env.verb: print("Enter SetupMasses()")
        #
        # some checks
        #
        sources, sources_lower = masses_sources()
        if source.lower() not in sources_lower:
            print('setup_masses.py: Source ',source,' is not in the list of sources.')
            print('setup_masses.py: list of sources:',sources)
            print('setup_masses.py: -- Exit the code --')
            exit()
        self.source = source
        if nuda.env.verb: print("source:",source)
        #
        obss = masses_obss( source = source )
        if obs not in obss:
            print('setup_masses.py: obs ',obs,' is not in the list of obs.')
            print('setup_masses.py: list of obs:',obss)
            print('setup_masses.py: -- Exit the code --')
            exit()
        self.obs = obs
        if nuda.env.verb: print("obs:",obs)
        #
        # fix `file_in` and some properties of the object
        #
        if source.lower()=='j1614–2230':
            file_in = nuda.param.path_data+'astro/masses/J1614–2230.dat'
            if obs==1:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='P. Demorest, T. Pennucci, S. Ransom, M. Roberts, J. Hessels, Nature 467, 1081 (2010)'
                #: Attribute providing the label the data is references for figures.
                self.label = 'J1614–2230 Demorest 2010'
                #: Attribute providing additional notes about the observation.
                self.note = "write here notes about this observation."
                self.marker = 'o'
            elif obs==2:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='E. Fonseca, et al., ApJ 832(2), 167 (2016)'
                #: Attribute providing the label the data is references for figures.
                self.label = 'J1614–2230 Fonseca 2016'
                #: Attribute providing additional notes about the observation.
                self.note = "write here notes about this observation."
                self.marker = 's'
            elif obs==3:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='Z. Arzoumanian, et al., ApJ Suppl. 235(2), 37 (2018)'
                #: Attribute providing the label the data is references for figures.
                self.label = 'J1614–2230 Arzoumanian 2018'
                #: Attribute providing additional notes about the observation.
                self.note = "write here notes about this observation."
                self.marker = 'o'
            elif obs==4:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='M. Alam, Z. Arzoumanian, P. Baker, H. Blumer et al., ApJ Suppl. 252(1) (2021)'
                #: Attribute providing the label the data is references for figures.
                self.label = 'J1614–2230 Alam 2021'
                #: Attribute providing additional notes about the observation.
                self.note = "write here notes about this observation."
                self.marker = 's'
            elif obs==5:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='G. Agazie, M.F. Alam, A. Anumarlapudi, A.M. Archibald et al., ApJ Lett. 951, L9 (2023)'
                #: Attribute providing the label the data is references for figures.
                self.label = 'J1614–2230 Agazie 2023'
                #: Attribute providing additional notes about the observation.
                self.note = "write here notes about this observation."
                self.marker = 'o'
        elif source.lower()=='j0348+0432':
            file_in = nuda.param.path_data+'astro/masses/J0348+0432.dat'
            if obs==1:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='J. Antoniadis, P.C. Freire, N. Wex, T.M. Tauris, et al., Science 340, 6131 (2013)'
                #: Attribute providing the label the data is references for figures.
                self.label = 'J0348+0432 Antoniadis 2013'
                #: Attribute providing additional notes about the observation.
                self.note = "write here notes about this observation."
                self.marker = 'o'
        elif source.lower()=='j2215+5135':
            file_in = nuda.param.path_data+'astro/masses/J2215+5135.dat'
            if obs==1:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='M. Linares, T. Shahbaz, J. Casares, ApJ 859, 54 (2018)'
                #: Attribute providing the label the data is references for figures.
                self.label = 'J2215+5135 Linares 2018'
                #: Attribute providing additional notes about the observation.
                self.note = "write here notes about this observation."
                self.marker = 'o'
        elif source.lower()=='j1600+3053':
            file_in = nuda.param.path_data+'astro/masses/J1600+3053.dat'
            if obs==1:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='Z. Arzoumanian, et al., ApJ Suppl. 235(2), 37 (2018)'
                #: Attribute providing the label the data is references for figures.
                self.label = 'J1600+3053 Arzoumanian 2018'
                #: Attribute providing additional notes about the observation.
                self.note = "write here notes about this observation."
                self.marker = 'o'
        elif source.lower()=='j0740+6620':
            file_in = nuda.param.path_data+'astro/masses/J0740+6620.dat'
            if obs==1:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='H.T. Cromartie, E. Fonseca, S.M. Ransom, P.B. Demorest, et al., Nature Astron. 4(1), 72 (2019)'
                #: Attribute providing the label the data is references for figures.
                self.label = 'J0740+6620 Cromartie 2019'
                #: Attribute providing additional notes about the observation.
                self.note = "write here notes about this observation."
                self.marker = 'o'
            elif obs==2:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='E. Fonseca, H.T. Cromartie, T.T. Pennucci, P.S. Ray, 915, L12 (2021)'
                #: Attribute providing the label the data is references for figures.
                self.label = 'J0740+6620 Fonseca 2021'
                #: Attribute providing additional notes about the observation.
                self.note = "write here notes about this observation."
                self.marker = 's'
            elif obs==3:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='G. Agazie, M.F. Alam, A. Anumarlapudi, A.M. Archibald et al., ApJ Lett. 951, L9 (2023)'
                #: Attribute providing the label the data is references for figures.
                self.label = 'J0740+6620 Agazie 2023'
                #: Attribute providing additional notes about the observation.
                self.note = "write here notes about this observation."
                self.marker = 'o'
        #
        #: Attribute the observational mass of the source.
        self.mass = None
        #: Attribute the positive uncertainty.
        self.sig_up = None
        #: Attribute the negative uncertainty.
        self.sig_lo = None
        #: Attribute latexCite.
        self.latexCite = None
        #
        # read file from `file_in`
        #
        with open(file_in,'r') as file:
            for line in file:
                if '#' in line: continue
                ele = line.split(',')
                #print('ele[0]:',ele[0],' obs:',obs,' ele[:]:',ele[:])
                if int(ele[0]) == obs:
                    self.mass = float(ele[1])
                    self.sig_up = float(ele[2])
                    self.sig_lo = float(ele[3])
                    self.latexCite = ele[4].replace('\n','').replace(' ','')
        #
        if nuda.env.verb: print("Exit setupMasses()")
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
        print("   source:  ",self.source)
        print("   obs:",self.obs)
        print("   mass:",self.mass)
        print("   sigma(mass):",self.sig_up,self.sig_lo)
        print("   latexCite:",self.latexCite)
        print("   ref:    ",self.ref)
        print("   label:  ",self.label)
        print("   note:   ",self.note)
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
            print(rf"- table: {self.source} & {self.obs} & ${self.mass:.2f}^{{{+self.sig_up}}}_{{{-self.sig_lo}}}$ & \cite{{{self.latexCite}}} \\\\")
        else:
            print(rf"- No table for source {self.source}. To get table, write 'verb_latex = True' in env.py.")
        #
        if nuda.env.verb: print("Exit print_latex()")
        #

class setupMassesAverage():
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
        if nuda.env.verb: print("Enter SetupMassesAverage()")
        #
        self.source = source
        self.latexCite = None
        self.ref = None
        self.label = source+' average'
        self.note = 'compute the centroid and standard deviation from the obs. data.'
        #
        obss = masses_obss( source = source )
        #print('obss:',obss)
        #
        # search for the boundary for the masses:
        mmin = 3.0; mmax = 0.0;
        for obs in obss:
            mass = nuda.setupMasses( source = source, obs = obs )
            #mass.print_outputs( )
            mlo = mass.mass - 3*mass.sig_lo
            mup = mass.mass + 3*mass.sig_up
            if mlo < mmin: mmin = mlo
            if mup > mmax: mmax = mup
        #print('mmin:',mmin)
        #print('mmax:',mmax)
        # construct the distribution of observations in ay
        ax = np.linspace(mmin,mmax,300)
        #print('ax:',ax)
        ay = np.zeros(300)
        for obs in obss:
            mass = nuda.setupMasses( source = source, obs = obs )
            #mass.print_outputs( )
            ay += gauss(ax,mass.mass,mass.sig_up,mass.sig_lo)
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
        if nuda.env.verb: print("Exit setupMassesAverage()")
    #
    def print_output( self ):
        """
        Method which print outputs on terminal's screen.
        """
        print("")
        #
        if nuda.env.verb: print("Enter print_output()")
        #
        if nuda.env.verb_output:
            print("- Print output:")
            print("   source:  ",self.source)
            print("   mass_cen:",self.mass_cen)
            print("   sig_std:",self.sig_std)
            print("   latexCite:",self.latexCite)
            print("   ref:    ",self.ref)
            print("   label:  ",self.label)
            print("   note:   ",self.note)
        else:
            print(f"- No output for source {self.source} (average). To get output, write 'verb_output = True' in env.py.")
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
            print(rf"- table: {self.source} & av & ${self.mass_cen:.2f}\pm{self.sig_std}$ \\\\")
        else:
            print(rf"- No table for source {self.source} (average). To get table, write 'verb_latex = True' in env.py.")
        #
        if nuda.env.verb: print("Exit print_latex()")
        #


def gauss( ax, mass, sig_up, sig_lo ):
    fac = math.sqrt( 2*math.pi )
    gauss = []
    for x in ax:
        if x < mass: 
            z = ( x - mass ) / sig_lo
            norm = sig_lo * fac
        else:
            z = ( x - mass ) / sig_up
            norm = sig_up * fac
        gauss.append( math.exp( -0.5*z**2 ) / norm )
    return gauss
