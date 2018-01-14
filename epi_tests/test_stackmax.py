from epi.stackmax import StackWithMax, StackWithMax2
import unittest

class TestStackWithMax(unittest.TestCase):
    def test_max(self):
        stack = StackWithMax()
        [stack.push(x) for x in [5,1,3,2,5,6,7,3,8,9,5,1]]
        self.assertEqual(stack.max(), 9)
        stack.pop()
        self.assertEqual(stack.max(), 9)
        stack.pop()
        stack.pop()
        self.assertEqual(stack.max(), 8)
        stack.pop()
        self.assertEqual(stack.max(), 7)

    def test_push_pop(self):
        stack = StackWithMax()
        ls = [5,1,3,2,5,6,7,3,8,9,5,1]
        [stack.push(x) for x in ls]
        values = []
        while not stack.empty():
            values.append(stack.pop())

        self.assertListEqual(values, ls[::-1])

class TestStackWithMax2(unittest.TestCase):
    def test_max(self):
        stack = StackWithMax2()
        [stack.push(x) for x in [5,1,3,2,5,6,7,3,8,9,5,1]]
        self.assertEqual(stack.max(), 9)
        stack.pop()
        self.assertEqual(stack.max(), 9)
        stack.pop()
        stack.pop()
        self.assertEqual(stack.max(), 8)
        stack.pop()
        self.assertEqual(stack.max(), 7)

    def test_push_pop(self):
        stack = StackWithMax2()
        ls = [5,1,3,2,5,6,7,3,8,9,5,1]
        [stack.push(x) for x in ls]
        values = []
        while not stack.is_empty():
            values.append(stack.pop())

        self.assertListEqual(values, ls[::-1])
