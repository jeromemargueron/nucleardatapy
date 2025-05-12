.. nucleardatapy documentation master file, created by
   sphinx-quickstart on Wed Jun 12 20:05:31 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Welcome to nucleardatapy's documentation!
=========================================

**nucleardatapy** (/in short nuda/) is a Python library for nuclear physicists facilitating the access to theoretical or experimental nuclear data. It is specificaly designed for equation of state practitionners interested in the modeling of neutron stars, and it offers *simple* and *intuitive* APIs.

All data are provided with their reference, so when using these data in a scientific paper, reference to data should be provided explicitely. The reference to this toolkit could be given, but it should not mask the reference to data.

This python toolkit is designed to provide: 
1) microscopic calculations in nuclear matter, 
2) phenomenological predictions in nuclear matter,
3) experimental data for finite nuclei.

Check out the :doc:`source/usage` section for further information, including how to
:ref:`install <installation>` the project.

.. note::

   This project is under active development.

Contents
--------

.. toctree::

   source/usage
   source/api
   source/miscelaneous

Complement
----------

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   source/api/matter
   source/api/eos
   source/api/nuc
   source/api/crust
   source/api/astro
   source/api/corr
   
Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
