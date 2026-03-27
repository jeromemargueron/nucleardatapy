
import unittest
import numpy as np

import nucleardatapy as nuda

den = np.array( [ 0.01, 0.02, 0.03 ] )
e2a = np.array( [ 942.39275041, 944.42634541, 946.1280241 ] )
delta = np.zeros( den.size )

class SetupFFGTestCase(unittest.TestCase):
	def setUp(self):
		self.ffg = nuda.matter.setupFFGNuc( den = den, delta = delta, ms = 1.0 )
	def test_e2a(self):
		tk_e2a = self.ffg.e2a
		self.assertAlmostEqual(tk_e2a[2], e2a[2] )

if __name__ == '__main__':
	unittest.main()


