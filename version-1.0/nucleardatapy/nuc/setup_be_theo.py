import os
import sys
import math
import numpy as np  # 1.15.0

import nucleardatapy as nuda

def delta_emp( N, Z, formula ):
    A = N + Z
    if formula == 'classic':
       return 12.0 / A**0.5
    elif formula == 'Vogel':
       return ( 7.2 - 44.0 * ( 1.0 - 2.0 * Z / A )**2 ) / A**0.3333
    else:
       print('setup_be_theo: formula is badly defined ',formula)
       print('setup_be_theo: exit')
       exit()

def be_theo_tables():
    """
    Return a list of the tables available in this toolkit for the masses 
    predicted by theoretical approaches and print them all on the prompt. 
    These tables are the following ones: \
    [ '1988-GK', '1988-MJ', '1995-DZ', '1995-ETFSI', '1995-FRDM', \
    '2005-KTUY', '2007-HFB14', '2010-WS*', '2010-HFB21', '2011-WS3', '2013-HFB22', \
    '2013-HFB23', '2013-HFB24', '2013-HFB25', '2013-HFB26', '2021-BSkG1', \
    '2022-BSkG2', '2023-BSkG3', '2025-BSkG4' ]

    :return: The list of tables.
    :rtype: list[str].
    """
    #
    if nuda.env.verb: print("\nEnter be_theo_tables()")
    #
    tables = [ '1988-GK', '1988-MJ', '1995-DZ', '1995-ETFSI', '1995-FRDM', \
       '2005-KTUY', '2007-HFB14', '2010-WS*', '2010-HFB21','2011-WS3', '2013-HFB22', \
    '2013-HFB23', '2013-HFB24', '2013-HFB25', '2013-HFB26', '2021-BSkG1', \
    '2022-BSkG2', '2023-BSkG3', '2025-BSkG4' ]
    #
    #print('theory tables available in the toolkit:',tables)
    tables_lower = [ item.lower() for item in tables ]
    #print('theory tables available in the toolkit:',tables_lower)
    #
    if nuda.env.verb: print("Exit be_theo_tables()")
    #
    return tables, tables_lower

def conversionMBE(M,N,Z):
  """
    Convert the mass excess of a nucleus to its binding energy.  
  """
  xmn=8.07132281           # Neutron mass - atomic unit
  xmh=7.28896940           # Proton mass + electron mass - atomic unit
  rydb=13.6056981e-6       # binding energy of a Hydrogen atom
  B = -M + N*xmn+Z*(xmh+rydb) - 0.0000144381*Z**2.39 - 1.55468e-12*Z**5.35
  return - B


