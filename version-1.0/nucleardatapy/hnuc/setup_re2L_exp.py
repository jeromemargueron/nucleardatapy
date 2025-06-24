import os
import sys
import numpy as np  # 1.15.0

import nucleardatapy as nuda

def re2L_exp_tables():
    """
    Return a list of the tables available in this toolkit for the charge radiuus and
    print them all on the prompt.  These tables are the following
    ones: '2013-Ahm'.

    :return: The list of tables.
    :rtype: list[str].
    """
    #
    if nuda.env.verb: print("\nEnter re2L_exp_tables()")
    #
    tables = [ '2013-2L-Ahn' ]
    #
    #print('tables available in the toolkit:',tables)
    tables_lower = [ item.lower() for item in tables ]
    #print('tables available in the toolkit:',tables_lower)
    #
    if nuda.env.verb: print("Exit re2L_exp_tables()")
    #
    return tables, tables_lower

class setupRE2LExp():
   """
   Instantiate the object with binding energies given \
   from a table.

   This choice is defined in the variable `table`.

   The tables can chosen among the following ones: \
   '2013-Ahn'.

   :param table: Fix the name of `table`. Default value: '2013-Ahn'.
   :type table: str, optional. 

   **Attributes:**
   """
   #
   def __init__( self, table = '2013-2L-Ahn' ):
      """
      Parameters
      ----------
      model : str, optional
      The model to consider. Choose between: 2018 (default), , ...
      """
      #
      if nuda.env.verb: print("\nEnter setupRE2LExp()")
      #
      self.table = table
      if nuda.env.verb: print("table:",table)
      #
      tables, tables_lower = re2L_exp_tables()
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
      nuclre = []
      nuclre_err = []
      nucldre = []
      nucldre_err = []
      probe = []
      label = []
      color = []
      mark = []
      #
      if table.lower() == '2013-2l-ahn':
         #
         file_in = os.path.join(nuda.param.path_data,'hnuclei/2013-2L-Ahn.csv')
         if nuda.env.verb: print('Reads file:',file_in)
         #: Attribute providing the full reference to the paper to be citted.
         self.ref = 'J. K. Ahn, H. Akikawa, S. Aoki, K. Arai, Phys. Rev. C 88, 014003 (2013)'
         self.keyref = 'JKAhn:2013'
         #: Attribute providing additional notes about the data.
         self.note = "write here notes about this table."
         #
      #
      with open(file_in,'r') as file:
         for line in file:
            if '#' in line:
               continue
            linesplit = line.split(',')
            if len(linesplit) > 1:
               nucZ.append(linesplit[0].strip())
               nucSymb.append(linesplit[1].strip())
               nucN.append(linesplit[2].strip())
               nuclre.append(linesplit[3].strip())
               nuclre_err.append(linesplit[4].strip())
               nucldre.append(linesplit[5].strip())
               nucldre_err.append(linesplit[6].strip())
               probe.append(linesplit[6].strip().strip('\n'))
               if probe[-1] == 'emul':
                  label.append("Ahn-2013 Emul")
                  color.append('blue')
                  mark.append('s')
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
      self.A = self.Z + self.N + 2*np.ones(len(self.N),dtype=int)
      #: charge of the hypernuclei (=Z, since Lamnda is charged 0)
      self.Q = self.Z
      #: Strangness number
      self.S = -2*np.ones(len(self.N),dtype=int)
      #: symbol representing the nucleus
      self.symb = nucSymb
      #: Attribute 2L removal energy in MeV.
      self.llre = np.array( nuclre, dtype = float )
      #: Attribute 2L removal energy error in MeV.
      self.llre_err = np.array( nuclre_err, dtype = float )
      #: Attribute 2L bond energy in MeV.
      self.lldre = np.array( nucldre, dtype = float )
      #: Attribute 2L bond energy error in MeV.
      self.lldre_err = np.array( nucldre_err, dtype = float )
      #: Attribute the probe.
      self.probe = probe
      #: Attribute the label for the data referenced in figures.
      self.label = label
      #: Attribute color of points
      self.color = color
      #: marker shape
      self.mark = mark
      #
      self.nbdata = len(self.N)
      #: Attribute lbe unit.
      self.be_unit = 'MeV'
      #
      # check and print
      #
      #for i in range(self.nbdata):
      #   print('i:',i,' ell:',self.ell[i],' A:',self.A[i],' lbe:',self.lbe[i],'+-',self.lbe_err[i],' in ',self.lbe_unit)
      #
      if nuda.env.verb: print("Exit setupRE2LExp()")
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
      print("   key:",self.keyref)
      print("   label:",self.label)
      print("   note:",self.note)
      if any(self.A): print(f"   A: {self.A}")
      if any(self.Z): print(f"   Z: {self.Z}")
      if any(self.N): print(f"   N: {self.N}")
      if any(self.S): print(f"   S: {self.S}")
      if any(self.Q): print(f"   Q: {self.Q}")
      if any(self.symb): print(f" symb: {self.symb}")
      if any(self.llre): print(f" be: {self.llre}")
      if any(self.llre_err): print(f" be_err: {self.llre_err}")
      if any(self.lldre): print(f" dbe: {self.lldre}")
      if any(self.lldre_err): print(f" dbe_err: {self.lldre_err}")
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
         print(rf" index & Z & N & S & ch & symb & $RE$  & $\Delta RE$ & Ref. \\\\")
         print(rf"       &   &   &   &    &      & (MeV) & (MeV)       & \\\\")
         for ind,A in enumerate(self.A):
            print(rf" {ind} & {self.Z[ind]} & {self.N[ind]} & {self.S[ind]} & {self.Q[ind]} & {self.symb[ind]} & ${self.llre[ind]:.3f}\pm {self.llre_err[ind]:.3f}$ & ${self.lldre[ind]:.3f}\pm {self.lldre_err[ind]:.3f}$ & \\cite{{"+self.keyref+"}  \\\\")
      else:
         print(f"- No  table for source {self.table} (average). To get table, write 'verb_latex = True' in env.py.")
      #
      if nuda.env.verb: print("Exit print_latex()")
      #

