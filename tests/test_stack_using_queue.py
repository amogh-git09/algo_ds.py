import unittest
from algo_ds.stack_using_queue import Stack

class TestStackUsingQueue(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(str(stack), "1 -> 2 -> 3 -> None")

    def test_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.pop(), None)

    def test_pop_iter(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.pop_iter(), 3)
        self.assertEqual(stack.pop_iter(), 2)
        self.assertEqual(stack.pop_iter(), 1)
        self.assertEqual(stack.pop_iter(), None)
