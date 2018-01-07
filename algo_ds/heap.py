class Heap(object):
    def __init__(self, arr):
        """
        Initializes a max-heap on arr.
        """
        self.arr = arr
        self.heap_size = 0
        self.length = len(arr)
        build_heap(self)

def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def parent(i):
    return (i-1) // 2

def swap(arr, a, b):
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp

def max_heapify(heap, i):
    l = left(i)
    r = right(i)

    # find largest element
    largest = i
    if l < heap.heap_size and heap.arr[l] > heap.arr[largest]:
        largest = l
    if r < heap.heap_size and heap.arr[r] > heap.arr[largest]:
        largest = r

    # swap if larger child exists
    if largest != i:
        swap(heap.arr, i, largest)
        max_heapify(heap, largest)

def build_heap(heap):
    """
    Turns heap.arr into a max-heap.
    """
    heap.heap_size = heap.length
    for i in range(parent(heap.length-1), -1, -1):
        max_heapify(heap, i)

def sort(arr):
    """
    Sorts list arr using heapsort algorithm.
    """
    # build max-heap
    heap = Heap(arr)

    # sort
    for i in range(heap.length-1, 0, -1):
        swap(heap.arr, 0, i)
        heap.heap_size -= 1
        max_heapify(heap, 0) 
