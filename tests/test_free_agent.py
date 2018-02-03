from algo_ds.free_agent import *
import unittest, time

class TestFreeAgent(unittest.TestCase):
    def test_free_agent(self):
        fee = [[10,20,5,8],
               [15,10,12,14],
               [2,4,10,22,15],
               [5,8,16,14,10],
               [1,14,12,22,6]]

        vorp = [[8,6,7,2,4],
                [1,8,10,8,5],
                [2,7,6,7,8],
                [9,7,9,5,3],
                [6,6,6,4,8]]

        budget = 10

        start = time.time()
        result = maximize_vorp(budget, fee, vorp)
        end = time.time()
        print(result)
        print("Time taken: {} ms".format((end - start)*1000))

        start = time.time()
        result = maximize_vorp2(budget, fee, vorp)
        end = time.time()
        # [print(["{0:2d}".format(a.vorp) for a in r]) for r in result]
        # print("Time taken: {} ms".format((end - start)*1000))
        print_players(result, fee, vorp, budget)
        print("Time taken: {} ms".format((end - start)*1000))
