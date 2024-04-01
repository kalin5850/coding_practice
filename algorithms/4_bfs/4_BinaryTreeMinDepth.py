from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_tree_min_depth(root: Node) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    queue = deque([root])
    min_level = 0

    while len(queue):
        n = len(queue)

        for _ in range(n):
            curr = queue.popleft()
            if curr.left == None and curr.right == None:
                return min_level
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        min_level += 1

    return min_level - 1
