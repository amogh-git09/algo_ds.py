from algo_ds.heap import Heap, sort
import unittest

class TestMaxHeap(unittest.TestCase):
    def test_build_heap(self):
        heap = Heap([5,1,3,2,4,6])
        self.assertListEqual(heap.arr, [6, 4, 5, 2, 1, 3])

    def test_heapsort(self):
        self.check_sort([6,1,3,4,2,6])
        self.check_sort([1,1,1,1])
        self.check_sort([])
        self.check_sort([6,1,3,4,-2,6])

    def check_sort(self, a):
        b = [x for x in a]
        sort(a)
        self.assertListEqual(a, sorted(a))
