
Usage
=====

.. _installation:

Installation
------------

To install the toolkit, launch:

.. code-block:: console

   $ pip install nucleardatapy

This installs the lattest version of the toolkit.

Now everything is done about the installation.

Test
------------

A set of tests can be easily performed. They are stored in tests/ folder.

Launch:

.. code-block:: console

   $ bash run_tests.sh

   
.. _Use:

Use nucleardatapy
-----------------

The GitHub folder `nucleardatapy/nucleardatapy_samples/` contains a
lot of examples on how to use the function and to draw figures. They
are all python scripts that can be launched with `python3`. For
instance, you can grab these samples anywhere in your computer and
try:

.. code-block:: console

   $ python3 matter_setupMicro_script.py

.. _Get started:

Get started
-----------

How to obtain microscopic results for APR equation of state:

.. code-block:: python

   import nucleardatapy as nuda

   # Instantiate the micro object with the content of the APR equation
   of state
   micro = nuda.matter.setMicro( model = '1998-VAR-AM-APR')

   # print outputs from the micro object
   micro.print_outputs( )

