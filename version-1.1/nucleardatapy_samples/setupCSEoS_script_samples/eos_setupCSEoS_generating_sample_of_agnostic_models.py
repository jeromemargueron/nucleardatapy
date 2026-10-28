import nucleardatapy as nuda
import numpy as np
import os
import h5py







def Generate_many_extrapolated_EoSs_and_Save_them_h5py(output_folder="Random_agnostic_EoSs",fname=None, n_seeds=10):
    #
    print(50*'-')
    print("Enter in function eos_setupCSEoS_generating_sample_of_agnostic_models:")
    print(50*'-')
    print("Generates a sample of EoSs with random seeds and saves the EoS and related information in a h5py file ")
    print("pass the number of EoSs you want as n_seeds=n, default n=10")
    print("Pass the folder name you want :output_folder, default : Random_agnostic_EoSs")
    print("Pass the file name you want :fname, default : random_eoss_{n_seeds}.h5")
    
    os.makedirs(output_folder, exist_ok=True)
    if fname is None:
        filename = os.path.join(output_folder, f"random_eoss_{n_seeds}.h5")
    else:
        filename = os.path.join(output_folder, f"{fname}.h5")
    
    eos_object = {"outer_core": {"model": "2019-l59",
                                "function": "random_speed_of_sound","parameters": { "den_tr": 0.2, "den_max": 2.0} }}

    with h5py.File(filename, "w") as f:
        for seed in range(n_seeds):
            eos_object["outer_core"]["parameters"]["seed"] = seed
            try:
                eos = nuda.eos.setupCSEoS(eos_object=eos_object,full_outputs=True)
                eos.Final_EoS()
                if not all( getattr(eos, key, None) is not None for key in ("den_tot", "pre_tot", "eps_tot", "cs2_tot") ):
                    print(f"Seed {seed}: missing EoS data. Skipping.")
                    continue

                # Save data for this seed
                g = f.create_group(f"seed_{seed}")

                for key in ("den_tot", "pre_tot", "eps_tot", "cs2_tot"):
                    g.create_dataset(key, data=getattr(eos, key))
                for key in ("den_random_extrapolation", "cs2_random_extrapolation"):
                    value = getattr(eos, key, None)
                    if value is not None:
                        g.create_dataset(key, data=value)

                # Save transition-point quantities and units
                for key in ("den_tr", "pre_tr", "eps_tr", "cs2_tr", "den_unit", "pre_unit", "eps_unit", "cs2_unit"):
                    value = getattr(eos, key, None)
                    if value is not None:
                        g.attrs[key] = str(value)

                # Save the seed and model
                g.attrs["seed"] = seed
                for layer, model in eos.eos_layers.items():
                    g.attrs[layer] = str(model)
                print(f"\n Succed for Seed: {seed}")
            except Exception as exc:
                print(f"Seed {seed} failed: {exc}")
                continue

    print(f"\n All successful EoSs and their details are saved in:\n{filename}")
    print(50*'-')
    print("Exit eos_setupCSEoS_generating_sample_of_agnostic_models")
    print(50*'-')

    #return filename
    
     
 

def Generate_many_extrapolated_EoSs_and_Save_them_json(output_folder="Random_agnostic_EoSs", fname=None, n_seeds=10):
    #
    print(50*'-')
    print("Enter in function eos_setupCSEoS_generating_sample_of_agnostic_models:")
    print(50*'-')
    print("Generates a sample of EoSs with random seeds and saves the EoS and related information in a JSON file.")
    print("Pass the number of EoSs you want as n_seeds=n, default n=10")
    print("Pass the folder name you want: output_folder, default: Random_agnostic_EoSs")
    print("Pass the file name you want: fname, default: random_eoss_{n_seeds}.json")
    import json

    os.makedirs(output_folder, exist_ok=True)

    if fname is None:
        filename = os.path.join(output_folder, f"random_eoss_{n_seeds}.json")
    else:
        filename = os.path.join(output_folder, f"{fname}.json")

    eos_object = { "outer_core": {    "model": "2019-l59",
            "function": "random_speed_of_sound",
            "parameters": {"den_tr": 0.2, "den_max": 2.0}  }}

    json_data = {}

    for seed in range(n_seeds):
        eos_object["outer_core"]["parameters"]["seed"] = seed
        
        

        try:
            eos = nuda.eos.setupCSEoS(eos_object=eos_object, full_outputs=True)
            eos.Final_EoS()
            #print(eos.eos_layers)

            if not all(getattr(eos, key, None) is not None for key in ("den_tot", "pre_tot", "eps_tot", "cs2_tot")):
                print(f"Seed {seed}: missing EoS data. Skipping.")
                continue

            # Save EoS data for this seed
            json_data[f"seed_{seed}"] = {
                "seed": seed,
                "eos_object": json.loads(json.dumps(eos_object)),
                "eos_layers": json.loads(json.dumps(eos.eos_layers)),
                "den_tot": eos.den_tot.tolist(),
                "pre_tot": eos.pre_tot.tolist(),
                "eps_tot": eos.eps_tot.tolist(),
                "cs2_tot": eos.cs2_tot.tolist()
            }

            # Save random extrapolation data
            for key in ("den_random_extrapolation", "cs2_random_extrapolation"):
                value = getattr(eos, key, None)
                if value is not None:
                    json_data[f"seed_{seed}"][key] = value.tolist()

            # Save transition-point quantities and units
            for key in ("den_tr", "pre_tr", "eps_tr", "cs2_tr"):
                value = getattr(eos, key, None)
                if value is not None:
                    json_data[f"seed_{seed}"][key] = value
            for key in ("den_unit", "pre_unit", "eps_unit", "cs2_unit"):
                value = getattr(eos, key, None)
                if value is not None:
                    json_data[f"seed_{seed}"][key] = value

            print(f"\nSucceeded for Seed: {seed}")

        except Exception as exc:
            print(f"Seed {seed} failed: {exc}")
            continue

    # Write all successful EoSs to the JSON file
    with open(filename, "w") as f:
        json.dump(json_data, f, indent=4)

    print(f"\nAll successful EoSs and their details are saved in:\n{filename}")
    print(50*'-')
    print("Exit eos_setupCSEoS_generating_sample_of_agnostic_models")
    print(50*'-')

    
    
    







if __name__ == "__main__":
    Generate_many_extrapolated_EoSs_and_Save_them_h5py()
    Generate_many_extrapolated_EoSs_and_Save_them_json()
    

