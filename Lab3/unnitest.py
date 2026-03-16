import unittest
from Lab import BinaryTree, find_successor


def build_tree():
    root = BinaryTree(10)
    root.left = BinaryTree(5, parent=root)
    root.right = BinaryTree(15, parent=root)
    root.left.left = BinaryTree(3, parent=root.left)
    root.left.right = BinaryTree(7, parent=root.left)
    root.right.right = BinaryTree(20, parent=root.right)
    return root


class TestFindSuccessor(unittest.TestCase):

    def setUp(self):
        self.root = build_tree()

    def test_successor_of_7_is_10(self):
        result = find_successor(self.root, self.root.left.right)
        self.assertEqual(result.value, 10)

    def test_successor_of_5_is_7(self):
        result = find_successor(self.root, self.root.left)
        self.assertEqual(result.value, 7)

    def test_successor_of_10_is_15(self):
        result = find_successor(self.root, self.root)
        self.assertEqual(result.value, 15)

    def test_successor_of_15_is_20(self):
        result = find_successor(self.root, self.root.right)
        self.assertEqual(result.value, 20)

    def test_successor_of_3_is_5(self):
        result = find_successor(self.root, self.root.left.left)
        self.assertEqual(result.value, 5)

    def test_successor_of_max_is_none(self):
        result = find_successor(self.root, self.root.right.right)
        self.assertIsNone(result)

    def test_full_inorder_sequence(self):
        nodes = [
            self.root.left.left,
            self.root.left,
            self.root.left.right,
            self.root,
            self.root.right,
            self.root.right.right,
        ]
        expected = [5, 7, 10, 15, 20, None]

        for node, exp in zip(nodes, expected):
            result = find_successor(self.root, node)
            result_val = result.value if result else None
            self.assertEqual(result_val, exp)

    def test_single_node_no_successor(self):
        single = BinaryTree(42)
        self.assertIsNone(find_successor(single, single))

    def test_right_skewed_tree(self):
        root = BinaryTree(1)
        root.right = BinaryTree(2, parent=root)
        root.right.right = BinaryTree(3, parent=root.right)
        root.right.right.right = BinaryTree(4, parent=root.right.right)

        self.assertEqual(find_successor(root, root).value, 2)
        self.assertEqual(find_successor(root, root.right).value, 3)
        self.assertEqual(find_successor(root, root.right.right).value, 4)
        self.assertIsNone(find_successor(root, root.right.right.right))

    def test_left_skewed_tree(self):
        root = BinaryTree(4)
        root.left = BinaryTree(3, parent=root)
        root.left.left = BinaryTree(2, parent=root.left)
        root.left.left.left = BinaryTree(1, parent=root.left.left)

        self.assertEqual(find_successor(root, root.left.left.left).value, 2)
        self.assertEqual(find_successor(root, root.left.left).value, 3)
        self.assertEqual(find_successor(root, root.left).value, 4)
        self.assertIsNone(find_successor(root, root))


if __name__ == "__main__":
    unittest.main(verbosity=2)