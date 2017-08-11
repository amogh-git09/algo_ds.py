class Element(object):
    def __init__(self, key, val=None):
        self.key = key
        self.val = val

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

    @staticmethod
    def parent(index):
        return (index-1)//2

    def swap(self, a, b):
        tmp = self.arr[a]
        self.arr[a] = self.arr[b]
        self.arr[b] = tmp

    def get_keys(self):
        return [x.key for x in self.arr[:self.size]]
