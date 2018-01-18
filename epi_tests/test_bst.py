from epi.bst import *
import unittest

class TestBST(unittest.TestCase):
    def test_is_bst(self):
        self.assertEqual(is_bst(self.get_valid_bst()), True)
        self.assertEqual(is_bst(self.get_invalid_bst()), False)

        self.assertEqual(is_bst2(self.get_valid_bst()), True)
        self.assertEqual(is_bst2(self.get_invalid_bst()), False)

        self.assertEqual(is_bst3(self.get_valid_bst()), True)
        self.assertEqual(is_bst3(self.get_invalid_bst()), False)

        self.assertEqual(is_bst4(self.get_valid_bst()), True)
        self.assertEqual(is_bst4(self.get_invalid_bst()), False)

    def get_invalid_bst(self):
        """
              3
            /   \
           1     5
          / \
         0   4
        """
        nodes = [TreeNode(i) for i in range(6)]
        nodes[3].left = nodes[1]
        nodes[3].right = nodes[5]
        nodes[1].left = nodes[0]
        nodes[1].right = nodes[4]
        return nodes[3]

    def get_valid_bst(self):
        """
              3
            /   \
           2     5
          /     /
         0     4
          \
           1
        """
        nodes = [TreeNode(i) for i in range(6)]
        nodes[3].left = nodes[2]
        nodes[3].right = nodes[5]
        nodes[2].left = nodes[0]
        nodes[0].right = nodes[1]
        nodes[5].left = nodes[4]
        return nodes[3]
