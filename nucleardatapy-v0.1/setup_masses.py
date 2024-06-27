import os
import sys
import math
import numpy as np  # 1.15.0

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nudy

CST_AtmMass = 931.494028
#CST_mpc2 = 938.272081
#CST_mnc2 = 939.565413
#CST_mec2 = 0.5109989461
CST_mnc2 = 8.0713171
CST_dmnc2= 0.0000005
CST_mHc2 = 7.2889706
CST_dmHc2= 0.0000001
yearMin=1890

# time conversion:
ns = 1.e-9
ms = 1.e-3
h = 60*60 # number of seconds per hour
d = h*24 # number of seconds per day
m = 30*d # number of second per month (30 days)
y = d*365.25 #number of seconds per year
ky = y*1.e3 # mille years
my = y*1.e6 # million of years
Gy = y*1.e9 # giga years
ILt = 100*Gy # infinite Large time
ISt = 1.e-30 # infinite Short time

def stable_fit():
    Z = np.arange(110)
    N = Z + 6.e-3*Z*Z
    return N, Z

def tables_masses():
    """
    Return a list of the tables available in this toolkit and
    print them all on the prompt.

    :return: The list of tables.
    :rtype: list[str].
    """
    #
    if nudy.env.verb: print("\nEnter tables_masses()")
    #
    tables = [ 'AME' ]
    #
    print('tables available in the toolkit:',tables)
    tables_lower = [ item.lower() for item in tables ]
    print('tables available in the toolkit:',tables_lower)
    #
    if nudy.env.verb: print("Exit tables_masses()")
    #
    return tables, tables_lower

def versions_masses( table ):
    """
    Return a list with the versions of the table available in 
    this toolkit for a given model and print them all on the prompt.

    :param table: The table for which there are different versions.
    :type table: str.
    :return: The list of versions.
    :rtype: list[str].
    """
    #
    if nudy.env.verb: print("\nEnter versions_masses()")
    #
    if table.lower()=='ame':
        versions= [ '2020', '2016', '2012' ]
    #
    print('Versions available in the toolkit:',versions)
    versions_lower = [ item.lower() for item in versions ]
    #
    if nudy.env.verb: print("Exit versions_masses()")
    #
    return versions, versions_lower


