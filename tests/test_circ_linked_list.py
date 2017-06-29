import unittest
from algo_ds.circ_linked_list import CircularLinkedList
from algo_ds.circ_node import CNode

class TestCircularLinkedList(unittest.TestCase):
    def test_insert_at_end(self):
        cll = CircularLinkedList()
        node1 = CNode(1)
        cll.insert_at_end(node1)
        self.assertEqual(cll.last, node1)
        self.assertEqual(cll.last, node1.next)
        node2 = CNode(2)
        cll.insert_at_end(node2)
        self.assertEqual(cll.last, node2)
        self.assertEqual(cll.last.next, node1)

    def test_str(self):
        cll = CircularLinkedList()
        cll.insert_at_end(CNode(1))
        cll.insert_at_end(CNode(2))
        print(cll)
        self.assertEqual(str(cll), "1 -> 2 -> ")

    def test_split(self):
        cll = CircularLinkedList()
        cll.insert_at_end(CNode(1))
        cll.insert_at_end(CNode(2))
        cll.insert_at_end(CNode(3))
        cll.insert_at_end(CNode(4))

        cll1, cll2 = cll.split()
        self.assertEqual(str(cll1), "1 -> 2 -> ")
        self.assertEqual(str(cll2), "3 -> 4 -> ")


        cll = CircularLinkedList()
        cll.insert_at_end(CNode(1))
        cll.insert_at_end(CNode(2))
        cll.insert_at_end(CNode(3))
        cll.insert_at_end(CNode(4))
        cll.insert_at_end(CNode(5))

        cll1, cll2 = cll.split()
        self.assertEqual(str(cll1), "1 -> 2 -> 3 -> ")
        self.assertEqual(str(cll2), "4 -> 5 -> ")


        cll = CircularLinkedList()
        cll.insert_at_end(CNode(1))
        cll.insert_at_end(CNode(2))

        cll1, cll2 = cll.split()
        self.assertEqual(str(cll1), "1 -> ")
        self.assertEqual(str(cll2), "2 -> ")

if __name__ == '__main__':
    unittest.main()
