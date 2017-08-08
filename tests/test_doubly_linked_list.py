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

    def test_merge(self):
        l1 = DoublyLinkedList()
        l1.insert_at_end(DNode(1))
        l1.insert_at_end(DNode(3))
        l1.insert_at_end(DNode(5))
        l1.insert_at_end(DNode(6))

        l2 = DoublyLinkedList()
        l2.insert_at_end(DNode(2))
        l2.insert_at_end(DNode(4))
        l2.insert_at_end(DNode(5))

        merged = DoublyLinkedList.merge(l1, l2)
        self.assertEqual(str(merged), "1 -> 2 -> 3 -> 4 -> 5 -> 5 -> 6 -> None")

        l1 = DoublyLinkedList()
        l1.insert_at_end(DNode(1))
        l1.insert_at_end(DNode(3))
        l1.insert_at_end(DNode(5))
        l1.insert_at_end(DNode(6))

        l2 = DoublyLinkedList()
        l2.insert_at_end(DNode(2))

        merged = DoublyLinkedList.merge(l1, l2)
        self.assertEqual(str(merged), "1 -> 2 -> 3 -> 5 -> 6 -> None")

        l1 = DoublyLinkedList()
        l2 = DoublyLinkedList()
        merged = DoublyLinkedList.merge(l1, l2)
        self.assertEqual(str(merged), "")

    def test_merge_sort(self):
        dll = DoublyLinkedList()
        dll.insert_at_end(DNode(3))
        dll.insert_at_end(DNode(1))
        dll.insert_at_end(DNode(4))
        dll.insert_at_end(DNode(2))
        dll.insert_at_end(DNode(2))
        dll.merge_sort()
        self.assertEqual(str(dll), "1 -> 2 -> 2 -> 3 -> 4 -> None")

        dll = DoublyLinkedList()
        dll.merge_sort()
        self.assertEqual(str(dll), "")

        dll = DoublyLinkedList()
        dll.insert_at_end(DNode(3))
        self.assertEqual(str(dll), "3 -> None")

    def test_dll_to_tree(self):
        dll = TestDoublyLinkedList.get_test_dll()
        root = dll.dll_to_tree()
        self.assertEqual(root.val, 4)
        self.assertEqual(root.prev.val, 2)
        self.assertEqual(root.next.val, 6)
        self.assertEqual(root.prev.prev.val, 1)
        self.assertEqual(root.prev.next.val, 3)
        self.assertEqual(root.next.prev.val, 5)
        self.assertEqual(root.next.next.val, 7)
        self.assertEqual(root.next.prev.prev, None)

    def test_dll_to_tree(self):
        dll = TestDoublyLinkedList.get_test_dll()
        root = dll.dll_to_tree2()
        self.assertEqual(root.val, 4)
        self.assertEqual(root.prev.val, 2)
        self.assertEqual(root.next.val, 6)
        self.assertEqual(root.prev.prev.val, 1)
        self.assertEqual(root.prev.next.val, 3)
        self.assertEqual(root.next.prev.val, 5)
        self.assertEqual(root.next.next.val, 7)
        self.assertEqual(root.next.prev.prev, None)

    def get_test_dll():
        dll = DoublyLinkedList()
        dll.insert_at_end(DNode(1))
        dll.insert_at_end(DNode(2))
        dll.insert_at_end(DNode(3))
        dll.insert_at_end(DNode(4))
        dll.insert_at_end(DNode(5))
        dll.insert_at_end(DNode(6))
        dll.insert_at_end(DNode(7))
        return dll

if __name__ == '__main__':
    unittest.main()
