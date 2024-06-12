import os
import sys
import numpy as np  # 1.15.0

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nudy

class SetupAME():
    """
    Instantiate the experimental nuclear masses from AMDC

    :param A: (optional) if given returns only the binding energy for nuclei with mass 'A', otherwise returns the entier mass table (default: 0, 208 for instance).
    :type  A: int.
    :param Z: (optional) if given returns only the binding energy for nuclei with charge 'Z', otherwise returns the entier mass table (default: 0, 82 for instance).
    :type  Z: int.
    :param Amin: (optional) if given sets the lower bound in A of the mass table, otherwise returns the entier mass table ( default: 0, 12 for instance).
    :type  Amin: int.
    :param Zmin: (optional) if given sets the lower bound in Z of the mass table, otherwise returns the entier mass table ( default: 0, 6 for instance).
    :type  Zmin: int.
    :param version: (optional) version release of the AMDC data table (default: '2016', '2012', '2003', '1995', '1993', '1983').
    :type  version: str.
    :param interp: (optional) include interpolated data (default: 'n', 'y').
    :type  interp: str.
    :param every: (optional) select one nucleus every N. if N=1 no selection (by default).
    :type  every: integer. 
    """
    def __init__(self, A = 0, Z = 0, Amin = 0, Zmin = 0, version = '2020', interp = 'n', every = 1):
        #
        if nudy.env.verb: print("Enter SetupAME()")
        #
        self.version = version
        self.interp = interp
        #
        if nudy.env.verb: print("version:",version)
        if nudy.env.verb: print("interp:",interp)
        #
        # check the consistency of the input variables
        #
        if int(A) != 0 and int(A) < int(Amin):
            print("readADMC.py: the requested value for A is in conflict with the value for Amin")
            print("A:",A)
            print("Amin:",Amin)
            print("stop code")
            exit()
        if int(Z) != 0 and int(Z) < int(Zmin):
            print("readADMC.py: the requested value for Z is in conflict with the value for Zmin")
            print("Z:",Z)
            print("Zmin:",Zmin)
            print("stop code")
            exit()
        #
        if version=='2012':
            file_ame = nudy.param.path_data+'AME/2012/nubase.mas12.txt'
            nbLine_skip = 3
            cbe = 18
            cdbe = 29
            cdbee = 38
            cyear=105 # column for the discovery year
        elif version=='2016':
            file_ame = nudy.param.path_data+'AME/2016/nubase2016.txt'
            nbLine_skip = 0
            cbe = 18
            cdbe = 29
            cdbee = 38
            cyear=105 # column for the discovery year
        elif version=='2020':
            file_ame = nudy.param.path_data+'AME/2020/nubase_3.mas20.txt'
            nbLine_skip = 26
            cbe = 18
            cdbe = 31
            cdbee = 42
            cyear=114 # column for the discovery year
            #
            # read the AMDC table
            #
        nbLine = 0
        iNuc = 0
        nbNuc = 0
        nucAmax = 0
        nucZmax = 0
        yearMin = 1890
        yearFull = []
        # Initialize nucBENZ and nucdBENZ
        nucAZN = np.zeros( (4,10000), dtype=int)
        nucBE  = np.zeros( (2,10000), dtype=float)
        nucTot = np.zeros( (4,10000), dtype=float)
        #
        with open(file_amdc,'r') as file:
            for line in file:
                nbLine = nbLine + 1
                # skip the header of the file
                if nbLine < nbLine_skip: continue
                # limit to the first 50 lines
                #if env.verb and nbLine > 50: continue
                if (env.verb): print('line:'+str(nbLine)+':'+line[0:-2])
                # if '#' in line[14:40]: continue
                # Read input file:
                nucA=int(line[0:3])
                if nucA < int(Amin): continue
                if int(A) != 0 and nucA != int(A): continue
                nucZ=int(line[4:7])
                if nucZ < int(Zmin): continue
                if int(Z) != 0 and nucZ != int(Z): continue
                nucN=nucA-nucZ
                nuci=int(line[7:8])
                if (env.verb): print('   nucleus:',nucA,nucZ,nucN)
                if (env.verb): print('   nuci:'+str(nuci))
                # select only GS by skiping all contributions from other states (nuci != 0)
                if nuci != 0: continue
                #
                nucName=line[11:16]
                nucEx=line[16:17]
                yearStr=line[cyear:cyear+4]
                # check if there is '#' in the string or if the value is absent:
                #if ' '*11 in line[18:31]: continue
                #print("   test:",line[cbe:cdbe],".",(cdbe-cbe))
                #if '#' in line[cbe:cdbe]:
                # check that there is a data for the measured mass:
                if line[cbe:cdbe] == ' '*(cdbe-cbe): continue
                if '#' in line[cbe:cdbe]:
                    nucME=float(line[cbe:cdbe].replace('#',''))
                    nucdME=float(line[cdbe:cdbee].replace('#',''))
                    nucInterp='y'
                    yearInt=int(version)+1
                else:
                    nucME=float(line[cbe:cdbe])
                    nucdME=float(line[cdbe:cdbee])
                    nucInterp='n'
                    if yearStr != ' '*4: yearInt=int(yearStr)
                # date could be missing even if the mass measurement exists
                if ( len(yearStr) == 4 and yearStr == ' '*4 and nucInterp == 'n' ): continue
                #
                # Additional options: analyze the year of discovery
                #
                #print(nucA,nucZ,nucName)
                #if ( len(yearStr) == 4 and yearStr == ' '*4 and nucInterp == 'n' ):
                #    print('issue with:',nucA,nucZ,nucName)
                #yearInt = 0
                #yearInt=int(yearStr)
                #
                # All tests passed sucessfully.
                #
                iNuc = iNuc + 1
                # skip nuclei depending on every:
                if iNuc % every != 0 :
                    continue
                yearFull.append(yearInt)
                yearInd=int((yearInt-yearMin)/10)
                if (env.verb): print('   year:'+str(yearInt)+',index:'+str(yearInd))
                #
                if ( nucName[0:3].isdigit() ):
                    nucEl=nucName[3:5]
                elif ( nucName[0:2].isdigit() ):
                    nucEl=nucName[2:4]
                else:
                    nucEl=nucName[1:3]
                if env.verb: print('   El,Ex:',nucEl,nucEx)
                #nucGS=False
                #if ( nucEx.strip() == '' ): nucGS=True
                #if env.verb: print("   GS:",nucGS)
                if (env.verb): print("   ME:",nucME,nucdME)
                nucMass = nucA * CST_AtmMass + nucME / 1000.0
                nucdMass = nucdME / 1000.0 
                # nucBE = ( nucMass - nucZ * ( CST_mpc2 + CST_mec2 ) - nucN * CST_mnc2 )
                nucBDE = nucME / 1000.0 - nucZ * CST_mHc2 - nucN * CST_mnc2
                nucdBDE = math.sqrt( nucdMass**2 + nucZ * CST_dmHc2**2 + nucN * CST_dmnc2**2 )
                if (env.verb): print("   BDE:",nucBDE,nucdBDE)
                # fill nucAZN
                nucAZN[0][nbNuc]=nucA
                nucAZN[1][nbNuc]=nucZ
                nucAZN[2][nbNuc]=nucN
                nucAZN[3][nbNuc]=yearInt
                # fill nucBE
                nucBE[0][nbNuc]=nucBDE
                nucBE[1][nbNuc]=nucdBDE
                nucTot[0][nbNuc]=nucA
                nucTot[1][nbNuc]=nucZ
                nucTot[2][nbNuc]=nucBDE
                nucTot[3][nbNuc]=nucdBDE
                if interp == 'n' and interp==nucInterp:
                    nbNuc = nbNuc + 1
                    nucAmax = nucA
                    nucZmax = nucZ
                if interp == 'y':
                    nbNuc = nbNuc + 1
                    nucAmax = nucA
                    nucZmax = nucZ
                #if env.verb: print('BE of all:',nucN,nucZ,nucBENZ[nucN][nucZ])

#return nbLine, iNuc, nbNuc, nucAZN[:][0:nbNuc], nucBE[:][0:nbNuc], nucTot[:][0:nbNuc], nucAmax, nucZmax

        self.nbLine = nbLine
        self.nbNuc_all = iNuc
        self.nbNuc = nbNuc
        self.nucAmax = nucAmax
        self.nucZmax = nucZmax
        self.nucAZN = nucAZN
        self.nucBE = nucBE
        self.nucTot = nucTot        
        #
        if nudy.env.verb: print("Exit SetupAME()")

