from typing import List


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pre_order(root: Node) -> List[int]:
    "5 -> 4 -> 3 -> 8 -> 1 -> 2 -> 6 -> 9"
    stack = []
    result = []
    curr = root

    while True:
        if curr:
            stack.append(curr)
            result.append(curr.val)
            curr = curr.left
        elif stack:
            curr = stack.pop()
            curr = curr.right
        else:
            break

    print(result)


def build_tree(nodes):
    val = next(nodes)
    if val == "x":
        return None
    curr = Node(val)
    curr.left = build_tree(nodes)
    curr.right = build_tree(nodes)

    return curr


if __name__ == "__main__":
    # tree 1
    """
                5
              /   \  
            4       6
          /   \      \
        3       8     9
              /   \
             1     2
    """
    tree = "5 4 3 x x 8 1 x x 2 x x 6 x 9 x x"
    root = build_tree(iter(tree.split(" ")))
    pre_order(root)
