import os
import sys
import numpy as np  # 1.15.0

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nudy

def tables_rad_ch():
    """
    Return a list of the tables available in this toolkit and
    print them all on the prompt.

    :return: The list of tables.
    :rtype: list[str].
    """
    #
    if nudy.env.verb: print("\nEnter tables_radch()")
    #
    tables = [ '2013-Angeli' ]
    #
    print('tables available in the toolkit:',tables)
    tables_lower = [ item.lower() for item in tables ]
    print('tables available in the toolkit:',tables_lower)
    #
    if nudy.env.verb: print("Exit tables_radch()")
    #
    return tables, tables_lower

class SetupRadCh():
   """
   Instantiate the object with microscopic results choosen by the toolkit practitioner. This choice is defined in the variable model. If not defined, it is taken to be the APR equation of state by default.

   ...

   Attributes
   ----------
   table : str, optional
    The table to consider. Choose between: 2010-isgmr-li, 2018-ismgr_garg (default), ...
   Z : list
    A list with nuclear charge.
   A : list
    A list with nuclear masses.
   E_cen : list
    A list with ISGMR centroid energies.
   E_errp : list
    A list with positive errors in the ISGMR energies.
   E_errm : list
    A list with negative errors in the ISGMR energies.
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
      if nudy.env.verb: print("\nEnter SetupRadCh()")
      #
      self.table = table
      if nudy.env.verb: print("table:",table)
      #
      self.Z = []
      self.symb = []
      self.N = []
      self.A = []
      self.R_ch = []
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
         file_in = os.path.join(nudy.param.path_data,'nuclei/radch/2013-Angeli.csv')
         if nudy.env.verb: print('Reads file:',file_in)
         self.ref = 'I. Angeli and K.P. Marinova, Table of experimental nuclear ground state charge radii: An update, Atomic Data and Nuclear Data Tables 69, 69 (2013)'
         self.label = 'Angeli-Marinova-2013'
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
         self.R_unit = 'fm'
         #
         if nudy.env.verb: print("Exit SetupRadCh()")
   #
   def print_outputs( self ):
      """
      Print outputs on terminal's screen.
      """
      print("")
      #
      if nudy.env.verb: print("Enter print_outputs()")
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
      if nudy.env.verb: print("Exit print_outputs()")
      #

