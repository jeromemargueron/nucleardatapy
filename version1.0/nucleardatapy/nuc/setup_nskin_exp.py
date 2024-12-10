import os
import sys
import math
import numpy as np  # 1.15.0

# nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
# sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def nskin_exp():
    """
    Return a list of the nuclei (source) for which a neutron skin is given

    :return: The list of nuclei.
    :rtype: list[str].
    """
    #
    if nuda.env.verb: print("\nEnter nskin_exp()")
    #
    sources = [ '48Ca', '208Pb' ]
    #
    # print('sources available in the toolkit:',sources)
    sources_lower = [ item.lower() for item in sources ]
    # print('sources available in the toolkit:',sources_lower)
    #
    if nuda.env.verb: print("Exit nskin_exp()")
    #
    return sources, sources_lower

def nskin_exp_source(source):
    """
    Return a list of values for a given source (nuclei).

    :param source: The nuclei for which there are different calculations.
    :type source: str.
    :return: The list of calculations.
    :rtype: list[int].
    """
    if nuda.env.verb: print("\nEnter nskin_exp_source()")

    cals = []
    if source.lower() == '48ca':
        cals = list(range(1, 19))  
    elif source.lower() == '208pb':
        cals = list(range(1, 23))
    else:
        raise ValueError(f"Source '{source}' is not supported. Supported sources are: '48Ca' and '208Pb'.")

    if nuda.env.verb: print("Exit nskin_source()")
    return cals

