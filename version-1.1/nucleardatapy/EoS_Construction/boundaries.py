import numpy as np
import os

def get_boundaries(fname):
    rho, pre, den = np.loadtxt(fname, usecols=(0, 1, 2), unpack=True)
    return {
        'den': [float(np.min(den)), float(np.max(den))],
        'pre': [float(np.min(pre)), float(np.max(pre))],
        'rho': [float(np.min(rho)), float(np.max(rho))]
    }

def create_dictionary_boundary():
    layers = ['atmosphere', 'outer_crust', 'inner_crust', 'outer_core', 'inner_core']
    dic = {}

    for layer in layers:
        dic[layer] = {}
        print(f'In {layer}:')

        if layer != 'inner_core':
            eoss = [fn for fn in os.listdir(layer) if fn.endswith('.dat')]
            for eos in eoss:
                fname = os.path.join(layer, eos)
                print(f'fname: {fname}')
                dic[layer][eos] = get_boundaries(fname)

        else:
            for eos_type in ['YM', 'QM']:
                type_path = os.path.join(layer, eos_type)
                if not os.path.isdir(type_path):
                    continue

                dic[layer][eos_type] = {}
                print(f'  Type: {eos_type}')

                eoss = [fn for fn in os.listdir(type_path) if fn.endswith('.dat')]
                for eos in eoss:
                    fname = os.path.join(type_path, eos)
                    print(f'  fname: {fname}')
                    dic[layer][eos_type][eos] = get_boundaries(fname)

    save_dict_to_file(dic)

def save_dict_to_file(dic):
    with open('dict.txt', 'w') as f:
        f.write(repr(dic))

def load_dict_from_file():
    with open('dict.txt', 'r') as f:
        return eval(f.read())

if __name__ == "__main__":
    create_dictionary_boundary()
