from epi.sorted_intersection import *
import unittest

class TestSortedIntersection(unittest.TestCase):
    def test_sorted_intersection(self):
        self.assertListEqual(sorted_intersection(
            [1,1,2,4,5,6,7,7,10,15,15],
            [2,2,5,6,7,9,12,13,15,15,15,15,20,25]
        ), [2,5,6,7,15])
