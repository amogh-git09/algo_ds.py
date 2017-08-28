from algo_ds.cormen_bst import *
import unittest

class TestBst(unittest.TestCase):
    def test_insert_delete(self):
        # insertion
        bst = BST()
        node50 = Node(50)
        bst.insert(node50)
        bst.insert(Node(40))
        node20 = Node(20)
        bst.insert(node20)
        node10 = Node(10)
        bst.insert(node10)
        bst.insert(Node(30))
        bst.insert(Node(60))
        res = []
        bst.root.inorder_walk(lambda node: res.append(node.key))
        self.assertEqual(res, [10, 20, 30, 40, 50, 60])
        self.assertEqual(bst.root.left.key, 40)
        self.assertEqual(bst.root.left.left.key, 20)

        # deletion
        bst.delete(node10)
        res = []
        bst.root.inorder_walk(lambda node: res.append(node.key))
        self.assertEqual(res, [20, 30, 40, 50, 60])

        bst.delete(node20)
        res = []
        bst.root.inorder_walk(lambda node: res.append(node.key))
        self.assertEqual(res, [30, 40, 50, 60])

        bst.delete(node50)
        res = []
        bst.root.inorder_walk(lambda node: res.append(node.key))
        self.assertEqual(res, [30, 40, 60])