class SetupNeutronSkinExp():
    """
    Instantiate the neutron skin calculations for a given source and cal.

    This choice is defined in the variables `source` and `cal`.

    `source` can chosen among the following ones: '48Ca'.

    `cal` depends on the chosen source.

    :param source: Fix the name of `source`. Default value: ''.
    :type source: str, optional. 
    :param cal: Fix the `cal`. Default value: 1.
    :type cal: str, optional. 

    **Attributes:**
    """
    def __init__(self, source = '208Pb', cal = 1 ):
        #
        if nuda.env.verb: print("Enter SetupNeutronSkin()")
        #
        # some checks
        #
        sources, sources_lower = nskin_exp()
        if source.lower() not in sources_lower:
            print('Source ',source,' is not in the list of sources.')
            print('list of sources:',sources)
            print('-- Exit the code --')
            exit()
        self.source = source
        if nuda.env.verb: print("source:",source)
        #
        cals = nskin_exp_source( source = source )
        if cal not in cals:
            print('cal ',cal,' is not in the list of cal.')
            print('list of cal:',cals)
            print('-- Exit the code --')
            exit()
        self.cal = cal
        if nuda.env.verb: print("cal:",cal)
        #
        # fix `file_in` and some properties of the object
        #
        file_in = None
        if source.lower() == '48ca':
            file_in = nuda.param.path_data + 'nuclei/nskin/48Ca.dat'
        elif source.lower() == '208pb':
            file_in = nuda.param.path_data + 'nuclei/nskin/208Pb.dat'
        else:
            raise ValueError(f"Unsupported source '{source}'. Expected '48Ca' or '208Pb'.")
        if file_in is None:
            raise RuntimeError("file_in was not initialized.")
        # 
        # Initialize object attributes with some defaults or handle cases where cal is not matched
        self.ref = None
        self.label = None
        self.note = None
        self.marker = None
        # 
        if source.lower()=='48Ca':
            if cal==1:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='J.C. Lombardi, R.N. Boyd, R. Arking, and A.B. Robbins, NPA 188, 103 (1972).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Lombardi 1972'
                #: Attribute providing additional notes about the calculation.
                self.note = "10.8-16.3 MeV p elastic scattering."
                self.marker = 'o'
            elif cal==2:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='I. Brissaud, Y. Le Bornec, B. Tatischeff, et al., NPA 191, 145 (1972).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Brissaud 1972'
                #: Attribute providing additional notes about the calculation.
                self.note = "166 MeV α elastic scattering."
                self.marker = 's'
            elif cal==3:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='G.D. Alkhazov, T. Bauer, R. Beurtey, et al., NPA 274, 443 (1976).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Alkhazov 1976'
                #: Attribute providing additional notes about the for.
                self.note = "1044 MeV p elastic scattering."
                self.marker = 'v'              
            elif cal==4:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='G.D. Alkhazov, T. Bauer, R. Bertini et al., NPA 280, 365 (1977).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Alkhazov 1977'
                #: Attribute providing additional notes about the .
                self.note = "1370 MeV α elastic scattering ."
                self.marker = '^'              
            elif cal==5:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='M.J. Jakcalon, G.R. Burleson, J.R. Calarco, et al., PRL 38, 21 (1977).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Jakcalon 1977'
                #: Attribute providing additional notes about the calculation.
                self.note = "π− and π+ scattering ."
                self.marker = '>'            
            elif cal==6:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='A. Chaumeaux, V. Layly, R. Schaeffer, PLB 72, 5 (1977).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Chaumeaux 1977'
                #: Attribute providing additional notes about the calculation.
                self.note = "1040 MeV p elastic scattering."
                self.marker = '<'   
            elif cal==7:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='E. Friedman, H.J. Gils, H. Rebel, Z. Majka, PRL 41, 18 (1978).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Friedman 1978'
                #: Attribute providing additional notes about the calculation.
                self.note = "104 MeV αelastic scattering."
                self.marker = 'p'         
            elif cal==8:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='I. Brissaud, X. Campi, PLB 96, 145 (1979).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Brissaud 1979'
                #: Attribute providing additional notes about the calculation.
                self.note = "1040 MeV p scattering ."
                self.marker = 'h'        
            elif cal==9:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='G. Igo, G.S. Adams, T.S. Bauer, et al., PLB 81, 151 (1979).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Igo 1979'
                #: Attribute providing additional notes about the calculation.
                self.note = "800 MeV ⃗p+48Ca."
                self.marker = 'H'
            elif cal==10:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='K.G. Boyer, W.J. Braithwaite, W.B. Cottingame, et al., PRC 29, 182 (1984).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Boyer 1984'
                #: Attribute providing additional notes about the calculation.
                self.note = "π− and π+ scattering ."
                self.marker = 'o'
            elif cal==11:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='F.J. Hartmann, R. Schmidt, B. Ketzer, et al., PRC 65, 014306 (2001).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Hartmann 2001'
                #: Attribute providing additional notes about the calculation.
                self.note = "analysis of antiprotonic atoms."
                self.marker = 's'
            elif cal==12:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='B.C. Clark, L.J. Kerr, S. Ham, PRC 67, 054605 (2003).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Clark 2003'
                #: Attribute providing additional notes about the calculation.
                self.note = "500-1040 MeV p scattering."
                self.marker = 'v'
            elif cal==13:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='J. Piekarewicz, B. K. Agrawal, G. Colò, et al., PRC 85, 041302(R) (2012).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Piekarewicz 2012'
                #: Attribute providing additional notes about the calculation.
                self.note = "electric dipole polarizability - reanalsis of Tamii 2011."
                self.marker = '^'
            elif cal==14:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='J. Birkhan, M. Miorelli, S. Bacca, et al., PRL 118, 252501 (2017).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Birkhan 2017'
                #: Attribute providing additional notes about the calculation.
                self.note = "electric dipole polarizability."
                self.marker = '>'
            elif cal==15:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='M.H. Mahzoon, M.C. Atkinson, R.J. Charity, W.H. Dickhoff, PRL 119, 222503 (2017).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Mahzoon 2017'
                #: Attribute providing additional notes about the calculation.
                self.note = "n+48Ca and p+48Ca scattering."
                self.marker = '<'
            elif cal==16:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='M. Tanaka, M. Takechi, A. Homma, et al., PRL 124, 102501 (2020).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Tanaka 2020'
                #: Attribute providing additional notes about the calculation.
                self.note = "48Ca+12C interaction cross section."
                self.marker = 'p'
            elif cal==17:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='S. Tagami, T. Wakasa, M. Takechi, et al., Results in Physics 33, 105155 (2022).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Tagami 2022'
                #: Attribute providing additional notes about the calculation.
                self.note = "p+48Ca and 48Ca+12C scattering."
                self.marker = 'h'
            elif cal==18:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='D. Adhikari, H. Albataineh, D. Androic, et al., PRL 129, 042501 (2022).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Adhikari 2022'
                #: Attribute providing additional notes about the calculation.
                self.note = "CREX."
                self.marker = 'H'                                       
        elif source.lower()=='208Pb':
            if cal==1:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='A. Krasznahorkay, J. Bacelar, J.A. Bordewijk, et al., PRL 66, 1287 (1991).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Krasznahorkay 1991'
                #: Attribute providing additional notes about the calculation.
                self.note = "giant dipole resonance; 120 MeV α-scattering."
                self.marker = 'o'
            elif cal==2:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='V.E. Starodubsky and N.M. Hintz, PRC 49, 2118 (1994).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Starodubsky 1994'
                #: Attribute providing additional notes about the calculation.
                self.note = "elastic p scattering at 650 MeV."
                self.marker = 's'
            elif cal==3:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='S. Karataglidis, K. Amos, B.A. Brown, and P.K. Deb, PRC 65, 044306 (2002).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Karataglidis 2002'
                #: Attribute providing additional notes about the calculation.
                self.note = "elastic p and n scattering at 40, 65, 200 MeV."
                self.marker = 'v'  
            elif cal==4:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='A. Krasznahorkay, H. Akimune, A.M. van den Berg, et al., NPA 731, 224 (2004).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Krasznahorkay 2004'
                #: Attribute providing additional notes about the calculation.
                self.note = "giant dipole resonance; 196 MeV α-scattering."
                self.marker = '^'    
            elif cal==5:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='B. Kłos, A. Trzcińska, J. Jastrzębski, et al., PRC 76, 014311 (2007).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Kłos 2007'
                #: Attribute providing additional notes about the calculation.
                self.note = "antiprotonic atoms."
                self.marker = '>'    
            elif cal==6:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='S. Wycech, F.J. Hartmann, J. Jastrzębsk, et al., PRC 76, 034316 (2007).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Wycech 2007'
                #: Attribute providing additional notes about the calculation.
                self.note = "antiprotonic atoms."
                self.marker = '<'    
            elif cal==7:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='B.A. Brown, G. Shen, G.C. Hillhouse, J. Meng, and A. Trzcińska, PRC 76, 034305 (2007).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Brown 2007'
                #: Attribute providing additional notes about the calculation.
                self.note = "antiprotonic atoms."
                self.marker = 'p'    
            elif cal==8:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='A. Klimkiewicz, N. Paar, P. Adrich, et al., PRC 76, 051603(R) (2007).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Klimkiewicz 2007'
                #: Attribute providing additional notes about the calculation.
                self.note = "strength of pigmy dipole resonance."
                self.marker = 'h'    
            elif cal==9:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='J. Zenihiro, H. Sakaguchi, T. Murakami, et al., PRC 82, 044611 (2010).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Zenihiro 2010'
                #: Attribute providing additional notes about the calculation.
                self.note = "elastic p scattering at 295 MeV."
                self.marker = 'H'    
            elif cal==10:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='A. Carbone, G. Colò, A. Bracco, et al., PRC 81, 041301(R) (2010).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Carbone 2010'
                #: Attribute providing additional notes about the calculation.
                self.note = "strength of pigmy dipole resonance."
                self.marker = 'D'    
            elif cal==11:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='A. Tamii, I. Poltoratska, P. von Neumann-Cosel, et al., PRL 107, 062502 (2011).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Tamii 2011'
                #: Attribute providing additional notes about the calculation.
                self.note = "electric dipole polarizability ."
                self.marker = 'x'    
            elif cal==12:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='J. Piekarewicz, B.K. Agrawal, G. Colò, et al., PRC 85, 041302(R) (2012).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Piekarewicz 2012'
                #: Attribute providing additional notes about the calculation.
                self.note = "electric dipole polarizability - reanalsis of Tamii 2011."
                self.marker = 'o'    
            elif cal==13:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='S. Abrahamyan, Z. Ahmed, H. Albataineh, et al., PRL 108, 112502 (2012).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Abrahamyan 2012'
                #: Attribute providing additional notes about the calculation.
                self.note = "PREX-1: parity violating e− scattering."
                self.marker = 's'    
            elif cal==14:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='A. Krasznahorkay, N. Paar, D. Vretenar, and M.N. Harakeh, Physica Scripta T154, 014018 (2013).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Krasznahorkay 2013'
                #: Attribute providing additional notes about the calculation.
                self.note = "anti-analog giant dipole resonance."
                self.marker = 'v'    
            elif cal==15:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='J. Yasuda, T. Wakasa, M. Okamoto, et al., Prog. Theor. Exp. Phys 2013, 063D02 (2013).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Yasuda 2013'
                #: Attribute providing additional notes about the calculation.
                self.note = "anti-analog giant dipole resonance."
                self.marker = '^'    
            elif cal==16:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='C.M. Tarbert, D.P. Watts, D.I. Glazier, et al., PRL 112, 242502 (2014).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Tarbert 2014'
                #: Attribute providing additional notes about the calculation.
                self.note = "coherent π0 production."
                self.marker = '>'    
            elif cal==17:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='A. Tamii, P. von Neumann-Cosel, and I. Poltoratska, Eur. Phys. J. A. 50, 28 (2014).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Tamii 2014'
                #: Attribute providing additional notes about the calculation.
                self.note = "by ⃗p-scattering at 295 MeV."
                self.marker = '<'    
            elif cal==18:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='F.J. Fattoyev, J. Piekarewicz, and C.J. Horowitz, PRL 120, 172702 (2018).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Fattoyev 2018'
                #: Attribute providing additional notes about the calculation.
                self.note = "analysis of LIGO-Virgo (GW170817) data."
                self.marker = 'p' 
            elif cal==19:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='B.T. Reed, F.J. Fattoyev, C.J. Horowitz, and J. Piekarewicz, PRL 126, 172503 (2021).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Reed 2021'
                #: Attribute providing additional notes about the calculation.
                self.note = "analysis of NICER data."
                self.marker = 'h'    
            elif cal==20:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='S. Tagami, T. Wakasa, J. Matsui, et al., PRC 104, 024606 (2021).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Tagami 2021'
                #: Attribute providing additional notes about the calculation.
                self.note = "p+208Pb reaction cross section at 30 - 100 MeV."
                self.marker = 'H'    
            elif cal==21:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='D. Adhikari, H. Albataineh, D. Androic, et al., PRL 126, 172502 (2021).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Adhikari 2021'
                #: Attribute providing additional notes about the calculation.
                self.note = "PREX-2: parity violating e− scattering."
                self.marker = 'D'    
            elif cal==22:
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='G. Giacalone, G. Nijs, and W. van der Schee, PRL 131, 202302 (2023).'
                #: Attribute providing the label the data is references for figures.
                self.label = 'Giacalone 2023'
                #: Attribute providing additional notes about the calculation.
                self.note = "208Pb+208Pb at LHC."
                self.marker = 'x'                          
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
        # Helper function for safe conversion
        def safe_float(value):
            stripped_value = value.strip()
            return float(stripped_value) if stripped_value else None
        # 
        with open(file_in,'r') as file:
            for line in file:
                if '#' in line: continue
                ele = line.split(',')
                a = ele[0]
                # print('ele[0]:',ele[0],' cal:',cal,' ele[:]:',ele[:])
                if int(a) == cal:
                    self.nrad = safe_float(ele[1])
                    self.nrad_sig_up = safe_float(ele[2])
                    self.nrad_sig_do = safe_float(ele[3])
                    self.prad = safe_float(ele[4])
                    self.prad_sig_up = safe_float(ele[5])
                    self.prad_sig_do = safe_float(ele[6])
                    self.nskin = safe_float(ele[7])
                    self.nskin_sig_up = safe_float(ele[8])
                    self.nskin_sig_do = safe_float(ele[9])
                    self.latexCite = ele[10].replace('\n','').replace(' ','')
        #
        if nuda.env.verb: print("Exit SetupNeutronSkin()")
        #
    #
    def print_outputs( self ):
        """
        Method which print outputs on terminal's screen.
        """
        #
        if nuda.env.verb: print("Enter print_output()")
        #
        print("- Print output:")
        print("   source:  ",self.source)
        print("   cal:",self.cal)
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
        #
        if nuda.env.verb: print("Exit print_output()")
        #
    #
