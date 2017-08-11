import unittest
from algo_ds.linked_list_node import Node

class TestNode(unittest.TestCase):
    def test_construct(self):
        node = Node(3)
        self.assertEqual(node.val, 3)

    def test_insert_at_end(self):
        node = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node.insert_at_end(node2)
        node.insert_at_end(node3)
        self.assertEqual(node.next, node2)
        self.assertEqual(node.next.next, node3)
        self.assertEqual(node2.next, node3)

        node4 = Node(4)
        node2.insert_at_end(node4)
        self.assertEqual(node.next.next.next, node4)
        self.assertEqual(node2.next.next, node4)
        self.assertEqual(node3.next, node4)

    def test_reverse(self):
        node = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node.insert_at_end(node2)
        node.insert_at_end(node3)
        node.reverse()
        self.assertEqual(node3.next, node2)
        self.assertEqual(node2.next, node)
        self.assertEqual(node.next, None)

    def test_merge(self):
        node1 = Node(1).insert_at_end(Node(3)).insert_at_end(Node(5))
        node2 = Node(2).insert_at_end(Node(4)).insert_at_end(Node(6))
        head = Node.merge(node1, node2)
        self.assertEqual(head, node1)
        self.assertEqual(head.next, node2)
        self.assertEqual(head.next.next.val, 3)
        self.assertEqual(head.next.next.next.val, 4)
        self.assertEqual(head.next.next.next.next.val, 5)
        self.assertEqual(head.next.next.next.next.next.val, 6)

    def test_find_middle(self):
        node1 = Node(1).insert_at_end(Node(2)).insert_at_end(Node(3))
        prev, middle = node1.find_middle()
        self.assertEqual(prev, node1)
        self.assertEqual(middle.val, 2)

if __name__ == '__main__':
    unittest.main()
