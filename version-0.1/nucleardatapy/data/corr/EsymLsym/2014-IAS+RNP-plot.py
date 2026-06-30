
import numpy as np
import matplotlib.pyplot as plt

def func(x,xmin,xmax,ymin,ymax):
	return ymin + (x-xmin)/(xmax-xmin)*(ymax-ymin)

Lsym, Esym = np.loadtxt( '2014-IAS+RNP.dat', usecols=(0,1), unpack=True )
Esym2, Lsym2, Lsym2_err = np.loadtxt( '2014-IAS+RNP-err.dat', usecols=(0,1,2), unpack=True )

plt.plot(Esym,Lsym)
plt.errorbar(Esym2,Lsym2,yerr=Lsym2_err)

plt.savefig('test.png')
plt.close()

#print('y_max(28.8):',func(28.8,28,34.8,15,100))
#print('y_min(34.8):',func(34.8,28.8,37.5,8,95))
#print('y_cent(31.0):',func(31.0,28.8,34.8,16.5,84))
#print('y_cent(33.0):',func(33.0,28.8,34.8,16.5,84))
#print('y_max(31.0):',func(31.0,28,34.8,15,100))
#print('y_max(33.0):',func(33.0,28,34.8,15,100))
#print('y_min(31.0):',func(31.0,28.8,37.5,8,95))
#print('y_min(33.0):',func(33.0,28.8,37.5,8,95))
