import numpy as np
import os

import nucleardatapy as nuda

def get_boundaries(fname):
    rho, pre, den = np.loadtxt(fname, usecols=(0, 1, 2), unpack=True)
    return {
        'den': [float(np.min(den)), float(np.max(den))],
        'pre': [float(np.min(pre)), float(np.max(pre))],
        'rho': [float(np.min(rho)), float(np.max(rho))]
    }

def create_boundaries():
    layers = ['atmosphere', 'outer_crust', 'inner_crust', 'outer_core', 'inner_core']
    dic = {}

    for layer in layers:
        dic[layer] = {}
        print(f'In {layer}:')

        if layer != 'inner_core':
            path_layer = nuda.param.path_eos+'/'+layer
            eoss = [fn for fn in os.listdir(path_layer) if fn.endswith('.dat')]
            for eos in eoss:
                fname = os.path.join(path_layer, eos)
                print(f'fname: {fname}')
                dic[layer][eos] = get_boundaries(fname)

        else:
            for eos_type in ['YM', 'QM']:
                path_type = os.path.join(path_layer, eos_type)
                if not os.path.isdir(path_type):
                    continue

                dic[layer][eos_type] = {}
                print(f'  Type: {eos_type}')

                eoss = [fn for fn in os.listdir(path_type) if fn.endswith('.dat')]
                for eos in eoss:
                    fname = os.path.join(path_type, eos)
                    print(f'  fname: {fname}')
                    dic[layer][eos_type][eos] = get_boundaries(fname)

    save_dict_to_file(dic)

def save_dict_to_file(dic):
    with open('nuda.param.path_eos/dict_boundaries.txt', 'w') as f:
        f.write(repr(dic))

def load_dict_from_file():
    with open('nuda.param.path_eos/dict_boundaries.txt', 'r') as f:
        return eval(f.read())

if __name__ == "__main__":
    create_dictionary_boundary()
