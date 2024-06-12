import unittest
import math

nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nudy

class SetupMicroTestCase(unittest.TestCase):
	def setUp(self):
		self.mic = nudy.SetupMicro( model = '1998-VAR-AM-APR')
	def test_apr_den(self):
		den = self.mic.den
		self.assertEqual(den, [0.04, 0.08, 0.12, 0.16, 0.20, 0.24, 0.32, 0.40, 0.48, 0.56, 0.64, 0.80, 0.96])
	def test_apr_sm_e2a(self):
		sm_e2a = self.mic.sm_e2a
		self.assertEqual(sm_e2a, [-6.48, -12.13, -15.04, -16.00, -15.09, -12.88, -5.03, 2.12, 15.46, 34.39, 58.35, 121.25, 204.02])


if __name__ == '__main__':
	unittest.main()


