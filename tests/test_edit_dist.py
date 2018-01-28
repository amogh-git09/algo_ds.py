from algo_ds.edit_dist import *
import unittest

class TestEditDist(unittest.TestCase):
    def test_edit_dist(self):
        x, y = "algorithm", "altruistic"
        c = edit_dist(x, y,
                {'cop': 5,
                 'rep': 10,
                 'del': 10,
                 'ins': 10,
                 'twi': 0,
                 'kil': 1})
        print_ops(c, x, y)
