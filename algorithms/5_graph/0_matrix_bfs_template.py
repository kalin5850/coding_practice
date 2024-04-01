from collections import deque

num_rows, num_cols = len(grid), len(grid[0])


def get_neighbors(coord):
    row, col = coord
    delta_row = [-1, 0, 1, 0]
    delta_col = [0, 1, 0, -1]
    result = []

    for i in range(len(delta_row)):
        neighbor_row = row + delta_row[i]
        neighbor_col = col + delta_col[i]
        if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < neighbor_col:
            result.append((neighbor_row, neighbor_col))

    return result


def bfs(start_node):
    queue = deque([start_node])
    visited = set([start_node])

    while len(queue):
        curr = queue.popleft()
        for neighbor in get_neighbors(curr):
            if neighbor in visited:
                continue

            # Do studd with the node if required
            # ...
            queue.append(neighbor)
            visited.add(neighbor)
