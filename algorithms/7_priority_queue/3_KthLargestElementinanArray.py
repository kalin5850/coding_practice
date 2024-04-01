"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not necessarily the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2

Output: 5

Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4

Output: 4

Note:

You may assume k is always valid, 1 ≤ k ≤ array's length.
"""

import heapq
from typing import List


def find_kth_largest(nums: List[int], k: int) -> int:
    max_heap = []
    result = 0
    for num in nums:
        heapq.heappush(max_heap, -num)
    for _ in range(k):
        result = heapq.heappop(max_heap)

    return -result
