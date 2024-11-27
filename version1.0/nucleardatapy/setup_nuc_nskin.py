import os
import sys
import math
import numpy as np  # 1.15.0

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def nuc_nskin():
    """
    Return a list of the nuclei (source) for which a neutron skin is given

    :return: The list of nuclei.
    :rtype: list[str].
    """
    #
    if nuda.env.verb: print("\nEnter nuc_nskin()")
    #
    sources = [ '48Ca', '208Pb' ]
    #
    #print('sources available in the toolkit:',sources)
    sources_lower = [ item.lower() for item in sources ]
    #print('sources available in the toolkit:',sources_lower)
    #
    if nuda.env.verb: print("Exit nuc_nskin()")
    #
    return sources, sources_lower

def nuc_nskin_source( source ):
    """
    Return a list of values for a given source (nuclei) and print them all on the prompt.

    :param source: The nuclei for which there are different calculations.
    :type source: str.
    :return: The list of calculations. \
    If source == '208Pb': 1, 2, 3, 4, 5,...,22
    :rtype: list[str].
    """
    #
    if nuda.env.verb: print("\nEnter nuc_nskin_source()")
    #
    if source.lower()=='48Ca':
        obss = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 ]
    elif source.lower()=='208Pb':
        obss = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
    #
    #print('Calculations available in the toolkit:',obss)
    #
    if nuda.env.verb: print("Exit nuc_nskin_source()")
    #
    return obss

