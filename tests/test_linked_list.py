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

    def test_remove(self):
        ll = self.get_test_list()
        self.assertEqual(ll.as_python_list(), [50, 80, 40, 60, 10, 30])
        self.assertEqual(ll.remove(), 50)
        self.assertEqual(ll.remove(), 80)
        self.assertEqual(ll.remove(), 40)
        self.assertEqual(ll.as_python_list(), [60, 10, 30])

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
