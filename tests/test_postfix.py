from algo_ds.postfix import convert_to_postfix
import unittest

class TestPostfix(unittest.TestCase):
    def test_convert_to_postfix(self):
        self.assertEqual(convert_to_postfix("1+2"), "12+")
        self.assertEqual(convert_to_postfix("3*4+2*8*6+5"), "34*28*6*+5+")
        self.assertEqual(convert_to_postfix("(1+2)*3*4*(5-6)"), "12+3*4*56-*")
