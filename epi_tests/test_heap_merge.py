from epi.heap_merge import *
import unittest
import functools

class TestHeapMerge(unittest.TestCase):
    def test_heap_merge(self):
        lists = [[0,1,2],[1,1,5],[]]
        self.assertListEqual(kwaymerge(lists), sorted(functools.reduce(lambda x, y: x + y, lists, [])))
