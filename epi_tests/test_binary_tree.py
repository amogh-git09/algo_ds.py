from epi.binary_tree import *
import unittest

class TestBinaryTree(unittest.TestCase):
    def test_is_balanced(self):
        self.assertEqual(is_balanced(self.get_tree()), True)
        self.assertEqual(is_balanced(self.get_tree2()), False)

    def get_tree(self):
        nodes = [TreeNode(x) for x in range(5)]
        nodes[3].left = nodes[1]
        nodes[1].left = nodes[0]
        nodes[1].right = nodes[2]
        nodes[3].right = nodes[4]
        return nodes[3]

    def get_tree2(self):
        nodes = [TreeNode(x) for x in range(5)]
        nodes[3].left = nodes[1]
        nodes[1].left = nodes[0]
        nodes[1].right = nodes[2]
        nodes[2].right = nodes[4]
        return nodes[3]
