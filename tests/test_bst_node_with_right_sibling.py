from algo_ds.bst_node_with_right_sibling import Node
import unittest

class TestBstNodeWithRightSibling(unittest.TestCase):
    def test_connect_right_siblings(self):
        node50 = Node(50)
        node30 = Node(30)
        node60 = Node(60)
        node62 = Node(62)
        node55 = Node(55)
        node70 = Node(70)
        node22 = Node(22)
        node80 = Node(80)
        node94 = Node(94)
        node38 = Node(38)

        node50.left = node30
        node50.right = node60
        node30.left = node62
        node60.left = node55
        node60.right = node70
        node62.right = node22
        node55.left = node80
        node55.right = node94
        node70.right = node38

        node50.connect_siblings()
        self.assertEqual(node50.right_sibling, None)
        self.assertEqual(node30.right_sibling, node60)
        self.assertEqual(node60.right_sibling, None)
        self.assertEqual(node62.right_sibling, node55)
        self.assertEqual(node55.right_sibling, node70)
        self.assertEqual(node70.right_sibling, None)
        self.assertEqual(node22.right_sibling, node80)
        self.assertEqual(node80.right_sibling, node94)
        self.assertEqual(node94.right_sibling, node38)
        self.assertEqual(node38.right_sibling, None)
