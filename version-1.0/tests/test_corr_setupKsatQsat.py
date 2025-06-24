
import unittest
import numpy as np

import nucleardatapy as nuda

# energy per particle in SM:
Ksat_sky = [ 239.3441, 241.6726, 241.6857, 241.6553, 230.0156, 230.0252, 230.0084, 217.0589, 
210.7857, 244.224, 240.245, 225.6646, 239.5167, 245.005, 214.651, 355.3754, 237.2519, 240.7237, 
247.7449, 230.8828, 223.3613, 222.3165, 201.0341, 237.3913, 271.0816, 230.1072, 229.9148, 
229.9628, 229.9107, 229.9151, 305.6799, 235.9693, 230.0255, 230.0195, 220.0152 ]

class corrSetupKQTestCase(unittest.TestCase):
	def setUp(self):
		self.kq = nuda.corr.setupKsatQsat( constraint = 'EDF-SKY' )

	def test_kq(self):
		tk_kq = self.kq.Ksat
		print(tk_kq[2], Ksat_sky[2] )
		self.assertEqual(tk_kq[2], Ksat_sky[2] )

if __name__ == '__main__':
	unittest.main()

