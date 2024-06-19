import os
import sys
import numpy as np  # 1.15.0

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nudy

def tables_isgmr():
    """
    Returns a list with the name of the models available in this toolkit and
    print them all.
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
   def __init__( self, table = '2018-ISGMR-GARG' ):
      """
      Parameters
      ----------
      model : str, optional
      The model to consider. Choose between: 1998-VAR-AM-APR (default), 2008-AFDMC-NM, ...
      """
      #
      if nudy.env.verb: print("\nEnter SetupISGMR()")
      #
      self.table = table
      if nudy.env.verb: print("table:",table)
      #
      self.Z = []
      self.A = []
      self.E_cen = []
      self.E_errp = []
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
         self.ref = 'T. Li, U. Garg, Y. Liu et al., Phys. Rev. C 81, 034309 (2010)'
         self.label = 'Li-Garg-Liu-2010'
         self.note = "write here notes about this table."
         self.Z, self.A, self.E_cen, self.E_errp, self.E_errm = \
            np.loadtxt( file_in, usecols=(0,1,2,3,4), comments='#', unpack = True )
         self.Z = np.array( self.Z, dtype=int )
         self.A = np.array( self.A, dtype=int )
         self.E_erra = [ self.E_errp, self.E_errm ]
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
      self.E_unit = 'MeV'
      #
      if nudy.env.verb: print("Exit SetupISGMR()")
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
      if any(self.E_cen): print(f"   E: {self.E_cen}")
      if any(self.E_errp): print(f"   E_errp: {self.E_errp}")
      if any(self.E_errm): print(f"   E_errm: {self.E_errm}")
      #
      if nudy.env.verb: print("Exit print_outputs()")
      #
