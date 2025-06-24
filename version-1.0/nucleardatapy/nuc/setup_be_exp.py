import os
import sys
import math
import numpy as np  # 1.15.0

import nucleardatapy as nuda

CST_AtmMass = 931.494028
#CST_mpc2 = 938.272081
#CST_mnc2 = 939.565413
#CST_mec2 = 0.5109989461
CST_mnc2 = 8.0713171
CST_dmnc2= 0.0000005
CST_mHc2 = 7.2889706
CST_dmHc2= 0.0000001
yearMin=1890

# time conversion (using tropical year as in NUBASE2020):
ns = 1e-9
minute = 60 # in s
hour = 60 * minute # (hours) in s
day = 24 * hour # (day) in s # days = 86400 # in s
month = 30 * day # (month) (30 days) in s
year = 365.2422 * day # (year) in s
#print('years:',years)
#print('type(years):',type(years))
ILt = 1e30 * year # infinite Large time
ISt = 1.e-30 # infinite Short time
HTsl = day # half-time for short live nuclei
HTvsl = 1.0 # half-time for very short live nuclei
HThsl = 1.e-3 # half-time for hyper short live nuclei

def stable_fit_Z(Zmin = 1, Zmax = 120):
    Z = np.linspace(start=Zmin, stop=Zmax, num=1+Zmax-Zmin, dtype = int )
    N = np.array( Z + 6.e-3*Z*Z, dtype = int )
    return N, Z

def stable_fit_N(Nmin = 1, Nmax = 170):
    N = np.linspace(start=Nmin, stop=Nmax, num=1+Nmax-Nmin, dtype = int )
    Z = np.array( N - 3.8e-3*N*N + 9.e-6*N*N*N, dtype = int )
    return N, Z

def be_exp_tables():
    """
    Return a list of the tables available in this toolkit for the experimental masses and
    print them all on the prompt. These tables are the following
    ones: 'AME'.

    :return: The list of tables.
    :rtype: list[str].
    """
    #
    if nuda.env.verb: print("\nEnter be_exp_tables()")
    #
    tables = [ 'AME' ]
    #
    #print('tables available in the toolkit:',tables)
    tables_lower = [ item.lower() for item in tables ]
    #print('tables available in the toolkit:',tables_lower)
    #
    if nuda.env.verb: print("Exit be_exp_tables()")
    #
    return tables, tables_lower

def be_exp_versions( table ):
    """
    Return a list of versions of tables available in 
    this toolkit for a given model and print them all on the prompt.

    :param table: The table for which there are different versions.
    :type table: str.
    :return: The list of versions. \
    If table == 'AME': '2020', '2016', '2012'.
    :rtype: list[str].
    """
    #
    if nuda.env.verb: print("\nEnter be_exp_versions()")
    #
    if table.lower()=='ame':
        versions= [ '2020', '2016', '2012' ]
    #
    #print('Versions available in the toolkit:',versions)
    versions_lower = [ item.lower() for item in versions ]
    #
    if nuda.env.verb: print("Exit be_exp_tables_versions()")
    #
    return versions, versions_lower

def plot_shells(axs):
    #
    # plot shells for isotopes and isotones
    #
    axs.plot( [0,40], [7,7], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [0,40], [9,9], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [6,60], [19,19], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [6,60], [21,21], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [12,90], [27,27], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [12,90], [29,29], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [34,138], [49,49], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [34,138], [51,51], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [76,170], [81,81], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [76,170], [83,83], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [126,190], [127,127], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [126,190], [129,129], linestyle='dotted', linewidth=1, color='gray')
    #
    # plot shells for isotones
    #
    axs.plot( [7,7], [0,24], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [9,9], [0,24], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [19,19], [4,40], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [21,21], [4,40], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [27,27], [4,46], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [29,29], [4,46], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [49,49], [14,60], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [51,51], [14,60], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [81,81], [20,86], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [83,83], [20,86], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [127,127], [40,132], linestyle='dotted', linewidth=1, color='gray')
    axs.plot( [129,129], [40,132], linestyle='dotted', linewidth=1, color='gray')
    #
    return axs

