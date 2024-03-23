"""
Given an (unweighted) connected graph, return the length of the shortest path between two nodes A and B, in terms of the number of edges.

Assume there always exists a path between nodes A and B.

Input:

    graph = [[1, 2], [0, 2, 3], [0, 1], [1]]
    A = 0
    B = 3

Output: 2
"""

from collections import deque
from typing import List


def shortest_path(graph: List[List[int]], a: int, b: int) -> int:

    def get_neighbors(idx):
        return graph[idx]

    def bfs(node: int, target: int) -> int:
        queue = deque([node])
        visited = set([node])
        min_level = 0

        while len(queue):
            n = len(queue)
            for _ in range(n):
                curr = queue.popleft()
                if curr == target:
                    return min_level
                for neighbor in get_neighbors(curr):
                    if neighbor in visited:
                        continue
                    queue.append(neighbor)
                    visited.add(neighbor)
            min_level += 1

        return min_level

    return bfs(a, b)


if __name__ == "__main__":
    # graph = [[int(x) for x in input().split()] for _ in range(int(input()))]
    # a = int(input())
    # b = int(input())
    graph = [[1, 2], [0, 2, 3], [0, 1], [1]]
    a = 0
    b = 3
    res = shortest_path(graph, a, b)
    print(res)
