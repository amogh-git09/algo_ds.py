from algo_ds.horner import horner, naive
import unittest
import time

class TestHorner(unittest.TestCase):
    def test_horner(self):
        self.check_horner([1, 2], 5, 1 + 2*5)
        self.check_horner([1, 2, 3], 5, 1 + 2*5 + 3*25)
        self.check_horner([], 1, 0)
        self.check_horner([1, 2], 0, 1)

    def test_naive(self):
        self.check_naive([1, 2], 5, 1 + 2*5)
        self.check_naive([1, 2, 3], 5, 1 + 2*5 + 3*25)
        self.check_naive([], 1, 0)
        self.check_naive([1, 2], 0, 1)

    def test_runtime(self):
        start = int(round(time.time() * 1000))
        horner(range(1, 500), 3)
        end = int(round(time.time() * 1000))
        # print("Horner: {} ms".format(end - start))

        start = int(round(time.time() * 1000))
        naive(range(1, 500), 3)
        end = int(round(time.time() * 1000))
        # print("Naive : {} ms".format(end - start))

    def check_naive(self, A, x, res):
        self.assertEqual(naive(A, x), res)

    def check_horner(self, A, x, res):
        self.assertEqual(horner(A, x), res)