class SetupMasses():
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
    def __init__(self, table = 'AME', version = '2020'):
        #
        if nudy.env.verb: print("Enter SetupMasses()")
        #
        tables, tables_lower = tables_masses()
        if table.lower() not in tables_lower:
            print('Table ',table,' is not in the list of tables.')
            print('list of tables:',tables)
            print('-- Exit the code --')
            exit()
        self.table = table
        if nudy.env.verb: print("table:",table)
        #
        versions, versions_lower = versions_masses( table = table )
        if version.lower() not in versions_lower:
            print('Version ',version,' is not in the list of versions.')
            print('list of versions:',versions)
            print('-- Exit the code --')
            exit()
        self.version = version
        if nudy.env.verb: print("version:",version)
        #
        self.A = []
        self.Z = []
        self.symb = []
        self.N = []
        self.I = []
        self.Interp = []
        self.stbl = [] # ='y' if stable nucleus
        self.HT = [] # half-time in s
        self.year = []
        self.BE = []
        self.BE_err = []
        #
        self.Zmax=0
        #
        if table.lower()=='ame':
            if version=='2012':
                file_in = nudy.param.path_data+'nuclei/masses/AME/2012/nubase.mas12.txt'
                nbLine_skip = 3 # lines in the header to skip
                cbe = 18 # column giving the binding energy
                cdbe = 29 # column giving the uncertainty in the binding energy
                cdbee = 38 # column ??
                cyear=105 # column for the discovery year
            elif version=='2016':
                file_in = nudy.param.path_data+'nuclei/masses/AME/2016/nubase2016.txt'
                nbLine_skip = 0
                cbe = 18
                cdbe = 29
                cdbee = 38
                cyear=105 # column for the discovery year
            elif version=='2020':
                file_in = nudy.param.path_data+'nuclei/masses/AME/2020/nubase_3.mas20.txt'
                nbLine_skip = 26
                cbe = 18
                cdbe = 31
                cdbee = 42
                cyear=114 # column for the discovery year
                self.ref='F.G. Kondev, M. Wang, W.J. Huang, S. Naimi, and G. Audi, Chin. Phys. C45, 030001 (2021)'
                self.label = 'AME-2020'
                self.note = "write here notes about this table."
            #
            # read the AME table
            #
            nbLine = 0
            nbNuc = 0
            #
            with open(file_in,'r') as file:
                for line in file:
                    nbLine = nbLine + 1
                    # skip the header of the file
                    if nbLine < nbLine_skip: continue
                    if (nudy.env.verb): print('line:'+str(nbLine)+':'+line[0:-2])
                    # if '#' in line[14:40]: continue
                    # Read input file:
                    nucA=int(line[0:3])
                    #if nucA < int(Amin): continue
                    #if int(A) != 0 and nucA != int(A): continue
                    nucZ=int(line[4:7])
                    #if nucZ < int(Zmin): continue
                    #if int(Z) != 0 and nucZ != int(Z): continue
                    nucN=nucA-nucZ
                    if (nudy.env.verb): print('   nucleus:',nucA,nucZ,nucN)
                    nucI=int(line[7:8]) # if nuci==0: ground-state (GS)
                    if (nudy.env.verb): print('   nucI:'+str(nucI))
                    # select only GS by skiping all contributions from other states (nuci != 0)
                    #if nucI != 0: continue
                    #
                    nucName=line[11:16]
                    if ( nucName[0:3].isdigit() ):
                        nucSymb=nucName[3:5]
                    elif ( nucName[0:2].isdigit() ):
                        nucSymb=nucName[2:4]
                    else:
                        nucSymb=nucName[1:3]
                    if nudy.env.verb: print('   Symbol:',nucSymb)
                    nucIsomer=line[16:17]
                    if nudy.env.verb: print('   Isomer:',nucIsomer)
                    nucStbl = 'n'
                    ht=line[69:78]
                    htu=line[78:80]
                    print('ht:',ht,' unit:',htu)
                    fac = 1.0
                    if 'stbl' in ht:
                        nucStbl = 'y'
                        ht = ILt
                    elif 'p-unst' in ht:
                        nucStbl = 'n'
                        ht = ISt
                    elif ht==' '*9: # be carefull: there is no time associated, so it gives a short time by default
                        nucStbl = 'n'
                        ht = ISt
                    elif '\n' in ht: # be carefull: there is no data given here, so it gives short time by default
                        nucStbl = 'n'
                        ht = ISt
                    elif '>' in ht and '#' in ht: # be carefull: there is only upper limit for the half-time, so it gives it by default
                        nucStbl = 'n'
                        ht = float( ht.replace('#','').replace('>','') )
                    elif '<' in ht and '#' in ht: # be carefull: there is only upper limit for the half-time, so it gives it by default
                        nucStbl = 'n'
                        ht = float( ht.replace('#','').replace('<','') )
                    elif '>' in ht: # be carefull: there is only lower limit for the half-time, so it gives it by default
                        nucStbl = 'n'
                        ht = float( ht.replace('>','') )
                    elif '<' in ht: # be carefull: there is only upper limit for the half-time, so it gives it by default
                        nucStbl = 'n'
                        ht = float( ht.replace('<','') )
                    elif '#' in ht: # be carefull: there is only upper limit for the half-time, so it gives it by default
                        nucStbl = 'n'
                        ht = float( ht.replace('#','') )
                    elif '~' in ht: # be carefull: there is only upper limit for the half-time, so it gives it by default
                        nucStbl = 'n'
                        ht = float( ht.replace('~','') )
                    else:
                        nucStbl = 'n'
                        ht = float( ht )
                        if htu==' s':
                            print('second')
                            fac = 1.0
                        elif htu=='ms':
                            print('milli-second')
                            fac = ms
                        elif htu==' y':
                            print('year')
                            fac = y
                        elif htu=='ys':
                            print('years')
                            fac = y
                        elif htu==' d':
                            print('day')
                            fac = d
                        elif htu=='ns':
                            print('nano-second')
                            fac = ns
                        elif htu=='as':
                            print('as')
                            fac = d
                        elif htu=='ps':
                            print('ps')
                            fac = d
                        elif htu=='fs':
                            print('fs')
                            fac = d
                        elif htu=='zs':
                            print('zs')
                            fac = d
                        elif htu=='us':
                            print('us')
                            fac = d
                        elif htu=='ky':
                            print('mille years')
                            fac = ky
                        elif htu=='My':
                            print('Million of years')
                            fac = my
                        elif htu=='Gy':
                            print('Giga years')
                            fac = Gy
                    nucHT = ht * fac
                    year=line[cyear:cyear+4]
                    if nudy.env.verb: print('   year:',year)
                    # check if there is '#' in the string or if the value is absent:
                    #if ' '*11 in line[18:31]: continue
                    #print("   test:",line[cbe:cdbe],".",(cdbe-cbe))
                    #if '#' in line[cbe:cdbe]:
                    # check that there is a data for the measured mass:
                    if line[cbe:cdbe] == ' '*(cdbe-cbe): continue
                    if '#' in line[cbe:cdbe]:
                        nucME=float(line[cbe:cdbe].replace('#',''))
                        nucdME=float(line[cdbe:cdbee].replace('#',''))
                        nucInterp = 'y'
                        nucYear=int(version)+1 # define a fake year which is after the table release
                    else:
                        nucME=float(line[cbe:cdbe])
                        nucdME=float(line[cdbe:cdbee])
                        nucInterp = 'n'
                        print('type(year):',type(year))
                        print('len(year):',len(year))
                        #nucYear=int(year)
                        if len(year) == 4 and year != ' '*4: 
                            nucYear=int(year)
                        else:
                            nucYear=int(version)+1
                        #if year != ' '*4: nucYear=int(year)
                    if (nudy.env.verb): print("   ME:",nucME,' +- ',nucdME,' keV')
                    # date could be missing even if the mass measurement exists
                    #if ( len(year) == 4 and year == ' '*4 and nucInterp == 'n' ): continue # to be checked
                    #
                    # Additional options: analyze the year of discovery
                    #
                    #print(nucA,nucZ,nucName)
                    #if ( len(yearStr) == 4 and yearStr == ' '*4 and nucInterp == 'n' ):
                    #    print('issue with:',nucA,nucZ,nucName)
                    #yearInt = 0
                    #yearInt=int(yearStr)
                    #
                    # When all tests passed sucessfully: the new line can be stored
                    #
                    #yearFull.append(yearInt)
                    #yearInd=int((yearInt-yearMin)/10)
                    #if (env.verb): print('   year:'+str(yearInt)+',index:'+str(yearInd))
                    #
                    nucMass = nucA * CST_AtmMass + nucME / 1000.0 # conversion to MeV
                    nucdMass = nucdME / 1000.0 
                    # nucBE = ( nucMass - nucZ * ( CST_mpc2 + CST_mec2 ) - nucN * CST_mnc2 )
                    nucBE = nucME / 1000.0 - nucZ * CST_mHc2 - nucN * CST_mnc2
                    nucdBE = math.sqrt( nucdMass**2 + nucZ * CST_dmHc2**2 + nucN * CST_dmnc2**2 )
                    if (nudy.env.verb): print("   BE:",nucBE,nucdBE)
                    # add nucleus to the table
                    self.A.append( nucA )
                    self.Z.append( nucZ )
                    if nucZ > self.Zmax: self.Zmax = nucZ
                    self.N.append( nucN )
                    self.symb.append( nucSymb )
                    self.I.append( nucI )
                    self.Interp.append( nucInterp )
                    self.stbl.append( nucStbl )
                    self.HT.append( nucHT )
                    self.year.append( nucYear )
                    self.BE.append( nucBE )
                    self.BE_err.append( nucdBE )
                    nbNuc = nbNuc + 1
            self.nbLine = nbLine
            self.nbNuc = nbNuc
        #
        if nudy.env.verb: print("Exit SetupMasses()")
        #
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
       print("   table:  ",self.table)
       print("   version:",self.version)
       print("   ref:    ",self.ref)
       print("   label:  ",self.label)
       print("   note:   ",self.note)
       if any(self.Z): print(f"   Z: {self.Z}")
       if any(self.A): print(f"   A: {self.A}")
       #
       if nudy.env.verb: print("Exit print_outputs()")
       #
    def select(self, Amin = 0, Zmin = 0, interp = 'n', state= 'gs', nucleus = 'unstable', every = 1):
        #
        if nudy.env.verb: print("Enter select()")
        #
        if interp.lower() not in [ 'y', 'n' ]:
            print('Interp ',interp,' is not "y" or "n".')
            print('-- Exit the code --')
            exit()
        self.interp = interp
        if nudy.env.verb: print("interp:",interp)
        #
        if state.lower() not in [ 'gs' ]:
            print('State ',state,' is not "gs".')
            print('-- Exit the code --')
            exit()
        self.state = state
        if nudy.env.verb: print("state:",state)
        #
        if nucleus.lower() not in [ 'stable', 'unstable' ]:
            print('Nucleus ',nucleus,' is not "stable" or "unstable".')
            print('-- Exit the code --')
            exit()
        self.nucleus = nucleus
        if nudy.env.verb: print("nucleus:",nucleus)
        #
        nbNucTot = 0
        nbNucSta = 0
        nbNucSel = 0
        #
        self.sel_A = []
        self.sel_Z = []
        self.sel_symb = []
        self.sel_N = []
        self.sel_I = []
        self.sel_Interp = []
        self.sel_HT = [] # half-time in s
        self.sel_year = []
        self.sel_BE = []
        self.sel_BE_err = []
        #
        self.sel_Zmax = 0
        #
        #for nucA,ind in enumerate(self.A):
        for ind in range(self.nbNuc):
            #
            nucA = self.A[ind]
            nucZ = self.Z[ind]
            nucN = self.N[ind]
            nucI = self.I[ind]
            nucSymb = self.symb[ind]
            nucInterp = self.Interp[ind]
            nucStbl = self.stbl[ind]
            nucHT = self.HT[ind]
            nucYear = self.year[ind]
            nucBE = self.BE[ind]
            nucdBE = self.BE_err[ind]
            #print('select:',ind,nucA,nucZ,nucN,nucSymb)
            # skip nuclei below Amin and Zmin:
            if nucA < Amin or nucZ < Zmin:
                continue
            if nucStbl == 'n' and nucleus.lower() == 'stable':
                continue
            if nucStbl == 'y' and nucleus.lower() == 'unstable':
                continue
            nbNucTot = nbNucTot + 1
            # skip nucleus if interpolated data
            if nucInterp == 'y':
                continue
            # skip nuclei not in GS
            if state == 'gs' and nucI != 0:
                continue
            nbNucSta = nbNucSta + 1
            # skip nuclei depending on every:
            if nbNucSta % every != 0 :
                continue
            nbNucSel = nbNucSel + 1
            self.sel_A.append( nucA )
            self.sel_Z.append( nucZ )
            if nucZ > self.sel_Zmax: self.sel_Zmax = nucZ
            self.sel_N.append( nucN )
            self.sel_symb.append( nucSymb )
            self.sel_I.append( nucI )
            self.sel_Interp.append( nucInterp )
            self.sel_HT.append( nucHT )
            self.sel_year.append( nucYear )
            self.sel_BE.append( nucBE )
            self.sel_BE_err.append( nucdBE )
        self.sel_nbNucTot = nbNucTot
        self.sel_nbNucSta = nbNucSta
        self.sel_nbNucSel = nbNucSel
        print('number of nuclei(Tot):',self.sel_nbNucTot)
        print('number of nuclei(Sta):',self.sel_nbNucSta)
        print('number of nuclei(Sel):',self.sel_nbNucSel)
        #
        if nudy.env.verb: print("Exit select()")
        #
        return self
        #
    def drip(self, Zmax = 95 ):
        #
        if nudy.env.verb: print("Enter drip()")
        #
        Nstable, Zstable = stable_fit()
        #
        self.drip_Z = []
        self.drip_Nmin = []
        self.drip_Nmax = []
        #
        for Z,ind in enumerate(Zstable):
            #
            if Z >= Zmax :
                break
            #
            Nmin = Nstable[ind]
            Nmax = Nstable[ind]
            #
            #print('sel_Z:',self.sel_Z)
            #exit()
            for ind2 in range(self.sel_nbNucSel):
                #if self.sel_Z[ind] == Z:
                #    print('sel_Z:',self.sel_Z)
                #    exit()
                #print('ind:',ind,Z,self.sel_Zmax,self.sel_Z[ind2],Nmin,Nmax)
                #print('sel_N:',self.sel_N[ind2])
                if self.sel_Z[ind2] == Z and self.sel_N[ind2] < Nmin:
                    Nmin = self.sel_N[ind2]
                if self.sel_Z[ind2] == Z and self.sel_N[ind2] > Nmax:
                    Nmax = self.sel_N[ind2]
            self.drip_Z.append( Z )
            self.drip_Nmin.append( Nmin )
            self.drip_Nmax.append( Nmax )
        #print('drip: Z',self.drip_Z)
        #print('drip: Nmin:',self.drip_Nmin)
        #print('drip: Nmax:',self.drip_Nmax)
        #
        if nudy.env.verb: print("Exit drip()")
        #
        return self
        #
