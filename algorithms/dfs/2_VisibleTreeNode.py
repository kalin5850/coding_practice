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
        if node.val >= max_value:
            total += 1
            max_value = node.val

        total += dfs(node.left, max_value)
        total += dfs(node.right, max_value)

        return total

    return dfs(root, -float("inf"))
