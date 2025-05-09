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
$ pip install nucleardatapy
```
This installs the lattest version of the toolkit.

Now everything is done about the installation. 

## Test the python toolkit

A set of tests can be easily performed. They are stored in tests/ folder.

Launch:

```
$ bash run_tests.sh
```

## Short introduction to the toolkit:

The call of the toolkit in python code is performed in the usual way:
```Python
import nucleardatapy as nuda
```

The list of functions and global variables available in the toolkit can be printed from the following instruction:
```Python
print(dir(nuda))
```

A detailed view of the function can be obtained in the following way
```Python
print(help(nuda))
```

The principle of the toolkit is that it instantiates objects that contain all the information available. For instance, the following command
```Python
mass = nuda.astro.setupMasses()
```
instantiate the object `mass` with the default mass of pulsars. In this case, it is the mass of PSR J1614-2230. All the properties that this object provide can be listed in the following way:
```Python
mass.__dict__
```

## Use nucleardatapy python toolkit

The GitHub folder `nucleardatapy/nucleardatapy_samples/` contains a lot of examples on how to use the function and to draw figures. They are all python scripts that can be launched with `python3`. For instance, you can grab these samples anywhere in your computer and try:
```
$ python3 matter_setupMicro_script.py
```

There are also tutorials that can be employed to learn how to use the different functions in the toolkit. The tutorials are written for `jupyter notebook`.

## Get started

Here is an example to obtain microscopic results for APR equation of state:

```Python
import nucleardatapy as nuda

# Instantiate a micro object
micro = nuda.matter.setMicro( model = '1998-VAR-AM-APR')

# print outputs
micro.print_outputs( )
```

More examples are shown in the associated paper[Give reference here], as well as in the sample folder or tutorials as previously written.


## Contributing

The file `how_to_contribute.md` details how contributors could join our team or share their results.

## License

CC BY-NC-ND 4.0

## Report issues

Issues can be reported using GitHub.

## Thanks

A special thanks to all contributors who accepted to share their results in this toolkit.


