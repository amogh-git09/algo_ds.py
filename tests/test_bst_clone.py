from algo_ds.bst_clone import Node
import unittest

class TestClone(unittest.TestCase):
    def test_clone(self):
        node60 = Node(60, 1)
        node30 = Node(30, 2)
        node40 = Node(40, 3)
        node35 = Node(35, 4)
        node45 = Node(45, 5)
        node80 = Node(80, 6)
        node70 = Node(70, 7)
        node75 = Node(75, 8)

        node60.left = node30
        node30.right = node40
        node40.left = node35
        node40.right = node45
        node60.right = node80
        node80.left = node70
        node70.right = node75

        node60.random = node40
        node30.random = node70
        node35.random = node45
        node45.random = node70
        node80.random = node75

        clone = Node.clone(node60)
        self.assertEqual(clone.key, 60)
        self.assertEqual(clone.left.key, 30)
        self.assertEqual(clone.right.key, 80)
        self.assertEqual(clone.random.key, 40)
        self.assertEqual(clone.left.left, None)
        self.assertEqual(clone.left.right.key, 40)
        self.assertEqual(clone.left.random.key, 70)
        self.assertEqual(clone.left.right.left.key, 35)
        self.assertEqual(clone.left.right.right.key, 45)
        self.assertEqual(clone.left.right.left.random.key, 45)
        self.assertEqual(clone.right.key, 80)
        self.assertEqual(clone.right.left.key, 70)
        self.assertEqual(clone.right.right, None)
        self.assertEqual(clone.right.random.key, 75)
