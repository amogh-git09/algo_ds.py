from algo_ds.max_heap import MaxHeap
import unittest

class TestMaxHeap(unittest.TestCase):
    def test_heap_sort(self):
        arr = [4, 2, 1, 5, 3]
        MaxHeap.heap_sort(arr)
        self.assertEqual(arr, [1,2,3,4,5])

        check = arr = [43,345,46,75,12,2,5,7,6,3,43,46,75]
        MaxHeap.heap_sort(arr)
        self.assertEqual(arr, sorted(check))
