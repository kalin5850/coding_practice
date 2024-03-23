from collections import deque


# Traverse each vertex
def bfs(root):
    queue = deque([root])
    visited = set([root])
    while queue:
        node = queue.popleft()
        for neighbor in get_neighbors(node):
            if neighbor in visited:
                continue
            queue.append(neighbor)
            visited.add(neighbor)


# Tracking levels/Finding distance
def bfs(root):
    queue = deque([root])
    visited = set([root])
    level = 0
    while queue:
        n = len(queue)
        for _ in range(n):
            node = queue.popleft()
            for neighbor in get_neighbors(node):
                if neighbor in visited:
                    continue
                queue.append(neighbor)
                visited.add(neighbor)
        level += 1


def dfs(root, visited):
    for neighbor in get_neighbors(root):
        if neighbor in visited:
            continue
        visited.add(neighbor)
        dfs(neighbor, visited)
