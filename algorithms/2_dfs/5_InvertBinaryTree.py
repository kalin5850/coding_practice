class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_binary_tree(tree: Node) -> Node:
    def pre_order(node: Node) -> Node:
        if node == None:
            return

        node.left, node.right = node.right, node.left

        pre_order(node.left)
        pre_order(node.right)

        return node

    return pre_order(tree)
