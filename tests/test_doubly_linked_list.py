import unittest
from algo_ds.doubly_linked_list import DoublyLinkedList
from algo_ds.doubly_linked_node import DNode

class TestDoublyLinkedList(unittest.TestCase):
    def test_insert_at_front(self):
        dll = DoublyLinkedList()
        dll.insert_at_front(DNode(1))
        self.assertEqual(str(dll), "1 -> None")

        dll.insert_at_front(DNode(2))
        self.assertEqual(str(dll), "2 -> 1 -> None")

    def test_insert_at_end(self):
        dll = DoublyLinkedList()
        dll.insert_at_end(DNode(1))
        self.assertEqual(str(dll), "1 -> None")

        dll.insert_at_end(DNode(2))
        self.assertEqual(str(dll), "1 -> 2 -> None")
