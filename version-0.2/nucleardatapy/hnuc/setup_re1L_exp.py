import os
import sys
import numpy as np  # 1.15.0

import nucleardatapy as nuda

def re1L_exp_tables():
    """
    Return a list of the tables available in this toolkit for the charge radiuus and
    print them all on the prompt.  These tables are the following
    ones: '2013-Angeli'.

    :return: The list of tables.
    :rtype: list[str].
    """
    #
    if nuda.env.verb: print("\nEnter re1L_exp_tables()")
    #
    tables = [ '2016-1L-GHM' ]
    #tables = [ '2016-GHM-piK', '2016-GHM-eeK', '2016-GHM-emul', '2016-GHM-Kpi' ]
    #
    #print('tables available in the toolkit:',tables)
    tables_lower = [ item.lower() for item in tables ]
    #print('tables available in the toolkit:',tables_lower)
    #
    if nuda.env.verb: print("Exit re1L_exp_tables()")
    #
    return tables, tables_lower

class setupRE1LExp():
   """
   Instantiate the object with binding energies given \
   from a table.

   This choice is defined in the variable `table`.

   The tables can chosen among the following ones: \
   '2018'.

   :param table: Fix the name of `table`. Default value: '2016-GHM'.
   :type table: str, optional. 

   **Attributes:**
   """
   #
   def __init__( self, table = '2016-1L-GHM' ):
      """
      Parameters
      ----------
      model : str, optional
      The model to consider. Choose between: 2018 (default), , ...
      """
      #
      if nuda.env.verb: print("\nEnter setupRE1LExp()")
      #
      self.table = table
      if nuda.env.verb: print("table:",table)
      #
      tables, tables_lower = re1L_exp_tables()
      #
      if table.lower() not in tables_lower:
         print('Table ',table,' is not in the list of tables.')
         print('list of tables:',tables)
         print('-- Exit the code --')
         exit()
      #
      # Read the table
      #
      nucZ = []
      nucSymb = []
      nucN = []
      nucA = []
      nucsps = []
      nucell = []
      nuclre = []
      nuclre_err = []
      probe = []
      label = []
      color = []
      mark = []
      #
      if table.lower() == '2016-1l-ghm':
         #
         file_in = os.path.join(nuda.param.path_data,'hnuclei/2016-1L-GHM.csv')
         if nuda.env.verb: print('Reads file:',file_in)
         #: Attribute providing the full reference to the paper to be citted.
         self.ref = 'Gal, Hungerford, and Millener, Rev. Mod. Phys. 88, 1 (2016)'
         self.keyref = 'AGal:2016'
         #: Attribute providing additional notes about the data.
         self.note = "write here notes about this table."
         #
      #
      with open(file_in,'r') as file:
         for line in file:
            #print('line:',line.strip('\n'))
            if '#' in line:
               continue
            #print('line:',line)
            linesplit = line.split(',')
            #print('split:',linesplit)
            #print('line.split:',linesplit)
            if len(linesplit) > 1:
               nucZ.append(linesplit[0].strip())
               nucSymb.append(linesplit[1].strip())
               nucN.append(linesplit[2].strip())
               nucsps.append(linesplit[3].strip())
               if nucsps[-1] == '1s':
                  nucell.append(0)
               elif nucsps[-1] == '1p':
                  nucell.append(1)
               elif nucsps[-1] == '1d':
                  nucell.append(2)
               elif nucsps[-1] == '1f':
                  nucell.append(3)
               elif nucsps[-1] == '1g':
                  nucell.append(4)
               #print('sps:',nucsps[-1])
               nuclre.append(linesplit[4].strip())
               nuclre_err.append(linesplit[5].strip())
               probe.append(linesplit[6].strip().strip('\n'))
               if probe[-1] == 'piK':
                  label.append(r"GHM-2016 ($\pi$,K)")
                  color.append('k')
                  mark.append('s')
               elif probe[-1] == 'eeK':
                  label.append("GHM-2016 (e,e'K)")
                  color.append('red')
                  mark.append('o')
               elif probe[-1] == 'emul':
                  label.append("GHM-2016 Emul")
                  color.append('blue')
                  mark.append('^')
               elif probe[-1] == 'emul1':
                  label.append("GHM-2016 Emul1")
                  color.append('pink')
                  mark.append('^')
               elif probe[-1] == 'Kpi':
                  label.append(r"GHM-2016 (K,$\pi$)")
                  color.append('magenta')
                  mark.append('D')
            else:
               break
      #
      # Define the attributes of the class
      #
      #: Attribute Z (charge of the nucleus).
      self.Z = np.array( nucZ, dtype = int )
      #: Attribute N (number of neutrons of the nucleus).
      self.N = np.array( nucN, dtype = int )
      #: Attribute A (mass of the nucleus).
      self.A = self.Z + self.N + np.ones(len(self.N),dtype=int)
      #: charge of the hypernuclei (=Z, since Lamnda is charged 0)
      self.Q = self.Z
      #: Strangness number
      self.S = -1*np.ones(len(self.N),dtype=int)
      #: symbol representing the nucleus
      self.symb = nucSymb
      #: Attribute the s.p. state.
      self.sps = nucsps
      #: Attribute the angular momentum of the state.
      self.ell = np.array( nucell, dtype = int )
      #: Attribute 1L removal energy in MeV.
      self.lre = np.array( nuclre, dtype = float )
      #: Attribute 1L binding energy error in MeV.
      self.lre_err = np.array( nuclre_err, dtype = float )
      #: Attribute the probe.
      self.probe = probe
      #: Attribute the label for the data referenced in figures.
      self.label = label
      #: Attribute color of points
      self.color = color
      #: marker shape
      self.mark = mark
      #
      self.lmin = min(self.ell)
      self.lmax = max(self.ell)
      #print('ell min/max:',self.lmin,self.lmax)
      self.nbdata = len(self.N)
      #: Attribute lbe unit.
      self.e_unit = 'MeV'
      #
      # check and print
      #
      #for i in range(self.nbdata):
      #   print('i:',i,' ell:',self.ell[i],' A:',self.A[i],' lbe:',self.lbe[i],'+-',self.lbe_err[i],' in ',self.lbe_unit)
      #
      if nuda.env.verb: print("Exit setupRE1LExp()")
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
      if any(self.A): print(f"   A: {self.A}")
      if any(self.Z): print(f"   Z: {self.Z}")
      if any(self.N): print(f"   N: {self.N}")
      if any(self.S): print(f"   S: {self.S}")
      if any(self.Q): print(f"   Q: {self.Q}")
      if any(self.symb): print(f" symb: {self.symb}")
      if any(self.ell): print(f" ell: {self.ell}")
      if any(self.lre): print(f"  re: {self.lre}")
      if any(self.lre_err): print(f" re_err: {self.lre_err}")
      #
      if nuda.env.verb: print("Exit print_outputs()")
      #
   def print_latex( self ):
      """
      Method which print outputs on terminal's screen in Latex format.
      """
      print("")
      #
      if nuda.env.verb: print("Enter print_latex()")
      #
      if nuda.env.verb_latex:
         print(f"- table: {self.table}")
         print(rf" index & Z & N & S & ch & symb & $RE$  & Ref. \\\\")
         print(rf"       &   &   &   &    &      & (MeV) &      \\\\")
         for ind,A in enumerate(self.A):
            print(rf" {ind} & {self.Z[ind]} & {self.N[ind]} & {self.S[ind]} & {self.Q[ind]} & {self.symb[ind]} & ${self.lre[ind]:.3f}\pm {self.lre_err[ind]:.3f}$ & \cite{{"+self.keyref+"} \\\\")
      else:
         print(f"- No  table for source {self.table} (average). To get table, write 'verb_latex = True' in env.py.")
      #
      if nuda.env.verb: print("Exit print_latex()")
      #
