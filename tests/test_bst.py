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

    def test_traversal_postorder(self):
        tree = BinarySearchTree()
        tree.insert(32, 1)
        tree.insert(20, 2)
        tree.insert(38, 3)
        tree.insert(35, 4)
        tree.insert(10, 5)
        result = []
        tree.traversal_postorder(lambda node: result.append(node))
        self.assertEqual(result[0], tree.root.left.left)
        self.assertEqual(result[1], tree.root.left)
        self.assertEqual(result[2], tree.root.right.left)
        self.assertEqual(result[3], tree.root.right)
        self.assertEqual(result[4], tree.root)

    def test_traversal_preorder(self):
        tree = BinarySearchTree()
        tree.insert(32, 1)
        tree.insert(20, 2)
        tree.insert(38, 3)
        tree.insert(35, 4)
        tree.insert(10, 5)
        result = []
        tree.traversal_preorder(lambda node: result.append(node))
        self.assertEqual(result[0], tree.root)
        self.assertEqual(result[1], tree.root.left)
        self.assertEqual(result[2], tree.root.left.left)
        self.assertEqual(result[3], tree.root.right)
        self.assertEqual(result[4], tree.root.right.left)

    def test_traversal_breadth_first(self):
        tree = BinarySearchTree()
        tree.insert(32, 1)
        tree.insert(20, 2)
        tree.insert(38, 3)
        tree.insert(35, 4)
        tree.insert(10, 5)
        result = []
        tree.traversal_breadth_first(lambda node: result.append(node))
        self.assertEqual(result[0], tree.root)
        self.assertEqual(result[1], tree.root.left)
        self.assertEqual(result[2], tree.root.right)
        self.assertEqual(result[3], tree.root.left.left)
        self.assertEqual(result[4], tree.root.right.left)

    def test_height(self):
        tree = BinarySearchTree()
        tree.insert(32, 1)
        tree.insert(20, 2)
        tree.insert(38, 3)
        tree.insert(35, 4)
        tree.insert(10, 5)
        self.assertEqual(tree.height(), 2)

        tree = BinarySearchTree()
        tree.insert(32, 1)
        tree.insert(31, 2)
        tree.insert(30, 3)
        tree.insert(29, 4)
        tree.insert(28, 5)
        self.assertEqual(tree.height(), 4)

        tree = BinarySearchTree()
        tree.insert(1, 1)
        self.assertEqual(tree.height(), 0)

        tree = BinarySearchTree()
        self.assertEqual(tree.height(), -1)


    def test_search(self):
        tree = BinarySearchTree()
        tree.insert(32, 1)
        tree.insert(20, 2)
        tree.insert(38, 3)
        tree.insert(35, 4)
        tree.insert(10, 5)
        self.assertEqual(tree.search(38).val, 3)
        self.assertEqual(tree.search(200), None)

    def test_minimum(self):
        tree = BinarySearchTree()
        tree.insert(32, 1)
        tree.insert(20, 2)
        tree.insert(38, 3)
        tree.insert(35, 4)
        tree.insert(10, 5)
        self.assertEqual(tree.minimum().val, 5)

    def test_maximum(self):
        tree = BinarySearchTree()
        tree.insert(32, 1)
        tree.insert(20, 2)
        tree.insert(38, 3)
        tree.insert(35, 4)
        tree.insert(10, 5)
        self.assertEqual(tree.maximum().val, 3)
