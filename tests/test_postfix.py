from algo_ds.postfix import convert_to_postfix, evaluate
import unittest

class TestPostfix(unittest.TestCase):
    def test_convert_to_postfix(self):
        self.assertEqual(convert_to_postfix("1+2"), "12+")
        self.assertEqual(convert_to_postfix("3*4+2*8*6+5"), "34*28*6*+5+")
        self.assertEqual(convert_to_postfix("(1+2)*3*4*(5-6)"), "12+3*4*56-*")

    def test_evaluate(self):
        self.assertEqual(evaluate(convert_to_postfix("(1+2)*3*4*(5-6)")), -36)
        self.assertEqual(evaluate(convert_to_postfix("1+2*4/4")), 3)
        self.assertEqual(evaluate(convert_to_postfix("(1+2*3)*3*4*(5*2-6/2)")), 588)
        self.assertEqual(evaluate(convert_to_postfix("")), 0)
        self.assertEqual(evaluate(convert_to_postfix("()")), 0)
