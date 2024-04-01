"""
Given a 2-dimensional matrix of values with 0 and 1, count the number of islands of 1. An island consists of all value 1 cells and is surrounded by either an edge or all 0 cells. A cell can only be adjacent to each other horizontally or vertically, not diagonally.
"""

from collections import deque
from typing import List

def count_number_of_islands(grid: List[List[int]]) -> int:
    num_rows, num_cols = len(grid), len(grid[0])
    count_island = 0
    
    def get_neighbors(coord):
        row, col = coord
        delta_row = [-1, 0, 1, 0]
        delta_col = [0, 1, 0, -1]
        
        for i in range(len(delta_row)):
            neighbor_row = row + delta_row[i]
            nieghbor_col = col + delta_col[i]
            if 0 <= neighbor_row < num_rows and 0 <= nieghbor_col < num_cols:
                yield neighbor_row, nieghbor_col
    
    def bfs(coord):
        queue = deque([coord])
        visited = set([coord])
        while len(queue):
            curr = queue.popleft()
            for neighbor in get_neighbors(curr):
                r, c = neighbor
                if neighbor not in visited and grid[r][c] == 1:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    grid[r][c] = 0
    
    for r in range(num_rows):
        for c in range(num_cols):
            if grid[r][c] == 1:
                bfs((r, c))
                count_island += 1

    return count_island

if __name__ == '__main__':
    # grid = [[int(x) for x in input().split()] for _ in range(int(input()))]
    grid1 = [[1, 1, 1, 0, 0, 0], [1, 1, 1, 1, 0, 0], [1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0]]
    grid2 = [[1, 0, 1], [0, 1, 0]]
    grid3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    grid4 = [[1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1]]
    res = count_number_of_islands(grid4)
    print(res)

