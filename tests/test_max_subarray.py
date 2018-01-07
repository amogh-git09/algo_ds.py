from algo_ds.max_subarray import max_subarray
import unittest

class TestMaxSubarray(unittest.TestCase):
    def test_max_subarray(self):
        self.check([1, 0, -5, 3, 5, 5], (3, 5, 13))
        self.check([10, 1, -5, -4, -2, 1, 8], (0, 1, 11))
        self.check([10, 1, 5, 4, 2, 1, 8], (0, 6, 31))
        self.check([10, 1, -5, 4, 2, 1, 8], (0, 6, 21))
        self.check([4, 1, -5, 4, 2, 1, 8], (3, 6, 15))

    def check(self, A, res):
        self.assertEqual(max_subarray(A), res)