class setupBETheo():
    """
    Instantiate the theory nuclear masses.

    This choice is defined in the variable `table`.

    `table` can chosen among the following ones: \
    [ '1988-GK', '1988-MJ', '1995-DZ', '1995-ETFSI', '1995-FRDM', \
    '2005-KTUY', '2007-HFB14', '2010-WS*', '2010-HFB21','2011-WS3', '2013-HFB26', '2021-BSkG1', \
    '2022-BSkG2', '2023-BSkG3', '2025-BSkG4' ]

    :param table: Fix the name of `table`. Default value: '1995-DZ'.
    :type table: str, optional. 

    **Attributes:**
    """
    def __init__(self, table = '1995-DZ' ):
        #
        if nuda.env.verb: print("Enter setupBETheo()")
        #
        tables, tables_lower = be_theo_tables()
        if table.lower() not in tables_lower:
            print('setup_be_theo: Table ',table,' is not in the list of tables.')
            print('setup_be_theo: list of tables:',tables)
            print('setup_be_theo: -- Exit the code --')
            exit()
        self.table = table
        if nuda.env.verb: print("table:",table)
        #
        self = setupBETheo.init_self( self )
        #
        if table.lower()=='1988-gk':
            #
            # read the Masson-Janecke theoretical mass table
            #
            file_in = nuda.param.path_data+'nuclei/masses/Theory/1988-GK.txt'
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'J. Jaenecke and P.J. Masson, At. Data and Nuc. Data Tables 39, 265 (1988).'
            self.note = "write here notes about this EOS."
            self.label = 'GK-1988'
            self.nucZr, self.nucNr, self.nucMass  = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.nucZ = np.array( [ int(ele) for ele in self.nucZr ] )
            self.nucN = np.array( [ int(ele) for ele in self.nucNr ] )
            self.nucA = self.nucZ + self.nucN
            #self.nucBE = self.nucBE2A * self.nucA
            self.nucBE = conversionMBE(self.nucMass,self.nucN,self.nucZ)
            self.nucBE2A = self.nucBE / self.nucA
            self.Zmax = int( max( self.nucZ ) )
            #
        elif table.lower()=='1988-mj':
            #
            # read the Masson-Janecke theoretical mass table
            #
            file_in = nuda.param.path_data+'nuclei/masses/Theory/1988-MJ.txt'
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'P.J. Masson and J. Jaenecke, At. Data and Nuc. Data Tables 39, 273 (1988).'
            self.note = "write here notes about this EOS."
            self.label = 'MJ-1988'
            self.nucZr, self.nucNr, self.nucMass  = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.nucZ = np.array( [ int(ele) for ele in self.nucZr ] )
            self.nucN = np.array( [ int(ele) for ele in self.nucNr ] )
            self.nucA = self.nucZ + self.nucN
            #self.nucBE = self.nucBE2A * self.nucA
            self.nucBE = conversionMBE(self.nucMass,self.nucN,self.nucZ)
            self.nucBE2A = self.nucBE / self.nucA
            self.Zmax = int( max( self.nucZ ) )
            #
        elif table.lower()=='1995-dz':
            #
            # read the Duflo-Zuker theoretical mass table
            #
            file_in = nuda.param.path_data+'nuclei/masses/Theory/1995-DZ.txt'
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'J. Duflo and A.P. Zuker, Phys. Rev. C 52, (1995)'
            self.note = "write here notes about this EOS."
            self.label = 'DZ-1995'
            self.nucZr, self.nucNr, self.nucMass  = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.nucZ = np.array( [ int(ele) for ele in self.nucZr ] )
            self.nucN = np.array( [ int(ele) for ele in self.nucNr ] )
            self.nucA = self.nucZ + self.nucN
            #self.nucBE = self.nucBE2A * self.nucA
            self.nucBE = conversionMBE(self.nucMass,self.nucN,self.nucZ)
            self.nucBE2A = self.nucBE / self.nucA
            self.Zmax = int( max( self.nucZ ) )
            #
        elif table.lower()=='1995-etfsi':
            #
            # read the ETFSI theoretical mass table
            #
            file_in = nuda.param.path_data+'nuclei/masses/Theory/1995-ETFSI.txt'
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'Y. Aboussir et al., At. Data and Nuc. Data Tables 61, 127 (1995).'
            self.note = "write here notes about this EOS."
            self.label = 'ETFSI-1995'
            self.nucZr, self.nucNr, self.nucMass  = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.nucZ = np.array( [ int(ele) for ele in self.nucZr ] )
            self.nucN = np.array( [ int(ele) for ele in self.nucNr ] )
            self.nucA = self.nucZ + self.nucN
            #self.nucBE = self.nucBE2A * self.nucA
            self.nucBE = conversionMBE(self.nucMass,self.nucN,self.nucZ)
            self.nucBE2A = self.nucBE / self.nucA
            self.Zmax = int( max( self.nucZ ) )
            #
        elif table.lower()=='1995-frdm':
            #
            # read the FRDM theoretical mass table
            #
            #file_in = nuda.param.path_data+'nuclei/masses/Theory/1995-FRDM.txt'
            file_in = nuda.param.path_data+'nuclei/masses/Theory/1995-FRDM.dat'
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'P. Moeller, J.R. Nix, W.D. Myers, W.J. Swiatecki, At. Data and Nuc. Data Tables 59, 185 (1995).'
            self.note = "write here notes about this EOS."
            self.label = 'FRDM-1995'
            self.nucZ = []; self.nucN = []; self.nucA = []; self.eps2 = []; self.eps3 = []; 
            self.eps4 = []; self.eps6 = []; self.eps6sym = []; self.beta2 = []; self.beta3 = []; 
            self.beta4 = []; self.beta6 = []; self.Emic = []; self.nucMass = []; self.Mexp = []; 
            self.Mexp_err = []; self.EmicFL = []; self.MthFL = [];
            with open(file_in,'r') as file:
                for line in file:
                    #print('line:',line)
                    if '#' in line: 
                        continue
                    #ele = line.split()
                    #print('ele:',ele)
                    #exit()
                    self.nucZ.append( int(line[0:5]) )
                    self.nucN.append( int(line[6:10]) )
                    self.nucA.append( int(line[11:16]) )
                    self.eps2.append( float(line[17:25]) )
                    if line[26:35] != ' '*9: self.eps3.append( float(line[26:35]) )
                    else: self.eps3.append( 0.0 )
                    self.eps4.append( float(line[36:45]) )
                    self.eps6.append( float(line[46:56]) )
                    if line[57:66] != ' '*9: self.eps6sym.append( float(line[57:66]) )
                    else: self.eps6sym.append( 0.0 )
                    self.beta2.append( float(line[67:76]) )
                    if line[77:86] != ' '*9: self.beta3.append( float(line[77:86]) )
                    else: self.beta3.append( 0.0 )
                    self.beta4.append( float(line[87:96]) )
                    self.beta6.append( float(line[97:106]) )
                    self.Emic.append( float(line[107:116]) )
                    self.nucMass.append( float(line[117:126]) )
                    if line[127:136] != ' '*9: self.Mexp.append( float(line[127:136]) )
                    else: self.Mexp.append( 0.0 )
                    if line[137:146] != ' '*9: self.Mexp_err.append( float(line[137:146]) )
                    else: self.Mexp_err.append( 0.0 )
                    self.EmicFL.append( float(line[147:156]) )
                    self.MthFL.append( float(line[157:166]) )
                    #print('N,Z:',self.nucN, self.nucZ)
            #self.nucZr, self.nucNr, self.nucAr, self.eps2, self.eps3, self.eps4, self.eps6, self.eps6sym, \
            #  self.beta2, self.beta3, self.beta4, self.beta6, self.Emic, self.Mth, self.Mexp, self.Mexp_err, \
            #  self.EmicFL, self.MthFL \
            #  = np.loadtxt( file_in, usecols=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17), delimiter='   ', unpack = True )
            #self.nucZ = np.array( [ int(ele) for ele in self.nucZr ] )
            #self.nucN = np.array( [ int(ele) for ele in self.nucNr ] )
            #self.nucA = self.nucZ + self.nucN
            self.nucA = np.array( self.nucA )
            self.nucN = np.array( self.nucN )
            self.nucZ = np.array( self.nucZ )
            self.nucMass = np.array( self.nucMass )
            #self.nucBE = self.Mth * self.nucA
            self.nucBE = conversionMBE(self.nucMass,self.nucN,self.nucZ)
            self.nucBE2A = self.nucBE / self.nucA
            #print('nucZ:',self.nucZ)
            self.Zmax = max( self.nucZ )
            #
        elif table.lower()=='2005-ktuy':
            #
            # read the KTUY theoretical mass table
            #
            file_in = nuda.param.path_data+'nuclei/masses/Theory/2005-KTUY.txt'
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'H. Koura, T. Tachibana, M. Uno, M. Yamada, Prog. Theor. Phys. 119, 305 (2005).'
            self.note = "write here notes about this EOS."
            self.label = 'KTUY-2005'
            self.nucZr, self.nucNr, self.nucMass  = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.nucZ = np.array( [ int(ele) for ele in self.nucZr ] )
            self.nucN = np.array( [ int(ele) for ele in self.nucNr ] )
            self.nucA = self.nucZ + self.nucN
            #self.nucBE = self.nucBE2A * self.nucA
            self.nucBE = conversionMBE(self.nucMass,self.nucN,self.nucZ)
            self.nucBE2A = self.nucBE / self.nucA
            self.Zmax = int( max( self.nucZ ) )
            #
        elif table.lower()=='2007-hfb14':
            #
            # read the HFB14 theoretical mass table
            #
            file_in = nuda.param.path_data+'nuclei/masses/Theory/2007-HFB14.txt'
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'S. Goriely, M. Samyn, J.M. Pearson, Phys. Rev. C 75, 064312 (2007).'
            self.note = "write here notes about this EOS."
            self.label = 'HFB14-2007'
            self.nucZr, self.nucNr, self.nucMass  = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.nucZ = np.array( [ int(ele) for ele in self.nucZr ] )
            self.nucN = np.array( [ int(ele) for ele in self.nucNr ] )
            self.nucA = self.nucZ + self.nucN
            #self.nucBE = self.nucBE2A * self.nucA
            self.nucBE = conversionMBE(self.nucMass,self.nucN,self.nucZ)
            self.nucBE2A = self.nucBE / self.nucA
            self.Zmax = int( max( self.nucZ ) )
            #
        elif table.lower()=='2010-hfb21':
            #
            # read the HFB21 theoretical mass table
            #
            #file_in = nuda.param.path_data+'nuclei/masses/Theory/2007-HFB14.txt'
            file_in = nuda.param.path_data+'nuclei/masses/Theory/2010-HFB21.dat'
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'S. Goriely, N. Chamel, and J. M. Pearson, Phys. Rev. C 82, 035804 (2010).'
            self.note = "write here notes about this EOS."
            self.label = 'HFB21-2010'
            self.nucZr, self.nucAr, self.beta2, self.beta4, self.Rch, self.Edef, self.Sn, self.Sp, \
               self.Qbet, self.nucMass, self.dif, self.Jexp, self.Jth, self.Pexp, self.Pth  = \
               np.loadtxt( file_in, usecols=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14), unpack = True )
            self.nucZ = np.array( [ int(ele) for ele in self.nucZr ] )
            self.nucA = np.array( [ int(ele) for ele in self.nucAr ] )
            self.nucN = self.nucA - self.nucZ
            #self.nucBE = self.Mcal * self.nucA
            self.nucBE = conversionMBE(self.nucMass,self.nucN,self.nucZ)
            self.nucBE2A = self.nucBE / self.nucA
            self.Zmax = int( max( self.nucZ ) )
            #
        elif table.lower()=='2010-ws*':
            #
            # read the WS3 theoretical mass table
            #
            file_in = nuda.param.path_data+'nuclei/masses/Theory/2010-WS3.txt'
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'N. Wang, Z. Liang, M. Liu, X. Wu, Phys. Rev. C 82, 044304 (2010).'
            self.note = "write here notes about this EOS."
            self.label = 'WS3-2010'
            self.nucZr, self.nucNr, self.nucMass  = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.nucZ = np.array( [ int(ele) for ele in self.nucZr ] )
            self.nucN = np.array( [ int(ele) for ele in self.nucNr ] )
            self.nucA = self.nucZ + self.nucN
            #self.nucBE = self.nucBE2A * self.nucA
            self.nucBE = conversionMBE(self.nucMass,self.nucN,self.nucZ)
            self.nucBE2A = self.nucBE / self.nucA
            self.Zmax = int( max( self.nucZ ) )
            #
        elif table.lower()=='2011-ws3':
            #
            # read the WS3 theoretical mass table
            #
            file_in = nuda.param.path_data+'nuclei/masses/Theory/2011-WS3.txt'
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'M. Liu, N. Wang, Y. Deng, X. Wu, Phys. Rev. C 84, 014333 (2011).'
            self.note = "write here notes about this EOS."
            self.label = 'WS3-2011'
            self.nucZr, self.nucNr, self.nucMass  = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.nucZ = np.array( [ int(ele) for ele in self.nucZr ] )
            self.nucN = np.array( [ int(ele) for ele in self.nucNr ] )
            self.nucA = self.nucZ + self.nucN
            #self.nucBE = self.nucBE2A * self.nucA
            self.nucBE = conversionMBE(self.nucMass,self.nucN,self.nucZ)
            self.nucBE2A = self.nucBE / self.nucA
            self.Zmax = int( max( self.nucZ ) )
            #
        elif table.lower()=='2013-hfb22':
            #
            # read the HFB22 theoretical mass table
            #
            file_in = nuda.param.path_data+'nuclei/masses/Theory/2013-HFB22.txt'
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'S. Goriely, N. Chamel, J.M. Pearson, Phys. Rev. C 88, 024308 (2013).'
            self.note = "write here notes about this EOS."
            self.label = 'HFB22-2013'
            self.nucZr, self.nucNr, self.nucMass  = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.nucZ = np.array( [ int(ele) for ele in self.nucZr ] )
            self.nucN = np.array( [ int(ele) for ele in self.nucNr ] )
            self.nucA = self.nucZ + self.nucN
            #self.nucBE = self.nucBE2A * self.nucA
            self.nucBE = conversionMBE(self.nucMass,self.nucN,self.nucZ)
            self.nucBE2A = self.nucBE / self.nucA
            self.Zmax = int( max( self.nucZ ) )
            #
        elif table.lower()=='2013-hfb23':
            #
            # read the HFB23 theoretical mass table
            #
            file_in = nuda.param.path_data+'nuclei/masses/Theory/2013-HFB23.txt'
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'S. Goriely, N. Chamel, J.M. Pearson, Phys. Rev. C 88, 024308 (2013).'
            self.note = "write here notes about this EOS."
            self.label = 'HFB23-2013'
            self.nucZr, self.nucNr, self.nucMass  = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.nucZ = np.array( [ int(ele) for ele in self.nucZr ] )
            self.nucN = np.array( [ int(ele) for ele in self.nucNr ] )
            self.nucA = self.nucZ + self.nucN
            #self.nucBE = self.nucBE2A * self.nucA
            self.nucBE = conversionMBE(self.nucMass,self.nucN,self.nucZ)
            self.nucBE2A = self.nucBE / self.nucA
            self.Zmax = int( max( self.nucZ ) )
            #
        elif table.lower()=='2013-hfb24':
            #
            # read the HFB24 theoretical mass table
            #
            file_in = nuda.param.path_data+'nuclei/masses/Theory/2013-HFB24.txt'
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'S. Goriely, N. Chamel, J.M. Pearson, Phys. Rev. C 88, 024308 (2013).'
            self.note = "write here notes about this EOS."
            self.label = 'HFB24-2013'
            self.nucZr, self.nucNr, self.nucMass  = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.nucZ = np.array( [ int(ele) for ele in self.nucZr ] )
            self.nucN = np.array( [ int(ele) for ele in self.nucNr ] )
            self.nucA = self.nucZ + self.nucN
            #self.nucBE = self.nucBE2A * self.nucA
            self.nucBE = conversionMBE(self.nucMass,self.nucN,self.nucZ)
            self.nucBE2A = self.nucBE / self.nucA
            self.Zmax = int( max( self.nucZ ) )
            #
        elif table.lower()=='2013-hfb25':
            #
            # read the HFB25 theoretical mass table
            #
            file_in = nuda.param.path_data+'nuclei/masses/Theory/2013-HFB25.txt'
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'S. Goriely, N. Chamel, J.M. Pearson, Phys. Rev. C 88, 024308 (2013).'
            self.note = "write here notes about this EOS."
            self.label = 'HFB25-2013'
            self.nucZr, self.nucNr, self.nucMass  = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.nucZ = np.array( [ int(ele) for ele in self.nucZr ] )
            self.nucN = np.array( [ int(ele) for ele in self.nucNr ] )
            self.nucA = self.nucZ + self.nucN
            #self.nucBE = self.nucBE2A * self.nucA
            self.nucBE = conversionMBE(self.nucMass,self.nucN,self.nucZ)
            self.nucBE2A = self.nucBE / self.nucA
            self.Zmax = int( max( self.nucZ ) )
            #
        elif table.lower()=='2013-hfb26':
            #
            # read the HFB14 theoretical mass table
            #
            file_in = nuda.param.path_data+'nuclei/masses/Theory/2013-HFB26.txt'
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'S. Goriely, N. Chamel, J.M. Pearson, Phys. Rev. C 88, 024308 (2013).'
            self.note = "write here notes about this EOS."
            self.label = 'HFB26-2013'
            self.nucZr, self.nucNr, self.nucMass  = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.nucZ = np.array( [ int(ele) for ele in self.nucZr ] )
            self.nucN = np.array( [ int(ele) for ele in self.nucNr ] )
            self.nucA = self.nucZ + self.nucN
            #self.nucBE = self.nucBE2A * self.nucA
            self.nucBE = conversionMBE(self.nucMass,self.nucN,self.nucZ)
            self.nucBE2A = self.nucBE / self.nucA
            self.Zmax = int( max( self.nucZ ) )
            #
        elif table.lower()=='2021-bskg1':
            #
            # read the BSkG1 theoretical mass table
            #
            file_in = nuda.param.path_data+'nuclei/masses/Theory/2021-BSkG1.txt'
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'G. Scamps, S. Goriely, E. Olsen, M. Bender, and W. Ryssens, EPJA 57, 333 (2021).'
            self.note = "write here notes about this EOS."
            self.label = 'BSkG1-2021'
            #self.nucZr, self.nucNr, self.nucBE2A  = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.nucZr, self.nucNr, self.nucMass, self.Ebind, self.beta20, self.beta22, self.beta2, self.Erot, \
            self.gap_n, self.gap_p, self.moi = \
            np.loadtxt( file_in, usecols=(0,1,3,5,6,7,8,9,10,11,15), unpack = True )
            self.nucZ = np.array( [ int(ele) for ele in self.nucZr ] )
            self.nucN = np.array( [ int(ele) for ele in self.nucNr ] )
            self.nucA = self.nucZ + self.nucN
            #self.nucBE = self.nucBE2A * self.nucA
            self.nucBE = conversionMBE(self.nucMass,self.nucN,self.nucZ)
            self.nucBE2A = self.nucBE / self.nucA
            self.Zmax = int( max( self.nucZ ) )
            #
        elif table.lower()=='2022-bskg2':
            #
            # read the BSkG2 theoretical mass table
            #
            file_in = nuda.param.path_data+'nuclei/masses/Theory/2022-BSkG2.txt'
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'W. Ryssens, G. Scamps, S. Goriely, and M. Bender, EPJA 58, 246 (2022).'
            self.note = "write here notes about this EOS."
            self.label = 'BSkG2-2022'
            #self.nucZr, self.nucNr, self.nucBE2A  = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.nucZr, self.nucNr, self.nucMass, self.Ebind, self.beta20, self.beta22, self.beta2, self.Erot, \
            self.gap_n, self.gap_p, self.moi = \
            np.loadtxt( file_in, usecols=(0,1,3,5,6,7,8,9,10,11,15), unpack = True )
            self.nucZ = np.array( [ int(ele) for ele in self.nucZr ] )
            self.nucN = np.array( [ int(ele) for ele in self.nucNr ] )
            self.nucA = self.nucZ + self.nucN
            #self.nucBE = self.nucBE2A * self.nucA
            self.nucBE = conversionMBE(self.nucMass,self.nucN,self.nucZ)
            self.nucBE2A = self.nucBE / self.nucA
            self.Zmax = int( max( self.nucZ ) )
            #
        elif table.lower()=='2023-bskg3':
            #
            # read the BSkG3 theoretical mass table
            #
            file_in = nuda.param.path_data+'nuclei/masses/Theory/2023-BSkG3.txt'
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'G. Grams, W. Ryssens, G. Scamps, S. Goriely, and N. Chamel, EPJA 59, 270 (2023).'
            self.note = "write here notes about this EOS."
            self.label = 'BSkG3-2023'
            #self.nucZr, self.nucNr, self.nucBE2A  = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.nucZr, self.nucNr, self.nucMass, self.Ebind, self.beta20, self.beta22, self.beta2, \
            self.beta30, self.beta32, self.Erot, self.gap_n, self.gap_p, self.moi = \
            np.loadtxt( file_in, usecols=(0,1,3,5,6,7,8,9,10,11,12,13,17), unpack = True )
            self.nucZ = np.array( [ int(ele) for ele in self.nucZr ] )
            self.nucN = np.array( [ int(ele) for ele in self.nucNr ] )
            self.nucA = self.nucZ + self.nucN
            #self.nucBE = self.nucBE2A * self.nucA
            self.nucBE = conversionMBE(self.nucMass,self.nucN,self.nucZ)
            self.nucBE2A = self.nucBE / self.nucA
            self.Zmax = int( max( self.nucZ ) )
            #
        elif table.lower()=='2025-bskg4':
            #
            # read the BSkG4 theoretical mass table
            #
            file_in = nuda.param.path_data+'nuclei/masses/Theory/2025-BSkG4.txt'
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'G. Grams, W. Ryssens, N. Shchechilin, A. Sanchez-Fernandez, N. Chamel, and S. Goriely,  EPJA 61, 35 (2025).'
            self.note = "write here notes about this EOS."
            self.label = 'BSkG4-2024'
            #self.nucZr, self.nucNr, self.nucBE2A  = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.nucZr, self.nucNr, self.nucMass, self.Ebind, self.beta20, self.beta22, self.beta2, \
            self.beta30, self.beta32, self.Erot, self.gap_n, self.gap_p, self.moi = \
            np.loadtxt( file_in, usecols=(0,1,3,5,6,7,8,9,10,11,12,13,17), unpack = True )
            self.nucZ = np.array( [ int(ele) for ele in self.nucZr ] )
            self.nucN = np.array( [ int(ele) for ele in self.nucNr ] )
            self.nucA = self.nucZ + self.nucN
            #self.nucBE = self.nucBE2A * self.nucA
            self.nucBE = conversionMBE(self.nucMass,self.nucN,self.nucZ)
            self.nucBE2A = self.nucBE / self.nucA
            self.Zmax = int( max( self.nucZ ) )
            #
        self.nucI = ( self.nucN - self.nucZ ) / self.nucA
        #
        if nuda.env.verb: print("Exit setupBETheo()")
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
        print("   table:  ",self.table)
        print("   ref:    ",self.ref)
        print("   label:  ",self.label)
        print("   note:   ",self.note)
        if self.Zmax is not None: print(f"   Zmax: {self.Zmax}")
        if self.nucZ is not None: print(f"   Z: {self.nucZ[0:-1:10]}")
        if self.nucA is not None: print(f"   A: {self.nucA[0:-1:10]}")
        #
        if nuda.env.verb: print("Exit print_outputs()")
        #
    def isotopes(self, Zref = 50 ):
        """
        Method which find the first and last isotopes for Z=Zref.

        :param Zref: Fix the charge for the search of isotopes.
        :type Zref: int, optional. Default: 50.

        **Attributes:**
        """
        #
        if nuda.env.verb: print("Enter isotopes()")
        #
        if Zref < 0:
            print('setup_be_exp.py: issue with the function isotopes.')
            print('setup_be_exp.py: Bad definition for Zref')
            print('setup_be_exp.py: It is expected that Zref>0')
            print('setup_be_exp.py: Zref:',Zref)
            print('setup_be_exp.py: exit')
            exit()
        #
        Nstable, Zstable = nuda.nuc.stable_fit_Z( Zmin = Zref, Zmax = Zref )
        #
        nucNmin = Nstable[0]
        nucNmax = Nstable[0]
        #
        for ind,A in enumerate(self.nucA):
            if self.nucZ[ind] == Zref and self.nucN[ind] < nucNmin:
                nucNmin = self.nucN[ind]
            if self.nucZ[ind] == Zref and self.nucN[ind] > nucNmax:
                nucNmax = self.nucN[ind]
        self.itp_nucZ = Zref
        self.itp_nucNmin = nucNmin
        self.itp_nucNmax = nucNmax
        #
        if nuda.env.verb: print("Exit isotopes()")
        #
        return self
        #
    def isotones(self, Nref = 50 ):
        """
        Method which find the first and last isotones for N=Nref.

        :param Nref: Fix the neutron number for the search of isotones.
        :type Nref: int, optional. Default: 50.

        **Attributes:**
        """
        #
        if nuda.env.verb: print("Enter isotones()")
        #
        if Nref < 0:
            print('setup_be_exp.py: issue with the function isotones.')
            print('setup_be_exp.py: Bad definition for Nref')
            print('setup_be_exp.py: It is expected that Nref>0')
            print('setup_be_exp.py: Nref:',Nref)
            print('setup_be_exp.py: exit')
            exit()
        #
        Nstable, Zstable = nuda.nuc.stable_fit_N( Nmin = Nref, Nmax = Nref )
        #
        nucZmin = Zstable[0]
        nucZmax = Zstable[0]
        #
        for ind,A in enumerate(self.nucA):
            if self.nucN[ind] == Nref and self.nucZ[ind] < nucZmin:
                nucZmin = self.nucZ[ind]
            if self.nucN[ind] == Nref and self.nucZ[ind] > nucZmax:
                nucZmax = self.nucZ[ind]
        self.itn_nucN = Nref
        self.itn_nucZmin = nucZmin
        self.itn_nucZmax = nucZmax
        #
        if nuda.env.verb: print("Exit isotones()")
        #
        return self
        #
    def S2n( self, Zref = 50 ):
        """
        Compute the two-neutron separation energy (S2n)
        S2n = E(Z,N)-E(Z,N-2)
        """
        #
        if nuda.env.verb: print("Enter S2n()")
        #
        if Zref < 0:
            print('setup_be_theo: In S2n attribute function of setup_be_theo.py:')
            print('setup_be_theo: Bad definition of Zref')
            print('setup_be_theo: It is expected that Zref>=0')
            print('setup_be_theo: Zref:',Zref)
            print('setup_be_theo: exit')
            exit()
        #
        S2n_N = []
        S2n_E = []
        #
        Nmin=self.itp_nucNmin
        Nmax=self.itp_nucNmax
        #
        for N in range(Nmin+2,Nmax+1):
            #
            flagN = False; flagNm2 = False;
            #
            for ind,Z in enumerate(self.nucZ):
                #
                if Z == Zref and self.nucN[ind] == N:
                    indN = ind
                    flagN = True
                if Z == Zref and self.nucN[ind] == N-2:
                    indNm2 = ind
                    flagNm2 = True
                    #
            if flagN and flagNm2:
                S2n_N.append( N )
                S2n_E.append( self.nucBE[indN] - self.nucBE[indNm2] )
        self.S2n_N = np.array( S2n_N, dtype = int )
        self.S2n_E = np.array( S2n_E, dtype = float )
        #
        if nuda.env.verb: print("Exit S2n()")
        #
        return self
        #
    def S2p( self, Nref = 50 ):
        """
        Compute the two-proton separation energy (S2p)
        S2p(Z,Nref) = E(Z,Nref)-E(Z-2,Nref)
        """
        #
        if nuda.env.verb: print("Enter S2p()")
        #
        if Nref < 0:
            print('setup_be_exp.py: In S2p attribute function of setup_be_exp.py:')
            print('setup_be_exp.py: Bad definition of Nref')
            print('setup_be_exp.py: It is expected that Nref>=0')
            print('setup_be_exp.py: Nref:',Nref)
            print('setup_be_exp.py: exit')
            exit()
        #
        S2p_Z = []
        S2p_E = []
        #
        Zmin=self.itn_nucZmin
        Zmax=self.itn_nucZmax
        #
        for Z in range(Zmin+2,Zmax+1):
            #
            flagZ = False; flagZm2 = False;
            #
            for ind,N in enumerate(self.nucN):
                #
                if N == Nref and self.nucZ[ind] == Z:
                    indZ = ind
                    flagZ = True
                if N == Nref and self.nucZ[ind] == Z-2:
                    indZm2 = ind
                    flagZm2 = True
                    #
            if flagZ and flagZm2:
                S2p_Z.append( Z )
                S2p_E.append( self.nucBE[indZ] - self.nucBE[indZm2] )
        self.S2p_Z = np.array( S2p_Z, dtype = int )
        self.S2p_E = np.array( S2p_E, dtype = float )
        #
        if nuda.env.verb: print("Exit S2p()")
        #
        return self
        #
    def drip_S2n(self, Zmin = 1, Zmax = 95 ):
        """
        Method which find the drip-line nuclei from S2n (neutron side).

        :param Zmin: Fix the minimum charge for the search of the neutron drip line.
        :type Zmin: int, optional. Default: 1.
        :param Zmax: Fix the maximum charge for the search of the neutron drip line.
        :type Zmax: int, optional. Default: 95.

        **Attributes:**
        """
        #
        if nuda.env.verb: print("Enter drip_S2n()")
        #
        if Zmin > Zmax:
            print('setup_be_theo: In drip_S2n attribute function of setup_be_theo.py:')
            print('setup_be_theo: Bad definition of Zmin and Zmax')
            print('setup_be_theo: It is expected that Zmin<=Zmax')
            print('setup_be_theo: Zmin,Zmax:',Zmin,Zmax)
            print('setup_be_theo: exit')
            exit()
        #
        if not any(self.S2n_Z):
            print('setup_be_theo: In drip_S2n attribute function of setup_be_theo.py:')
            print('setup_be_theo: Should compute first S2n')
            print('setup_be_theo: exit')
            exit()
        #
        #Nstable, Zstable = stable_fit( Zmin = Zmin, Zmax = Zmax )
        #
        self.drip_S2n_Z = []
        self.drip_S2n_N = []
        #
        for ind,Z in enumerate(self.S2n_Z):
            #
            if Z > Zmax :
                break
            if Z < Zmin :
                continue
            #
            #Nmax = Nstable[ind]
            Nmax = 0
            #
            for ind2,Z2 in enumerate(self.S2n_Z):
                if Z2 == Z and self.S2n_N[ind2] > Nmax and self.S2n[ind2] > 0.0:
                    Nmax = self.S2n_N[ind2]
            self.drip_S2n_Z.append( Z )
            self.drip_S2n_N.append( Nmax )
        #
        if nuda.env.verb: print("Exit drip_S2n()")
        #
        return self
        #
    #
    def drip_S2p(self, Nmin = 1, Nmax = 95 ):
        """
        Method which find the drip-line nuclei from S2p (proton side).

        :param Nmin: Fix the minimum neutron number for the search of the proton drip line.
        :type Nmin: int, optional. Default: 1.
        :param Nmax: Fix the maximum neutron number for the search of the proton drip line.
        :type Nmax: int, optional. Default: 95.

        **Attributes:**
        """
        #
        if nuda.env.verb: print("Enter drip_S2p()")
        #
        if Nmin > Nmax:
            print('setup_be_theo: In drip_S2p attribute function of setup_be_theo.py:')
            print('setup_be_theo: Bad definition of Nmin and Nmax')
            print('setup_be_theo: It is expected that Nmin<=Nmax')
            print('setup_be_theo: Nmin,Nmax:',Nmin,Nmax)
            print('setup_be_theo: exit')
            exit()
        #
        if not any(self.S2p_N):
            print('setup_be_theo: In drip_S2p attribute function of setup_be_theo.py:')
            print('setup_be_theo: Should compute first S2p')
            print('setup_be_theo: exit')
            exit()
        #
        self.drip_S2p_Z = []
        self.drip_S2p_N = []
        #
        for ind,N in enumerate(self.S2p_N):
            #
            if N > Nmax :
                break
            if N < Nmin :
                continue
            #
            Zmax = 0
            #
            for ind2,N2 in enumerate(self.S2p_N):
                if N2 == N and self.S2p_Z[ind2] > Zmax and self.S2p[ind2] > 0.0:
                    Zmax = self.S2p_Z[ind2]
            self.drip_S2p_N.append( N )
            self.drip_S2p_Z.append( Zmax )
        #
        if nuda.env.verb: print("Exit drip_S2p()")
        #
        return self
        #
    def D3n( self, Zref = 50 ):
        """
        Compute the three-points odd-even mass staggering (D3n)
        D3n = (-)**N * ( 2*E(Z,N)-E(Z,N+1)-E(Z,N-1) ) / 2
        """
        #
        if nuda.env.verb: print("Enter D3n()")
        #
        if Zref < 0:
            print('setup_be_theo: In D3n attribute function of setup_be_theo.py:')
            print('setup_be_theo: Bad definition of Zref')
            print('setup_be_theo: It is expected that Zref>=0')
            print('setup_be_theo: Zref:',Zref)
            print('setup_be_theo: exit')
            exit()
        #
        D3n_N_even = []
        D3n_E_even = []
        D3n_N_odd = []
        D3n_E_odd = []
        #
        Nmin=self.itp_nucNmin
        Nmax=self.itp_nucNmax
        #
        for N in range(Nmin+1,Nmax+1):
            #
            flagN = False; flagNm1 = False; flagNp1 = False;
            #
            for ind,Z in enumerate(self.nucZ):
                #
                if Z == Zref and self.nucN[ind] == N:
                    indN = ind
                    flagN = True
                    if N % 2:
                        sign = -1.0 # odd
                    else:
                        sign = 1.0 # even
                if Z == Zref and self.nucN[ind] == N-1:
                    indNm1 = ind
                    flagNm1 = True
                if Z == Zref and self.nucN[ind] == N+1:
                    indNp1 = ind
                    flagNp1 = True
                    #
            if flagN and flagNm1 and flagNp1:
                if sign > 0.0: #even
                    D3n_N_even.append( N )
                    D3n_E_even.append( sign/2.0*( -2*self.nucBE[indN] + self.nucBE[indNm1] + self.nucBE[indNp1] ) )
                else:
                    D3n_N_odd.append( N )
                    D3n_E_odd.append( sign/2.0*( -2*self.nucBE[indN] + self.nucBE[indNm1] + self.nucBE[indNp1] ) )
        self.D3n_N_even = np.array( D3n_N_even, dtype = int )
        self.D3n_E_even = np.array( D3n_E_even, dtype = float )
        self.D3n_N_odd = np.array( D3n_N_odd, dtype = int )
        self.D3n_E_odd = np.array( D3n_E_odd, dtype = float )
        #
        if nuda.env.verb: print("Exit D3n()")
        #
        return self
        #
    def D3p( self, Nref = 50 ):
        """
        Compute the three-points odd-even mass staggering (D3n)
        D3p = (-)**Z * ( 2*E(Z,N)-E(Z+1,N)-E(Z-1,N) ) / 2
        """
        #
        if nuda.env.verb: print("Enter D3p()")
        #
        if Nref < 0:
            print('setup_be_theo: In D3p attribute function of setup_be_theo.py:')
            print('setup_be_theo: Bad definition of Nref')
            print('setup_be_theo: It is expected that Nref>=0')
            print('setup_be_theo: Nref:',Nref)
            print('setup_be_theo: exit')
            exit()
        #
        D3p_Z_even = []
        D3p_E_even = []
        D3p_Z_odd = []
        D3p_E_odd = []
        #
        Zmin=self.itn_nucZmin
        Zmax=self.itn_nucZmax
        #
        for Z in range(Zmin+1,Zmax+1):
            #
            flagZ = False; flagZm1 = False; flagZp1 = False;
            #
            for ind,N in enumerate(self.nucN):
                #
                if N == Nref and self.nucZ[ind] == Z:
                    indZ = ind
                    flagZ = True
                    if Z % 2:
                        sign = -1.0 # odd
                    else:
                        sign = 1.0 # even
                if N == Nref and self.nucZ[ind] == Z-1:
                    indZm1 = ind
                    flagZm1 = True
                if N == Nref and self.nucZ[ind] == Z+1:
                    indZp1 = ind
                    flagZp1 = True
                    #
            if flagZ and flagZm1 and flagZp1:
                if sign > 0.0: #even
                    D3p_Z_even.append( Z )
                    D3p_E_even.append( sign/2.0*( -2*self.nucBE[indZ] + self.nucBE[indZm1] + self.nucBE[indZp1] ) )
                else:
                    D3p_Z_odd.append( Z )
                    D3p_E_odd.append( sign/2.0*( -2*self.nucBE[indZ] + self.nucBE[indZm1] + self.nucBE[indZp1] ) )
        self.D3p_Z_even = np.array( D3p_Z_even, dtype = int )
        self.D3p_E_even = np.array( D3p_E_even, dtype = float )
        self.D3p_Z_odd = np.array( D3p_Z_odd, dtype = int )
        self.D3p_E_odd = np.array( D3p_E_odd, dtype = float )
        #
        if nuda.env.verb: print("Exit D3p()")
        #
        return self
        #
    def D3n_old( self, Zmin = 1, Zmax = 95 ):
        """
        Compute the three-points odd-even mass staggering (D3n)
        D3N = (-)**N * ( 2*E(Z,N)-E(Z,N+1)-E(Z,N-1) ) / 2
        """
        #
        if nuda.env.verb: print("Enter D3n()")
        #
        if Zmin > Zmax:
            print('setup_be_theo: In D3n attribute function of setup_be_exp.py:')
            print('setup_be_theo: Bad definition of Zmin and Zmax')
            print('setup_be_theo: It is expected that Zmin<=Zmax')
            print('setup_be_theo: Zmin,Zmax:',Zmin,Zmax)
            print('setup_be_theo: exit')
            exit()
        #
        D3n_Z_even = []
        D3n_Z_odd = []
        D3n_N_even = []
        D3n_N_odd = []
        D3n_even = []
        D3n_odd = []
        #
        for ind,Z in enumerate(self.nucZ):
            #
            if Z > Zmax :
                continue
            if Z < Zmin :
                continue
            #
            N = self.nucN[ind]
            #
            if N % 2 == 0:
                sign = 1.0 #even
            else:
                sign = -1.0 # odd
            #
            #print('For Z,N:',Z,N)
            #
            # search index for Z,N+2
            #
            flag_find1 = 0
            for ind1,Z1 in enumerate(self.nucZ):
                if Z == Z1 and self.nucN[ind1] == N+1:
                    flag_find1 = 1
                    break
            flag_find2 = 0
            for ind2,Z2 in enumerate(self.nucZ):
                if Z == Z2 and self.nucN[ind2] == N-1:
                    flag_find2 = 1
                    break
            if flag_find1*flag_find2 == 1: 
                if sign > 0: #even
                    D3n_Z_even.append( self.nucZ[ind] )
                    D3n_N_even.append( self.nucN[ind] )
                    D3n_even.append( sign/2.0*( -2*self.nucBE[ind] + self.nucBE[ind1] + self.nucBE[ind2] ) )
                else:
                    D3n_Z_odd.append( self.nucZ[ind] )
                    D3n_N_odd.append( self.nucN[ind] )
                    D3n_odd.append( sign/2.0*( -2*self.nucBE[ind] + self.nucBE[ind1] + self.nucBE[ind2] ) )
        self.D3n_N_even = np.array( D3n_N_even, dtype = int )
        self.D3n_N_odd  = np.array( D3n_N_odd,  dtype = int )
        self.D3n_Z_even = np.array( D3n_Z_even, dtype = int )
        self.D3n_Z_odd  = np.array( D3n_Z_odd,  dtype = int )
        self.D3n_even   = np.array( D3n_even,   dtype = float )
        self.D3n_odd    = np.array( D3n_odd,    dtype = float )            
        #
        if nuda.env.verb: print("Exit D3n()")
        #
        return self
    #
    def D3p_old( self, Nmin = 1, Nmax = 95 ):
        """
        Compute the three-points odd-even mass staggering (D3p)
        D3Z = (-)**Z * ( 2*E(Z,N)-E(Z+1,N)-E(Z-1,N) ) / 2
        """
        #
        if nuda.env.verb: print("Enter D3p()")
        #
        if Nmin > Nmax:
            print('setup_be_theo: In D3p attribute function of setup_be_exp.py:')
            print('setup_be_theo: Bad definition of Nmin and Nmax')
            print('setup_be_theo: It is expected that Nmin<=Nmax')
            print('setup_be_theo: Nmin,Nmax:',Nmin,Nmax)
            print('setup_be_theo: exit')
            exit()
        #
        D3p_Z_even = []
        D3p_Z_odd = []
        D3p_N_even = []
        D3p_N_odd = []
        D3p_even = []
        D3p_odd = []
        #
        for ind,N in enumerate(self.nucN):
            #
            if N > Nmax :
                continue
            if N < Nmin :
                continue
            #
            Z = self.nucZ[ind]
            #
            if Z % 2 == 0:
                sign = 1.0 #even
            else:
                sign = -1.0 # odd
            #
            #print('For Z,N:',Z,N)
            #
            # search index for Z,N+2
            #
            flag_find1 = 0
            for ind1,N1 in enumerate(self.nucN):
                if N == N1 and self.nucZ[ind1] == Z+1:
                    flag_find1 = 1
                    break
            flag_find2 = 0
            for ind2,N2 in enumerate(self.nucN):
                if N == N2 and self.nucZ[ind2] == Z-1:
                    flag_find2 = 1
                    break
            if flag_find1*flag_find2 == 1: 
                if sign > 0: #even
                    D3p_Z_even.append( self.nucZ[ind] )
                    D3p_N_even.append( self.nucN[ind] )
                    D3p_even.append( sign/2.0*( -2*self.nucBE[ind] + self.nucBE[ind1] + self.nucBE[ind2] ) )
                else:
                    D3p_Z_odd.append( self.nucZ[ind] )
                    D3p_N_odd.append( self.nucN[ind] )
                    D3p_odd.append( sign/2.0*( -2*self.nucBE[ind] + self.nucBE[ind1] + self.nucBE[ind2] ) )
        self.D3p_N_even = np.array( D3p_N_even, dtype = int )
        self.D3p_N_odd  = np.array( D3p_N_odd,  dtype = int )
        self.D3p_Z_even = np.array( D3p_Z_even, dtype = int )
        self.D3p_Z_odd  = np.array( D3p_Z_odd,  dtype = int )
        self.D3p_even   = np.array( D3p_even,   dtype = float )
        self.D3p_odd    = np.array( D3p_odd,    dtype = float )            
        #
        if nuda.env.verb: print("Exit D3p()")
        #
        return self
    #
    def diff(self, table, Zref = 50 ):
        """
        Method calculates the difference between a given mass 
        model and table_ref.

        :param table: Fix the table to analyze.
        :type table: str.
        :param Zref: Fix the isotopic chain to study.
        :type Zref: int, optional. Default: 50.

        **Attributes:**
        """
        #
        if nuda.env.verb: print("Enter diff()")
        #
        if self.table == table:
            print('setup_be_theo: we have self.table = table')
            print('setup_be_theo: self.table:',self.table)
            print('setup_be_theo: table:',table)
            print('setup_be_theo: exit()')
            exit()
        #
        # table_ref
        #
        BE_ref = []
        N_ref = []
        A_ref = []
        for k in range(len(self.nucZ)):
            if int( self.nucZ[k] ) == Zref:
                BE_ref.append( self.nucBE[k] )
                N_ref.append( self.nucN[k] )
                A_ref.append( self.nucA[k] )
        N_ref = np.array( N_ref )
        #print('N_ref:',N_ref)
        #
        # table
        #
        mod = nuda.setupBETheo( table = table )
        BE_mod = []
        N_mod = []
        A_mod = []
        for k in range(len(mod.nucZ)):
            if int( mod.nucZ[k] ) == Zref:
                BE_mod.append( mod.nucBE[k] )
                N_mod.append( mod.nucN[k] )
                A_mod.append( mod.nucA[k] )
        N_mod = np.array( N_mod )
        print('N_ref:',N_ref)
        print('N_mod:',N_mod)
        N_min = max( N_ref[0], N_mod[0] )
        print('N_min:',N_min)
        N_max = min( N_ref[-1], N_mod[-1] )
        print('N_max:',N_max)
        k_ref_min, = np.where( N_ref[:] == N_min )[0]
        print('k_ref_min:',k_ref_min)
        k_mod_min, = np.where( N_mod[:] == N_min )[0]
        print('k_mod_min:',k_mod_min)
        #
        # diff
        #
        N_diff = []
        A_diff = []
        BE_diff = []
        print('k goes from 0 to ',N_max-N_min+1)
        print('Last elements of:')
        #print('ref:',N_ref[k_ref_min+N_max-N_min])
        #print('mod:',N_mod[k_mod_min+N_max-N_min-1])
        for k in range(N_max-N_min+1):
            k_ref = k_ref_min + k
            k_mod = k_mod_min + k
            print('k,k_ref,k_mod,N_ref,N_mod:',k,k_ref,k_mod,N_ref[k_ref],N_mod[k_mod])
            if N_ref[k_ref] > N_mod[k_mod]:
                k_ref_min -= 1
                continue
            elif N_mod[k_mod] > N_ref[k_ref]:
                k_mod_min -= 1
                continue
            elif N_ref[k_ref] == N_mod[k_mod]:
                N_diff.append( int( N_mod[k_mod] ) )
                A_diff.append( int( A_mod[k_mod] ) )
                BE_diff.append( BE_mod[k_mod]-BE_ref[k_ref] )
            else:
                print('impossible case')
                print('Exit()')
                exit()
        #print('N_diff:',N_diff)
        N_diff = np.array( N_diff )
        A_diff = np.array( A_diff )
        BE_diff = np.array( BE_diff )
        BE2A_diff = BE_diff / A_diff
        #
        if nuda.env.verb: print("Exit diff()")
        #
        return N_diff, A_diff, BE_diff, BE2A_diff
        #
    def diff_exp(self, table_exp, version_exp, Zref = 50 ):
        """
        Method calculates the difference between a given experimental 
        mass (identified by `table_exp` and `version_exp`) and table_ref.

        :param table: Fix the table to analyze.
        :type table: str.
        :param Zref: Fix the isotopic chain to study.
        :type Zref: int, optional. Default: 50.

        **Attributes:**
        """
        #
        if nuda.env.verb: print("Enter diff()")
        #
        if self.table == table_exp:
            print('setup_be_theo: we have self.table = table_exp')
            print('setup_be_theo: self.table:',self.table)
            print('setup_be_theo: table:',table_exp)
            print('setup_be_theo: exit()')
            exit()
        #
        # table_ref
        #
        BE_ref = []
        N_ref = []
        A_ref = []
        for k in range(len(self.nucZ)):
            if int( self.nucZ[k] ) == Zref:
                BE_ref.append( self.nucBE[k] )
                N_ref.append( self.nucN[k] )
                A_ref.append( self.nucA[k] )
        N_ref = np.array( N_ref )
        #print('N_ref:',N_ref)
        #
        # table
        #
        exp = nuda.setupBEExp( table = table_exp, version = version_exp )
        exp2 = exp.select( state= 'gs', interp = 'n', nucleus = 'unstable' )
        BE_exp = []
        N_exp = []
        A_exp = []
        for k in range(len(exp2.sel_nucZ)):
            if int( exp2.sel_nucZ[k] ) == Zref:
                BE_exp.append( exp2.sel_nucBE[k] )
                N_exp.append( exp2.sel_nucN[k] )
                A_exp.append( exp2.sel_nucA[k] )
                #print('N,Z(exp),I:',N_exp[-1],A_exp[-1]-N_exp[-1],exp2.sel_flagI[k])
        N_exp = np.array( N_exp )
        N_min = max( N_ref[0], N_exp[0] )
        N_max = min( N_ref[-1], N_exp[-1] )
        k_ref_min, = np.where( N_ref == N_min )[0]
        k_exp_min, = np.where( N_exp == N_min )[0]
        #
        # diff
        #
        N_diff = []
        A_diff = []
        BE_diff = []
        for k in range(N_max-N_min+1):
            k_ref = k_ref_min + k
            k_exp = k_exp_min + k
            #print('k,k_ref,k_exp,N_ref,N_exp:',k,k_ref,k_exp,N_ref[k_ref],N_exp[k_exp])
            if N_ref[k_ref] > N_exp[k_exp]:
                k_ref_min -= 1
                continue
            elif N_exp[k_exp] > N_ref[k_ref]:
                k_exp_min -= 1
                continue
            elif N_ref[k_ref] == N_exp[k_exp]:
                N_diff.append( int( N_exp[k_exp] ) )
                A_diff.append( int( A_exp[k_exp] ) )
                BE_diff.append( BE_exp[k_exp]-BE_ref[k_ref] )
            else:
                print('impossible case')
                print('Exit()')
                exit()

            N_diff.append( int( N_exp[k_exp] ) )
            A_diff.append( int( A_exp[k_exp] ) )
            BE_diff.append( BE_exp[k_exp]-BE_ref[k_ref] )
        #print('N_diff:',N_diff)
        N_diff = np.array( N_diff )
        A_diff = np.array( A_diff )
        BE_diff = np.array( BE_diff )
        BE2A_diff = BE_diff / A_diff
        #
        if nuda.env.verb: print("Exit diff()")
        #
        return N_diff, A_diff, BE_diff, BE2A_diff
        #
    def init_self( self ):
        """
        Initialize variables in self.
        """
        #
        if nuda.env.verb: print("Enter init_self()")
        #
        #: Attribute A (mass of the nucleus).
        self.nucA = None
        #: Attribute Z (charge of the nucleus).
        self.nucZ = None
        #: Attribute N (number of neutrons of the nucleus).
        self.nucN = None
        #: Attribute deformations
        self.beta20 = None
        self.beta22 = None
        self.beta2  = None
        self.beta30 = None
        self.beta32 = None
        #: Attribute rotation energy
        self.Erot = None
        #: Attribute average pairing energy
        self.gap_n = None
        self.gap_p = None
        #: Attribute moment of inertia (moi)
        self.moi = None
        #: Attribute Mass of the nucleus.
        self.nucMass = None
        #: Attribute Ebind of the nucleus.
        self.Ebind = None
        #: Attribute BE (Binding Energy) of the nucleus.
        self.nucBE = None
        #: Attribute uncertainty in the BE (Binding Energy) of the nucleus.
        self.nucBE2A = None
        #: Attribute Zmax: maximum charge of nuclei present in the table.
        self.Zmax = None
        #
        if nuda.env.verb: print("Exit init_self()")
        #
        return self        

