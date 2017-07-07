import unittest
from algo_ds.stack import Stack

class TestStack(unittest.TestCase):
    def test_push_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        self.assertEqual(str(stack), "4 -> 3 -> 2 -> 1 -> None")

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
        self.assertEqual(str(Stack.reverse(stack)), "1 -> 2 -> 3 -> 4 -> None")

    def test_merge(self):
        s1 = Stack()
        s1.push(1)
        s1.push(3)
        s1.push(5)
        s1.push(7)
        s2 = Stack()
        s2.push(2)
        s2.push(4)
        self.assertEqual(str(Stack.merge(s1, s2)), "7 -> 5 -> 4 -> 3 -> 2 -> 1 -> None")

    def test_split(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(4)
        s.push(5)
        s1, s2 = s.split()
        self.assertEqual(str(s1), "2 -> 1 -> None")
        self.assertEqual(str(s2), "3 -> 4 -> 5 -> None")

    def test_merge_sort(self):
        s = Stack()
        s.push(3)
        s.push(1)
        s.push(5)
        s.push(2)
        s.push(4)
        self.assertEqual(str(Stack.merge_sort(s)), "5 -> 4 -> 3 -> 2 -> 1 -> None")

if __name__ == '__main__':
    unittest.main()
