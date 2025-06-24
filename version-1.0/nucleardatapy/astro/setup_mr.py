import math
import numpy as np  # 1.15.0

import nucleardatapy as nuda

def mr_sources():
    """
    Return a list of the astrophysical sources for which a mass is given

    :return: The list of sources.
    :rtype: list[str].
    """
    #
    if nuda.env.verb: print("\nEnter astro_mr()")
    #
    sources = [ 'J0030+0451', 'J0740+6620', 'J0437-4715' ]
    #
    #print('sources available in the toolkit:',sources)
    sources_lower = [ item.lower() for item in sources ]
    #print('sources available in the toolkit:',sources_lower)
    #
    if nuda.env.verb: print("Exit astro_mr()")
    #
    return sources, sources_lower

def mr_obss( source ):
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
        obss = [ 1, 2, 3, 4 ]
    elif source.lower()=='j0740+6620':
        obss = [ 1, 2, 3 ]
    elif source.lower()=='j0437-4715':
        obss = [ 1 ]
    #
    #print('Observations available in the toolkit:',obss)
    #
    if nuda.env.verb: print("Exit astro_mr_source()")
    #
    return obss

class setupMR():
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
        if nuda.env.verb: print("Enter setupMR()")
        #
        # some checks
        #
        sources, sources_lower = mr_sources()
        if source.lower() not in sources_lower:
            print('Source ',source,' is not in the list of sources.')
            print('list of sources:',sources)
            print('-- Exit the code --')
            exit()
        self.source = source
        if nuda.env.verb: print("source:",source)
        #
        obss = mr_obss( source = source )
        if obs not in obss:
            print('Obs ',obs,' is not in the list of obs.')
            print('list of obs:',obss)
            print('-- Exit the code --')
            exit()
        self.obs = obs
        if nuda.env.verb: print("obs:",obs)
        #
        # fix `file_in` and some properties of the object
        #
        if source.lower()=='j0030+0451':
            file_in = nuda.param.path_data+'astro/NICER/J0030+0451.dat'
            if obs==1:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='M.C. Miller, F.K. Lamb, A.J. Dittmann, aet al., ApJL 887, L24 (2019).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'J0030 Miller 2019'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this observation."
                self.marker = 'o'
            elif obs==2:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='T.E. Riley, A.L. Watts, S. Bogdanov, P.S. Ray, et al., ApJ 887, L21 (2019).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'J0030 Riley 2019'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this observation."
                self.marker = 's'
            elif obs==3:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='S. Vinciguerra, T. Salmi, A.L. Watts, D. Choudhury, et al., ApJ 961, 62 (2024).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'J0030 Vinciguerra 2024a'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this observation."
                self.marker = 'x'
            elif obs==4:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='S. Vinciguerra, T. Salmi, A.L. Watts, D. Choudhury, et al., ApJ 961, 62 (2024).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'J0030 Vinciguerra 2024b'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this observation."
                self.marker = 'x'
        elif source.lower()=='j0740+6620':
            file_in = nuda.param.path_data+'astro/NICER/J0740+6620.dat'
            if obs==1:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='M.C. Miller, F.K. Lamb, A.J. Dittmann, S. Bogdanov, et al., ApJL 918, L28 (2021).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'J0740 Miller 2021'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this observation."
                self.marker = 'o'
            elif obs==2:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='T.E. Riley, A.L. Watts, P.S. Ray, S. Bogdanov, et al., ApJL 918, L27 (2021).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'J0740 Riley 2021'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this observation."
                self.marker = 's'
            elif obs==3:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='T. Salmi, D. Choudhury, Y. Kini, T.E. Riley et al., ApJ 974, 294 (2024).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'J0740 Salmi 2024'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this observation."
                self.marker = 's'
        elif source.lower()=='j0437-4715':
            file_in = nuda.param.path_data+'astro/NICER/J0437-4715.dat'
            if obs==1:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='D. Choudhury, T. Salmi, S. Vinciguerra, T.E. Riley, et al., ApJL 971, L20 (2024).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'J0437 Choudhury 2024'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this observation."
                self.marker = 'o'
        #
        #: Attribute the observational mass of the source.
        self.mass = None
        #: Attribute the positive uncertainty.
        self.mass_sig_up = None
        #: Attribute the negative uncertainty.
        self.mass_sig_lo = None
        #: Attribute the observational mass of the source.
        self.rad = None
        #: Attribute the positive uncertainty.
        self.rad_sig_up = None
        #: Attribute the negative uncertainty.
        self.rad_sig_lo = None
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
                    self.rad = float(ele[1])
                    self.rad_sig_up = float(ele[2])
                    self.rad_sig_lo = float(ele[3])
                    self.mass = float(ele[4])
                    self.mass_sig_up = float(ele[5])
                    self.mass_sig_lo = float(ele[6])
                    #print('ele[7]:',ele[7],' len:',len(ele[7]))
                    if len(ele[7])>1:
                        self.comp = float(ele[7])
                        self.comp_sig_up = float(ele[8])
                        self.comp_sig_lo = float(ele[9])
                    else:
                        self.comp = 0.0
                        self.comp_sig_up = 1.0
                        self.comp_sig_lo = 1.0
                    self.latexCite = ele[10].replace('\n','').replace(' ','')
        #
        # compute compactness
        #
        # fix the boundary for the masses and the radii:
        #mmin = self.mass - 3*self.mass_sig_lo
        #mmax = self.mass + 3*self.mass_sig_up
        #rmin = self.rad - 3*self.rad_sig_lo
        #rmax = self.rad + 3*self.rad_sig_up
        #print('Sch rad of the sun:',nuda.cst.rshsol_si)
        # construct the distribution of observations in ay
        #ar = np.linspace(rmin,rmax,300); ar=np.array( ar )
        #am = np.linspace(mmin,mmax,300); am=np.array( am )
        ##ac = 0.5 * am / ar
        #ac = 0.5 * nuda.cst.rshsol_si / 1.e3 * am / ar
        #ayr = gauss(ar,self.rad,self.rad_sig_up,self.rad_sig_lo); ayr=np.array( ayr )
        #aym = gauss(am,self.mass,self.mass_sig_up,self.mass_sig_lo); aym=np.array( aym )
        #ayc = aym * ayr 
        # determine the centroid and standard deviation for the compactness
        #noc = sum( ayc )
        #cenc = sum( ayc*ac )
        #stdc = sum ( ayc*ac**2 )
        #self.comp = cenc / noc
        #self.comp_sig_std = round( math.sqrt( stdc/noc - self.comp**2 ), 3 )
        #self.comp = round( self.comp, 3)
        #
        if nuda.env.verb: print("Exit setupMR()")
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
        print("   obs:",self.obs)
        print("   mass:",self.mass,' in Mo')
        print("   sigma(mass):",self.mass_sig_up,self.mass_sig_lo,' in Mo')
        print("   rad:",self.rad,' in km')
        print("   sigma(mass):",self.rad_sig_up,self.rad_sig_lo,' in km')
        print("   compactness:",self.comp)
        print("   sigma(comp):",self.comp_sig_up,self.comp_sig_lo)
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
            print(rf"- table: {self.source} & {self.obs} & ${{{self.rad:.2f}}}^{{{+self.rad_sig_up}}}_{{{-self.rad_sig_lo}}}$ & ${self.mass:.3f}^{{{+self.mass_sig_up}}}_{{{-self.mass_sig_lo}}}$ & ${self.comp}^{{{+self.comp_sig_up}}}_{{{-self.comp_sig_lo}}}$ & \cite{{{self.latexCite}}} \\\\")
        else:
            print(rf"- No  table for source {self.source}. To get  table, write  'verb_table = True' in env.py.")
        #
        if nuda.env.verb: print("Exit print_latex()")
        #

