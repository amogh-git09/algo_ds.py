import unittest
from algo_ds.bst_node import Node

class TestBSTNode(unittest.TestCase):
    def test_insert(self):
        node1 = Node(32,1)
        node2 = Node(20,2)
        node3 = Node(38,3)
        node1.insert(node2)
        self.assertEqual(node1.left, node2)
        self.assertEqual(node1.right, None)
        node1.insert(node3)
        self.assertEqual(node1.left, node2)
        self.assertEqual(node1.right, node3)
        node4 = Node(35, 4)
        node1.insert(node4)
        self.assertEqual(node1.right.left, node4)
