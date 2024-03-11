from typing import Optional


# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(root: Node, target):
    if root is None:
        return None
    if root.value == target:
        return root
    left = dfs(root.left, target)
    if left is not None:
        return left
    return dfs(root.right, target)


def dfs(node, state):
    if node is null:
        ...
        return
    left = dfs(node.left, state)
    right = dfs(node.right, state)

    ...

    return ...
