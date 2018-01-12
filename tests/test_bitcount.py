import unittest
from algo_ds.bitcount import count_bits

class TestBitCount(unittest.TestCase):
    def test_count_bits(self):
        self.assertEqual(count_bits(1), 1)
        self.assertEqual(count_bits(2), 1)
        self.assertEqual(count_bits(3), 2)
        self.assertEqual(count_bits(4), 1)
        self.assertEqual(count_bits(7), 3)
        self.assertEqual(count_bits(0), 0)
