from epi.palindrome import *
import unittest

class TestPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertEqual(is_palindrome("jahaj"), True)
        self.assertEqual(is_palindrome(""), True)
        self.assertEqual(is_palindrome("a"), True)
        self.assertEqual(is_palindrome("abcd"), False)
        self.assertEqual(is_palindrome("Dad"), True)

    def test_can_form_palindrome(self):
        self.assertEqual(can_form_palindrome("amogh"), False)
        self.assertEqual(can_form_palindrome("jahaj"), True)
        self.assertEqual(can_form_palindrome("edified"), True)
