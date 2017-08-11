from functools import total_ordering

@total_ordering
class Element(object):
    def __init__(self, key, val=None):
        self.key = key
        self.val = val

    def __eq__(self, other):
        return self.key == other.key

    def __lt__(self, other):
        return self.key < other.key

    def __str__(self):
        return ("<key: {}, val: {}>".format(self.key, self.val))

class BinaryHeap(object):
    def __init__(self, capacity=50):
        self.capacity = capacity
        self.size = 0
        self.arr = [None]*capacity

    def insert(self, key, val=None):
        if self.size >= self.capacity:
            raise IndexError("Exceeding capacity")
        self.arr[self.size] = Element(key, val)
        self.fix_heap_prop(self.size)
        self.size += 1

    def fix_heap_prop(self, index):
        p = self.parent(index)
        while p >= 0 and self.arr[p].key > self.arr[index].key:
            self.swap(p, index)
            index = p
            p = self.parent(index)

    def heapify(self, index=0):
        c1 = self.left_child(index)
        c2 = self.right_child(index)
        if c1 >= self.size:
            return
        min_index = index
        if self.arr[min_index] > self.arr[c1]:
            min_index = c1
        if c2 < self.size and self.arr[min_index] > self.arr[c2]:
            min_index = c2
        if min_index != index:
            self.swap(min_index, index)
            self.heapify(min_index)

    def get_min(self):
        if self.size <= 0:
            raise IndexError("Heap empty")
        return self.arr[0]

    def extract_min(self):
        if self.size <= 0:
            raise IndexError("Heap empty")
        self.swap(0, self.size-1)
        self.size -= 1
        self.heapify()
        return self.arr[self.size]

    @staticmethod
    def left_child(index):
        return 2*index + 1

    @staticmethod
    def right_child(index):
        return 2*index + 2

    @staticmethod
    def parent(index):
        return (index-1)//2

    def swap(self, a, b):
        tmp = self.arr[a]
        self.arr[a] = self.arr[b]
        self.arr[b] = tmp

    def get_keys(self):
        return [x.key for x in self.arr[:self.size]]