class setupNeutronSkinAverage():
    """
    Instantiate the experimental/analitical data for a given source and averaged over cal.

    This choice is defined in the variable `source`.

    `source` can chosen among the following ones: '48Ca'.

    :param source: Fix the name of `source`. Default value: '208Pb'.
    :type source: str, optional. 

    **Attributes:**
    """
    def __init__(self, source = '208Pb' ):
        #
        if nuda.env.verb: print("Enter setupNeutronSkinAverage()")
        #
        self.source = source
        self.latexCite = None
        self.ref = None
        self.label = source+' average'
        self.note = 'compute the centroid and standard deviation from the cal. data.'
        #
        cals = nskin_exp( source = source )
        # print('cals:',cals)
        #
        # search for the boundary for the neutron skin:
        nsmin = 0.5; nsmax = 0.0;
        for cal in cals:
            nskin = nuda.SetupNeutronSkinExp( source = source, cal = cal )
            #nskin.print_outputs( )
            nsdo = nskin.nskin - 0.5*nskin.nskin_sig_do
            nsup = nskin.nskin + 0.5*nskin.nskin_sig_up
            if nsdo < nsmin: nsmin = nsdo
            if nsup > nsmax: nsmax = nsup
        #print('nsmin:',nsmin)
        #print('nsmax:',nsmax)
        # construct the distribution of calervations in ay
        ax = np.linspace(nsmin,nsmax,300)
        #print('ax:',ax)
        ay = np.zeros(300)
        for cal in cals:
            nskin = nuda.SetupNeutronSkinExp( source = source, cal = cal )
            #nskin.print_outputs( )
            ay += gauss(ax,nskin.nskin,nskin.nskin_sig_up,nskin.nskin_sig_do)
        # determine the centroid and standard deviation from the distribution of cal. 
        nor = sum( ay )
        cen = sum( ay*ax )
        std = sum ( ay*ax**2 )
        self.nskin_cen = cen / nor
        self.sig_std = round( math.sqrt( std/nor - self.nskin_cen**2 ), 3 )
        self.nskin_cen = round( self.nskin_cen, 3)
        #print('nskin:',self.nskin_cen)
        #print('std:',self.sig_std)
        #
        if nuda.env.verb: print("Exit setupNeutronSkinAverage()")
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
            print("   nskin_cen:",self.nskin_cen)
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

def gauss( ax, nskin, sig_up, sig_do ):
    fac = math.sqrt( 2*math.pi )
    gauss = []
    for x in ax:
        if x < nskin: 
            z = ( x - nskin ) / sig_do
            norm = sig_do * fac
        else:
            z = ( x - nskin ) / sig_up
            norm = sig_up * fac
        gauss.append( math.exp( -0.5*z**2 ) / norm )
    return gauss

