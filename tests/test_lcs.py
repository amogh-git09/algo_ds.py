from algo_ds.lcs import *
import unittest

class TestLcs(unittest.TestCase):
    def test_lcs(self):
        X, Y = "character", "retcarahc"
        c, b = lcs_length(X, Y)
        print_lcs(b, X, Y)
