from epi.letter_constructible import *
import unittest

class TestLetterConstructible(unittest.TestCase):
    def test_is_letter_constructible(self):
        self.assertEqual(is_letter_constructible(
            "kakaji rampurwale",
            "rampurwale kakaji"
        ), True)
        self.assertEqual(is_letter_constructible(
            "kakajii rampurwale",
            "rampurwale kakaji"
        ), False)
        self.assertEqual(is_letter_constructible(
            "abcd",
            ""
        ), False)
        self.assertEqual(is_letter_constructible(
            "aa aa",
            "aaaaaaa"
        ), False)
