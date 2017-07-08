import unittest
from algo_ds.queue_arr import Queue

class TestQueue(unittest.TestCase):
    def test_enqueue(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(5)
        self.assertEqual(str(q), "1 2 3 4 5")
        self.assertRaises(IndexError, q.enqueue, 6)

    def test_dequeue(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)
        self.assertRaises(IndexError, q.dequeue)

        q.enqueue(4)
        q.enqueue(5)
        q.enqueue(6)
        q.enqueue(7)
        q.enqueue(8)
        self.assertEqual(str(q), "4 5 6 7 8")
        q.dequeue()
        q.dequeue()
        q.dequeue()
        self.assertEqual(str(q), "7 8")
        q.enqueue(9)
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(str(q), "7 8 9 1 2")
        self.assertRaises(IndexError, q.enqueue, 3)

if __name__ == '__main__':
    unittest.main()
