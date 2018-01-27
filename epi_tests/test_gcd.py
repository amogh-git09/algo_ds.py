from epi.gcd import *
import unittest

class TestGcd(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(gcd(80, 15), 5)
        self.assertEqual(gcd(15, 80), 5)

        self.assertEqual(gcd(80, 80), 80)
        self.assertEqual(gcd(80, 80), 80)
