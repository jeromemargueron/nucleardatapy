# nucdatapy

This python toolkit is designed to provide 1) microscopic calculations
in nuclear matter, 2) phenomenological predictions in nuclear matter,
and 3) experimental data from finite nuclei.

Install the toolkit:

$ bash install.sh

Using TestPyPI with pip:

$ python3 -m pip install --index-url https://test.pypi.org/simple/ nucdatapy

Create an environement variable that will be used by python:

export NUCDATAPY_TK=/path/to/nucdatapy-tk

put this command in your .profile or .zprofile of .bashrc for instance.

Now everything is done about the compilation. You can come back to the
python folder.

# Finally, use the python toolkit

go to the folder samples/ and try that:

$ python3 sample_tovSolver_read.py

# Test the python toolkit

A set of tests can be easily performed. They are stored in tests/
folder.

Launch:

$ bash tests_run.bash


