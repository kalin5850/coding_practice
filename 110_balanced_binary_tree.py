from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    is_balanced = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> int:
            left = right = 0
            if node == None:
                self.is_balanced = True
                return 0
            if node.left:
                left = dfs(node.left)
            if node.right:
                right = dfs(node.right)
            if abs(left - right) >= 2:
                self.is_balanced = False
            # print("left %s - right %s " % (left, right))
            return max(left, right) + 1

        dfs(root)
        return self.is_balanced
