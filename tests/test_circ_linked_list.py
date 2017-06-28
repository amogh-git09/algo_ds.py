import unittest
from algo_ds.circ_linked_list import CircularLinkedList
from algo_ds.circ_node import CNode

class TestCircularLinkedList(unittest.TestCase):
    def test_insert(self):
        cll = CircularLinkedList()
        node1 = CNode(1)
        cll.insert(node1)
        self.assertEqual(cll.last, node1)
        self.assertEqual(cll.last, node1.next)
        node2 = CNode(2)
        cll.insert(node2)
        self.assertEqual(cll.last, node2)
        self.assertEqual(cll.last.next, node1)

    def test_str(self):
        cll = CircularLinkedList()
        cll.insert(CNode(1))
        cll.insert(CNode(2))
        print(cll)
        self.assertEqual(str(cll), "1 -> 2 -> ")

if __name__ == '__main__':
    unittest.main()
