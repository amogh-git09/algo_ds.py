from epi.incr_integer import *
import unittest

class TestIncrInteger(unittest.TestCase):
    def test_incr(self):
        self.assertListEqual(incr([1,2,3]), [1,2,4])
        self.assertListEqual(incr([1,2,9]), [1,3,0])
        self.assertListEqual(incr([9,9,9]), [1,0,0,0])

    def test_add_bits(self):
        self.assertListEqual(add_bits([1,1,1], [1,1]), [1,0,1,0])
        self.assertListEqual(add_bits([0,0,1], [1]), [0,1,0])
