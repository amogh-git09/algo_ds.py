from epi.anagram import *
import unittest

class TestAnagram(unittest.TestCase):
    def test_find_anagrams(self):
        result = find_anagrams(['elvis', 'levis', 'money', 'listen', 'silent',
            'algorithm', 'logarithm', 'debitcard', 'badcredit'])
        expected = [['elvis', 'levis'], ['listen', 'silent'],
            ['algorithm', 'logarithm'], ['debitcard', 'badcredit']]
        self.assertListEqual(sorted(result), sorted(expected))
