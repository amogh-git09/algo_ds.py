from epi.max_subarray import *
import unittest

class TestMaxSubarray(unittest.TestCase):
    def test_max_subarray(self):
        self.assertEqual(max_subarray([-6,-7,-2,10]), 10)
        self.assertEqual(max_subarray([3,-1,2,4,-5,6]), 9)
        self.assertEqual(max_subarray([-3,-4,-2,-1,-5]), 0)
