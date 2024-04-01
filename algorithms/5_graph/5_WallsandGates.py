"""
You are given an m by n grid of integers representing a map of a dungeon. In this map:

-1 represents a wall or an obstacle of some kind.
0 represents a gate out of the dungeon.
INF represents empty space.
For this question, let INF be 2^31 - 1 == 2147483647, which is the max value of the integer type in many programming languages.

Venturing into the dungeon is very dangerous, so you would like to know how close you are at each point in the dungeon to the closest exit. Given the map of the dungeon, return the same map, but for each empty space, that space is replaced by the number of steps it takes to reach the closest exit. If a space cannot reach the exit, that space remains INF.

Note that each step, you can move horizontally or vertically, but you cannot move pass a wall or an obstacle.

Input

dungeon_map: a matrix of integer representing the dungeon map.
Output

A matrix of integer representing the dungeon map with the addition of distance to an exit for each empty space.

Examples

Example 1:

Input:

dungeon_map = [
  [INF, -1, 0, INF],
  [INF, INF, INF, -1],
  [INF, -1, INF, -1],
  [0, -1, INF, INF],
]

Output: [ [3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4], ]

Explanation:

Constraints

1 <= n, m <= 500

"""

from collections import deque
from typing import List, Tuple

INF = 2147483647


def map_gate_distances(dungeon_map: List[List[int]]) -> List[List[int]]:
    # WRITE YOUR BRILLIANT CODE HERE
    queue: deque[tuple[int, ...]] = deque()
    visited: tuple[int, ...] = set()
    count = 1
    nums_row, nums_col = len(dungeon_map), len(dungeon_map[0])

    def get_neighbors(coord: Tuple[int, ...]) -> Tuple[int, ...]:
        delta_row = [1, 0, -1, 0]
        delta_col = [0, 1, 0, -1]
        row, col = coord

        for i in range(len(delta_row)):
            neighbor_row = row + delta_row[i]
            neighbor_col = col + delta_col[i]
            if 0 <= neighbor_row < nums_row and 0 <= neighbor_col < nums_col:
                yield neighbor_row, neighbor_col

    for i in range(nums_row):
        for j in range(nums_col):
            if dungeon_map[i][j] == 0:
                queue.append((i, j))
                visited.add((i, j))

    while len(queue):
        n = len(queue)
        for _ in range(n):
            curr = queue.popleft()
            for neighbor in get_neighbors(curr):
                row, col = neighbor
                if dungeon_map[row][col] in visited:
                    continue
                if dungeon_map[row][col] == INF:
                    dungeon_map[row][col] = count
                    queue.append((row, col))
                    visited.add((row, col))
        count += 1

    return dungeon_map


if __name__ == "__main__":
    # dungeon_map = [[int(x) for x in input().split()] for _ in range(int(input()))]
    dungeon_map = [
        [INF, -1, 0, INF],
        [INF, INF, INF, -1],
        [INF, -1, INF, -1],
        [0, -1, INF, INF],
    ]
    res = map_gate_distances(dungeon_map)
    for row in res:
        print(" ".join(map(str, row)))
