import unittest
from algo_ds.binary_heap import BinaryHeap

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
