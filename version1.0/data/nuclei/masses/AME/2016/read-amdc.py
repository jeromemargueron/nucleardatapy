# ---------------------------------------------------------
# CODE NAME
# ---------------------------------------------------------
#
# read-amdc.py
#
# ---------------------------------------------------------
# DESCRIPTION
# ---------------------------------------------------------
#
# Read the data from file 'nubtab16d.asc'
#
#
#
# ---------------------------------------------------------
# IMPORT
# ---------------------------------------------------------
#
import math
import matplotlib.pyplot as plt
#
# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

print('*'*10,' HEADER ','*'*10)
print('RUN read-amdc.py (with python3)')
print('*'*30)


# ---------------------------------------------------------
# INPUTS
# ---------------------------------------------------------

# verbose True or False
#verbose=True
verbose=False

# File to read
file_amdc='nubtab16d.asc'

CST_AtmMass = 931.494028
CST_mpc2 = 938.272081
CST_mnc2 = 939.565413
CST_mec2 = 0.5109989461


CST_mnc2 = 8.0713171
CST_dmnc2= 0.0000005
CST_mHc2 = 7.2889706
CST_dmHc2= 0.0000001

print('-'*10)
print('This code reads the parameter files for the various models')
print('AMDC:',file_amdc)

yearMin=1890

print('-'*10)
yearDistX=[]
yearDistY=[]
yearFull=[]
for i in range(15):
    yearDistX.append(yearMin+i*10)
    yearDistY.append(0)
yearIntMin=10000
yearIntMax=0
nbLine=0
nbNuclei=0
with open(file_amdc,'r') as file:
    for line in file:
        nbLine = nbLine + 1
        if (verbose): print('line:'+str(nbLine))
#        if '#' in line[14:40]: continue
        # Read input file:
        nucA=int(line[0:3])
        nucZ=int(line[4:7])
        nucN=nucA-nucZ
        nucName=line[11:17]
        # check if there is '#' in the string or if the value is absent:
        if ' '*11 in line[18:29]: continue
        if '#' in line[18:29]:
            nucME=float(line[18:29].replace('#',''))
            nucdME=float(line[29:38].replace('#',''))
            nucInterp='Y'
        else:
            nucME=float(line[18:29])
            nucdME=float(line[29:38])
            nucInterp='N'
        nucMass = nucA * CST_AtmMass + nucME / 1000.0
        nucdMass = nucdME / 1000.0 
#        nucBE = ( nucMass - nucZ * ( CST_mpc2 + CST_mec2 ) - nucN * CST_mnc2 )
        nucBE = nucME / 1000.0 - nucZ * CST_mHc2 - nucN * CST_mnc2
        nucdBE = math.sqrt( nucdMass**2 + nucZ * CST_dmHc2**2 + nucN * CST_dmnc2**2 )
            
        printLine=False
        if ( nucA == 16 and nucZ == 8 ): printLine=True
        if ( nucA == 34 and nucZ == 14 ): printLine=True
        if ( nucA == 40 and nucZ == 20 ): printLine=True
        if ( nucA == 48 and nucZ == 20 ): printLine=True
        if ( nucA == 52 and nucZ == 20 ): printLine=True
        if ( nucA == 54 and nucZ == 20 ): printLine=True
        if ( nucA == 48 and nucZ == 28 ): printLine=True
        if ( nucA == 56 and nucZ == 28 ): printLine=True
        if ( nucA == 78 and nucZ == 28 ): printLine=True
        if ( nucA == 90 and nucZ == 40 ): printLine=True
        if ( nucA == 100 and nucZ == 50 ): printLine=True
        if ( nucA == 132 and nucZ == 50 ): printLine=True
        if ( nucA == 208 and nucZ == 82 ): printLine=True
        if (printLine): print('A:'+str(nucA)+',Z:'+str(nucZ)+',nucl:'+nucName+',BE:'+str(nucBE)+',dBE:'+str(nucdBE)+',Interpolated:'+nucInterp)

        yearInt = 0
        yearStr=line[105:109]
        if (verbose): print(yearStr)
        if (verbose): print(len(yearStr))
        if ( len(yearStr) == 4 and yearStr != ' '*4 and nucInterp != 'Y' ):
            yearInt=int(yearStr)
            yearFull.append(yearInt)
            yearInd=int((yearInt-yearMin)/10)
            if (verbose): print('year:'+str(yearInt)+',ind:'+str(yearInd))
            yearDistY[yearInd] = yearDistY[yearInd] + 1
            if (yearInt>yearIntMax): yearIntMax=yearInt
            if (yearInt<yearIntMin): yearIntMin=yearInt
            nbNuclei = nbNuclei + 1
        if (verbose): print('.'+yearStr+'.')
       
print('Year min:'+str(yearIntMin)+',input:'+str(yearMin))
print('Year max:'+str(yearIntMax))
print('Number of lines :'+str(nbLine))
print('Number of nuclei:'+str(nbNuclei)+','+str(sum(yearDistY)))
print('yearDistX.:'+str(yearDistX))
print('yearDistY.:'+str(yearDistY))

#Plot histogram for YearDist
plt.hist(yearFull,bins=yearDistX)
plt.title('Number of nuclei discovered per decades')
plt.xlabel('Year')
plt.text(1900,800,'Total:'+str(nbNuclei))
plt.text(2000,800,'AMDC2016')
for i in range(15):
    plt.text(yearDistX[i],yearDistY[i],str(yearDistY[i]))
plt.savefig('yearDist.png')
plt.show()

#Plot histogram for YearDist (zoom 2000)
plt.hist(yearFull,bins=8,range=(2000,2016))
plt.title('Number of nuclei discovered since 2000')
plt.xlabel('Year')
plt.text(2013,60,'AMDC2016')
plt.savefig('yearDist-2000.png')
plt.show()
