from algo_ds.mergesort import sort
import unittest

class TestMergeSort(unittest.TestCase):
    def testMergeSort(self):
        self.check([5,2,4,2,1,4,5])
        self.check([0,1,3,-1])
        self.check([])

    def check(self, A):
        B = [x for x in A]
        sort(A)
        self.assertListEqual(A, sorted(B))
