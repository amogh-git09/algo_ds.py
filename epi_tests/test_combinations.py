from epi.combinations import *
import unittest, time

class TestCombinations(unittest.TestCase):
    def test_combinations(self):
        self.assertEqual(combinations(12, [2,3,7]), 4)

        # start = time.time()
        # print(combinations(250, [2,3,4,5,6]))
        # end = time.time()
        # print("Time taken: {} ms".format((end-start)*1000))

        # start = time.time()
        # print(combinations2(250, [2,3,4,5,6]))
        # end = time.time()
        # print("Time taken: {} ms".format((end-start)*1000))

        # start = time.time()
        # print(combinations3(100000, [2,3,4,5,6]))
        # end = time.time()
        # print("Time taken: {} ms".format((end-start)*1000))

        # start = time.time()
        # print(combinations4(100000, [2,3,4,5,6]))
        # end = time.time()
        # print("Time taken: {} ms".format((end-start)*1000))

        # start = time.time()
        # print(permutations(20, [2,3,4,5,6]))
        # end = time.time()
        # print("Time taken: {} ms".format((end-start)*1000))

        start = time.time()
        print(permutations_2_teams(10, 4, [2,3,7]))
        end = time.time()
        print("Time taken: {} ms".format((end-start)*1000))
