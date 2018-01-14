from epi.linked_list import *
import unittest

def get_list(L):
    ret = []
    while L:
        ret.append(L.data)
        L = L.next
    return ret

class TestLinkedList(unittest.TestCase):
    def test_merge(self):
        self.check([1,3,5,7], [2,4], [1,2,3,4,5,7])
        self.check([1,3,5,7], [1], [1,1,3,5,7])

    def check(self, l1, l2, result):
        L1 = ListNode(l1[0])
        [insert_end(L1, ListNode(x)) for x in l1[1:]]
        L2 = ListNode(l2[0])
        [insert_end(L2, ListNode(x)) for x in l2[1:]]
        self.assertListEqual(get_list(merge(L1, L2)), result)
