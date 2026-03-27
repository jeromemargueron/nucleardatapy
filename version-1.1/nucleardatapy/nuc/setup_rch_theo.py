import os
import sys
import numpy as np  # 1.15.0

import nucleardatapy as nuda

def rch_emp( A, Z, formula ):
   if formula == 'classic':
      return 1.2 * A**0.3333
   elif formula == '1994-NPP':
      # B. Nerlo-Pomorska and K. Pomorski, Z. Phys. A 348, 169 (1994)
      r0 = 1.240
      b = 0.191
      c = 1.646
   elif formula == '2013-BAKS-1':
      # T. Bayram, S. Akkoyun, S. Okan Kara, A. Sinan, Acta Phys. Pol. B 44, 1791 (2013)
      r0 = 0.951
      b = 0.0
      c = 0.0
   elif formula == '2013-BAKS-2':
      # T. Bayram, S. Akkoyun, S. Okan Kara, A. Sinan, Acta Phys. Pol. B 44, 1791 (2013)
      r0 = 0.996
      b = 0.278
      c = 0.0
   elif formula == '2013-BAKS-3':
      # T. Bayram, S. Akkoyun, S. Okan Kara, A. Sinan, Acta Phys. Pol. B 44, 1791 (2013)
      r0 = 0.966
      b = 0.182
      c = 1.652
   else:
      print('setup_rch_theo: formula is badly defined ',formula)
      print('setup_rch_theo: exit')
      exit()
      #return ( 1.19 - 0.8 * (1-2*Z/A)**2 ) * A**0.3333 - 0.3* A**0.1666 
   return r0 * ( 1.0 - b * (1.0-2.0*Z/A) + c/ A  ) * A**0.3333

def rch_theo_tables():
    """
    Return a list of the tables available in this toolkit for the charge radiuus and
    print them all on the prompt.  These tables are the following
    ones: '2013-Angeli'.

    :return: The list of tables.
    :rtype: list[str].
    """
    #
    if nuda.env.verb: print("\nEnter rch_theo_tables()")
    #
    tables = [ '2021-BSkG1', '2022-BSkG2', '2023-BSkG3', '2025-BSkG4'  ]
    #
    print('tables available in the toolkit:',tables)
    tables_lower = [ item.lower() for item in tables ]
    print('tables available in the toolkit:',tables_lower)
    #
    if nuda.env.verb: print("Exit rch_theo_tables()")
    #
    return tables, tables_lower

