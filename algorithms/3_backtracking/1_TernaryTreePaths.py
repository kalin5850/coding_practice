from typing import List


class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children


def traversal_tree_path(node: Node):

    def dfs1(node: Node, path, result) -> List[str]:
        if len(node.children) == 0:
            return result.append("->".join(path))

        for node in node.children:
            path.append(str(node.val))
            dfs1(node, path, result)
            path.pop()

        return result

    path = []
    path.append(str(node.val))

    return dfs1(node, path, [])


def traversal_dfs(node: Node):
    stack: Node = []
    stack.append(node)
    paths = []

    while stack:
        current = stack.pop()


def traversal_bfs(node: Node):
    queue: Node = []
    queue.append(node)
    result: int = []

    while queue:
        curr = queue.pop(0)
        result.append(curr.val)
        for child in curr.children:
            queue.append(child)

    print(result)


def build_tree(nodes):
    val = next(nodes)
    num = int(next(nodes))
    children = [build_tree(nodes) for _ in range(num)]
    return Node(val, children)


if __name__ == "__main__":
    # ternary tree 1
    tree = "1 3 2 1 5 0 3 0 4 0"
    root = build_tree(iter(tree.split(" ")))
    # traversal_bfs(root)
    print(traversal_tree_path(root))
