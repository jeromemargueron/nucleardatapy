import numpy as np
import os
from pathlib import Path
import nucleardatapy as nuda

def get_boundaries(fname):
    rho, pre, den = np.loadtxt(fname, usecols=(0, 1, 2), unpack=True)
    return {
        'den': [float(np.min(den)), float(np.max(den))],
        'pre': [float(np.min(pre)), float(np.max(pre))],
        'rho': [float(np.min(rho)), float(np.max(rho))]
    }

def available_models(layer):
    layers = ['atmosphere', 'outer_crust', 'inner_crust', 'outer_core', 'inner_core']

    if layer not in layers:
        raise KeyError(f"Wrong layer '{layer}'. Available layers: {layers}")

    path_layer = os.path.join(nuda.param.path_eos, layer)

    if layer != 'inner_core':
        return {
            layer: [
                os.path.splitext(fn)[0]
                for fn in os.listdir(path_layer)
                if os.path.isfile(os.path.join(path_layer, fn))
            ]
        }

    models = {}

    for eos_type in ['YM', 'QM']:
        path_type = os.path.join(path_layer, eos_type)

        if os.path.isdir(path_type):
            models[eos_type] = [
                os.path.splitext(fn)[0]
                for fn in os.listdir(path_type)
                if os.path.isfile(os.path.join(path_type, fn))
            ]

    return {layer: models}


"""

def save_dict_to_file(dic):
    fname = os.path.join(nuda.param.path_eos,'dict_boundaries.txt')
    with open(fname, 'w') as f:
        f.write(repr(dic))

def load_dict_from_file():
    with open('nuda.param.path_eos/dict_boundaries.txt', 'r') as f:
        return eval(f.read())




if __name__ == "__main__":
    create_boundaries()
    
    
BOUNDARIES_FILE = os.path.join(nuda.param.path_eos,'dict_boundaries.txt')

if not os.path.isfile(BOUNDARIES_FILE):
    create_boundaries()
    
"""
