from typing import List


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zig_zag_traversal(root: Node) -> List[List[int]]:
    result = []
    queue = []
    queue.append(root)
    count_level = 0

    while len(queue):
        n = len(queue)
        tmp = []

        for _ in range(n):
            curr = queue.pop(0)
            tmp.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        if tmp and count_level % 2 == 0:
            result.append(tmp)
        else:
            tmp = sorted(tmp, reverse=True)
            result.append(tmp)

        count_level += 1

    return result
