
import unittest
import math
import numpy as np

import os
import sys

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

sly5_den = [0.01099999982398003, 0.02099999960046262, 0.0309999993769452]
sly5_e2a = np.array([-1.96707605066046, -4.04540366344016, -5.91626890362765]) 

class SetupMicroTestCase(unittest.TestCase):
	def setUp(self):
		self.mic = nuda.eos.Micro( model = '1998-VAR-AM-APR')
	def test_apr_den(self):
		den = self.mic.sm_den
		self.assertEqual(den[2], sly5_den[2])
	def test_apr_sm_e2a(self):
		sm_e2a = self.mic.sm_e2a
		self.assertEqual(sm_e2a[2], sly5_e2a[2] )


if __name__ == '__main__':
	unittest.main()