class setupMRAverage():
    """
    Instantiate the observational mass for a given source and averaged over obs.

    This choice is defined in the variable `source`.

    `source` can chosen among the following ones: 'J1614–2230'.

    :param source: Fix the name of `source`. Default value: 'J1614–2230'.
    :type source: str, optional. 

    **Attributes:**
    """
    def __init__(self, source = 'J1614–2230', obss = [ 1, 2 ] ):
        #
        if nuda.env.verb: print("Enter SetupAstroMRAverage()")
        #
        self.source = source
        self.latexCite = None
        self.ref = None
        self.label = source+' average'
        self.note = 'compute the centroid and standard deviation over several obs. data.'
        #
        #obss = mr_obss( source = source )
        #
        # search for the boundary for the masses and the radii:
        mmin = 3.0; mmax = 0.0;
        rmin = 30.0; rmax = 0.0;
        cmin = 30.0; cmax = 0.0;
        for obs in obss:
            # mass:
            mr = nuda.setupMR( source = source, obs = obs )
            mlo = mr.mass - 3*mr.mass_sig_lo
            mup = mr.mass + 3*mr.mass_sig_up
            if mlo < mmin: mmin = mlo
            if mup > mmax: mmax = mup
            # radius:
            rlo = mr.rad - 3*mr.rad_sig_lo
            rup = mr.rad + 3*mr.rad_sig_up
            if rlo < rmin: rmin = rlo
            if rup > rmax: rmax = rup
            # compactness:
            clo = mr.comp - 3*mr.comp_sig_lo
            cup = mr.comp + 3*mr.comp_sig_up
            if clo < cmin: cmin = clo
            if cup > cmax: cmax = cup
        # construct the distribution of observations in ay
        ar = np.linspace(rmin,rmax,300); ar=np.array( ar )
        am = np.linspace(mmin,mmax,300); am=np.array( am )
        print('cmax:',cmax)
        print('cmin:',cmin)
        ac = np.linspace(cmin,cmax,300); ac=np.array( ac )
        #ac = 0.5 * nuda.cst.rshsol_si / 1.e3 * am / ar
        ayr = np.zeros(300); ayr=np.array( ayr )
        aym = np.zeros(300); aym=np.array( aym )
        ayc = np.zeros(300); ayc=np.array( ayc )
        for obs in obss:
            mr = nuda.setupMR( source = source, obs = obs )
            ayr += gauss(ar,mr.rad,mr.rad_sig_up,mr.rad_sig_lo)
            aym += gauss(am,mr.mass,mr.mass_sig_up,mr.mass_sig_lo)
            ayc += gauss(ac,mr.comp,mr.comp_sig_up,mr.comp_sig_lo)
        #ayc = aym * ayr 
        # determine the centroid and standard deviation from the distribution of obs. 
        nor = sum( ayr )
        nom = sum( aym )
        noc = sum( ayc )
        cenr = sum( ayr*ar )
        cenm = sum( aym*am )
        cenc = sum( ayc*ac )
        stdr = sum ( ayr*ar**2 )
        stdm = sum ( aym*am**2 )
        stdc = sum ( ayc*ac**2 )
        self.rad_cen = cenr / nor
        self.mass_cen = cenm / nom
        self.comp_cen = cenc / noc
        self.rad_sig_std = round( math.sqrt( stdr/nor - self.rad_cen**2 ), 3 )
        self.mass_sig_std = round( math.sqrt( stdm/nom - self.mass_cen**2 ), 3 )
        self.comp_sig_std = round( math.sqrt( stdc/noc - self.comp_cen**2 ), 3 )
        self.rad_cen = round( self.rad_cen, 3)
        self.mass_cen = round( self.mass_cen, 3)
        self.comp_cen = round( self.comp_cen, 3)
        #
        if nuda.env.verb: print("Exit setupMRAverage()")
    #
    def print_output( self ):
        """
        Method which print outputs on terminal's screen.
        """
        #
        if nuda.env.verb: print("Enter print_output()")
        #
        if nuda.env.verb_output:
            print("- Print output (average):")
            print("   source:  ",self.source)
            print("   mass_cen:",self.mass_cen,' in Mo')
            print("   mass_sig_std:",self.mass_sig_std,' in Mo')
            print("   rad_cen:",self.rad_cen,' in km')
            print("   rad_sig_std:",self.rad_sig_std,' in km')
            print("   compactness:",self.comp_cen)
            print("   sigma(comp):",self.comp_sig_std)
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
            print(rf"- table: {self.source} & av & ${self.rad_cen:.2f}\pm{self.rad_sig_std}$ & ${self.mass_cen:.3f}\pm{self.mass_sig_std}$ & ${self.comp_cen}\pm{self.comp_sig_std}$ & \\\\")
        else:
            print(rf"- No table for source {self.source} (average). To get table, write 'verb_latex = True' in env.py.")
        #
        if nuda.env.verb: print("Exit print_latex()")
        #

def gauss( ax, cent, sig_up, sig_lo ):
    fac = math.sqrt( 2*math.pi )
    gauss = []
    for x in ax:
        if x < cent: 
            z = ( x - cent ) / sig_lo
            norm = sig_lo * fac
        else:
            z = ( x - cent ) / sig_up
            norm = sig_up * fac
        gauss.append( math.exp( -0.5*z**2 ) / norm )
    return gauss

