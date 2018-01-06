from algo_ds.max_subarray_dnc import *
import unittest

class TestMaxSubarray(unittest.TestCase):
    def test_recursive(self):
        arr = [6,-2,4,-8,9,-5]
        self.assertEqual(find_max_subarray(arr, 0, len(arr)-1), (4, 4, 9))
