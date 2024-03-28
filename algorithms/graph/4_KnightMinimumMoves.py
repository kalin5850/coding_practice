from collections import deque


def get_knight_shortest_path(x: int, y: int) -> int:
    def get_neighbor(coord):
        delta_row = [1, 2, 2, 1, -1, -2, -2, -1]
        delta_col = [2, 1, -1, -2, -2, -1, 1, 2]
        row, col = coord
        result = []

        for i in range(len(delta_row)):
            neighbor_row = row + delta_row[i]
            neighbor_col = col + delta_col[i]
            result.append((neighbor_row, neighbor_col))

        return result

    def bfs(node):
        queue = deque([node])
        visited = set([node])
        count = 0

        while len(queue):
            n = len(queue)
            for _ in range(n):
                curr = queue.popleft()
                if curr == (x, y):
                    return count
                for neighbor in get_neighbor(curr):
                    if neighbor in visited:
                        continue
                    queue.append(neighbor)
                    visited.add(neighbor)
            count += 1

        return count

    return bfs((0, 0))


if __name__ == "__main__":
    x, y = 5, 5
    res = get_knight_shortest_path(x, y)
    print(res)
