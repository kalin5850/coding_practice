class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(tree: Node) -> bool:

    def post_order(node: Node) -> int:
        if node == None:
            return 0

        left = post_order(node.left)
        right = post_order(node.right)

        if abs(left - right) > 1:
            return -1

        return max(left, right) + 1

    return post_order(tree) != -1


def is_balanced(tree: Node) -> bool:
    balanced = True

    def post_order(node: Node) -> int:

        if node == None:
            return 0

        nonlocal balanced

        left_h = post_order(node.left) + 1
        right_h = post_order(node.right) + 1

        if abs(left_h - right_h) > 1:
            balanced = False

        return max(left_h, right_h)

    post_order(tree)

    return balanced
