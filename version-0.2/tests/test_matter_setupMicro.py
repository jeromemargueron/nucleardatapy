import unittest
import numpy as np

import nucleardatapy as nuda

# energy per particle in SM:
e2a = [
    -1.676,
    -2.585,
    -3.402,
    -4.647,
    -6.265,
    -8.292,
    -10.6,
    -13.6,
    -15.3,
    -16.0,
    -15.32,
    -14.13,
    -12.28,
    -10.14,
    -7.546,
    -2.501,
    3.464,
    14.8,
    30.55,
    49.74,
    110.2,
    218.5,
    439.9,
    786.7,
]


class SetupMicroTestCase(unittest.TestCase):
    def setUp(self):
        self.micro = nuda.matter.setupMicro(model="1981-VAR-AM-FP")
        # self.micro.print_outputs()

    def test_e2a(self):
        tk_e2a = self.micro.sm_e2a
        tk_e2a_int = self.micro.sm_e2a_int
        self.assertEqual(tk_e2a_int[2], e2a[2])


if __name__ == "__main__":
    unittest.main()
