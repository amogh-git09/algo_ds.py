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

    def test_traversal_inorder(self):
        tree = BinarySearchTree()
        tree.insert(32, 1)
        tree.insert(20, 2)
        tree.insert(38, 3)
        tree.insert(35, 4)
        tree.insert(10, 5)
        result = []
        tree.traversal_inorder(lambda node: result.append(node))
        self.assertEqual(result[0], tree.root.left.left)
        self.assertEqual(result[1], tree.root.left)
        self.assertEqual(result[2], tree.root)
        self.assertEqual(result[3], tree.root.right.left)
        self.assertEqual(result[4], tree.root.right)

    def test_traversal_preorder(self):
        tree = BinarySearchTree()
        tree.insert(32, 1)
        tree.insert(20, 2)
        tree.insert(38, 3)
        tree.insert(35, 4)
        tree.insert(10, 5)
        result = []
        tree.traversal_preorder(lambda node: result.append(node))
        self.assertEqual(result[0], tree.root.left.left)
        self.assertEqual(result[1], tree.root.left)
        self.assertEqual(result[2], tree.root.right.left)
        self.assertEqual(result[3], tree.root.right)
        self.assertEqual(result[4], tree.root)
