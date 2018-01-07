from algo_ds.priority_queue import MaxPriorityQueue
import unittest

class TestMaxPriorityQueue(unittest.TestCase):
    def test_insert(self):
        q = MaxPriorityQueue(10)
        q.insert(3)
        self.assertListEqual(q.arr[0:1], [3])
        q.insert(5)
        self.assertListEqual(q.arr[0:2], [5, 3])
        q.insert(8)
        self.assertListEqual(q.arr[0:3], [8, 3, 5])

    def test_max(self):
        q = MaxPriorityQueue(10)
        [q.insert(x) for x in [6,3,5,2,1,4]]
        self.assertEqual(q.maximum(), 6)

    def test_extract_max(self):
        q = MaxPriorityQueue(10)
        [q.insert(x) for x in [6,3,5,2,1,4]]
        self.assertEqual(q.extract_max(), 6)
        self.assertEqual(q.extract_max(), 5)
        self.assertEqual(q.extract_max(), 4)
        self.assertEqual(q.extract_max(), 3)
        self.assertEqual(q.extract_max(), 2)
        self.assertEqual(q.extract_max(), 1)
