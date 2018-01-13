from epi.max_profit import *
import unittest

class TestMaxProfit(unittest.TestCase):
    def test_max_profit(self):
        self.assertEqual(max_profit([3,2,1,4]), 3)
        self.assertEqual(max_profit([3,2,1]), 0)

    def test_max_subarray_len(self):
        self.assertEqual(max_subarray_len([1,1,1,2,2,3,3,3,3,3]), 5)
