from epi.str_int import *
import unittest

class TestStrInt(unittest.TestCase):
    def test_str2int(self):
        self.assertEqual(str2int('321'), 321)
        self.assertEqual(str2int('-321'), -321)
        self.assertRaises(ValueError, str2int, '10a002')

    def test_int2str(self):
        self.assertEqual(int2str(321), '321')
        self.assertEqual(int2str(-321), '-321')
        self.assertEqual(int2str(0), '0')
        self.assertEqual(int2str(1), '1')
