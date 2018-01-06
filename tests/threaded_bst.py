from algo_ds.insertion import sort
import unittest

class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        A = [5,1,2,6,3,2,1,6,7]
        sort(A)
        self.assertListEqual(A, sorted(A))

if __name__ == '__main__':
    unittest.main()
