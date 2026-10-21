import numpy as np
import os

def create_dictionary_boundary():
	# scan all files in layers and store boundaries for den, pre and rho
	layers = [ 'atmosphere', 'outer_crust', 'inner_crust', 'outer_core', 'inner_core1','inner_core2' ]
	dic = {}
	for layer in layers:
		dic[layer] = {}
		print(f'In {layer}:')
		eoss = [fn for fn in os.listdir(layer) if fn.endswith('.dat')]
		if '.DS_Store' in eoss:
			eoss.remove('.DS_Store')
		#print(f'eoss: {eoss}')
		for eos in eoss:
			dic[layer][eos] = {}
			#print(f'eos: {eos}')
			fname = layer+'/'+eos
			print(f'fname: {fname}')
			rho, pre, den = np.loadtxt( fname, usecols=(0,1,2), unpack = True )
			den_min = min(den); den_max = max(den);
			pre_min = min(pre); pre_max = max(pre);
			rho_min = min(rho); rho_max = max(rho);
			dic[layer][eos]['den'] = [ den_min, den_max ]
			dic[layer][eos]['pre'] = [ pre_min, pre_max ]
			dic[layer][eos]['rho'] = [ rho_min, rho_max ]
	# save dic in file
	save_dict_to_file(dic)


def save_dict_to_file(dic):
    f = open('dict.txt','w')
    f.write(str(dic))
    f.close()

def load_dict_from_file():
    f = open('dict.txt','r')
    data=f.read()
    f.close()
    return eval(data)

if __name__ == "__main__":
    create_dictionary_boundary()