class setupRchTheo():
   """
   Instantiate the object with charge radii choosen \
   from a table.

   This choice is defined in the variable `table`.

   The tables can chosen among the following ones: \
   '2013-Angeli'.

   :param table: Fix the name of `table`. Default value: '2013-Angeli'.
   :type table: str, optional. 

   **Attributes:**
   """
   #
   def __init__( self, table = '2021-BSkG1' ):
      """
      Parameters
      ----------
      table : str, optional
      The theoretical table to consider. Choose between: 2021-BSkG1 (default), 2022-BSkG2, 2023-BSkG3, 2025-BSkG4 ...
      """
      #
      if nuda.env.verb: print("\nEnter setupRchTheo()")
      #
      self.table = table
      if nuda.env.verb: print("table:",table)
      #
      #: Attribute Z (charge of the nucleus).
      self.nucZ = []
      #: Attribute symb (symbol) of the element, e.g., Fe.
      self.nucSymb = []
      #: Attribute N (number of neutrons of the nucleus).
      self.nucN = []
      #: Attribute A (mass of the nucleus).
      self.nucA = []
      #: Attribue R_ch (charge radius) in fm.
      self.nucRch = []
      #
      tables, tables_lower = rch_theo_tables()
      #
      if table.lower() not in tables_lower:
         print('Table ',table,' is not in the list of tables.')
         print('list of tables:',tables)
         print('-- Exit the code --')
         exit()
      #
      if table.lower() == '2021-bskg1':
         #
         file_in = os.path.join(nuda.param.path_data,'nuclei/masses/Theory/2021-BSkG1.txt')
         if nuda.env.verb: print('Reads file:',file_in)
         #: Attribute providing the full reference to the paper to be citted.
         self.ref = 'G. Scamps, S. Goriely, E. Olsen, M. Bender, and W. Ryssens, EPJA 57, 333 (2021).'
         #: Attribute providing additional notes about the data.
         self.note = "write here notes about this EOS."
         #: Attribute providing the label the data is references for figures.
         self.label = 'BSkG1-2021'
         #self.nucZr, self.nucNr, self.nucBE2A  = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
         self.nucZr, self.nucNr, self.nucMass, self.Ebind, self.beta20, self.beta22, self.beta2, self.Erot, \
         self.gap_n, self.gap_p, self.nucRch, self.moi = \
         np.loadtxt( file_in, usecols=(0,1,3,5,6,7,8,9,10,11,12,15), unpack = True )
         self.nucZ = np.array( [ int(ele) for ele in self.nucZr ] )
         self.nucN = np.array( [ int(ele) for ele in self.nucNr ] )
         self.nucA = self.nucZ + self.nucN
         #
      elif table.lower() == '2022-bskg2':
         #
         file_in = os.path.join(nuda.param.path_data,'nuclei/masses/Theory/2022-BSkG2.txt')
         if nuda.env.verb: print('Reads file:',file_in)
         #: Attribute providing the full reference to the paper to be citted.
         self.ref = 'W. Ryssens, G. Scamps, S. Goriely, and M. Bender, EPJA 58, 246 (2022).'
         #: Attribute providing additional notes about the data.
         self.note = "write here notes about this EOS."
         #: Attribute providing the label the data is references for figures.
         self.label = 'BSkG2-2022'
         #self.nucZr, self.nucNr, self.nucBE2A  = np.loadtxt( file_in, usecols=(0,1,2), unpack = True )
         self.nucZr, self.nucNr, self.nucMass, self.Ebind, self.beta20, self.beta22, self.beta2, self.Erot, \
         self.gap_n, self.gap_p, self.nucRch, self.moi = \
         np.loadtxt( file_in, usecols=(0,1,3,5,6,7,8,9,10,11,12,15), unpack = True )
         self.nucZ = np.array( [ int(ele) for ele in self.nucZr ] )
         self.nucN = np.array( [ int(ele) for ele in self.nucNr ] )
         self.nucA = self.nucZ + self.nucN
         #
      elif table.lower() == '2023-bskg3':
         #
         file_in = os.path.join(nuda.param.path_data,'nuclei/masses/Theory/2023-BSkG3.txt')
         if nuda.env.verb: print('Reads file:',file_in)
         #: Attribute providing the full reference to the paper to be citted.
         self.ref = 'G. Grams, W. Ryssens, G. Scamps, S. Goriely, and N. Chamel, EPJA 59, 270 (2023).'
         #: Attribute providing additional notes about the data.
         self.note = "write here notes about this EOS."
         #: Attribute providing the label the data is references for figures.
         self.label = 'BSkG3-2023'
         self.nucZr, self.nucNr, self.nucMass, self.Ebind, self.beta20, self.beta22, self.beta2, \
         self.beta30, self.beta32, self.Erot, self.gap_n, self.gap_p, self.nucRch, self.moi = \
         np.loadtxt( file_in, usecols=(0,1,3,5,6,7,8,9,10,11,12,13,14,17), unpack = True )
         self.nucZ = np.array( [ int(ele) for ele in self.nucZr ] )
         self.nucN = np.array( [ int(ele) for ele in self.nucNr ] )
         self.nucA = self.nucZ + self.nucN
         #
      elif table.lower() == '2025-bskg4':
         #
         file_in = os.path.join(nuda.param.path_data,'nuclei/masses/Theory/2025-BSkG4.txt')
         if nuda.env.verb: print('Reads file:',file_in)
         #: Attribute providing the full reference to the paper to be citted.
         self.ref = 'G. Grams, W. Ryssens, N. Shchechilin, A. Sanchez-Fernandez, N. Chamel, and S. Goriely,  EPJA 61, 35 (2025).'
         #: Attribute providing additional notes about the data.
         self.note = "write here notes about this EOS."
         #: Attribute providing the label the data is references for figures.
         self.label = 'BSkG4-2025'
         self.nucZr, self.nucNr, self.nucMass, self.Ebind, self.beta20, self.beta22, self.beta2, \
         self.beta30, self.beta32, self.Erot, self.gap_n, self.gap_p, self.nucRch, self.moi = \
         np.loadtxt( file_in, usecols=(0,1,3,5,6,7,8,9,10,11,12,13,14,17), unpack = True )
         self.nucZ = np.array( [ int(ele) for ele in self.nucZr ] )
         self.nucN = np.array( [ int(ele) for ele in self.nucNr ] )
         self.nucA = self.nucZ + self.nucN
         #
      #: Attribute radius unit.
      self.R_unit = 'fm'
      #
      if nuda.env.verb: print("Exit setupChTheo()")
   #
   def Rch_isotopes(self, Zref = 50 ):
      """
      This method provide a list if radii for an isotopic chain defined by Zref.

      """
      #
      if nuda.env.verb: print("Enter Rch_isotopes()")
      #
      Nref = []
      Aref = []
      Rchref = []
      for k in range(len(self.nucZ)):
         if int( self.nucZ[k] ) == Zref:
            Nref.append( self.nucN[k] )
            Aref.append( self.nucA[k] )
            Rchref.append( self.nucRch[k] )
      Nref = np.array( Nref, dtype = int )
      Aref = np.array( Aref, dtype = int )
      Rchref = np.array( Rchref, dtype = float )
      #
      return Nref, Aref, Rchref
      #
      if nuda.env.verb: print("Exit Rch_isotopes()")
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
      print("   table:",self.table)
      print("   ref:",self.ref)
      print("   label:",self.label)
      print("   note:",self.note)
      if any(self.nucZ): print(f"   Z: {self.nucZ}")
      if any(self.nucA): print(f"   A: {self.nucA}")
      if any(self.nucRch): print(f"   Rch: {self.nucRch}")
      #
      if nuda.env.verb: print("Exit print_outputs()")
      #

class setupRchTheoIsotopes():
   """
   Instantiate the object with charge radii choosen \
   from a table.

   This method provide a list if radii for an isotopic chain defined by Zref.

   :param table: Fix the name of `table`. Default value: '2013-Angeli'.
   :type table: str, optional. 

   **Attributes:**
   """
   #
   def __init__( self, rch, Zref = 50 ):
      """
      Parameters
      ----------
      model : str, optional
      The model to consider. Choose between: 1998-VAR-AM-APR (default), 2008-AFDMC-NM, ...
      """
      #
      if nuda.env.verb: print("\nEnter setupRchExpIsotopes()")
      #
      self.label = 'Isotope Z='+str(Zref)
      #
      Nref = []
      Aref = []
      Rchref = []
      Rchref_err = []
      for k in range(len(rch.nucZ)):
         if int( rch.nucZ[k] ) == Zref:
            Nref.append( rch.nucN[k] )
            Aref.append( rch.nucA[k] )
            Rchref.append( rch.nucRch[k] )
      self.N = np.array( Nref, dtype = int )
      self.A = np.array( Aref, dtype = int )
      self.Z = Zref * np.ones( self.N.size )
      self.Rch = np.array( Rchref, dtype = float )
      #
      if nuda.env.verb: print("Exit setupRchExpIsotopes()")
      #

