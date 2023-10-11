from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> int:
            left = right = 0
            if node == None:
                return 0
            if node.left:
                left = dfs(node.left)
            if node.right:
                right = dfs(node.right)
            self.diameter = max(left + right, self.diameter)
            return max(left, right) + 1

        dfs(root)
        return self.diameter


if __name__ == "__main__":
    node6 = TreeNode(
        val=6,
        left=TreeNode(val=0, right=TreeNode(val=-1)),
        right=TreeNode(val=6, left=TreeNode(val=-4)),
    )
    node_7 = TreeNode(
        val=-7,
        left=TreeNode(val=-6, left=TreeNode(val=5)),
        right=TreeNode(val=-6, left=TreeNode(val=9, left=TreeNode(val=-2))),
    )
    node_9 = TreeNode(val=-9, left=TreeNode(val=9, left=node6), right=node_7)
    node_3 = TreeNode(
        val=-3, left=node_9, right=TreeNode(val=-3, left=TreeNode(val=-4))
    )
    root = TreeNode(val=4, left=TreeNode(val=-7), right=node_3)

    print(Solution().diameterOfBinaryTree(root=root))
