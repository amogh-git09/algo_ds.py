import unittest
from algo_ds.queue import Queue

class TestQueue(unittest.TestCase):
    def test_enqueue(self):
        q = Queue()
        q.enqueue(1)
        self.assertEqual(str(q), "1 -> None")

        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(5)
        self.assertEqual(str(q), "1 -> 2 -> 3 -> 4 -> 5 -> None")

    def test_dequeue(self):
        q = Queue()
        q.enqueue(1)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), None)
        self.assertEqual(q.dequeue(), None)
