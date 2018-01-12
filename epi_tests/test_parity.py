import unittest
from epi.parity import brute, brute_better, parity, quick_mod

class TestParity(unittest.TestCase):
    def test_brute(self):
        self.check(brute)
        self.check(brute_better)
        self.check(parity)

    def check(self, fun):
        self.assertEqual(fun(7), 1)
        self.assertEqual(fun(2), 1)
        self.assertEqual(fun(3), 0)
        self.assertEqual(fun(1515235), 1)

    def test_quick_mod(self):
        self.assertEqual(quick_mod(11, 4), 3)
        self.assertEqual(quick_mod(11, 2), 1)
        self.assertEqual(quick_mod(11, 8), 3)
        self.assertEqual(quick_mod(11, 16), 11)
        self.assertEqual(quick_mod(30, 8), 6)