class setupBEExp():
    """
    Instantiate the experimental nuclear masses from AME mass table.

    This choice is defined in the variables `table` and `version`.

    `table` can chosen among the following ones: 'AME'.

    `version` can be chosen among the following choices: '2020', '2016', '2012'.

    :param table: Fix the name of `table`. Default value: 'AME'.
    :type table: str, optional. 
    :param version: Fix the name of `version`. Default value: 2020'.
    :type version: str, optional. 

    **Attributes:**
    """
    def __init__(self, table = 'AME', version = '2020'):
        #
        if nuda.env.verb: print("Enter setupBEExp()")
        #
        tables, tables_lower = be_exp_tables()
        if table.lower() not in tables_lower:
            print('setup_be_exp.py: Table ',table,' is not in the list of tables.')
            print('setup_be_exp.py: list of tables:',tables)
            print('setup_be_exp.py: -- Exit the code --')
            exit()
        self.table = table
        if nuda.env.verb: print("table:",table)
        #
        versions, versions_lower = be_exp_versions( table = table )
        if version.lower() not in versions_lower:
            print('setup_be_exp.py: Version ',version,' is not in the list of versions.')
            print('setup_be_exp.py: list of versions:',versions)
            print('setup_be_exp.py: -- Exit the code --')
            exit()
        self.version = version
        if nuda.env.verb: print("version:",version)
        #
        #: Attribute A (mass of the nucleus).
        self.nucA = []
        #: Attribute Z (charge of the nucleus).
        self.nucZ = []
        #: Attribute symb (symbol) of the element, e.g., Fe.
        self.nucSymb = []
        #: Attribute N (number of neutrons of the nucleus).
        self.nucN = []
        #: Attribute I (isospin asymmetry):
        self.nucI = []
        #: Attribute I.
        self.flagI = []
        #: Attribute Interp (interpolation). Interp='y' is the nucleus\
        #: has not been measured but is in the table based on interpolation expressions.\
        #: otherwise Interp = 'n' for nuclei produced in laboratory and measured.
        self.flagInterp = []
        #: Attribute stbl. stbl='y' if the nucleus is stable (according to the table). Otherwise stbl = 'n'.
        self.nucStbl = [] # ='y' if stable nucleus
        #: Attribute HT (half-Time) of the nucleus.
        self.nucHT = [] # half-time in s
        #: Attribute year of the discovery of the nucleus.
        self.nucYear = []
        #: Attribute BE (Binding Energy) of the nucleus.
        self.nucBE = []
        #: Attribute uncertainty in the BE (Binding Energy) of the nucleus.
        self.nucBE_err = []
        #: Attribute Zmax: maximum charge of nuclei present in the table.
        self.Zmax=0
        #
        if table.lower()=='ame':
            if version=='2012':
                file_in = nuda.param.path_data+'nuclei/masses/AME/2012_nubase.mas12.txt'
                nbLine_skip = 3 # lines in the header to skip
                cbe = 18 # column giving the binding energy
                cdbe = 29 # column giving the uncertainty in the binding energy
                cdbee = 38 # column ??
                cyear=105 # column for the discovery year
            elif version=='2016':
                file_in = nuda.param.path_data+'nuclei/masses/AME/2016_nubase2016.txt'
                nbLine_skip = 0
                cbe = 18
                cdbe = 29
                cdbee = 38
                cyear=105 # column for the discovery year
            elif version=='2020':
                file_in = nuda.param.path_data+'nuclei/masses/AME/2020_nubase_4.mas20.txt'
                nbLine_skip = 26
                cbe = 18
                cdbe = 31
                cdbee = 42
                cyear=114 # column for the discovery year
                #: Attribute providing the full reference to the paper to be citted.
                self.ref='F.G. Kondev, M. Wang, W.J. Huang, S. Naimi, and G. Audi, Chin. Phys. C45, 030001 (2021)'
                #: Attribute providing the label the data is references for figures.
                self.label = 'AME-2020'
                #: Attribute providing additional notes about the data.
                self.note = "write here notes about this table."
            #
            # read the AME table
            #
            nbLine = 0
            nbNuc = 0
            #
            self.ind_min = 10000
            self.ind_max = 0
            self.year_min = 3000
            self.year_max = 1600
            #
            with open(file_in,'r') as file:
                for line in file:
                    nbLine = nbLine + 1
                    # skip the header of the file
                    if nbLine < nbLine_skip: continue
                    if (nuda.env.verb): print('line:'+str(nbLine)+':'+line[0:-2])
                    # if '#' in line[14:40]: continue
                    # Read input file:
                    AA=int(line[0:3])
                    #if nucA < int(Amin): continue
                    #if int(A) != 0 and nucA != int(A): continue
                    ZZ=int(line[4:7])
                    #if nucZ < int(Zmin): continue
                    #if int(Z) != 0 and nucZ != int(Z): continue
                    NN = AA - ZZ
                    II = ( NN - ZZ ) / AA
                    if (nuda.env.verb): print('   nucleus:',AA,ZZ,NN)
                    #if ZZ == 20: print('   nucleus:',AA,ZZ,NN)
                    flagI=int(line[7:8]) # if nuci==0: ground-state (GS)
                    if (nuda.env.verb): print('   flagI:'+str(flagI))
                    # select only GS by skiping all contributions from other states (flagI = 0)
                    #if flagI != 0: continue
                    #
                    name=line[11:16]
                    if ( name[0:3].isdigit() ):
                        symb=name[3:5]
                    elif ( name[0:2].isdigit() ):
                        symb=name[2:4]
                    else:
                        symb=name[1:3]
                    if nuda.env.verb: print('   Symbol:',symb)
                    isomer=line[16:17]
                    if nuda.env.verb: print('   Isomer:',isomer)
                    stbl = 'n'
                    ht=line[69:78]
                    htu=line[78:80]
                    #print('ht:',ht,' unit:',htu)
                    fac = 1.0
                    if 'stbl' in ht:
                        stbl = 'y'
                        ht = ILt
                    elif 'p-unst' in ht:
                        stbl = 'n'
                        ht = ISt
                    elif ht==' '*9: # be carefull: there is no time associated, so it gives a short time by default
                        stbl = 'n'
                        ht = ISt
                    elif '\n' in ht: # be carefull: there is no data given here, so it gives short time by default
                        stbl = 'n'
                        ht = ISt
                    elif '>' in ht and '#' in ht: # be carefull: there is only upper limit for the half-time, so it gives it by default
                        stbl = 'n'
                        ht = float( ht.replace('#','').replace('>','') )
                    elif '<' in ht and '#' in ht: # be carefull: there is only upper limit for the half-time, so it gives it by default
                        stbl = 'n'
                        ht = float( ht.replace('#','').replace('<','') )
                    elif '>' in ht: # be carefull: there is only lower limit for the half-time, so it gives it by default
                        stbl = 'n'
                        ht = float( ht.replace('>','') )
                    elif '<' in ht: # be carefull: there is only upper limit for the half-time, so it gives it by default
                        stbl = 'n'
                        ht = float( ht.replace('<','') )
                    elif '#' in ht: # be carefull: there is only upper limit for the half-time, so it gives it by default
                        stbl = 'n'
                        ht = float( ht.replace('#','') )
                    elif '~' in ht: # be carefull: there is only upper limit for the half-time, so it gives it by default
                        stbl = 'n'
                        ht = float( ht.replace('~','') )
                    else:
                        stbl = 'n'
                        ht = float( ht )
                        if htu=='ys': 
                            fac = 1.e-24 #print('yoctoseconds (1.e-24)')
                        elif htu=='zs':
                            fac = 1.e-21 # print('zeptoseconds (1.e-21)')
                        elif htu=='as':
                            fac = 1.e-18 # print('attoseconds (1.e-18)')
                        elif htu=='fs':
                            fac = 1.e-15 # print('femtosecond (1.e-15)')
                        elif htu=='ps':
                            fac = 1.e-12 # print('picoseconds (1.e-12)')
                        elif htu=='ns':
                            fac = 1.e-9 # print('nano-second (1.e-9)')
                        elif htu=='us':
                            fac = 1.e-6 # print('us (microsecond?) (1.e-6)')
                        elif htu=='ms':
                            fac = 1.e-3 # print('milliseconds (1.e-3)')
                        elif htu==' s':
                            fac = 1.0 # print('second')
                        elif htu==' h':
                            fac = hour # print('hours')
                        elif htu==' d':
                            fac = day # print('day')
                        elif htu==' m':
                            fac = month # print('month')
                        elif htu==' y':
                            fac = year # print('year')
                        elif htu=='ky':
                            fac = 1e3 * year # print('Kiloyears (1e3)')
                        elif htu=='My':
                            fac = 1e6 * year # print('Megayears (1e6)')
                        elif htu=='Gy':
                            fac = 1e9 * year # print('Gigayears (1e9)')
                        elif htu=='Ty':
                            fac = 1e12 * year # print('Terayears (1e12)')
                        elif htu=='Py':
                            fac = 1e15 * year # print('Petayears (1e15)')
                        elif htu=='Ey':
                            fac = 1e18 * year # print('Exayears (1e18)')
                        elif htu=='Zy':
                            fac = 1e21 * year # print('Zettayears (1e21)')
                        elif htu=='Yy':
                            fac = 1e24 * year # print('Yottayears (1e24)')
                        else:
                            print('unknown lifetime unit')
                            print('ht:',ht,' unit:',htu)
                            print('Exit()')
                            exit()
                    hts = ht * fac
                    year=line[cyear:cyear+4]
                    if nuda.env.verb: print('   year:',year)
                    # check if there is '#' in the string or if the value is absent:
                    #if ' '*11 in line[18:31]: continue
                    #print("   test:",line[cbe:cdbe],".",(cdbe-cbe))
                    #if '#' in line[cbe:cdbe]:
                    # check that there is a data for the measured mass:
                    if line[cbe:cdbe] == ' '*(cdbe-cbe): continue
                    if '#' in line[cbe:cdbe]:
                        ME=float(line[cbe:cdbe].replace('#',''))
                        ME_err=float(line[cdbe:cdbee].replace('#',''))
                        interp = 'y'
                        year=int(version)+10 # define a fake year which is after the table release
                    else:
                        ME=float(line[cbe:cdbe])
                        ME_err=float(line[cdbe:cdbee])
                        interp = 'n'
                        #print('type(year):',type(year))
                        #print('len(year):',len(year))
                        #nucYear=int(year)
                        if len(year) == 4 and year != ' '*4: 
                            year=int(year)
                        else:
                            year=int(version)+10
                        #if year != ' '*4: nucYear=int(year)
                    if (nuda.env.verb): print("   ME:",ME,' +- ',ME_err,' keV')
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
                    if year > self.year_max: 
                        self.year_max = year
                        #self.i_max = nbNuc
                    if year < self.year_min: 
                        self.year_min = year
                        #self.i_min = nbNuc
                    #print('nucYear:',nucYear,self.year_min)
                    #
                    Mass = AA * CST_AtmMass + ME / 1000.0 # conversion to MeV
                    Mass_err = ME_err / 1000.0 
                    # nucBE = ( nucMass - nucZ * ( CST_mpc2 + CST_mec2 ) - nucN * CST_mnc2 )
                    BE = ME / 1000.0 - ZZ * CST_mHc2 - NN * CST_mnc2
                    BE_err = math.sqrt( Mass_err**2 + ZZ * CST_dmHc2**2 + NN * CST_dmnc2**2 )
                    if (nuda.env.verb): print("   BE:",BE,' +- ',BE_err)
                    # add nucleus to the table
                    self.nucA.append( AA )
                    self.nucZ.append( ZZ )
                    if ZZ > self.Zmax: self.Zmax = ZZ
                    self.nucN.append( NN )
                    self.nucI.append( II )
                    self.nucSymb.append( symb )
                    self.flagI.append( flagI )
                    self.flagInterp.append( interp )
                    self.nucStbl.append( stbl )
                    self.nucHT.append( hts )
                    self.nucYear.append( year )
                    self.nucBE.append( BE )
                    self.nucBE_err.append( BE_err )
                    nbNuc = nbNuc + 1
            if self.year_max > int(version): self.year_max = int(version)
            #: Attribute with the number of line in the file.
            self.nbLine = nbLine
            #: Attribute with the number of nuclei read in the file.
            self.nbNuc = nbNuc
        print('Oldest discovery is from: ',self.year_min)
        print('Most recent discovery is from: ',self.year_max)
        #
        # clasify per year of discovery discovered 
        #
        dist_nyear = 20
        #mas = nuda.SetupMasses( table = table, version = '2020' )
        #: attribute distribution of years
        self.dist_year = int(self.year_min/10) + np.arange(dist_nyear)
        #: attribute number of nuclei discovered per year
        self.dist_nbNuc = np.zeros( (dist_nyear) )
        for i in range(self.nbNuc):
            i_year = int( (self.nucYear[i]-self.year_min)/10 )
            self.dist_nbNuc[i_year] += 1
        print( 'dist:',self.dist_nbNuc )
        #
        # convert to numpy array:
        #
        self.nucA = np.array( self.nucA , dtype = int )
        self.nucN = np.array( self.nucN , dtype = int )
        self.nucZ = np.array( self.nucZ , dtype = int )
        self.flagI = np.array( self.flagI , dtype = int )
        self.nucYear = np.array( self.nucYear , dtype = int )
        self.nucI = np.array( self.nucI , dtype = float )
        self.nucHT = np.array( self.nucHT , dtype = float )
        self.nucBE = np.array( self.nucBE , dtype = float )
        self.nucBE_err = np.array( self.nucBE_err , dtype = float )
        #
        if nuda.env.verb: print("Exit SetupNucBEExp()")
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
       print("   table:  ",self.table)
       print("   version:",self.version)
       print("   ref:    ",self.ref)
       print("   label:  ",self.label)
       print("   note:   ",self.note)
       if any(self.nucZ): print(f"   Z: {self.nucZ[0:-1:10]}")
       if any(self.nucA): print(f"   A: {self.nucA[0:-1:10]}")
       #
       if nuda.env.verb: print("Exit print_outputs()")
       #
    def select(self, Amin = 0, Zmin = 0, interp = 'n', state= 'gs', nucleus = 'unstable', every = 1):
        """
        Method which select some nuclei from the table according to some criteria.

        :param interp: If interp='n', exclude the interpolated nuclei from the selected ones. \
        If interp='y' consider them in the table, in addition to the others.
        :type interp: str, optional. Default = 'n'.
        :param state: select the kind of state. If state='gs', select nuclei measured in their ground state.
        :type state: str, optional. Default 'gs'.
        :param nucleus: 'unstable'.
        :type nucleus: str, optional. Default 'unstable'. \
        It can be set to 'stable', 'longlive' (with LT>10 min), 'shortlive' (with 10min>LT>1 ns), \
        'veryshortlive' (with LT< 1ns)
        :param every: consider only 1 out of `every` nuclei in the table.
        :type every: int, optional. Default every = 1.

        **Attributes:**
        """

        #
        if nuda.env.verb: print("Enter select()")
        #
        if interp.lower() not in [ 'y', 'n' ]:
            print('setup_be_exp.py: Interp ',interp,' is not "y" or "n".')
            print('setup_be_exp.py: -- Exit the code --')
            exit()
        self.nucInterp = interp
        if nuda.env.verb: print("interp:",interp)
        #
        if state.lower() not in [ 'gs' ]:
            print('setup_be_exp.py: State ',state,' is not "gs".')
            print('setup_be_exp.py: -- Exit the code --')
            exit()
        self.state = state
        if nuda.env.verb: print("state:",state)
        #
        nuclei = [ 'stable', 'unstable', 'longlive', 'shortlive', 'veryshortlive', 'hypershortlive' ]
        #
        if nucleus.lower() not in nuclei:
            print('setup_be_exp.py: Nucleus ',nucleus,' is not in the list: ',nuclei)
            print('setup_be_exp.py: -- Exit the code --')
            exit()
        self.nucleus = nucleus
        if nuda.env.verb: print("nucleus:",nucleus)
        #
        nbNucTot = 0
        nbNucSta = 0
        nbNucSel = 0
        #
        #: Attribute sel_A (mass of the selected nuclei).
        self.sel_nucA = []
        #: Attribute sel_Z (charge of the selected nuclei).
        self.sel_nucZ = []
        #: Attribute sel_symb (symbol of the selected nuclei).
        self.sel_nucSymb = []
        self.sel_nucN = []
        self.sel_nucI = []
        self.sel_flagI = []
        self.sel_flagInterp = []
        self.sel_nucHT = [] # half-time in s
        self.sel_nucYear = []
        self.sel_nucBE = []
        self.sel_nucBE_err = []
        #
        self.sel_Zmax = 0
        #
        for ind in range(self.nbNuc):
            #
            nucA = self.nucA[ind]
            nucZ = self.nucZ[ind]
            nucN = self.nucN[ind]
            nucI = self.nucI[ind]
            flagI = self.flagI[ind]
            nucSymb = self.nucSymb[ind]
            flagInterp = self.flagInterp[ind]
            nucStbl = self.nucStbl[ind]
            nucHT = self.nucHT[ind]
            nucYear = self.nucYear[ind]
            nucBE = self.nucBE[ind]
            nucBE_err = self.nucBE_err[ind]
            #print('select:',ind,nucA,nucZ,nucN,nucSymb)
            # skip nuclei below Amin and Zmin:
            if nucA < Amin or nucZ < Zmin:
                continue
            #
            if nucleus.lower() == 'stable' and nucStbl == 'y':
                pass
            elif nucleus.lower() == 'unstable' and nucStbl == 'n':
                pass
            elif nucleus.lower() == 'longlive' and nucStbl == 'n' and nucHT > HTsl:
                pass
            elif nucleus.lower() == 'shortlive' and nucStbl == 'n' and nucHT < HTsl and nucHT > HTvsl:
                pass
            elif nucleus.lower() == 'veryshortlive' and nucStbl == 'n' and nucHT < HTvsl  and nucHT > HThsl:
                pass
            elif nucleus.lower() == 'hypershortlive' and nucStbl == 'n' and nucHT < HThsl:
                pass
            else:
                continue
            #
            nbNucTot = nbNucTot + 1
            # skip nucleus if interpolated data
            if flagInterp == 'y':
                continue
            # skip nuclei not in GS
            if state == 'gs' and flagI != 0:
                continue
            nbNucSta = nbNucSta + 1
            # skip nuclei depending on every:
            if nbNucSta % every != 0 :
                continue
            nbNucSel = nbNucSel + 1
            self.sel_nucA.append( nucA )
            self.sel_nucZ.append( nucZ )
            if nucZ > self.sel_Zmax: self.sel_Zmax = nucZ
            self.sel_nucN.append( nucN )
            self.sel_nucI.append( nucI )
            self.sel_nucSymb.append( nucSymb )
            self.sel_flagI.append( flagI )
            self.sel_flagInterp.append( flagInterp )
            self.sel_nucHT.append( nucHT )
            self.sel_nucYear.append( nucYear )
            self.sel_nucBE.append( nucBE )
            self.sel_nucBE_err.append( nucBE_err )
        self.sel_nbNucTot = nbNucTot
        self.sel_nbNucSta = nbNucSta
        self.sel_nbNucSel = nbNucSel
        print('number of nuclei(Tot):',self.sel_nbNucTot)
        print('number of nuclei(Sta):',self.sel_nbNucSta)
        print('number of nuclei(Sel):',self.sel_nbNucSel)
        #print(' sel_nucA:',self.sel_nucA)
        # convert to numpy array:
        self.sel_nucA = np.array( self.sel_nucA , dtype = int )
        self.sel_nucN = np.array( self.sel_nucN , dtype = int )
        self.sel_nucZ = np.array( self.sel_nucZ , dtype = int )
        self.sel_flagI = np.array( self.sel_flagI , dtype = int )
        self.sel_nucYear = np.array( self.sel_nucYear , dtype = int )
        self.sel_nucI = np.array( self.sel_nucI , dtype = float )
        self.sel_nucHT = np.array( self.sel_nucHT , dtype = float )
        self.sel_nucBE = np.array( self.sel_nucBE , dtype = float )
        self.sel_nucBE_err = np.array( self.sel_nucBE_err , dtype = float )
        #
        if nuda.env.verb: print("Exit select()")
        #
        return self
        #
    def select_year(self, year_min=1940, year_max=1960, state= 'gs'):
        """
        Method which select some nuclei from the table according to the discovery year.

        :param year_min:
        :type year_min:
        :param year_max:
        :type year_max:
        :param state: select the kind of state. If state='gs', select nuclei measured in their ground state.
        :type state: str, optional. Default 'gs'.

        **Attributes:**
        """
        #
        if self.nucYear is None:
            print('setup_be_exp.py: There is no year in the experimental mass table')
            print('setup_be_exp.py: Table:',self.table)
            print('setup_be_exp.py: Version:',self.version)
            print('setup_be_exp.py: Exit()')
            exit()
        if year_min > int(self.version) or year_max < yearMin:
            print('setup_be_exp.py: year_min or year_max is not well defined')
            print('setup_be_exp.py: year_min:',year_min,' >? ',int(self.version))
            print('setup_be_exp.py: year_max:',year_max,' <? ',yearMin)
            print('setup_be_exp.py: -- Exit the code --')
            exit()
        self.year_min = year_min
        self.year_max = year_max
        #
        if state.lower() not in [ 'gs' ]:
            print('setup_be_exp.py: State ',state,' is not "gs".')
            print('setup_be_exp.py: -- Exit the code --')
            exit()
        self.state = state
        #
        nbNucTot = 0
        nbNucSta = 0
        nbNucSel = 0
        #
        #: Attribute sel_A (mass of the selected nuclei).
        self.sel_A = []
        #: Attribute sel_Z (charge of the selected nuclei).
        self.sel_Z = []
        #: Attribute sel_symb (symbol of the selected nuclei).
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
        for ind in range(self.nbNuc):
            #
            nucA = self.nucA[ind]
            nucZ = self.nucZ[ind]
            nucN = self.nucN[ind]
            nucI = self.flagI[ind]
            nucSymb = self.nucSymb[ind]
            nucInterp = self.flagInterp[ind]
            nucStbl = self.nucStbl[ind]
            nucHT = self.nucHT[ind]
            nucYear = self.nucYear[ind]
            nucBE = self.nucBE[ind]
            nucdBE = self.nucBE_err[ind]
            # skip nuclei out of the year range:
            if nucYear < year_min or nucYear >= year_max:
                continue
            #
            #print('discovery year:',nucYear)
            nbNucTot = nbNucTot + 1
            # skip nucleus if interpolated data
            if nucInterp == 'y':
                continue
            # skip nuclei not in GS
            if state == 'gs' and nucI != 0:
                continue
            nbNucSta = nbNucSta + 1
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
        if nuda.env.verb: print("Exit select()")
        #
        return self
        #
    def isotopes(self, Zref = 50 ):
        """
        Method which find the first and last isotopes for Z=Zref.

        :param Zref: Fix the charge for the search of isotopes.
        :type Zref: int, optional. Default: 50.

        **Attributes:**
        """
        #
        if nuda.env.verb: print("Enter isotopes()")
        #
        if Zref < 0:
            print('setup_be_exp.py: issue with the function isotopes.')
            print('setup_be_exp.py: Bad definition for Zref')
            print('setup_be_exp.py: It is expected that Zref>0')
            print('setup_be_exp.py: Zref:',Zref)
            print('setup_be_exp.py: exit')
            exit()
        #
        Nstable, Zstable = stable_fit_Z( Zmin = Zref, Zmax = Zref )
        #
        nucNmin = Nstable[0]
        nucNmax = Nstable[0]
        #
        for ind,A in enumerate(self.sel_nucA):
            #
            if self.sel_nucZ[ind] == Zref and self.sel_nucN[ind] < nucNmin:
                nucNmin = self.sel_nucN[ind]
            if self.sel_nucZ[ind] == Zref and self.sel_nucN[ind] > nucNmax:
                nucNmax = self.sel_nucN[ind]
            #
        self.itp_nucZ = Zref
        self.itp_nucNmin = nucNmin
        self.itp_nucNmax = nucNmax
        #
        if nuda.env.verb: print("Exit isotopes()")
        #
        return self
        #
    def isotones(self, Nref = 50 ):
        """
        Method which find the first and last isotones for N=Nref.

        :param Nref: Fix the neutron number for the search of isotones.
        :type Nref: int, optional. Default: 50.

        **Attributes:**
        """
        #
        if nuda.env.verb: print("Enter isotones()")
        #
        if Nref < 0:
            print('setup_be_exp.py: issue with the function isotones.')
            print('setup_be_exp.py: Bad definition for Nref')
            print('setup_be_exp.py: It is expected that Nref>0')
            print('setup_be_exp.py: Nref:',Nref)
            print('setup_be_exp.py: exit')
            exit()
        #
        Nstable, Zstable = stable_fit_N( Nmin = Nref, Nmax = Nref )
        #
        nucZmin = Zstable[0]
        nucZmax = Zstable[0]
        #
        for ind,A in enumerate(self.sel_nucA):
            #
            if self.sel_nucN[ind] == Nref and self.sel_nucZ[ind] < nucZmin:
                nucZmin = self.sel_nucZ[ind]
            if self.sel_nucN[ind] == Nref and self.sel_nucZ[ind] > nucZmax:
                nucZmax = self.sel_nucZ[ind]
            #
        self.itn_nucN = Nref
        self.itn_nucZmin = nucZmin
        self.itn_nucZmax = nucZmax
        #
        if nuda.env.verb: print("Exit isotones()")
        #
        return self
        #
    def S2n( self, Zref = 50 ):
        """
        Compute the two-neutron separation energy (S2n)
        S2n(Zref,N) = E(Zref,N)-E(Zref,N-2)
        """
        #
        if nuda.env.verb: print("Enter S2n()")
        #
        if Zref < 0:
            print('setup_be_exp.py: In S2n attribute function of setup_be_exp.py:')
            print('setup_be_exp.py: Bad definition of Zref')
            print('setup_be_exp.py: It is expected that Zref>=0')
            print('setup_be_exp.py: Zref:',Zref)
            print('setup_be_exp.py: exit')
            exit()
        #
        S2n_N = []
        S2n_E = []
        S2n_E_err = []
        #
        Nmin=self.itp_nucNmin
        Nmax=self.itp_nucNmax
        print('Nmin,Nmax:',Nmin,Nmax)
        #
        for N in range(Nmin+2,Nmax+1):
            #
            flagN = False; flagNm2 = False;
            #
            for ind,Z in enumerate(self.sel_nucZ):
                #
                if Z == Zref and self.sel_nucN[ind] == N:
                    indN = ind
                    flagN = True
                if Z == Zref and self.sel_nucN[ind] == N-2:
                    indNm2 = ind
                    flagNm2 = True
                    #
            if flagN and flagNm2:
                S2n_N.append( N )
                S2n_E.append( self.sel_nucBE[indN] - self.sel_nucBE[indNm2] )
                S2n_E_err.append( self.sel_nucBE_err[indN] + self.sel_nucBE_err[indNm2] )
        self.S2n_N = np.array( S2n_N, dtype = int )
        self.S2n_E = np.array( S2n_E, dtype = float )
        self.S2n_E_err = np.array( S2n_E_err, dtype = float )
        #
        if nuda.env.verb: print("Exit S2n()")
        #
        return self
        #
    def S2p( self, Nref = 50 ):
        """
        Compute the two-proton separation energy (S2p)
        S2p(Z,Nref) = E(Z,Nref)-E(Z-2,Nref)
        """
        #
        if nuda.env.verb: print("Enter S2p()")
        #
        if Nref < 0:
            print('setup_be_exp.py: In S2p attribute function of setup_be_exp.py:')
            print('setup_be_exp.py: Bad definition of Nref')
            print('setup_be_exp.py: It is expected that Nref>=0')
            print('setup_be_exp.py: Nref:',Nref)
            print('setup_be_exp.py: exit')
            exit()
        #
        S2p_Z = []
        S2p_E = []
        S2p_E_err = []
        #
        Zmin=self.itn_nucZmin
        Zmax=self.itn_nucZmax
        print('Zmin,Zmax:',Zmin,Zmax)
        #
        for Z in range(Zmin+2,Zmax+1,2):
            #
            flagZ = False; flagZm2 = False;
            #
            for ind,N in enumerate(self.sel_nucN):
                #
                if N == Nref and self.sel_nucZ[ind] == Z:
                    indZ = ind
                    flagZ = True
                if N == Nref and self.sel_nucZ[ind] == Z-2:
                    indZm2 = ind
                    flagZm2 = True
                    #
            if flagZ and flagZm2:
                S2p_Z.append( Z )
                S2p_E.append( self.sel_nucBE[indZ] - self.sel_nucBE[indZm2] )
                S2p_E_err.append( self.sel_nucBE_err[indZ] + self.sel_nucBE_err[indZm2] )
        self.S2p_Z = np.array( S2p_Z, dtype = int )
        self.S2p_E = np.array( S2p_E, dtype = float )
        self.S2p_E_err = np.array( S2p_E_err, dtype = float )
        #
        if nuda.env.verb: print("Exit S2p()")
        #
        return self
        #
    def D3n( self, Zref = 50 ):
        """
        Compute the three-points odd-even mass staggering (D3p_n)
        D3n(Z,N) = (-)**N * ( 2*E(Z,N)-E(Z,N+1)-E(Z,N-1) ) / 2
        """
        #
        if nuda.env.verb: print("Enter D3n()")
        #
        if Zref < 0:
            print('setup_be_exp.py: In D3n attribute function of setup_be_exp.py:')
            print('setup_be_exp.py: Bad definition of Zref')
            print('setup_be_exp.py: It is expected that Zref>=0')
            print('setup_be_exp.py: Zref:',Zref)
            print('setup_be_exp.py: exit')
            exit()
        #
        D3n_N_even = []
        D3n_N_odd = []
        D3n_E_even = []
        D3n_E_odd = []
        D3n_E_err_even = []
        D3n_E_err_odd = []
        #
        Nmin=self.itp_nucNmin
        Nmax=self.itp_nucNmax
        print('Nmin,Nmax:',Nmin,Nmax)
        #
        for N in range(Nmin+1,Nmax):
            #
            flagN = False; flagNm1 = False; flagNp1 = False;
            #
            for ind,Z in enumerate(self.sel_nucZ):
                #
                if Z == Zref and self.sel_nucN[ind] == N:
                    indN = ind
                    flagN = True
                    if N % 2:
                        sign = -1.0 # odd
                    else:
                        sign = 1.0 # even
                if Z == Zref and self.sel_nucN[ind] == N-1:
                    indNm1 = ind
                    flagNm1 = True
                if Z == Zref and self.sel_nucN[ind] == N+1:
                    indNp1 = ind
                    flagNp1 = True
                    #
            if flagN and flagNm1 and flagNp1:
                if sign > 0.0: #even
                    D3n_N_even.append( N )
                    D3n_E_even.append( sign/2.0*( -2*self.sel_nucBE[indN] + self.sel_nucBE[indNm1] + self.sel_nucBE[indNp1] ) )
                    D3n_E_err_even.append( 0.5*( 2*self.sel_nucBE_err[indN] + self.sel_nucBE_err[indNm1] + self.sel_nucBE_err[indNp1] ) )
                else:
                    D3n_N_odd.append( N )
                    D3n_E_odd.append( sign/2.0*( -2*self.sel_nucBE[indN] + self.sel_nucBE[indNm1] + self.sel_nucBE[indNp1] ) )
                    D3n_E_err_odd.append( 0.5*( 2*self.sel_nucBE_err[indN] + self.sel_nucBE_err[indNm1] + self.sel_nucBE_err[indNp1] ) )
            #
        self.D3n_N_even = np.array( D3n_N_even, dtype = int )
        self.D3n_E_even = np.array( D3n_E_even, dtype = float )
        self.D3n_E_err_even = np.array( D3n_E_err_even, dtype = float )
        self.D3n_N_odd = np.array( D3n_N_odd, dtype = int )
        self.D3n_E_odd = np.array( D3n_E_odd, dtype = float )
        self.D3n_E_err_odd = np.array( D3n_E_err_odd, dtype = float )
        #
        if nuda.env.verb: print("Exit D3n()")
        #
        return self
        #
    def D3p( self, Nref = 50 ):
        """
        Compute the three-points odd-even mass staggering (D3p_n)
        D3p(Z,N) = (-)**Z * ( 2*E(Z,N)-E(Z+1,N)-E(Z-1,N) ) / 2
        """
        #
        if nuda.env.verb: print("Enter D3p()")
        #
        if Nref < 0:
            print('setup_be_exp.py: In D3p attribute function of setup_be_exp.py:')
            print('setup_be_exp.py: Bad definition of Nref')
            print('setup_be_exp.py: It is expected that Nref>=0')
            print('setup_be_exp.py: Nref:',Nref)
            print('setup_be_exp.py: exit')
            exit()
        #
        D3p_Z_even = []
        D3p_Z_odd = []
        D3p_E_even = []
        D3p_E_odd = []
        D3p_E_err_even = []
        D3p_E_err_odd = []
        #
        Zmin=self.itn_nucZmin
        Zmax=self.itn_nucZmax
        print('Zmin,Zmax:',Zmin,Zmax)
        #
        for Z in range(Zmin+1,Zmax):
            #
            flagZ = False; flagZm1 = False; flagZp1 = False;
            #
            for ind,N in enumerate(self.sel_nucN):
                #
                if N == Nref and self.sel_nucZ[ind] == Z:
                    indZ = ind
                    flagZ = True
                    if Z % 2:
                        sign = -1.0 # odd
                    else:
                        sign = 1.0 # even
                if N == Nref and self.sel_nucZ[ind] == Z-1:
                    indZm1 = ind
                    flagZm1 = True
                if N == Nref and self.sel_nucZ[ind] == Z+1:
                    indZp1 = ind
                    flagZp1 = True
                    #
            if flagZ and flagZm1 and flagZp1:
                if sign > 0.0: #even
                    D3p_Z_even.append( Z )
                    D3p_E_even.append( sign/2.0*( -2*self.sel_nucBE[indZ] + self.sel_nucBE[indZm1] + self.sel_nucBE[indZp1] ) )
                    D3p_E_err_even.append( 0.5*( 2*self.sel_nucBE_err[indZ] + self.sel_nucBE_err[indZm1] + self.sel_nucBE_err[indZp1] ) )
                else:
                    D3p_Z_odd.append( Z )
                    D3p_E_odd.append( sign/2.0*( -2*self.sel_nucBE[indZ] + self.sel_nucBE[indZm1] + self.sel_nucBE[indZp1] ) )
                    D3p_E_err_odd.append( 0.5*( 2*self.sel_nucBE_err[indZ] + self.sel_nucBE_err[indZm1] + self.sel_nucBE_err[indZp1] ) )
            #
        self.D3p_Z_even = np.array( D3p_Z_even, dtype = int )
        self.D3p_E_even = np.array( D3p_E_even, dtype = float )
        self.D3p_E_err_even = np.array( D3p_E_err_even, dtype = float )
        self.D3p_Z_odd = np.array( D3p_Z_odd, dtype = int )
        self.D3p_E_odd = np.array( D3p_E_odd, dtype = float )
        self.D3p_E_err_odd = np.array( D3p_E_err_odd, dtype = float )
        #
        if nuda.env.verb: print("Exit D3p()")
        #
        return self
        #
