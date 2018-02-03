from algo_ds.inventory import *
import unittest, time

class TestInventory(unittest.TestCase):
    def test_inventory(self):
        d = [1,4,5,12,15,25,35,8,12]
        m = 10
        h = lambda x: x
        c = 4

        # start = time.time()
        # cost, stocks = plan(d,m,h,c)
        # end = time.time()
        # print(cost)
        # print(stocks)
        # print("Time taken: {} ms".format((end - start)*1000))
        # print("")
        # interpret_result(stocks, d, c, h, m)

        start = time.time()
        cost = plan2(d,m,h,c)
        end = time.time()
        print("Time taken: {} ms".format((end - start)*1000))
        # [print(c) for c in cost]
        # [print(["{0:2d}".format(a) for a in x]) for x in cost]
        interpret_result(cost, d, c, h, m)
