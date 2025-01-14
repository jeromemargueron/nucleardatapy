import os
import sys
import numpy as np  # 1.15.0

import nucleardatapy as nuda

def spe_exp_tables():
    """
    Return a list of the tables available in this toolkit for the charge radiuus and
    print them all on the prompt.  These tables are the following
    ones: '2013-Angeli'.

    :return: The list of tables.
    :rtype: list[str].
    """
    #
    if nuda.env.verb: print("\nEnter spe_exp_tables()")
    #
    tables = [ '2016-GHM-piK', '2016-GHM-eeK', '2016-GHM-emul', '2016-GHM-Kpi' ]
    #
    print('tables available in the toolkit:',tables)
    tables_lower = [ item.lower() for item in tables ]
    print('tables available in the toolkit:',tables_lower)
    #
    if nuda.env.verb: print("Exit spe_exp_tables()")
    #
    return tables, tables_lower

class setupSPEExp():
   """
   Instantiate the object with single particle energies choosen \
   from a table.

   This choice is defined in the variable `table`.

   The tables can chosen among the following ones: \
   '2018'.

   :param table: Fix the name of `table`. Default value: '2018'.
   :type table: str, optional. 

   **Attributes:**
   """
   #
   def __init__( self, table = '2016-GHM-piK' ):
      """
      Parameters
      ----------
      model : str, optional
      The model to consider. Choose between: 2018 (default), , ...
      """
      #
      if nuda.env.verb: print("\nEnter setupSPEExp()")
      #
      self.table = table
      if nuda.env.verb: print("table:",table)
      #
      nucZ = []
      nucSymb = []
      nucN = []
      nucA = []
      nucsps = []
      nucell = []
      nucspe = []
      nucspe_err = []
      #
      tables, tables_lower = spe_exp_tables()
      #
      if table.lower() not in tables_lower:
         print('Table ',table,' is not in the list of tables.')
         print('list of tables:',tables)
         print('-- Exit the code --')
         exit()
      #
      if table.lower() == '2016-ghm-pik':
         #
         file_in = os.path.join(nuda.param.path_data,'hnuclei/2016-GHM-piK.csv')
         if nuda.env.verb: print('Reads file:',file_in)
         #: Attribute providing the full reference to the paper to be citted.
         self.ref = 'Gal, Hungerford, and Millener, Rev. Mod. Phys. 88, 1 (2016)'
         #: Attribute providing the label the data is references for figures.
         self.label = "GHM 2016 ($\pi$,K)"
         #: Attribute providing additional notes about the data.
         self.note = "write here notes about this table."
         #: Attribute color of points
         self.color='k'
         #: marker shape
         self.mark='s'
         #
      elif table.lower() == '2016-ghm-eek':
         #
         file_in = os.path.join(nuda.param.path_data,'hnuclei/2016-GHM-eeK.csv')
         if nuda.env.verb: print('Reads file:',file_in)
         #: Attribute providing the full reference to the paper to be citted.
         self.ref = 'Gal, Hungerford, and Millener, Rev. Mod. Phys. 88, 1 (2016)'
         #: Attribute providing the label the data is references for figures.
         self.label = "GHM 2016 (e,e'K)"
         #: Attribute providing additional notes about the data.
         self.note = "write here notes about this table."
         #: Attribute color of points
         self.color='red'
         #: marker shape
         self.mark='o'
         #
      elif table.lower() == '2016-ghm-emul':
         #
         file_in = os.path.join(nuda.param.path_data,'hnuclei/2016-GHM-emul.csv')
         if nuda.env.verb: print('Reads file:',file_in)
         #: Attribute providing the full reference to the paper to be citted.
         self.ref = 'Gal, Hungerford, and Millener, Rev. Mod. Phys. 88, 1 (2016)'
         #: Attribute providing the label the data is references for figures.
         self.label = "GHM 2016 Emulsion"
         #: Attribute providing additional notes about the data.
         self.note = "write here notes about this table."
         #: Attribute color of points
         self.color='blue'
         #: marker shape
         self.mark='^'
         #
      elif table.lower() == '2016-ghm-kpi':
         #
         file_in = os.path.join(nuda.param.path_data,'hnuclei/2016-GHM-Kpi.csv')
         if nuda.env.verb: print('Reads file:',file_in)
         #: Attribute providing the full reference to the paper to be citted.
         self.ref = 'Gal, Hungerford, and Millener, Rev. Mod. Phys. 88, 1 (2016)'
         #: Attribute providing the label the data is references for figures.
         self.label = "GHM 2016 (K,$\pi$)"
         #: Attribute providing additional notes about the data.
         self.note = "write here notes about this table."
         #: Attribute color of points
         self.color='magenta'
         #: marker shape
         self.mark='D'
         #
      #
      with open(file_in,'r') as file:
         for line in file:
            #print('line:',line)
            if '#' in line:
               continue
            #print('line:',line)
            linesplit = line.split(',')
            #print('split:',linesplit)
            #print('line.split:',linesplit)
            if len(linesplit) > 1:
               nucZ.append(linesplit[0])
               nucSymb.append(linesplit[1])
               nucN.append(linesplit[2])
               nucsps.append(linesplit[3])
               nucell.append(linesplit[4])
               nucspe.append(linesplit[5])
               nucspe_err.append(linesplit[6])
            else:
               break
            #
      nucZ = np.array( nucZ, dtype = int )
      nucN = np.array( nucN, dtype = int )
      nucA = nucZ + nucN + np.ones(len(nucN))
      nucell = np.array( nucell, dtype = int )
      nucspe = np.array( nucspe, dtype = float )
      nucspe_err = np.array( nucspe_err, dtype = float )
      #
      self.lmin = min(nucell)
      self.lmax = max(nucell)
      # create dictionary spe
      self.marker = {}
      #: Attribute A (mass of the nucleus).
      self.A = {}
      #: Attribute Z (charge of the nucleus).
      self.Z = {}
      #: Attribute N (number of neutrons of the nucleus).
      self.N = {}
      #: Attribue spe in MeV.
      self.spe = {}
      #: Attribue spe error in MeV.
      self.spe_err = {}
      for ell in range(self.lmin,self.lmax+1):
         #print('ell:',ell)
         self.marker[ell] = self.mark
         self.A[ell] = []
         self.Z[ell] = []
         self.N[ell] = []
         self.spe[ell] = []
         self.spe_err[ell] = []
         for ind,lstt in enumerate(nucell):
            if ell == lstt:
               self.A[ell].append(nucA[ind])
               self.Z[ell].append(nucZ[ind])
               self.N[ell].append(nucN[ind])
               self.spe[ell].append(nucspe[ind])
               self.spe_err[ell].append(nucspe_err[ind])
         print('ell:',ell,' A:',self.A[ell],' spe:',self.spe[ell],'+-',self.spe_err[ell],' MeV')
      #
      #: Attribute spe unit.
      self.spe_unit = 'MeV'
      #
      if nuda.env.verb: print("Exit setupSPEExp()")
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
      print("   table:",self.table)
      print("   ref:",self.ref)
      print("   label:",self.label)
      print("   note:",self.note)
      for ell in range(self.lmin,self.lmax+1):
         print('For ell:',ell)
         if any(self.A): print(f"   A: {self.A[ell]}")
         if any(self.Z): print(f"   Z: {self.Z[ell]}")
         if any(self.N): print(f"   N: {self.N[ell]}")
         if any(self.spe): print(f"   spe: {self.spe[ell]}")
         if any(self.spe_err): print(f"   spe_err: {self.spe_err[ell]}")
      #
      if nuda.env.verb: print("Exit print_outputs()")
      #

