import math
import numpy as np  # 1.15.0

import nucleardatapy as nuda

def mup_sources():
    """
    Return a list of the astrophysical sources for which a mass is given

    :return: The list of sources.
    :rtype: list[str].
    """
    #
    if nuda.env.verb: print("\nEnter astro_mup()")
    #
    sources = [ 'GW170817', 'GW190814' ]
    #
    #print('sources available in the toolkit:',sources)
    sources_lower = [ item.lower() for item in sources ]
    #print('sources available in the toolkit:',sources_lower)
    #
    if nuda.env.verb: print("Exit astro_mup()")
    #
    return sources, sources_lower

def mup_hyps( source ):
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
    elif source.lower()=='gw190814':
        hyps = [ 1 ]
    #
    #print('Hypotheses available in the toolkit:',hyps)
    #
    if nuda.env.verb: print("Exit astro_mup_source()")
    #
    return hyps

class setupMup():
    """
    Instantiate the upper mass for a given source and hyptheses.

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
        if nuda.env.verb: print("Enter setupMup()")
        #
        # some checks
        #
        sources, sources_lower = mup_sources()
        if source.lower() not in sources_lower:
            print('Source ',source,' is not in the list of sources.')
            print('list of sources:',sources)
            print('-- Exit the code --')
            exit()
        self.source = source
        if nuda.env.verb: print("source:",source)
        #
        hyps = mup_hyps( source = source )
        if hyp not in hyps:
            print('Hyp ',hyp,' is not in the list of hypotheses.')
            print('list of hyp:',hyps)
            print('-- Exit the code --')
            exit()
        self.hyp = hyp
        if nuda.env.verb: print("hyp:",hyp)
        #
        # fix `file_in` and some properties of the object
        #
        if source.lower()=='gw170817':
            file_in = nuda.param.path_data+'astro/masses/GW170817.dat'
            if hyp == 1:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='B.P. Abbott, R. Abbott, T.D. Abbott, et al., PRL 119, 161101 (2017)'
                #: Attribute providing the label the data is references for figures.
                self.label = 'GW170817 low-spin Abbott 2017'
                #: Attribute providing additional notes about the observation.
                self.note = "write here notes about this observation."
                self.marker = 'o'
            elif hyp == 2:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='B.P. Abbott, R. Abbott, T.D. Abbott, et al., PRL 119, 161101 (2017)'
                #: Attribute providing the label the data is references for figures.
                self.label = 'GW170817 high-spin Abbott 2017'
                #: Attribute providing additional notes about the observation.
                self.note = "write here notes about this observation."
                self.marker = 's'
            elif hyp == 3:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref=' B.P. Abbott, R. Abbott, T.D. Abbott, F. Acernese, et al., PRX 9, 011001 (2019)'
                #: Attribute providing the label the data is references for figures.
                self.label = 'GW170817 low-spin Abbott 2019'
                #: Attribute providing additional notes about the observation.
                self.note = "write here notes about this observation."
                self.marker = 'o'
            elif hyp == 4:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref=' B.P. Abbott, R. Abbott, T.D. Abbott, F. Acernese, et al., PRX 9, 011001 (2019)'
                #: Attribute providing the label the data is references for figures.
                self.label = 'GW170817 high-spin Abbott 2019'
                #: Attribute providing additional notes about the observation.
                self.note = "write here notes about this observation."
                self.marker = 's'
        elif source.lower()=='gw190814':
            file_in = nuda.param.path_data+'astro/masses/GW190814.dat'
            if hyp == 1:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='B.P. Abbott, R. Abbott, T.D. Abbott, et al., ApJL 892, L3 (2020)'
                #: Attribute providing the label the data is references for figures.
                self.label = 'GW190814 Abbott 2020'
                #: Attribute providing additional notes about the observation.
                self.note = "write here notes about this observation."
                self.marker = 'o'
        #
        #: Attribute the observational mass of the source.
        self.mup = None
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
                #print('ele[0]:',ele[0],' hyp:',str(hyp),' ele[:]:',ele[:])
                #if ele[0].replace("'","") == str(hyp):
                if int(ele[0]) == hyp:
                    self.mup = float(ele[2])
                    self.sig_up = float(ele[3])
                    self.sig_lo = float(ele[4])
                    self.latexCite = ele[5].replace('\n','').replace(' ','')
        #
        if nuda.env.verb: print("Exit setupMup()")
        #
    #
    def print_output( self ):
        """
        Method which print outputs on terminal's screen.
        """
        #
        if nuda.env.verb: print("Enter print_output()")
        #
        print("- Print output:")
        print("   source:  ",self.source)
        print("   hyp:",self.hyp)
        print("   mup:",self.mup)
        print("   sigma(mup):",self.sig_up,self.sig_lo)
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
            print(rf"- table: {self.source} & {self.hyp} & ${self.mup:.2f}^{{{+self.sig_up}}}_{{{-self.sig_lo}}}$ & \cite{{{self.latexCite}}} \\\\")
        else:
            print(rf"- No table for source {self.source}. To get table, write 'verb_latex = True' in env.py.")
        #
        if nuda.env.verb: print("Exit print_latex()")
        #


class setupMupAverage():
    """
    Instantiate the upper mass for a given source and averaged over hypotheses.

    This choice is defined in the variable `source`.

    `source` can chosen among the following ones: 'GW170817'.

    :param source: Fix the name of `source`. Default value: 'GW170817'.
    :type source: str, optional. 

    **Attributes:**
    """
    def __init__(self, source = 'GW170817', hyps = [ 1 ] ):
        #
        if nuda.env.verb: print("Enter SetupAstroMupAverage()")
        #
        self.source = source
        self.latexCite = None
        self.ref = None
        self.label = source+' average'
        self.note = 'compute the centroid and standard deviation from the obs. data.'
        #
        #hyps = mup_hyps( source = source )
        #
        # search for the boundary for mup:
        mupmin = 3.0; mupmax = 0.0;
        for hyp in hyps:
            mup = nuda.setupMup( source = source, hyp = hyp )
            #mup.print_outputs( )
            muplo = mup.mup - 3*mup.sig_lo
            mupup = mup.mup + 3*mup.sig_up
            if muplo < mupmin: mupmin = muplo
            if mupup > mupmax: mupmax = mupup
        # construct the distribution of observations in ay
        ax = np.linspace(mupmin,mupmax,300)
        #print('ax:',ax)
        ay = np.zeros(300)
        for hyp in hyps:
            #print('hyp:',hyp)
            mup = nuda.setupMup( source = source, hyp = hyp )
            #mup.print_outputs( )
            ay += gauss(ax,mup.mup,mup.sig_up,mup.sig_lo)
        # determine the centroid and standard deviation from the distribution of obs. 
        nor = sum( ay )
        cen = sum( ay*ax )
        std = sum ( ay*ax**2 )
        self.mup_cen = cen / nor
        self.sig_std = round( math.sqrt( std/nor - self.mup_cen**2 ), 3 )
        self.mup_cen = round( self.mup_cen, 3)
        #
        if nuda.env.verb: print("Exit SetupAstroMupAverage()")
    #
    def print_output( self ):
        """
        Method which print outputs on terminal's screen.
        """
        #
        if nuda.env.verb: print("Enter print_output()")
        #
        if nuda.env.verb_output:
            print("- Print output:")
            print("   source:  ",self.source)
            print("   mup_cen:",self.mup_cen)
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
            print(rf"- table: {self.source} & ${self.mup_cen:.2f}\pm{+self.sig_std}$ & \cite{{{self.latexCite}}} \\\\")
        else:
            print(rf"- No table for source {self.source}. To get table, write 'verb_latex = True' in env.py.")
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
