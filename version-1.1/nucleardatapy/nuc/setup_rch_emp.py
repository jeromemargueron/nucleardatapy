import os
import sys
import numpy as np  # 1.15.0

import nucleardatapy as nuda

def rch_emp_formulas( ):
   """
   Return the list of empirical formulas encoded in nuda.
   :return: The list of formulas.
   :rtype: list[str].
   """
   #
   if nuda.env.verb: print("\nEnter rch_emp_formulas()")
   #
   formulas = [ 'classic', 'liquid-drop', 'exponent', '1961-Elton', '1994-NPP', '2004-Angeli', \
   '2004-Angeli-core', '2013-BAKS-1', '2013-BAKS-2', '2013-BAKS-3'  ]
   #
   #print('formulas available in the toolkit:',formulas)
   formulas_lower = [ item.lower() for item in formulas ]
   #print('formulas available in the toolkit (lower case):',formulas_lower)
   #
   if nuda.env.verb: print("Exit rch_emp_formulas()")
   #
   return formulas, formulas_lower


class setupRchEmp():
   """
   Instantiate the object with charge radii.

   This choice is defined in the variable `formula`.

   The formulas can chosen among the following ones: \
   'classic', 'liquid-drop', 'exponent', '1961-Elton', '1994-NPP', '2004-Angeli', \
   '2004-Angeli-core', '2013-BAKS-1', '2013-BAKS-2', '2013-BAKS-3'

   **Attributes:**
   """
   #
   def __init__( self, A = 208, Z = 82, formula = 'liquid-drop' ):
      """
      Return charge radii for (A,Z) nucleus using empirical expression defined in formula.

      Parameters
      ----------
      :param A: Fix the mass of the nucleus. Default value: 208.
      :type A: int or real, optional. 
      :param Z: Fix the charge of the nucleus. Default value: 82.
      :type Z: int or real, optional. 
      :param formula: Fix the name of `formula`. Default value: 'liquid-drop'.
      :type formula: str, optional. 
      """
      #
      if nuda.env.verb: print("\nEnter setupRchEmp()")
      #
      self.formula = formula
      if nuda.env.verb: print("formula:",formula)
      #
      print(' A:',A,' size:',np.size(A))
      print(' Z:',Z,' size:',np.size(Z))
      #
      #: Attribute A (mass of the nucleus).
      if np.size(A) > 1:
         self.nucA = np.array( [ int(ele) for ele in A ] )
      else:
         self.nucA = np.array( [ A ] )
      #: Attribute Z (charge of the nucleus).
      if np.size(Z) > 1:
         self.nucZ = np.array( [ int(ele) for ele in Z ] )
      else:
         self.nucZ = np.array( [ Z ] )
      #: Attribute N (number of neutrons of the nucleus).
      self.nucN = self.nucA - self.nucZ
      #: Attribue R_ch (charge radius) in fm.
      self.nucRch = []
      #
      formulas, formulas_lower = rch_emp_formulas()
      #
      if formula.lower() not in formulas_lower:
         print('setup_rch_emp: formula ',formula,' is not in the list of formulas.')
         print('setup_rch_emp: list of formulas:',formulas)
         print('setup_rch_emp: -- Exit the code --')
         exit()
      #
      rch = []
      #
      for indA,AA in enumerate(self.nucA):
         #
         ZZ = self.nucZ[indA]
         NN = AA - ZZ
         if formula == 'classic':
            #: Attribute providing the full reference to the paper to be citted.
            self.ref = ''
            #: Attribute providing additional notes about the data.
            self.note = "write here notes about this rch formula."
            #: Attribute providing the label the data is references for figures.
            self.label = 'empirical(classic)'
            r0 = 1.2
            a = 0.0
            b = 0.0
            c = 0.0
            r1 = 0.0
            r2 = 0.0
            gamma = 0.3333
         elif formula == 'liquid-drop':
            # I. Angeli, Atomic Data and Nuclear Data Tables 87, 185 (2004)
            #: Attribute providing the full reference to the paper to be citted.
            self.ref = 'I. Angeli, Atomic Data and Nuclear Data Tables 87, 185 (2004)'
            #: Attribute providing additional notes about the data.
            self.note = "write here notes about this rch formula."
            #: Attribute providing the label the data is references for figures.
            self.label = 'empirical(liquid-drop)'
            r0 = 0.9542
            a = 0.0
            b = 0.0
            c = 0.0
            r1 = 0.0
            r2 = 0.0
            gamma = 0.3333
         elif formula == 'exponent':
            # I. Angeli, Atomic Data and Nuclear Data Tables 87, 185 (2004)
            #: Attribute providing the full reference to the paper to be citted.
            self.ref = 'I. Angeli, Atomic Data and Nuclear Data Tables 87, 185 (2004)'
            #: Attribute providing additional notes about the data.
            self.note = "write here notes about this rch formula."
            #: Attribute providing the label the data is references for figures.
            self.label = 'empirical(exponent)'
            r0 = 1.153
            a = 0.0
            b = 0.0
            c = 0.0
            r1 = 0.0
            r2 = 0.0
            gamma = 0.2938
         elif formula == '1961-Elton':
            # L.R.B. Elton, Nuclear sizes, Oxford University Press, Oxford, 1961
            #: Attribute providing the full reference to the paper to be citted.
            self.ref = 'L.R.B. Elton, Nuclear sizes, Oxford University Press, Oxford, 1961'
            #: Attribute providing additional notes about the data.
            self.note = "write here notes about this rch formula."
            #: Attribute providing the label the data is references for figures.
            self.label = 'empirical(1961-Elton)'
            r0 = 0.9071
            a = 0.0
            b = 0.0
            c = 0.0
            r1 = 1.105
            r2 = -0.548
            gamma = 0.3333
         elif formula == '1994-NPP':
            # B. Nerlo-Pomorska and K. Pomorski, Z. Phys. A 348, 169 (1994)
            #: Attribute providing the full reference to the paper to be citted.
            self.ref = 'B. Nerlo-Pomorska and K. Pomorski, Z. Phys. A 348, 169 (1994)'
            #: Attribute providing additional notes about the data.
            self.note = "write here notes about this rch formula."
            #: Attribute providing the label the data is references for figures.
            self.label = 'empirical(1994-NPP)'
            r0 = 1.240
            a = 0.0
            b = 0.191
            c = 1.646
            r1 = 0.0
            r2 = 0.0
            gamma = 0.3333
         elif formula == '2004-Angeli':
            # I. Angeli, Atomic Data and Nuclear Data Tables 87, 185 (2004)
            #: Attribute providing the full reference to the paper to be citted.
            self.ref = 'I. Angeli, Atomic Data and Nuclear Data Tables 87, 185 (2004)'
            #: Attribute providing additional notes about the data.
            self.note = "write here notes about this rch formula."
            #: Attribute providing the label the data is references for figures.
            self.label = 'empirical(2004-Angeli)'
            if ZZ < 14:
               # For light nuclei Z<14
               r0 = 0.982
               a = 3.93
               r1 = 0.32
               r2 = 0.55
            else:
               # heavier nuclei
               r0 = 0.8966
               a = 0.0809
               r1 = 1.128
               r2 = -0.58
            # for all
            b = 0.0
            c = 0.0
            gamma = 0.3333
         elif formula == '2004-Angeli-core':
            # I. Angeli, Atomic Data and Nuclear Data Tables 87, 185 (2004)
            #: Attribute providing the full reference to the paper to be citted.
            self.ref = 'I. Angeli, Atomic Data and Nuclear Data Tables 87, 185 (2004)'
            #: Attribute providing additional notes about the data.
            self.note = "write here notes about this rch formula."
            #: Attribute providing the label the data is references for figures.
            self.label = 'empirical(2004-Angeli-core)'
            if ZZ < 14:
               # For light nuclei Z<14
               r0 = 0.982
               r1 = 0.32
               r2 = 0.55
            else:
               # heavier nuclei
               r0 = 0.8966
               r1 = 1.128
               r2 = -0.58
            # for all
            a = 0.0
            b = 0.0
            c = 0.0
            gamma = 0.3333
         elif formula == '2013-BAKS-1':
            # T. Bayram, S. Akkoyun, S. Okan Kara, A. Sinan, Acta Phys. Pol. B 44, 1791 (2013)
            #: Attribute providing the full reference to the paper to be citted.
            self.ref = 'T. Bayram, S. Akkoyun, S. Okan Kara, A. Sinan, Acta Phys. Pol. B 44, 1791 (2013)'
            #: Attribute providing additional notes about the data.
            self.note = "write here notes about this rch formula."
            #: Attribute providing the label the data is references for figures.
            self.label = 'empirical(2013-BAKS-1)'
            r0 = 0.951
            a = 0.0
            b = 0.0
            c = 0.0
            r1 = 0.0
            r2 = 0.0
            gamma = 0.3333
         elif formula == '2013-BAKS-2':
            # T. Bayram, S. Akkoyun, S. Okan Kara, A. Sinan, Acta Phys. Pol. B 44, 1791 (2013)
            #: Attribute providing the full reference to the paper to be citted.
            self.ref = 'T. Bayram, S. Akkoyun, S. Okan Kara, A. Sinan, Acta Phys. Pol. B 44, 1791 (2013)'
            #: Attribute providing additional notes about the data.
            self.note = "write here notes about this rch formula."
            #: Attribute providing the label the data is references for figures.
            self.label = 'empirical(2013-BAKS-2)'
            r0 = 0.996
            a = 0.0
            b = 0.278
            c = 0.0
            r1 = 0.0
            r2 = 0.0
            gamma = 0.3333
         elif formula == '2013-BAKS-3':
            # T. Bayram, S. Akkoyun, S. Okan Kara, A. Sinan, Acta Phys. Pol. B 44, 1791 (2013)
            #: Attribute providing the full reference to the paper to be citted.
            self.ref = 'T. Bayram, S. Akkoyun, S. Okan Kara, A. Sinan, Acta Phys. Pol. B 44, 1791 (2013)'
            #: Attribute providing additional notes about the data.
            self.note = "write here notes about this rch formula."
            #: Attribute providing the label the data is references for figures.
            self.label = 'empirical(2013-BAKS-3)'
            r0 = 0.966
            a = 0.0
            b = 0.182
            c = 1.652
            r1 = 0.0
            r2 = 0.0
            gamma = 0.3333
         else:
            print('setup_rch_theo: formula is badly defined ',formula)
            print('setup_rch_theo: exit')
            exit()
         if a != 0.0:
            # core
            ZM = [ 2, 6, 14, 28, 50, 82, 114 ]
            NM = [ 2, 8, 14, 28, 50, 82, 126, 184 ]
            Zlist = ZM - ZZ*np.ones( len(ZM) ); Nlist = NM - NN*np.ones( len(NM) )
            for indZ,Ztest in enumerate(Zlist):
               if Ztest >= 0: 
                  Zcore = ZM[indZ-1]
                  break
            for indN,Ntest in enumerate(Nlist):
               if Ntest >= 0: 
                  Ncore = NM[indN-1]
                  break
            Acore = Zcore + Ncore
            Np = ZZ - Zcore; Nn = NN - Ncore
            print(' for A:',AA,' Z:',ZZ,' N:',NN)
            print('        Zlist:',Zlist)
            print('        Nlist:',Nlist)
            print('        Zcore:',Zcore,' Ncore:',Ncore)
            print('        Np:',Np,' Nn:',Nn)
            if Np == 0 and Nn == 0:
               Prom = 0.0
               facA = 0.0
            else:
               Prom = Np * Nn / ( Np + Nn )
               # radius of the core nucleus
               R0P = setupRchEmp( Acore, Zcore, formula='2004-Angeli-core' )
               print('        Prom:',Prom,' R0P:',R0P.nucRch[0])
               facA = Prom / R0P.nucRch[0]
         else:
            facA = 0.0
         #
         #rchA = ( 1.19 - 0.8 * (1-2*Z/A)**2 ) * A**0.3333 - 0.3* A**0.1666
         rchA = r0 * ( 1.0 - b * (1.0-2.0*ZZ/AA) + c / AA  + r1/r0 / AA**0.6666 + r2/r0 / AA**1.3333  ) * AA**gamma + a*facA
         rch.append( rchA )
      #
      self.nucRch = np.array( rch, dtype=float )
      #: Attribute radius unit.
      self.Rch_unit = 'fm'
      #
      if nuda.env.verb: print("Exit setupChEmp()")
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
      print("   formula:",self.formula)
      print("   ref:",self.ref)
      print("   label:",self.label)
      print("   note:",self.note)
      if any(self.nucA): print(f"   A: {self.nucA}")
      if any(self.nucZ): print(f"   Z: {self.nucZ}")
      if any(self.nucRch): print(f"   Rch: {self.nucRch}")
      #
      if nuda.env.verb: print("Exit print_outputs()")
      #
