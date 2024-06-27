import os
import sys
import numpy as np  # 1.15.0

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nudy

def tables_isgmr():
    """
    Return a list of tables available in this toolkit for the ISGMR energy and
    print them all on the prompt. These tables are the following
    ones: '2010-ISGMR-LI', '2018-ISGMR-GARG'.

    :return: The list of tables.
    :rtype: list[str].    
    """
    #
    if nudy.env.verb: print("\nEnter tables_isgmr()")
    #
    tables = [ '2010-ISGMR-LI', '2018-ISGMR-GARG' ]
    print('tables available in the toolkit:',tables)
    tables_lower = [ item.lower() for item in tables ]
    print('tables available in the toolkit:',tables_lower)
    #
    if nudy.env.verb: print("Exit tables_isgmr()")
    #
    return tables, tables_lower

class SetupISGMR():
   """
   Instantiate the object with microscopic results choosen \
   by the toolkit practitioner. \

   This choice is defined in the variable `table`.

   The `table` can chosen among the following ones: \
   '2010-ISGMR-LI', '2018-ISGMR-GARG'.

   :param table: Fix the name of `table`. Default value: '2018-ISGMR-GARG'.
   :type table: str, optional. 

   **Attributes:**
   """
   #
   def __init__( self, table = '2018-ISGMR-GARG' ):
      """
      Parameters
      ----------
      table : str, optional
      The table to consider. \
      Choose between: 2018-ISGMR-GARG (default) and 2010-ISGMR-LI.
      """
      #
      if nudy.env.verb: print("\nEnter SetupISGMR()")
      #: Attribute table.
      self.table = table
      if nudy.env.verb: print("table:",table)
      #
      #: Attribute Z (charge of the nucleus).
      self.Z = []
      #: Attribute A (mass of the nucleus).
      self.A = []
      #: Attribute energy centroid.
      self.E_cen = []
      #: Attribute (+) uncertainty in the energy centroid.
      self.E_errp = []
      #: Attribute (-) uncertainty in the energy centroid.
      self.E_errm = []
      #
      tables, tables_lower = tables_isgmr()
      #
      if table.lower() not in tables_lower:
          print('Table ',table,' is not in the list of tables.')
          print('list of tables:',tables)
          print('-- Exit the code --')
          exit()
      #
      if table.lower() == '2010-isgmr-li':
         #
         file_in = os.path.join(nudy.param.path_data,'nuclei/isgmr/2010-ISGMR-Li.dat')
         if nudy.env.verb: print('Reads file:',file_in)
         #: Attribute providing the full reference to the paper to be citted.
         self.ref = 'T. Li, U. Garg, Y. Liu et al., Phys. Rev. C 81, 034309 (2010)'
         #: Attribute providing the label the data is references for figures.
         self.label = 'Li-Garg-Liu-2010'
         #: Attribute providing additional notes about the data.
         self.note = "write here notes about this table."
         self.Z, self.A, self.E_cen, self.E_errp, self.E_errm = \
            np.loadtxt( file_in, usecols=(0,1,2,3,4), comments='#', unpack = True )
         self.Z = np.array( self.Z, dtype=int )
         self.A = np.array( self.A, dtype=int )
         #: Attribute list with + and - uncertainty
         self.E_erra = [ self.E_errp, self.E_errm ]
         #: Attribute symmetrised uncertainty (average between + and - uncertainty).
         self.E_errs = 0.5 * ( self.E_errp + self.E_errm )
         #
      elif table.lower() == '2018-isgmr-garg':
         #
         file_in = os.path.join(nudy.param.path_data,'nuclei/isgmr/2018-ISGMR-Garg.dat')
         if nudy.env.verb: print('Reads file:',file_in)
         self.ref = 'U. Garg and G. Colo, Prog. Part. Nucl. Phys. 101, 55 (2018)'
         self.label = 'Garg-Colo-2018'
         self.note = "write here notes about this table."
         self.Z, self.A, self.E_cen, self.E_errp, self.E_errm = \
            np.loadtxt( file_in, usecols=(0,1,2,3,4), comments='#', unpack = True )
         self.Z = np.array( self.Z, dtype=int )
         self.A = np.array( self.A, dtype=int )
         self.E_erra = [ self.E_errp, self.E_errm ]
         self.E_errs = 0.5 * ( self.E_errp + self.E_errm )
         #
      #: Attribute energy unit.
      self.E_unit = 'MeV'
      #
      if nudy.env.verb: print("Exit SetupISGMR()")
   #
   def print_outputs( self ):
      """
      Method which print outputs on terminal's screen.
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
      if any(self.E_cen): print(f"   E: {self.E_cen}")
      if any(self.E_errp): print(f"   E_errp: {self.E_errp}")
      if any(self.E_errm): print(f"   E_errm: {self.E_errm}")
      #
      if nudy.env.verb: print("Exit print_outputs()")
      #
