import numpy as np
import os
from pathlib import Path
import nucleardatapy as nuda


def available_models(layer):
    layers = ['atmosphere', 'outer_crust', 'inner_crust', 'outer_core', 'inner_core']

    if layer not in layers:
        raise KeyError(f"Wrong layer '{layer}'. Available layers: {layers}")

    path_layer = os.path.join(nuda.param.path_eos, layer)

    if layer != 'inner_core':
        models = [os.path.splitext(fn)[0] for fn in os.listdir(path_layer) if os.path.isfile(os.path.join(path_layer, fn))]

        if layer == 'outer_core':
            models += nuda.matter.micro_esym_models()[0]
            models += [model for m in nuda.matter.pheno_esym_models()[0] for model in nuda.pheno_esym_params(model=m)[0]]

        return {layer: sorted(set(models))}

    models = {}

    for eos_type in ['YM', 'QM']:
        path_type = os.path.join(path_layer, eos_type)

        if os.path.isdir(path_type):
            models[eos_type] = [os.path.splitext(fn)[0] for fn in os.listdir(path_type) if os.path.isfile(os.path.join(path_type, fn))]

    return {layer: models}




def available_modelsi(layer):
    layers = ['atmosphere', 'outer_crust', 'inner_crust', 'outer_core', 'inner_core']

    if layer not in layers:
        raise KeyError(f"Wrong layer '{layer}'. Available layers: {layers}")

    path_layer = os.path.join(nuda.param.path_eos, layer)

    if layer != 'inner_core':
        models = [os.path.splitext(fn)[0] for fn in os.listdir(path_layer) if os.path.isfile(os.path.join(path_layer, fn))]

        if layer == 'outer_core':
            param_nuda = []
            model_types, _ = nuda.matter.matter_models()
            for model_type in model_types:
                params, params_lower = nuda.matter.matter_esym_params( model = model_type)
                param_nuda += params
            
            models += param_nuda
            #models += [model for m in nuda.matter.pheno_esym_models()[0] for model in nuda.pheno_esym_params(model=m)[0]]

        return {layer: sorted(set(models))}

    models = {}

    for eos_type in ['YM', 'QM']:
        path_type = os.path.join(path_layer, eos_type)

        if os.path.isdir(path_type):
            models[eos_type] = [os.path.splitext(fn)[0] for fn in os.listdir(path_type) if os.path.isfile(os.path.join(path_type, fn))]

    return {layer: models}


