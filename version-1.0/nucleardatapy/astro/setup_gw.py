import math
import numpy as np  # 1.15.0

import nucleardatapy as nuda

def gw_sources():
    """
    Return a list of the astrophysical sources for which a mass is given

    :return: The list of sources.
    :rtype: list[str].
    """
    #
    if nuda.env.verb: print("\nEnter gw_sources()")
    #
    sources = [ 'GW170817', 'GW190425' ]
    #
    #print('sources available in the toolkit:',sources)
    sources_lower = [ item.lower() for item in sources ]
    #print('sources available in the toolkit:',sources_lower)
    #
    if nuda.env.verb: print("Exit gw_sources()")
    #
    return sources, sources_lower

def gw_hyps( source ):
    """
    Return a list of observations for a given source and print them all on the prompt.

    :param source: The source for which there are different hypotheses.
    :type source: str.
    :return: The list of hypotheses. \
    If source == 'GW170817': 1, 2, 3, 4, 5.
    :rtype: list[str].
    """
    #
    if nuda.env.verb: print("\nEnter gw_hyps()")
    #
    if source.lower()=='gw170817':
        hyps = [ 1, 2, 3, 4, 5 ]
    elif source.lower()=='gw190425':
        hyps = [ 1, 2 ]
    #
    #print('Hypothesis available in the toolkit:',hyps)
    #
    if nuda.env.verb: print("Exit gw_hyps()")
    #
    return hyps

