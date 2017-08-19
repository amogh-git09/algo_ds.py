from algo_ds.doubly_linked_list import DoublyLinkedList

class Element(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val

class HashTable(object):
    def __init__(self):
        self.m = 157
        self.table = [None] * self.m

    def hash(self, key):
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
