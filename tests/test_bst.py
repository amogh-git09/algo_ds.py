from algo_ds.bst import BinarySearchTree
import unittest

class TestBinarySearchTree(unittest.TestCase):
    def test_insert(self):
        tree = BinarySearchTree()
        tree.insert(32, 1)
        tree.insert(20, 2)
        tree.insert(38, 3)
        tree.insert(35, 4)
        tree.insert(10, 5)
        self.assertEqual(tree.root.key, 32)
        self.assertEqual(tree.root.left.key, 20)
        self.assertEqual(tree.root.right.key, 38)
        self.assertEqual(tree.root.left.left.key, 10)
        self.assertEqual(tree.root.right.left.key, 35)
        self.assertEqual(tree.root.parent, None)
        self.assertEqual(tree.root.right.parent, tree.root)

    def test_traversal_inorder(self):
        tree = BinarySearchTree()
        tree.insert(32, 1)
        tree.insert(20, 2)
        tree.insert(38, 3)
        tree.insert(35, 4)
        tree.insert(10, 5)
        result = []
        tree.traversal_inorder(lambda node: result.append(node))
        self.assertEqual(result[0], tree.root.left.left)
        self.assertEqual(result[1], tree.root.left)
        self.assertEqual(result[2], tree.root)
        self.assertEqual(result[3], tree.root.right.left)
        self.assertEqual(result[4], tree.root.right)

    def test_traversal_postorder(self):
        tree = BinarySearchTree()
        tree.insert(32, 1)
        tree.insert(20, 2)
        tree.insert(38, 3)
        tree.insert(35, 4)
        tree.insert(10, 5)
        result = []
        tree.traversal_postorder(lambda node: result.append(node))
        self.assertEqual(result[0], tree.root.left.left)
        self.assertEqual(result[1], tree.root.left)
        self.assertEqual(result[2], tree.root.right.left)
        self.assertEqual(result[3], tree.root.right)
        self.assertEqual(result[4], tree.root)

    def test_traversal_preorder(self):
        tree = BinarySearchTree()
        tree.insert(32, 1)
        tree.insert(20, 2)
        tree.insert(38, 3)
        tree.insert(35, 4)
        tree.insert(10, 5)
        result = []
        tree.traversal_preorder(lambda node: result.append(node))
        self.assertEqual(result[0], tree.root)
        self.assertEqual(result[1], tree.root.left)
        self.assertEqual(result[2], tree.root.left.left)
        self.assertEqual(result[3], tree.root.right)
        self.assertEqual(result[4], tree.root.right.left)

    def test_traversal_breadth_first(self):
        tree = BinarySearchTree()
        tree.insert(32, 1)
        tree.insert(20, 2)
        tree.insert(38, 3)
        tree.insert(35, 4)
        tree.insert(10, 5)
        result = []
        tree.traversal_breadth_first(lambda node: result.append(node))
        self.assertEqual(result[0], tree.root)
        self.assertEqual(result[1], tree.root.left)
        self.assertEqual(result[2], tree.root.right)
        self.assertEqual(result[3], tree.root.left.left)
        self.assertEqual(result[4], tree.root.right.left)

    def test_height(self):
        tree = BinarySearchTree()
        tree.insert(32, 1)
        tree.insert(20, 2)
        tree.insert(38, 3)
        tree.insert(35, 4)
        tree.insert(10, 5)
        self.assertEqual(tree.height(), 2)

        tree = BinarySearchTree()
        tree.insert(32, 1)
        tree.insert(31, 2)
        tree.insert(30, 3)
        tree.insert(29, 4)
        tree.insert(28, 5)
        self.assertEqual(tree.height(), 4)

        tree = BinarySearchTree()
        tree.insert(1, 1)
        self.assertEqual(tree.height(), 0)

        tree = BinarySearchTree()
        self.assertEqual(tree.height(), -1)


    def test_search(self):
        tree = BinarySearchTree()
        tree.insert(32, 1)
        tree.insert(20, 2)
        tree.insert(38, 3)
        tree.insert(35, 4)
        tree.insert(10, 5)
        self.assertEqual(tree.search(38).val, 3)
        self.assertEqual(tree.search(200), None)

    def test_minimum(self):
        tree = BinarySearchTree()
        tree.insert(32, 1)
        tree.insert(20, 2)
        tree.insert(38, 3)
        tree.insert(35, 4)
        tree.insert(10, 5)
        self.assertEqual(tree.minimum().val, 5)

    def test_maximum(self):
        tree = BinarySearchTree()
        tree.insert(32, 1)
        tree.insert(20, 2)
        tree.insert(38, 3)
        tree.insert(35, 4)
        tree.insert(10, 5)
        self.assertEqual(tree.maximum().val, 3)

    def test_succ(self):
        tree = BinarySearchTree()
        tree.insert(32, 1)
        tree.insert(20, 2)
        tree.insert(38, 3)
        tree.insert(35, 4)
        tree.insert(10, 5)
        tree.insert(37, 6)
        tree.insert(50, 6)
        tree.insert(40, 6)
        tree.insert(41, 6)
        tree.insert(42, 6)
        tree.insert(43, 6)
        node1 = tree.search(38)
        node2 = tree.search(35)
        node3 = tree.search(37)
        self.assertEqual(node2.succ(), node3)
        self.assertEqual(node3.succ(), node1)
        node4 = tree.search(43)
        node5 = tree.search(50)
        self.assertEqual(node4.succ(), node5)

    def test_pred(self):
        tree = BinarySearchTree()
        tree.insert(32, 1)
        tree.insert(20, 2)
        tree.insert(38, 3)
        tree.insert(35, 4)
        tree.insert(10, 5)
        tree.insert(37, 6)
        tree.insert(50, 6)
        tree.insert(40, 6)
        tree.insert(41, 6)
        tree.insert(42, 6)
        tree.insert(43, 6)
        node1 = tree.search(38)
        node2 = tree.search(35)
        node3 = tree.search(37)
        node4 = tree.search(32)
        self.assertEqual(node2.pred(), node4)
        self.assertEqual(node3.pred(), node2)
        node4 = tree.search(43)
        node5 = tree.search(42)
        self.assertEqual(node4.pred(), node5)
        node6 = tree.search(10)
        self.assertEqual(node6.pred(), None)

    def test_diameter(self):
        tree = BinarySearchTree()
        self.assertEqual(tree.diameter(), -1)
        tree.insert(20, 1)
        self.assertEqual(tree.diameter(), 0)
        tree.insert(15, 2)
        self.assertEqual(tree.diameter(), 1)
        tree.insert(17, 3)
        self.assertEqual(tree.diameter(), 2)
        tree.insert(28, 4)
        self.assertEqual(tree.diameter(), 3)
        tree.insert(32, 5)
        self.assertEqual(tree.diameter(), 4)
        tree.insert(11, 6)
        tree.insert(8, 7)
        tree.insert(14, 8)
        tree.insert(12, 9)
        tree.insert(12, 10)
        tree.insert(19, 11)
        tree.insert(18, 12)
        tree.insert(18, 13)
        self.assertEqual(tree.diameter(), 8)

    def test_traversal_inorder_iter(self):
        tree = BinarySearchTree()
        tree.insert(32, 1)
        tree.insert(20, 2)
        tree.insert(38, 3)
        tree.insert(35, 4)
        tree.insert(10, 5)
        result = []
        tree.traversal_inorder_iter(lambda node: result.append(node))
        self.assertEqual(result[0], tree.root.left.left)
        self.assertEqual(result[1], tree.root.left)
        self.assertEqual(result[2], tree.root)
        self.assertEqual(result[3], tree.root.right.left)
        self.assertEqual(result[4], tree.root.right)

    def test_traversal_inorder_iter(self):
        tree = BinarySearchTree()
        tree.insert(32, 1)
        tree.insert(20, 2)
        tree.insert(38, 3)
        tree.insert(35, 4)
        tree.insert(10, 5)
        result = []
        tree.traversal_inorder_morris(lambda node: result.append(node))
        self.assertEqual(result[0], tree.root.left.left)
        self.assertEqual(result[1], tree.root.left)
        self.assertEqual(result[2], tree.root)
        self.assertEqual(result[3], tree.root.right.left)
        self.assertEqual(result[4], tree.root.right)

    def test_make_tree(self):
        inorder =  ['D','B','E','A','F','C']
        preorder = ['A','B','D','E','C','F']
        tree = BinarySearchTree.make_tree(inorder, preorder)
        in_result = []
        tree.traversal_inorder_morris(lambda node: in_result.append(node.key))
        self.assertEqual(in_result, inorder)
        pre_result = []
        tree.traversal_preorder(lambda node: pre_result.append(node.key))
        self.assertEqual(pre_result, preorder)

    def test_make_tree(self):
        inorder =  ['A','C','D','E','B','F']
        preorder = ['C','A','D','B','E','F']

        tree = BinarySearchTree.make_tree_2(inorder, preorder)
        in_result = []
        tree.traversal_inorder_morris(lambda node: in_result.append(node.key))
        self.assertEqual(in_result, inorder)
        pre_result = []
        tree.traversal_preorder(lambda node: pre_result.append(node.key))
        self.assertEqual(pre_result, preorder)

        inorder =  ['D','B','E','A','F','C']
        preorder = ['A','B','D','E','C','F']

        tree = BinarySearchTree.make_tree_2(inorder, preorder)
        in_result = []
        tree.traversal_inorder_morris(lambda node: in_result.append(node.key))
        self.assertEqual(in_result, inorder)
        pre_result = []
        tree.traversal_preorder(lambda node: pre_result.append(node.key))
        self.assertEqual(pre_result, preorder)

    def test_width(self):
        tree = BinarySearchTree()
        tree.insert(32, 1)
        tree.insert(20, 2)
        tree.insert(38, 3)
        tree.insert(35, 4)
        tree.insert(10, 5)
        self.assertEqual(tree.width(), 2)

        tree = BinarySearchTree()
        tree.insert(50, None)
        tree.insert(20, None)
        tree.insert(70, None)
        tree.insert(10, None)
        tree.insert(30, None)
        tree.insert(75, None)
        tree.insert(5, None)
        tree.insert(15, None)
        tree.insert(73, None)
        tree.insert(80, None)
        tree.insert(4, None)
        tree.insert(18, None)
        tree.insert(77, None)
        tree.insert(75, None)
        tree.insert(16, None)
        self.assertEqual(tree.width(), 4)

        tree = BinarySearchTree()
        tree.insert(50, None)
        tree.insert(60, None)
        tree.insert(70, None)
        tree.insert(80, None)
        self.assertEqual(tree.width(), 1)

    def test_print_nodes_at_dist_k(self):
        tree = BinarySearchTree()
        tree.insert(50, None)
        tree.insert(20, None)
        tree.insert(70, None)
        tree.insert(10, None)
        tree.insert(30, None)
        tree.insert(75, None)
        tree.insert(5, None)
        tree.insert(15, None)
        tree.insert(73, None)
        tree.insert(80, None)
        tree.insert(4, None)
        tree.insert(18, None)
        tree.insert(77, None)
        tree.insert(85, None)
        tree.insert(16, None)
        result = []
        tree.print_nodes_at_dist_k(4, lambda node: result.append(node.key))
        self.assertCountEqual(result, [4, 18, 77, 85])

    def test_operate_ancestors(self):
        tree = BinarySearchTree()
        tree.insert(50, None)
        tree.insert(20, None)
        tree.insert(70, None)
        tree.insert(10, None)
        tree.insert(30, None)
        tree.insert(75, None)
        tree.insert(5, None)
        tree.insert(15, None)
        tree.insert(73, None)
        tree.insert(80, None)
        tree.insert(4, None)
        tree.insert(18, None)
        tree.insert(77, None)
        tree.insert(85, None)
        tree.insert(16, None)

        result = []
        tree.operate_ancestors(73, lambda node: result.append(node.key))
        self.assertCountEqual(result, [75, 70, 50])

        result = []
        tree.operate_ancestors(85, lambda node: result.append(node.key))
        self.assertCountEqual(result, [80, 75, 70, 50])

    def test_subtree(self):
        tree = BinarySearchTree()
        tree.insert(50, None)
        tree.insert(20, None)
        tree.insert(70, None)
        tree.insert(10, None)
        tree.insert(30, None)
        tree.insert(75, None)
        tree.insert(5, None)
        tree.insert(15, None)
        tree.insert(73, None)
        tree.insert(80, None)
        tree.insert(4, None)
        self.assertEqual(tree.is_subtree(tree), True)
        self.assertEqual(tree.is_subtree(BinarySearchTree(tree.root.right)), True)
        self.assertEqual(tree.is_subtree(BinarySearchTree(tree.root.left.left)), True)

        tree2 = BinarySearchTree()
        tree2.insert(20, None)
        tree2.insert(10, None)
        tree2.insert(30, None)
        tree2.insert(5, None)
        tree2.insert(15, None)
        tree2.insert(4, None)
        self.assertEqual(tree.is_subtree(tree2), True)

        tree2 = BinarySearchTree()
        tree2.insert(20, None)
        tree2.insert(10, None)
        tree2.insert(30, None)
        tree2.insert(5, None)
        tree2.insert(15, None)
        self.assertEqual(tree.is_subtree(tree2), False)
