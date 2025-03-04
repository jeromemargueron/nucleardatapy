
import unittest
import numpy as np

import nucleardatapy as nuda

# energy per particle in SM:
Ksat_sky = [ -1.676, -2.585, -3.402, -4.647, -6.265, -8.292, -10.6, -13.6, -15.3, -16., -15.32, -14.13, -12.28, -10.14, -7.546, -2.501, 3.464, 14.8,
30.55, 49.74, 110.2, 218.5, 439.9, 786.7 ]

class SetupMicroTestCase(unittest.TestCase):
	def setUp(self):
		self.kq = nuda.corr.setupKsatQsat( constraint = '2024-DFT-SKY' )
	def test_kq(self):
		sky_kq = self.kq.Ksat
		self.assertEqual(sky_kq[2], Ksat_sky[2] )

if __name__ == '__main__':
	unittest.main()

