import unittest
from algo_ds.doubly_linked_stack import DStack

class TestDoublyLinkedStack(unittest.TestCase):
    def test_push_pop(self):
        stack = DStack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertRaises(IndexError, stack.pop)

    def test_find_middle(self):
        stack = DStack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.find_middle(), 2)
        self.assertEqual(stack.find_middle(), 2)

    def test_delete_middle(self):
        stack = DStack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.delete_middle(), 2)
        self.assertEqual(stack.delete_middle(), 1)
        self.assertEqual(stack.delete_middle(), 3)
