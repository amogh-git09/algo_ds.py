import unittest
from algo_ds.circ_node import CNode

class TestCNode(unittest.TestCase):
    def test_find_middle(self):
        node = CNode(1)
        mid, mid_next = node.find_middle()
        self.assertEqual(mid, node)
        self.assertEqual(mid_next, node)

        node2 = CNode(2)
        node.insert_at_end(node2)
        mid, mid_next = node2.find_middle()
        self.assertEqual(mid, node)
        self.assertEqual(mid_next, node2)

        node3 = CNode(3)
        node2.insert_at_end(node3)
        mid, mid_next = node3.find_middle()
        self.assertEqual(mid, node2)
        self.assertEqual(mid_next, node3)

        node4 = CNode(4)
        node3.insert_at_end(node4)
        node5 = CNode(5)
        node4.insert_at_end(node5)
        mid, mid_next = node5.find_middle()
        self.assertEqual(mid, node3)
        self.assertEqual(mid_next, node4)

    def test_split(self):
        node = CNode(1)
        node2 = CNode(2)
        node.insert_at_end(node2)
        n1, n2 = node2.split()
        self.assertEqual(n1, node)
        self.assertEqual(n2, node2)

        node3 = CNode(3)
        node4 = CNode(4)
        node5 = CNode(5)

        node2.insert_at_end(node3)
        node3.insert_at_end(node4)
        node4.insert_at_end(node5)

        n1, n2 = node5.split()
        self.assertEqual(n1, node3)
        self.assertEqual(n2, node5)

    def test_insert_sorted(self):
        node = CNode(1)
        node2 = CNode(2)
        last = node.insert_sorted(node2)
        self.assertEqual(last, node2)

        node = CNode(1)
        node2 = CNode(0)
        last = node.insert_sorted(node2)
        self.assertEqual(last, node)
        node3 = CNode(3)
        last = last.insert_sorted(node3)
        self.assertEqual(last, node3)
        node4 = CNode(2)
        last = last.insert_sorted(node4)
        self.assertEqual(last, node3)
        self.assertEqual(last.next, node2)
        self.assertEqual(last.next.next, node)
        self.assertEqual(last.next.next.next, node4)

if __name__ == '__main__':
    unittest.main()
