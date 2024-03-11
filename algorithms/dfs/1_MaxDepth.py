class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_max_depth(root: Node) -> int:

    def dfs(node: Node) -> int:
        if node is None:
            return 0

        left += dfs(node.left) + 1
        right += dfs(node.right) + 1

        return max(left, right)

    return dfs(root) - 1 if root else 0
