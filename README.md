# The toolkit `nucleardatapy`

## Purpose:

<img align="right" width="250" src="book/logo.png">

The purpose of this toolkit is to provide an easy access to theoretical or experimental or observational data and allows meta-analyses in a straightforward way.

This python toolkit is designed to provide:

1. microscopic calculations in nuclear matter,
2. phenomenological predictions in nuclear matter,
3. experimental data for finite nuclei,
4. astrophysical observations and theoretical predictions.

All data are provided with their reference, so when using these data in a scientific paper, reference to data should be provided explicitly. The reference to this toolkit could be given, but it should not mask the reference to the original source of data.

## Installation of the toolkit:

To install the toolkit, launch:

```
$ pip install nucleardatapy
```

This installs the latest version of the toolkit.

If the github repository is downloaded, one can also install the toolkit using

```
$ pip install -e .
```

from within the root folder of the nucleardatapy directory.

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

The toolkit classes instantiate objects that contain all the information available. For instance, the following command

```Python
mass = nuda.astro.setupMasses()
```

instantiates the object `mass` with the mass of PSR J1614-2230 which is the default case. All the properties of this object can be listed in the following way:

```Python
mass.__dict__
```

## Documentation

The documentation for the toolkit can be found here: [https://nucleardatapy.readthedocs.io/en/latest/index.html](https://nucleardatapy.readthedocs.io/en/latest/index.html). The documentation is also available in the docs/ folder and can be built using the following command:

```
sphinx-build -b html docs docs/build_html
```

The pdf version of the documentation can be found by clicking this [link](https://github.com/jeromemargueron/nucleardatapy/blob/main/docs/nucleardatapy.pdf).

## Tutorials

The tutorials to get started with nucleardatapy toolkit can be found here: [https://jeromemargueron.github.io/nucleardatapy/landing.html](https://jeromemargueron.github.io/nucleardatapy/landing.html). The tutorials are written using `jupyter notebook` and can be tried on your computer by downloading them or by using `google-colab`. In the github repository, the tutorials are available in the book/notebooks folder.

## Use nucleardatapy python toolkit

The GitHub folder `nucleardatapy/nucleardatapy_samples/` contains a lot of examples on how to use the function and to draw figures. They are all python scripts that can be launched with `python3`. For instance, you can grab these samples anywhere in your computer and try:

```
$ python3 matter_setupMicro_script.py
```

There are also tutorials that can be employed to learn how to use the different functions in the toolkit.

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

Issues can be reported using [GitHub Issues](https://github.com/jeromemargueron/nucleardatapy/issues).

## Thanks

A special thanks to all contributors who accepted to share their results in this toolkit.