class setupGW():
    """
    Instantiate the tidal deformability for a given source and obs.

    This choice is defined in the variables `source` and `obs`.

    `source` can chosen among the following ones: 'GW170817'.

    `obs` depends on the chosen source.

    :param source: Fix the name of `source`. Default value: 'GW170817'.
    :type source: str, optional. 
    :param obs: Fix the `obs`. Default value: 1.
    :type obs: str, optional. 

    **Attributes:**
    """
    def __init__(self, source = 'GW170817', hyp = 1 ):
        #
        if nuda.env.verb: print("Enter setupGW()")
        #
        # some checks
        #
        sources, sources_lower = gw_sources()
        if source.lower() not in sources_lower:
            print('Source ',source,' is not in the list of sources.')
            print('list of sources:',sources)
            print('-- Exit the code --')
            exit()
        self.source = source
        if nuda.env.verb: print("source:",source)
        #
        hyps = gw_hyps( source = source )
        if hyp not in hyps:
            print('Hyp ',hyp,' is not in the list of hyp.')
            print('list of hyps:',hyps)
            print('-- Exit the code --')
            exit()
        self.hyp = hyp
        if nuda.env.verb: print("hyp:",hyp)
        #
        # initialize self
        #
        self = setupGW.init_self( self )
        #
        # fix `file_in` and some properties of the object
        #
        if source.lower()=='gw170817':
            file_in = nuda.param.path_data+'astro/GW/GW170817.dat'
            if hyp==1:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='B.P. Abbott, R. Abbott, T.D. Abbott, et al., PRL 119, 161101 (2017)'
                #: Attribute providing the label the data is references for figures.
                self.label = 'GW170817 LS Abbott 2017'
                #: Attribute providing additional notes about the data.
                self.note = "write here notes about this observation."
                self.marker = 'o'
            elif hyp==2:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='B.P. Abbott, R. Abbott, T.D. Abbott, et al., PRL 119, 161101 (2017)'
                #: Attribute providing the label the data is references for figures.
                self.label = 'GW170817 HS Abbott 2017'
                #: Attribute providing additional notes about the data.
                self.note = "write here notes about this observation."
                self.marker = 's'
            elif hyp==3:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='S. De, D. Finstad, J.M. Lattimer, D.A. Brown, E. Berger, C.M. Biwer, PRL 121, 091102 (2018)'
                #: Attribute providing the label the data is references for figures.
                self.label = 'GW170817 De 2018'
                #: Attribute providing additional notes about the data.
                self.note = "write here notes about this observation."
                self.marker = 'o'
            elif hyp==4:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref=' B.P. Abbott, R. Abbott, T.D. Abbott, F. Acernese, et al., Phys. Rev. X 9, 011001 (2019)'
                #: Attribute providing the label the data is references for figures.
                self.label = 'GW170817 LS Abbott 2019'
                #: Attribute providing additional notes about the data.
                self.note = "write here notes about this observation."
                self.marker = 'o'
            elif hyp==5:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref=' B.P. Abbott, R. Abbott, T.D. Abbott, F. Acernese, et al., Phys. Rev. X 9, 011001 (2019)'
                #: Attribute providing the label the data is references for figures.
                self.label = 'GW170817 HS Abbott 2019'
                #: Attribute providing additional notes about the data.
                self.note = "write here notes about this observation."
                self.marker = 's'
        elif source.lower()=='gw190425':
            file_in = nuda.param.path_data+'astro/GW/GW190425.dat'
            if hyp==1:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='B.P. Abbott, R. Abbott, T.D. Abbott, S. Abraham, et al., ApJL 892, L3 (2020)'
                #: Attribute providing the label the data is references for figures.
                self.label = 'GW190425 LS Abbott 2020'
                #: Attribute providing additional notes about the data.
                self.note = "write here notes about this observation."
                self.marker = 'o'
            elif hyp==2:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='B.P. Abbott, R. Abbott, T.D. Abbott, S. Abraham, et al., ApJL 892, L3 (2020)'
                #: Attribute providing the label the data is references for figures.
                self.label = 'GW190425 HS Abbott 2020'
                #: Attribute providing additional notes about the data.
                self.note = "write here notes about this observation."
                self.marker = 's'
        #
        # read file from `file_in`
        #
        with open(file_in,'r') as file:
            for line in file:
                if '#' in line: continue
                ele = line.split(',')
                #print('ele[0]:',ele[0],' obs:',obs, 'ele[:]:',ele[:])
                if int(ele[0]) == hyp:
                    self.mchirp = float(ele[1])
                    self.mchirp_sig_up = float(ele[2])
                    self.mchirp_sig_lo = float(ele[3])
                    self.q_lo = float(ele[4])
                    self.q_up = float(ele[5])
                    self.lam = float(ele[6])
                    self.lam_sig_up = float(ele[7])
                    self.lam_sig_lo = float(ele[8])
                    self.latexCite = ele[9].replace('\n','').replace(' ','')
        #
        if nuda.env.verb: print("Exit setupGW()")
        #
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
            print("   source:       ",self.source)
            print("   hyp:          ",self.hyp)
            print("   m_chirp:      ",self.mchirp)
            print("   sig(m_chirp): ",self.mchirp_sig_up,self.mchirp_sig_lo)
            print("   q_lo, q_up:   ",self.q_lo, self.q_up)
            print("   lambda:       ",self.lam)
            print("   sig(lambda):  ",self.lam_sig_up,self.lam_sig_lo)
            print("   latexCite:    ",self.latexCite)
            print("   ref:          ",self.ref)
            print("   label:        ",self.label)
            print("   note:         ",self.note)
        else:
            print(f"- No output for source {self.source}. To get output, write 'verb_output = True' in env.py.")
        #
        if nuda.env.verb: print("Exit print_outputs()")
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
            print(rf"- table: {self.source} & {self.hyp} & ${self.mchirp:.4f}^{{{+self.mchirp_sig_up}}}_{{{-self.mchirp_sig_lo}}}$ & $[{self.q_lo}:{self.q_up}]$ & ${{{self.lam:.2f}}}^{{{+self.lam_sig_up}}}_{{{-self.lam_sig_lo}}}$ & \cite{{{self.latexCite}}} \\\\")
        else:
            print(rf"- No  table for source {self.source}. To get  table, write  'verb_table = True' in env.py.")
        #
        if nuda.env.verb: print("Exit print_latex()")
        #
        #
    def init_self( self ):
        """
        Initialize variables in self.
        """
        #
        if nuda.env.verb: print("Enter init_self()")
        #
        #: Attribute providing the full reference to the paper to be citted.
        self.ref = None
        #: Attribute providing the label the data is references for figures.
        self.label = None
        #: Attribute providing additional notes about the data.
        self.note = None
        self.marker = None
        #: Attribute latexCite.
        self.latexCite = None
        #
        self.mchirp = None
        self.mchirp_sig_up = None
        self.mchirp_sig_lo = None
        self.q_lo = None
        self.q_up = None
        self.lam  = None
        #: Attribute the lower bound of the tidal deformability for the source.
        self.lambda_sig_up = None
        #: Attribute the upper bound of the tidal deformability for the source.
        self.lambda_sig_lo = None
        #
        if nuda.env.verb: print("Exit init_self()")
        #
        return self        

