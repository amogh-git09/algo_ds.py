from algo_ds.heap import left, right, parent, max_heapify, swap
import sys

class MaxPriorityQueue(object):
    def __init__(self, capacity):
        self.arr = [0]*capacity
        self.heap_size = 0
        self.capacity = capacity

    def maximum(self):
        if self.heap_size == 0:
            raise ValueError("Heap empty")
        return self.arr[0]

    def extract_max(self):
        if self.heap_size == 0:
            raise ValueError("Heap empty")
        swap(self.arr, 0, self.heap_size-1)
        self.heap_size -= 1
        max_heapify(self, 0)
        return self.arr[self.heap_size]

    def heap_increase_key(self, i, key):
        """
        Increases the key of element at index i to 'key'
        """
        if key < self.arr[i]:
            raise ValueError("New key must be larger than existing key.")

        # set new key
        self.arr[i] = key

        # find new spot
        while i > 0 and self.arr[parent(i)] < key:
            swap(self.arr, i, parent(i))
            i = parent(i)

    def insert(self, key):
        """
        Inserts new key into the priority queue.
        """
        if self.heap_size == self.capacity:
            raise ValueError("Overflow!")
        self.arr[self.heap_size] = -sys.maxsize-1
        self.heap_size += 1
        self.heap_increase_key(self.heap_size-1, key)

    def __str__(self):
        return str(self.arr[0:self.heap_size])
