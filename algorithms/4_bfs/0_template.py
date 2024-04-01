from collections import deque


def bfs_by_queue(root):
    queue = deque([root])
    while len(queue):
        node = queue.popleft()
        for child in node.children:
            if OK(child):
                return FOUND(child)
            queue.append(child)

    return NOT_FOUND
