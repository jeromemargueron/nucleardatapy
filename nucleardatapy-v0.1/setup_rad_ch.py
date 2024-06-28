import os
import sys
import numpy as np  # 1.15.0

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def tables_rad_ch():
    """
    Return a list of the tables available in this toolkit for the charge radiuus and
    print them all on the prompt.  These tables are the following
    ones: '2013-Angeli'.

    :return: The list of tables.
    :rtype: list[str].
    """
    #
    if nuda.env.verb: print("\nEnter tables_radch()")
    #
    tables = [ '2013-Angeli' ]
    #
    print('tables available in the toolkit:',tables)
    tables_lower = [ item.lower() for item in tables ]
    print('tables available in the toolkit:',tables_lower)
    #
    if nuda.env.verb: print("Exit tables_radch()")
    #
    return tables, tables_lower

class SetupRadCh():
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
      if nuda.env.verb: print("\nEnter SetupRadCh()")
      #
      self.table = table
      if nuda.env.verb: print("table:",table)
      #
      #: Attribute Z (charge of the nucleus).
      self.Z = []
      #: Attribute symb (symbol) of the element, e.g., Fe.
      self.symb = []
      #: Attribute N (number of neutrons of the nucleus).
      self.N = []
      #: Attribute A (mass of the nucleus).
      self.A = []
      #: Attribue R_ch (charge radius) in fm.
      self.R_ch = []
      #: Attribue uncertainty in R_ch (charge radius) in fm.
      self.R_ch_err = []
      #
      tables, tables_lower = tables_rad_ch()
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
               self.Z.append(linesplit[0])
               self.symb.append(linesplit[1])
               self.N.append(linesplit[2])
               self.A.append(linesplit[3])
               self.R_ch.append(linesplit[4])
               self.R_ch_err.append(linesplit[5])
            #self.Z, self.symb, self.N, self.A, self.R_ch, self.R_ch_err = \
               #np.loadtxt( file_in, usecols=(0,1,2,3,4,5), delimiter=',', comments='#', unpack = True )
            #self.Z = np.array( self.Z, dtype=int )
            #self.N = np.array( self.N, dtype=int )
            #self.A = np.array( self.A, dtype=int )
            #
         #: Attribute radius unit.
         self.R_unit = 'fm'
         #
         if nuda.env.verb: print("Exit SetupRadCh()")
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
      if any(self.Z): print(f"   Z: {self.Z}")
      if any(self.A): print(f"   A: {self.A}")
      if any(self.R_ch): print(f"   R_ch: {self.R_ch}")
      if any(self.R_ch_err): print(f"   R_ch_err: {self.R_ch_err}")
      #
      if nuda.env.verb: print("Exit print_outputs()")
      #

