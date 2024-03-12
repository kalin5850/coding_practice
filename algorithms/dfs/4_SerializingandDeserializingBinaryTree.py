"""
Given a binary tree, write a serialize function that converts the tree into a string and a deserialize function that converts a string to a binary tree. You may serialize the tree into any string representation you want as long as it can be deseralized.
"""


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    result = ""

    def pre_order(node) -> str:
        nonlocal result

        if node == None:
            result += "x "
            return ""

        result += "%s " % (node.val,)
        pre_order(node.left)
        pre_order(node.right)

    pre_order(root)

    return result


def deserialize(s):
    def pre_order(node):
        value = next(node)
        if value == "x":
            return

        current_node = Node(value)
        current_node.left = pre_order(node)
        current_node.right = pre_order(node)

        return current_node

    return pre_order(iter(s.split(" ")))


def build_tree(nodes):
    val = next(nodes)
    if val == "x":
        return None
    curr = Node(val)
    curr.left = build_tree(nodes)
    curr.right = build_tree(nodes)

    return curr


def print_tree(root):
    if not root:
        yield "x"
        return
    yield str(root.val)
    yield from print_tree(root.left)
    yield from print_tree(root.right)


if __name__ == "__main__":
    # tree 1
    tree = "1 2 4 x 7 x x 5 x x 3 x 6 x x"
    root = build_tree(iter(tree.split(" ")))
    serrialize_tree = serialize(root)
    print(serrialize_tree)
    deserialize(iter(serrialize_tree.split(" ")))

    #  tree 2
    tree = "1 2 4 x 7 x x 5 x x 3 x 6 8 x x x"
    root = build_tree(iter(tree.split(" ")))
    serrialize_tree = serialize(root)
    print(serrialize_tree)
    deserialize(iter(serrialize_tree.split(" ")))

    # tree 3
    tree = "1 2 3 x x 4 x 6 x x 5 x x"
    root = build_tree(iter(tree.split(" ")))
    serrialize_tree = serialize(root)
    print(serrialize_tree)
    deserialize(iter(serrialize_tree.split(" ")))

    # tree 4
    tree = "1 2 3 x x 4 x 6 x x 5 x 7 x x"
    root = build_tree(iter(tree.split(" ")))
    serrialize_tree = serialize(root)
    print(serrialize_tree)
    deserialize(iter(serrialize_tree.split(" ")))

    # tree 5
    tree = "1 2 3 x x 4 x x 5 6 x 7 x x x"
    root = build_tree(iter(tree.split(" ")))
    serrialize_tree = serialize(root)
    print(serrialize_tree)
    deserialize(iter(serrialize_tree.split(" ")))

    #  tree 6
    tree = "1 2 3 7 x x x 4 x x 5 6 x x x"
    root = build_tree(iter(tree.split(" ")))
    serrialize_tree = serialize(root)
    print(serrialize_tree)
    deserialize(iter(serrialize_tree.split(" ")))
