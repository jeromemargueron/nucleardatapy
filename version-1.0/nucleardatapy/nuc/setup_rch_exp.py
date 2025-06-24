import os
import sys
import numpy as np  # 1.15.0

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def rch_exp_tables():
    """
    Return a list of the tables available in this toolkit for the charge radiuus and
    print them all on the prompt.  These tables are the following
    ones: '2013-Angeli'.

    :return: The list of tables.
    :rtype: list[str].
    """
    #
    if nuda.env.verb: print("\nEnter rch_exp_tables()")
    #
    tables = [ '2013-Angeli' ]
    #
    #print('tables available in the toolkit:',tables)
    tables_lower = [ item.lower() for item in tables ]
    #print('tables available in the toolkit:',tables_lower)
    #
    if nuda.env.verb: print("Exit rch_exp_tables()")
    #
    return tables, tables_lower

class setupRchExp():
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
   def __init__( self, table = '2013-Angeli' ):
      """
      Parameters
      ----------
      model : str, optional
      The model to consider. Choose between: 1998-VAR-AM-APR (default), 2008-AFDMC-NM, ...
      """
      #
      if nuda.env.verb: print("\nEnter setupRchExp()")
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
      #: Attribue uncertainty in R_ch (charge radius) in fm.
      self.nucRch_err = []
      #
      tables, tables_lower = rch_exp_tables()
      #
      if table.lower() not in tables_lower:
         print('Table ',table,' is not in the list of tables.')
         print('list of tables:',tables)
         print('-- Exit the code --')
         exit()
      #
      if table.lower() == '2013-angeli':
         #
         file_in = os.path.join(nuda.param.path_data,'nuclei/radch/2013-Angeli.csv')
         if nuda.env.verb: print('Reads file:',file_in)
         #: Attribute providing the full reference to the paper to be citted.
         self.ref = 'I. Angeli and K.P. Marinova, Table of experimental nuclear ground state charge radii: An update, Atomic Data and Nuclear Data Tables 69, 69 (2013)'
         #: Attribute providing the label the data is references for figures.
         self.label = 'Angeli-Marinova-2013'
         #: Attribute providing additional notes about the data.
         self.note = "write here notes about this table."
         #
         with open(file_in,'r') as file:
            for line in file:
               #print('line:',line)
               if '#' in line:
                  continue
               linesplit = line.split(',')
               #print('line.split:',linesplit)
               self.nucZ.append(linesplit[0])
               self.nucSymb.append(linesplit[1])
               self.nucN.append(linesplit[2])
               self.nucA.append(linesplit[3])
               self.nucRch.append(linesplit[4])
               self.nucRch_err.append(linesplit[5])
               #
         #: Attribute radius unit.
         self.R_unit = 'fm'
         #
         if nuda.env.verb: print("Exit setupRchExp()")
   #
   def isotopes(self, Zref = 50 ):
      """
      This method provide a list if radii for an isotopic chain defined by Zref.

      """
      #
      if nuda.env.verb: print("Enter isotopes()")
      #
      Nref = []
      Aref = []
      Rchref = []
      Rchref_err = []
      for k in range(len(self.nucZ)):
         if int( self.nucZ[k] ) == Zref:
            Nref.append( self.nucN[k] )
            Aref.append( self.nucA[k] )
            Rchref.append( self.nucRch[k] )
            Rchref_err.append( self.nucRch_err[k] )
      Nref = np.array( Nref, dtype = int )
      Aref = np.array( Aref, dtype = int )
      Rchref = np.array( Rchref, dtype = float )
      Rchref_err = np.array( Rchref_err, dtype = float )
      #
      if nuda.env.verb: print("Exit isotopes()")
      #
      return Nref, Aref, Rchref, Rchref_err
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
      if any(self.nucRch_err): print(f"   Rch_err: {self.nucRch_err}")
      #
      if nuda.env.verb: print("Exit print_outputs()")
      #

class setupRchExpIsotopes():
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
            Rchref_err.append( rch.nucRch_err[k] )
      self.N = np.array( Nref, dtype = int )
      self.A = np.array( Aref, dtype = int )
      self.Z = Zref * np.ones( self.N.size )
      self.Rch = np.array( Rchref, dtype = float )
      self.Rch_err = np.array( Rchref_err, dtype = float )
      #
      if nuda.env.verb: print("Exit setupRchExpIsotopes()")
      #
