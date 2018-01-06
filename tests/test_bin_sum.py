from algo_ds.bin_sum import add
import unittest

class TestBinSum(unittest.TestCase):
    def test_add(self):
        self.check([1,0,1], [0,0,1], [0,1,1,0])
        self.check([1,1,1], [0,0,0], [0,1,1,1])
        self.check([1,1,1], [1,1,1], [1,1,1,0])
        self.check([0,0,0], [0,0,0], [0,0,0,0])

    def check(self, A, B, C):
        res = add(A, B)
        self.assertListEqual(res, C)
