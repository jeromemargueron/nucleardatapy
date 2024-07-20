Usage
=====

.. _installation:

Installation
------------

To use nucleardatapy, first download the .zip file from the git repository, or clone it in your local computer:

.. code-block:: console

   $ git clone https://github.com/jeromemargueron/nucleardatapy

If you have downloaded the .zip file, you can unzip it anywhere in your local computer:

.. code-block:: console

   $ unzip nucleardatapy.zip

Then, in all cases, you shall enter into the new folder `/nucleardatapy`:

.. code-block:: console

   $ cd nucleardatapy

and launch the install script:

.. code-block:: console

   $ bash install.sh

This will copy the Python toolkit into $HOME/mylib/ as well as a few samples. It will also give you the content of the global variable NUCLEARDATAPY_TK. If you edit install.sh, you can change the version (by default it is set to the latest one) as well as the destination folder (by default it is $HOME/mylib).

Finally, you will have to create the global variable NUCLEARDATAPY_TK with its right content. If you do not want to create it each time you open a new terminal, then you can define it in your .profile or .zprofil or .bash file as:

.. code-block:: console

   export NUCLEARDATAPY_TK=$HOME/mylib/nucleardatapy

.. note::

   The exact path to write above is given at the end of the installation.

.. _Use:

Use nucleardatapy
-----------------

Go to the folder `mylib/nucleardatapy/samples/nucleardatapy_samples/` and try that:

.. code-block:: console

   $ python3 sample_SetupMicroMatter.py

.. _Test:

Test nucleardatapy
------------------

A set of tests can be easily performed. They are stored in tests/ folder.

.. code-block:: console

   $ bash run_tests.sh

.. _Get started:

Get started
-----------

How to obtain microscopic results for APR equation of state:

.. code-block:: python

   import os
   nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
   sys.path.insert(0, nucleardatapy_tk)

   import nucleardatapy as nuda

   mic = nuda.SetupMicroMatter( model = '1998-VAR-AM-APR' )

   mic.print_outputs( )
