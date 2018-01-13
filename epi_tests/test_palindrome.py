from epi.palindrome import *
import unittest

class TestPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertEqual(is_palindrome("jahaj"), True)
        self.assertEqual(is_palindrome(""), True)
        self.assertEqual(is_palindrome("a"), True)
        self.assertEqual(is_palindrome("abcd"), False)
        self.assertEqual(is_palindrome("Dad"), True)
