"""
Given k sorted lists of numbers, merge them into one sorted list.

Input: [[1, 3, 5], [2, 4, 6], [7, 10]]

Output: [1, 2, 3, 4, 5, 6, 7, 10]
"""

import heapq
from typing import List


def merge_k_sorted_lists(lists: List[List[int]]) -> List[int]:
    min_heap = []
    result = []
    for item in lists:
        heapq.heappush(min_heap, (item[0], item, 0))

    # super magic
    while min_heap:
        value, item, idx = heapq.heappop(min_heap)
        result.append(value)
        idx += 1
        if idx < len(item):
            heapq.heappush(min_heap, (item[idx], item, idx))

    return result


if __name__ == "__main__":
    lists = [[1, 3, 5], [2, 4, 6], [7, 10]]
    res = merge_k_sorted_lists(lists)
    print(" ".join(map(str, res)))
