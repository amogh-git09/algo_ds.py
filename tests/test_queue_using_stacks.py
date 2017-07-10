import unittest
from algo_ds.queue_using_stacks import QueueUsingStacks

class TestQueueUsingStack(unittest.TestCase):
    def test_enqueue_dequeue(self):
        s = QueueUsingStacks()
        s.enqueue(1)
        s.enqueue(2)
        s.enqueue(3)
        self.assertEqual(s.dequeue(), 1)
        self.assertEqual(s.dequeue(), 2)
        self.assertEqual(s.dequeue(), 3)
        self.assertRaises(IndexError, s.dequeue)
