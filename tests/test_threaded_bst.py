from algo_ds.threaded_bst import BinarySearchTree
from algo_ds.threaded_node import Node
import unittest

class TestBinarySearchTree(unittest.TestCase):
    def test_insert(self):
        tree = BinarySearchTree()
        tree.insert(40, 1)
        self.assertEqual(tree.root.key, 40)
        tree.insert(20, 2)
        self.assertEqual(tree.root.left.left_is_thread, False)
        self.assertEqual(tree.root.left.right_is_thread, True)
        self.assertEqual(tree.root.left.right, tree.root)
        tree.insert(60, 3)
        self.assertEqual(tree.root.right.right_is_thread, False)
        self.assertEqual(tree.root.right.left_is_thread, True)
        self.assertEqual(tree.root.right.left, tree.root)
        tree.insert(30, 4)
        self.assertEqual(tree.root.left.right.left, tree.root.left)
        self.assertEqual(tree.root.left.right.right, tree.root)
        self.assertEqual(tree.root.left.right.left_is_thread, True)
        self.assertEqual(tree.root.left.right.right_is_thread, True)
        self.assertEqual(tree.root.left.left_is_thread, False)
        self.assertEqual(tree.root.left.right_is_thread, False)
        tree.insert(50, 5)
        self.assertEqual(tree.root.right.left.key, 50)
        self.assertEqual(tree.root.right.left.left, tree.root)
        self.assertEqual(tree.root.right.left.right, tree.root.right)
        self.assertEqual(tree.root.right.left.left_is_thread, True)
        self.assertEqual(tree.root.right.left.right_is_thread, True)
        self.assertEqual(tree.root.right.left_is_thread, False)
        self.assertEqual(tree.root.right.right_is_thread, False)

    def test_traversal_inorder(self):
        tree = BinarySearchTree()
        tree.insert(40, 1)
        tree.insert(20, 2)
        tree.insert(30, 2)
        tree.insert(60, 2)
        tree.insert(50, 2)
        tree.insert(55, 2)
        tree.insert(57, 2)
        tree.insert(56, 2)
        tree.insert(58, 2)
        result = []
        tree.traversal_inorder(lambda node: result.append(node))
        self.assertEqual([n.key for n in result], [20,30,40,50,55,56,57,58,60])
