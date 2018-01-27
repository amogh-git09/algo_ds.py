from algo_ds.lcs import *
import unittest

class TestLcs(unittest.TestCase):
    def test_lcs(self):
        lcs_length("ABCBDAB", "BDCABA")
