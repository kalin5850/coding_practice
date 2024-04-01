class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert_bst(bst: Node, val: int) -> Node:
    # WRITE YOUR BRILLIANT CODE HERE

    def dfs(node: Node, value: int) -> Node:

        if node == None:
            return Node(value)

        if node.val == value:
            return node

        if node.val > value:
            node.left = dfs(node.left, value)
        else:
            node.right = dfs(node.right, value)

        return node

    return dfs(bst, val)


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
    tree = "8 4 2 1 x x 3 x x 6 x x 12 10 x x 14 x 15 x x"
    root = build_tree(iter(tree.split(" ")))
    print(insert_bst(root, 7))

    #  tree 2
    tree = "37 19 2 x x 28 23 x x 35 x x 44 x 58 52 x x 67 x x"
    root = build_tree(iter(tree.split(" ")))
    print(insert_bst(root, 42))

    # tree 3
    tree = "421 223 79 42 x x 157 133 x x x 327 x 404 356 x x 415 x x 741 626 x x 887 801 795 x x 842 x x 903 x 977 x x 404"
    root = build_tree(iter(tree.split(" ")))
    print(insert_bst(root, 404))
