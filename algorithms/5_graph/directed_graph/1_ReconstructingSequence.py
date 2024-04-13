"""
A sequence s is a list of integers. Its subsequence is a new sequence that can be made up by deleting elements from s, without changing the order of integers.

We are given an original sequence and a list of subsequences seqs.

Determine whether original is the only sequence that can be reconstructed from seqs. Reconstruction means building the shortest sequence so that all sequences in seqs are subsequences of it.

Parameters

original: a list of integers of size n representing the original sequence.
seqs: a list of sequences of size m representing the sequences to be reconstructed.
Result

true or false, depending on whether the original sequence can be uniquely reconstructed.
Examples

Example 1:

Input: original: [1,2,3], seqs: [[1,2], [1,3]]

Output: false

Explanation:

[1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.

Example 2:

Input: original: [1,2,3], seqs: [[1,2]]

Output: false

Explanation:

There is only one subsequence, so the reconstructed original sequence can only be [1,2] which is missing 3.

Example 3:

Input: orginal: [1,2,3], seqs: [[1,2], [1,3], [2,3]]

Output: true

Explanation:

[1,2,3] is the only sequence that can be reconstructed from [1,2], [1,3], and [2,3].

Example 4:

Input: original: [4,1,5,2,6,3], seqs: [[5,2,6,3], [4,1,5,2]]

Output: true

Explanation:

[4,1,5,2,6,3] is the only sequence that can be reconstructed from [[5,2,6,3], [4,1,5,2]].

Constraints

1 <= n <= 10^4
1 <= m <= 10^4
1 <= len(seqs[i]) <= n
"""

from collections import deque
from typing import List


def sequence_reconstruction(original: List[int], seqs: List[List[int]]) -> bool:

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
            if len(queue) > 1:
                return False
            curr = queue.popleft()
            result.append(curr)
            for neighbor in graph[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return len(result) == len(original)

    def create_graph(original, seqs):
        graph = {node: [] for node in original}
        for edge in seqs:
            n = len(edge)
            for i in range(n - 1):
                j = i + 1
                if n > 1:
                    graph[edge[i]].append(edge[j])
        return graph

    graph = create_graph(original, seqs)
    return topo_sort(graph)


if __name__ == "__main__":
    original = [int(x) for x in input().split()]
    seqs = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = sequence_reconstruction(original, seqs)
    print("true" if res else "false")
