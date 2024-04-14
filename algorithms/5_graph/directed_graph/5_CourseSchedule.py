"""
There are a total of n courses a student has to take, numbered from 0 to n-1. A course may have prerequisites. The "depends on" relationship is expressed as a pair of numbers. For example, [0, 1] means you need to take course 1 before taking course 0. Given n and the list of prerequisites, decide if it is possible to take all the courses.

Example 1:

Input: n = 2, prerequisites = [[0, 1]]

Output: true

Explanation: we can take 1 first and then 0.

Example 2:

Input: n = 2, prerequisites = [[0, 1], [1, 0]]

Output: false

Explanation: the two courses depend on each other, there is no way to take them
"""

from collections import deque
from typing import List, Dict


def is_valid_course_schedule(n: int, prerequisites: List[List[int]]) -> bool:

    def create_graph(n: int, prerequisites: List[List[int]]) -> Dict[str, List[str]]:
        graph = {node: [] for node in range(n)}
        for edge in prerequisites:
            for i in range(len(edge) - 1):
                j = i + 1
                graph[edge[i]].append(edge[j])
        return graph

    def find_degree(graph: Dict[str, List[str]]) -> Dict[str, int]:
        indegree = {node: 0 for node in graph}
        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] += 1
        return indegree

    def topo_sort(graph) -> bool:
        result = []
        queue = deque()
        indegree = find_degree(graph)
        for node in indegree:
            if indegree[node] == 0:
                queue.append(node)
        while len(queue):
            curr = queue.popleft()
            result.append(curr)
            for neighbor in graph[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return len(result) == n

    graph = create_graph(n, prerequisites)
    return topo_sort(graph)


if __name__ == "__main__":
    n = 2
    prerequisites = [[0, 1]]
    res = is_valid_course_schedule(n, prerequisites)
    print("true" if res else "false")
    n = 2
    prerequisites = [[0, 1], [1, 0]]
    res = is_valid_course_schedule(n, prerequisites)
    print("true" if res else "false")
