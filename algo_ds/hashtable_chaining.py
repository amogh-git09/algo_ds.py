from algo_ds.doubly_linked_list import DoublyLinkedList
from math import floor

class Element(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __str__(self):
        return "<key: {}, val: {}>".format(self.key, self.val)

class HashTable(object):
    def __init__(self, multiplication_hash=False):
        self.multiplication_hash = multiplication_hash
        if multiplication_hash:
            self.m = 256
        else:
            self.m = 157
        self.table = [None] * self.m

    def hash(self, key):
        if self.multiplication_hash:
            A = 0.51
            return floor(self.m * (key*A % 1))
        else:
            # division method
            return key % self.m

    def insert(self, x):
        if not isinstance(x, Element):
            raise ValueError("Element to insert is not of type 'Element'")

        slot = self.hash(x.key)
        if not self.table[slot]:
            self.table[slot] = DoublyLinkedList()
        self.table[slot].insert_at_front(x)

    def search(self, key):
        slot = self.hash(key)
        if self.table[slot]:
            return self.table[slot].search_by_func(lambda e: e.key == key)
        else:
            return None

    def delete(self, x):
        if not isinstance(x, Element):
            raise ValueError("Element to delete is not of type 'Element'")

        slot = self.hash(x.key)
        self.table[slot].delete(x)
