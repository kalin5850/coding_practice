class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_max_depth(root: Node) -> int:

    def dfs(node: Node) -> int:
        if node is None:
            return 0

        left = dfs(node.left) + 1
        right = dfs(node.right) + 1

        return max(left, right)

    return dfs(root) - 1 if root else 0


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
    """
                5
              /   \  
            4       6
          /   \
        3       8
    """
    tree = "5 4 3 x x 8 x x 6 x x"
    root = build_tree(iter(tree.split(" ")))
    print(tree_max_depth(root))

    #  tree 2
    """
                1
    """
    tree = "1 x x"
    root = build_tree(iter(tree.split(" ")))
    print(tree_max_depth(root))

    # tree 3
    """
                x
    """
    tree = "x"
    root = build_tree(iter(tree.split(" ")))
    print(tree_max_depth(root))

    # tree 4
    """
        6
        |
        9
        |
        11
        |
        7
    """
    tree = "6 x 9 x 11 x 7 x x"
    root = build_tree(iter(tree.split(" ")))
    print(tree_max_depth(root))
