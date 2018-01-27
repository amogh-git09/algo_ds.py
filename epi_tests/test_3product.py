from epi.product3 import *
import unittest

class TestProduct3(unittest.TestCase):
    def test_product3(self):
        for target in range(30):
            print(productk([5,10,20,2,3,6,8], target, 4))
