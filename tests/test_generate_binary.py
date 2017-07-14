from algo_ds.generate_binary import *
import unittest

class TestToBinary(unittest.TestCase):
    def test_to_binary(self):
        self.assertEqual(to_binary(5), "101")
        self.assertEqual(to_binary(0), "0")
        self.assertEqual(to_binary(34), "100010")

    def test_add_one(self):
        self.assertEqual(add_one([0]), [1])
        self.assertEqual(add_one([1]), [1, 0])
        self.assertEqual(add_one([1, 1, 1]), [1, 0, 0, 0])

    def test_print_binaries(self):
        self.assertEqual(print_binaries(0), "[0]")
        self.assertEqual(print_binaries(1), ", [1]")
        self.assertEqual(print_binaries(2), ", [1], [1, 0]")
        self.assertEqual(print_binaries(3), ", [1], [1, 0], [1, 1]")
        self.assertEqual(print_binaries(4), ", [1], [1, 0], [1, 1], [1, 0, 0]")

    def test_get_binaries(self):
        self.assertEqual(get_binaries(0), ["0"])
        self.assertEqual(get_binaries(1), ["1"])
        self.assertEqual(get_binaries(2), ["1", "10"])
        self.assertEqual(get_binaries(3), ["1", "10", "11"])
        self.assertEqual(get_binaries(8), ["1", "10", "11", "100", "101", "110", "111", "1000"])
        self.assertEqual(get_binaries(7), ["1", "10", "11", "100", "101", "110", "111"])
