import unittest
from algo_ds.stack import Stack

class TestStack(unittest.TestCase):
    def test_push_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)

        self.assertEqual(stack.pop(), 4)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)

    def test_reverse(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack = stack.reverse()
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 4)

    def test_merge(self):
        s1 = Stack()
        s1.push(1)
        s1.push(3)
        s1.push(5)
        s1.push(7)
        s2 = Stack()
        s2.push(2)
        s2.push(4)
        merged = Stack.merge(s1, s2)
        self.assertEqual(merged.pop(), 7)
        self.assertEqual(merged.pop(), 5)
        self.assertEqual(merged.pop(), 4)
        self.assertEqual(merged.pop(), 3)
        self.assertEqual(merged.pop(), 2)
        self.assertEqual(merged.pop(), 1)

    def test_split(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(4)
        s.push(5)
        s1, s2 = s.split()
        self.assertEqual(s1.pop(), 2)
        self.assertEqual(s1.pop(), 1)
        self.assertEqual(s2.pop(), 3)
        self.assertEqual(s2.pop(), 4)
        self.assertEqual(s2.pop(), 5)

    def test_merge_sort(self):
        s = Stack()
        s.push(3)
        s.push(1)
        s.push(5)
        s.push(2)
        s.push(4)
        s = Stack.merge_sort(s)
        self.assertEqual(s.pop(), 5)
        self.assertEqual(s.pop(), 4)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)

    def test_sort(self):
        s = Stack()
        s.push(3)
        s.push(1)
        s.push(5)
        s.push(2)
        s.push(4)
        s.sort()
        self.assertEqual(s.pop(), 5)
        self.assertEqual(s.pop(), 4)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)

        s = Stack()
        s.push(1)
        s.sort()
        self.assertEqual(s.pop(), 1)

        s = Stack()
        s.sort()
        self.assertRaises(IndexError, s.pop)

    def test_get_min(self):
        s = Stack()
        s.push(3)
        s.push(1)
        s.push(5)
        s.push(2)
        s.push(4)
        self.assertEqual(s.get_min(), 1)

        s = Stack()
        self.assertEqual(s.get_min(), None)

if __name__ == '__main__':
    unittest.main()
