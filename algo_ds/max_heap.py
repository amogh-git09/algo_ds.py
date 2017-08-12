class MaxHeap(object):
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.arr = [None]*capacity

    def set_arr(self, arr):
        self.arr = arr
        self.size = len(arr)
        if self.capacity < self.size:
            self.capacity = self.size

    def heapify(self, index):
        c1 = self.left_child(index)
        c2 = self.right_child(index)
        max_index = index
        if c1 < self.size and self.arr[c1] > self.arr[max_index]:
            max_index = c1
        if c2 < self.size and self.arr[c2] > self.arr[max_index]:
            max_index = c2
        if max_index != index:
            self.swap(max_index, index)
            self.heapify(max_index)

    def build_heap(self):
        for i in range(self.size//2-1, -1, -1):
            self.heapify(i)

    def extract_min(self):
        self.swap(0, self.size-1)
        self.size -= 1
        self.heapify(0)
        return self.arr[self.size]

    @staticmethod
    def heap_sort(arr):
        heap = MaxHeap()
        heap.set_arr(arr)

        heap.build_heap()
        for i in range(0, heap.size-1):
            heap.extract_min()

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
