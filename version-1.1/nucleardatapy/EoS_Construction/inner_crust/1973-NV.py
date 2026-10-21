import nucleardatapy as nuda
#import numpy as np
#import os

def create_NV_crust_EOS():
	model = '1973-Negele-Vautherin'
	crust = nuda.crust.setupCrust( model = model )
	print(f'den_cgs: {crust.den_cgs}')
	print("size:",crust.den_cgs.size)
	with open("1973-NV.dat", "w") as f:
		f.write('# Negele Vautherin crust NPA (1973).\n')
		f.write('# ref: G. Baym, H.A. Bethe, C. J. Pethick, NPA 175, 225 (1971)\n')
		f.write('# rho pre nb A Z\n')
		f.write('# g/cc dyn.cm2 cm-3\n')
		for k, value in enumerate(crust.den_cgs):
			print('nb:',value,crust.den_cgs[k])
			f.write(f'{crust.eps_tot[k]} {crust.pre_tot[k]} {value} {crust.A[k]} {crust.Z[k]}\n')



if __name__ == "__main__":
    create_NV_crust_EOS()