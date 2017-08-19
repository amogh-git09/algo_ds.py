import unittest
from algo_ds.doubly_linked_list import DoublyLinkedList
from algo_ds.doubly_linked_node import DNode

class TestDoublyLinkedList(unittest.TestCase):
    def test_insert_at_front(self):
        dll = DoublyLinkedList()
        dll.insert_at_front(1)
        self.assertEqual(str(dll), "1 -> None")

        dll.insert_at_front(2)
        self.assertEqual(str(dll), "2 -> 1 -> None")

    def test_insert_at_end(self):
        dll = DoublyLinkedList()
        dll.insert_at_end(1)
        self.assertEqual(str(dll), "1 -> None")

        dll.insert_at_end(2)
        self.assertEqual(str(dll), "1 -> 2 -> None")

    def test_reverse(self):
        dll = DoublyLinkedList()
        dll.insert_at_end(1)
        dll.insert_at_end(2)
        dll.insert_at_end(3)
        dll.insert_at_end(4)
        dll.reverse()
        self.assertEqual(str(dll), "4 -> 3 -> 2 -> 1 -> None")

        dll = DoublyLinkedList()
        dll.insert_at_end(1)
        dll.reverse()
        self.assertEqual(str(dll), "1 -> None")

        dll = DoublyLinkedList()
        dll.reverse()

    def test_quick_sort(self):
        dll = DoublyLinkedList()
        dll.insert_at_end(1)
        dll.insert_at_end(1)
        dll.insert_at_end(4)
        dll.insert_at_end(2)
        dll.quick_sort()
        self.assertEqual(str(dll), "1 -> 1 -> 2 -> 4 -> None")

        dll.insert_at_end(8)
        dll.insert_at_end(2)
        dll.insert_at_end(1)
        dll.insert_at_end(6)
        dll.quick_sort()
        self.assertEqual(str(dll), "1 -> 1 -> 1 -> 2 -> 2 -> 4 -> 6 -> 8 -> None")

    def test_merge(self):
        l1 = DoublyLinkedList()
        l1.insert_at_end(1)
        l1.insert_at_end(3)
        l1.insert_at_end(5)
        l1.insert_at_end(6)

        l2 = DoublyLinkedList()
        l2.insert_at_end(2)
        l2.insert_at_end(4)
        l2.insert_at_end(5)

        merged = DoublyLinkedList.merge(l1, l2)
        self.assertEqual(str(merged), "1 -> 2 -> 3 -> 4 -> 5 -> 5 -> 6 -> None")

        l1 = DoublyLinkedList()
        l1.insert_at_end(1)
        l1.insert_at_end(3)
        l1.insert_at_end(5)
        l1.insert_at_end(6)

        l2 = DoublyLinkedList()
        l2.insert_at_end(2)

        merged = DoublyLinkedList.merge(l1, l2)
        self.assertEqual(str(merged), "1 -> 2 -> 3 -> 5 -> 6 -> None")

        l1 = DoublyLinkedList()
        l2 = DoublyLinkedList()
        merged = DoublyLinkedList.merge(l1, l2)
        self.assertEqual(str(merged), "")

    def test_merge_sort(self):
        dll = DoublyLinkedList()
        dll.insert_at_end(3)
        dll.insert_at_end(1)
        dll.insert_at_end(4)
        dll.insert_at_end(2)
        dll.insert_at_end(2)
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

    def test_sum_exists(self):
        dll = TestDoublyLinkedList.get_test_dll()
        self.assertEqual(dll.sum_exists(3), True)
        self.assertEqual(dll.sum_exists(-3), False)
        self.assertEqual(dll.sum_exists(8), True)
        self.assertEqual(dll.sum_exists(10), True)
        self.assertEqual(dll.sum_exists(20), False)

    def test_search_by_func(self):
        dll = TestDoublyLinkedList.get_test_dll()
        self.assertEqual(dll.search_by_func(lambda e: e == 4), 4)
        self.assertEqual(dll.search_by_func(lambda e: e == 334), None)

    def test_delete(self):
        dll = TestDoublyLinkedList.get_test_dll()
        dll.delete(4)
        self.assertEqual(str(dll), "1 -> 2 -> 3 -> 5 -> 6 -> 7 -> None")
        dll.delete(7)
        self.assertEqual(str(dll), "1 -> 2 -> 3 -> 5 -> 6 -> None")
        dll.delete(1)
        self.assertEqual(str(dll), "2 -> 3 -> 5 -> 6 -> None")

    def get_test_dll():
        dll = DoublyLinkedList()
        dll.insert_at_end(1)
        dll.insert_at_end(2)
        dll.insert_at_end(3)
        dll.insert_at_end(4)
        dll.insert_at_end(5)
        dll.insert_at_end(6)
        dll.insert_at_end(7)
        return dll

if __name__ == '__main__':
    unittest.main()
