import os
import sys
import math
import numpy as np  # 1.15.0

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def tables_masses_theory():
    """
    Return a list of the tables available in this toolkit for the masses 
    predicted by theoretical approaches and print them all on the prompt. 
    These tables are the following ones: \
    [ '1988-GK', '1988-MJ', '1995-DZ', '1995-ETFSI', '1995-FRDM', \
    '2005-KTUY', '2007-HFB14', '2010-WS3', '2010-HFB21', '2011-WS3', '2013-HFB26' ]

    :return: The list of tables.
    :rtype: list[str].
    """
    #
    if nuda.env.verb: print("\nEnter tables_masses_theory()")
    #
    tables = [ '1988-GK', '1988-MJ', '1995-DZ', '1995-ETFSI', '1995-FRDM', \
       '2005-KTUY', '2007-HFB14', '2010-WS3', '2010-HFB21','2011-WS3', '2013-HFB26' ]
    #
    print('theory tables available in the toolkit:',tables)
    tables_lower = [ item.lower() for item in tables ]
    print('theory tables available in the toolkit:',tables_lower)
    #
    if nuda.env.verb: print("Exit tables_masses_theory()")
    #
    return tables, tables_lower

class SetupMassesTheory():
    """
    Instantiate the theory nuclear masses.

    This choice is defined in the variable `table`.

    `table` can chosen among the following ones: \
    [ '1988-GK', '1988-MJ', '1995-DZ', '1995-ETFSI', '1995-FRDM', \
    '2005-KTUY', '2007-HFB14', '2010-WS3', '2010-HFB21','2011-WS3', '2013-HFB26' ]

    :param table: Fix the name of `table`. Default value: '1995-DZ'.
    :type table: str, optional. 

    **Attributes:**
    """
    def __init__(self, table = '1995-DZ' ):
        #
        if nuda.env.verb: print("Enter SetupMassesTheory()")
        #
        tables, tables_lower = tables_masses_theory()
        if table.lower() not in tables_lower:
            print('Table ',table,' is not in the list of tables.')
            print('list of tables:',tables)
            print('-- Exit the code --')
            exit()
        self.table = table
        if nuda.env.verb: print("table:",table)
        #
        self = SetupMassesTheory.init_self( self )
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
            self.nucZr, self.nucNr, self.nucBE2A  = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.nucZ = np.array( [ int(ele) for ele in self.nucZr ] )
            self.nucN = np.array( [ int(ele) for ele in self.nucNr ] )
            self.nucA = self.nucZ + self.nucN
            self.nucBE = self.nucBE2A * self.nucA
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
            self.nucZr, self.nucNr, self.nucBE2A  = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.nucZ = np.array( [ int(ele) for ele in self.nucZr ] )
            self.nucN = np.array( [ int(ele) for ele in self.nucNr ] )
            self.nucA = self.nucZ + self.nucN
            self.nucBE = self.nucBE2A * self.nucA
            self.Zmax = int( max( self.nucZ ) )
            #
        elif table.lower()=='1995-dz':
            #
            # read the Duflo-Zuker theoretical mass table
            #
            file_in = nuda.param.path_data+'nuclei/masses/Theory/1995-DUZU.txt'
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'J. Duflo and A.P. Zuker, Phys. Rev. C 52, (1995)'
            self.note = "write here notes about this EOS."
            self.label = 'DZ-1995'
            self.nucZr, self.nucNr, self.nucBE2A  = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.nucZ = np.array( [ int(ele) for ele in self.nucZr ] )
            self.nucN = np.array( [ int(ele) for ele in self.nucNr ] )
            self.nucA = self.nucZ + self.nucN
            self.nucBE = self.nucBE2A * self.nucA
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
            self.nucZr, self.nucNr, self.nucBE2A  = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.nucZ = np.array( [ int(ele) for ele in self.nucZr ] )
            self.nucN = np.array( [ int(ele) for ele in self.nucNr ] )
            self.nucA = self.nucZ + self.nucN
            self.nucBE = self.nucBE2A * self.nucA
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
            self.beta4 = []; self.beta6 = []; self.Emic = []; self.Mth = []; self.Mexp = []; 
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
                    self.Mth.append( float(line[117:126]) )
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
            self.Mth = np.array( self.Mth )
            self.nucBE = self.Mth * self.nucA
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
            self.nucZr, self.nucNr, self.nucBE2A  = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.nucZ = np.array( [ int(ele) for ele in self.nucZr ] )
            self.nucN = np.array( [ int(ele) for ele in self.nucNr ] )
            self.nucA = self.nucZ + self.nucN
            self.nucBE = self.nucBE2A * self.nucA
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
            self.nucZr, self.nucNr, self.nucBE2A  = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.nucZ = np.array( [ int(ele) for ele in self.nucZr ] )
            self.nucN = np.array( [ int(ele) for ele in self.nucNr ] )
            self.nucA = self.nucZ + self.nucN
            self.nucBE = self.nucBE2A * self.nucA
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
               self.Qbet, self.Mcal, self.dif, self.Jexp, self.Jth, self.Pexp, self.Pth  = \
               np.loadtxt( file_in, usecols=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14), unpack = True )
            self.nucZ = np.array( [ int(ele) for ele in self.nucZr ] )
            self.nucA = np.array( [ int(ele) for ele in self.nucAr ] )
            self.nucN = self.nucA - self.nucZ
            self.nucBE = self.Mcal * self.nucA
            self.Zmax = int( max( self.nucZ ) )
            #
        elif table.lower()=='2010-ws3':
            #
            # read the HFB14 theoretical mass table
            #
            file_in = nuda.param.path_data+'nuclei/masses/Theory/2010-WS3.txt'
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'N. Wang, Z. Liang, M. Liu, X. Wu, Phys. Rev. C 82, 044304 (2010).'
            self.note = "write here notes about this EOS."
            self.label = 'WS3-2010'
            self.nucZr, self.nucNr, self.nucBE2A  = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.nucZ = np.array( [ int(ele) for ele in self.nucZr ] )
            self.nucN = np.array( [ int(ele) for ele in self.nucNr ] )
            self.nucA = self.nucZ + self.nucN
            self.nucBE = self.nucBE2A * self.nucA
            self.Zmax = int( max( self.nucZ ) )
            #
        elif table.lower()=='2011-ws3':
            #
            # read the HFB14 theoretical mass table
            #
            file_in = nuda.param.path_data+'nuclei/masses/Theory/2011-WS3.txt'
            if nuda.env.verb: print('Reads file:',file_in)
            self.ref = 'M. Liu, N. Wang, Y. Deng, X. Wu, Phys. Rev. C 84, 014333 (2011).'
            self.note = "write here notes about this EOS."
            self.label = 'WS3-2011'
            self.nucZr, self.nucNr, self.nucBE2A  = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.nucZ = np.array( [ int(ele) for ele in self.nucZr ] )
            self.nucN = np.array( [ int(ele) for ele in self.nucNr ] )
            self.nucA = self.nucZ + self.nucN
            self.nucBE = self.nucBE2A * self.nucA
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
            self.nucZr, self.nucNr, self.nucBE2A  = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
            self.nucZ = np.array( [ int(ele) for ele in self.nucZr ] )
            self.nucN = np.array( [ int(ele) for ele in self.nucNr ] )
            self.nucA = self.nucZ + self.nucN
            self.nucBE = self.nucBE2A * self.nucA
            self.Zmax = int( max( self.nucZ ) )
            #
        #
        if nuda.env.verb: print("Exit SetupMassesTheory()")
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
    def drip(self, Zmax = 95 ):
        """
        Method which find the drip-line nuclei (on the two sides).

        :param Zmax: Fix the maximum charge for the search of the drip line.
        :type Zmax: int, optional. Default: 95.

        **Attributes:**
        """
        #
        if nuda.env.verb: print("Enter drip()")
        #
        Nstable, Zstable = stable_fit()
        #
        self.drip_Z = []
        self.drip_Nmin = []
        self.drip_Nmax = []
        #
        for Z,ind in enumerate(Zstable):
            #
            if Z >= Zmax :
                break
            #
            Nmin = Nstable[ind]
            Nmax = Nstable[ind]
            #
            for ind2 in range(self.sel_nbNucSel):
                if self.sel_Z[ind2] == Z and self.sel_N[ind2] < Nmin:
                    Nmin = self.sel_N[ind2]
                if self.sel_Z[ind2] == Z and self.sel_N[ind2] > Nmax:
                    Nmax = self.sel_N[ind2]
            self.drip_Z.append( Z )
            self.drip_Nmin.append( Nmin )
            self.drip_Nmax.append( Nmax )
        #
        if nuda.env.verb: print("Exit drip()")
        #
        return self
        #
       #
    def diff(self, table, Zref = 50 ):
        """
        Method calculates the difference between a given mass model and the table_ref.

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
            print('we have self.table = table')
            print('self.table:',self.table)
            print('table:',table)
            print('exit()')
            exit()
        #
        # table_ref
        #
        N_ref = self.nucN
        BE_ref = self.nucBE
        #
        # table
        #
        mas = nuda.SetupMassesTheory( table = table )
        BE = []
        N = []
        for k in range(len(mas.nucZ)):
            if int( mas.nucZ[k] ) == Zref:
                BE.append( mas.nucBE[k] )
                N.append( mas.nucN[k] )
        N_min = max( N[0], N_ref[0] )
        k_ref, = np.where( N_ref[:] == N_min )[0]
        k_init, = np.where( N[:] == N_min )[0]
        #
        # diff
        #
        N_dif = []
        BE_dif = []
        for k in range(k_init,len(N)-k_init):
            k_ref += N[k] - N_ref[k_ref]
            BE_dif.append( BE[k]-BE_ref[k_ref] )
            N_dif.append( N[k] )
            k_ref += 1
        #
        if nuda.env.verb: print("Exit diff()")
        #
        return N_dif, BE_dif
        #
    def init_self( self ):
        """
        Initialize variables in self.
        """
        #
        if nuda.env.verb: print("Enter init_self()")
        #
        #: Attribute A (mass of the nucleus).
        self.A = None
        #: Attribute Z (charge of the nucleus).
        self.Z = None
        #: Attribute N (number of neutrons of the nucleus).
        self.N = None
        #: Attribute BE (Binding Energy) of the nucleus.
        self.BE = None
        #: Attribute uncertainty in the BE (Binding Energy) of the nucleus.
        self.BE2A = None
        #: Attribute Zmax: maximum charge of nuclei present in the table.
        self.Zmax = None
        #
        if nuda.env.verb: print("Exit init_self()")
        #
        return self        

