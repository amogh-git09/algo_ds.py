import unittest
from algo_ds.deque import Deque

class TestDeque(unittest.TestCase):
    def test_insert_rear(self):
        q = Deque(3)
        q.insert_rear(1)
        q.insert_rear(2)
        q.insert_rear(3)
        self.assertEqual(str(q), "1 2 3")
        self.assertRaises(IndexError, q.insert_rear, 3)

    def test_insert_front(self):
        q = Deque(3)
        q.insert_front(1)
        q.insert_front(2)
        q.insert_front(3)
        self.assertEqual(str(q), "3 2 1")
        self.assertEqual(q.arr[0], 1)
        self.assertEqual(q.arr[2], 2)
        self.assertEqual(q.arr[1], 3)

    def test_delete_front(self):
        q = Deque(3)
        q.insert_rear(1)
        q.insert_rear(2)
        q.insert_front(3)
        self.assertEqual(q.delete_front(), 3)
        self.assertEqual(q.delete_front(), 1)
        self.assertEqual(q.delete_front(), 2)
        self.assertRaises(IndexError, q.delete_front)

    def test_delete_rear(self):
        q = Deque(3)
        q.insert_rear(1)
        q.insert_rear(2)
        q.insert_front(3)
        self.assertEqual(q.delete_rear(), 2)
        self.assertEqual(q.delete_rear(), 1)
        self.assertEqual(q.delete_rear(), 3)
        self.assertRaises(IndexError, q.delete_front)

    def test_get_front(self):
        q = Deque(3)
        q.insert_rear(1)
        q.insert_rear(2)
        q.insert_front(3)
        self.assertEqual(q.get_front(), 3)

    def test_get_rear(self):
        q = Deque(3)
        q.insert_rear(1)
        q.insert_rear(2)
        q.insert_front(3)
        self.assertEqual(q.get_rear(), 2)

    def test_is_empty(self):
        q = Deque(3)
        self.assertEqual(q.is_empty(), True)
        q.insert_rear(1)
        self.assertEqual(q.is_empty(), False)

    def test_is_full(self):
        q = Deque(3)
        self.assertEqual(q.is_full(), False)
        q.insert_rear(1)
        self.assertEqual(q.is_full(), True)
