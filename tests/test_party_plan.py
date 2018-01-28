from algo_ds.party_plan import *
import unittest, random

class TestPartyPlan(unittest.TestCase):
    def test_party_plan(self):
        tree = self.get_tree()
        [print(n) for n in max_conv(tree)]

    def get_tree(self):
        nodes = [Node(id = i, conv = random.randint(0, 10)) for i in range(20)]

        nodes[0].left = nodes[1]
        nodes[1].right_sibling = nodes[2]
        nodes[2].right_sibling = nodes[3]
        nodes[3].right_sibling = nodes[4]

        nodes[1].left = nodes[5]
        nodes[5].right_sibling = nodes[6]

        nodes[2].left = nodes[7]
        nodes[7].right_sibling = nodes[8]

        nodes[3].left = nodes[9]
        nodes[9].right_sibling = nodes[10]

        nodes[4].left = nodes[11]

        nodes[5].left = nodes[12]
        nodes[12].right_sibling = nodes[13]

        nodes[7].left = nodes[14]

        nodes[10].left = nodes[15]
        nodes[15].right_sibling = nodes[16]

        nodes[15].left = nodes[17]
        nodes[17].right_sibling = nodes[18]

        nodes[16].left = nodes[19]

        return nodes[0]
