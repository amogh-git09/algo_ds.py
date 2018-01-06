from algo_ds.insertion import sort
import unittest

class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        A = [5,1,2,6,3,2,1,6,7]
        sort(A)
        self.assertListEqual(A, sorted(A))

        B = []
        sort(B)
        self.assertListEqual(B, [])

        C = [1,1,1]
        sort(C)
        self.assertListEqual(C, [1,1,1])

if __name__ == '__main__':
    unittest.main()
