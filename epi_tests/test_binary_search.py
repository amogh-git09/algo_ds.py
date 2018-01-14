from epi.binary_search import *
import unittest

class TestBinarySearch(unittest.TestCase):
    def test_search_student(self):
        students = [Student(s[0], s[1]) for s in [
            ('Babu', 4.0),
            ('Kaka', 4.0),
            ('Bhole', 3.9),
            ('Ramu', 3.8),
            ('Fasori', 3.7),
            ('Birju', 2.0),
            ('Jasmeet', 1.0),
        ]]
        [self.assertEqual(search_student(students, s), True) for s in students]
        self.assertEqual(search_student(students, Student('Amogh', 4.0)), False)

    def test_search_leftmost(self):
        self.assertEqual(search_leftmost([2,2,2,2,2], 2), 0)
        self.assertEqual(search_leftmost([0,2,2,2,2], 0), 0)
        self.assertEqual(search_leftmost([2,2,3,3,3], 3), 2)
        self.assertEqual(search_leftmost([], 2), -1)
        self.assertEqual(search_leftmost([1,2,2,3,3,4,4], 5), -1)
        self.assertEqual(search_leftmost([1,2,2,3,3,4,4], 0), -1)

    def test_bisect_right(self):
        self.assertEqual(bisect_right([2,2,2,2,2], 2), 5)
        self.assertEqual(bisect_right([0,2,2,2,2], 0), 1)
        self.assertEqual(bisect_right([2,2,3,3,3], 3), 5)
        self.assertEqual(bisect_right([], 2), -1)
        self.assertEqual(bisect_right([1,2,2,3,3,4,4], 5), -1)
        self.assertEqual(bisect_right([1,2,2,3,3,4,4], 0), 0)

    def test_local_minimum(self):
        self.assertEqual(local_minimum([4,2,3,4,5]), 1)
        self.assertEqual(local_minimum([1]), 0)
        self.assertEqual(local_minimum([2, 1]), 1)
