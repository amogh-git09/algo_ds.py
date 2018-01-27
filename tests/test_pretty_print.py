from algo_ds.pretty_print import *
import unittest

class TestPrettyPrint(unittest.TestCase):
    def test_pretty_print(self):
        para = "It starts with one thing i do not know why it does not even matter how hard you try keep that in mind i designed this rhyme to explain in due time all i know time is a valuable thing watch it fly by as the pendulum swings watch it count down till the end of the day the clock ticks life away."
        words = para.split()
        pretty_print(words, 40)
