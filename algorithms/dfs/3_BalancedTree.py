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


def build_tree(nodes):
    val = next(nodes)
    if val == "x":
        return None
    curr = Node(val)
    curr.left = build_tree(nodes)
    curr.right = build_tree(nodes)

    return curr


if __name__ == "__main__":
    # tree 1
    tree = "1 2 4 x 7 x x 5 x x 3 x 6 x x"
    root = build_tree(iter(tree.split(" ")))
    print(is_balanced(root))

    #  tree 2
    tree = "1 2 4 x 7 x x 5 x x 3 x 6 8 x x x"
    root = build_tree(iter(tree.split(" ")))
    print(is_balanced(root))

    # tree 3
    tree = "1 2 3 x x 4 x 6 x x 5 x x"
    root = build_tree(iter(tree.split(" ")))
    print(is_balanced(root))

    # tree 4
    tree = "1 2 3 x x 4 x 6 x x 5 x 7 x x"
    root = build_tree(iter(tree.split(" ")))
    print(is_balanced(root))

    # tree 5
    tree = "1 2 3 x x 4 x x 5 6 x 7 x x x"
    root = build_tree(iter(tree.split(" ")))
    print(is_balanced(root))

    #  tree 6
    tree = "1 2 3 7 x x x 4 x x 5 6 x x x"
    root = build_tree(iter(tree.split(" ")))
    print(is_balanced(root))
