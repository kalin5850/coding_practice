"""
This problem is similar to Task Scheduling. The primary difference is now we assign times to tasks and we ask for the minimum amount of time to complete all tasks. There will be an extra times array such that times[i] indicates the time required to complete task[i]. You have also invited all your friends to help complete your tasks so you can work on any amount of tasks at a given time. Remember that task a must be completed before completing task b (but the starting times don't need to be in order).

There is guaranteed to be a solution.

Examples

Example 1

Input:

tasks = ["a", "b", "c", "d"]
times = [1, 1, 2, 1]
requirements = [["a", "b"], ["c", "b"], ["b", "d"]]

Output: 4
"""

from collections import deque
from typing import List


def task_scheduling_2(
    tasks: List[str], times: List[int], requirements: List[List[str]]
) -> int:

    def create_graph(tasks, requirements):
        graph = {node: [] for node in tasks}
        for edge in requirements:
            n = len(edge)
            if n > 1:
                for i in range(n - 1):
                    j = i + 1
                    graph[edge[i]].append(edge[j])
        return graph

    def create_time_map(tasks, times):
        return {value: times[idx] for idx, value in enumerate(tasks)}

    def find_degree(graph):
        indegree = {node: 0 for node in graph}
        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] += 1
        return indegree

    def topo_sort(graph, time_map):
        mini_time = 0
        counter = {node: 0 for node in graph}
        queue = deque()
        indegree = find_degree(graph)
        for node in indegree:
            if indegree[node] == 0:
                queue.append(node)
                counter[node] = time_map[node]
                mini_time = max(mini_time, counter[node])
        while len(queue):
            curr = queue.popleft()
            for neighbor in graph[curr]:
                indegree[neighbor] -= 1
                counter[neighbor] = max(
                    counter[neighbor], counter[curr] + time_map[neighbor]
                )
                mini_time = max(mini_time, counter[neighbor])
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return mini_time

    time_map = create_time_map(tasks, times)
    graph = create_graph(tasks, requirements)
    if time_map and graph:
        return topo_sort(graph, time_map)

    return 0


if __name__ == "__main__":
    tasks = ["a", "b", "c", "d"]
    times = [1, 1, 2, 1]
    requirements = [["a", "b"], ["c", "b"], ["b", "d"]]
    res = task_scheduling_2(tasks, times, requirements)
    print(res)
    tasks = ["brad", "cad", "dag", "ethereum", "forget", "aggregate"]
    times = [20, 190, 2930, 2375, 123, 5623749]
    requirements = [
        ["forget", "ethereum"],
        ["ethereum", "dag"],
        ["dag", "cad"],
        ["cad", "brad"],
        ["brad", "aggregate"],
    ]
    res = task_scheduling_2(tasks, times, requirements)
    print(res)
    tasks = [
        "abbreviate",
        "bricks",
        "cardinals",
        "dextrous",
        "fibre",
        "green",
        "height",
    ]
    times = [1, 1, 1, 1, 1, 100, 1]
    requirements = [
        ["abbreviate", "bricks"],
        ["cardinals", "bricks"],
        ["dextrous", "bricks"],
        ["bricks", "fibre"],
        ["green", "fibre"],
    ]
    res = task_scheduling_2(tasks, times, requirements)
    print(res)
    tasks = []
    times = []
    requirements = []
    res = task_scheduling_2(tasks, times, requirements)
    print(res)
    tasks = ["aaaabc", "bbbbbabc", "cccccabc", "ddddddabc"]
    times = [1, 2, 3, 1]
    requirements = [
        ["aaaabc", "bbbbbabc"],
        ["aaaabc", "cccccabc"],
        ["bbbbbabc", "ddddddabc"],
        ["cccccabc", "ddddddabc"],
    ]
    res = task_scheduling_2(tasks, times, requirements)
    print(res)
