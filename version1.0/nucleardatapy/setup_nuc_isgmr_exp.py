import os
import sys
import numpy as np  # 1.15.0
import math

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def nuc_isgmr_exp_tables():
    """
    Return a list of tables available in this toolkit for the ISGMR energy and
    print them all on the prompt. These tables are the following
    ones: '2010-ISGMR-LI', '2018-ISGMR-GARG', '2018-ISGMR-GARG-LATEX'.

    :return: The list of tables.
    :rtype: list[str].    
    """
    #
    if nuda.env.verb: print("\nEnter nuc_isgmr_exp_tables()")
    #
    tables = [ '2010-ISGMR-LI', '2018-ISGMR-GARG', '2018-ISGMR-GARG-LATEX' ]
    print('tables available in the toolkit:',tables)
    tables_lower = [ item.lower() for item in tables ]
    print('tables available in the toolkit:',tables_lower)
    #
    if nuda.env.verb: print("Exit nuc_isgmr_exp_tables()")
    #
    return tables, tables_lower

class SetupNucISGMRExp():
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
      if nuda.env.verb: print("\nEnter SetupNucISGMRExp()")
      #: Attribute table.
      self.table = table
      if nuda.env.verb: print("table:",table)
      #
      #: Attribute Z (charge of the nucleus).
      self.nucZ = []
      #: Attribute A (mass of the nucleus).
      self.nucA = []
      #: Attribute the symbol of the element.
      self.nucSymbol = []
      #: Attribute energy centroid.
      self.nucM12Mm1_cent = []
      #: Attribute (+) uncertainty in the energy centroid.
      self.nucM12Mm1_errp = []
      #: Attribute (-) uncertainty in the energy centroid.
      self.nucM12Mm1_errm = []
      #
      tables, tables_lower = nuc_isgmr_exp_tables()
      #
      if table.lower() not in tables_lower:
          print('Table ',table,' is not in the list of tables.')
          print('list of tables:',tables)
          print('-- Exit the code --')
          exit()
      # dictionary
      isgmr = {}
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
         Z, A, self.nucM12Mm1_cent, self.nucM12Mm1_errp, self.nucM12Mm1_errm = \
            np.loadtxt( file_in, usecols=(0,1,2,3,4), comments='#', unpack = True )
         self.nucZ = np.array( Z, dtype=int )
         self.nucZ = np.array( list(set( self.nucZ )), dtype=int )
         self.nucA = np.array( A, dtype=int )
         #: Attribute list with + and - uncertainty
         #self.E_erra = [ self.E_errp, self.E_errm ]
         #: Attribute symmetrised uncertainty (average between + and - uncertainty).
         #self.E_errs = 0.5 * ( self.E_errp + self.E_errm )
         isgmr['Z'] = self.nucZ
         isgmr['A'] = self.nucA
         for k,ZZ in enumerate(self.nucZ):
            if str(ZZ) not in isgmr.keys():
               isgmr[str(ZZ)] = {}
            print('ZZ:',ZZ)
            symbol = nuda.param.elements[ ZZ-1 ]
            self.nucSymbol.append( symbol )
            isgmr[str(ZZ)]['symbol'] = symbol
            AA = self.nucA[k]
            print('ZZ:',ZZ,' AA:',AA,' symbol:',isgmr[str(ZZ)]['symbol'])
            print('  keys:',isgmr[str(ZZ)].keys())
            if 'A' in isgmr[str(ZZ)].keys():
               isgmr[str(ZZ)]['A'].append( AA )
            else:
               isgmr[str(ZZ)]['A'] = [ AA ]
            isgmr[str(ZZ)][str(AA)] = {}
            isgmr[str(ZZ)][str(AA)]['symbol'] = symbol
            isgmr[str(ZZ)][str(AA)]['M12Mm1'] = {}
            isgmr[str(ZZ)][str(AA)]['M12Mm1']['cent'] = self.nucM12Mm1_cent[k]
            isgmr[str(ZZ)][str(AA)]['M12Mm1']['errp'] = self.nucM12Mm1_errp[k]
            isgmr[str(ZZ)][str(AA)]['M12Mm1']['errm'] = self.nucM12Mm1_errm[k]
         #
      elif table.lower() == '2018-isgmr-garg':
         #
         file_in = os.path.join(nuda.param.path_data,'nuclei/isgmr/2018-ISGMR-Garg.dat')
         if nuda.env.verb: print('Reads file:',file_in)
         self.ref = 'U. Garg and G. Colo, Prog. Part. Nucl. Phys. 101, 55 (2018)'
         self.label = 'Garg-Colo-2018'
         self.note = "write here notes about this table."
         Z, A, self.nucM12Mm1_cent, self.nucM12Mm1_errp, self.nucM12Mm1_errm = \
            np.loadtxt( file_in, usecols=(0,1,2,3,4), comments='#', unpack = True )
         self.nucZ = np.array( Z, dtype=int )
         self.nucZ = np.array( list(set( self.nucZ )), dtype=int )
         self.nucA = np.array( A, dtype=int )
         #self.nucE_erra = [ self.E_errp, self.E_errm ]
         #self.nucE_errs = 0.5 * ( self.E_errp + self.E_errm )
         isgmr['Z'] = self.nucZ
         isgmr['A'] = self.nucA
         for k,ZZ in enumerate(self.nucZ):
            isgmr[str(ZZ)] = {}
            symbol = nuda.param.elements[ ZZ-1 ]
            self.nucSymbol.append( symbol )
            isgmr[str(ZZ)]['symbol'] = symbol
            AA = self.nucA[k]
            print('ZZ:',ZZ,' AA:',AA,' symbol:',isgmr[str(ZZ)]['symbol'])
            if 'A' in isgmr[str(ZZ)].keys():
               isgmr[str(ZZ)]['A'].append( AA )
            else:
               isgmr[str(ZZ)]['A'] = [ AA ]
            isgmr[str(ZZ)][str(AA)] = {}
            isgmr[str(ZZ)][str(AA)]['symbol'] = symbol
            isgmr[str(ZZ)][str(AA)]['M12Mm1'] = {}
            isgmr[str(ZZ)][str(AA)]['M12Mm1']['cent'] = self.nucM12Mm1_cent[k]
            isgmr[str(ZZ)][str(AA)]['M12Mm1']['errp'] = self.nucM12Mm1_errp[k]
            isgmr[str(ZZ)][str(AA)]['M12Mm1']['errm'] = self.nucM12Mm1_errm[k]
         #
      elif table.lower() == '2018-isgmr-garg-latex':
         #
         file_in = os.path.join(nuda.param.path_data,'nuclei/isgmr/2018-ISGMR-Garg.tex')
         if nuda.env.verb: print('Reads file:',file_in)
         self.ref = 'U. Garg and G. Colo, Prog. Part. Nucl. Phys. 101, 55 (2018)'
         self.label = 'Garg-Colo-2018'
         self.note = "Parameters of the ISGMR peaks and moment ratios of the ISGMR strength distributions in stable nuclei as reported by the TAMU and RCNP groups. The probes employed in the measurements are listed for each case. Entries marked with $\\star$ indicate that the $\\Gamma$ is an RMS width, not that of a fitted peak. Entries marked with $\\dagger$ indicate a multimodal strength distribution; in those cases the parameters for only the ``main'' ISGMR peak are included. For the TAMU data, the peak parameters correspond to a Gaussian fit, whereas for the RCNP  data, the corresponding parameters are for a Lorentzian fit."
         #
         nucA=[]; nucZ=[]; nucSymbol=[]; nucEprobe=[]; nucProj=[]; 
         nucE0=[]; nucE0_errp=[]; nucE0_errm=[];
         nucG=[]; nucG_errp=[]; nucG_errm=[]; 
         nucEWSR=[]; nucEWSR_errp=[]; nucEWSR_errm=[]; 
         nucM12M0=[]; nucM12M0_errp=[]; nucM12M0_errm=[]; 
         nucM12Mm1=[]; nucM12Mm1_errp=[]; nucM12Mm1_errm=[]; 
         nucM32M1=[]; nucM32M1_errp=[]; nucM32M1_errm=[];
         nucRef=[];
         nbk = 0
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
                  nucSymbol.append( nucSymbol[-1] )
                  nucA.append( nucA[-1] )
                  nucZ.append( nucZ[-1] )
               else:
                  nuc += 1
                  symbol = ele[0].split('$')[2].strip()
                  ZZ, = np.where( nuda.param.elements == symbol )[0]
                  ZZ += 1
                  nucZ.append( str( ZZ ) )
                  #print('Z=',ZZ,' symbol:',symbol,'.')
                  nucSymbol.append( symbol )
                  AA = int( ele[0].split('$')[1].strip('^').strip('{').strip('}') )
                  nucA.append( str( AA ) )
                  #print('A=',AA)
               # ele[1]: probe
               #print('ele[1]:',ele[1])
               if ele[1] == ' ' or ele[1] == '  ':
                  nucEprobe.append( None )
                  nucProj.append( None )
               else:
                  Eprobe = int( ele[1].split('MeV')[0].strip() )
                  proj = ele[1].split('-')[1].strip()
                  nucEprobe.append( Eprobe )
                  nucProj.append( proj )
               # ele[3]: E0
               cent, errp, errm = nuda.param.tex2str( ele[3] )
               nucE0.append( cent ); nucE0_errp.append( errp ); nucE0_errm.append( errm );
               # ele[3]: Gamma
               cent, errp, errm = nuda.param.tex2str( ele[4] )
               nucG.append( cent ); nucG_errp.append( errp ); nucG_errm.append( errm );
               # ele[4]: EWSR
               cent, errp, errm = nuda.param.tex2str( ele[5] )
               nucEWSR.append( cent ); nucEWSR_errp.append( errp ); nucEWSR_errm.append( errm );
               # ele[5]: nada
               # ele[6]: M12M0
               cent, errp, errm = nuda.param.tex2str( ele[7] )
               nucM12M0.append( cent ); nucM12M0_errp.append( errp ); nucM12M0_errm.append( errm );
               # ele[7]: M12Mm1
               cent, errp, errm = nuda.param.tex2str( ele[8] )
               nucM12Mm1.append( cent ); nucM12Mm1_errp.append( errp ); nucM12Mm1_errm.append( errm );
               # ele[8]: M32M1
               cent, errp, errm = nuda.param.tex2str( ele[9] )
               nucM32M1.append( cent ); nucM32M1_errp.append( errp ); nucM32M1_errm.append( errm );
               # ele[9]: nada
               # ele[10]: ref
               nucRef.append( ele[11] )
               #print('nuc:',nuc,nucA,nucSymbol,nucProbe,nucTarget,nucG,nucEWSR,nucM12M0,nucM12Mm1,nucM32M1,nucRef)
               #exit()
               nbk += 1
         #
         nbk -= 1
         print('\nnumber of nuclei:',nuc)
         print('\nnumber of entries:',nbk)
         #
         isgmr['Z'] = np.array( sorted(set( nucZ[0:-2] )), dtype=int )
         isgmr['A'] = np.array( nucA[0:-2], dtype=int )
         #self.nucZ = nucZ
         self.nucZ = np.array( sorted(set( nucZ[0:-2] )), dtype=int )
         self.nucA = np.array( nucA[0:-2], dtype=int )
         self.nucSymbol = nucSymbol
         self.nucM12Mm1_cent = nucM12Mm1
         self.nucM12Mm1_errp = nucM12Mm1_errp
         self.nucM12Mm1_errm = nucM12Mm1_errm
         k = 0
         while k < nbk:
            ZZ = str( nucZ[k] )
            AA = str( nucA[k] )
            if ZZ not in isgmr.keys():
               isgmr[ZZ] = {}
            if 'A' not in isgmr[ZZ].keys():
               isgmr[ZZ]['A'] = []
            isgmr[ZZ]['symbol'] = nucSymbol[k]
            for l in range(k+1,nbk+1):
               if int(nucZ[l]) != int(nucZ[k]) or int(nucA[l]) != int(nucA[k]):
                  break
            kend = l
            x = slice( k, kend )
            k = kend
            isgmr[ZZ][AA] = {}
            isgmr[ZZ]['A'] = isgmr[ZZ]['A'] + nucA[x]
            isgmr[ZZ][AA]['A'] = nucA[x]
            isgmr[ZZ][AA]['Eprobe'] = nucEprobe[x]
            isgmr[ZZ][AA]['proj'] = nucProj[x]
            isgmr[ZZ][AA]['E0'] = {}
            isgmr[ZZ][AA]['E0']['cent'] = nucE0[x]
            isgmr[ZZ][AA]['E0']['errp'] = nucE0_errp[x] 
            isgmr[ZZ][AA]['E0']['errm'] = nucE0_errm[x]
            isgmr[ZZ][AA]['G'] = {}
            isgmr[ZZ][AA]['G']['cent'] = nucG[x]
            isgmr[ZZ][AA]['G']['errp'] = nucG_errp[x]
            isgmr[ZZ][AA]['G']['errm'] = nucG_errm[x]
            isgmr[ZZ][AA]['EWSR'] = {}
            isgmr[ZZ][AA]['EWSR']['cent'] = nucEWSR[x]
            isgmr[ZZ][AA]['EWSR']['errp'] = nucEWSR_errp[x]
            isgmr[ZZ][AA]['EWSR']['errm'] = nucEWSR_errm[x]
            isgmr[ZZ][AA]['M12M0'] = {}
            isgmr[ZZ][AA]['M12M0']['cent'] = nucM12M0[x]
            isgmr[ZZ][AA]['M12M0']['errp'] = nucM12M0_errp[x]
            isgmr[ZZ][AA]['M12M0']['errm'] = nucM12M0_errm[x]
            isgmr[ZZ][AA]['M12Mm1'] = {}
            isgmr[ZZ][AA]['M12Mm1']['cent'] = nucM12Mm1[x]
            isgmr[ZZ][AA]['M12Mm1']['errp'] = nucM12Mm1_errp[x]
            isgmr[ZZ][AA]['M12Mm1']['errm'] = nucM12Mm1_errm[x]
            isgmr[ZZ][AA]['M32M1'] = {}
            isgmr[ZZ][AA]['M32M1']['cent'] = nucM32M1[x]
            isgmr[ZZ][AA]['M32M1']['errp'] = nucM32M1_errp[x]
            isgmr[ZZ][AA]['M32M1']['errm'] = nucM32M1_errm[x]
            isgmr[ZZ][AA]['ref'] = nucRef[x]
      self.isgmr = isgmr
      #
      print('\nkeys():',list(isgmr.keys()))
      print('\nZ:',isgmr['Z'])
      print('\nA:',isgmr['A'])
      for Z in self.isgmr['Z']:
         print('For Z:',Z,' A:',self.isgmr[str(Z)]['A'])
      #print('\nnucA:',self.nucA)
      #print('\nnucSymbol:',self.nucSymbol)
      #print('\nM12Mm1:',self.nucM12Mm1_cent)
      #print('\nM12Mm1_errp:',self.nucM12Mm1_errp)
      #print('\nM12Mm1_errm:',self.nucM12Mm1_errm)
      #
      #: Attribute energy unit.
      self.E_unit = 'MeV'
      #
      if nuda.env.verb: print("Exit SetupNucISGMRExp()")
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
      print('\nZ:',self.isgmr['Z'])
      print('\nA:',self.isgmr['A'])
      for Z in self.isgmr['Z']:
         print('For Z:',Z,' A:',self.isgmr[str(Z)]['A'])
         for A in self.isgmr[str(Z)]['A']:
            print('Centroid energy:',self.isgmr[str(Z)][str(A)]['M12Mm1']['cent'])
            print('   with errp:',self.isgmr[str(Z)][str(A)]['M12Mm1']['errp'])
            print('   with errm:',self.isgmr[str(Z)][str(A)]['M12Mm1']['errm'])
      #
      if nuda.env.verb: print("Exit print_outputs()")
      #
