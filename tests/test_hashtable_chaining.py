from algo_ds.hashtable_chaining import *
import unittest

class TestHashTable(unittest.TestCase):
    def test_insert_search(self):
        ht = self.get_hash_table()
        self.assertEqual(ht.search(134).val, 1)
        self.assertEqual(ht.search(542).val, 2)
        self.assertEqual(ht.search(626).val, 3)
        self.assertEqual(ht.search(123).val, 4)
        self.assertEqual(ht.search(949).val, 5)
        self.assertEqual(ht.search(346).val, 6)

    def test_insert_search_multiplication(self):
        ht = self.get_hash_table(True)
        self.assertEqual(ht.search(134).val, 1)
        self.assertEqual(ht.search(542).val, 2)
        self.assertEqual(ht.search(626).val, 3)
        self.assertEqual(ht.search(123).val, 4)
        self.assertEqual(ht.search(949).val, 5)
        self.assertEqual(ht.search(346).val, 6)

    def test_delete(self):
        ht = self.get_hash_table()
        elem = ht.search(626)
        ht.delete(elem)
        self.assertEqual(ht.search(elem.key), None)

    def get_hash_table(self, multiplication_hash=False):
        ht = HashTable(multiplication_hash)
        ht.insert(Element(134, 1))
        ht.insert(Element(542, 2))
        ht.insert(Element(626, 3))
        ht.insert(Element(123, 4))
        ht.insert(Element(949, 5))
        ht.insert(Element(346, 6))
        return ht
