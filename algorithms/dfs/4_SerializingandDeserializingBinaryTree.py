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
