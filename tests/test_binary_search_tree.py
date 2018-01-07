from algo_ds.binary_search_tree import BinarySearchTree
from algo_ds.binary_search_node import *
import unittest

class TestBinarySearchTree(unittest.TestCase):
    def test_insertion(self):
        t = BinarySearchTree()
        nodes = [TreeNode(x) for x in [5, 1, 7, 4]]
        [t.insert_node(node) for node in nodes]

        self.assertEqual(t.root, nodes[0])
        self.assertEqual(t.root.left, nodes[1])
        self.assertEqual(t.root.right, nodes[2])
        self.assertEqual(t.root.left.right, nodes[3])

        self.check_parent_child(nodes[0], nodes[1], True)
        self.check_parent_child(nodes[0], nodes[2], False)
        self.check_parent_child(nodes[1], nodes[3], False)

    def get_test_tree(self):
        t = BinarySearchTree()
        nodes = [TreeNode(x) for x in [8,1,4,6,2,3,7,5]]
        [t.insert_node(node) for node in nodes]
        return t

    def test_deletion(self):
        t = BinarySearchTree()
        nodes = [TreeNode(x) for x in [8,1,4,6,2,3,7,5]]
        [t.insert_node(node) for node in nodes]

        self.assertEqual(t.root.left.right.left.right.key, 3)
        t.delete(nodes[5])
        self.assertEqual(t.root.left.right.left.right, None)

        self.assertEqual(t.root.key, 8)
        t.delete(nodes[0])
        self.assertEqual(t.root.key, 1)

        self.assertEqual(t.root.right.key, 4)
        t.delete(nodes[2])
        self.assertEqual(t.root.right.key, 5)
        self.assertEqual(t.root.right.left.key, 2)
        self.assertEqual(t.root.right.right.key, 6)

        self.assertEqual(t.root.right.key, 5)
        t.delete(nodes[7])
        self.assertEqual(t.root.right.key, 6)
        self.assertEqual(t.root.right.left.key, 2)
        self.assertEqual(t.root.right.right.key, 7)

    def test_inorder_walk(self):
        t = self.get_test_tree()
        # inorder_tree_walk(nodes[0])
        # inorder_tree_walk_iter(nodes[0])

    def test_search(self):
        t = self.get_test_tree()
        self.assertEqual(search(t.root, 4).key, 4)
        self.assertEqual(search(t.root, 123), None)
        self.assertEqual(search(t.root, 5).key, 5)

        self.assertEqual(search_iter(t.root, 4).key, 4)
        self.assertEqual(search_iter(t.root, 123), None)
        self.assertEqual(search_iter(t.root, 5).key, 5)

    def test_minimum(self):
        t = self.get_test_tree()
        self.assertEqual(minimum(t.root).key, 1)
        self.assertEqual(minimum(t.root.left).key, 1)

    def test_maximum(self):
        t = self.get_test_tree()
        self.assertEqual(maximum(t.root).key, 8)
        self.assertEqual(maximum(t.root.left).key, 7)

    def test_succ(self):
        t = self.get_test_tree()
        self.assertEqual(succ(t.root), None)
        self.assertEqual(succ(t.root.left).key, 2)

    def test_pred(self):
        t = self.get_test_tree()
        self.assertEqual(pred(t.root).key, 7)
        self.assertEqual(pred(t.root.left), None)

    def check_parent_child(self, p, c, is_left):
        self.assertEqual(c.parent, p)
        if is_left:
            self.assertEqual(p.left, c)
        else:
            self.assertEqual(p.right, c)
