from algo_ds.bitonic_ts import *
import unittest

class TestBitonicTravellingSalesman(unittest.TestCase):
    def test_bitonic_ts(self):
        d = [[ 0, 4, 7, 6,10, 9,15],
             [ 4, 0, 3, 5, 6, 7,10],
             [ 7, 3, 0, 4, 3, 5, 6],
             [ 6, 5, 4, 0, 6, 4, 8],
             [10, 6, 3, 6, 0, 3, 3],
             [ 9, 7, 5, 4, 3, 0, 2],
             [15,10, 6, 8, 3, 2, 0]]

        c, b = bitonic_travelling_salesman(d)
        n = len(d)-1
        print(c[n] + d[n-1][n])
        print_path(b)
