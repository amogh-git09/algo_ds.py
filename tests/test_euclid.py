import unittest
from algo_ds.euclid import *

class TestEuclid(unittest.TestCase):
    def test_euclid(self):
        self.assertEqual(euclid(10, 7), 1)
        self.assertEqual(euclid(10, 5), 5)
        self.assertEqual(euclid(10, 13), 1)
        self.assertEqual(euclid(10, 15), 5)

    def test_extended_euclid(self):
        self.assertEqual(extended_euclid(99, 78), (3, -11, 14))
