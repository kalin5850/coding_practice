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

    print(" -> ".join(result))


def in_order(root: Node) -> List[int]:
    "x -> 3 -> x -> 4 -> x -> 1 -> x -> 8 -> x -> 2 -> x -> 5 -> x -> 6 -> x -> 9 -> x"
    " 3 -> 4 -> 1 -> 8 -> 2 -> 5 -> 6 -> 9"
    stack = []
    result = []
    curr = root

    while True:
        if curr:
            stack.append(curr)
            curr = curr.left
        elif stack:
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        else:
            break

    print(" -> ".join(result))


# TODO
def post_order(root: Node) -> List[int]:
    "x -> x -> 3 -> x -> 1 -> x -> x -> 2 -> 8 -> 4 -> x -> x -> x -> x -> 9 -> 6 -> 5"
    "3 -> 1 -> 2 -> 8 -> 4 -> 9 -> 6 -> 5"
    stack1 = []

    while True:
        while root != None:
            stack1.append(root)
            stack1.append(root)
            root = root.left

        if len(stack1) == 0:
            return

        root = stack1.pop()

        if len(stack1) > 0 and stack1[-1] == root:
            root = root.right
        else:
            print(root.val, end=" ")
            root = None


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
    in_order(root)
    post_order(root)
