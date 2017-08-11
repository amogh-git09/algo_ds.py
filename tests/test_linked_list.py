import unittest
from algo_ds.linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def test_insert(self):
        ll = LinkedList()
        ll.insert(1)
        ll.insert(2)
        ll.insert(3)
        self.assertEqual(ll.head.val, 3)
        self.assertEqual(ll.head.next.val, 2)
        self.assertEqual(ll.head.next.next.val, 1)

    def test_insert_at_end(self):
        ll = LinkedList()
        ll.insert_at_end(1)
        ll.insert_at_end(2)
        ll.insert_at_end(3)
        self.assertEqual(ll.head.val, 1)
        self.assertEqual(ll.head.next.val, 2)
        self.assertEqual(ll.head.next.next.val, 3)

    def test_remove(self):
        ll = self.get_test_list()
        self.assertEqual(ll.as_python_list(), [50, 80, 40, 60, 10, 30])
        self.assertEqual(ll.remove(), 50)
        self.assertEqual(ll.remove(), 80)
        self.assertEqual(ll.remove(), 40)
        self.assertEqual(ll.as_python_list(), [60, 10, 30])
        self.assertEqual(ll.remove(), 60)
        self.assertEqual(ll.remove(), 10)
        self.assertEqual(ll.remove(), 30)
        self.assertRaises(IndexError, ll.remove)

    def test_remove_from_end(self):
        ll = self.get_test_list()
        self.assertEqual(ll.as_python_list(), [50, 80, 40, 60, 10, 30])
        self.assertEqual(ll.remove_from_end(), 30)
        self.assertEqual(ll.remove_from_end(), 10)
        self.assertEqual(ll.remove_from_end(), 60)
        self.assertEqual(ll.as_python_list(), [50, 80, 40])
        self.assertEqual(ll.remove_from_end(), 40)
        self.assertEqual(ll.remove_from_end(), 80)
        self.assertEqual(ll.remove_from_end(), 50)
        self.assertRaises(IndexError, ll.remove_from_end)

    def test_length(self):
        ll = self.get_test_list()
        self.assertEqual(ll.length(), 6)
        ll.remove()
        self.assertEqual(ll.length(), 5)

    def get_test_list(self):
        ll = LinkedList()
        ll.insert(30)
        ll.insert(10)
        ll.insert(60)
        ll.insert(40)
        ll.insert(80)
        ll.insert(50)
        return ll

if __name__ == '__main__':
    unittest.main()
