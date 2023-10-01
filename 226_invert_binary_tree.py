from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        "BFS"
        stack = [root]
        while len(stack) > 0:
            current_node = stack.pop()
            if current_node:
                stack.insert(0, current_node.left)
                stack.insert(0, current_node.right)
                # swape left and right node
                current_node.left, current_node.right = (
                    current_node.right,
                    current_node.left,
                )

        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        "BFS with recursive"
        # base case
        current_node = root
        if current_node == None:
            return root
        current_node.left, current_node.right = (
            current_node.right,
            current_node.left,
        )
        self.invertTree(root=current_node.left)
        self.invertTree(root=current_node.right)

        return root


if __name__ == "__main__":
    node2 = TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=3))
    node7 = TreeNode(val=7, left=TreeNode(val=6), right=TreeNode(val=9))
    root = TreeNode(val=4, left=node2, right=node7)

    result = Solution().invertTree1(root=root)
    print(result.__dict__)
    tmp = TreeNode(val=1)
    if tmp.left is None:
        print(None)
