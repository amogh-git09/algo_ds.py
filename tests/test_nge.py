from algo_ds.next_great_element import nge
import unittest

class TestNge(unittest.TestCase):
    def test_nge(self):
        self.assertEqual(nge([1,2,3,4]), [2,3,4,-1])
        self.assertEqual(nge([3,5,2,8,21,5]), [5,8,8,21,-1,-1])
        self.assertEqual(nge([4,3,2,1]), [-1,-1,-1,-1])
