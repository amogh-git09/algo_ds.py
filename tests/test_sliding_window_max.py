from algo_ds.sliding_window_max import *
import unittest

class TestSlidingWindowMax(unittest.TestCase):
    def test_sliding_window_max(self):
        arr = [2,1,4,5,3,1,3,4]
        self.assertEqual(sliding_window_max(arr,3), "4 5 5 5 3 4")
        arr = [2,1,4,5,3,1,3,4]
        self.assertEqual(sliding_window_max(arr,4), "5 5 5 5 4")
        arr = [2,1,4,5,3,1,3,4]
        self.assertEqual(sliding_window_max(arr,2), "2 4 5 5 3 3 4")
        arr = [2,1,4,5,3,1,3,4]
        self.assertEqual(sliding_window_max(arr,1), "2 1 4 5 3 1 3 4")
        arr = []
        self.assertRaises(ValueError, sliding_window_max, arr, 1)
        arr = []
        self.assertEqual(sliding_window_max(arr,0), "")
