class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lca_on_bst(bst: Node, p: int, q: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    if bst.val > p and bst.val > q:
        value = lca_on_bst(bst.left, p, q)
    elif bst.val < p and bst.val < q:
        value = lca_on_bst(bst.right, p, q)
    else:
        value = bst.val
    return value
