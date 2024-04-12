from collections import deque

"""
    graph = {
        a: [...],
        b: [...],
        c: [...]
    }
"""


def create_graph(tasks, requirements):
    graph = {node: [] for node in tasks}
    for edge in requirements:
        n = len(edge)
        if n > 1:
            for i in range(n - 1):
                j = i + 1
                graph[edge[i]].append(edge[j])

    return graph


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
    return result if len(graph) == len(result) else None
