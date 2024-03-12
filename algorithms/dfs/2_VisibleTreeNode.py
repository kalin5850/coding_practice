# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def visible_tree_node(root: Node) -> int:
    def dfs(node: Node, max_value: int) -> int:
        if node == None:
            return 0

        total = 0
        if float(node.val) >= float(max_value):
            total += 1
            max_value = node.val

        total += dfs(node.left, max_value)
        total += dfs(node.right, max_value)

        return total

    return dfs(root, -float("inf"))


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
    tree = "5 4 3 x x 8 x x 6 x x"
    root = build_tree(iter(tree.split(" ")))
    print(visible_tree_node(root))

    #  tree 2
    tree = "-100 x -500 x -50 x x"
    root = build_tree(iter(tree.split(" ")))
    print(visible_tree_node(root))

    # tree 3
    tree = "9 8 11 x x 20 x x 6 x x"
    root = build_tree(iter(tree.split(" ")))
    print(visible_tree_node(root))

    # tree 4
    tree = "5 8 3 x x 8 x x 6 x x"
    root = build_tree(iter(tree.split(" ")))
    print(visible_tree_node(root))

    # tree 5
    tree = "3 1 3 x x 3 x x 1 2 5 x x x x"
    root = build_tree(iter(tree.split(" ")))
    print(visible_tree_node(root))

    #  tree 6
    tree = "5 8 3 x x 9 x 7 8 x x x 6 x x"
    root = build_tree(iter(tree.split(" ")))
    print(visible_tree_node(root))
