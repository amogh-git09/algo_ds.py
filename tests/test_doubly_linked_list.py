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

    def test_reverse(self):
        dll = DoublyLinkedList()
        dll.insert_at_end(DNode(1))
        dll.insert_at_end(DNode(2))
        dll.insert_at_end(DNode(3))
        dll.insert_at_end(DNode(4))
        dll.reverse()
        self.assertEqual(str(dll), "4 -> 3 -> 2 -> 1 -> None")

        dll = DoublyLinkedList()
        dll.insert_at_end(DNode(1))
        dll.reverse()
        self.assertEqual(str(dll), "1 -> None")

        dll = DoublyLinkedList()
        dll.reverse()

    def test_quick_sort(self):
        dll = DoublyLinkedList()
        dll.insert_at_end(DNode(1))
        dll.insert_at_end(DNode(1))
        dll.insert_at_end(DNode(4))
        dll.insert_at_end(DNode(2))
        dll.quick_sort()
        self.assertEqual(str(dll), "1 -> 1 -> 2 -> 4 -> None")

        dll.insert_at_end(DNode(8))
        dll.insert_at_end(DNode(2))
        dll.insert_at_end(DNode(1))
        dll.insert_at_end(DNode(6))
        dll.quick_sort()
        self.assertEqual(str(dll), "1 -> 1 -> 1 -> 2 -> 2 -> 4 -> 6 -> 8 -> None")
