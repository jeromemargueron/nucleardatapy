import os
import sys
import numpy as np  # 1.15.0
import math

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def tables_isgmr():
    """
    Return a list of tables available in this toolkit for the ISGMR energy and
    print them all on the prompt. These tables are the following
    ones: '2010-ISGMR-LI', '2018-ISGMR-GARG', '2018-ISGMR-GARG-LATEX'.

    :return: The list of tables.
    :rtype: list[str].    
    """
    #
    if nuda.env.verb: print("\nEnter tables_isgmr()")
    #
    tables = [ '2010-ISGMR-LI', '2018-ISGMR-GARG', '2018-ISGMR-GARG-LATEX' ]
    print('tables available in the toolkit:',tables)
    tables_lower = [ item.lower() for item in tables ]
    print('tables available in the toolkit:',tables_lower)
    #
    if nuda.env.verb: print("Exit tables_isgmr()")
    #
    return tables, tables_lower

class SetupISGMR():
   """
   Instantiate the object with microscopic results choosen \
   by the toolkit practitioner. \

   This choice is defined in the variable `table`.

   The `table` can chosen among the following ones: \
   '2010-ISGMR-LI', '2018-ISGMR-GARG'.

   :param table: Fix the name of `table`. Default value: '2018-ISGMR-GARG', '2018-ISGMR-GARG-LATEX'.
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
      if nuda.env.verb: print("\nEnter SetupISGMR()")
      #: Attribute table.
      self.table = table
      if nuda.env.verb: print("table:",table)
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
         file_in = os.path.join(nuda.param.path_data,'nuclei/isgmr/2010-ISGMR-Li.dat')
         if nuda.env.verb: print('Reads file:',file_in)
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
         file_in = os.path.join(nuda.param.path_data,'nuclei/isgmr/2018-ISGMR-Garg.dat')
         if nuda.env.verb: print('Reads file:',file_in)
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
      elif table.lower() == '2018-isgmr-garg-latex':
         #
         file_in = os.path.join(nuda.param.path_data,'nuclei/isgmr/2018-ISGMR-Garg.tex')
         if nuda.env.verb: print('Reads file:',file_in)
         self.ref = 'U. Garg and G. Colo, Prog. Part. Nucl. Phys. 101, 55 (2018)'
         self.label = 'Garg-Colo-2018'
         self.note = "Parameters of the ISGMR peaks and moment ratios of the ISGMR strength distributions in stable nuclei as reported by the TAMU and RCNP groups. The probes employed in the measurements are listed for each case. Entries marked with $\star$ indicate that the $\Gamma$ is an RMS width, not that of a fitted peak. Entries marked with $\dagger$ indicate a multimodal strength distribution; in those cases the parameters for only the ``main'' ISGMR peak are included. For the TAMU data, the peak parameters correspond to a Gaussian fit, whereas for the RCNP  data, the corresponding parameters are for a Lorentzian fit."
         #
         nucA=[]; nucSymbol=[]; nucProbe=[]; nucTarget=[]; 
         nucE0=[]; nucE0_err=[]; nucE0_errp=[]; nucE0_errm=[];
         nucG=[]; 
         nucEWSR=[]; nucM12M0=[]; nucM12Mm1=[]; nucM32M1=[];nucRef=[];
         nuc = -1
         with open(file_in,'r') as file:
            for line in file:
               #print('line:',line)
               if '#' in line[0]: 
                  continue
               ele = line.split('&')
               #print('ele:',ele)
               # ele[0]: nucleus
               if ele[0] == '  ' or ele[0] == ' ':
                  nucSymbol.append( None )
                  nucA.append( None )
               else:
                  nuc += 1
                  nucSymbol.append( ele[0].split('$')[2] )
                  nucA.append( ele[0].split('$')[1].split('{')[1].split('}')[0] )
               # ele[1]: probe
               #print('ele[1]:',ele[1])
               if ele[1] == '  ':
                  nucProbe.append( 'unknown' )
                  nucTarget.append( 'unknown' )
               else:
                  nucProbe.append( ele[1].split('MeV')[0] )
                  nucTarget.append( ele[1].split('-')[1] )
               # ele[3]: E0
               #print('ele[3]:',ele[3])
               if '\pm' in ele[3]:
                  nucE0.append( ele[3].split('\pm')[0][2:] )
                  nucE0_err.append( ele[3].split('\pm')[1] )
                  nucE0_errp.append( nucE0_err[-1] )
                  nucE0_errm.append( nucE0_err[-1] )
               elif '^' in ele[3]:
                  nucE0.append( ele[3].split('^')[0][3:-1] )
                  nucE0_errp.append( ele[3].split('^')[1].split('_')[0][1:-2] )
                  nucE0_errm.append( ele[3].split('^')[1].split('_')[1][1:-3] )
                  nucE0_err.append( str( math.sqrt( float(nucE0_errp[-1])**2 + float(nucE0_errm[-1])**2 ) ) )
               else:
                  nucE0.append( None )
                  nucE0_err.append( None )
                  nucE0_errp.append( None )
                  nucE0_errm.append( None )                  
               # ele[3]: Gamma
               nucG.append( ele[4] )
               # ele[4]: EWSR
               nucEWSR.append( ele[5] )
               # ele[5]: nada
               # ele[6]: M12M0
               nucM12M0.append( ele[7] )
               # ele[7]: M12Mm1
               nucM12Mm1.append( ele[8] )
               # ele[8]: M32M1
               nucM32M1.append( ele[9] )
               # ele[9]: nada
               # ele[10]: ref
               nucRef.append( ele[11] )
               #print('nuc:',nuc,nucA,nucSymbol,nucProbe,nucTarget,nucG,nucEWSR,nucM12M0,nucM12Mm1,nucM32M1,nucRef)
         #
         print('\nnumber of nuclei:',nuc)
         print('\nnuc:',nuc)
         print('\nnucA:',nucA)
         print('\nnucSymbol:',nucSymbol)
         print('\nE0:',nucE0)
         print('\nE0_err:',nucE0_err)
         print('\nE0_errp:',nucE0_errp)
         print('\nE0_errm:',nucE0_errm)
         print('\nM12Mm1:',nucM12Mm1)
      #: Attribute energy unit.
      self.E_unit = 'MeV'
      #
      if nuda.env.verb: print("Exit SetupISGMR()")
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
      if any(self.E_cen): print(f"   E: {self.E_cen}")
      if any(self.E_errp): print(f"   E_errp: {self.E_errp}")
      if any(self.E_errm): print(f"   E_errm: {self.E_errm}")
      #
      if nuda.env.verb: print("Exit print_outputs()")
      #