class SetupNeutronSkin():
    """
    Instantiate the neutron skin calculations for a given source and obs.

    This choice is defined in the variables `source` and `obs`.

    `source` can chosen among the following ones: '48Ca'.

    `obs` depends on the chosen source.

    :param source: Fix the name of `source`. Default value: ''.
    :type source: str, optional. 
    :param obs: Fix the `obs`. Default value: 1.
    :type obs: str, optional. 

    **Attributes:**
    """
    def __init__(self, source = '48Ca', obs = 1 ):
        #
        if nuda.env.verb: print("Enter SetupNeutronSkin()")
        #
        # some checks
        #
        sources, sources_lower = nuc_nskin()
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
        # fix `file_in` and some properties of the object
        #
        if source.lower()=='48Ca':
            file_in = nuda.param.path_data+'nuclei/nskin/48Ca.dat'  
            if obs==1:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='J.C. Lombardi, R.N. Boyd, R. Arking, and A.B. Robbins, NPA 188, 103 (1972).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Lombardi 1972'
                #: Attribute providing additional notes about the calculation.
                self.note = "write notes about this calculation."
                self.marker = 'o'
            elif obs==2:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='I. Brissaud, Y. Le Bornec, B. Tatischeff, et al., NPA 191, 145 (1972).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Brissaud 1972'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this calculation."
                self.marker = 's'
            elif obs==3:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='G.D. Alkhazov, T. Bauer, R. Beurtey, et al., NPA 274, 443 (1976).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Alkhazov 1976'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this calculation."
                self.marker = 'o'              
            elif obs==4:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='G.D. Alkhazov, T. Bauer, R. Bertini et al., NPA 280, 365 (1977).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Alkhazov 1977'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this calculation."
                self.marker = 's'              
            elif obs==5:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='M.J. Jakobson, G.R. Burleson, J.R. Calarco, et al., PRL 38, 21 (1977).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Jakobson 1977'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this calculation."
                self.marker = 'o'            
            elif obs==6:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='A. Chaumeaux, V. Layly, R. Schaeffer, PLB 72, 5 (1977).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Chaumeaux 1977'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this calculation."
                self.marker = 's'   
            elif obs==7:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='E. Friedman, H.J. Gils, H. Rebel, Z. Majka, PRL 41, 18 (1978).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Friedman 1978'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this calculation."
                self.marker = 'o'         
            elif obs==8:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='I. Brissaud, X. Campi, PLB 96, 145 (1979).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Brissaud 1979'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this calculation."
                self.marker = 's'        
            elif obs==9:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='G. Igo, G.S. Adams, T.S. Bauer, et al., PLB 81, 151 (1979).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Igo 1979'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this calculation."
                self.marker = 'o'
            elif obs==10:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='K.G. Boyer, W.J. Braithwaite, W.B. Cottingame, et al., PRC 29, 182 (1984).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Boyer 1984'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this calculation."
                self.marker = 's'
            elif obs==11:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='F.J. Hartmann, R. Schmidt, B. Ketzer, et al., PRC 65, 014306 (2001).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Hartmann 2001'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this calculation."
                self.marker = 'o'
            elif obs==12:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='B.C. Clark, L.J. Kerr, S. Ham, PRC 67, 054605 (2003).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Clark 2003'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this calculation."
                self.marker = 's'
            elif obs==13:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='J. Piekarewicz, B. K. Agrawal, G. Colò, et al., PRC 85, 041302(R) (2012).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Piekarewicz 2012'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this calculation."
                self.marker = 'o'
            elif obs==14:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='J. Birkhan, M. Miorelli, S. Bacca, et al., PRL 118, 252501 (2017).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Birkhan 2017'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this calculation."
                self.marker = 's'
            elif obs==15:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='M.H. Mahzoon, M.C. Atkinson, R.J. Charity, W.H. Dickhoff, PRL 119, 222503 (2017).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Mahzoon 2017'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this calculation."
                self.marker = 'o'
            elif obs==16:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='M. Tanaka, M. Takechi, A. Homma, et al., PRL 124, 102501 (2020).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Tanaka 2020'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this calculation."
                self.marker = 's'
            elif obs==17:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='S. Tagami, T. Wakasa, M. Takechi, et al., Results in Physics 33, 105155 (2022).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Tagami 2022'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this calculation."
                self.marker = 'o'
            elif obs==18:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='D. Adhikari, H. Albataineh, D. Androic, et al., PRL 129, 042501 (2022).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'CREX Adhikari 2022'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this calculation."
                self.marker = 's'                                       
        elif source.lower()=='208Pb':
            file_in = nuda.param.path_data+'nuclei/nskin/208Pb.dat'
            if obs==1:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='A. Krasznahorkay, J. Bacelar, J.A. Bordewijk, et al., PRL 66, 1287 (1991).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Krasznahorkay 1991'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this calculation."
                self.marker = 'o'
            elif obs==2:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='V.E. Starodubsky and N.M. Hintz, PRC 49, 2118 (1994).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Starodubsky 1994'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this calculation."
                self.marker = 's'
            elif obs==3:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='S. Karataglidis, K. Amos, B.A. Brown, and P.K. Deb, PRC 65, 044306 (2002).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Karataglidis 2002'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this calculation."
                self.marker = 'o'  
            elif obs==4:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='A. Krasznahorkay, H. Akimune, A.M. van den Berg, et al., NPA 731, 224 (2004).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Krasznahorkay 2004'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this calculation."
                self.marker = 's'    
            elif obs==5:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='B. Kłos, A. Trzcińska, J. Jastrzębski, et al., PRC 76, 014311 (2007).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Kłos 2007'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this calculation."
                self.marker = 'o'    
            elif obs==6:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='S. Wycech, F.J. Hartmann, J. Jastrzębsk, et al., PRC 76, 034316 (2007).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Wycech 2007'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this calculation."
                self.marker = 's'    
            elif obs==7:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='B.A. Brown, G. Shen, G.C. Hillhouse, J. Meng, and A. Trzcińska, PRC 76, 034305 (2007).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Brown 2007'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this calculation."
                self.marker = 'o'    
            elif obs==8:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='A. Klimkiewicz, N. Paar, P. Adrich, et al., PRC 76, 051603(R) (2007).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Klimkiewicz 2007'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this calculation."
                self.marker = 's'    
            elif obs==9:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='J. Zenihiro, H. Sakaguchi, T. Murakami, et al., PRC 82, 044611 (2010).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Zenihiro 2010'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this calculation."
                self.marker = 'o'    
            elif obs==10:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='A. Carbone, G. Colò, A. Bracco, et al., PRC 81, 041301(R) (2010).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Carbone 2010'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this calculation."
                self.marker = 's'    
            elif obs==11:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='A. Tamii, I. Poltoratska, P. von Neumann-Cosel, et al., PRL 107, 062502 (2011).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Tamii 2011'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this calculation."
                self.marker = 'o'    
            elif obs==12:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='J. Piekarewicz, B.K. Agrawal, G. Colò, et al., PRC 85, 041302(R) (2012).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Piekarewicz 2012'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this calculation."
                self.marker = 's'    
            elif obs==13:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='S. Abrahamyan, Z. Ahmed, H. Albataineh, et al., PRL 108, 112502 (2012).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Abrahamyan 2012'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this calculation."
                self.marker = 'o'    
            elif obs==14:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='A. Krasznahorkay, N. Paar, D. Vretenar, and M.N. Harakeh, Physica Scripta T154, 014018 (2013).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Krasznahorkay 2013'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this calculation."
                self.marker = 's'    
            elif obs==15:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='J. Yasuda, T. Wakasa, M. Okamoto, et al., Prog. Theor. Exp. Phys 2013, 063D02 (2013).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Yasuda 2013'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this calculation."
                self.marker = 'o'    
            elif obs==16:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='C.M. Tarbert, D.P. Watts, D.I. Glazier, et al., PRL 112, 242502 (2014).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Tarbert 2014'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this calculation."
                self.marker = 's'    
            elif obs==17:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='A. Tamii, P. von Neumann-Cosel, and I. Poltoratska, Eur. Phys. J. A. 50, 28 (2014).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Tamii 2014'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this calculation."
                self.marker = 'o'    
            elif obs==18:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='F.J. Fattoyev, J. Piekarewicz, and C.J. Horowitz, PRL 120, 172702 (2018).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Fattoyev 2018'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this calculation."
                self.marker = 's' 
            elif obs==19:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='B.T. Reed, F.J. Fattoyev, C.J. Horowitz, and J. Piekarewicz, PRL 126, 172503 (2021).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Reed 2021'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this calculation."
                self.marker = 'o'    
            elif obs==20:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='S. Tagami, T. Wakasa, J. Matsui, et al., PRC 104, 024606 (2021).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Tagami 2021'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this calculation."
                self.marker = 's'    
            elif obs==21:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='D. Adhikari, H. Albataineh, D. Androic, et al., PRL 126, 172502 (2021).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'PREX2 Adhikari 2021'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this calculation."
                self.marker = 'o'    
            elif obs==22:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='G. Giacalone, G. Nijs, and W. van der Schee, PRL 131, 202302 (2023).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Giacalone 2023'
                #: Attribute providing additional notes about the observation.
                self.note = "write notes about this calculation."
                self.marker = 's'                                  
        #
        #: Attribute the neutron radius of the source.
        self.nrad = None
        #: Attribute the positive uncertainty.
        self.nrad_sig_up = None
        #: Attribute the negative uncertainty.
        self.nrad_sig_do = None
        #: Attributethe proton radius of the source.
        self.prad = None
        #: Attribute the positive uncertainty.
        self.prad_sig_up = None
        #: Attribute the negative uncertainty.
        self.prad_sig_do = None
        #: Attributethe neutron skin of the source.
        self.nskin = None
        #: Attribute the positive uncertainty.
        self.nskin_sig_up = None
        #: Attribute the negative uncertainty.
        self.nskin_sig_do = None
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
                    self.nrad = float(ele[1])
                    self.nrad_sig_up = float(ele[2])
                    self.nrad_sig_do = float(ele[3])
                    self.prad = float(ele[4])
                    self.prad_sig_up = float(ele[5])
                    self.prad_sig_do = float(ele[6])
                    self.nskin = float(ele[7])
                    self.nskin_sig_up = float(ele[8])
                    self.nskin_sig_do = float(ele[9])
                    self.latexCite = ele[10].replace('\n','').replace(' ','')
        #
        if nuda.env.verb: print("Exit SetupNeutronSkin()")
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
            print("   source:  ",self.source)
            print("   obs:",self.obs)
            print("   Rn:",self.nrad,' in fm')
            print("   sigma(Rn):",self.nrad_sig_up,self.nrad_sig_do,' in fm')
            print("   Rp:",self.prad,' in fm')
            print("   sigma(Rp):",self.prad_sig_up,self.prad_sig_do,' in fm')
            print("   Rskin:",self.nskin,' in fm')
            print("   sigma(Rskin):",self.nskin_sig_up,self.nskin_sig_do,' in fm')
            print("   latexCite:",self.latexCite)
            print("   ref:    ",self.ref)
            print("   label:  ",self.label)
            print("   note:   ",self.note)
        else:
            print(f"- No output for source {self.source}. To get output, write 'verb_output = True' in env.py.")
        #
        if nuda.env.verb: print("Exit print_output()")
        #
    #
    def print_table( self ):
        """
        Method which print outputs in table format (latex) on terminal's screen.
        """
        #
        if nuda.env.verb: print("Enter print_table()")
        #
        if nuda.env.verb_table:
            print(f"- table: {self.source} & {self.obs} & ${self.nrad:.2f}^{{{+self.nrad_sig_up}}}_{{{-self.nrad_sig_do}}}$ & ${{{self.prad:.2f}}}^{{{+self.prad_sig_up}}}_{{{-self.prad_sig_do}}}$ & ${self.nskin:.2f}^{{{+self.nskin_sig_up}}}_{{{-self.nskin_sig_do}}}$ & \\cite{{{self.latexCite}}} \\\\")
        else:
            print(f"- No  table for source {self.source}. To get  table, write  'verb_table = True' in env.py.")
        #
        if nuda.env.verb: print("Exit print_table()")
        #
