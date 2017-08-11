import unittest
from algo_ds.binary_heap import BinaryHeap, Element

class TestBinaryHeap(unittest.TestCase):
    def test_insert(self):
        heap = BinaryHeap(8)
        heap.insert(50)
        heap.insert(60)
        heap.insert(20)
        heap.insert(40)
        heap.insert(30)
        heap.insert(80)
        self.assertEqual(heap.get_keys(), [20,30,50,60,40,80])
        self.assertEqual(heap.size, 6)
        heap.insert(75)
        heap.insert(70)
        self.assertRaises(IndexError, heap.insert, 80)

    def test_heapify(self):
        heap = BinaryHeap(8)
        heap.arr = [Element(x) for x in [4,7,1,3,2,8,5,6]]
        heap.size = len(heap.arr)
        for i in range(0, len(heap.arr)//2):
            heap.heapify(i)
        self.assertEqual(heap.get_keys(), [1,2,4,3,7,8,5,6])

    def test_get_min(self):
        heap = self.get_test_heap()
        self.assertEqual(heap.get_min().key, 20)
        self.assertEqual(heap.get_min().key, 20)

    def test_extract_min(self):
        heap = self.get_test_heap()
        size = heap.size
        self.assertEqual(heap.extract_min().key, 20)
        self.assertEqual(heap.size, size-1)
        self.assertEqual(heap.extract_min().key, 30)
        self.assertEqual(heap.extract_min().key, 40)
        self.assertEqual(heap.extract_min().key, 50)
        self.assertEqual(heap.extract_min().key, 60)
        self.assertEqual(heap.extract_min().key, 80)
        self.assertRaises(IndexError, heap.extract_min)

    @staticmethod
    def get_test_heap():
        heap = BinaryHeap(8)
        heap.insert(50)
        heap.insert(60)
        heap.insert(20)
        heap.insert(40)
        heap.insert(30)
        heap.insert(80)
        return heap
