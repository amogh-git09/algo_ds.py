from epi.quicksort import *
import unittest

class TestQuicksort(unittest.TestCase):
    def test_partition(self):
        A = [2,1,3,2,1,1,2,3,2]
        q, t = partition(A, 0, len(A)-1, len(A)-1)
        self.assertListEqual(A[0:q+1], [1]*3)
        self.assertListEqual(A[q+1:t+1], [2]*4)

    def test_quicksort(self):
        A = [1,2,4,3,1,2,3,4,4,3,2,1,2,3,4]
        sort(A)
        print(A)
