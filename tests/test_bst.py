from algo_ds.bst import BinarySearchTree
import unittest

class TestBinarySearchTree(unittest.TestCase):
    def test_insert(self):
        tree = BinarySearchTree()
        tree.insert(32, 1)
        tree.insert(20, 2)
        tree.insert(38, 3)
        tree.insert(35, 4)
        tree.insert(10, 5)
        self.assertEqual(tree.root.key, 32)
        self.assertEqual(tree.root.left.key, 20)
        self.assertEqual(tree.root.right.key, 38)
        self.assertEqual(tree.root.left.left.key, 10)
        self.assertEqual(tree.root.right.left.key, 35)