class setupGWAverage():
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
        if nuda.env.verb: print("Enter setupGWAverage()")
        #
        self.source = source
        #
        # initialize self
        #
        self = setupGWAverage.init_self( self )
        #
        hyps = gw_hyps( source = source )
        #
        # search for the boundary for mtot:
        lammin = 3000.0; lammax = 0.0;
        for hyp in hyps:
            gw = nuda.astro.setupGW( source = source, hyp = hyp )
            #gw.print_outputs( )
            lamlo = gw.lam - 3*gw.lam_sig_lo
            lamup = gw.lam + 3*gw.lam_sig_up
            if lamlo < lammin: lammin = lamlo
            if lamup > lammax: lammax = lamup
        # construct the distribution of observations in ay
        ax = np.linspace(lammin,lammax,300)
        ay = np.zeros(300)
        for hyp in hyps:
            #print('hyp:',hyp)
            gw = nuda.astro.setupGW( source = source, hyp = hyp )
            #gw.print_outputs( )
            ay += gauss(ax,gw.lam,gw.lam_sig_up,gw.lam_sig_lo)
        # determine the centroid and standard deviation from the distribution of obs. 
        nor = sum( ay )
        cen = sum( ay*ax )
        std = sum ( ay*ax**2 )
        self.lam_cen = cen / nor
        self.lam_sig_std = round( math.sqrt( std/nor - self.lam_cen**2 ), 3 )
        self.lam_cen = round( self.lam_cen, 3)
        #
        if nuda.env.verb: print("Exit setupGWAverage()")
    #
    def print_output( self ):
        """
        Method which print outputs on terminal's screen.
        """
        #
        if nuda.env.verb: print("Enter print_outputs()")
        #
        if nuda.env.verb_output:
            print("- Print output:")
            print("   source:  ",self.source)
            print("   lam_cen:",self.lam_cen)
            print("   lam_sig_std:",self.lam_sig_std)
            print("   latexCite:",self.latexCite)
            print("   ref:    ",self.ref)
            print("   label:  ",self.label)
            print("   note:   ",self.note)
        else:
            print(f"- No output for source {self.source} (average). To get output, write 'verb_output = True' in env.py.")
        #
        if nuda.env.verb: print("Exit print_output()")
        #
    def print_latex( self ):
        """
        Method which print outputs in table format (latex) on terminal's screen.
        """
        #
        if nuda.env.verb: print("Enter print_latex()")
        #
        if nuda.env.verb_latex:
            print(rf"- table: {self.source} &  &  &  &  &  \\\\")
        else:
            print(rf"- No  table for source {self.source} (average). To get  table, write  'verb_table = True' in env.py.")
        #
        if nuda.env.verb: print("Exit print_latex()")
        #
    def init_self( self ):
        """
        Initialize variables in self.
        """
        #
        if nuda.env.verb: print("Enter init_self()")
        #
        self.latexCite = None
        self.ref = None
        self.label = self.source+' average'
        self.note = 'compute the centroid and standard deviation from the obs. data.'
        #
        self.lam_cen = None
        self.lam_sig_std = None        
        #
        if nuda.env.verb: print("Exit init_self()")
        #
        return self        

def gauss( ax, lam, sig_up, sig_lo ):
    fac = math.sqrt( 2*math.pi )
    gauss = []
    for x in ax:
        if x < lam: 
            z = ( x - lam ) / sig_lo
            norm = sig_lo * fac
        else:
            z = ( x - lam ) / sig_up
            norm = sig_up * fac
        gauss.append( math.exp( -0.5*z**2 ) / norm )
    return gauss

