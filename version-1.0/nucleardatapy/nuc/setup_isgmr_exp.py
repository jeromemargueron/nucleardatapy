import os
import sys
import numpy as np  # 1.15.0
import math

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def isgmr_exp_tables():
    """
    Return a list of tables available in this toolkit for the ISGMR energy and
    print them all on the prompt. These tables are the following
    ones: '2010-ISGMR-LI', '2018-ISGMR-GARG', '2018-ISGMR-GARG-LATEX'.

    :return: The list of tables.
    :rtype: list[str].    
    """
    #
    if nuda.env.verb: print("\nEnter isgmr_exp_tables()")
    #
    tables = [ '2010-ISGMR-LI', '2018-ISGMR-GARG', '2018-ISGMR-GARG-few', '2022-ISGMR-average' ]
    #print('tables available in the toolkit:',tables)
    tables_lower = [ item.lower() for item in tables ]
    #print('tables available in the toolkit:',tables_lower)
    #
    if nuda.env.verb: print("Exit isgmr_exp_tables()")
    #
    return tables, tables_lower

class setupISGMRExp():
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
      if nuda.env.verb: print("\nEnter setupISGMRExp()")
      #: Attribute table.
      self.table = table
      if nuda.env.verb: print("table:",table)
      #
      tables, tables_lower = isgmr_exp_tables()
      #
      if table.lower() not in tables_lower:
          print('Table ',table,' is not in the list of tables.')
          print('list of tables:',tables)
          print('-- Exit the code --')
          exit()
      #
      nucA=[]; nucZ=[]; nucN=[]; nucSymbol=[]; nucEprobe=[]; nucProj=[]; 
      nucE0=[]; nucE0_errp=[]; nucE0_errm=[];
      nucG=[]; nucG_errp=[]; nucG_errm=[]; 
      nucEWSR=[]; nucEWSR_errp=[]; nucEWSR_errm=[]; 
      nucM12M0=[]; nucM12M0_errp=[]; nucM12M0_errm=[]; 
      nucM12Mm1=[]; nucM12Mm1_errp=[]; nucM12Mm1_errm=[]; 
      nucM32M1=[]; nucM32M1_errp=[]; nucM32M1_errm=[];
      nucRef=[];
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
         nucZ, nucA, nucM12Mm1, nucM12Mm1_errp, nucM12Mm1_errm = \
            np.loadtxt( file_in, usecols=(0,1,4,5,6), comments='#', unpack = True )
         nucN = nucA - nucZ
         for k,Z in enumerate(nucZ):
            nucSymbol.append( nuda.param.elements[int(Z)-1] )
            nucEprobe.append( '386' )
            nucProj.append( '$\alpha$' )
            nucE0.append( None ); nucE0_errp.append( None ); nucE0_errm.append( None )
            nucG.append( None ); nucG_errp.append( None ); nucG_errm.append( None )
            nucEWSR.append( None ); nucEWSR_errp.append( None ); nucEWSR_errm.append( None )
            nucM12M0.append( None ); nucM12M0_errp.append( None ); nucM12M0_errm.append( None )
            nucM32M1.append( None ); nucM32M1_errp.append( None ); nucM32M1_errm.append( None )
         nuc = len( nucZ ); nbk = nuc
         #
      elif table.lower() == '2018-isgmr-garg-few':
         #
         file_in = os.path.join(nuda.param.path_data,'nuclei/isgmr/2018-ISGMR-Garg.dat')
         if nuda.env.verb: print('Reads file:',file_in)
         self.ref = 'U. Garg and G. Colo, Prog. Part. Nucl. Phys. 101, 55 (2018)'
         self.label = 'Garg-Colo-2018-few'
         self.note = "write here notes about this table."
         nucZ, nucA, nucM12Mm1, nucM12Mm1_errp, nucM12Mm1_errm = \
            np.loadtxt( file_in, usecols=(0,1,2,3,4), comments='#', unpack = True )
         nucN = nucA - nucZ
         #print('elements:',nuda.param.elements)
         for k,Z in enumerate(nucZ):
            nucSymbol.append( nuda.param.elements[int(Z)-1] )
            nucEprobe.append( '100' )
            nucProj.append( '$\alpha$' )
            nucE0.append( None ); nucE0_errp.append( None ); nucE0_errm.append( None )
            nucG.append( None ); nucG_errp.append( None ); nucG_errm.append( None )
            nucEWSR.append( None ); nucEWSR_errp.append( None ); nucEWSR_errm.append( None )
            nucM12M0.append( None ); nucM12M0_errp.append( None ); nucM12M0_errm.append( None )
            nucM32M1.append( None ); nucM32M1_errp.append( None ); nucM32M1_errm.append( None )
         nuc = len( nucZ ); nbk = nuc
         #
      elif table.lower() == '2018-isgmr-garg':
         #
         file_in = os.path.join(nuda.param.path_data,'nuclei/isgmr/2018-ISGMR-Garg.tex')
         if nuda.env.verb: print('Reads file:',file_in)
         self.ref = 'U. Garg and G. Colo, Prog. Part. Nucl. Phys. 101, 55 (2018)'
         self.label = 'Garg-Colo-2018'
         self.note = "Parameters of the ISGMR peaks and moment ratios of the ISGMR strength distributions in stable nuclei as reported by the TAMU and RCNP groups. The probes employed in the measurements are listed for each case. Entries marked with $\\star$ indicate that the $\\Gamma$ is an RMS width, not that of a fitted peak. Entries marked with $\\dagger$ indicate a multimodal strength distribution; in those cases the parameters for only the ``main'' ISGMR peak are included. For the TAMU data, the peak parameters correspond to a Gaussian fit, whereas for the RCNP  data, the corresponding parameters are for a Lorentzian fit."
         #
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
                  nucN.append( nucN[-1] )
               else:
                  nuc += 1
                  symbol = ele[0].split('$')[2].strip()
                  ZZ, = np.where( nuda.param.elements == symbol )[0] + 1
                  AA = int( ele[0].split('$')[1].strip('^').strip('{').strip('}') )
                  NN = AA - ZZ
                  #ZZ += 1
                  #print('Z=',ZZ,' symbol:',symbol,' A=',AA,' N=',NN)
                  nucSymbol.append( symbol )
                  nucA.append( str( AA ) )
                  nucZ.append( str( ZZ ) )
                  nucN.append( str( NN ) )
                  #print('A=',AA)
               #print('Z=',nucZ[-1],' symbol:',nucSymbol[-1],' A=',nucA[-1],' N=',nucN[-1])
               # ele[1]: probe
               #print('ele[1]:',ele[1])
               if ele[1] == ' ' or ele[1] == '  ':
                  nucEprobe.append( nucEprobe[-1] )
                  nucProj.append( nucProj[-1] )
               else:
                  Eprobe = int( ele[1].split('MeV-')[0].strip() )
                  proj = ele[1].split('MeV-')[1].strip()
                  nucEprobe.append( Eprobe )
                  nucProj.append( proj )
               #print('Z=',nucZ[-1],' symbol:',nucSymbol[-1],' A=',nucA[-1],' N=',nucN[-1],' Eprobe=',nucEprobe[-1],' proj:',nucProj[-1])
               # ele[3]: E0
               cent, errp, errm = nuda.param.tex2str( ele[3] )
               nucE0.append( cent ); nucE0_errp.append( errp ); nucE0_errm.append( errm );
               #print('Z=',nucZ[-1],' symbol:',nucSymbol[-1],' A=',nucA[-1],' N=',nucN[-1],' Eprobe=',nucEprobe[-1],' proj:',nucProj[-1],' E0:',nucE0[-1],nucE0_errp[-1],nucE0_errm[-1])
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
               print('nbk:',nbk,' nuc:',nuc,' Z=',nucZ[-1],' symbol:',nucSymbol[-1],' A=',nucA[-1],' N=',nucN[-1],' Eprobe=',nucEprobe[-1],' proj:',nucProj[-1],' E0:',nucE0[-1],nucE0_errp[-1],nucE0_errm[-1])
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
         #
      elif table.lower() == '2022-isgmr-average':
         #
         file_in = os.path.join(nuda.param.path_data,'nuclei/isgmr/2022-ISGMR-average.dat')
         if nuda.env.verb: print('Reads file:',file_in)
         self.ref = 'U. Garg and G. Colo, Prog. Part. Nucl. Phys. 101, 55 (2018)'
         self.label = 'Average-2022'
         self.note = "write here notes about this table."
         nucZ, nucA, nucM12Mm1, nucM12Mm1_errp, nucM12Mm1_errm = \
            np.loadtxt( file_in, usecols=(0,1,2,3,4), comments='#', unpack = True )
         nucN = nucA - nucZ
         #print('elements:',nuda.param.elements)
         for k,Z in enumerate(nucZ):
            nucSymbol.append( nuda.param.elements[int(Z)-1] )
            nucEprobe.append( '100' )
            nucProj.append( '$\alpha$' )
            nucE0.append( None ); nucE0_errp.append( None ); nucE0_errm.append( None )
            nucG.append( None ); nucG_errp.append( None ); nucG_errm.append( None )
            nucEWSR.append( None ); nucEWSR_errp.append( None ); nucEWSR_errm.append( None )
            nucM12M0.append( None ); nucM12M0_errp.append( None ); nucM12M0_errm.append( None )
            nucM32M1.append( None ); nucM32M1_errp.append( None ); nucM32M1_errm.append( None )
         nuc = len( nucZ ); nbk = nuc
      #
      print('\nnumber of different nuclei:',nuc)
      print('\nnumber of total entries:   ',nbk)
      #
      isgmr = {}
      isgmr['A'] = nucA; isgmr['Z'] = nucZ; isgmr['N'] = nucN; isgmr['symbol'] = nucSymbol
      isgmr['Eprobe'] = nucEprobe; isgmr['proj'] = nucProj
      isgmr['E0'] = nucE0; isgmr['E0_errp'] = nucE0_errp; isgmr['E0_errm'] = nucE0_errm
      isgmr['G'] = nucG; isgmr['G_errp'] = nucG_errp; isgmr['G_errm'] = nucG_errm
      isgmr['EWSR'] = nucEWSR; isgmr['EWSR_errp'] = nucEWSR_errp; isgmr['EWSR_errm'] = nucEWSR_errm
      isgmr['M12M0'] = nucM12M0; isgmr['M12M0_errp'] = nucM12M0_errp; isgmr['M12M0_errm'] = nucM12M0_errm
      isgmr['M12Mm1'] = nucM12Mm1; isgmr['M12Mm1_errp'] = nucM12Mm1_errp; isgmr['M12Mm1_errm'] = nucM12Mm1_errm
      isgmr['M32M1'] = nucM32M1; isgmr['M32M1_errp'] = nucM32M1_errp; isgmr['M32M1_errm'] = nucM32M1_errm
      isgmr['ref'] = nucRef
      self.isgmr = isgmr
      #
      #: Attribute energy unit.
      self.E_unit = 'MeV'
      #
      if nuda.env.verb: print("Exit setupISGMRExp()")
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
      for ind,Z in enumerate( self.isgmr['Z'] ):
         print('For Z:',Z,' A:',self.isgmr['A'][ind])
         for A in self.isgmr['A'][ind]:
            print('Centroid energy:',self.isgmr['M12Mm1'][ind])
            print('   with errp:',self.isgmr['M12Mm1_errp'][ind])
            print('   with errm:',self.isgmr['M12Mm1_errm'][ind])
      #
      if nuda.env.verb: print("Exit print_outputs()")
      #
   #
   def average( self ):
      """
      Method to average the data when same target is given.

      **Attributes:**
      """
      print("")
      #
      if nuda.env.verb: print("Enter average()")
      #
      k = 0
      AAm1 = 0
      ZZm1 = 0
      #
      nA=[]; nZ=[]; nN=[]; nSymbol=[];  
      nE0=[]; nE0_errp=[]; nE0_errm=[];
      nG=[]; nG_errp=[]; nG_errm=[]; 
      nEWSR=[]; nEWSR_errp=[]; nEWSR_errm=[]; 
      nM12M0=[]; nM12M0_errp=[]; nM12M0_errm=[]; 
      nM12Mm1=[]; nM12Mm1_errp=[]; nM12Mm1_errm=[]; 
      nM32M1=[]; nM32M1_errp=[]; nM32M1_errm=[];
      #
      while k < nbk:
         AA   = nucA[k]
         ZZ   = nucZ[k]
         if k>0: 
            AAm1 = nucA[k-1]
            ZZm1 = nucZ[k-1]
         if k < nbk-1:
            AAp1 = nucA[k+1]
            ZZp1 = nucZ[k+1]
         else:
            AAp1 = 0
            ZZp1 = 0
         #
         if AA != AAm1 or ZZ != ZZm1:
            #
            # Initialisation
            #
            nbE0 = 0
            if nucE0[k] is not None:
               nbE0 += 1
               E0m = float(nucE0[k])
               E0m_errp = float(nucE0_errp[k])**2
               E0m_errm = float(nucE0_errm[k])**2
            nbG = 0
            if nucG[k] is not None:
               nbG += 1
               Gm = float(nucG[k])
               Gm_errp = float(nucG_errp[k])**2
               Gm_errm = float(nucG_errm[k])**2
            nbEWSR = 0
            if nucEWSR[k] is not None:
               nbEWSR += 1
               EWSRm = float(nucEWSR[k])
               EWSRm_errp = float(nucEWSR_errp[k])**2
               EWSRm_errm = float(nucEWSR_errm[k])**2
            nbM12M0 = 0
            if nucM12M0[k] is not None:
               nbM12M0 += 1
               M12M0m = float(nucM12M0[k])
               M12M0m_errp = float(nucM12M0_errp[k])**2
               M12M0m_errm = float(nucM12M0_errm[k])**2
            nbM12Mm1 = 0
            if nucM12Mm1[k] is not None:
               nbM12Mm1 += 1
               M12Mm1m = float(nucM12Mm1[k])
               M12Mm1m_errp = float(nucM12Mm1_errp[k])**2
               M12Mm1m_errm = float(nucM12Mm1_errm[k])**2
            nbM32M1 = 0
            if nucM32M1[k] is not None:
               nbM32M1 += 1
               M32M1m = float(nucM32M1[k])
               M32M1m_errp = float(nucM32M1_errp[k])**2
               M32M1m_errm = float(nucM32M1_errm[k])**2
            #
         if AA == AAp1 and ZZ == ZZp1:
            #
            if nucE0[k+1] is not None:
               nbE0 += 1
               E0m += float(nucE0[k+1])
               E0m_errp += float(nucE0_errp[k+1])**2
               E0m_errm += float(nucE0_errm[k+1])**2
            if nucG[k+1] is not None:
               nbG += 1
               Gm += float(nucG[k+1])
               Gm_errp += float(nucG_errp[k+1])**2
               Gm_errm += float(nucG_errm[k+1])**2
            if nucEWSR[k+1] is not None:
               nbEWSR += 1
               EWSRm += float(nucEWSR[k+1])
               EWSRm_errp += float(nucEWSR_errp[k+1])**2
               EWSRm_errm += float(nucEWSR_errm[k+1])**2
            if nucM12M0[k+1] is not None:
               nbM12M0 += 1
               M12M0m += float(nucM12M0[k+1])
               M12M0m_errp += float(nucM12M0_errp[k+1])**2
               M12M0m_errm += float(nucM12M0_errm[k+1])**2
            if nucM12Mm1[k+1] is not None:
               nbM12Mm1 += 1
               M12Mm1m += float(nucM12Mm1[k+1])
               M12Mm1m_errp += float(nucM12Mm1_errp[k+1])**2
               M12Mm1m_errm += float(nucM12Mm1_errm[k+1])**2
            if nucM32M1[k+1] is not None:
               nbM32M1 += 1
               M32M1m += float(nucM32M1[k+1])
               M32M1m_errp += float(nucM32M1_errp[k+1])**2
               M32M1m_errm += float(nucM32M1_errm[k+1])**2
            #
         else:
            #
            nA.append( nucA[k] )
            nZ.append( nucZ[k] )
            nN.append( nucN[k] )
            nSymbol.append( nucSymbol[k] )
            if nbE0 == 0:
               nE0.append( None )
               nE0_errp.append( None )
               nE0_errm.append( None )
            else:
               nE0.append( E0m / nbE0 )
               nE0_errp.append( math.sqrt( E0m_errp / nbE0 ) )
               nE0_errm.append( math.sqrt( E0m_errm / nbE0 ) )
            if nbG == 0:
               nG.append( None )
               nG_errp.append( None )
               nG_errm.append( None )
            else:
               nG.append( Gm / nbG )
               nG_errp.append( math.sqrt( Gm_errp / nbG ) )
               nG_errm.append( math.sqrt( Gm_errm / nbG ) )
            if nbEWSR == 0:
               nEWSR.append( None )
               nEWSR_errp.append( None )
               nEWSR_errm.append( None )
            else:
               nEWSR.append( EWSRm / nbEWSR )
               nEWSR_errp.append( math.sqrt( EWSRm_errp / nbEWSR ) )
               nEWSR_errm.append( math.sqrt( EWSRm_errm / nbEWSR ) )
            if nbM12M0 == 0:
               nM12M0.append( None )
               nM12M0_errp.append( None )
               nM12M0_errm.append( None )
            else:
               nM12M0.append( M12M0m / nbM12M0 )
               nM12M0_errp.append( math.sqrt( M12M0m_errp / nbM12M0 ) )
               nM12M0_errm.append( math.sqrt( M12M0m_errm / nbM12M0 ) )
            if nbM12Mm1 == 0:
               nM12Mm1.append( None )
               nM12Mm1_errp.append( None )
               nM12Mm1_errm.append( None )
            else:
               nM12Mm1.append( M12Mm1m / nbM12Mm1 )
               nM12Mm1_errp.append( math.sqrt( M12Mm1m_errp / nbM12Mm1 ) )
               nM12Mm1_errm.append( math.sqrt( M12Mm1m_errm / nbM12Mm1 ) )
            if nbM32M1 == 0:
               nM32M1.append( None )
               nM32M1_errp.append( None )
               nM32M1_errm.append( None )
            else:
               nM32M1.append( M32M1m / nbM32M1 )
               nM32M1_errp.append( math.sqrt( M32M1m_errp / nbM32M1 ) )
               nM32M1_errm.append( math.sqrt( M32M1m_errm / nbM32M1 ) )
         k += 1
      print('End k:',k)
      isgmrm = {}
      isgmrm['A'] = nA; isgmrm['Z'] = nZ; isgmrm['N'] = nN; isgmrm['symbol'] = nSymbol
      isgmrm['E0'] = nE0; isgmrm['E0_errp'] = nE0_errp; isgmrm['E0_errm'] = nE0_errm
      isgmrm['G'] = nG; isgmrm['G_errp'] = nG_errp; isgmrm['G_errm'] = nG_errm
      isgmrm['EWSR'] = nEWSR; isgmrm['EWSR_errp'] = nEWSR_errp; isgmrm['EWSR_errm'] = nEWSR_errm
      isgmrm['M12M0'] = nM12M0; isgmrm['M12M0_errp'] = nM12M0_errp; isgmrm['M12M0_errm'] = nM12M0_errm
      isgmrm['M12Mm1'] = nM12Mm1; isgmrm['M12Mm1_errp'] = nM12Mm1_errp; isgmrm['M12Mm1_errm'] = nM12Mm1_errm
      isgmrm['M32M1'] = nM32M1; isgmrm['M32M1_errp'] = nM32M1_errp; isgmrm['M32M1_errm'] = nM32M1_errm
      self.isgmrm = isgmrm
      #
      for k in range(len(isgmrm['A'])):
         print('Z=',isgmrm['Z'][k],' symbol:',isgmrm['symbol'][k],' A=',isgmrm['A'][k],' N=',isgmrm['N'][k],' E0:',isgmrm['E0'][k],isgmrm['E0_errp'][k],isgmrm['E0_errm'][k])
      #
      return self
      #
      if nuda.env.verb: print("Exit average()")
      #
   #
   def select( self, Zref=50, obs = 'M12Mm1' ):
      """
      Method to select a subset of data.

      :param Zref: Fix the reference charge for the search of isotopes.
      :type Zref: int, optional. Default: 1.
      :param obs: kind of observable to extract: 'M12M0', 'M12Mm1', 'M32M1'.
      :type obs: str
      **Attributes:**
      """
      print("")
      #
      if nuda.env.verb: print("Enter select()")
      #
      nucA = []; cent = []; errp = []; errm = [];
      for ind,A in enumerate(self.isgmr['A']):
         if obs == 'M12M0' and int( self.isgmr['Z'][ind] ) == Zref and self.isgmr['M12M0'][ind] is not None:
            nucA.append( int(A) )
            cent.append( float( self.isgmr['M12M0'][ind] ) )
            errp.append( float( self.isgmr['M12M0_errp'][ind] ) )
            errm.append( float( self.isgmr['M12M0_errm'][ind] ) )
         if obs == 'M12Mm1' and int( self.isgmr['Z'][ind] ) == Zref and self.isgmr['M12Mm1'][ind] is not None:
            nucA.append( int(A) )
            cent.append( float( self.isgmr['M12Mm1'][ind] ) )
            errp.append( float( self.isgmr['M12Mm1_errp'][ind] ) )
            errm.append( float( self.isgmr['M12Mm1_errm'][ind] ) )
         if obs == 'M32M1' and int( self.isgmr['Z'][ind] ) == Zref and self.isgmr['M32M1'][ind] is not None:
            nucA.append( int(A) )
            cent.append( float( self.isgmr['M32M1'][ind] ) )
            errp.append( float( self.isgmr['M32M1_errp'][ind] ) )
            errm.append( float( self.isgmr['M32M1_errm'][ind] ) )
      erra = 0.5 * np.add( errp, errm )
      self.nucA = nucA
      self.cent = cent
      self.errp = errp
      self.errm = errm
      self.erra = erra
      #
      return self
      #
      if nuda.env.verb: print("Exit select()")
      #
