"""
A binary search tree is a binary tree with the property that for any node, the value of this node is greater than any node in its left subtree and less than any node's value in its right subtree. In other words, an inorder traversal of a binary search tree yields a list of values that is monotonically increasing (strictly increasing).
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def valid_bst(root: Node) -> bool:

    def in_order(node: Node, min_val: int, max_val: int) -> None:

        if node == None:
            return True

        if not (min_val < float(node.val) < max_val):
            return False

        left = in_order(node.left, min_val, node.val)
        right = in_order(node.right, node.val, max_val)

        return left and right

    return in_order(root, -float("inf"), float("inf"))


def build_tree(nodes):
    val = next(nodes)
    if val == "x":
        return None
    curr = Node(val)
    curr.left = build_tree(nodes)
    curr.right = build_tree(nodes)

    return curr


def print_tree(root):
    if not root:
        yield "x"
        return
    yield str(root.val)
    yield from print_tree(root.left)
    yield from print_tree(root.right)


if __name__ == "__main__":
    # tree 1
    tree = "6 4 3 x x 5 x x 8 x x"
    root = build_tree(iter(tree.split(" ")))
    print(valid_bst(root))

    #  tree 2
    tree = "6 4 3 x x 8 x x 8 x x"
    root = build_tree(iter(tree.split(" ")))
    print(valid_bst(root))

    # tree 3
    tree = "1 2 x x 3 x x"
    root = build_tree(iter(tree.split(" ")))
    print(valid_bst(root))

    # tree 4
    tree = "x"
    root = build_tree(iter(tree.split(" ")))
    print(valid_bst(root))

    # tree 5
    tree = "3 2 1 x x x 4 x 5 x x"
    root = build_tree(iter(tree.split(" ")))
    print(valid_bst(root))

    #  tree 6
    tree = "6 5 x 4 x x x"
    root = build_tree(iter(tree.split(" ")))
    print(valid_bst(root))
