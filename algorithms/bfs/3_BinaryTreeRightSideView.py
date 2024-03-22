from collections import deque
from typing import List


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_tree_right_side_view(root: Node) -> List[int]:
    result = []
    queue = deque([root])

    while len(queue):
        tmp = []
        n = len(queue)

        for _ in range(n):
            curr = queue.popleft()
            tmp.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        if len(tmp):
            result.append(tmp[-1])

    return result
