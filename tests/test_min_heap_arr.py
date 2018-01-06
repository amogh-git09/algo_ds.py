import unittest
from algo_ds.min_heap_arr import *

class TestSortAlmostSorted(unittest.TestCase):
    def test_sort_almost_sorted(self):
        arr = [3,1,4,2,6,5]
        arr = sort_almost_sorted(arr, 2)
        self.assertEqual(arr, [1,2,3,4,5,6])
