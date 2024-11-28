# The toolkit `nucleardatapy`

## Purpose:

The purpose of this toolkit is to simply the access to data, that can be theoretical data or experimental ones. All data are provided with their reference, so when using these data in a scientific paper, reference to data should be provided explicitely. The reference to this toolkit could be given, but it should not mask the reference to data.

This python toolkit is designed to provide: 
1) microscopic calculations in nuclear matter, 
2) phenomenological predictions in nuclear matter,
3) experimental data for finite nuclei.

## Installation of the toolkit:

To install the toolkit, launch:
```
$ bash install.sh
```

In `install.sh`, the default directory where the toolkit is installed is `mylib` in the home directory. There, you have `mylib/nucleardatapy` folder pointing to the version of the toolkit defined in `install.sh` (currently `VER=0.1`). These default options could be changed directly in the header of `install.sh`.

Create an environement variable that will be used by python:
```
export NUCLEARDATAPY_TK=/path/to/nucleardatapy
```

Add this environement variable to the one of python:
```
export PYTHONPATH=$NUCLEARDATAPY_TK
```

In this way, your library will be visible everywhere in your computer.

Put these commands in your `.profile` or `.zprofile` or `.bashrc` for instance (depending on your OS).

The first time, you should run again the `.zprofile` for instance:

```
$ source .zprofile
```

Now everything is done about the installation. You can go to the folder `mylib` in your home directory.

## Use nucleardatapy python toolkit

Go to the folder `mylib/nucleardatapy/samples/nucleardatapy_samples/` and try that:

```
$ python3 sample_SetupMicro.py
```

## Test the python toolkit

A set of tests can be easily performed. They are stored in tests/ folder.

Launch:

```
$ bash run_tests.sh
```

## Get started
How to obtain microscopic results for APR equation of state:

```Python
import os
import sys
nuda_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nuda_tk)

import nucleardatapy as nuda

# Instantiate a microscopic object
mic = nuda.SetMicroMatter( model = '1998-VAR-AM-APR')

# print outputs
mic.print_outputs( )
```

## Contributing

The file `how_to_contribute.md` details how contributors could join our team or share their results.

## License

TBC.

## Report issues

For the current version, we report issues chatting among us. 
Once this toolkit is released, we should setup a way that users could contact us and report issues or difficulties in installing or using the toolkit.

## Thanks

A special thanks to all contributors who accepted to share their results in this toolkit.


