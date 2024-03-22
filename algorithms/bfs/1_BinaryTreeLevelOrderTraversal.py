from collections import deque
from typing import List


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order_traversal(root: Node) -> List[List[int]]:
    result = []
    queue = deque([root])

    while len(queue):
        n = len(queue)
        tmp = []

        for _ in range(n):
            curr = queue.popleft()
            tmp.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        if tmp:
            result.append(tmp)
    return result


def build_tree(nodes):
    val = next(nodes)
    if val == "x":
        return None
    curr = Node(val)
    curr.left = build_tree(nodes)
    curr.right = build_tree(nodes)

    return curr


if __name__ == "__main__":
    # root = build_tree(iter(input().split()), int)
    tree = "1 2 4 x 7 x x 5 x x 3 x 6 x x"
    root = build_tree(iter(tree.split(" ")))
    res = level_order_traversal(root)
    for row in res:
        print(" ".join(map(str, row)))
