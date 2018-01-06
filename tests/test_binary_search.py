from algo_ds.binary_search import search
import unittest

class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        self.check([1,3,5,7,8], 3, 1)
        self.check([1,3,5,7,8], 1, 0)
        self.check([1,3,5,7,8], 7, 3)
        self.check([1,3,5,7,8], 4, -1)
        self.check([1,3,5,7,8], 0, -1)
        self.check([], 6, -1)

    def check(self, A, x, res):
        self.assertEqual(search(A, x), res)
