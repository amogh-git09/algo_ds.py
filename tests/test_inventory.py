from algo_ds.inventory import *
import unittest

class TestInventory(unittest.TestCase):
    def test_inventory(self):
        d = [8,15,25,4,4,30]
        m = 10
        h = lambda x: x
        c = 2

        r, x, s, cost = plan(d,m,h,c)
        print(["{0:2d}".format(x) for x in r])
        print(["{0:2d}".format(a) for a in x])
        print(["{0:2d}".format(x) for x in s])
        print(["{0:2d}".format(x) for x in d])
        print(["{0:2d}".format(x) for x in cost])
