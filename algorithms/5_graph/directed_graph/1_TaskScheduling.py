"""
For this problem, given a list of tasks and a list of requirements, compute a sequence of tasks that can be performed, such that we complete every task once while satisfying all the requirements.

Each requirement will be in the form of a list [a, b], where task a needs to be completed first before task b can be completed,

There is guaranteed to be a solution.

Examples

Example 1

Input:

1tasks = ["a", "b", "c", "d"]
2requirements = [["a", "b"], ["c", "b"], ["b", "d"]]
Output: ["a", "c", "b", "d"]
"""

from collections import deque
from typing import List


def task_scheduling(tasks: List[str], requirements: List[List[str]]) -> List[str]:
    graph = {node: [] for node in tasks}

    def find_degree(graph):
        indegree = {node: 0 for node in graph}
        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] += 1

        return indegree

    def topo_sort(graph):
        result = []
        queue = deque()
        indegree = find_degree(graph)
        for node, value in indegree.items():
            if value == 0:
                queue.append(node)
        while len(queue):
            curr = queue.popleft()
            result.append(curr)
            for neighbor in graph[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return result if len(result) == len(graph) else None

    for requirement in requirements:
        for idx in range(1, len(requirement)):
            graph[requirement[0]].append(requirement[idx])

    return topo_sort(graph)


if __name__ == "__main__":
    tasks = ["a", "b", "c", "d"]
    requirements = [["a", "b"], ["c", "b"], ["b", "d"]]
    res = task_scheduling(tasks, requirements)
    if len(res) != len(tasks):
        print(f"output size {len(res)} does not match input size {len(tasks)}")
        exit()
    indices = {task: i for i, task in enumerate(res)}
    for req in requirements:
        for task in req:
            if task not in indices:
                print(f"'{task}' is not in output")
                exit()
        a, b = req
        if indices[a] >= indices[b]:
            print(f"'{a}' is not before '{b}'")
            exit()
    print("ok")

    # tasks = ["brad", "cad", "dag", "ethereum", "forget", "aggregate"]
    # requirements = [
    #     ["forget", "ethereum"],
    #     ["ethereum", "dag"],
    #     ["dag", "cad"],
    #     ["cad", "brad"],
    #     ["brad", "aggregate"],
    # ]
    # tasks = [
    #     "abbreviate",
    #     "bricks",
    #     "cardinals",
    #     "dextrous",
    #     "fibre",
    #     "green",
    #     "height",
    # ]
    # requirements = [
    #     ["abbreviate", "bricks"],
    #     ["cardinals", "bricks"],
    #     ["dextrous", "bricks"],
    #     ["bricks", "fibre"],
    #     ["green", "fibre"],
    # ]
    # tasks, requirements = [], []
