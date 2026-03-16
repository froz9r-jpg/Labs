class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def find_successor(tree: BinaryTree, node: BinaryTree) -> BinaryTree:
    if node.right:
        current = node.right
        while current.left:
            current = current.left
        return current

    successor = None
    current = tree
    while current:
        if node.value < current.value:
            successor = current
            current = current.left
        elif node.value > current.value:
            current = current.right
        else:
            break

    return successor