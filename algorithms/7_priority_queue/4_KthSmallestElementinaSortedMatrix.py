"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

Input:

matrix = [
  [ 1,  5,  9],
  [10, 11, 13],
  [12, 13, 15]
],
k = 8,

Output: 13
"""

import heapq
from typing import List


def kth_smallest(matrix: List[List[int]], k: int) -> int:
    min_heap = []
    count = 0
    for row in matrix:
        heapq.heappush(min_heap, (row[0], row, 0))

    while min_heap:
        value, row, idx = heapq.heappop(min_heap)
        if count + 1 == k:
            return value
        idx += 1
        count += 1
        if idx < len(row):
            heapq.heappush(min_heap, (row[idx], row, idx))

    return 0


if __name__ == "__main__":
    matrix = ([[1, 5, 9], [10, 11, 13], [12, 13, 15]],)
    k = 8
    res = kth_smallest(matrix, k)
    print(res)
