
import unittest
import numpy as np
import nucleardatapy as nuda

# energy per particle in SM:
mass = 1.97

class astroSetupMassesTestCase(unittest.TestCase):
	def setUp(self):
		self.m = nuda.astro.setupMasses( source = 'J1614–2230', obs = 1 )
	def test_m(self):
		tk_mass = self.m.mass
		self.assertEqual(tk_mass, mass )

if __name__ == '__main__':
	unittest.main()

