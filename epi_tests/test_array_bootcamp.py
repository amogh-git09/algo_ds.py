from epi.array_bootcamp import *
import unittest

class TestArrayBootcamp(unittest.TestCase):
    def test_separate_even_odd(self):
        self.assertListEqual(separate_even_odd([1,2,3,4]), [4,2,3,1])
        self.assertListEqual(separate_even_odd([]), [])
        self.assertListEqual(separate_even_odd([1,1,1,1]), [1,1,1,1])
        self.assertListEqual(separate_even_odd([2,2,2,2]), [2,2,2,2])

    def test_separate_true_false(self):
        self.assertListEqual(separate_true_false([True, False, False, True]), [False, False, True, True])

    def test_sep_true_false(self):
        self.assertListEqual(sep_true_false([True, False, False, True]), [False, False, True, True])
